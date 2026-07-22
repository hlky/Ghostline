# Ghostline Roadmap

Last audited: 2026-07-22

This file tracks the current state and the next work needed to turn `gq000`
from a dialogue prototype into a playable quest slice. The current 2026-07-22
custom Patch candidate is based on the runtime-proven repaired world,
mq003-sequenced meeting lifecycle, shared-lipsync-slot baseline, and sorted
choice locStore. The first custom-character run proved TweakXL registration,
Patch naming, scene acquisition, and the repaired first choice group, but the
actor was invisible because the community requested the internal `.app` name.
The current candidate fixes the root/community appearance namespace. Runtime
retest confirms Patch is visible with the reviewed design and all three first
choice labels display; the second group and cache handoff remain the focused
completion checks.
Detailed command usage, runtime flow, crash conclusions,
world-reference notes, and packaging instructions now live in focused docs:

- `docs/quest-scene-flow.md`
- `docs/tooling.md`
- `docs/testing.md`
- `docs/scene-authoring-rules.md`
- `docs/crash-investigation.md`
- `docs/world-references.md`
- `docs/packaging.md`

## Current Status

### Current Custom Patch Candidate

- The first synchronized current-raw build crashed after accepting the meeting
  with `On my way` and fast travelling near the bridge. The dump recorded
  `Loading world`, resource throttling in `Flood`, and an invalid allocator
  pointer on `redDispatcher20`; plugin logs showed no Ghostline registration or
  merge error.
- The first repair allowed the nearby fast travel to finish, but both a normal
  approach and a deliberately slow retry then crashed at the 10-unit engage
  boundary while the game was fully loaded. Both dumps failed at
  `Cyberpunk2077+0x1d173be` before dialogue visualization began.
- Moving scene launch to the 90-unit setup boundary moved the same
  `Cyberpunk2077+0x1d173be` failure to 89.27 horizontal units from the scene
  origin. This rules out the engage trigger itself and ties the failure to
  scene initialization.
- The current candidate inherits the audited `mq003` lifecycle instead of
  launching the scene at engage range: activate and validate the community
  first, launch the scene from the broad setup gate, then let the running scene
  progress through case-mood, someone-coming, opening line, and engage gates.
  It additionally assigns both the Patch-role actor and V to
  lipsync slot `0` and emits one generic lipsync reference. This is a
  diagnostic cardinality probe, not the intended final lipsync design. The
  newer root phone flow and post-accept cache phase remain unchanged.
- Runtime testing of that slot-0 build completed the full route without a
  crash: phone message, nearby fast travel, normal bridge approach, all spoken
  dialogue/subtitles/VO, `job_accept`, meet-objective cleanup, and activation
  of the cache objective and its 275-metre marker all worked.
- The same test exposed one remaining scene UI defect. In the first three-row
  choice group only `Ghostline?` displayed; the other two rows were blank. In
  the second group `I'm in.` displayed correctly, while `Who's behind it?`
  incorrectly resolved to `Why me?`. All choice payloads exist, so this is an
  embedded locStore lookup-order defect rather than missing localization.
- The world baseline keeps the proven 12-unit trigger height, restores
  horizontal radii `90/10/60/20`, and gives the always-loaded registry node a
  distinct global ID instead of reusing the streamed community area's ID.
- All 58 Python regression tests pass. The meeting phase and scene also
  pass exact WolvenKit 8.17.4 serialize/deserialize SHA-256 round trips. Their
  respective SHA-256 hashes are
  `A07A6DA858EFE86E5C9984395E7A933D3C5081D2CBB619AD423C9FAF67BDD5FB`
  and
  `9DDFD4F05344B11206820414D6D9A9B0854CC570D9AC0EBAA751AF91CE2EA303`.
- The rebuilt archive contains 173 verified entries from 176 files under
  `source/archive`. The only exclusions are the Patch `.tmp` file and the two
  Patch head readmes that WolvenKit does not pack.
