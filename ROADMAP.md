# Ghostline Roadmap

Last audited: 2026-07-22

This file tracks the current state and the next work needed to turn `gq000`
from a dialogue prototype into a playable quest slice. The 2026-07-21
mq003-sequenced isolation build keeps the repaired world and newer phone/cache
progression while changing only the meeting phase/scene lifecycle. Detailed
command usage, runtime crash conclusions, world-reference notes, and packaging
instructions now live in focused docs:

- `docs/tooling.md`
- `docs/testing.md`
- `docs/scene-authoring-rules.md`
- `docs/crash-investigation.md`
- `docs/world-references.md`
- `docs/packaging.md`

## Current Status

### MQ003-Sequenced Test Build

- The first synchronized current-raw build crashed after accepting the job and
  fast travelling near the bridge. The dump recorded `Loading world`, resource
  throttling in `Flood`, and an invalid allocator pointer on `redDispatcher20`;
  plugin logs showed no Ghostline registration or merge error.
- The first repair allowed the nearby fast travel to finish, but both a normal
  approach and a deliberately slow retry then crashed at the 10-unit engage
  boundary while the game was fully loaded. Both dumps failed at
  `Cyberpunk2077+0x1d173be` before dialogue visualization began.
- Moving scene launch to the 90-unit setup boundary moved the same
  `Cyberpunk2077+0x1d173be` failure to 89.27 horizontal units from the scene
  origin. This rules out the engage trigger itself and ties the failure to
  scene initialization.
- The current isolation build follows the audited `mq003` lifecycle instead of
  launching the scene at engage range: activate and validate the community
  first, launch the scene from the broad setup gate, then let the running scene
  progress through case-mood, someone-coming, opening line, and engage gates.
  It additionally assigns both Patch and V to lipsync slot `0` and emits one
  generic lipsync reference. This is a diagnostic cardinality probe, not the
  intended final lipsync design. The newer root phone flow and post-accept
  cache phase remain unchanged.
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
- All 22 Python regression tests pass. The meeting phase and changed scene also
  pass exact WolvenKit 8.17.4 serialize/deserialize SHA-256 round trips. Their
  respective SHA-256 hashes are
  `A07A6DA858EFE86E5C9984395E7A933D3C5081D2CBB619AD423C9FAF67BDD5FB`
  and
  `9DDFD4F05344B11206820414D6D9A9B0854CC570D9AC0EBAA751AF91CE2EA303`.
- The rebuilt archive contains 173 verified entries from 176 files under
  `source/archive`. The only exclusions are the Patch `.tmp` file and the two
  Patch head readmes that WolvenKit does not pack.
- Compared with the previous installed mq003-sequenced archive, exactly one
  payload changed: the meet scene. No depot paths were added or removed; the
  meeting phase, world, localization, audio, journal, character, and root phase
  stayed byte-identical.
- The candidate archive, repo package, and installed game archive all have
  SHA-256
  `FEAEC7D66E6C3E492ACE2454A0E32FFB7E1DCBA6B8C08B7E44A427745BF21CAC`.
  `Ghostline.zip` was rebuilt from the six-file `packed` tree, has SHA-256
  `DE75D0D62FA08E90A2BE0A316035762E9B29007094A81713CA6F51A5361DA3C9`,
  and every ZIP payload matches its packed source.
- Build and round-trip evidence is retained at
  `H:\Ghostline-builds\choice-locstore-sort-20260722-002552`. The successful
  but label-broken slot-0 build is retained at
  `H:\Ghostline-backups\pre-choice-locstore-sort-20260722-002552`.
- The crashing synchronized package is retained at
  `H:\Ghostline-backups\pre-stability-fix-20260721-224252`. The earlier
  pre-sync package remains at
  `H:\Ghostline-backups\stabilize-5b8449d-sync-20260721-214058`.
- The archive currently contains 93 `base\...` global overrides and 80
  `mod\...` assets. The global overrides remain a packaging risk pending
  validation. It also carries 26 valid WEM files while the VO map references
  13 of them.
