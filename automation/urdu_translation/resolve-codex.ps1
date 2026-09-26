function Resolve-CodexExecutable {
    $command = Get-Command codex.exe -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($command -and (Test-Path -LiteralPath $command.Source)) {
        return $command.Source
    }

    $extensionRoots = @(
        (Join-Path $env:USERPROFILE '.vscode\extensions'),
        (Join-Path $env:USERPROFILE '.vscode-insiders\extensions')
    )

    $candidates = foreach ($extensionRoot in $extensionRoots) {
        if (-not (Test-Path -LiteralPath $extensionRoot)) {
            continue
        }

        Get-ChildItem -LiteralPath $extensionRoot -Directory -Filter 'openai.chatgpt-*-win32-x64' -ErrorAction SilentlyContinue |
            ForEach-Object {
                $candidate = Join-Path $_.FullName 'bin\windows-x86_64\codex.exe'
                if (Test-Path -LiteralPath $candidate) {
                    Get-Item -LiteralPath $candidate
                }
            }
    }

    $selected = $candidates | Sort-Object LastWriteTime -Descending | Select-Object -First 1
    if ($selected) {
        return $selected.FullName
    }

    throw 'Could not locate codex.exe in PATH or an installed OpenAI VS Code extension.'
}
