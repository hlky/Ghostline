# Ghostline Agent Notes

## Project Shape

- This is a Cyberpunk 2077 WolvenKit project. The packed/game-ready resources live under `source/archive`.
- WolvenKit project resources live under `source/resources`; this includes ArchiveXL `.xl` files and TweakXL YAML files that are copied as loose resources when packing.
- `modding_docs` is a git submodule containing `CDPR-Modding-Documentation/Cyberpunk-Modding-Docs`. Treat it as local reference material, not Ghostline-owned source, unless the task explicitly asks to edit the docs.
- Files under `source/archive` are CR2W binaries, including paths ending in `.json` such as localization resources. Do not edit these as text.
- Files under `source/raw` are editable JSON forms of CR2W resources, except `source/raw/gq000_01_manifest.json`, which is a plain generated manifest and is not serialized back to CR2W.
- `GraphEditorStates` contains WolvenKit graph editor state JSON. Treat it as editor support data, not the packed asset source of truth.
- `generated` contains older/generated JSON snapshots. Prefer `source/raw` when preparing CR2W assets for use.

## Local Modding Docs

- Before guessing at Cyberpunk-specific behavior, check `modding_docs` locally.
- Useful starting points:
  - `modding_docs/SUMMARY.md` for the docs map.
  - `modding_docs/for-mod-creators-theory/modding-tools/wolvenkit.md` for WolvenKit context.
  - `modding_docs/for-mod-creators-theory/files-and-what-they-do/file-formats/quests-.scene-files` for quest and scene theory.
  - `modding_docs/modding-guides/quest` for quest and scene workflows.
  - `modding_docs/for-mod-creators-theory/files-and-what-they-do/file-formats/entity-.ent-files` and `appearance-.app-files` for character/entity resource structure.
  - `modding_docs/for-mod-creators-theory/files-and-what-they-do/audio-files.md` for voiceover and subtitle mapping.
  - `modding_docs/for-mod-creators-theory/core-mods-explained/archivexl` for ArchiveXL `.xl` registration, resource patching, tags, resource links, dynamic appearances, and localization.
  - `modding_docs/for-mod-creators-theory/core-mods-explained/tweakxl` for TweakXL/YAML records.

## Archive Layout

- `source/archive/base` may contain supporting base game files. It currently contains custom NPC template files.
- `source/archive/mod` contains all mod-owned packed resources.
- `source/archive/mod/ghostline` is for generic Ghostline files shared across the quest series, such as characters.
- `source/archive/mod/ghostline/characters` contains Ghostline character resources.
- `source/archive/mod/ghostline/characters/patch` contains the first custom character, Patch. The root `.ent` entity points to `.app` appearance file(s). Files under `body/` and `head/` are also part of the custom NPC template file set.
- `source/archive/mod/ghostline/localization/en-us/onscreens/ghostline.json` contains generic Ghostline onscreen localization, including Patch's display name and the Ghostline faction name.
- `source/archive/mod/gq000` contains the first Ghostline quest. `gq` means Ghostline quest, and `000` identifies the first quest.
- `source/archive/mod/gq000/localization/en-us` contains quest subtitles and voiceover maps. Add quest-specific onscreens there when journal/objective/UI text needs it, then register them in `source/resources/Ghostline.archive.xl`.
- `source/archive/mod/gq000/phases` contains questphase resources. `gq000.questphase` is the main questphase for the `gq000` quest, and `gq000_patch_meet.questphase` is the first stage where the player meets the quest giver.
- `source/archive/mod/gq000/scenes` contains scene resources used for dialogue, interactions, animations, and related scene work. `gq000_patch_meet.scene` is part of `gq000_patch_meet.questphase`.

## Character Resources

- `.ent` files are top-level entity containers. For NPCs, the root `.ent` is the game entry point and lists appearances that resolve into `.app` files.
- `.app` files hold appearance definitions and per-appearance components. Components on the root `.ent` are shared across appearances; components in the `.app` are appearance-specific.
- For Patch, keep the root `.ent` and referenced `.app` appearance names in sync with the TweakDB `entityTemplatePath`/character record.

