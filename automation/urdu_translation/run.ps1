param(
    [switch]$Force
)

$ErrorActionPreference = 'Stop'
$automationRoot = $PSScriptRoot
$repoRoot = 'G:\dua-ruqyah'
$workspace = 'G:\dua-ruqyah\dua_main_ur_translation'
$statePath = Join-Path $automationRoot 'state.json'
$promptPath = Join-Path $automationRoot 'PROMPT.md'
$schemaPath = Join-Path $automationRoot 'result-schema.json'
$rateLimitScript = Join-Path $automationRoot 'get-rate-limits.ps1'
$codexResolver = Join-Path $automationRoot 'resolve-codex.ps1'
$lockPath = Join-Path $automationRoot 'run.lock'
$logsRoot = Join-Path $automationRoot 'logs'

. $codexResolver
$codexPath = Resolve-CodexExecutable

if (-not (Test-Path -LiteralPath $logsRoot)) {
    New-Item -ItemType Directory -Path $logsRoot | Out-Null
}

if (Test-Path -LiteralPath $lockPath) {
    $lockAge = (Get-Date) - (Get-Item -LiteralPath $lockPath).LastWriteTime
    if ($lockAge.TotalHours -lt 8) {
        exit 0
    }
    Remove-Item -LiteralPath $lockPath -Force
}

New-Item -ItemType File -Path $lockPath -ErrorAction Stop | Out-Null

