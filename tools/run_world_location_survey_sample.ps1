param([string]$GameRoot = 'K:\Cyberpunk 2077')

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
$configPath = Join-Path $PSScriptRoot 'world-location-capture-survey-v2.json'
$config = Get-Content -LiteralPath $configPath -Raw | ConvertFrom-Json
$outputRoot = if ([IO.Path]::IsPathRooted($config.output_root)) { $config.output_root } else { Join-Path $repoRoot $config.output_root }
$manifest = Get-Content -LiteralPath (Join-Path $outputRoot 'reports\survey-trial.json') -Raw | ConvertFrom-Json
$ids = @($manifest.views | ForEach-Object { $_.location_id })
if ($ids.Count -ne 10 -or @($ids | Select-Object -Unique).Count -ne 10) {
    throw 'Expected ten distinct survey trial views.'
}
Write-Host 'Survey trial: landing sweep, four raised parking views, vending-machine sweep. Activate FreeFly and close overlays.'
& (Join-Path $PSScriptRoot 'run_world_location_overnight.ps1') -Config $configPath -GameRoot $GameRoot -Limit 10 -LocationId $ids