- Compared with the invisible-actor custom Patch archive, exactly two payloads
  changed: Patch's root `.ent` and the always-loaded sector. Both now use the
  exposed root appearance name `ghostline_patch_default`; `default` remains the
  internal `.app` definition name. No depot paths were added or removed.
- The candidate archive, staged archive, and installed game archive all have
  SHA-256
  `40148CE9F102C5CF77BEA31C1D9043FB20F53B8937873235BDBE3D1A82EF6786`.
  `Ghostline.zip` was rebuilt from the six-file `packed` tree, has SHA-256
  `890166AA958650A537BCCA32B9B91214E139C3C4FBDF51AC431EF965668D7162`,
  and every ZIP payload matches its packed source.
- Build, extraction, and comparison evidence is retained at
  `H:\Ghostline-builds\patch-appearance-name-fix-20260722-130000`. The exact
  invisible-actor install is backed up at
  `H:\Ghostline-backups\pre-patch-appearance-name-fix-20260722-130000`.
- The crashing synchronized package is retained at
  `H:\Ghostline-backups\pre-stability-fix-20260721-224252`. The earlier
  pre-sync package remains at
  `H:\Ghostline-backups\stabilize-5b8449d-sync-20260721-214058`.
- The archive currently contains 93 `base\...` global overrides and 80
  `mod\...` assets. The global overrides remain a packaging risk pending
  validation. It also carries 26 valid WEM files while the VO map references
  13 of them.
- The local game install has ArchiveXL and official TweakXL 1.11.3. TweakXL was
  installed immediately before this candidate and has not yet been exercised
  by a game launch, so its load log and Patch record registration remain part
  of the focused runtime test.

### Project Registration

`source/resources/Ghostline.archive.xl` currently registers:

- `mod\gq000\phases\gq000.questphase` as a root questphase under
  `base\quest\cyberpunk2077.quest`.
- `mod\gq000\journal\gq000.journal`.
- Generic onscreen localization at
  `mod\ghostline\localization\en-us\onscreens\ghostline.json`.
- Quest onscreen localization at
  `mod\gq000\localization\en-us\onscreens\gq000.json`.
- Subtitle map `mod\gq000\localization\en-us\subtitles\gq000_01_subtitles_map.json`.
- VO map `mod\gq000\localization\en-us\vo\gq000_01.json`.
- Streaming block `mod\gq000\world\gq000_patch_meet.streamingblock`.

### Patch Character

- Patch has packed resources under
  `source/archive/mod/ghostline/characters/patch`, including `patch.ent`,
  `patch.app`, body/head meshes, textures, and morphtargets.
- Editable raw files exist for the root entity and appearance:
  - `source/raw/mod/ghostline/characters/patch/patch.ent.json`
  - `source/raw/mod/ghostline/characters/patch/patch.app.json`
- `source/resources/r6/tweaks/ghostline/character_patch.yaml` defines
  `Character.GhostlinePatch` with `entityTemplatePath:
  mod\ghostline\characters\patch\patch.ent`, display names using
  `gq_npc_patch`, `Factions.Ghostline`, and `voiceTag: gq_patch`.
- `source/resources/r6/tweaks/ghostline/faction_ghostline.yaml` defines
  `Factions.Ghostline`.
- `patch.ent` appearance `ghostline_patch_default` maps `appearanceName:
  default` to `mod\ghostline\characters\patch\patch.app`.
- Patch's `.app` head/body mesh components now point at real
  `mod\ghostline\characters\patch\...` depot paths instead of unresolved
  numeric `ResourcePath` IDs. The optional `h0_cyberware_face` mesh is disabled
  because its numeric mesh ID did not resolve to any packed game or mod
  resource.
- Patch's root mapping is named `ghostline_patch_default` and selects internal
  `.app` definition `default`. Runtime communities and `defaultAppearance`
  must use the root mapping name. The first custom run requested the internal
  name and produced an invisible but scene-acquirable puppet; generator/world
  regressions now enforce the correct namespace.
- Runtime retest of the corrected build confirms Patch renders at the bridge
  with the reviewed hair and outfit, participates in the scene, and presents
  all three first-menu labels correctly.
