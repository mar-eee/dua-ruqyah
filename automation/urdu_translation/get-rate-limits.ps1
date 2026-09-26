param(
    [switch]$AsJson
)

$ErrorActionPreference = 'Stop'
$process = $null
. (Join-Path $PSScriptRoot 'resolve-codex.ps1')

try {
    $codexPath = Resolve-CodexExecutable
    $startInfo = New-Object System.Diagnostics.ProcessStartInfo
    $startInfo.FileName = $codexPath
    $startInfo.Arguments = 'app-server --stdio'
    $startInfo.UseShellExecute = $false
    $startInfo.CreateNoWindow = $true
    $startInfo.RedirectStandardInput = $true
    $startInfo.RedirectStandardOutput = $true
    $startInfo.RedirectStandardError = $false

    $process = New-Object System.Diagnostics.Process
    $process.StartInfo = $startInfo
    if (-not $process.Start()) {
        throw 'Could not start Codex app-server.'
    }

    $initialize = @{
        method = 'initialize'
        id = 0
        params = @{
            clientInfo = @{
                name = 'dua_ruqyah_automation'
                title = 'Dua Ruqyah Urdu Automation'
                version = '1.0.0'
            }
        }
    } | ConvertTo-Json -Compress -Depth 8
    $initialized = @{ method = 'initialized'; params = @{} } | ConvertTo-Json -Compress -Depth 4
    $request = @{ method = 'account/rateLimits/read'; id = 6 } | ConvertTo-Json -Compress

    $process.StandardInput.WriteLine($initialize)
    $process.StandardInput.WriteLine($initialized)
    $process.StandardInput.WriteLine($request)
    $process.StandardInput.Flush()

    $deadline = (Get-Date).AddSeconds(25)
    $response = $null
    while ((Get-Date) -lt $deadline -and $null -eq $response) {
        $readTask = $process.StandardOutput.ReadLineAsync()
        $remaining = [int][Math]::Max(1, ($deadline - (Get-Date)).TotalMilliseconds)
        if (-not $readTask.Wait($remaining)) {
            break
        }
        $line = $readTask.Result
        if ($null -eq $line) {
            break
        }
        try {
            $message = $line | ConvertFrom-Json
            if ($message.id -eq 6) {
                if ($message.error) {
                    throw ($message.error | ConvertTo-Json -Compress -Depth 8)
                }
                $response = $message.result
            }
        }
        catch {
            if ($_.Exception.Message -like '*Could not convert*') {
                continue
            }
            throw
        }
    }

    if ($null -eq $response) {
        throw 'Codex app-server did not return rate limits before the timeout.'
    }

    if ($AsJson) {
        $response | ConvertTo-Json -Compress -Depth 12
    }
    else {
        $response
    }
}
finally {
    if ($null -ne $process -and -not $process.HasExited) {
        $process.Kill()
        $process.WaitForExit(5000) | Out-Null
    }
    if ($null -ne $process) {
        $process.Dispose()
    }
}
