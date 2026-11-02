param(
    [string]$GameRoot = 'K:\Cyberpunk 2077',
    [switch]$RegisterCodex
)
$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
$environmentPath = Join-Path $repoRoot 'converted\cyberpunk-mcp\venv'
$gameplayPython = Join-Path $environmentPath 'Scripts\python.exe'
if (-not (Test-Path -LiteralPath $gameplayPython)) {
    & (Join-Path $repoRoot '.venv\Scripts\python.exe') -m venv $environmentPath
    if ($LASTEXITCODE -ne 0) { throw 'Cyberpunk MCP environment creation failed.' }
}
& $gameplayPython -m pip install -r (Join-Path $PSScriptRoot 'cyberpunk_mcp\requirements.txt')
if ($LASTEXITCODE -ne 0) { throw 'Cyberpunk MCP dependency installation failed.' }
$entry = Join-Path $PSScriptRoot 'cyberpunk_mcp.py'
& $gameplayPython $entry install --game-root $GameRoot
if ($LASTEXITCODE -ne 0) { throw 'Cyberpunk MCP installation failed.' }
if ($RegisterCodex) {
    & codex mcp add cyberpunk_mcp -- $gameplayPython $entry serve
    if ($LASTEXITCODE -ne 0) { throw 'Cyberpunk MCP registration failed.' }
}
Write-Host 'Cyberpunk MCP installed separately. Reload CET when idle, disable FreeFly, then run doctor.'