- Patch's root entity was compared with the downloaded NPV male template on
  2026-07-22. Both have the same 110 root components and, after excluding the
  intended appearance/default and export-timestamp fields, only those excluded
  fields differ. Treat the root as a versioned generator template rather than
  character-authored data.
- The NPV template's Blender file contains import, shape-key application, and
  export scripts. Blender 5.1 has Cyberpunk IO Suite 1.8.0 installed locally,
  and the complete headless round trip is now scripted and smoke-tested. The
  Patch subset exported 13 morphtarget GLBs, requested temporary shape value
  22, exported 13 mesh GLBs, rebuilt 13 CR2W meshes, and verified every header
  and hash in isolated temporary output. A later target-name audit proved that
  22 selects missing `h21` and is a geometry no-op; the current builder derives
  actual targets from GLB metadata and permits Basis/value 1 plus named values
  2 through 21.
- The local WebGL UI now renders Patch's real 100-target head, applies all five
  facial controls immediately, and preserves Blender for the final bake only.
  The default preview is the 25.7-MiB core head; optional layers are loaded only
  on request.
- The installed-game path index currently contains 4,965 records from base and
  EP1: 1,329 clothing, 1,528 hair, 1,772 head, 144 body, and 192 player-item
  appearance resources. The UI searches slot/frame/family/path metadata and
  successfully uncooked Patch's military boot to an isolated GLB preview. PMA
  torso, legs, and feet primary meshes are now selectable: the UI reads real
  appearances from the cooked mesh, records a canonical indexed override, and
  the generator updates both appearance component copies. Live QA assigned the
  military boot's `black_red` appearance and passed full manifest validation.
- Patch's reviewed design manifest now selects the black-carbon `hh_146` dread
  undercut, a `quest005_grey` high-collar shirt, `camo_black` computer cargo
  trousers, and the existing black/red military boots and braindance specs.
  The look follows the quest's low-profile signal-broker characterization:
  practical dark layers with the existing spiral eyes, magenta/rose face
  details, gold hardware, and red accents providing the deliberate flair.
- The curated `hh_146` option carries its vanilla animgraph, dangle rig, NPC
  shadow, component-class change, skinning target, and parent bindings. New
  binding handles are allocated after the template maximum; browser and CLI
  generation agree, and the resulting 105 handle IDs are unique. An isolated
  WolvenKit CR2W round trip preserved the complete bundle topology. The
  original Patch selections remain covered by a semantic-equivalence
  regression test.
- This reviewed design has been applied to `source/raw`, rebuilt into
  `source/archive`, packed, and installed. The indexed shirt and trousers still
  retain their original curated cuff/shadow companions, and the complete look
  needs focused in-game tests for fit, animation, LODs, scene use, and
  streaming.
- The 17 `ep1\...` string occurrences in Patch's root entity are identical to
  the downloaded male template. Resolve this at the reusable template layer or
  declare Phantom Liberty as a generated-character dependency.
- `docs/character-creation-pipeline.md` defines the manifest-driven generator,
  machine-readable catalogs, validation boundary, current local UI, and Patch
  migration plan.
- Packaging still has a risk: `source/archive/base` contains copied
  `base\characters\head\player_base_heads\player_man_average\...` resources
  that should not ship as global base-path overrides unless validated.

### Quest Phases

- Packed and raw questphase resources exist for:
  - `mod\gq000\phases\gq000.questphase`
  - `mod\gq000\phases\gq000_patch_meet.questphase`
  - `mod\gq000\phases\gq000_post_accept.questphase`
- `gq000.questphase` is now the staged root flow:
  `input -> phone start guard -> Patch phone message -> phone choice group ->
  wait for On my way reply -> meet objective/description/mappin ->
  gq000_patch_meet phase -> accepted-state check -> gq000_post_accept phase`.
- The root phase no longer starts the meeting objective from the bridge trigger
  and no longer sets `gq000_done`. Current staged facts include
  `gq000_phone_start_sent`, `gq000_phone_reply_on_my_way`,
  `gq000_job_accepted`, and `gq000_02_started`.
