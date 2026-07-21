# Ghostline Roadmap

Last audited: 2026-07-21

This file tracks the current state and the next work needed to turn `gq000`
from a dialogue prototype into a playable quest slice. The 2026-07-21 test
baseline deliberately follows the newest `source/raw` resources even where the
scene generator/spec and older tests have not caught up. Detailed command usage,
runtime crash conclusions, world-reference notes, and packaging instructions now
live in focused docs:

- `docs/tooling.md`
- `docs/testing.md`
- `docs/scene-authoring-rules.md`
- `docs/crash-investigation.md`
- `docs/world-references.md`
- `docs/packaging.md`

## Current Status

### Synchronized Test Baseline

- The pre-build worktree was captured in commit `5b8449d`, then all 15 raw
  CR2W-JSON resources were deserialized into `source/archive` with WolvenKit
  8.17.4. The plain generated `source/raw/gq000_01_manifest.json` was correctly
  excluded from CR2W conversion.
- The rebuilt archive contains 173 verified entries from 176 files under
  `source/archive`. The only exclusions are the Patch `.tmp` file and the two
  Patch head readmes that WolvenKit does not pack.
- The candidate archive, repo package, and installed game archive all have
  SHA-256
  `4833BE432CCD685591CDFAE56D47ED9AE163E120D32B1A96B678360EBFC4E42F`.
  `Ghostline.zip` was rebuilt from the six-file `packed` tree and every ZIP
  payload was checked against its source file.
- The previous repo package, installed archive, and ZIP are retained at
  `H:\Ghostline-backups\stabilize-5b8449d-sync-20260721-214058` until the
  in-game test succeeds.
- This is a synchronized current-raw test build, not a fully green production
  build. The current raw scene has intentional/unreconciled drift from
  `tools/gq000_patch_meet.scene-spec.json`, and four unit tests still describe
  an older scene shape.
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
- The current raw `gq000_patch_meet.questphase` is a seven-node, six-edge
  linear acceptance path: input -> wait for `#gq000_01_tr_setup` -> start
  `mod\gq000\scenes\gq000_patch_meet.scene` at
  `#gq000_01_sm_patch_bridge` -> on `job_accept`, succeed
  `gq000_01_obj_meet_patch` -> disable `gq000_01_qmp_patch_bridge` -> set the
  acceptance fact -> terminating output.
- The current meeting phase has no non-accept `end` route and no phase-level
  community activation, `CharacterSpawned`, engage-trigger, or checkpoint
  nodes. Spawn and approach gating currently live inside the raw scene. This
  differs from the generator/spec-era flow described in older tests and must
  be validated as part of this baseline.
- `gq000_post_accept.questphase` is a minimal skeleton that activates/tracks
  `gq000_02_obj_reach_cache`, activates its description and
  `gq000_02_qmp_cache`, then sets `gq000_02_started`.

### Scene

- Packed and raw scene resources exist at
  `mod\gq000\scenes\gq000_patch_meet.scene`.
- The current raw scene, exported 2026-05-08, is the source of truth for this
  test build. It contains 17 graph nodes, 18 edges, 13 spoken lines, two choice
  nodes, two end nodes, and six scene-local quest nodes.
- The active dialogue still presents five choices: `What's the job?`,
  `Ghostline?`, `Why me?`, `I'm in.`, and `Who's behind it?`. The raw
  screenplay store contains eight options, leaving three orphaned options that
  are not connected to choice nodes.
- The scene embeds the bridge-case-mood pause, community spawn manager,
  `CharacterSpawned` pause, Puppet AI setup, someone-coming pause, and engage
  pause before/around the dialogue. That logic is not present in the current
  meeting questphase.
- Only end node 19 is connected, and the only declared exit point is
  `job_accept`. End node 18 is orphaned, so the generator/spec's non-accept
  `end` fallback is absent from the current raw baseline.
