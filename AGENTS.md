# Ghostline Agent Notes

## Project Shape

- This is a Cyberpunk 2077 WolvenKit project. The packed/game-ready resources live under `source/archive`.
- Files under `source/archive` are CR2W binaries, including paths ending in `.json` such as localization resources. Do not edit these as text.
- Files under `source/raw` are editable JSON forms of CR2W resources, except `source/raw/gq000_01_manifest.json`, which is a plain generated manifest and is not serialized back to CR2W.
- `GraphEditorStates` contains WolvenKit graph editor state JSON. Treat it as editor support data, not the packed asset source of truth.
- `generated` contains older/generated JSON snapshots. Prefer `source/raw` when preparing CR2W assets for use.

## Archive Layout

- `source/archive/base` may contain supporting base game files. It currently contains custom NPC template files.
- `source/archive/mod` contains all mod-owned packed resources.
- `source/archive/mod/ghostline` is for generic Ghostline files shared across the quest series, such as characters.
- `source/archive/mod/ghostline/characters` contains Ghostline character resources.
- `source/archive/mod/ghostline/characters/patch` contains the first custom character, Patch. The root `.ent` entity points to `.app` appearance file(s). Files under `body/` and `head/` are also part of the custom NPC template file set.
- `source/archive/mod/gq000` contains the first Ghostline quest. `gq` means Ghostline quest, and `000` identifies the first quest.
- `source/archive/mod/gq000/localization/en-us` contains subtitles, onscreens, and voiceover maps.
- `source/archive/mod/gq000/phases` contains questphase resources. `gq000.questphase` is the main questphase for the `gq000` quest, and `gq000_patch_meet.questphase` is the first stage where the player meets the quest giver.
- `source/archive/mod/gq000/scenes` contains scene resources used for dialogue, interactions, animations, and related scene work. `gq000_patch_meet.scene` is part of `gq000_patch_meet.questphase`.

## Tweak Resources

- `resources/r6/tweaks` is also part of the mod.
- `resources/r6/tweaks/ghostline/character_patch.yaml` defines the custom NPC.
- `resources/r6/tweaks/ghostline/faction_ghostline.yaml` defines the custom Ghostline faction.

## Generator

- Run `python .\create_files.py` from the repo root to generate the `gq000_01` conversation resources from `template.scene.json`.
- The generator builds subtitles, VO map data, scene dialogue/options, section/choice node ids, and `source/raw/gq000_01_manifest.json`.
- The generator expects WAV files in `source/archive/mod/gq000/localization/en-us/vo`. If a WAV named after a line key exists, it renames it to the hashed actor filename.
- `create_files.py` uses random dialogue gaps when building section timing, so reruns can change generated scene timing even with the same dialogue.
- The generator writes CR2W-JSON files, not game-ready CR2W binaries. Convert them before use.

## Voice Generation

- `voice_generate.py` is the voice design and voice clone process.
- For the Player Character ("V"), use voice clone only.
- For custom characters, design a voice first, then clone it for repeated usage.

## WolvenKit CLI

Use the local console build:

```powershell
$wk = 'H:\WolvenKit.Console-8.17.4\WolvenKit.CLI.exe'
```

WolvenKit command naming is easy to invert:

- `convert serialize` means CR2W binary to JSON.
- `convert deserialize` means JSON to CR2W binary.

When converting more than one file, avoid a single flat output directory if assets share a basename. For example, subtitles and VO both output as `gq000_01.json.json`, so they must use separate output directories.

## CR2W to Raw JSON

Use this when a resource was changed in WolvenKit and the editable JSON needs to be refreshed.

```powershell
& $wk convert serialize .\source\archive\mod\gq000\localization\en-us\subtitles\gq000_01.json -o .\source\raw\mod\gq000\localization\en-us\subtitles -v Minimal
& $wk convert serialize .\source\archive\mod\gq000\localization\en-us\vo\gq000_01.json -o .\source\raw\mod\gq000\localization\en-us\vo -v Minimal
& $wk convert serialize .\source\archive\mod\gq000\phases\gq000_patch_meet.questphase -o .\source\raw\mod\gq000\phases -v Minimal
& $wk convert serialize .\source\archive\mod\gq000\scenes\gq000_patch_meet.scene -o .\source\raw\mod\gq000\scenes -v Minimal
```

The expected raw outputs are:

- `source/raw/mod/gq000/localization/en-us/subtitles/gq000_01.json.json`
- `source/raw/mod/gq000/localization/en-us/vo/gq000_01.json.json`
- `source/raw/mod/gq000/phases/gq000_patch_meet.questphase.json`
- `source/raw/mod/gq000/scenes/gq000_patch_meet.scene.json`

## Raw JSON to CR2W

Use this before packing or testing the asset in game.

```powershell
& $wk convert deserialize .\source\raw\mod\gq000\localization\en-us\subtitles\gq000_01.json.json -o .\source\archive\mod\gq000\localization\en-us\subtitles -v Minimal
& $wk convert deserialize .\source\raw\mod\gq000\localization\en-us\vo\gq000_01.json.json -o .\source\archive\mod\gq000\localization\en-us\vo -v Minimal
& $wk convert deserialize .\source\raw\mod\gq000\phases\gq000_patch_meet.questphase.json -o .\source\archive\mod\gq000\phases -v Minimal
& $wk convert deserialize .\source\raw\mod\gq000\scenes\gq000_patch_meet.scene.json -o .\source\archive\mod\gq000\scenes -v Minimal
```

WolvenKit may print `Oodle couldn't be loaded. Using Kraken.dll instead could cause errors.` during JSON to CR2W conversion. That warning appeared during testing, but the round-tripped `gq000_patch_meet.scene` binary matched the original SHA256 hash.

## Verification

- A CR2W binary starts with `CR2W`; verify with `Format-Hex -Count 4`.
- A raw CR2W-JSON file should begin with `{` and contain a `Header` and `Data` object.
- For exact round-trip checks, compare hashes with `Get-FileHash`.
- Keep `Header.ArchiveFileName` pointed at the intended `source/archive` target when editing raw JSON.