- The Patch phone message has been confirmed to trigger in game when tested
  from a fresh save.
- The current raw `gq000_patch_meet.questphase` is a 10-node, 10-edge flow:
  input -> activate community `patch/default` -> wait for `CharacterSpawned`
  on `#gq000_01_com_patch_bridge` -> wait for `#gq000_01_tr_setup` ->
  checkpoint -> start
  `mod\gq000\scenes\gq000_patch_meet.scene` at
  `#gq000_01_sm_patch_bridge`.
- Scene exit `end` terminates the meeting phase without acceptance. Scene exit
  `job_accept` succeeds `gq000_01_obj_meet_patch`, disables
  `gq000_01_qmp_patch_bridge`, sets `gq000_job_accepted = 1`, and then
  terminates. The root phase's accepted-state check then starts the current
  post-accept cache phase.
- `gq000_post_accept.questphase` is a minimal skeleton that activates/tracks
  `gq000_02_obj_reach_cache`, activates its description and
  `gq000_02_qmp_cache`, then sets `gq000_02_started`.

### Scene

- Packed and raw scene resources exist at
  `mod\gq000\scenes\gq000_patch_meet.scene`.
- The current raw scene is generated from
  `tools/gq000_patch_meet.scene-spec.json`. It contains 15 graph nodes, 16
  edges, 13 spoken lines, two choice nodes, two end nodes, and four
  scene-local quest nodes.
- The screenplay store contains exactly the five connected choices:
  `What's the job?`, `Ghostline?`, `Why me?`, `I'm in.`, and
  `Who's behind it?`. The three orphaned options from the crashed current-raw
  build are gone.
- Community activation and `CharacterSpawned` readiness are owned by the
  meeting questphase. At setup range the scene starts Puppet AI in parallel
  with the ordered bridge-case-mood -> someone-coming -> opening-line ->
  engage -> first-choice path. This matches `mq003`'s division of lifecycle
  ownership and avoids registering the 60- and 20-unit waits only after the
  player is already inside the 10-unit engage trigger.
- Exit points `end` and `job_accept` are both declared. Acceptance reaches
  `job_accept` through end node 19; end node 18 is currently not reached by an
  active dialogue branch, so the non-accept fallback still needs runtime/design
  validation.
- All five choice locstrings have the audited vanilla-style
  `db_db`/`pl_pl`/`en_us` locStore descriptor coverage. Runtime testing proved
  that locale grouping alone is insufficient: every locale block must also be
  numerically sorted by `locstringId`, as it is in all four audited vanilla
  scenes. The generator, validator, and checked-in-raw regression now enforce
  that order; in-game confirmation is pending.
- Questphase journal paths follow the journal file-entry index rule: phone
  contact paths use `fileEntryIndex: 1`, while quest objective, description,
  and quest map pin paths under `quests/minor_quest/gq000` use
  `fileEntryIndex: 2`.
- The generator/spec pins `Header.ExportedDateTime`, emits multiple configured
  end nodes, and uses full unsigned 64-bit FNV output for event and locStore
  IDs. Raw validation now passes with no drift errors.
- Runtime testing confirmed the previous `INT63_MASK` probe was the approach
  crash source. Scene event RUIDs and locStore variant IDs must keep the full
  unsigned 64-bit FNV output; do not mask them down to signed 63-bit values.
- The current shared-slot diagnostic scene assigns both the Patch-role actor
  and V `lipsyncAnimSet.id: 0` and contains exactly one
  generic lipsync resource reference. The previous scene assigned V slot `1`
  while both raw slots used
  the same depot path; its packed import table and runtime lookup exposed only
  one distinct resource before the engine requested index `1`. The shared-slot
  build completed the full meeting route without a crash, strongly confirming
  that cardinality mismatch as the scene-start failure.
- The previous installed 14-node scene and late-gated meeting phase remain
  recoverable from
  `H:\Ghostline-backups\pre-mq003-sequence-20260721-233546`; see
  `docs/testing.md` for the historical baseline.

