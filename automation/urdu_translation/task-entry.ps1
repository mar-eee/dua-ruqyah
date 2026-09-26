$ErrorActionPreference = 'Continue'

$automationRoot = $PSScriptRoot
$runner = Join-Path $automationRoot 'run.ps1'
$taskLog = Join-Path $automationRoot 'task-entry.log'
$powerShell = (Get-Command powershell.exe).Source
$startedAt = [DateTimeOffset]::Now.ToString('o')

Add-Content -Encoding utf8 -LiteralPath $taskLog -Value "[$startedAt] START user=$env:USERDOMAIN\$env:USERNAME runner=$runner"

& $powerShell -NoProfile -NonInteractive -ExecutionPolicy Bypass -File $runner *>> $taskLog
$runnerExitCode = $LASTEXITCODE

$finishedAt = [DateTimeOffset]::Now.ToString('o')
Add-Content -Encoding utf8 -LiteralPath $taskLog -Value "[$finishedAt] EXIT code=$runnerExitCode"
exit $runnerExitCode
