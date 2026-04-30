# Ghostline Roadmap

Last audited: 2026-04-30

This file records the current project state and the next work needed to turn `gq000` from a dialogue prototype into a playable quest slice. It is based on the files under `source`, the helper explorers in `tools`, and local references in `modding_docs`.

## Current Status

### Project registration

- `source/resources/Ghostline.archive.xl` exists and currently registers:
  - `mod\gq000\phases\gq000.questphase` as a root questphase under `base\quest\cyberpunk2077.quest`
  - `mod\ghostline\localization\en-us\onscreens\ghostline.json` for generic onscreen localization
  - `mod\gq000\journal\gq000.journal` for the first quest journal data
  - `mod\gq000\localization\en-us\onscreens\gq000.json` for quest-specific onscreen localization
  - `mod\gq000\world\gq000_patch_meet.streamingblock` for the Patch meeting world data

### Patch character

- Patch has packed character resources under `source/archive/mod/ghostline/characters/patch`:
  - `patch.ent`
  - `patch.app`
  - body/head meshes, textures, and morphtargets
- `source/resources/r6/tweaks/ghostline/character_patch.yaml` defines `Character.GhostlinePatch` with:
  - `entityTemplatePath: mod\ghostline\characters\patch\patch.ent`
  - `displayName` and `fullDisplayName` set to `gq_npc_patch`
  - `affiliation: Factions.Ghostline`
  - `voiceTag: gq_patch`
- `source/resources/r6/tweaks/ghostline/faction_ghostline.yaml` defines `Factions.Ghostline`.
- `source/raw/mod/ghostline/localization/en-us/onscreens/ghostline.json.json` contains onscreen entries for `gq_npc_patch` and `mod_gq_faction_ghostline`.
- Raw CR2W-JSON source files now exist for Patch's root entity and appearance resource:
  - `source/raw/mod/ghostline/characters/patch/patch.ent.json`
  - `source/raw/mod/ghostline/characters/patch/patch.app.json`
- `py .\tools\explore_ent_app.py summary` reports:
  - `patch.ent`: 1 root appearance, 110 root components, 249 handles, 61 resolved dependencies
  - `patch.app`: 1 appearance definition named `default`, 47 appearance components, 103 handles
- `patch.ent` appearance `ghostline_patch_default` maps `appearanceName: default` to `mod\ghostline\characters\patch\patch.app`.
- Checked 2026-04-29: Patch's `.app` currently references zero of the copied
  `mod\ghostline\characters\patch\...` mesh, morphtarget, and texture files by
  custom path. The copied files are present under `source/archive`, but the
  appearance still points at base/player resources or numeric resource hashes.
  If the Judy community probe works, the next Patch-specific fix is to
  custompath/repoint the `.app` and dependent mesh resources rather than only
  packaging the copied files.
- Fixed 2026-04-30: Patch's `.app` head/body mesh components now point at real
  depot paths instead of unresolved numeric `ResourcePath` IDs. The copied
  head, body, makeup, beard, nails, arms, genitals, eyes, teeth, and personal
  slot meshes now use `mod\ghostline\characters\patch\...` paths in both the
  appearance components and compiled chunks. The optional `h0_cyberware_face`
  mesh was disabled because its numeric mesh ID did not resolve to any packed
  game or mod resource.
- Packaging risk 2026-04-29: the scoped archive currently includes
  `source/archive/base`, which packs many
  `base\characters\head\player_base_heads\player_man_average\...` files as
  global base-path overrides. These should not ship in the normal install
  archive unless Patch's `.app` genuinely requires them and their impact on
  player/base NPC resources has been validated.

### Quest phases

- Packed questphase binaries exist:
  - `source/archive/mod/gq000/phases/gq000.questphase`
  - `source/archive/mod/gq000/phases/gq000_patch_meet.questphase`
- Editable raw JSON now exists for both current questphases:
  - `source/raw/mod/gq000/phases/gq000.questphase.json`
  - `source/raw/mod/gq000/phases/gq000_patch_meet.questphase.json`
- `gq000.questphase` has 7 graph nodes and 7 edges:
  - input
  - phase node id `2` containing setup/community/journal work
  - phase node id `3`, which loads `mod\gq000\phases\gq000_patch_meet.questphase`
  - logical hub node id `11` on the phase failure branch
  - facts DB manager node id `12` on the phase success branch
  - phase node id `13`
  - terminating output
- The root phase flow is `input -> phase id 2 -> gq000_patch_meet phase id 3 -> facts/logical branch -> phase id 13 -> output`.
- Fixed 2026-04-29: root phase community activation/deactivation now targets
  community entry `patch` and phase `default`, matching the generated
  community registry and streamable community area. It previously targeted
  entry `None` and activation phase `start`.
- `gq000_patch_meet.questphase` currently has 7 graph nodes and 6 edges:
  - input
  - journal node for `points_of_interest/minor_quests/gq000_01_poi_patch_bridge`
  - trigger wait for `#gq000_01_tr_setup`
  - checkpoint `gq000_patch_meet`
  - trigger wait for `#gq000_01_tr_engage`
  - scene node for `mod\gq000\scenes\gq000_patch_meet.scene` at `#gq000_01_sm_patch_bridge`
  - terminating output
- The phase exits through the scene node socket `job_accept` into a terminating output. No post-accept gameplay phase/objective branch exists yet.

### Scene

- Packed and raw scene files exist:
  - `source/archive/mod/gq000/scenes/gq000_patch_meet.scene`
  - `source/raw/mod/gq000/scenes/gq000_patch_meet.scene.json`
- The scene has 18 graph nodes, 21 edges, 13 spoken lines, and 5 player choices.
- Actors:
  - Patch is acquired from the active community entry `patch` at
    `#gq000_01_com_patch_bridge`, matching the vanilla `mq003_01_homeless`
    scene actor pattern.
  - V is found in context via `Character.Player_Puppet_Base`
- The scene includes `performersDebugSymbols`, which is required for scenes built from scratch according to `modding_docs/modding-guides/quest/creating-custom-scenes.md`.
- The dialogue flow is currently:
  - Patch intro line
  - optional choices: `Ghostline?`, `Why me?`
  - required choice: `What's the job?`
  - optional choice: `Who's behind it?`
  - required accept choice: `I'm in.`
- Fixed 2026-04-29: the scene no longer points at stale tutorial lipsync
  animsets under `mod\audiowaredialogtest\localization\en-us\lipsync`. Patch
  and V now keep their indexed lipsync animset entries pointed at the base
  generic facial lipsync gesture animset until Ghostline-owned lipsync assets
  are generated.
- Fixed 2026-04-30: the Patch scene actor no longer uses the tutorial-style
  `spawnDespawn` acquisition at `#gq000_01_sm_patch_bridge`. A vanilla mq003
  comparison showed community-spawned quest NPCs are scene-bound with
  `acquisitionPlan: community`, `communityParams.reference`, and
  `communityParams.entryName`; `gq000_patch_meet.scene` now uses that pattern
  for `#gq000_01_com_patch_bridge` / `patch`.

### Dialogue localization and VO

