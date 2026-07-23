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
- The current root, meeting, and post-accept questphases each list
  `#gq000_pr_patch_meet` in root `phasePrefabs` because their journal/mappin or
  lifecycle graphs depend on world references under that prefab.
- Root phase nodes `30` and `32` load the meeting and post-accept resources.
  Their `phaseInstancePrefabs` arrays are empty because each child resource
  declares its own root `phasePrefabs`.

Ghostline world binding:

- `gq000_patch_meet.streamingblock` binds
  `questPrefabNodeRef: $/mod/gq000/#gq000_pr_patch_meet`.
- `gq000_patch_meet.streamingsector` registers quest-sector child refs under
  that prefab root and assigns matching `nodeData.QuestPrefabRefHash` values:
  - `#gq000_01_tr_setup`
  - `#gq000_01_tr_engage`
  - `#gq000_01_tr_bridge_case_mood`
  - `#gq000_01_tr_someone_coming`
  - `#gq000_01_spot_patch_bridge`
  - `#gq000_01_com_patch_bridge`
- `gq000_always_loaded.streamingsector` registers concrete always-loaded marker
  nodes for `#gq000_01_sm_patch_bridge`, `#gq000_01_mp_patch_bridge`, and
  `#gq000_02_mp_cache`.
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
- The cache map-pin marker is `#gq000_02_mp_cache`.
- The delivery map-pin marker is `#gq000_03_mp_drop_point`, colocated with
  native Kabuki `drop_point_009` but independent of its cooked NodeRef. The
  custom marker stays at the native entity root; its journal entry adds a
  two-unit vertical offset to reproduce the native `UI_Interaction` height.
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
- Runtime testing confirmed the dedicated meeting tracker/mappin path and its
  cleanup after `job_accept`, plus the post-accept cache marker. The delivery
  marker uses the yellow `DefaultQuestVariant`. The first complete route test
  confirmed the marker, native deposit, Morrow thread, reward, and quest
  success, but also exposed a floor-level icon and stale dotted route back
  toward the bridge. The next candidate raises the custom marker to the native
  interaction height and clears previous mappin state on delivery activation.

## Community And Triggers

The quest sector contains:

- `#gq000_01_tr_setup`: 90-unit radius, height 12.
- `#gq000_01_tr_engage`: 10-unit radius, height 12.
- `#gq000_01_tr_bridge_case_mood`: 60-unit radius, height 12.
- `#gq000_01_tr_someone_coming`: 20-unit radius, height 12.
- `#gq000_01_spot_patch_bridge`: Patch community AI spot.
- `#gq000_01_com_patch_bridge`: streamable community area.
- `#gq000_02_tr_cache_arrive`: 25-unit cache-arrival radius, height 12.
- `#gq000_02_tr_cache_cleanup`: 75-unit delayed-cleanup radius, height 16.
- `#gq000_02_ap_cache`: Ghostline-owned native access point mounted at the
  selected cabinet.
- `#gq000_02_spot_guard_ranged_m` and
  `#gq000_02_spot_guard_ranged_m_patrol_02`: a finite, ordered patrol pair.
- `#gq000_02_spot_guard_ranged_f` and `#gq000_02_spot_guard_melee`: close
  static sentry workspots.
- `#gq000_02_com_cache_guards`: inactive-on-start three-entry Tyger Claw
  community.

The community registry maps `patch/default` to:

- source object id `7897875840529598144`;
- spot NodeRef
  `$/mod/gq000/#gq000_pr_patch_meet/#gq000_01_spot_patch_bridge`;
- current runtime character `Character.GhostlinePatch`;
- current runtime appearance `ghostline_patch_default`, which is the exposed
  root `.ent` mapping name rather than internal `.app` definition `default`.

The community area's NodeRef hash, its `sourceObjectId`, and the registry
item's `communityId` intentionally share `7897875840529598144`. The separate
always-loaded registry node must have a different global identity. It now uses
`7571954536596633334`, derived from the synthetic full ref
`$/mod/gq000/#gq000_pr_patch_meet/#gq000_01_com_patch_bridge_registry`.

The 2026-07-22 Patch shipping candidate restored
`Character.GhostlinePatch` after installing TweakXL 1.11.3. Its first runtime
pass must validate the custom record and appearance while repeating the
sorted-locStore label regression. The preceding Judy mapping remains the
known-good lifecycle baseline.

The cache guard registry uses the exact records extracted from vanilla
Japantown activity `ma_wbr_jpn_013_claws_com.community`:

- `Character.jpn_tyger_claws_gangster2_ranged2_sidewinder_ma`
- `Character.jpn_tyger_claws_biker2_ranged2_copperhead_wa`
- `Character.jpn_tyger_claws_biker1_melee1_baseball_ma`