### Dialogue Localization And VO

- Subtitle and VO map raw resources for `gq000_01` are aligned by string ID.
- `source/raw/gq000_01_manifest.json` contains 13 spoken records with key,
  string ID, speaker/addressee, text, audio path, and duration, plus five choice
  records with key, string ID, and text only.
- The `gq000_01` spoken locstring IDs were regenerated across the manifest, raw
  subtitles, raw VO map, and generated scene during the intro-choice semantics
  probe. Choice locstring IDs remain scene-embedded and do not belong in the
  subtitle or VO maps.
- The VO map points at 13 current `.wem` paths under `source/archive`.
  `generated` retains those 13 authored WAVs plus 13 byte-identical legacy
  hash-name duplicates; the manifest-filtered converter selects only the
  current basenames.
- A subtitle map resource now registers the subtitle entries with ArchiveXL.
- Runtime testing confirmed every spoken subtitle and VO line in the meeting
  scene plays correctly.
- The manifest-filtered Wwise 2025.1.7 conversion pass processes exactly 13
  active WAVs; a `-NoCopy` verification regenerated all 13 current WEMs
  byte-identically. It intentionally does not remove the 13 legacy WEM names
  retained for candidate-archive parity.
- The scene still uses a base generic facial lipsync animset as a placeholder;
  Ghostline-owned lipsync `.anims` files have not been integrated.

### Journal And Quest UI

- Packed and raw `gq000` journal resources exist at
  `mod\gq000\journal\gq000.journal`.
- The journal defines:
  - quest root `quests/minor_quest/gq000`
  - phase `quests/minor_quest/gq000/gq000_01`
  - objective `quests/minor_quest/gq000/gq000_01/gq000_01_obj_meet_patch`
  - description
    `quests/minor_quest/gq000/gq000_01/gq000_01_obj_meet_patch/gq000_01_desc_meet_patch`
  - quest map pin
    `quests/minor_quest/gq000/gq000_01/gq000_01_obj_meet_patch/gq000_01_qmp_patch_bridge`
  - point of interest
    `points_of_interest/minor_quests/gq000_01_poi_patch_bridge`
  - phase `quests/minor_quest/gq000/gq000_02`
  - objective `quests/minor_quest/gq000/gq000_02/gq000_02_obj_reach_cache`
  - description
    `quests/minor_quest/gq000/gq000_02/gq000_02_obj_reach_cache/gq000_02_desc_reach_cache`
  - quest map pin
    `quests/minor_quest/gq000/gq000_02/gq000_02_obj_reach_cache/gq000_02_qmp_cache`
  - Patch contact thread `contacts/patch/gq000_01_start` with message
    `01_msg_patch_bridge`, choice group `02_ch_meet_patch`, and reply choice
    `02a_ch_on_my_way`
- Quest onscreen localization exists at
  `mod\gq000\localization\en-us\onscreens\gq000.json`.
- Journal references in the questphase and scene use full journal paths rather
  than bare leaf IDs.
- The quest map pin and POI mappin have been moved to dedicated always-loaded
  marker `#gq000_01_mp_patch_bridge`. Vanilla files confirm this must stay
  separate from scene marker `#gq000_01_sm_patch_bridge`. Runtime testing
  confirmed the meeting tracker/mappin path and its cleanup; explicit map-screen
  and POI presentation still need focused validation.
- The placeholder next objective uses Ghostline-owned always-loaded marker
  `#gq000_02_mp_cache`, roughly 300 units northeast of the bridge origin.
- Runtime testing confirmed acceptance clears the meeting flow, activates
  `Go to the cache coordinates.`, and displays the cache marker at about 275
  metres from the bridge.

### World Placement And Community

- Generated raw and packed world resources exist for:
  - `mod\gq000\world\gq000_patch_meet.streamingsector`
  - `mod\gq000\world\gq000_always_loaded.streamingsector`
  - `mod\gq000\world\gq000_patch_meet.streamingblock`