- `source/raw/mod/gq000/localization/en-us/subtitles/gq000_01.json.json` and `source/raw/mod/gq000/localization/en-us/vo/gq000_01.json.json` are aligned.
- `py .\tools\explore_localization.py check` reports no subtitle/VO coverage problems.
- `source/raw/gq000_01_manifest.json` records the generated line keys, string IDs, text, audio paths, and durations.
- The VO map points at `.wem` paths, and `source/archive/mod/gq000/localization/en-us/vo` now contains matching Wwise-generated `.wem` files alongside the authored `.wav` sources.
- `tools/convert_wavs_to_wem.ps1` normalizes WAVs into `wwise_conversion\ExternalSources`, writes `external_sources.wsources`, runs Wwise external source conversion for Windows with `Vorbis Quality High`, and copies WEMs back into the VO folder without deleting WAVs.
- Checked 2026-04-27: WolvenKit.CLI 8.17.4 exposes a `wwise` command, but its implementation only supports `.wem` to `.ogg` conversion when `--wem` is set and cannot convert the current `.wav` VO sources to `.wem`.
- Checked 2026-04-29: `gq000_patch_meet.scene` still does not use
  Ghostline-owned generated lipsync `.anims` files; it uses a base generic
  facial lipsync animset as a non-missing placeholder.

### Journal and quest UI

- Added journal explorer tooling:
  - `tools/explore_journal.py`
  - `py .\tools\explore_journal.py prefixes --with-types` summarizes one representative `.journal` file for each first-dot prefix in `reference/journal`.
- Explored representative journal reference prefixes:
  - `briefings`: briefing folders plus `gameJournalBriefing*` sections.
  - `codex`: codex categories/groups/entries/descriptions.
  - `contacts`: `gameJournalContact`.
  - `internet_sites`: internet site/page entries.
  - `onscreens`: onscreen groups and onscreen entries.
  - `points_of_interest`: `gameJournalPointOfInterestGroup` and `gameJournalPointOfInterestMappin`.
  - `quests`: `gameJournalQuest`, phase, objective, description, quest map pin, and codex link entries.
  - `tarots`: tarot group/card entries.
- Added packed and raw `gq000` journal resources:
  - `source/archive/mod/gq000/journal/gq000.journal`
  - `source/raw/mod/gq000/journal/gq000.journal.json`
- The `gq000` journal currently defines:
  - quest root `quests/minor_quest/gq000`
  - phase `quests/minor_quest/gq000/gq000_01`
  - objective `quests/minor_quest/gq000/gq000_01/gq000_01_obj_meet_patch`
  - description `quests/minor_quest/gq000/gq000_01/gq000_01_obj_meet_patch/gq000_01_desc_meet_patch`
  - quest map pin `quests/minor_quest/gq000/gq000_01/gq000_01_obj_meet_patch/gq000_01_qmp_patch_bridge`
  - point of interest `points_of_interest/minor_quests/gq000_01_poi_patch_bridge`
- Added packed and raw quest onscreen localization:
  - `source/archive/mod/gq000/localization/en-us/onscreens/gq000.json`
  - `source/raw/mod/gq000/localization/en-us/onscreens/gq000.json.json`
- Quest onscreen localization uses ArchiveXL-style `primaryKey: "0"` entries with unique `gl_` secondary keys, and the journal fields reference those secondary keys directly.
- Updated `gq000.questphase`, `gq000_patch_meet.questphase`, and `gq000_patch_meet.scene` raw and packed resources so journal references use full journal paths instead of bare leaf ids.
- Runtime finding 2026-04-29: ArchiveXL reported
  `Can't resolve mappin #3133219362 position`, and the quest marker did not
  appear on the map. The journal still correctly points both the quest map pin
  and POI static mappin at `#gq000_01_sm_patch_bridge`; the world data now
  registers the corresponding full NodeRef
  `$/mod/gq000/#gq000_pr_patch_meet/#gq000_01_sm_patch_bridge` in the
  always-loaded sector so the cooked mappin can resolve before the quest sector
  streams at the player.
- Runtime follow-up 2026-04-29: after the always-loaded mappin registration,
  ArchiveXL resolves cooked mappin `3133219362` to NodeRef hash
  `15587754031372558371`, but Patch still does not appear and the game crashes
  on approach near `[-791, 392, 19]`. The next isolation target is the
  community/entity spawn path, not journal mappin resolution.
- Runtime follow-up 2026-04-29: a no-base probe that excluded
  `source/archive/base` still crashed on save load, and its
  `Engine/LoadExports` hashes resolved to the game's built-in always-loaded
  sectors:
  - `0x9A885B987F8F0678` =
    `base\worlds\03_night_city\_compiled\default\always_loaded_0.streamingsector`
  - `0xD99DB827623875A2` =
    `base\worlds\03_night_city\_compiled\default\always_loaded_2.streamingsector`
  - `0xF01E02F0B66AE3F0` =
    `base\worlds\03_night_city\_compiled\default\ep1\always_loaded_0.streamingsector`
  This rules out the packaged base-path overrides as the sole cause and points
  back at our always-loaded streaming merge shape.

### World reference assets

- `reference/world` contains two deserialized reference sets:
  - `000`: mq003 quest-sector references.
  - `001`: Object Spawner-style streaming block, exterior sector, and always-loaded community registry sector.
- Added world reference tooling:
  - `tools/serialize_reference_world.ps1` serializes `.streamingblock` and `.streamingsector` CR2W binaries under `reference/world` into colocated CR2W-JSON.
  - `tools/explore_world.py` summarizes streaming block descriptors, sector nodes, NodeRefs, trigger outlines, and community registry/area wiring.
  - `tools/generate_world.py` generates Ghostline-owned raw `.streamingsector.json`
    and `.streamingblock.json` files from a coordinate spec, including static
    markers, quest trigger areas, optional Patch community/AI spot wiring,
    always-loaded NodeRef registrations, ArchiveXL registration, and optional
    WolvenKit deserialization.
  - `tools/gq000_world_spec.example.json` documents the current generator spec
    shape for the Patch meeting world data.
  - `tools/world_spec.md` is the full generator spec reference, including
    coordinate units, anchors, trigger outlines, notifiers, community fields,
    node-data overrides, and validation workflow.
- `py .\tools\explore_world.py summary` reports:
  - `reference/world/000/blocks/all.streamingblock.json`: 2 quest descriptors, both with `questPrefabNodeRef` values under the mq003 Santo Domingo prefab path.
  - `reference/world/000/always_loaded_0.streamingsector.json`: 0 nodes, 4 `nodeData` entries, and 32 registered `nodeRefs`; this is a useful reference for alias registration separate from concrete node definitions.
  - `reference/world/000/quest_606b61008df2ba6f.streamingsector.json`: 21 quest-sector nodes, including 11 `worldAISpotNode`, 6 `worldTriggerAreaNode`, 3 `worldSplineNode`, and 1 `worldVehicleForbiddenAreaNode`.
  - `reference/world/001/world/all.streamingblock.json`: 1 `Exterior` descriptor for `mod\sectors\npcac.streamingsector` plus 1 `AlwaysLoaded` descriptor for `mod\sectors\mod_always_loaded.streamingsector`.
  - `reference/world/001/sectors/npcac.streamingsector.json`: 1 `worldAISpotNode`, 1 `worldCompiledCommunityAreaNode_Streamable`, and 2 `worldTriggerAreaNode` nodes.
  - `reference/world/001/sectors/mod_always_loaded.streamingsector.json`: 1 `worldCommunityRegistryNode`.
- Community reference findings from `py .\tools\explore_world.py communities`:
  - The registry sector maps entry `judy`, phase `default`, character `Character.Judy`, and source object id `982477135194481732` to spot NodeRef `$/mod/npcac/#npcac_spot`.
  - The streamable community area sector uses the same entry, phase, and source object id, and maps it to spot id `1141382493228110045`.
- Trigger reference findings from `py .\tools\explore_world.py nodes --type TriggerArea --limit 0`:
  - mq003 quest triggers and Object Spawner trigger examples both use `worldTriggerAreaNode` with `AreaShapeOutline` height `2` and 4 points.
  - The current Ghostline trigger names have direct mq003 analogs for engage, case mood, and someone-coming trigger patterns.
