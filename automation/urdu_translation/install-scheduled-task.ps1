$ErrorActionPreference = 'Stop'

$taskName = 'Dua Ruqyah Urdu Translation Automation'
$runner = Join-Path $PSScriptRoot 'task-entry.ps1'
$powerShell = (Get-Command powershell.exe).Source
$arguments = "-NoProfile -NonInteractive -ExecutionPolicy Bypass -File `"$runner`""

$action = New-ScheduledTaskAction -Execute $powerShell -Argument $arguments -WorkingDirectory $PSScriptRoot
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date).AddMinutes(2) -RepetitionInterval (New-TimeSpan -Minutes 5)
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable -MultipleInstances IgnoreNew
$settings.Hidden = $true
$principal = New-ScheduledTaskPrincipal -UserId "$env:USERDOMAIN\$env:USERNAME" -LogonType Interactive -RunLevel Limited

Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger -Settings $settings -Principal $principal -Description 'Adaptive natural-Urdu Dua and Ruqyah translation/review automation using the urdu-dua-ruqyah skill.' -Force | Out-Null

Get-ScheduledTask -TaskName $taskName | Select-Object TaskName, State, TaskPath
