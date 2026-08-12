[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$InputFile,

    [Parameter(Mandatory = $true)]
    [string]$OutputFile,

    [string]$WolvenKitCore = ""
)

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent $PSScriptRoot
if (-not $WolvenKitCore) {
    $WolvenKitCore = Join-Path $repoRoot "WolvenKit\WolvenKit.CLI\bin\Release\net8.0\WolvenKit.Core.dll"
}

$resolvedInput = (Resolve-Path -LiteralPath $InputFile).Path
$resolvedCore = (Resolve-Path -LiteralPath $WolvenKitCore).Path
$resolvedOutput = [IO.Path]::GetFullPath($OutputFile)
$outputParent = Split-Path -Parent $resolvedOutput
if ($outputParent) {
    New-Item -ItemType Directory -Force -Path $outputParent | Out-Null
}

[Reflection.Assembly]::LoadFrom($resolvedCore) | Out-Null
[byte[]]$inputBytes = [IO.File]::ReadAllBytes($resolvedInput)
[byte[]]$oggBytes = $null
$converted = [WolvenKit.Core.Wwise.Wem]::TryConvert($inputBytes, [ref]$oggBytes)
if (-not $converted -or -not $oggBytes -or $oggBytes.Length -eq 0) {
    throw "WolvenKit failed to decode WEM: $resolvedInput"
}

[IO.File]::WriteAllBytes($resolvedOutput, $oggBytes)
Write-Output $resolvedOutput
