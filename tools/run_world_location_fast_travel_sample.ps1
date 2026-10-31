param([string]$GameRoot = 'K:\Cyberpunk 2077')

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
$configPath = Join-Path $PSScriptRoot 'world-location-capture-fast-travel-v1.json'
$config = Get-Content -LiteralPath $configPath -Raw | ConvertFrom-Json
$outputRoot = if ([IO.Path]::IsPathRooted($config.output_root)) { $config.output_root } else { Join-Path $repoRoot $config.output_root }
$manifest = Get-Content -LiteralPath (Join-Path (Join-Path $outputRoot $config.reports) 'fast-travel-calibration-sample.json') -Raw | ConvertFrom-Json
$ids = @($manifest.views | ForEach-Object { $_.location_id })
if ($ids.Count -ne 16 -or @($ids | Select-Object -Unique).Count -ne 16) {
    throw 'Expected sixteen distinct fast-travel calibration views.'
}
Write-Host 'Fast travel calibration: eight locations, terminal and arrival-area views. Activate FreeFly and close CET overlay.'
& (Join-Path $PSScriptRoot 'run_world_location_overnight.ps1') -Config $configPath -GameRoot $GameRoot -Category fast_travel -Limit 16 -LocationId $ids
