# Ghostline Roadmap

Last audited: 2026-05-01

This file tracks the current state and the next work needed to turn `gq000`
from a dialogue prototype into a playable quest slice. Detailed command usage,
runtime crash conclusions, world-reference notes, and packaging instructions now
live in focused docs:

- `docs/tooling.md`
- `docs/testing.md`
- `docs/scene-authoring-rules.md`
- `docs/crash-investigation.md`
- `docs/world-references.md`
- `docs/packaging.md`

## Current Status

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
- `gq000_patch_meet.questphase` currently:
  - activates the `patch/default` community entry,
  - waits for `#gq000_01_tr_setup`,
  - creates checkpoint `gq000_patch_meet`,
  - waits for `#gq000_01_tr_engage`,
  - waits for the Patch community at `#gq000_01_com_patch_bridge` to report
    `CharacterSpawned`,
  - starts `mod\gq000\scenes\gq000_patch_meet.scene` at
    `#gq000_01_sm_patch_bridge`,
  - exits through scene socket `end` as a non-accept fallback,
  - exits through scene socket `job_accept` by succeeding
    `gq000_01_obj_meet_patch`, disabling `gq000_01_qmp_patch_bridge`, setting
    `gq000_job_accepted`, and returning to the root phase.
- `gq000_post_accept.questphase` is a minimal skeleton that activates/tracks
  `gq000_02_obj_reach_cache`, activates its description and
  `gq000_02_qmp_cache`, then sets `gq000_02_started`.

### Scene

- Packed and raw scene resources exist at
  `mod\gq000\scenes\gq000_patch_meet.scene`.
- The current scene is represented by
  `tools/gq000_patch_meet.scene-spec.json` and `tools/generate_scene.py`,
  including the staged acceptance routing.
- The current scene is a 14-node full meeting dialogue with 15 connected
  edges, 13 spoken lines, and 5 player choices.
- Normal-speed approach no longer crashes after adding a pre-scene
  `CharacterSpawned` gate for `#gq000_01_com_patch_bridge` in
  `gq000_patch_meet.questphase` and after raising/centering the bridge trigger
  volumes to cover the meeting bridge's varying height.
- Patch is acquired from active community entry `patch` at
  `#gq000_01_com_patch_bridge` with the vanilla community actor pattern. V is
  found in context through `Character.Player_Puppet_Base`.
- The current scene flow is:
  `start -> puppet_ai / bridge_case_mood pause -> someone_coming pause ->
  Patch intro -> intro choice hub`. The optional `Ghostline?` and `Why me?`
  branches loop back to the intro choice hub; the required `What's the job?`
  branch advances to the post-job choice hub. The optional
  `Who's behind it?` branch loops back to that second hub; the required
  `I'm in.` branch closes the scene through dedicated exit `job_accept`.
- Scene-local journal/objective/mappin creation has been removed from the
  active meeting path. Quest state is now owned by the questphase flow.
- The intro choice probe currently sets `isSingleChoice: 0` on all three
  options, with `type.properties: 0` for the two optional/info branches and
  `type.properties: 1` for the main progression branch.
- Questphase journal paths now follow the journal file-entry index rule: phone
  contact paths use `fileEntryIndex: 1`, while quest objective, description,
  and quest map pin paths under `quests/minor_quest/gq000` use
  `fileEntryIndex: 2`.
- The later `Who's behind it?` and `I'm in.` choice group is restored in the
  generated scene.
- `tools/generate_scene.py` now supports multiple end nodes via `end_nodes`;
  `gq000_patch_meet.scene-spec.json` routes only the acceptance branch to the
  `job_accept` exit.
- The fresh generated shape now uses root `version: 5`, `PLATFORM_PC`,
  `minorQuests`, vanilla spoken line IDs `1 + 256n`, choice option IDs
  `2 + 256n`, padded choice sockets, deterministic event IDs, and embedded
  vanilla-style `db_db`/`pl_pl`/`en_us` choice locStore coverage. Choice
  locstrings now get two `db_db` descriptors, a blank fallback and a source text
  payload, before the other locale blocks.
- The scene spec pins `Header.ExportedDateTime` so generator and WolvenKit
  deserialization output can be checked byte-for-byte across repeated runs.
- The previous 18-node generated dialogue scene crashed on approach. The
  10-node journal handoff probe was validated in game after fixing the quest
  mappin `fileEntryIndex`. The later normal-speed approach crash was fixed by
  adding the pre-scene `CharacterSpawned` gate in the questphase. The later
  `Ghostline?` `Db-db` display issue was fixed by switching choice locStores to
  the audited vanilla-style descriptor shape. The current staged build removes
  scene-local quest UI execution and restores `job_accept` routing through the
  meeting questphase.

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
- The four meeting trigger areas use taller 12-unit trigger volumes centered
  around the captured bridge origin to cover the bridge's varying deck height.
  Runtime testing confirmed this resolved the bridge approach crash path.
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

- Validate the regenerated 63-bit scene locstring IDs in game. Previous testing
  confirmed the full questphase/scene sequence works, but the second and third
  options on the first choice node displayed blank before the locstring probe.
- Validate the dedicated always-loaded map-pin markers
  `#gq000_01_mp_patch_bridge` and `#gq000_02_mp_cache` in game.
- Validate post-accept progression: meet objective succeeds, bridge mappin
  disables, `gq000_job_accepted` is set, and the placeholder cache
  objective/mappin appears.
- Rebuild the scene marker under a vanilla-style scene-prefab child path when
  fresh world/scene tooling replaces the current generated shape.
- Revert the temporary Judy community registry entry to `Character.GhostlinePatch`
  and re-test Patch spawn after the scene path is stable.
- Decide whether `source/archive/base` resources are still required. They
  should be excluded from normal install archives unless their impact is
  validated.
- Audit remaining `ep1\...` animation/effect dependencies in Patch's entity or
  explicitly require Phantom Liberty if Patch still crashes when streamed.

## Next Milestones

### 1. Validate Fresh Meeting Scene

- Use `tools/generate_scene.py` and
  `tools/gq000_patch_meet.scene-spec.json` as the source path for fresh scene
  resources.
- Validate the staged full dialogue in game, especially the non-accept `end`
  fallback and `job_accept` acceptance route.
- If runtime issues remain, fix the generator/spec against vanilla reference
  shapes rather than patching the packed scene manually.
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

- Deserialize updated raw CR2W-JSON into `source/archive`.
- Verify packed CR2W resources.
- Build an install package from the scoped archive tree, not from the repo
  root.
- Check ArchiveXL, TweakXL, Patch spawn, trigger progression, journal/mappin
  visibility, subtitles, and voice playback.