- The world spec uses captured origin `(-795.7447, 390.34177, 17.272781)`.
  Yaw remains provisional because the captured `ToVector4` did not include
  actor heading.
- The streaming block contains a Quest descriptor for the quest sector and an
  AlwaysLoaded descriptor for the always-loaded sector. The quest descriptor
  binds `questPrefabNodeRef: $/mod/gq000/#gq000_pr_patch_meet`.
- The quest sector contains four trigger areas, one AI spot, and one streamable
  community area.
- The four meeting trigger areas use 12-unit-tall volumes centered around the
  captured bridge origin. Their restored footprint radii are 90 for setup, 10
  for engage, 60 for bridge-case mood, and 20 for someone-coming. Prior
  testing showed that raising/centering the volumes fixed bridge-height misses;
  restoring the smaller horizontal radii prevents the nearby fast-travel point
  from immediately entering setup.
- The always-loaded sector contains the community registry and concrete marker
  nodes needed for early NodeRef resolution: `#gq000_01_sm_patch_bridge`,
  `#gq000_01_mp_patch_bridge`, and `#gq000_02_mp_cache`.
- The community registry maps entry `patch/default` to source object id
  `7897875840529598144` and spot NodeRef
  `$/mod/gq000/#gq000_pr_patch_meet/#gq000_01_spot_patch_bridge`.
- The separate always-loaded registry node now has global ID
  `7571954536596633334`. It no longer collides with the streamed community
  area's global/source ID `7897875840529598144`; generator tests reject any
  future collision.
- The active world spec now uses `Character.GhostlinePatch` and exposed root
  appearance `ghostline_patch_default` for the `patch/default` entry. The
  preceding Judy route remains the stable lifecycle baseline.
- See `docs/world-references.md` for the resolved prefab/NodeRef model and
  current world findings.

### Generated And Editor Support Data

- Prefer `source/raw` over `generated` when preparing CR2W assets for use.
- `generated` contains older generated CR2W snapshots. Its temporary exception
  is the tracked authored WAV bank: use the current manifest and conversion
  helper rather than treating every WAV there as active.
- `GraphEditorStates` contains WolvenKit editor support data only. Do not
  treat it as packed asset source of truth.

## Open Blockers

- Validate all five choice labels with the sorted-locStore build. The first
  group must show `Ghostline?`, `Why me?`, and `What's the job?`; the second
  must show `Who's behind it?` and `I'm in.` without blanks or stale text.
- Decide whether the currently unreachable non-accept `end` scene branch is
  required. Both exit points exist and the phase handles `end`, but active
  dialogue progression currently reaches only `job_accept`.
- Rebuild the scene marker under a vanilla-style scene-prefab child path when
  fresh world/scene tooling replaces the current generated shape.
- Complete the combined sorted-locStore and custom Patch regression. Confirm
  TweakXL registration, Patch spawning, appearance, animation, LODs, streaming,
  and all five choice labels from the installed candidate.
- Recover or deliberately choose Patch's eyes, nose, mouth, jaw, and ears
  creator indices before regenerating his real head. Resolve the documented
  option-22 versus missing-`h21` mismatch rather than treating the shape-22
  toolchain smoke test as a face build.
- Enrich the path-only installed-game catalog through TweakDB/item records,
  root `.ent` mappings, `.app` appearances, component/control entities, chunk
  masks, visual tags, dependencies, and material graphs. Exact mesh appearance
  enumeration and provisional PMA torso/legs/feet primary-mesh assignment are
  implemented; complete bundle resolution is not.
  The audit bounds the effective wardrobe at 158 controller apps, 5,031
  appearance definitions, 12,850 components, and 739 referenced meshes; use a
  long-lived WolvenKit-backed C# helper rather than thousands of CLI launches.
- Add whole-character preview composition and RED material handling. Current
  item previews are neutral-material individual meshes and do not prove NPC
  garment fit or runtime deformation.
- Determine whether WolvenKit's garment-support warnings during head mesh
  re-import are harmless for these resources or require adjusted import
  settings before using generated heads in game.