## Quest and Scene Notes

- `.questphase` resources are graph-style quest flow files. They can reference scenes and other resources through graph nodes, noderefs, sockets, and handlerefs. Use WolvenKit's graph editor for structural inspection.
- Quest facts are signed integer state values. They default to `0` until explicitly set and are commonly read or written by `.questphase`, `.quest`, and `.scene` resources. Prefer `gq000_` prefixes for Ghostline quest facts.
- For custom scenes built from scratch, include `performerDebugSymbols` in the scene `debugSymbols` array. Actor debug symbols are calculated as `actorID * 256 + 1`; prop debug symbols as `propID * 256 + 2`.
- In scene sections, actors are referenced by `performerID`; in `screenplayStore -> lines`, dialogue lines are linked by `actorID`.
- Scene `locstringIds`, subtitle entries, and voiceover map entries must stay aligned. The subtitle String ID is the stable link between on-screen text and the voiceover resource.

## Tweak Resources

- `source/resources/r6/tweaks` is also part of the mod.
- `source/resources/r6/tweaks/ghostline/character_patch.yaml` defines the custom NPC.
- `source/resources/r6/tweaks/ghostline/faction_ghostline.yaml` defines the custom Ghostline faction.
- TweakXL loads `.yaml` or `.tweak` files from Cyberpunk's `r6/tweaks`; in this WolvenKit project, author them under `source/resources/r6/tweaks`.
- Tweak YAML is indentation-sensitive. Use 2 spaces, not tabs.
- Tweak record names must be unique. Do not base Ghostline records on generated `inlineX` records, because those names can shift between game updates.
- When editing NPC tweak records, prefer copying structure from a working base-game example in WolvenKit's Tweak Browser. Important NPC fields include `entityTemplatePath`, `displayName`, `fullDisplayName`, `voiceTag`, `baseAttitudeGroup`, `archetypeData`, and `affiliation`.

## ArchiveXL Resources

- `source/resources/Ghostline.archive.xl` is the ArchiveXL registration file. Keep it in `source/resources`; WolvenKit packs it next to the mod archive so ArchiveXL can process it.
- Use `quest: phases:` entries to attach Ghostline root questphases to the game, usually with `mod\gq000\phases\gq000.questphase` parented to `base\quest\cyberpunk2077.quest`. Add a Phantom Liberty standalone parent only when the quest is intended to initialize from PL standalone starts.
- Use `localization: onscreens:` entries to register custom onscreen translation JSON files. Tweak fields like `displayName`, `fullDisplayName`, and faction `localizedName` should have matching globally unique `secondaryKey` entries, with `primaryKey` left as `0` for ArchiveXL-generated keys.
- Use `journal:` entries when adding custom journal resources, and `streaming: blocks:` when adding world streaming blocks.
- Use `resource: patch:` for ArchiveXL resource patching instead of directly overwriting shared `.ent`, `.app`, or `.mesh` files when adding small changes to existing resources.
- Use `resource: link:` when multiple depot paths should resolve to the same resource, especially to avoid duplicate meshes for dynamic substitutions.
- Custom ArchiveXL tags live under `overrides: tags:` in `.xl` files, not in TweakXL YAML. Tags are case-sensitive and component names should be unique.
- Check `Cyberpunk 2077\red4ext\plugins\ArchiveXL\ArchiveXL.log` when `.xl` registrations, localization, journals, streaming, or resource patches do not appear in game.

## Generator

