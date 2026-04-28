---
name: ghostline-wolvenkit-cr2w
description: Use for Ghostline WolvenKit CLI work, especially serializing CR2W binaries to raw JSON, deserializing raw CR2W-JSON back to packed resources, keeping source/raw and source/archive synchronized, and verifying CR2W outputs.
---

# Ghostline WolvenKit CR2W Workflow

## CLI Setup

Use the local console build:

```powershell
$wk = 'H:\WolvenKit.Console-8.17.4\WolvenKit.CLI.exe'
```

WolvenKit command names are easy to invert:

- `convert serialize` means CR2W binary to JSON.
- `convert deserialize` means JSON to CR2W binary.

When converting more than one file, avoid a single flat output directory if
assets share a basename. Subtitles and VO both output as `gq000_01.json.json`,
so use separate output directories.

WolvenKit CLI serialization expects the `-o` output directory to exist for new
raw resource trees:

```powershell
New-Item -ItemType Directory -Force .\source\raw\mod\ghostline\characters\patch
```

## CR2W To Raw JSON

Use this when a resource was changed in WolvenKit and the editable JSON needs
to be refreshed.

```powershell
& $wk convert serialize .\source\archive\mod\gq000\localization\en-us\subtitles\gq000_01.json -o .\source\raw\mod\gq000\localization\en-us\subtitles -v Minimal
& $wk convert serialize .\source\archive\mod\gq000\localization\en-us\vo\gq000_01.json -o .\source\raw\mod\gq000\localization\en-us\vo -v Minimal
& $wk convert serialize .\source\archive\mod\ghostline\localization\en-us\onscreens\ghostline.json -o .\source\raw\mod\ghostline\localization\en-us\onscreens -v Minimal
& $wk convert serialize .\source\archive\mod\ghostline\characters\patch\patch.ent -o .\source\raw\mod\ghostline\characters\patch -v Minimal
& $wk convert serialize .\source\archive\mod\ghostline\characters\patch\patch.app -o .\source\raw\mod\ghostline\characters\patch -v Minimal
& $wk convert serialize .\source\archive\mod\gq000\phases\gq000.questphase -o .\source\raw\mod\gq000\phases -v Minimal
& $wk convert serialize .\source\archive\mod\gq000\phases\gq000_patch_meet.questphase -o .\source\raw\mod\gq000\phases -v Minimal
& $wk convert serialize .\source\archive\mod\gq000\scenes\gq000_patch_meet.scene -o .\source\raw\mod\gq000\scenes -v Minimal
```

Expected raw outputs:

- `source/raw/mod/gq000/localization/en-us/subtitles/gq000_01.json.json`
- `source/raw/mod/gq000/localization/en-us/vo/gq000_01.json.json`
- `source/raw/mod/ghostline/localization/en-us/onscreens/ghostline.json.json`
- `source/raw/mod/ghostline/characters/patch/patch.ent.json`
- `source/raw/mod/ghostline/characters/patch/patch.app.json`
- `source/raw/mod/gq000/phases/gq000.questphase.json`
- `source/raw/mod/gq000/phases/gq000_patch_meet.questphase.json`
- `source/raw/mod/gq000/scenes/gq000_patch_meet.scene.json`

## Raw JSON To CR2W

Use this before packing or testing the asset in game.

```powershell
& $wk convert deserialize .\source\raw\mod\gq000\localization\en-us\subtitles\gq000_01.json.json -o .\source\archive\mod\gq000\localization\en-us\subtitles -v Minimal
& $wk convert deserialize .\source\raw\mod\gq000\localization\en-us\vo\gq000_01.json.json -o .\source\archive\mod\gq000\localization\en-us\vo -v Minimal
& $wk convert deserialize .\source\raw\mod\ghostline\localization\en-us\onscreens\ghostline.json.json -o .\source\archive\mod\ghostline\localization\en-us\onscreens -v Minimal
& $wk convert deserialize .\source\raw\mod\ghostline\characters\patch\patch.ent.json -o .\source\archive\mod\ghostline\characters\patch -v Minimal
& $wk convert deserialize .\source\raw\mod\ghostline\characters\patch\patch.app.json -o .\source\archive\mod\ghostline\characters\patch -v Minimal
& $wk convert deserialize .\source\raw\mod\gq000\phases\gq000.questphase.json -o .\source\archive\mod\gq000\phases -v Minimal
& $wk convert deserialize .\source\raw\mod\gq000\phases\gq000_patch_meet.questphase.json -o .\source\archive\mod\gq000\phases -v Minimal
& $wk convert deserialize .\source\raw\mod\gq000\scenes\gq000_patch_meet.scene.json -o .\source\archive\mod\gq000\scenes -v Minimal
```

WolvenKit may print `Oodle couldn't be loaded. Using Kraken.dll instead could
cause errors.` during JSON to CR2W conversion. This warning appeared during
testing, but the round-tripped `gq000_patch_meet.scene` binary matched the
original SHA256 hash.

## Verification

- A CR2W binary starts with `CR2W`; verify with `Format-Hex -Count 4`.
- A raw CR2W-JSON file should begin with `{` and contain `Header` and `Data`.
- For exact round-trip checks, compare hashes with `Get-FileHash`.
- Keep `Header.ArchiveFileName` pointed at the intended `source/archive`
  target when editing raw JSON.