- Programmatic world-generation findings from 2026-04-28:
  - A generated raw `worldStreamingSector` containing a `worldStaticMarkerNode`
    and `worldTriggerAreaNode` deserialized with WolvenKit.CLI 8.17.4 and
    round-tripped back to JSON with the expected NodeRefs intact.
  - `AreaShapeOutline.buffer` is the trigger outline source of truth. It stores
    a little-endian `uint32` point count, local `Vector4` points with `W = 1`,
    and a trailing `float` height. WolvenKit may serialize the visible `points`
    array as a default square even when the buffer contains the real outline.
  - `WolvenKit.RED4.Types.NodeRef.GetRedHash()` returns the compound
    `worldGlobalNodeID` hash used by community spot IDs. The CLI `hash`
    command is plain FNV1A and does not produce these values.
  - A generated AI spot plus `worldCompiledCommunityAreaNode_Streamable`,
    always-loaded `worldCommunityRegistryNode`, and matching streaming block
    also deserialized to CR2W. This proves the CR2W shape is scriptable, but
    the generated resources still need in-game validation before treating the
    generator as production-ready.
  - Coordinate-distance investigation: CET player coordinates are used directly
    by WolvenKit sector search and streaming-sector grid math, reference sector
    positions measure out as plausible gameplay distances, and `WorldPosition`
    fixed-point values store coordinates as `coordinate * 131072`. Treat
    generator distances as world-coordinate units, approximately 1 unit per
    in-game meter, with final HUD/objective-distance calibration still required
    in game.

### World placement and community

- Added production world spec `tools/gq000_patch_meet.world.json` using captured
  origin `(-795.7447, 390.34177, 17.272781)`.
- The spec keeps yaw at provisional `0` because the captured `ToVector4` did
  not include actor heading. Trigger outlines are circular so quest progression
  is not dependent on that yaw before in-game facing tuning.
- The quest descriptor uses world-wide bounds during first validation, matching
  the mq003 quest-sector reference pattern and avoiding a too-tight streaming
  box while the location is still being tuned.
- Generated raw and packed world resources:
  - `source/raw/mod/gq000/world/gq000_patch_meet.streamingsector.json`
  - `source/archive/mod/gq000/world/gq000_patch_meet.streamingsector`
  - `source/raw/mod/gq000/world/gq000_always_loaded.streamingsector.json`
  - `source/archive/mod/gq000/world/gq000_always_loaded.streamingsector`
  - `source/raw/mod/gq000/world/gq000_patch_meet.streamingblock.json`
  - `source/archive/mod/gq000/world/gq000_patch_meet.streamingblock`
- `py .\tools\explore_world.py --file .\source\raw\mod\gq000\world summary`
  reports one always-loaded sector with 2 nodes:
  - `worldStaticMarkerNode` for `#gq000_01_sm_patch_bridge`
  - `worldCommunityRegistryNode` for the Patch community registry
- The quest sector now has 6 nodes:
  - four `worldTriggerAreaNode` nodes for the current quest and scene trigger refs
  - `worldAISpotNode` for `#gq000_01_spot_patch_bridge`
  - `worldCompiledCommunityAreaNode_Streamable` for `#gq000_01_com_patch_bridge`
- The always-loaded sector now creates the bridge static marker as a concrete
  `worldStaticMarkerNode`, rather than a synthetic registration-only node-data
  row. The marker's full NodeRef is
  `$/mod/gq000/#gq000_pr_patch_meet/#gq000_01_sm_patch_bridge`;
  `tools\generate_world.py hash` resolves it to `15587754031372558371`,
  matching the successful ArchiveXL mappin-resolution log from the first
  runtime pass.
- Trigger outline sizes in the current spec:
  - `#gq000_01_tr_setup`: 90-unit radius, height 4
  - `#gq000_01_tr_engage`: 4.5-unit radius, height 2.5
  - `#gq000_01_tr_bridge_case_mood`: 18-unit radius, height 3
  - `#gq000_01_tr_someone_coming`: 8-unit radius, height 2.5
- The streaming block contains a Quest descriptor for
  `mod\gq000\world\gq000_patch_meet.streamingsector` with
  `questPrefabNodeRef: $/mod/gq000/#gq000_pr_patch_meet` and world-wide
  bounds, plus an AlwaysLoaded descriptor for
  `mod\gq000\world\gq000_always_loaded.streamingsector`.
- The community registry maps `patch/default` to `Character.GhostlinePatch`,
  source object id `7897875840529598144`, and spot NodeRef
  `$/mod/gq000/#gq000_pr_patch_meet/#gq000_01_spot_patch_bridge`.
- Temporary runtime override 2026-04-30: while the Patch-specific approach
  crash is being isolated, the active `tools/gq000_patch_meet.world.json`
  community character record is `Character.Judy` for the same `patch/default`
  entry. The questphase and scene still use the `patch` community entry name,
  so this should be reverted to `Character.GhostlinePatch` after the crash is
  resolved.
- Diagnostic 2026-04-29: built `Ghostline_judy_probe.zip`, which keeps the
  same marker, triggers, community area, source object id, and AI spot, but
  swaps the registry `characterRecordId` from `Character.GhostlinePatch` to
  `Character.Judy`. If Judy appears without a crash, the remaining fault is in
  Patch's custom TweakXL/entity/appearance resources. If it still crashes, the
  remaining fault is in the generated community/world sector shape.
- Runtime follow-up 2026-04-29: the Judy probe crashed during save load, far
  from the quest location, before normal population state initialized. Treat
  this probe as inconclusive; swapping to a story NPC inside the always-loaded
  registry can introduce unrelated preload failures.
- Diagnostic 2026-04-29: built `Ghostline_no_base_probe.zip`, which keeps the
  current Ghostline-owned `mod\...` resources but excludes `source/archive/base`
  from the install archive. Use this to test whether the packaged
  `base\characters\head\player_base_heads\...` overrides are causing the
  load-time crash.
- Runtime follow-up 2026-04-29: `Ghostline_no_base_probe.zip` still crashed on
  load. Built `Ghostline_marker_alwaysloaded_probe.zip`, which keeps the
  no-base packaging but moves `#gq000_01_sm_patch_bridge` into the
  always-loaded sector as a real static marker node. Use this to test whether
  the previous registration-only always-loaded marker row was destabilizing the
  world streaming merge.
- Runtime follow-up 2026-04-29/30: the marker-in-always-loaded probe loaded and
  resolved the cooked mappin, but Patch did not appear and the game still
  crashed on approach. RedHotTools reported missing resource hash
  `14413217326793937713` (`0xC80608CB520ED331`), which does not exist in the
  installed content, EP1, or mod archives and does not appear in the serialized
  copied Patch mesh/morphtarget resources. Built
  `Ghostline_judy_marker_probe.zip` to retest the same world/community shape
  with `Character.Judy` after the always-loaded marker fix.
- Diagnostic 2026-04-30: built `Ghostline_custompath_patch_probe.zip`, which
  keeps the no-base packaging and fixed always-loaded marker, but includes the
  patched `patch.app` with real custom mesh paths. Use this before deeper
  entity surgery; if the missing hash changes, continue custompathing nested
  mesh/material dependencies.
- Runtime follow-up 2026-04-30: with the fixed always-loaded marker shape,
  `Character.Judy` successfully spawned from the Ghostline community spot, but
  the game still crashed on approach. This isolates the world/community
  registry and spot as functional and points at the approach scene handoff.
  RedHotTools reported missing hashes `14413217326793937713`
  (`0xC80608CB520ED331`) and `16106537288591666266`
  (`0xDF85EA53F016EC5A`); neither appears as a literal serialized reference in
  the Ghostline source. Built `Ghostline_scene_community_probe.zip` after
  switching the scene actor from `spawnDespawn` to vanilla-style community
  acquisition.