try {
    $state = Get-Content -Raw -Encoding utf8 -LiteralPath $statePath | ConvertFrom-Json
    if (-not $state.enabled) {
        exit 0
    }

    $now = [DateTimeOffset]::Now
    if (-not $Force -and $state.next_run_at) {
        $due = [DateTimeOffset]::Parse($state.next_run_at)
        if ($due -gt $now) {
            exit 0
        }
    }

    # Read the real ChatGPT-backed Codex primary and secondary quota windows.
    # These correspond to the active account's rolling and longer-term limits;
    # windowDurationMins and resetsAt are authoritative, so no fixed reset time
    # is guessed here.
    $rateSnapshot = $null
    $quotaMode = 'unknown'
    $maxUsedPercent = $null
    $blockingResetEpoch = $null
    try {
        $rateJson = & powershell.exe -NoProfile -NonInteractive -ExecutionPolicy Bypass -File $rateLimitScript -AsJson
        $rateSnapshot = $rateJson | ConvertFrom-Json

        $buckets = @()
        if ($rateSnapshot.rateLimitsByLimitId) {
            foreach ($property in $rateSnapshot.rateLimitsByLimitId.psobject.Properties) {
                $buckets += $property.Value
            }
        }
        elseif ($rateSnapshot.rateLimits) {
            $buckets += $rateSnapshot.rateLimits
        }

        $safeBucketSummaries = @()
        foreach ($bucket in $buckets) {
            $safeBucketSummaries += [pscustomobject]@{
                limitId = $bucket.limitId
                planType = $bucket.planType
                rateLimitReachedType = $bucket.rateLimitReachedType
                primary = $bucket.primary
                secondary = $bucket.secondary
            }
        }
        $state.last_rate_limits = [pscustomobject]@{
            checkedAt = $now.ToString('o')
            ordinaryUsageAllowed = $rateSnapshot.ordinaryUsageAllowed
            limits = $safeBucketSummaries
            resetCreditsAvailable = if ($rateSnapshot.rateLimitResetCredits) { $rateSnapshot.rateLimitResetCredits.availableCount } else { $null }
        }

        $windows = @()
        foreach ($bucket in $buckets) {
            if ($bucket.primary) { $windows += $bucket.primary }
            if ($bucket.secondary) { $windows += $bucket.secondary }
        }
        $usedValues = @($windows | Where-Object { $null -ne $_.usedPercent } | ForEach-Object { [double]$_.usedPercent })
        if ($usedValues.Count -gt 0) {
            $maxUsedPercent = ($usedValues | Measure-Object -Maximum).Maximum
        }

        $accountBlocked = ($rateSnapshot.ordinaryUsageAllowed -eq $false) -or
            (@($buckets | Where-Object { $_.spendControlReached -or $null -ne $_.rateLimitReachedType }).Count -gt 0)
        $blockingWindows = @($windows | Where-Object {
            if ($null -eq $_.usedPercent) { return $false }
            $used = [double]$_.usedPercent
            $duration = if ($null -eq $_.windowDurationMins) { 0 } else { [int]$_.windowDurationMins }
            if ($duration -gt 0 -and $duration -le 360) { return $used -ge 80 }
            return $used -ge 92
        })
        if ($accountBlocked -and $blockingWindows.Count -eq 0) {
            $blockingWindows = @($windows)
        }
        if ($blockingWindows.Count -gt 0) {
            $resetValues = @($blockingWindows | Where-Object { $null -ne $_.resetsAt } | ForEach-Object { [int64]$_.resetsAt })
            if ($resetValues.Count -gt 0) {
                $blockingResetEpoch = ($resetValues | Measure-Object -Maximum).Maximum
            }
            $quotaMode = 'wait_for_reset'
        }
        elseif (@($windows | Where-Object {
            if ($null -eq $_.usedPercent) { return $false }
            $used = [double]$_.usedPercent
            $duration = if ($null -eq $_.windowDurationMins) { 0 } else { [int]$_.windowDurationMins }
            if ($duration -gt 0 -and $duration -le 360) { return $used -ge 60 }
            return $used -ge 75
        }).Count -gt 0) {
            $quotaMode = 'conserve'
        }
        else {
            $quotaMode = 'normal'
        }
        $state.quota_mode = $quotaMode
    }
    catch {
        $state.quota_mode = 'unknown'
        $state.last_summary = "Rate-limit preflight unavailable: $($_.Exception.Message)"
    }

    if ($quotaMode -eq 'wait_for_reset') {
        $resumeAt = $now.AddHours(2)
        if ($null -ne $blockingResetEpoch) {
            $resumeAt = [DateTimeOffset]::FromUnixTimeSeconds([int64]$blockingResetEpoch).AddMinutes(5)
        }
        $state.last_run_at = $now.ToString('o')
        $state.last_result = 'quota_wait'
        $state.next_run_at = $resumeAt.ToString('o')
        $state.last_summary = "A Codex usage window reached the automation safety threshold. Paused until its exact reset time."
        $state | ConvertTo-Json -Depth 12 | Set-Content -Encoding utf8 -LiteralPath $statePath
        exit 0
    }

    $stamp = $now.ToString('yyyyMMdd-HHmmss')
    $eventsPath = Join-Path $logsRoot "$stamp-events.jsonl"
    $resultPath = Join-Path $logsRoot "$stamp-result.json"

    $context = @"
AUTOMATION STATE
- Current local time: $($now.ToString('o'))
- Previous result: $($state.last_result)
- Previous action: $($state.last_action)
- Previous table: $($state.last_table)
- Previous measured total tokens: $($state.last_total_tokens)
- Previous token pressure: $($state.last_token_pressure)
- Live quota mode: $quotaMode
- Highest live primary/secondary usage: $maxUsedPercent percent
- Consecutive failures: $($state.consecutive_failures)
- Next-action hint: $($state.next_action_hint)

Inspect the actual workspace and review evidence before trusting this hint. A
previous chat was interrupted while inspecting chunks 011 onward, so partial
inspection is not review evidence and must not be treated as completion.
"@

    if ($quotaMode -eq 'conserve') {
        $context += @"

QUOTA CONSERVATION RULE
The account is in conservation mode for at least one live usage window. Process no more
than two review chunks or one new-translation chunk in this run, keep tool
output compact, and recommend at least a 4-hour delay afterward.
"@
    }

    $template = Get-Content -Raw -Encoding utf8 -LiteralPath $promptPath
    $prompt = $template.Replace('{{AUTOMATION_CONTEXT}}', $context)

    $arguments = @(
        'exec',
        '-C', $repoRoot,
        '--approve-for-me',
        '--skip-git-repo-check',
        '--output-schema', $schemaPath,
        '--json',
        '--output-last-message', $resultPath,
        '-'
    )

    $savedErrorActionPreference = $ErrorActionPreference
    $ErrorActionPreference = 'Continue'
    $events = $prompt | & $codexPath @arguments 2>&1
    $exitCode = $LASTEXITCODE
    $ErrorActionPreference = $savedErrorActionPreference
    $events | Set-Content -Encoding utf8 -LiteralPath $eventsPath
    $eventText = $events -join "`n"

    function Get-LastNumericJsonValue {
        param([string]$Text, [string]$Name)
        $pattern = '"' + [regex]::Escape($Name) + '"\s*:\s*(\d+)'
        $matches = [regex]::Matches($Text, $pattern)
        if ($matches.Count -eq 0) { return $null }
        return [int64]$matches[$matches.Count - 1].Groups[1].Value
    }

    $inputTokens = Get-LastNumericJsonValue -Text $eventText -Name 'input_tokens'
    $outputTokens = Get-LastNumericJsonValue -Text $eventText -Name 'output_tokens'
    $totalTokens = $null
    if ($null -ne $inputTokens -or $null -ne $outputTokens) {
        $inputValue = if ($null -eq $inputTokens) { 0 } else { $inputTokens }
        $outputValue = if ($null -eq $outputTokens) { 0 } else { $outputTokens }
        $totalTokens = [int64]($inputValue + $outputValue)
    }

    $result = $null
    if (Test-Path -LiteralPath $resultPath) {
        try {
            $result = Get-Content -Raw -Encoding utf8 -LiteralPath $resultPath | ConvertFrom-Json
        }
        catch {
            $result = $null
        }
    }

    $success = $exitCode -eq 0 -and $null -ne $result -and
        ($result.result -in @('completed', 'skipped', 'all_done')) -and
        ($result.result -ne 'completed' -or $result.verification_passed)

    $state.last_run_at = $now.ToString('o')
    $state.last_log = $eventsPath
    $state.last_input_tokens = $inputTokens
    $state.last_output_tokens = $outputTokens
    $state.last_total_tokens = $totalTokens

    if ($success) {
        $state.last_result = $result.result
        $state.last_action = $result.action
        $state.last_table = $result.table
        $state.last_files_processed = @($result.files_processed)
        $state.last_token_pressure = $result.token_pressure
        $state.next_action_hint = $result.next_action
        $state.last_summary = $result.summary
        $state.consecutive_failures = 0

        if ($result.result -eq 'all_done') {
            $state.enabled = $false
            $state.next_run_at = $null
        }
        else {
            $delay = [int]$result.recommended_delay_hours
            if ($null -ne $totalTokens) {
                if ($totalTokens -ge 90000) {
                    $delay = [Math]::Max($delay, 4)
                }
                elseif ($totalTokens -ge 60000) {
                    $delay = [Math]::Max($delay, 3)
                }
                elseif ($totalTokens -ge 35000) {
                    $delay = [Math]::Max($delay, 2)
                }
            }
            elseif ($result.token_pressure -eq 'high') {
                $delay = [Math]::Max($delay, 4)
            }
            elseif ($result.token_pressure -eq 'medium') {
                $delay = [Math]::Max($delay, 2)
            }
            if ($quotaMode -eq 'conserve') {
                $delay = [Math]::Max($delay, 4)
            }
            $delay = [Math]::Min([Math]::Max($delay, 1), 8)
            $state.next_run_at = $now.AddHours($delay).ToString('o')
        }
    }
    else {
        $state.last_result = 'failed'
        $state.last_summary = "Codex automation failed with exit code $exitCode. See $eventsPath"
        $state.consecutive_failures = [int]$state.consecutive_failures + 1
        $backoffHours = [Math]::Min([Math]::Pow(2, $state.consecutive_failures), 8)
        $state.next_run_at = $now.AddHours($backoffHours).ToString('o')
    }

    $state | ConvertTo-Json -Depth 8 | Set-Content -Encoding utf8 -LiteralPath $statePath
}
finally {
    if (Test-Path -LiteralPath $lockPath) {
        Remove-Item -LiteralPath $lockPath -Force
    }
}
