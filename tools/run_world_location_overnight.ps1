param(
    [string]$GameRoot = 'K:\Cyberpunk 2077',
    [ValidateRange(1, 2147483647)]
    [int]$Limit = 2147483647,
    [string[]]$Category = @(),
    [string[]]$LocationId = @(),
    [string]$Config = (Join-Path $PSScriptRoot 'world-location-capture-roads-v1.json')
)

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
$python = Join-Path $repoRoot '.venv\Scripts\python.exe'
if (-not (Test-Path -LiteralPath $python)) {
    throw "Repository Python environment missing: $python"
}
Push-Location $repoRoot
try {
    & $python -B tools/world_location_capture.py --config $Config preflight --game-root $GameRoot
    if ($LASTEXITCODE -ne 0) {
        throw 'Capture preflight failed. Resolve the reported blockers before starting.'
    }
    $captureConfig = Get-Content -LiteralPath $Config -Raw | ConvertFrom-Json
    $outputRoot = if ([IO.Path]::IsPathRooted($captureConfig.output_root)) { $captureConfig.output_root } else { Join-Path $repoRoot $captureConfig.output_root }
    $logRoot = Join-Path $outputRoot $captureConfig.reports
    New-Item -ItemType Directory -Path $logRoot -Force | Out-Null
    $logPath = Join-Path $logRoot ('overnight-' + (Get-Date -Format 'yyyyMMdd-HHmmss') + '.log')
    Write-Host "Capture log: $logPath"
    # Windows PowerShell can treat redirected native stderr progress as errors.
    # The native exit code, rather than progress output, determines failure.
    $ErrorActionPreference = 'Continue'
    try {
        $captureArguments = @('-B', 'tools/world_location_capture.py', '--config', $Config, 'capture', '--game-profile', 'capture-free-roam', '--limit', "$Limit")
        foreach ($selectedCategory in $Category) { $captureArguments += @('--category', $selectedCategory) }
        foreach ($selectedLocation in $LocationId) {
            $captureArguments += @('--location-id', $selectedLocation)
        }
        & $python @captureArguments 2>&1 |
            Tee-Object -FilePath $logPath
        $captureExitCode = $LASTEXITCODE
    }
    finally {
        $ErrorActionPreference = 'Stop'
    }
    if ($captureExitCode -ne 0) {
        throw "Capture stopped with an error. Inspect $logPath and verify CET restoration."
    }
}
finally {
    Pop-Location
}
