# The Machine Stops (`gq002`)

## Premise

Patch introduces V to **Cinder**, the field organizer for **Common Ground**:
a mutual-aid collective that removes predatory smart infrastructure from
tenements and replaces it with repairable, locally controlled hardware.
Common Ground is anti-dependency rather than blindly anti-technology. Cinder
uses implants when lives depend on them, but distrusts systems whose owners can
withdraw access remotely.

Cinder wants a Kabuki telecom relay taken offline. She believes a
property consortium uses it to profile tenants before clearing a block for
redevelopment. At the site, V discovers that the relay also carries a
neighborhood clinic's emergency telemetry. The consortium deliberately mixed
the two services so that resistance to its surveillance would appear to endanger
patients.

The player can destroy the relay as contracted or preserve the medical route
and falsify evidence of a shutdown. Neither outcome is perfectly clean.

## Documents

- [Runtime flow](flow.md)
- [Act summaries](acts/)
- [Dialogue and text](script/)
- [Continuity](continuity.md)
- [Quest specification](implementation/quest.json)

## Build

Validate and compile the typed quest:

```powershell
py -B .\tools\quest_compiler.py validate `
  .\quests\story\ghostline\gq002\implementation\quest.json
py -B .\tools\quest_compiler.py compile `
  .\quests\story\ghostline\gq002\implementation\quest.json `
  --out .\converted\quests\gq002\gq002.questphase.json
```

Regenerate the quest-owned content:

```powershell
py -B .\quests\story\ghostline\gq002\implementation\build.py --deserialize
py -B .\tools\generate_dialogue_localization.py `
  --manifest .\quests\story\ghostline\gq002\script\gq002_01_manifest.json `
  --quest gq002 --dialogue gq002_01 --deserialize
py -B .\tools\generate_scene.py generate `
  --spec .\quests\story\ghostline\gq002\implementation\scenes\cinder-meet.scene-spec.json --deserialize
py -B .\tools\generate_world.py generate `
  --spec .\quests\story\ghostline\gq002\implementation\world\machine-stops.world.json --deserialize
```

The 11 reviewed source WAVs live in `voice/source`. Preview their WEM
conversion with:

```powershell
.\tools\convert_wavs_to_wem.ps1 `
  -SourceDir .\quests\story\ghostline\gq002\voice\source `
  -DestinationDir .\source\archive\mod\gq002\localization\en-us\vo `
  -Manifest .\quests\story\ghostline\gq002\script\gq002_01_manifest.json `
  -NoCopy
```

Run the focused gate:

```powershell
py -B -m unittest tests.test_gq002_content tests.test_quest_compiler `
  tests.test_generate_scene tests.test_generate_world -v
```

The installable archive is a whole-mod build from `source/archive`; follow
[`docs/workflows/build-and-package.md`](../../../../docs/workflows/build-and-package.md)
for packing and loose
resource staging.
