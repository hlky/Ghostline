# World And NodeRef References

This document preserves the resolved world, prefab, marker, trigger, and
community findings that were moved out of `ROADMAP.md`.

## Reference Sets

`reference/world` contains two useful deserialized reference sets:

- `000` - mq003 quest-sector references.
- `001` - Object Spawner-style streaming block, exterior sector, and
  always-loaded community registry sector.

Key reference findings:

- mq003 quest sectors use streaming block descriptors with
  `questPrefabNodeRef` values under a prefab root alias.
- mq003 always-loaded sectors can register NodeRefs separately from concrete
  node definitions.
- Object Spawner-style examples contain a streamable community area in an
  exterior sector and a community registry in an always-loaded sector.
- Reference trigger areas use `worldTriggerAreaNode` with
  `AreaShapeOutline` height values and four-point outlines.

## Quest Prefab NodeRef Model

The current `#gq000_pr_patch_meet` references in `gq000.questphase` and
`gq000_patch_meet.questphase` are backed by a Ghostline-owned streaming block
and quest sector.

Resolved model:

- Questphase `#` NodeRefs can load prefabs for the phase.
- Streaming sectors register NodeRef aliases through sector `nodeRefs`.
- Concrete sector nodes link back to aliases through
  `nodeData.QuestPrefabRefHash`.
- A quest streaming block descriptor provides the world-side root binding with
  `questPrefabNodeRef`.
- `phasePrefabs` is the questphase-level prefab dependency/declaration list.
  Any questphase that directly uses `#gq000_pr_patch_meet` should list it.
- `phaseInstancePrefabs` is the per-`questPhaseNodeDefinition` activation list
  for inline phase nodes.
- In `gq000.questphase`, phase node id `2` directly waits on
  `#gq000_01_tr_setup` and operates on `#gq000_01_com_patch_bridge`, so it
  should keep `#gq000_pr_patch_meet` in `phaseInstancePrefabs`.
- Parent phase node id `3` only loads
  `mod\gq000\phases\gq000_patch_meet.questphase`; it does not need a duplicate
  `phaseInstancePrefabs` entry because the child questphase has its own root
  `phasePrefabs`.

Ghostline world binding:

- `gq000_patch_meet.streamingblock` binds
  `questPrefabNodeRef: $/mod/gq000/#gq000_pr_patch_meet`.
- `gq000_patch_meet.streamingsector` registers quest-sector child refs under
  that prefab root and assigns matching `nodeData.QuestPrefabRefHash` values:
  - `#gq000_01_sm_patch_bridge`
  - `#gq000_01_tr_setup`
  - `#gq000_01_tr_engage`
  - `#gq000_01_tr_bridge_case_mood`
  - `#gq000_01_tr_someone_coming`
  - `#gq000_01_spot_patch_bridge`
  - `#gq000_01_com_patch_bridge`
- `gq000_always_loaded.streamingsector` registers concrete always-loaded marker
  nodes for `#gq000_01_sm_patch_bridge` and `#gq000_01_mp_patch_bridge`.
- Vanilla mq003 nests the scene marker under a scene prefab child path while
  keeping the map-pin marker directly under the quest prefab root. Current
  Ghostline source still registers `#gq000_01_sm_patch_bridge` directly under
  `#gq000_pr_patch_meet`; fresh world/scene tooling should correct that.

## Current World Resources

Generated raw and packed resources:

- `source/raw/mod/gq000/world/gq000_patch_meet.streamingsector.json`
- `source/archive/mod/gq000/world/gq000_patch_meet.streamingsector`
- `source/raw/mod/gq000/world/gq000_always_loaded.streamingsector.json`
- `source/archive/mod/gq000/world/gq000_always_loaded.streamingsector`
- `source/raw/mod/gq000/world/gq000_patch_meet.streamingblock.json`
- `source/archive/mod/gq000/world/gq000_patch_meet.streamingblock`

The production world spec uses origin `(-795.7447, 390.34177, 17.272781)`.
Yaw remains provisional because the captured `ToVector4` did not include actor
heading.

The quest descriptor uses broad bounds during validation, matching the mq003
quest-sector reference pattern and avoiding a too-tight streaming box while the
location is still being tuned.

## Markers And Mappins

