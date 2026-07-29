# Ghostline (`gq001`)

> **Status:** First canonical Ghostline story quest. This extends and replaces
> the `gq000` prototype.

V answers Patch's offer, meets him at the bridge, extracts the Quiet Spine
cache from a Tyger Claw relay, and brings it to Iris before completing the
physical handoff. The added Iris scene turns the original prototype into the
canonical first episode and establishes the cache that drives Black Lantern.

## Documents

- [Runtime flow](flow.md)
- [Act I: cache extraction](acts/01-quiet-spine-cache.md)
- [Act II: Iris handoff](acts/02-iris-handoff.md)
- [Continuity](continuity.md)
- [Quest specification](implementation/quest.json)
- [Iris scene dialogue manifest](script/gq001_03_manifest.json)

The validated `gq000` phases and Patch scene remain reusable implementation
templates; their reuse does not create a separate prior story event.

## Build

Validate and compile the typed quest manifest:

```powershell
py -B .\tools\quest_compiler.py validate `
  .\quests\story\ghostline\gq001\implementation\quest.json
py -B .\tools\quest_compiler.py compile `
  .\quests\story\ghostline\gq001\implementation\quest.json `
  --out .\converted\quests\gq001\gq001.questphase.json
```

Regenerate the quest-owned content:

```powershell
py -B .\quests\story\ghostline\gq001\implementation\build.py
py -B .\tools\generate_dialogue_localization.py `
  --manifest .\quests\story\ghostline\gq001\script\gq001_03_manifest.json `
  --quest gq001 --dialogue gq001_03 --deserialize
py -B .\tools\generate_scene.py generate `
  --spec .\quests\story\ghostline\gq001\implementation\scenes\iris-meet.scene-spec.json --deserialize
py -B .\tools\generate_world.py generate `
  --spec .\quests\story\ghostline\gq001\implementation\world\iris-meet.world.json --deserialize
```

The 12 selected source WAVs live in `voice/source`. Preview their WEM
conversion with:

```powershell
.\tools\convert_wavs_to_wem.ps1 `
  -SourceDir .\quests\story\ghostline\gq001\voice\source `
  -DestinationDir .\source\archive\mod\gq001\localization\en-us\vo `
  -Manifest .\quests\story\ghostline\gq001\script\gq001_03_manifest.json `
  -NoCopy
```

Run the focused gate:

```powershell
py -B .\tools\generate_scene.py audit `
  --spec .\quests\story\ghostline\gq001\implementation\scenes\iris-meet.scene-spec.json
py -B .\tools\generate_scene.py validate `
  --file .\source\raw\mod\gq001\scenes\gq001_iris_meet.scene.json `
  --spec .\quests\story\ghostline\gq001\implementation\scenes\iris-meet.scene-spec.json
py -B .\tools\generate_world.py generate `
  --spec .\quests\story\ghostline\gq001\implementation\world\iris-meet.world.json --dry-run
py -B -m unittest tests.test_quest_compiler -v
```

The installable archive is a whole-mod build from `source/archive`; follow
[`docs/workflows/build-and-package.md`](../../../../docs/workflows/build-and-package.md)
for packing and loose
resource staging.