- Diagnostic 2026-04-30: built `Ghostline_judy_scene_community_probe.zip`,
  which combines the vanilla-style community scene actor with a temporary
  `Character.Judy` registry record for entry `patch/default`. Use this package
  as the current crash-isolation baseline.
- Checked 2026-04-30: compared Ghostline community/AI spot wiring against
  `mq003_homeless`. Vanilla mq003 uses community scene acquisition and quest
  SpawnManager activation/deactivation for entries; the scene binds to an
  active community actor rather than spawning one itself.
- Checked 2026-04-30: hashed every typed/string `#` NodeRef-like value in
  Ghostline mod source/spec/generated files, including local and full-prefab
  variants plus numeric NodeRef fields. RedHotTools missing hashes
  `14413217326793937713` and `16106537288591666266` do not match any of them,
  or any explicit serialized resource-path string in those files, so they are
  likely runtime-generated dependency hashes rather than bad serialized
  `#gq000...` NodeRefs.
- Diagnostic 2026-04-30: set the temporary Judy community registry entry
  inactive by default (`entryActiveOnStart: 0`) and built
  `Ghostline_judy_inactive_community_probe.zip`. Use it to test the vanilla
  lifecycle shape while keeping Judy as the crash-isolation character.
- Runtime follow-up 2026-04-30: Judy still appears with
  `entryActiveOnStart: 0`, confirming the root quest SpawnManager activation
  path works. The mappin still does not show on the map, and the crash still
  occurs on approach near the engage/scene boundary. RedHotTools again reported
  missing hash `14413217326793937713`, but this remains unmatched to explicit
  Ghostline NodeRefs/resource paths.
- Diagnostic 2026-04-30: built
  `Ghostline_judy_skip_scene_inactive_probe.zip`, which keeps the same Judy
  inactive-community world state but rewires `gq000_patch_meet.questphase` so
  `#gq000_01_tr_engage` routes directly to the phase output instead of starting
  `mod\gq000\scenes\gq000_patch_meet.scene`. Use this to isolate whether the
  crash is caused by scene startup or by the world/quest trigger path before
  the scene.
- Runtime follow-up 2026-04-30: the skip-scene inactive-community probe still
  spawned Judy and did not crash, confirming the remaining crash is inside
  `gq000_patch_meet.scene` startup or scene graph execution rather than the
  world/community/trigger path.
- Diagnostic 2026-04-30: built two scene-start isolation packages:
  `Ghostline_judy_scene_start_end_probe.zip` rewires the scene start directly
  to the scene end node, while `Ghostline_judy_scene_direct_dialogue_probe.zip`
  rewires scene start directly to the first dialogue section. Test them in that
  order to split actor/scene startup, dialogue sections, and embedded scene
  quest nodes.
- Runtime follow-up 2026-04-30: `Ghostline_judy_scene_start_end_probe.zip`
  works, while `Ghostline_judy_scene_direct_dialogue_probe.zip` crashes on
  approach and RedHotTools reports missing resource hash `16106537288591666266`
  (`0xDF85EA53F016EC5A`) again. This narrows the active crash path to the first
  dialogue section, not actor acquisition, scene startup, world/community
  streaming, or trigger activation.
- Fixed/probe 2026-04-30: `source/resources/Ghostline.archive.xl` now
  registers the `gq000_01` subtitle map under `localization.subtitles` and
  the voiceover map under `localization.vomaps`. ArchiveXL logs previously
  reported "No voiceover maps to merge" and "No subtitles to merge", so
  `Ghostline_judy_vo_registration_probe.zip` should show concrete merge lines
  for `mod\gq000\localization\en-us\subtitles\gq000_01.json` and
  `mod\gq000\localization\en-us\vo\gq000_01.json` during runtime validation.
- Diagnostic 2026-04-30: built
  `Ghostline_judy_scene_direct_dialogue_registered_probe.zip`, which repeats
  the crashing direct-to-first-dialogue-section test but includes the new
  ArchiveXL subtitle/VO map registration. Test this before the normal full
  scene package if a tight before/after comparison is needed.
- Runtime follow-up 2026-04-30:
  `Ghostline_judy_scene_direct_dialogue_registered_probe.zip` still crashes on
  the first dialogue section. ArchiveXL successfully merged
  `mod\gq000\localization\en-us\vo\gq000_01.json`, but failed to load the
  subtitle registration because `gq000_01.json` is a
  `localizationPersistenceSubtitleEntries` resource, while ArchiveXL's
  `localization.subtitles` merger expects a `localizationPersistenceSubtitleMap`.
  The missing RedHotTools hash `16106537288591666266` still does not match the
  registered VO map or first-line WEM path.
- Fixed/probe 2026-04-30: added
  `mod\gq000\localization\en-us\subtitles\gq000_01_subtitles_map.json`, a
  one-entry `localizationPersistenceSubtitleMap` pointing to
  `mod\gq000\localization\en-us\subtitles\gq000_01.json`, and updated
  `Ghostline.archive.xl` to register that map. Built
  `Ghostline_judy_scene_direct_empty_section_probe.zip`, which starts the first
  section with its `scnDialogLineEvent` removed, and
  `Ghostline_judy_scene_direct_dialogue_subtitle_map_probe.zip`, which repeats
  the direct-dialogue crash test with the corrected subtitle map registration.
- Runtime follow-up 2026-04-30: both the direct empty-section probe and the
  direct dialogue-with-subtitle-map probe still crash on approach. ArchiveXL
  now cleanly merges voiceover and subtitles, so the remaining fault is not
  localization or the `scnDialogLineEvent` itself. Built
  `Ghostline_judy_scene_empty_section_end_probe.zip` to test a bare section
  node that exits directly to scene end, and
  `Ghostline_judy_scene_direct_post_section_chain_probe.zip` to test the
  post-section Xor -> journal -> mappin -> choice chain without entering a
  section first.
- Runtime follow-up 2026-04-30: both
  `Ghostline_judy_scene_empty_section_end_probe.zip` and
  `Ghostline_judy_scene_direct_post_section_chain_probe.zip` still crash on
  approach. This keeps the fault inside scene node activation, not the
  specific dialogue event, subtitle/VO registration, or mappin branch.
- Diagnostic 2026-04-30: built a lower-level scene probe matrix:
  `Ghostline_judy_scene_xor_end_probe.zip` (`Start -> Xor -> End`),
  `Ghostline_judy_scene_journal_end_probe.zip` (`Start -> Journal -> End`),
  `Ghostline_judy_scene_empty_section_no_actors_end_probe.zip`
  (`Start -> empty Section -> End` with no actor behaviors),
  `Ghostline_judy_scene_empty_section_player_only_end_probe.zip`, and
  `Ghostline_judy_scene_empty_section_patch_only_end_probe.zip`. Test in that
  order to separate generic non-End scene-node activation, embedded quest-node
  activation, and section actor binding.
- Checked 2026-04-30: extracted and serialized `mq003_01_homeless.scene` and
  `mq003_03_orbital_pod.scene` from the local game archives. Vanilla `mq003`
  does use direct `Start -> Section -> End` chains, so that graph shape is
  valid in principle. The current Ghostline scene still carries many unrelated
  SQ026/MQ055/player cinematic animation resource references from the template;
  prune those in a follow-up resource-minimal probe if non-section nodes do not
  isolate the crash.