- The scene marker is `#gq000_01_sm_patch_bridge`.
- The map-pin marker is `#gq000_01_mp_patch_bridge`.
- Vanilla files confirm that scene markers and map-pin markers should be
  separate NodeRefs. Keep `#gq000_01_mp_patch_bridge` as the current quest map
  pin and POI static mappin target; do not point journal mappins back at
  `#gq000_01_sm_patch_bridge`.
- Vanilla mq003 places the scene marker under a nested scene prefab path, while
  the map-pin marker sits directly under the quest prefab root. Mirror that
  split when rebuilding Ghostline world resources from scratch.
- The full always-loaded scene marker NodeRef
  `$/mod/gq000/#gq000_pr_patch_meet/#gq000_01_sm_patch_bridge` resolves to
  `15587754031372558371`. That was a historical validation of always-loaded
  marker registration before the dedicated map-pin marker was split out; it is
  not the current mappin target.
- Runtime validation is still needed for the current dedicated map-pin marker
  `#gq000_01_mp_patch_bridge`.

## Community And Triggers

The quest sector contains:

- `#gq000_01_tr_setup`: 90-unit radius, height 4.
- `#gq000_01_tr_engage`: 4.5-unit radius, height 2.5.
- `#gq000_01_tr_bridge_case_mood`: 18-unit radius, height 3.
- `#gq000_01_tr_someone_coming`: 8-unit radius, height 2.5.
- `#gq000_01_spot_patch_bridge`: Patch community AI spot.
- `#gq000_01_com_patch_bridge`: streamable community area.

The community registry maps `patch/default` to:

- source object id `7897875840529598144`;
- spot NodeRef
  `$/mod/gq000/#gq000_pr_patch_meet/#gq000_01_spot_patch_bridge`;
- currently, temporary runtime isolation character `Character.Judy`.

After scene stabilization, the registry character should return to
`Character.GhostlinePatch`.

## Generator Findings

- A generated `worldStreamingSector` containing a `worldStaticMarkerNode` and
  `worldTriggerAreaNode` deserialized with WolvenKit.CLI 8.17.4 and
  round-tripped back to JSON with expected NodeRefs intact.
- `AreaShapeOutline.buffer` is the trigger outline source of truth. It stores a
  little-endian `uint32` point count, local `Vector4` points with `W = 1`, and a
  trailing `float` height. WolvenKit may serialize the visible `points` array
  as a default square even when the buffer contains the real outline.
- `WolvenKit.RED4.Types.NodeRef.GetRedHash()` returns the compound
  `worldGlobalNodeID` hash used by community spot IDs. The WolvenKit CLI
  `hash` command is plain FNV1A and does not produce these values.
- Generated AI spot, streamable community area, always-loaded community
  registry, and matching streaming block all deserialize to CR2W.
- CET player coordinates are usable directly by WolvenKit sector search and
  streaming-sector grid math.
- `WorldPosition` fixed-point values store coordinates as
  `coordinate * 131072`.
- Treat generator distances as world-coordinate units, approximately 1 unit per
  in-game meter, with final HUD/objective-distance calibration still required
  in game.

## Completed Reference Work

- Removed the leftover `#mq003_pr_corpse` root prefab from `gq000.questphase`.
- Replaced remaining `#mq003_pr_homeless` root prefab references with
  `#gq000_pr_patch_meet`.
- Resolved the root-vs-instance prefab question from mq003 streaming block and
  quest sector references.
- Added the production `gq000_patch_meet` world spec, quest sector,
  always-loaded registry sector, and streaming block.
- Registered the block in `source/resources/Ghostline.archive.xl`.
- Generated packed CR2W resources for the world files.
- Added always-loaded marker support so marker nodes can be emitted directly
  into the always-loaded sector.

## Remaining Validation

- Confirm ArchiveXL loads the streaming block in game.
- Confirm every quest/scene NodeRef resolves in game.
- Confirm the dedicated map-pin marker appears on the map.
- Tune Patch facing, workspot placement, and trigger radii.
- If Patch still crashes when streamed, audit or replace remaining `ep1\...`
  animation/effect dependencies in `mod\ghostline\characters\patch\patch.ent`
  or explicitly require Phantom Liberty.
