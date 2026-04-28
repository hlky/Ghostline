# Ghostline

Cyberpunk 2077 quest mod (WIP)

## Questphase Explorer

Use `tools/explore_questphase.py` to inspect deserialized questphase JSON without
dumping the whole CR2W-JSON file into context.

The default target is
`source/raw/mod/gq000/phases/gq000_patch_meet.questphase.json`:

```powershell
py .\tools\explore_questphase.py summary
py .\tools\explore_questphase.py nodes --sockets
py .\tools\explore_questphase.py edges
py .\tools\explore_questphase.py refs
py .\tools\explore_questphase.py handles --type TriggerCondition
py .\tools\explore_questphase.py search gq000_01_tr
py .\tools\explore_questphase.py node id:11
py .\tools\explore_questphase.py handle 13
py .\tools\explore_questphase.py dot > questphase.dot
```

Pass another raw questphase with `--file`:

```powershell
py .\tools\explore_questphase.py --file .\source\raw\mod\gq000\phases\other.questphase.json summary
```

Large lists are bounded by default. Use `--limit`, `--offset`, or `--limit 0`
on list commands when you need more rows.

## Scene Explorer

Use `tools/explore_scene.py` to inspect deserialized `.scene` CR2W-JSON.

The default target is `source/raw/mod/gq000/scenes/gq000_patch_meet.scene.json`:

```powershell
py .\tools\explore_scene.py summary
py .\tools\explore_scene.py actors
py .\tools\explore_scene.py nodes
py .\tools\explore_scene.py edges
py .\tools\explore_scene.py events
py .\tools\explore_scene.py lines
py .\tools\explore_scene.py choices
py .\tools\explore_scene.py refs --kind NodeRef
py .\tools\explore_scene.py handles --type TriggerCondition
py .\tools\explore_scene.py node 8
py .\tools\explore_scene.py handle 41
py .\tools\explore_scene.py search gq000_01_tr
py .\tools\explore_scene.py dot > scene.dot
```

Pass another raw scene with `--file`:

```powershell
py .\tools\explore_scene.py --file .\source\raw\mod\gq000\scenes\other.scene.json summary
```

## Localization Explorer

Use `tools/explore_localization.py` to inspect subtitle and VO-map CR2W-JSON.
By default it loads the current `gq000_01` subtitle and VO raw JSON files
together, then cross-checks entries by `stringId`.

```powershell
py .\tools\explore_localization.py summary
py .\tools\explore_localization.py entries
py .\tools\explore_localization.py check
py .\tools\explore_localization.py search Arasaka
py .\tools\explore_localization.py entry 6099223344158574223
py .\tools\explore_localization.py refs
py .\tools\explore_localization.py types
```

Pass one or more localization files with repeated `--file` arguments:

```powershell
py .\tools\explore_localization.py --file .\source\raw\mod\gq000\localization\en-us\subtitles\gq000_01.json.json --file .\source\raw\mod\gq000\localization\en-us\vo\gq000_01.json.json check
```

## Entity / Appearance Explorer

Use `tools/explore_ent_app.py` to inspect deserialized `.ent` and `.app`
CR2W-JSON. By default it loads Patch's root entity and app files together:

```powershell
py .\tools\explore_ent_app.py summary
py .\tools\explore_ent_app.py appearances
py .\tools\explore_ent_app.py components --resources-only
py .\tools\explore_ent_app.py components --type SkinnedMesh
py .\tools\explore_ent_app.py component c124
py .\tools\explore_ent_app.py refs --kind ResourcePath
py .\tools\explore_ent_app.py handles
py .\tools\explore_ent_app.py search patch
py .\tools\explore_ent_app.py types
```

Pass one or more raw entity/app files with repeated `--file` arguments:

```powershell
py .\tools\explore_ent_app.py --file .\source\raw\mod\ghostline\characters\patch\patch.ent.json --file .\source\raw\mod\ghostline\characters\patch\patch.app.json summary
```

## Journal Explorer

Use `tools/explore_journal.py` to inspect deserialized `.journal` CR2W-JSON.
By default it loads the mq003 quest journal reference from `reference/journal`:

```powershell
py .\tools\explore_journal.py summary
py .\tools\explore_journal.py prefixes --with-types
py .\tools\explore_journal.py -f .\source\raw\mod\gq000\journal\gq000.journal.json tree --max-depth 6
py .\tools\explore_journal.py -f .\source\raw\mod\gq000\journal\gq000.journal.json refs
```

Pass a different reference directory to the prefix command with
`--reference-dir`.

## World Reference Explorer

Use `tools/serialize_reference_world.ps1` to serialize CR2W binary world
references under `reference/world` into CR2W-JSON companions:

```powershell
.\tools\serialize_reference_world.ps1
```

Use `tools/explore_world.py` to inspect deserialized `.streamingblock` and
`.streamingsector` CR2W-JSON without dumping full world files:

```powershell
py .\tools\explore_world.py summary
py .\tools\explore_world.py blocks
py .\tools\explore_world.py nodes --type TriggerArea --limit 0
py .\tools\explore_world.py nodes --type AISpot --limit 0
py .\tools\explore_world.py noderefs --contains mq003_tr --limit 0
py .\tools\explore_world.py communities
py .\tools\explore_world.py search gq000
```

Pass one or more files or directories with repeated `--file` arguments:

```powershell
py .\tools\explore_world.py --file .\reference\world\001\sectors summary
```

## Voiceover WEM Conversion

Use `tools/convert_wavs_to_wem.ps1` to convert quest WAV voiceover files into
Wwise `.wem` files. The script normalizes WAVs into
`wwise_conversion\ExternalSources`, writes `external_sources.wsources`, runs
Wwise external source conversion, and copies the resulting WEM files back into
the VO folder without deleting the source WAVs.

```powershell
.\tools\convert_wavs_to_wem.ps1
```

By default it uses:

```powershell
C:\Audiokinetic\Wwise2025.1.7.9143\Authoring\x64\Release\bin\WwiseConsole.exe
```

Override that path with `-WwiseConsole` or the `WWISE_CONSOLE` environment
variable if Wwise is installed somewhere else.