- Diagnostic 2026-04-30: built
  `Ghostline_judy_scene_xor_end_min_resources_probe.zip` and
  `Ghostline_judy_scene_empty_section_no_actors_min_resources_probe.zip`.
  These are the same graph probes as above, but all actor animation-set lists
  and scene resource reference lists are emptied. Use them after the normal
  `xor_end` / `empty_section_no_actors` tests if those still crash or produce
  the unknown resource-hash warnings.
- Runtime follow-up 2026-04-30:
  `Ghostline_judy_scene_xor_end_probe.zip`,
  `Ghostline_judy_scene_empty_section_no_actors_end_probe.zip`,
  `Ghostline_judy_scene_xor_end_min_resources_probe.zip`, and
  `Ghostline_judy_scene_empty_section_no_actors_min_resources_probe.zip`
  crash. `Ghostline_judy_scene_journal_end_probe.zip` works and starts the
  Ghostline journal entry. `Ghostline_judy_scene_empty_section_player_only_end_probe.zip`
  and `Ghostline_judy_scene_empty_section_patch_only_end_probe.zip` do not
  crash but have no visible payload. Current read: embedded quest nodes are
  safe, single-input `Xor` is unsafe, and a section with no actor behavior is
  unsafe; single-actor empty sections are safe.
- Diagnostic 2026-04-30: built
  `Ghostline_judy_scene_hub_end_probe.zip` to check whether `Hub` can replace
  the crashing `Xor`, `Ghostline_judy_scene_patch_only_dialogue_end_probe.zip`
  and `Ghostline_judy_scene_player_only_dialogue_end_probe.zip` to test
  single-actor dialogue line sections, `Ghostline_judy_scene_patch_only_dialogue_no_resources_end_probe.zip`
  to repeat Patch's line without inherited scene animation resource tables,
  and `Ghostline_judy_scene_direct_journal_mappin_choice_no_xor_probe.zip` to
  test the post-intro journal/mappin/choice chain without `Xor`.
- Runtime follow-up 2026-04-30: all five probes above crashed on approach.
  Treat the `Hub` result as inconclusive because the probe only changed the
  node type and did not rebuild the node with a verified vanilla `scnHubNode`
  shape; a single-input `Xor` remains suspect and should be avoided unless a
  vanilla-compatible use is copied. Dialogue sections still crash even with
  one actor, no inherited scene resources, and no post-dialogue `Xor`, so the
  next dialogue-specific probe should replace the generated max-int
  `scnSceneEventId` values on `scnDialogLineEvent`s with normal unique IDs.
  The combined journal/mappin/choice probe crashing does not contradict the
  working `Journal 15 -> End` probe; isolate `Journal 16`, `MappinManager`,
  and `Choice` independently.
- Diagnostic 2026-04-30: built the follow-up probe set:
  `Ghostline_judy_scene_patch_dialogue_fixed_event_ids_probe.zip`
  (`Start -> Patch-only dialogue section -> End` with normal unique dialogue
  event IDs),
  `Ghostline_judy_scene_player_dialogue_fixed_event_ids_probe.zip`
  (`Start -> V-only dialogue section -> End` with normal unique dialogue event
  IDs),
  `Ghostline_judy_scene_patch_dialogue_fixed_event_ids_no_resources_probe.zip`
  (same Patch dialogue path with inherited scene animation resource tables
  stripped),
  `Ghostline_judy_scene_journal16_end_probe.zip`
  (`Start -> Journal 16 -> End`),
  `Ghostline_judy_scene_mappin_end_probe.zip`
  (`Start -> MappinManager 17 -> End`), and
  `Ghostline_judy_scene_choice_end_probe.zip`
  (`Start -> Choice 8 -> End`, with all choice outputs redirected to End).
  Graph verification confirms the active paths are isolated and the dialogue
  probes no longer contain max-int `scnDialogLineEvent` IDs.
- Runtime follow-up 2026-04-30:
  `Ghostline_judy_scene_mappin_end_probe.zip` works and shows the map pin.
  `Ghostline_judy_scene_patch_dialogue_fixed_event_ids_no_resources_probe.zip`
  works: the line plays and the subtitle appears. The other probes in this
  batch crash: `journal16_end`, `choice_end`, `patch_dialogue_fixed_event_ids`,
  and `player_dialogue_fixed_event_ids`. Current read: dialogue needs both
  normal unique `scnDialogLineEvent` IDs and stripped inherited scene resource
  tables; `Journal 16` should not be activated directly; `MappinManager 17`
  is valid; `Choice 8` still has a bad node shape.
- Checked 2026-04-30: vanilla `mq003` choice nodes use `options + 6`
  `outputSockets` entries. Current Ghostline choice nodes only have one output
  socket per option. Build padded-choice probes before treating choice
  activation itself as unsafe. Also test whether the vanilla-style description
  journal node works only when preceded by the objective activation, because
  mq003 chains objective journal -> description journal -> mappin.
- Diagnostic 2026-04-30: built
  `Ghostline_judy_scene_journal15_journal16_end_probe.zip`
  (`Start -> Journal 15 objective -> Journal 16 description -> End`),
  `Ghostline_judy_scene_intro_journal15_mappin_end_probe.zip`
  (`Start -> fixed/no-resource Patch dialogue -> Journal 15 -> MappinManager
  17 -> End`, skipping the description node),
  `Ghostline_judy_scene_choice_padded_clear_persistent_end_probe.zip`
  (`Start -> padded Choice 8 -> End`, with persistent line events cleared),
  `Ghostline_judy_scene_intro_choice_padded_clear_persistent_end_probe.zip`
  (`Patch dialogue -> padded Choice 8 -> End`, persistent line events cleared),
  `Ghostline_judy_scene_intro_choice_padded_persistent_event_end_probe.zip`
  (`Patch dialogue -> padded Choice 8 -> End`, persistent line events pointed
  at the intro line event), and
  `Ghostline_judy_scene_intro_journal15_mappin_choice_padded_persistent_event_end_probe.zip`
  (minimal full spine with fixed/no-resource dialogue, objective journal,
  mappin, padded choice, and no description journal node). Verification shows
  Choice 8 now has 3 options and 9 output sockets in the padded variants.
- Runtime follow-up 2026-04-30:
  `Ghostline_judy_scene_intro_journal15_mappin_end_probe.zip` works and plays
  dialogue, starts the quest/journal entry, and triggers the mappin.
  `Ghostline_judy_scene_journal15_journal16_end_probe.zip` works, confirming
  Journal 16 is safe when preceded by the objective journal node. The padded
  choice variants with `persistentLineEvents` cleared work, but the first
  option is hidden and the visible options show the default `Db-db` side label.
  Both variants that repopulate `persistentLineEvents` crash, so keep scene
  choice `persistentLineEvents` empty for now.
- Checked 2026-04-30: vanilla `mq003` choice locstrings are stored in-scene
  in `locStore`, and each tested choice locstring has an `en_us` embedded
  variant in addition to `db_db` entries. Ghostline's generated choice strings
  only had `db_db` variants. Vanilla optional/info choices also use
  `type.properties: 0` with `isSingleChoice: 0`; Ghostline was using
  `isSingleChoice: 1` for optional choices. Built
  `Ghostline_judy_scene_choice_dialogue_fixed_labels_end_probe.zip`,
  `Ghostline_judy_scene_intro_choice_dialogue_fixed_labels_end_probe.zip`, and
  `Ghostline_judy_scene_intro_journal15_mappin_choice_dialogue_fixed_labels_end_probe.zip`
  to test `en_us` choice locStore variants, desired intro choice ordering
  (`What's the job?`, `Why me?`, `Ghostline?`), blue/info-style optional
  flags, vanilla-style padded choice sockets, and empty persistent line events.
