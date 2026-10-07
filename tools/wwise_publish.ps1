# Wwise result validation and rollback-safe publication. Dot-source from conversion or tests.
function Resolve-WemOutputs {
    param([Parameter(Mandatory)][string]$OutputRoot,
          [Parameter(Mandatory)][string]$Platform,
          [Parameter(Mandatory)][string[]]$Names)

    $root = [IO.Path]::GetFullPath($OutputRoot)
    $platformRoot = Join-Path $root $Platform
    $hasPlatform = Test-Path -LiteralPath $platformRoot -PathType Container
    $searchRoot = if ($hasPlatform) { $platformRoot } else { $root }
    $results = [ordered]@{}
    foreach ($name in $Names) {
        if ([IO.Path]::GetFileName($name) -ne $name -or $results.Contains($name)) {
            throw "Duplicate or unsafe WEM output name: $name"
        }
        $matches = @(Get-ChildItem -LiteralPath $searchRoot -Recurse:$hasPlatform -File -Filter $name)
        if ($matches.Count -ne 1 -or $matches[0].Length -eq 0) {
            throw "Expected one nonempty converted WEM for $name under $searchRoot; found $($matches.Count)."
        }
        $results[$name] = $matches[0].FullName
    }
    return $results
}

function Move-PublishedWem {
    param([string]$Source, [string]$Destination)
    Move-Item -LiteralPath $Source -Destination $Destination -Force -ErrorAction Stop
}

function Publish-WemSet {
    param([Parameter(Mandatory)][System.Collections.IDictionary]$Sources,
          [Parameter(Mandatory)][string]$DestinationDir)

    $destination = [IO.Path]::GetFullPath($DestinationDir)
    if ($Sources.Count -eq 0) { throw 'No WEM outputs to publish.' }
    New-Item -ItemType Directory -Force -Path $destination | Out-Null
    $stage = [IO.Path]::GetFullPath((Join-Path $destination ('.wem-publish-' + [guid]::NewGuid().ToString('N'))))
    # All recursive cleanup stays inside this verified, newly allocated transaction directory.
    if (-not $stage.StartsWith($destination.TrimEnd('\', '/') + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)) {
        throw 'WEM staging path escaped destination.'
    }
    New-Item -ItemType Directory -Path $stage | Out-Null
    $backups = Join-Path $stage 'backups'
    New-Item -ItemType Directory -Path $backups | Out-Null
    $published = [Collections.Generic.List[string]]::new()
    $oldFiles = @{}
    $cleanup = $true
    try {
        foreach ($name in $Sources.Keys) {
            if ([IO.Path]::GetFileName([string]$name) -ne $name) { throw "Unsafe WEM name: $name" }
            $target = Join-Path $destination $name
            if ((Test-Path -LiteralPath $target) -and -not (Test-Path -LiteralPath $target -PathType Leaf)) {
                throw "WEM destination is not a file: $target"
            }
            $staged = Join-Path $stage $name
            Copy-Item -LiteralPath $Sources[$name] -Destination $staged -ErrorAction Stop
            if ((Get-FileHash -LiteralPath $Sources[$name]).Hash -ne (Get-FileHash -LiteralPath $staged).Hash) {
                throw "Staging changed WEM content: $name"
            }
            $oldFiles[$name] = Test-Path -LiteralPath $target -PathType Leaf
            if ($oldFiles[$name]) { Copy-Item -LiteralPath $target -Destination (Join-Path $backups $name) -ErrorAction Stop }
        }
        foreach ($name in $Sources.Keys) {
            # Record before replacement so a partially successful filesystem operation is rolled back too.
            $published.Add($name)
            Move-PublishedWem -Source (Join-Path $stage $name) -Destination (Join-Path $destination $name)
        }
    } catch {
        $failure = $_
        try {
            foreach ($name in $published) {
                $target = Join-Path $destination $name
                if ($oldFiles[$name]) {
                    Copy-Item -LiteralPath (Join-Path $backups $name) -Destination $target -Force -ErrorAction Stop
                } elseif (Test-Path -LiteralPath $target -PathType Leaf) {
                    Remove-Item -LiteralPath $target -ErrorAction Stop
                }
            }
        } catch {
            $cleanup = $false
            throw "WEM rollback failed; recovery files remain at ${stage}. Original error: $failure. Rollback error: $_"
        }
        throw $failure
    } finally {
        if ($cleanup) { Remove-Item -LiteralPath $stage -Recurse -Force -ErrorAction Stop }
    }
}