- Decide whether `source/archive/base` resources are still required. They
  should be excluded from normal install archives unless their impact is
  validated.
- Move the 13 current authored WAVs to an explicit source-audio directory, then
  retire the 13 legacy hash-name WAV/WEM duplicates. Until then, the converter
  must keep filtering through `source/raw/gq000_01_manifest.json`.
- Audit remaining `ep1\...` animation/effect dependencies in Patch's entity or
  explicitly require Phantom Liberty if Patch still crashes when streamed.

## Next Milestones

### 1. Validate Fresh Meeting Scene

- Retest the installed 2026-07-22 custom Patch archive from a clean save. The
  preceding slot-0 baseline confirmed trigger progression, Judy spawn,
  dialogue/VO/subtitles, `job_accept`, journal cleanup, and the cache marker;
  the current changed surfaces are custom Patch and the still-unconfirmed
  embedded choice-label lookup order.
- Validate the staged full dialogue, especially the expected choice-label
  repair, the active `job_accept` route, and whether a non-accept `end` branch
  is needed.
- Continue using `tools/generate_scene.py` and the audited scene spec as source
  of truth rather than patching packed scene CR2W manually.
- Keep failed probe workarounds in `docs/crash-investigation.md` as historical
  context only.

### 2. Validate Meeting-Location World Data

- The full Judy route confirmed that ArchiveXL loads the streaming block and
  that the active community, scene marker, four triggers, meeting mappin, and
  cache mappin resolve in game.
- Validate explicit map-screen/POI presentation and the future nested
  scene-marker hierarchy separately from the already working HUD route.
- Tune Patch yaw, workspot placement, and trigger radii against the real
  location geometry.

### 3. Build The Character Pipeline And Validate Patch

- Schema-v1 manifest validation, the curated Patch catalog, isolated source
  generation, semantic baseline comparison, the complete headless head build,
  live morphable head preview, archive-derived path index, on-demand mesh
  preview, real mesh-appearance enumeration, provisional indexed PMA
  torso/legs/feet selection, and local web UI are implemented and covered by
  regression tests.
- Enrich the provisional primary-mesh selections into complete selectable
  bundles, add indexed hair/head/arms/item support, compose compatible
  body/head/clothing layers in one viewport, add material conversion, and add a
  fresh-character bootstrap command.
- Recover or choose Patch's real head-shape values, resolve the head-import
  garment warning, then eliminate Patch's global `base\...` head overrides.
- TweakXL 1.11.3, the applied generated appearance, and the restored
  `Character.GhostlinePatch` registry are installed. Test Patch spawn and
  approach independently from the already stable Judy lifecycle.
- Continue custom-pathing or replacing Patch dependencies only if missing
  resource hashes change or Patch-specific crashes remain.

### 4. Extend The Quest Beyond Acceptance

- Expand the placeholder post-accept phase after `job_accept`.
- Define `gq000_` facts for accepted job state, cache acquired, cache
  delivered, and quest completion.
- Add objective updates, mappin changes, failure branches, and completion
  branches.
- Keep prefab NodeRef lifecycle aligned with the resolved model in
  `docs/world-references.md`.

### 5. Validate Audio Packaging

- All 13 current subtitles, VO-map entries, and `.wem` assets played correctly
  in the stable meeting route. Revalidate that alignment after future dialogue,
  scene-line, or audio-map edits.
- Add Ghostline-owned lipsync resources if the final scene presentation needs
  them.

### 6. Pack And Test In Game

- The 2026-07-22 custom Patch build has been deserialized, structurally or
  byte-for-byte round-trip checked, packed, extracted, payload-verified,
  installed, and wrapped in a
  verified six-file ZIP. Installed archive SHA-256 is
  `40148CE9F102C5CF77BEA31C1D9043FB20F53B8937873235BDBE3D1A82EF6786`.
- Test ArchiveXL/TweakXL loading, trigger progression, Patch community spawn,
  appearance, dialogue choices, `job_accept`, journal/mappin visibility,
  subtitles, and voice playback from this exact baseline.
