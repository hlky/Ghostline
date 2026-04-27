[CmdletBinding()]
param(
    [string]$VoiceDir = 'source\archive\mod\gq000\localization\en-us\vo',
    [string]$WwiseProject = 'wwise_conversion\wwise_conversion.wproj',
    [string]$WwiseConsole = $(if ($env:WWISE_CONSOLE) { $env:WWISE_CONSOLE } else { 'C:\Audiokinetic\Wwise2025.1.7.9143\Authoring\x64\Release\bin\WwiseConsole.exe' }),
    [string]$OutputDir = 'converted',
    [string]$StagingDir = 'wwise_conversion\ExternalSources',
    [string]$SourceList = 'external_sources.wsources',
    [string]$Platform = 'Windows',
    [string]$Conversion = 'Vorbis Quality High',
    [switch]$SkipNormalize,
    [switch]$NoCopy
)

$ErrorActionPreference = 'Stop'

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path

function Resolve-RepoPath {
    param([Parameter(Mandatory)][string]$Path)

    if ([System.IO.Path]::IsPathRooted($Path)) {
        return [System.IO.Path]::GetFullPath($Path)
    }

    return [System.IO.Path]::GetFullPath((Join-Path $repoRoot $Path))
}

function Escape-Xml {
    param([Parameter(Mandatory)][string]$Value)
    return [System.Security.SecurityElement]::Escape($Value)
}

$voiceDirFull = Resolve-RepoPath $VoiceDir
$projectFull = Resolve-RepoPath $WwiseProject
$wwiseConsoleFull = Resolve-RepoPath $WwiseConsole
$outputDirFull = Resolve-RepoPath $OutputDir
$stagingDirFull = Resolve-RepoPath $StagingDir
$sourceListFull = Resolve-RepoPath $SourceList

if (-not (Test-Path -LiteralPath $wwiseConsoleFull -PathType Leaf)) {
    throw "WwiseConsole.exe not found: $wwiseConsoleFull"
}

if (-not (Test-Path -LiteralPath $projectFull -PathType Leaf)) {
    throw "Wwise project not found: $projectFull"
}

if (-not (Test-Path -LiteralPath $voiceDirFull -PathType Container)) {
    throw "Voice directory not found: $voiceDirFull"
}

$wavFiles = @(Get-ChildItem -LiteralPath $voiceDirFull -Filter '*.wav' -File | Sort-Object Name)
if ($wavFiles.Count -eq 0) {
    throw "No WAV files found in $voiceDirFull"
}

New-Item -ItemType Directory -Force -Path $outputDirFull | Out-Null

if ($SkipNormalize) {
    $sourceRoot = $voiceDirFull
    $sourceFiles = $wavFiles
} else {
    $ffmpeg = Get-Command ffmpeg -ErrorAction SilentlyContinue
    if (-not $ffmpeg) {
        throw 'ffmpeg is required unless -SkipNormalize is used.'
    }

    New-Item -ItemType Directory -Force -Path $stagingDirFull | Out-Null

    $sourceFiles = foreach ($wav in $wavFiles) {
        $normalizedPath = Join-Path $stagingDirFull $wav.Name
        & $ffmpeg.Source -y -hide_banner -loglevel error -i $wav.FullName -ar 48000 -ac 1 -af loudnorm -sample_fmt s16 $normalizedPath
        if ($LASTEXITCODE -ne 0) {
            throw "ffmpeg failed for $($wav.FullName)"
        }
        Get-Item -LiteralPath $normalizedPath
    }

    $sourceRoot = $stagingDirFull
}

$xmlLines = @(
    '<?xml version="1.0" encoding="UTF-8"?>',
    ('<ExternalSourcesList SchemaVersion="1" Root="{0}">' -f (Escape-Xml $sourceRoot))
)

foreach ($source in $sourceFiles) {
    $xmlLines += ('  <Source Path="{0}" Conversion="{1}"/>' -f (Escape-Xml $source.Name), (Escape-Xml $Conversion))
}

$xmlLines += '</ExternalSourcesList>'
$utf8NoBom = [System.Text.UTF8Encoding]::new($false)
[System.IO.File]::WriteAllText($sourceListFull, (($xmlLines -join [Environment]::NewLine) + [Environment]::NewLine), $utf8NoBom)

& $wwiseConsoleFull convert-external-source $projectFull --platform $Platform --source-file $sourceListFull --output $outputDirFull
if ($LASTEXITCODE -ne 0) {
    throw "Wwise external source conversion failed with exit code $LASTEXITCODE"
}

if ($NoCopy) {
    Write-Host "Converted $($wavFiles.Count) WAV file(s). WEM outputs are under $outputDirFull."
    exit 0
}

$copied = 0
$missing = @()

foreach ($wav in $wavFiles) {
    $wemName = [System.IO.Path]::ChangeExtension($wav.Name, '.wem')
    $converted = Get-ChildItem -LiteralPath $outputDirFull -Recurse -Filter $wemName -File | Sort-Object FullName | Select-Object -First 1

    if (-not $converted) {
        $missing += $wemName
        continue
    }

    Copy-Item -LiteralPath $converted.FullName -Destination (Join-Path $voiceDirFull $wemName) -Force
    $copied++
}

if ($missing.Count -gt 0) {
    throw "Missing converted WEM file(s): $($missing -join ', ')"
}

Write-Host "Converted and copied $copied WEM file(s) to $voiceDirFull."
Write-Host "Original WAV files were left in place."
