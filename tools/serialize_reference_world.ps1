param(
    [string]$ReferenceRoot = "reference\world",
    [string]$RedCli = "tools\ghostline-red\target\release\ghostline-red.exe",
    [string]$Schema = "red-schema.json"
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path -LiteralPath $RedCli)) {
    throw "ghostline-red release not found: $RedCli"
}

if (-not (Test-Path -LiteralPath $Schema)) {
    & $RedCli schema-generate ".\WolvenKit" $Schema
    if ($LASTEXITCODE -ne 0) {
        throw "ghostline-red schema generation failed"
    }
}

if (-not (Test-Path -LiteralPath $ReferenceRoot)) {
    throw "Reference world root not found: $ReferenceRoot"
}

$resources = Get-ChildItem -LiteralPath $ReferenceRoot -Recurse -File |
    Where-Object { $_.Name -match "\.(streamingsector|streamingblock)$" }

foreach ($resource in $resources) {
    $output = "$($resource.FullName).json"
    & $RedCli cr2w-serialize $resource.FullName $output --schema $Schema
    if ($LASTEXITCODE -ne 0) {
        throw "ghostline-red serialization failed for $($resource.FullName)"
    }
}