These provide one Sidewinder gunner, one Copperhead gunner, and one baseball-
bat melee guard.
Their records already use `tygerClaws_ow` and `Squad_Basic`, but runtime testing
showed that a quest-activated standalone community remains passive without an
encounter/security instruction. The phase therefore uses whole-community
`Activate None/None`, a whole-community `CharacterSpawned > 0` readiness gate,
and then a separate hostility branch when V enters the 25-unit arrival trigger.
The first border-patrol-derived attempt executed—the extraction objective
appeared—but its null/implicit target did not make these otherwise passive
guards attack. The current branch copies vanilla `mq022_combat.questphase` for
each named community entry: set `neutral`, set `hostile`, assign the immediate
combat target, then inject an explicit `#player` threat with
`dontForceHostileAttitude = 0`. The main objective flow does not wait on those
commands, and killing every guard is deliberately not an objective.

The first movement pass uses finite community workspot sequencing rather than
a spline. One gunner has two nearby `guard_stand.workspot` nodes with
`isWorkspotInfinite = 0`, while its phase period has `isSequence = 1` and
`quantity = 1`. The other two guards remain at close sentry spots. This is the
documented low-risk patrol path; a `worldSplineNode` would additionally require
quest movement or `AIPatrolRole` commands and is deferred until navmesh testing
proves the finite route.

The first runtime candidate placed all three AI spots at the cache but left
the streamable guard community-area node at the bridge origin, over a
kilometre away and outside its 320-unit stream distance. No guards could
materialize. The production spec now anchors that area at
`(-1000.02, 1497.2208, 6.957)`, beside its spots and the relay.

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
- `community.registry_node_id` defaults to a deterministic hash of the full
  community area ref with `_registry` appended. Generation fails if that ID is
  zero or collides with the community/source ID, spot ID, or an emitted world
  NodeRef.
- CET player coordinates are usable directly by WolvenKit sector search and
  streaming-sector grid math.
- `WorldPosition` fixed-point values store coordinates as
  `coordinate * 131072`.
- Treat generator distances as world-coordinate units, approximately 1 unit per
  in-game meter, with final HUD/objective-distance calibration still required
  in game.

### Cache Cabinet Collision Fingerprint

The cabinet-style relay inspected at `-999.564, 1497.221, 6.957` is not a
standalone entity or mesh node. World Inspector resolves it as zero-based actor
36 of 64 inside `NormalCollisionNode_087` in
`exterior_-8_11_0_1.streamingsector`:

- source prefab hash: `8325780084261042030`
- collision shape hash: `12135205187229491652`
- orientation: `i=0, j=0, k=0.698, r=0.716`
- visible proxy: `ecoset_recycling_station_a_21x9_adhelper_ProxyMesh`

Searching that sector by collision-shape hash finds 18 matching cabinet
actors across three collision nodes. A second capture in Rancho Coronado used
different debug and source-prefab identifiers but the same collision shape
hash, confirming that `12135205187229491652` is a reusable cabinet-family
fingerprint. Its inspected actor 59 resolves to
`145.1341, -1298.3799, 7.7528`, and actor 60 identifies the adjacent matching
panel. Use `tools/find_collision_instances.py` to recover exact transforms in
another serialized sector. The debug name alone is not a global cabinet
identifier: it names a composite collision bundle inside a source prefab.

The implemented interaction model is a Ghostline-owned device positioned at
one cabinet transform while preserving the vanilla recycling-station proxy and
collision. It uses
`base\gameplay\devices\masters\access_points\accesspoint.ent` with outer
appearance mapping `access_point_access_point_socket_f_neomil`. The template
provides the socket visual, personal-link workspot, interaction, native breach
minigame, and `AccessPointControllerPS`; no custom controller is needed.

The mount is `(-1000.02, 1497.2208, 8.3)`, yaw `178.6`. Runtime testing showed
that both `88.6` and its `-91.4` inverse leave the terminal plate perpendicular
to the cabinet row. Collision actors 36 and 44 establish a row heading of
approximately `-91.4` degrees, while the access-point plate normal and
personal-link side use entity-local `+X`. Mapping that local normal outward to
world `-X` requires absolute yaw `178.6` (equivalent to `-181.4`), which is a
shortest-path rotation of exactly `-90` degrees from the tested `-91.4` build.
The cache site mappin keeps its independent `88.6` yaw. The device instance starts `OFF`, uses
`DeviceContentAssignment.Autoscaling`, and names its network `QUIET SPINE
RELAY`. Its RedPackage uses buffer ID `1` because the sector node-data buffer
already owns ID `0`. WolvenKit 8.17.4 deserialization and serialization retain
both buffers and all generated world topology.