- The local game install has ArchiveXL but no TweakXL plugin. The temporary
  `Character.Judy` world entry avoids the custom Patch TweakDB record for this
  scene-isolation test, but Patch itself cannot be validated until TweakXL is
  installed or the dependency is otherwise removed.

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
- The current crash-isolation scene assigns both Patch and V
  `lipsyncAnimSet.id: 0` and contains exactly one generic lipsync resource
  reference. The previous scene assigned V slot `1` while both raw slots used
  the same depot path; its packed import table and runtime lookup exposed only
  one distinct resource before the engine requested index `1`. The shared-slot
  build completed the full meeting route without a crash, strongly confirming
  that cardinality mismatch as the scene-start failure.
- The previous installed 14-node scene and late-gated meeting phase remain
  recoverable from the pre-sequence backup recorded in the stability section.

### Dialogue Localization And VO

- Subtitle and VO map raw resources for `gq000_01` are aligned by string ID.
- `source/raw/gq000_01_manifest.json` records generated line keys, string IDs,
  text, audio paths, and durations.
- The `gq000_01` dialogue locstring IDs were regenerated across the manifest,
  raw subtitles, raw VO map, and generated scene during the intro-choice
  semantics probe.
- The VO map points at `.wem` paths, and matching Wwise-generated `.wem` files
  exist alongside the authored `.wav` files.
- A subtitle map resource now registers the subtitle entries with ArchiveXL.
- Runtime testing confirmed every spoken subtitle and VO line in the meeting
  scene plays correctly.
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
  separate from scene marker `#gq000_01_sm_patch_bridge`; runtime validation is
  still pending.
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
- Temporary runtime isolation state: the active world spec uses
  `Character.Judy` for the `patch/default` entry while scene crashes are being
  isolated. Revert it to `Character.GhostlinePatch` after the scene path is
  stable.
- See `docs/world-references.md` for the resolved prefab/NodeRef model and
  current world findings.

### Generated And Editor Support Data

- Prefer `source/raw` over `generated` when preparing CR2W assets for use.
- `generated` contains older generated snapshots.
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
- Install TweakXL before reverting the temporary Judy community registry entry
  to `Character.GhostlinePatch`, then re-test Patch spawn after the scene path
  is stable.
- Decide whether `source/archive/base` resources are still required. They
  should be excluded from normal install archives unless their impact is
  validated.
- Remove or document the 13 WEM files that are packaged but not referenced by
  the current VO map.
- Audit remaining `ep1\...` animation/effect dependencies in Patch's entity or
  explicitly require Phantom Liberty if Patch still crashes when streamed.

## Next Milestones

### 1. Validate Fresh Meeting Scene

- Test the installed mq003-sequenced archive from a clean save and capture precise
  trigger, spawn, dialogue, exit, journal, mappin, subtitle, and VO behavior.
- Validate the staged full dialogue, especially repaired choice labels, the
  active `job_accept` route, and whether a non-accept `end` branch is needed.
- Continue using `tools/generate_scene.py` and the audited scene spec as source
  of truth rather than patching packed scene CR2W manually.
- Keep failed probe workarounds in `docs/crash-investigation.md` as historical
  context only.

### 2. Validate Meeting-Location World Data

- Confirm ArchiveXL loads `mod\gq000\world\gq000_patch_meet.streamingblock`.
- Confirm scene marker, setup trigger, engage trigger, case-mood trigger,
  someone-coming trigger, Patch community, and map-pin NodeRefs all resolve.
- Tune Patch yaw, workspot placement, and trigger radii against the real
  location geometry.

### 3. Restore Patch As The Community Character

- Switch the temporary `Character.Judy` registry record back to
  `Character.GhostlinePatch`.
- Test Patch spawn and approach after the scene startup path is stable.
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

- Validate in game that subtitles, VO map, and `.wem` assets remain aligned
  after scene edits.
- Add Ghostline-owned lipsync resources if the final scene presentation needs
  them.

### 6. Pack And Test In Game

- The 2026-07-22 sorted-locStore build has been deserialized, round-trip
  checked, packed, extracted, payload-verified, installed, and wrapped in a
  verified six-file ZIP. Installed archive SHA-256 is
  `FEAEC7D66E6C3E492ACE2454A0E32FFB7E1DCBA6B8C08B7E44A427745BF21CAC`.
- Test ArchiveXL loading, trigger progression, Judy community spawn, dialogue
  choices, `job_accept`, journal/mappin visibility, subtitles, and voice
  playback from this exact baseline.
- Install TweakXL before testing the custom Patch character and its TweakDB
  records.
