param([Parameter(Mandatory)][string]$Work)
$ErrorActionPreference = 'Stop'
. (Join-Path $PSScriptRoot '../tools/wwise_publish.ps1')
$root = Join-Path $Work 'run'
$platform = Join-Path $root 'Windows'
$destination = Join-Path $Work 'destination'
New-Item -ItemType Directory -Force -Path $platform, $destination | Out-Null
[IO.File]::WriteAllText((Join-Path $platform 'a.wem'), 'new-a')
[IO.File]::WriteAllText((Join-Path $destination 'a.wem'), 'old-a')
[IO.File]::WriteAllText((Join-Path $destination 'b.wem'), 'old-b')
$failed = $false
try { Resolve-WemOutputs $root 'Windows' @('a.wem', 'b.wem') | Out-Null } catch { $failed = $true }
if (-not $failed) { throw 'Missing output was accepted.' }
if ([IO.File]::ReadAllText((Join-Path $destination 'a.wem')) -ne 'old-a') { throw 'Preflight changed destination.' }
[IO.File]::WriteAllText((Join-Path $platform 'b.wem'), 'new-b')
$duplicate = Join-Path $platform 'duplicate'
New-Item -ItemType Directory -Path $duplicate | Out-Null
[IO.File]::WriteAllText((Join-Path $duplicate 'a.wem'), 'duplicate')
$failed = $false
try { Resolve-WemOutputs $root 'Windows' @('a.wem', 'b.wem') | Out-Null } catch { $failed = $true }
if (-not $failed) { throw 'Duplicate output was accepted.' }
Remove-Item -LiteralPath (Join-Path $duplicate 'a.wem')
$sources = Resolve-WemOutputs $root 'Windows' @('a.wem', 'b.wem')
function Move-PublishedWem {
    param([string]$Source, [string]$Destination)
    if ([IO.Path]::GetFileName($Destination) -eq 'b.wem') { throw 'Injected late replacement failure' }
    Move-Item -LiteralPath $Source -Destination $Destination -Force
}
$failed = $false
try { Publish-WemSet $sources $destination } catch { $failed = $true }
if (-not $failed) { throw 'Injected failure did not fail publication.' }
foreach ($name in @('a', 'b')) {
    if ([IO.File]::ReadAllText((Join-Path $destination "$name.wem")) -ne "old-$name") { throw "Rollback failed for $name" }
}
. (Join-Path $PSScriptRoot '../tools/wwise_publish.ps1')
Publish-WemSet $sources $destination
foreach ($name in @('a', 'b')) {
    if ([IO.File]::ReadAllText((Join-Path $destination "$name.wem")) -ne "new-$name") { throw "Publication failed for $name" }
}
Write-Output 'PASS: missing/duplicate preflight, late-failure rollback, complete publication'