The custom `worldDeviceNode` also needs a device-registry entry; rendering the
socket and opening its minigame are not sufficient evidence that quest-side
controller lookup is reliable. The runtime-fix candidate therefore emits the
minimal resource `mod\gq000\world\gq000_custom_devices.devices` and
ArchiveXL resource-patches it into
`base\worlds\03_night_city\_compiled\default\03_night_city.devices`. Its one
`AccessPointControllerPS` entry uses full NodeRef
`$/mod/gq000/#gq000_pr_patch_meet/#gq000_02_ap_cache`, hash
`13482927561872837971`, and the relay position above. A `.psrep` resource may
be added later if persistent device state proves necessary, but it is not a
prerequisite for this test candidate; no sector persistent-state clone is
planned.

The same Rancho Coronado capture also identified a reusable standalone device
visual: `base\gameplay\devices\vending_machines\vending_machine_1.ent`,
appearance `vending_machines_b_cirrus_cage`. Never patch that shared entity or
replace its controller globally. A vending-machine cache must either be a
mod-owned clone or temporarily disable one specific vanilla instance while a
Ghostline access-point overlay is active.

### Delivery Drop-Point Reference

The active delivery target is the live, map-labelled `drop_point_009` in
Kabuki. World Inspector confirmed that it is publicly accessible. It is about
252.7 world units from the cache and beyond the 75-unit encounter-cleanup
radius:

- NodeRef:
  `$/03_night_city/c_watson/kabuki/kabuki_drop_points_prefabAR4NTYY/drop_point_009_prefabBIYNP3Y`
- position: `(-1168.66333, 1309.51709, 19.9768238)`
- orientation quaternion: `(0, 0, 0.999, 0.044)`, approximately `175` degrees
- debug name: `drop_point_009`
- record: `Devices.DropPoint`
- entity template: `base\gameplay\devices\drop_points\drop_point.ent`
- source sector: `exterior_-19_20_0_0.streamingsector`

Vanilla `sts_wat_kab_05` demonstrates the delivery contract: send
`ReserveItemToThisDropPoint` through `DropPointManager`/
`DropPointControllerPS`, then wait for the deposited item's short-name fact.
Ghostline's generated delivery phase uses the same fire-and-forget event fan-
out and reserves the separate `Items.gq000_datacache` quest package; the two
readable Quiet Spine shards remain in the inventory.

The native device NodeRef remains the reservation target, but it is not the
journal-UI target. ArchiveXL logged `Can't resolve mappin ... position` when the
quest mappin referenced a cooked cross-world drop-point NodeRef directly.
Ghostline therefore places always-loaded static marker
`#gq000_03_mp_drop_point` at the device template's transformed
`main_slot/navQuery` approach point and points the journal entry there with
`DefaultQuestVariant`, producing the normal yellow side-quest marker and a
walkable GPS endpoint. Reusing the device still requires no custom drop-point
device or Ghostline `.devices` registry entry; the custom node is only a UI
marker. The previous kiosk candidate was both poorly exposed by surrounding
geometry and unsuitable as a direct journal-mappin target.

The prefab and sector data are also sufficient to build a future selectable
pool. Enumerate serialized world entities whose record is `Devices.DropPoint`,
template is `drop_point.ent`, or NodeRef matches the sibling `drop_point_*`
pattern, then retain each exact NodeRef, transform, and source sector. Candidate
discovery is mechanical; every entry still needs an accessibility/map-label
review before inclusion, and a randomized runtime route must keep its native
reservation target paired with the corresponding Ghostline marker.

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
- Extended the generator to support native access-point devices, multiple
  communities, multiple entries, and multiple spots per entry.
- Added always-loaded marker support so marker nodes can be emitted directly
  into the always-loaded sector.
- Completed the full Judy isolation route through community activation, all
  four approach gates, scene placement, meeting mappin cleanup, and cache
  mappin activation. This confirms the active streaming block and NodeRef path;
  it does not validate the custom Patch character.

## Remaining Validation

- Validate explicit map-screen and POI behavior for the dedicated meeting
  marker.
- Rebuild and validate the scene marker under a vanilla-style nested scene
  prefab path.
- Keep the runtime-confirmed `Character.GhostlinePatch` mapping and appearance
  while validating future character edits.
- Tune trigger footprints only if real-location testing exposes presentation
  issues; keep the proven 90/60/20/10 radii and 12-unit height as the baseline.
- If Patch still crashes when streamed, audit or replace remaining `ep1\...`
  animation/effect dependencies in `mod\ghostline\characters\patch\patch.ent`
  or explicitly require Phantom Liberty.
- Confirm the corrected socket yaw and visually tune only its cabinet-face
  offset if needed; validate the three provisional guard workspots on navmesh.
- Confirm the cache arrival and delayed cleanup triggers fire at the intended
  boundaries and that surviving guards deactivate only after V leaves.
- Confirm `#gq000_03_mp_drop_point` resolves at the accessible machine, appears
  yellow, and clears after the native datacache deposit.
