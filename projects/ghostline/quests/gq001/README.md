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

The manifest's `composition` section owns the journal, onscreen text, contacts,
objectives, locations, and fact aliases. Stage references resolve from those
declarations before the shared compiler builds the graph.

Validate the manifest and generate a complete scratch build:

```powershell
py -B .\tools\quest_compiler.py validate `
  .\projects\ghostline\quests\gq001\implementation\quest.json
py -B .\projects\ghostline\quests\gq001\implementation\build.py `
  --out-root .\generated\quest-builds\gq001
```

This publishes eight resources together: the root, five child phases, journal,
and onscreen localization. Omit `--out-root` to update authored raw resources;
add `--deserialize` to convert and publish the corresponding CR2W binaries.
The shared build records its owned output paths for subsequent rebuilds.

Regenerate the separate dialogue, scene, and world resources:

```powershell
py -B .\tools\generate_dialogue_localization.py `
  --manifest .\projects\ghostline\quests\gq001\script\gq001_03_manifest.json `
  --quest gq001 --dialogue gq001_03 --deserialize
py -B .\tools\generate_scene.py generate `
  --spec .\projects\ghostline\quests\gq001\implementation\scenes\iris-meet.scene-spec.json --deserialize
py -B .\tools\generate_world.py generate `
  --spec .\projects\ghostline\quests\gq001\implementation\world\iris-meet.world.json --deserialize
```

The 12 selected source WAVs live in `voice/source`. Preview their WEM
conversion with:

```powershell
.\tools\convert_wavs_to_wem.ps1 `
  -SourceDir .\projects\ghostline\quests\gq001\voice\source `
  -DestinationDir .\projects\ghostline\source\archive\mod\gq001\localization\en-us\vo `
  -Manifest .\projects\ghostline\quests\gq001\script\gq001_03_manifest.json `
  -NoCopy
```

Run the focused gate:

```powershell
py -B .\tools\generate_scene.py audit `
  --spec .\projects\ghostline\quests\gq001\implementation\scenes\iris-meet.scene-spec.json
py -B .\tools\generate_scene.py validate `
  --file .\projects\ghostline\source\raw\mod\gq001\scenes\gq001_iris_meet.scene.json `
  --spec .\projects\ghostline\quests\gq001\implementation\scenes\iris-meet.scene-spec.json
py -B .\tools\generate_world.py generate `
  --spec .\projects\ghostline\quests\gq001\implementation\world\iris-meet.world.json --dry-run
py -B -m unittest tests.test_quest_compiler -v
```

## Lipsync

The Iris meeting has 12 authored clips (seven Iris lines and five V lines).
The reused Patch meeting has 13 (eight Patch lines and five V lines). Both
dialogue manifests explicitly select their `f_<locstring ID in hex>` clip for
both voice variants. These variants currently share the reviewed source audio.

Each meeting retains one shared lipsync resource slot. Its lipmap registers
both the NPC and V voice tags against the localized animset. Scene conversion
checks cooked data against authored data and falls back to WolvenKit if the
native writer loses a field, including the custom NPC voice tag. The offline
story lipsync tests check clip names, selectors, and mappings; WolvenKit exports
verify baked clip durations. Playback needs an in-game test.

Compile new facial clips with `--strip-donor-skeleton` so inherited donor body
animation cannot extend a clip beyond its source WAV duration. Check durations
after WolvenKit import, as well as in the generated GLB.

The installable story package combines this project's `source/archive` with
its declared shared runtime dependency. Build it from the repository root:

```powershell
uv run python -B tools/package_project.py --project ghostline --plan
uv run python -B tools/package_project.py --project ghostline --install
```

Follow
[`docs/workflows/build-and-package.md`](../../../../docs/workflows/build-and-package.md)
for packing and loose
resource staging.
