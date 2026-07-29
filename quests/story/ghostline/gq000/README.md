# Ghostline Quest Design

> **Status:** Superseded prototype and reusable runtime baseline. `gq001` extends and replaces this route as the first canonical Ghostline story quest.

## Story Spine

Ghostline has learned that the Tyger Claws are facilitating a quiet
data-laundering route for an Arasaka-adjacent broker. `gq000` is deliberately
small: meet Patch, reach the relay, breach it, recover the datacache, and
deliver it to an ordinary drop point.

The bridge meeting and its dialogue are implemented and runtime-confirmed. The
first cache site is implemented around a native hackable data relay with three
Tyger Claw guards. The delivery uses the live, map-labelled vanilla
`drop_point_009` machine in Kabuki, roughly 252.7 metres from the relay and
outside its cleanup radius.

## Documents

- [Runtime flow](flow.md)
- [Implementation runtime reference](implementation/runtime-flow.md)
- [Persistent state](implementation/state.md)
- [Archived conversations](script/readables.md)
- [Delivery messages](script/messages.md)

## Build

Regenerate the authored scene, world, dialogue localization, and generated
child phases:

```powershell
py -B .\tools\generate_scene.py audit `
  --spec .\quests\story\ghostline\gq000\implementation\scenes\patch-meet.scene-spec.json
py -B .\tools\generate_scene.py generate `
  --spec .\quests\story\ghostline\gq000\implementation\scenes\patch-meet.scene-spec.json --deserialize
py -B .\tools\generate_world.py generate `
  --spec .\quests\story\ghostline\gq000\implementation\world\patch-meet.world.json --deserialize
py -B .\tools\generate_dialogue_localization.py `
  --manifest .\quests\story\ghostline\gq000\script\gq000_01_manifest.json `
  --quest gq000 --dialogue gq000_01 --deserialize
py -B .\tools\generate_cache_phase.py
py -B .\tools\generate_delivery_phase.py
```

The 13 selected source WAVs live in `voice/source`. Preview their WEM
conversion with:

```powershell
.\tools\convert_wavs_to_wem.ps1 -NoCopy
```

The two phase generators write CR2W-JSON only. Deserialize their changed
outputs with the template-backed workflow in
[`agent/skills/ghostline-wolvenkit-cr2w/SKILL.md`](../../../../agent/skills/ghostline-wolvenkit-cr2w/SKILL.md).

Run the focused gate:

```powershell
py -B -m unittest tests.test_generate_scene tests.test_generate_world `
  tests.test_generate_cache_phase tests.test_generate_delivery_phase -v
```

The installable archive is a whole-mod build from `source/archive`, with loose
`source/resources` staged separately. Follow
[`docs/workflows/build-and-package.md`](../../../../docs/workflows/build-and-package.md);
do not pack this quest
directory.