- `tools/gq000_patch_meet.scene-spec.json` and `tools/generate_scene.py`
  describe a newer intended 14-node/15-edge scene with five stored options,
  phase-owned quest flow, and `db_db`/`pl_pl`/`en_us` locStore coverage. The
  generator audit passes, but validating the current raw scene against that
  spec reports 19 drift errors.
- All five active raw choices are missing part of the expected vanilla-style
  locStore descriptor coverage. The earlier blank/`Db-db` label risk is
  therefore still present in this exact build and must be checked in game.
- Questphase journal paths follow the journal file-entry index rule: phone
  contact paths use `fileEntryIndex: 1`, while quest objective, description,
  and quest map pin paths under `quests/minor_quest/gq000` use
  `fileEntryIndex: 2`.
- The generator/spec pins `Header.ExportedDateTime`, emits multiple configured
  end nodes, uses full unsigned 64-bit FNV output for event and locStore IDs,
  and remains the intended repair path after this baseline is tested.
- Runtime testing confirmed the previous `INT63_MASK` probe was the approach
  crash source. Scene event RUIDs and locStore variant IDs must keep the full
  unsigned 64-bit FNV output; do not mask them down to signed 63-bit values.
- Previous test conclusions about the 14-node generated scene and its
  phase-level `CharacterSpawned` gate remain useful history, but do not
  describe the 17-node current-raw build being tested now.

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
  captured bridge origin. Their current approximate footprint radii are 150
  for setup, 100 for engage, 25 for bridge-case mood, and 20 for
  someone-coming. Prior testing showed that raising/centering these volumes
  helped the bridge approach path; the current scene-owned gating sequence
  still needs a fresh runtime test.
- The always-loaded sector contains the community registry and concrete marker
  nodes needed for early NodeRef resolution: `#gq000_01_sm_patch_bridge`,
  `#gq000_01_mp_patch_bridge`, and `#gq000_02_mp_cache`.
- The community registry maps entry `patch/default` to source object id
  `7897875840529598144` and spot NodeRef
  `$/mod/gq000/#gq000_pr_patch_meet/#gq000_01_spot_patch_bridge`.
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

- Test the synchronized 2026-07-21 current-raw build before reconciling it with
  the generator/spec. Record which trigger, spawn, dialogue, exit, journal,
  mappin, subtitle, and VO behaviors actually work.
- Reconcile the 17-node raw scene with the intended 14-node generator/spec
  after runtime results identify which flow should be preserved. Four unit
  tests currently assert an older 17-node wrapper fixture and need updating as
  part of that reconciliation.
- Repair and validate the five active choice locStores. Current raw validation
  shows incomplete `db_db`/`pl_pl`/`en_us` coverage, so blank or `Db-db`
  choice labels remain a known risk.
- Decide whether the orphaned end node and absent non-accept `end` exit are
  intentional; only `job_accept` currently returns to the meeting questphase.
- Validate the dedicated always-loaded map-pin markers
  `#gq000_01_mp_patch_bridge` and `#gq000_02_mp_cache` in game.
- Validate post-accept progression: meet objective succeeds, bridge mappin
  disables, `gq000_job_accepted` is set, and the placeholder cache
  objective/mappin appears.
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

- Test the synchronized current-raw scene first and capture precise runtime
  observations.
- Use `tools/generate_scene.py` and
  `tools/gq000_patch_meet.scene-spec.json` as the repair path once the desired
  behavior is selected.
- Validate the staged full dialogue in game, especially the missing
  non-accept `end` fallback and the active `job_accept` acceptance route.
- Fix the generator/spec against vanilla reference shapes rather than patching
  the packed scene manually.
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

- The 2026-07-21 current-raw baseline has been deserialized, packed, extracted,
  hash-verified, installed, and wrapped in a verified six-file ZIP.
- Test ArchiveXL loading, trigger progression, Judy community spawn, dialogue
  choices, `job_accept`, journal/mappin visibility, subtitles, and voice
  playback from this exact baseline.
- Install TweakXL before testing the custom Patch character and its TweakDB
  records.
