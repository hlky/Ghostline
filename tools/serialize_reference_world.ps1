param(
    [string]$ReferenceRoot = "reference\world",
    [string]$WolvenKit = $env:WOLVENKIT_CLI
)

$ErrorActionPreference = "Stop"

if (-not $WolvenKit) {
    $WolvenKit = "H:\WolvenKit.Console-8.17.4\WolvenKit.CLI.exe"
}

if (-not (Test-Path -LiteralPath $WolvenKit)) {
    throw "WolvenKit CLI not found: $WolvenKit"
}

if (-not (Test-Path -LiteralPath $ReferenceRoot)) {
    throw "Reference world root not found: $ReferenceRoot"
}

$resources = Get-ChildItem -LiteralPath $ReferenceRoot -Recurse -File |
    Where-Object { $_.Name -match "\.(streamingsector|streamingblock)$" }

foreach ($resource in $resources) {
    & $WolvenKit convert serialize $resource.FullName -o $resource.DirectoryName -v Minimal
    if ($LASTEXITCODE -ne 0) {
        throw "WolvenKit serialization failed for $($resource.FullName)"
    }
}