- Runtime follow-up 2026-04-30:
  `Ghostline_judy_scene_choice_dialogue_fixed_labels_end_probe.zip` crashes,
  so do not continue with the combined fixed-label probes from that batch.
  In those probe names, `clear` referred specifically to clearing
  `persistentLineEvents`; it did not mean stripping inherited scene animation
  resource tables. Built a narrower one-change-at-a-time choice probe set:
  `Ghostline_judy_scene_choice_clear_recheck_end_probe.zip` recreates the
  known-good padded/cleared choice shape with legacy duplicate dummy sockets,
  `Ghostline_judy_scene_choice_clear_vanilla_socket_stamps_end_probe.zip`
  changes only dummy socket stamps to the vanilla-style `1:0` through `6:0`
  sockets, `Ghostline_judy_scene_choice_clear_en_us_locstore_only_end_probe.zip`
  changes only choice locStore coverage by adding `en_us` variants,
  `Ghostline_judy_scene_choice_clear_reorder_only_end_probe.zip` changes only
  intro choice ordering/captions, and
  `Ghostline_judy_scene_choice_clear_optional_flags_only_end_probe.zip`
  changes only optional-choice flags.
- Runtime follow-up 2026-04-30:
  `Ghostline_judy_scene_choice_clear_recheck_end_probe.zip` works as before.
  `Ghostline_judy_scene_choice_clear_en_us_locstore_only_end_probe.zip` works
  and removes the `Db-db` side label for the first visible option, but the
  remaining visible options still show shifted/default labels. The optional
  flag batch, physical option-array reorder, and vanilla dummy socket stamps
  all crash. Current read: keep the original choice option array and legacy
  duplicate dummy socket stamps; display order is likely tied to the stable
  `scnscreenplayItemId` sequence rather than a freely reorderable node array.
  Built follow-up probes for item-id remapping without option-array reorder,
  alternative `en_us` locStore layouts, and split optional flag tests
  (`isSingleChoice` only vs `type.properties` only).
- Runtime follow-up 2026-04-30: `choice_clear_item_id_remap_order_only`
  displays `What's the job?` first, then `Ghostline?`, then a blank option;
  `choice_clear_en_us_interleaved_only` crashes;
  `choice_clear_en_us_replace_locale_only` works and removes the `Db-db`
  label, but `Why me?` is still blank/missing; `choice_clear_single_zero_only`
  crashes; `choice_clear_properties_zero_only` works and makes the side
  choices blue/optional, with `What's the job?` promoted first, but the
  `Why me?` option remains blank. Current rule set: do not change
  `isSingleChoice`; use `type.properties: 0` for optional/blue choices; replace
  `db_db` with `en_us` rather than appending/interleaving new locale records;
  avoid physical choice-array reorder. Built three follow-up probes combining
  the safe pieces and isolating whether the blank `Why me?` is tied to its
  locstring id or item id.
- Runtime follow-up 2026-04-30:
  `choice_clear_en_us_replace_properties_zero_new_why_loc` displays the intro
  choice with no `Db-db` label, the desired progression option first, and all
  three choice labels visible. Changing only the `Why me?` choice locstring
  from `2326126148155397709` to `13264671179261890561` fixes the missing label
  while keeping item id `258`; changing the item id crashes. Extracted and
  serialized the installed base and EP1 `lang_en_text.archive` files and found
  no vanilla entry with either numeric string id. Vanilla does contain exact
  `Why me?` subtitle text under other string ids, so the old Ghostline id is
  confirmed bad for this scene shape but not confirmed to collide with a
  vanilla localization id.
- Diagnostic 2026-04-30: built the next probe batch:
  `Ghostline_judy_scene_section3_ghostline_fixed_ids_no_resources_end_probe.zip`,
  `Ghostline_judy_scene_section4_why_fixed_ids_no_resources_end_probe.zip`,
  and `Ghostline_judy_scene_section5_job_fixed_ids_no_resources_end_probe.zip`
  directly start the three intro-choice response sections with normal dialogue
  event ids and stripped inherited scene resource tables. Built matching
  full-spine probes
  `Ghostline_judy_scene_intro_journal15_mappin_choice_stable_new_why_loc_ghostline_section_end_probe.zip`,
  `Ghostline_judy_scene_intro_journal15_mappin_choice_stable_new_why_loc_why_section_end_probe.zip`,
  and `Ghostline_judy_scene_intro_journal15_mappin_choice_stable_new_why_loc_job_section_end_probe.zip`
  to route one stable choice option into the corresponding response section
  while other options end the scene. Also built
  `Ghostline_judy_scene_yolo_main_scene_all_known_fixes_probe.zip`, which
  applies all known safe fixes to the main scene flow: normal dialogue event
  ids, stripped inherited scene resource tables, no `Xor` handoff after the
  intro, `en_us` scene choice locStore descriptors, fresh `Why me?` locstring
  id, empty `persistentLineEvents`, legacy padded choice sockets, and
  optional-choice `type.properties: 0`.
- Runtime follow-up 2026-04-30:
  `Ghostline_judy_scene_yolo_main_scene_all_known_fixes_probe.zip` does not
  crash, but also does not show the intro dialogue, choice, or mappin. Treat
  that as an invalid main-flow probe because it kept the original scene start
  path into the generated pre-dialogue gate instead of forcing the already
  proven intro/journal/mappin spine. The direct section probes for section 3
  and section 4 both crash; section 5 was not tested because the earlier
  response sections already failed. In the full-spine probes, routing into the
  Ghostline branch crashes after the intro subtitle appears, while routing into
  `Why me?` or `What's the job?` shows the stable choice and then crashes when
  that response is selected. Current interpretation: the stable intro,
  journal, mappin, and choice setup is good; the fault follows response-section
  dialogue events. Since these response sections start with V/player dialogue
  events, the next probe batch should split player-line handling from section
  shape by testing Patch-only response replies, V-only response lines, and
  mq003-style player actor naming/id variants.
- Diagnostic 2026-04-30: built the response-section isolation batch:
  `Ghostline_judy_scene_section3_patch_reply_only_fixed_ids_no_resources_end_probe.zip`,
  `Ghostline_judy_scene_section4_patch_reply_only_fixed_ids_no_resources_end_probe.zip`,
  and `Ghostline_judy_scene_section5_patch_replies_only_fixed_ids_no_resources_end_probe.zip`
  keep only Patch-authored reply lines from the response sections, rebase the
  kept event timing to zero, strip inherited resource tables, and end the scene.
  Built `Ghostline_judy_scene_section3_v_only_fixed_ids_no_resources_end_probe.zip`,
  `Ghostline_judy_scene_section3_v_only_player_name_fixed_ids_no_resources_end_probe.zip`,
  and `Ghostline_judy_scene_section3_v_only_actor3_fixed_ids_no_resources_end_probe.zip`
  to isolate whether the V/player line crash follows player naming or
  actor-id wiring. Built
  `Ghostline_judy_scene_section3_v_line_patch_intro_loc_player_speaker_fixed_ids_no_resources_end_probe.zip`,
  `Ghostline_judy_scene_section3_v_line_as_patch_speaker_fixed_ids_no_resources_end_probe.zip`,
  and
  `Ghostline_judy_scene_section3_v_line_patch_intro_loc_as_patch_speaker_fixed_ids_no_resources_end_probe.zip`
  to separate the V line's speaker identity from the specific V locstring/VO
  resource. Also rebuilt the yolo probe as
  `Ghostline_judy_scene_yolo_main_scene_start_intro_all_known_fixes_probe.zip`,
  which now starts directly at the proven intro section and then chains
  Journal 15 -> mappin -> stable intro choice instead of entering the original
  generated pre-dialogue gate. These probes were packed from the `mod\...`
  namespace only, matching the recent scene probe size and avoiding the
  `source/archive/base` overrides.