- Run `python .\create_files.py` from the repo root to generate the `gq000_01` conversation resources from `template.scene.json`.
- The generator writes subtitles, VO map data, scene dialogue/options, section/choice node ids, and `source/raw/gq000_01_manifest.json`.
- The generator expects WAV files in `source/archive/mod/gq000/localization/en-us/vo`. If a WAV named after a line key exists, it renames it to the hashed actor filename.
- `create_files.py` uses random dialogue gaps when building section timing, so reruns can change generated scene timing even with the same dialogue.
- The generator writes CR2W-JSON files, not game-ready CR2W binaries. Convert them before use.

## Voice Generation

- `voice_generate.py` is the voice design and voice clone process.
- For the Player Character ("V"), use voice clone only.
- For custom characters, design a voice first, then clone it for repeated usage.
- Cyberpunk stores voiceovers as Wwise `.wem` resources in archives; voiceover `.json` resources map subtitle String IDs to voice files. Ghostline's generator starts from WAV inputs, then prepares the CR2W-JSON resources that must be converted before use.

## Packing and Load Order

- Cyberpunk loads legacy `.archive` mods from `Cyberpunk 2077/archive/pc/mod` in ASCII-alphabetical order by archive filename.
- REDmods under `Cyberpunk 2077/mods` load after legacy archive mods and also use ASCII ordering by mod folder unless REDmod load order is explicitly supplied.
- File conflicts are handled per resource path, and the first mod to change a file wins. Ghostline should avoid conflicts by using mod-owned paths unless intentionally overriding a base or dependency resource.

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
& $wk convert serialize .\source\archive\mod\ghostline\localization\en-us\onscreens\ghostline.json -o .\source\raw\mod\ghostline\localization\en-us\onscreens -v Minimal
& $wk convert serialize .\source\archive\mod\gq000\phases\gq000_patch_meet.questphase -o .\source\raw\mod\gq000\phases -v Minimal
& $wk convert serialize .\source\archive\mod\gq000\scenes\gq000_patch_meet.scene -o .\source\raw\mod\gq000\scenes -v Minimal
```

The expected raw outputs are:

- `source/raw/mod/gq000/localization/en-us/subtitles/gq000_01.json.json`
- `source/raw/mod/gq000/localization/en-us/vo/gq000_01.json.json`
- `source/raw/mod/ghostline/localization/en-us/onscreens/ghostline.json.json`
- `source/raw/mod/gq000/phases/gq000_patch_meet.questphase.json`
- `source/raw/mod/gq000/scenes/gq000_patch_meet.scene.json`

## Raw JSON to CR2W

Use this before packing or testing the asset in game.

```powershell
& $wk convert deserialize .\source\raw\mod\gq000\localization\en-us\subtitles\gq000_01.json.json -o .\source\archive\mod\gq000\localization\en-us\subtitles -v Minimal
& $wk convert deserialize .\source\raw\mod\gq000\localization\en-us\vo\gq000_01.json.json -o .\source\archive\mod\gq000\localization\en-us\vo -v Minimal
& $wk convert deserialize .\source\raw\mod\ghostline\localization\en-us\onscreens\ghostline.json.json -o .\source\archive\mod\ghostline\localization\en-us\onscreens -v Minimal
& $wk convert deserialize .\source\raw\mod\gq000\phases\gq000_patch_meet.questphase.json -o .\source\archive\mod\gq000\phases -v Minimal
& $wk convert deserialize .\source\raw\mod\gq000\scenes\gq000_patch_meet.scene.json -o .\source\archive\mod\gq000\scenes -v Minimal
```

WolvenKit may print `Oodle couldn't be loaded. Using Kraken.dll instead could cause errors.` during JSON to CR2W conversion. That warning appeared during testing, but the round-tripped `gq000_patch_meet.scene` binary matched the original SHA256 hash.

## Verification

- A CR2W binary starts with `CR2W`; verify with `Format-Hex -Count 4`.
- A raw CR2W-JSON file should begin with `{` and contain a `Header` and `Data` object.
- For exact round-trip checks, compare hashes with `Get-FileHash`.
- Keep `Header.ArchiveFileName` pointed at the intended `source/archive` target when editing raw JSON.
