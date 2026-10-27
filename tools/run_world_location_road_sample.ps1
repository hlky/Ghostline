param(
    [string]$GameRoot = 'K:\Cyberpunk 2077'
)

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
$config = Get-Content -LiteralPath (Join-Path $PSScriptRoot 'world-location-capture-roads-v1.json') -Raw | ConvertFrom-Json
$outputRoot = if ([IO.Path]::IsPathRooted($config.output_root)) { $config.output_root } else { Join-Path $repoRoot $config.output_root }
$manifestPath = Join-Path (Join-Path $outputRoot $config.reports) 'road-calibration-sample.json'
$manifest = Get-Content -LiteralPath $manifestPath -Raw | ConvertFrom-Json
$ids = @($manifest.views | ForEach-Object { $_.location_id })
if ($ids.Count -ne 8 -or @($ids | Select-Object -Unique).Count -ne 8) {
    throw 'Expected eight distinct road calibration views. Run prepare-road-sample first.'
}
Write-Host 'Road calibration: four positions, two opposing views each. Activate FreeFly and close the CET overlay before capture.'
& (Join-Path $PSScriptRoot 'run_world_location_overnight.ps1') -GameRoot $GameRoot -Limit 8 -Category road -LocationId $ids
