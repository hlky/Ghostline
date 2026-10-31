param(
    [string]$GameRoot = 'K:\Cyberpunk 2077',
    [switch]$Legacy,
    [ValidateSet('road', 'fast_travel', 'drop_point', 'vending_machine', 'parking_space', 'road_barrier', 'fake_door', 'fake_garage_door', 'intercom', 'access_point', 'terminal')]
    [string[]]$Categories = @('road', 'fast_travel', 'drop_point', 'vending_machine', 'parking_space', 'road_barrier', 'fake_door', 'fake_garage_door', 'intercom', 'access_point', 'terminal')
)

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
$python = Join-Path $repoRoot '.venv\Scripts\python.exe'
$surveyConfig = Join-Path $PSScriptRoot 'world-location-capture-survey-v2.json'
if (-not $Legacy -and -not (Test-Path -LiteralPath $surveyConfig)) {
    throw 'Survey workspace is not prepared. Run .venv\Scripts\python.exe tools/prepare_world_location_survey.py first, or select -Legacy.'
}
$batches = @(
    @{ Category = 'road'; Preset = 'world-location-capture-roads-v1.json' },
    @{ Category = 'fast_travel'; Preset = 'world-location-capture-fast-travel-v1.json' },
    @{ Category = 'drop_point'; Preset = 'world-location-capture-drop-points-v1.json' },
    @{ Category = 'vending_machine'; Preset = 'world-location-capture-vending-machines-v1.json' },
    @{ Category = 'parking_space'; Preset = 'world-location-capture-parking-areas-v1.json' },
    @{ Category = 'road_barrier'; Preset = 'world-location-capture-road-barriers-v1.json' },
    @{ Category = 'fake_garage_door'; Preset = 'world-location-capture-fake-garage-doors-v1.json' },
    @{ Category = 'intercom'; Preset = 'world-location-capture-intercoms-v1.json' },
    @{ Category = 'access_point'; Preset = 'world-location-capture-access-points-v1.json' },
    @{ Category = 'terminal'; Preset = 'world-location-capture-terminals-v1.json' },
    @{ Category = 'fake_door'; Preset = 'world-location-capture-fake-doors-v1.json' }
) | Where-Object { $_.Category -in $Categories }

# Let an already-running capture controller finish before taking over. The
# actual runners still acquire both OS locks, so this wait never bypasses them.
$waitCode = @'
import json,sys
from pathlib import Path
sys.path.insert(0,sys.argv[1])
from world_locations.protocol import exclusive_controller,ProtocolError
descriptor=json.loads(Path(sys.argv[2]).read_text())
try:
    with exclusive_controller(Path(descriptor['runtime_path'])/'controller.lock'): pass
except ProtocolError:
    sys.exit(2)
'@
$descriptor = Join-Path $repoRoot 'converted\world-location-database\category-runs\roads-v1\runtime\cet-runtime.json'
$announcedWait = $false
while ($true) {
    & $python -c $waitCode (Join-Path $repoRoot 'tools') $descriptor
    if ($LASTEXITCODE -eq 0) { break }
    if ($LASTEXITCODE -ne 2) { throw 'Unable to check the current capture controller.' }
    if (-not $announcedWait) { Write-Host 'Waiting for the current capture controller to finish...'; $announcedWait = $true }
    Start-Sleep -Seconds 5
}

if ($Legacy) {
    foreach ($batch in $batches) {
        $configPath = Join-Path $PSScriptRoot $batch.Preset
        Write-Host ("Starting/resuming category: " + $batch.Category)
        & (Join-Path $PSScriptRoot 'run_world_location_overnight.ps1') -GameRoot $GameRoot -Config $configPath -Category $batch.Category
    }
} else {
    Write-Host 'Starting/resuming geographic survey across the selected categories.'
    & (Join-Path $PSScriptRoot 'run_world_location_overnight.ps1') -GameRoot $GameRoot -Config $surveyConfig -Category $Categories
}
Write-Host ('Capture batch complete: ' + (($batches | ForEach-Object { $_.Category }) -join ', '))