- Runtime follow-up 2026-04-30: the response-section isolation batch shows the
  problem is not limited to V/player actor lookup. Section 3 Patch-only and
  section 5 Patch-only reply probes display the subtitle and begin dialogue,
  then crash. Section 4 Patch-only crashes outright. All V-only and
  player-name/player-id variants crash. Retargeting the section 3 V event to
  Patch with the known working intro locstring displays the intro subtitle and
  then crashes. The yolo v2 main-flow probe crashes as soon as it reaches the
  full scene path. Current read: the original section 2 intro line/event shape
  remains the only proven dialogue payload; non-intro response section nodes or
  their screenplay item/event/resource wiring still contain a crash surface.
  Next probes should clone the exact working intro event and/or screenplay item
  into response sections, then test response line item ids in the known-good
  section 2 shell.
- Checked/diagnostic 2026-04-30: mq003 uses spoken screenplay line item ids
  `1, 257, 513, ...` while player choice item ids occupy the adjacent
  `2, 258, 514, ...` slots. Ghostline's choice ids already follow the vanilla
  pattern, but its spoken line ids were `0, 256, 512, ...`; only the special
  intro item `0` had been proven safe. Built a vanilla-item-id probe batch that
  remaps spoken lines to `1 + 256n` and leaves choice ids unchanged:
  `Ghostline_judy_scene_section2_intro_vanilla_item_ids_no_resources_end_probe.zip`,
  `Ghostline_judy_scene_section2_patch_rsp_ghostline_in_intro_shell_vanilla_item_ids_no_resources_end_probe.zip`,
  `Ghostline_judy_scene_section3_patch_reply_vanilla_item_ids_no_resources_end_probe.zip`,
  `Ghostline_judy_scene_section4_patch_reply_vanilla_item_ids_no_resources_end_probe.zip`,
  `Ghostline_judy_scene_section5_patch_replies_vanilla_item_ids_no_resources_end_probe.zip`,
  `Ghostline_judy_scene_section3_v_only_vanilla_item_ids_no_resources_end_probe.zip`,
  `Ghostline_judy_scene_section3_full_vanilla_item_ids_no_resources_end_probe.zip`,
  and
  `Ghostline_judy_scene_yolo_main_scene_start_intro_all_known_fixes_vanilla_item_ids_probe.zip`.
  This is now the leading hypothesis for the dialogue crash.
- Runtime follow-up 2026-04-30: vanilla spoken item ids are not a broad fix.
  `section2_intro_vanilla_item_ids` crashes, so item `0 -> 1` breaks the
  previously safe intro line. `section2_patch_rsp_ghostline_in_intro_shell`
  plays the non-intro Patch response and shows its subtitle from inside the
  section 2 shell, which proves the response locstring/VO can play when routed
  through a known-good section/event shell. `section3_patch_reply_vanilla_item_ids`
  shows a subtitle and then crashes; `section4_patch_reply_vanilla_item_ids`
  crashes outright; `section5_patch_replies_vanilla_item_ids` plays and shows a
  subtitle, then crashes. The V-only, full section 3, and yolo vanilla probes
  still crash. Current read: the crash is not just VO/subtitle or player actor
  lookup. It likely involves response section node state, response section
  completion/output handling, or hidden section/event metadata around the
  response nodes. Potential next steps are:
  - Use section 2 as the safe shell and swap only one response line at a time,
    ending immediately, to validate all response audio/text payloads.
  - Clone the entire working section 2 node to new node ids for branches,
    changing only the screenplay line id and output destination, instead of
    reusing generated response section nodes 3-7.
  - Compare section 2 and response sections for hidden CR2W fields not exposed
    by the explorer, including `sectionDuration`, output socket count/stamps,
    actor behavior arrays, and editor/debug symbol references.
  - If cloned section-2 shells work, rebuild the main dialogue using cloned
    minimal section nodes and leave the generated response sections unused.
- Checked 2026-04-30: missing hashes `16106537288591666266` and
  `14413217326793937713` do not match FNV1A64 hashes of Ghostline raw
  `ResourcePath`, `NodeRef`, or string values, including expanded local
  `$/mod/gq000/#gq000_pr_patch_meet/#...` NodeRefs. WolvenKit also could not
  extract those hashes from the local base, EP1, or installed mod archives.
  This suggests they are not one of the explicit `#` NodeRefs in Ghostline
  source.
- Checked 2026-04-30: compared the earlier Judy scene-community always-loaded
  sector with the current inactive-community always-loaded sector. The static
  marker NodeRef and position are unchanged; the only serialized difference is
  the community entry's `entryActiveOnStart` value changing from `1` to `0`.
  The current missing map icon therefore does not appear to be caused by a
  changed marker resource.
- Diagnostic 2026-04-30: added a dedicated always-loaded map-pin marker
  `#gq000_01_mp_patch_bridge` and moved both the `gq000` quest map pin and the
  point-of-interest static mappin from `#gq000_01_sm_patch_bridge` to the new
  marker. This matches the mq003 pattern where scene markers and map-pin
  markers are separate NodeRefs. Built `Ghostline_judy_mp_marker_probe.zip` for
  runtime validation.
- Packed generated world resources were deserialized with WolvenKit.CLI 8.17.4
  and verified to start with `CR2W`.
- Remaining in-game validation:
  - Confirm ArchiveXL loads the streaming block.
  - Confirm every quest/scene NodeRef resolves in game.
  - Tune Patch facing, workspot placement, and trigger radii if the chosen
    location geometry needs tighter volumes.
  - If Patch still crashes when streamed, audit/replace the remaining
    `ep1\...` animation and effect dependencies in
    `mod\ghostline\characters\patch\patch.ent` or explicitly require Phantom
    Liberty for the mod.

### Generated/editor support data

- `generated` contains older generated snapshots. Prefer `source/raw` when changing CR2W assets.
- `GraphEditorStates` contains WolvenKit editor layout state only. Do not treat it as packed game data.
- Helper tools exist for inspection:
  - `tools/explore_questphase.py`
  - `tools/explore_scene.py`
  - `tools/explore_localization.py`
  - `tools/explore_ent_app.py`
  - `tools/explore_journal.py`

### Packaging audit

- Checked 2026-04-29: `WolvenKit.CLI build .` exits successfully but is not a
  safe packaging command for this repo layout. It packed repo support paths such
  as `reference`, `source/raw`, `generated`, `GraphEditorStates`, `tools`, and
  `modding_docs` into the archive before the bad test artifact was deleted.
- A scoped pack from `source/archive` produces a clean archive namespace with
  only `base\...`, `mod\gq000\...`, and `mod\ghostline\...` depot paths:
  `WolvenKit.CLI pack .\source\archive -o <out>`.
- A minimal installable test layout still needs the scoped archive copied or
  renamed to `Ghostline.archive` under
  `Cyberpunk 2077\archive\pc\mod`, plus `Ghostline.archive.xl` copied to the
  same directory. TweakXL YAML files from `source/resources\r6\tweaks` install
  under `Cyberpunk 2077\r6\tweaks\Ghostline`.

## Resolved World References

### Quest phase prefab NodeRef

The current `#gq000_pr_patch_meet` references in `gq000.questphase` and
`gq000_patch_meet.questphase` are now backed by a Ghostline-owned streaming
block and quest sector.

Resolved understanding from `reference/world/000` and the generated Ghostline
world data:

- Local quest docs say questphase `#` NodeRefs can be used to load prefabs for
  the phase.
- Local streamingsector docs say NodeRef aliases are registered through sector
  `nodeRefs` and linked to node instances through `QuestPrefabRefHash`.
