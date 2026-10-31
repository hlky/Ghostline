param(
    [string]$GameRoot = 'K:\Cyberpunk 2077',
    [switch]$RegisterCodex
)
$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
$environmentPath = Join-Path $repoRoot 'converted\game-scout\venv'
$scoutPython = Join-Path $environmentPath 'Scripts\python.exe'
if (-not (Test-Path -LiteralPath $scoutPython)) {
    & (Join-Path $repoRoot '.venv\Scripts\python.exe') -m venv $environmentPath
    if ($LASTEXITCODE -ne 0) { throw 'Scout environment creation failed.' }
}
& $scoutPython -m pip install -r (Join-Path $PSScriptRoot 'game_scout\requirements.txt')
if ($LASTEXITCODE -ne 0) { throw 'Scout dependency installation failed.' }
$entry = Join-Path $PSScriptRoot 'game_scout_mcp.py'
& $scoutPython $entry install --game-root $GameRoot
if ($LASTEXITCODE -ne 0) { throw 'Scout installation failed.' }
if ($RegisterCodex) {
    & codex mcp add game_scout -- $scoutPython $entry serve
    if ($LASTEXITCODE -ne 0) { throw 'Codex MCP registration failed.' }
}
Write-Host 'Game Scout is installed. Load its CET mod after the running capture finishes.'