- `reference/world/000/blocks/all.streamingblock.json` shows the missing
  world-side root binding: each quest sector descriptor has a
  `questPrefabNodeRef` absolute NodeRef ending in the prefab root alias, e.g.
  `$/03_night_city/.../#mq003_pr_homeless`.
- `reference/world/000/quest_606b61008df2ba6f.streamingsector.json` registers
  child refs under the same prefab root in `nodeRefs`, and each concrete node's
  `nodeData.QuestPrefabRefHash` points at the corresponding absolute child
  NodeRef, e.g. `.../#mq003_pr_homeless/#mq003_tr_engage_homeless`.
- `phasePrefabs` is the questphase-level prefab dependency/declaration list.
  Any questphase resource that directly uses `#gq000_pr_patch_meet` should list
  it there.
- `phaseInstancePrefabs` is the per-`questPhaseNodeDefinition` activation list
  for inline phase nodes. In `gq000.questphase`, phase node id `2` directly
  waits on `#gq000_01_tr_setup` and operates on `#gq000_01_com_patch_bridge`,
  so its `phaseInstancePrefabs` should keep `#gq000_pr_patch_meet`.
- Parent phase node id `3` only loads
  `mod\gq000\phases\gq000_patch_meet.questphase`; it does not need a duplicate
  `phaseInstancePrefabs` entry because the child questphase has its own root
  `phasePrefabs`.
- `gq000_patch_meet.streamingblock` creates the required world-side root
  binding with `questPrefabNodeRef: $/mod/gq000/#gq000_pr_patch_meet`.
- `gq000_patch_meet.streamingsector` registers these child refs under that
  prefab root and assigns matching `nodeData.QuestPrefabRefHash` values:
  - `#gq000_01_sm_patch_bridge`
  - `#gq000_01_tr_setup`
  - `#gq000_01_tr_engage`
  - `#gq000_01_tr_bridge_case_mood`
  - `#gq000_01_tr_someone_coming`
  - `#gq000_01_spot_patch_bridge`
  - `#gq000_01_com_patch_bridge`
- Keep current `phasePrefabs` and phase node id `2` `phaseInstancePrefabs`
  entries unless in-game validation shows the parent root phase loads too much
  too early.

Completed 2026-04-28:

- Removed the leftover `#mq003_pr_corpse` root prefab from `gq000.questphase`.
- Replaced remaining `#mq003_pr_homeless` root prefab references with
  `#gq000_pr_patch_meet`.
- Resolved the root-vs-instance prefab question using the deserialized
  `reference/world/000` streaming block and quest sector.

Completed 2026-04-29:

- Added the production `gq000_patch_meet` world spec, quest sector, always-loaded
  registry sector, and streaming block.
- Registered the block in `source/resources/Ghostline.archive.xl`.
- Generated packed CR2W resources for the new world files.
- Verified the generated raw world files with `tools/explore_world.py` and
  confirmed packed world resources start with `CR2W`.
- Added `always_loaded_node_refs` support to `tools/generate_world.py` and
  registered the Patch bridge static marker in the always-loaded sector for
  journal mappin resolution.
- Updated `tools/generate_world.py` so markers can be emitted directly into the
  always-loaded sector with `markers[].sector = "always_loaded"`. The
  production `gq000_patch_meet` spec now uses that shape for the Patch bridge
  marker.

## Next Milestones

### 1. Make all current packed assets inspectable (complete 2026-04-28)

- Serialized `gq000.questphase` into `source/raw/mod/gq000/phases/gq000.questphase.json`.
- Serialized `patch.ent` and `patch.app` into `source/raw/mod/ghostline/characters/patch`.
- Added `tools/explore_ent_app.py` for `.ent` and `.app` inspection.
- Re-ran the questphase, scene, localization, and ent/app explorers and updated the current notes above.

### 2. Add journal and quest UI data

- Completed 2026-04-28.
- Created `gq000` journal and quest onscreen localization resources in raw and packed form.
- Registered both `journal:` and quest onscreens in `source/resources/Ghostline.archive.xl`.
- Updated scene and questphase journal paths to full journal hierarchy paths.
- Added `tools/explore_journal.py` and documented first-dot `.journal` reference prefixes in `agent/skills/ghostline-quest-journal-scene/SKILL.md`.
- Docs checked:
  - `modding_docs/modding-guides/quest/how-to-add-new-text-messages-thread-to-cyberpunk-2077.md`
  - `modding_docs/modding-guides/quest/creating-custom-shards.md`
  - `modding_docs/for-mod-creators-theory/files-and-what-they-do/file-formats/translation-files-.json.md`

### 3. Validate the meeting-location world data

- Completed source/resource generation 2026-04-29.
- Test in game that ArchiveXL registers `mod\gq000\world\gq000_patch_meet.streamingblock`.
- Confirm the scene marker, setup trigger, engage trigger, case-mood trigger,
  someone-coming trigger, and Patch community NodeRefs all resolve.
- Tune Patch yaw/workspot offset and trigger radii against the real location
  geometry after the first in-game pass.

### 4. Extend the quest beyond acceptance

- Add the next quest phase after `job_accept`.
- Define facts with `gq000_` prefixes for accepted job state, cache acquired, cache delivered, and quest completion.
- Add objective updates, mappin changes, and failure/completion branches.
- Confirm prefab NodeRef lifecycle against base-game questphases and replace any
  remaining placeholder/base references with Ghostline-owned resources where needed.

### 5. Validate audio packaging

- Wwise `.wem` files have been generated for the current WAV voice lines referenced by the VO map.
- Add lipsync resources if the chosen scene presentation requires them.
- Validate in game that subtitles, VO map, and audio assets remain aligned after any dialogue edits.

### 6. Pack and test in game

- Deserialize updated raw CR2W-JSON into `source/archive`.
- Confirm packed CR2W files start with `CR2W`.
- Pack from `source/archive`, not from the repo root, then copy
  `source/resources\Ghostline.archive.xl` to
  `Cyberpunk 2077\archive\pc\mod` and
  `source/resources\r6\tweaks\ghostline` to
  `Cyberpunk 2077\r6\tweaks\Ghostline`.
- Check:
  - `Cyberpunk 2077\red4ext\plugins\ArchiveXL\ArchiveXL.log`
  - TweakXL load output
  - in-game Patch spawn
  - trigger progression
  - journal and mappin visibility
  - subtitles and voice playback

## Useful Commands

```powershell
py .\tools\explore_questphase.py summary
py .\tools\explore_questphase.py refs
py .\tools\explore_scene.py summary
py .\tools\explore_scene.py refs --kind NodeRef
py .\tools\explore_scene.py refs --kind journal_path
py .\tools\explore_localization.py check
py .\tools\explore_ent_app.py summary
py .\tools\explore_ent_app.py appearances
py .\tools\explore_ent_app.py components --resources-only
py .\tools\explore_ent_app.py refs --kind ResourcePath
py .\tools\explore_journal.py prefixes --with-types
py .\tools\explore_journal.py -f .\source\raw\mod\gq000\journal\gq000.journal.json summary
py .\tools\explore_journal.py -f .\source\raw\mod\gq000\journal\gq000.journal.json tree --max-depth 6
py .\tools\explore_world.py summary
py .\tools\explore_world.py blocks
py .\tools\explore_world.py nodes --type TriggerArea --limit 0
py .\tools\explore_world.py communities
py .\tools\generate_world.py generate --spec .\tools\gq000_world_spec.example.json --dry-run
py .\tools\generate_world.py hash "$/mod/npcac/#npcac_spot"
.\tools\serialize_reference_world.ps1
.\tools\convert_wavs_to_wem.ps1
```
