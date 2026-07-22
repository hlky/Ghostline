# Ghostline Roadmap

Last audited: 2026-07-22

This file tracks the current state and the next work needed to turn `gq000`
from a dialogue prototype into a playable quest slice. The current 2026-07-22
delivery/debrief candidate builds on the runtime-proven repaired world,
mq003-sequenced meeting lifecycle, visible custom Patch, sorted choice locStore,
and explicit-player Tyger Claw combat setup. The bridge meeting, all dialogue
labels, VO/subtitles, job acceptance, cache handoff, guard spawn/patrol/aggression,
terminal transform and marker, native breach, readable shards, leave-area beat,
and cleanup are confirmed. The active package extends that baseline with a
native Kabuki drop-point deposit, Morrow's two-choice phone debrief, a standard
completion reward, and quest success.
Detailed command usage, runtime flow, crash conclusions,
world-reference notes, and packaging instructions now live in focused docs:

- `docs/quest-scene-flow.md`
- `docs/quest-design.md`
- `docs/tooling.md`
- `docs/testing.md`
- `docs/scene-authoring-rules.md`
- `docs/crash-investigation.md`
- `docs/world-references.md`
- `docs/drop-points.md`
- `docs/packaging.md`

## Current Status

### Recovered Quest Design

- The original narrative brief has been recovered and normalized in
  `docs/quest-design.md`. It defines Ghostline, Morrow, Iris, Patch, the Tyger
  Claw/Arasaka-adjacent laundering route, the bridge-to-cache-to-drop flow,
  two archived conversations, and Morrow's delivery thread.
- `Quiet Spine` is the selected data-courier network name. Four unused names
  and alternate writing variants remain documented for later quests.
- The extraction and leave-area objectives, both archived-conversation journal
  entries, two matching readable shard items, and the separate datacache package
  are live. The active native deposit target is map-labelled Kabuki
  `drop_point_009` at `(-1168.66333, 1309.51709, 19.9768238)`, about 252.7
  units from the relay. Morrow's complete post-delivery phone conversation and
  both V response branches are wired into the generated delivery phase.
- The intended cabinet-style cache visual is baked into a larger recycling
  station proxy. Its inspected collision is actor 36 of 64 in
  `NormalCollisionNode_087`, source prefab hash `8325780084261042030`, rather
  than a standalone entity. The cache should therefore use a Ghostline-owned
  device/interaction overlay while preserving the vanilla mesh and collision.

### Meeting And Patch Baseline

- The early synchronized raw build crashed first near the bridge and then at
  whichever boundary launched the scene. The mq003-shaped lifecycle and a
  shared lipsync slot isolated the failure to scene initialization and produced
  the first stable end-to-end meeting run. Detailed crash evidence and failed
  probes remain in `docs/crash-investigation.md`.
- A custom Patch initially stayed invisible because the community requested
  the `.app` definition name instead of the root entity's exposed appearance.
  The live community now requests `ghostline_patch_default`, which maps to
  internal appearance `default`.
- Numeric sorting within each embedded locStore locale block repaired the
  blank/stale dialogue labels. Runtime testing confirms all three first-group
  labels and both second-group labels, along with Patch visibility, animation,
  subtitles, VO, acceptance, and journal cleanup.
- The stable world baseline keeps 12-unit-tall meeting triggers with horizontal
  radii `90/10/60/20` and a distinct always-loaded registry node ID. The current
  cache and delivery work deliberately preserves that meeting lifecycle.
- Historical build hashes and isolation packages are retained in
  `docs/testing.md`; the active delivery/debrief package and evidence are in
  `Next Milestones -> Pack And Test In Game` below.
- The archive still carries unvalidated `base\...` global overrides and 26
  valid WEM files while the VO map references 13. The overrides remain a
  packaging risk pending validation.
- The local game install has ArchiveXL and official TweakXL 1.11.3. Patch, the
  Ghostline faction, and both readable-shard records are runtime-confirmed;
  the separate datacache package and completion reward are part of the active
  delivery/debrief test.

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
- Minimal device registry `mod\gq000\world\gq000_custom_devices.devices`,
  resource-patched into
  `base\worlds\03_night_city\_compiled\default\03_night_city.devices` so the
  custom relay's `AccessPointControllerPS` can be resolved reliably.

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
- The downloaded female NPV root is now pinned separately as checked
  CR2W-JSON. It has 116 root components and its appearance uses
  `baseEntityType: WomanAverage`; it must not be synthesized from the
  110-component male root. Schema-v1 frame profiles now bind the root, entity
  type, PMA/PWA token, head preview, and creator range together, and validation
  rejects cross-frame templates, catalogs, and indexed overrides.
- The NPV template's Blender file contains import, shape-key application, and
  export scripts. Blender 5.1 has Cyberpunk IO Suite 1.8.0 installed locally,
  and the complete headless round trip is now scripted and smoke-tested. The
  Patch subset exported 13 morphtarget GLBs, requested temporary shape value
  22, exported 13 mesh GLBs, rebuilt 13 CR2W meshes, and verified every header
  and hash in isolated temporary output. A later target-name audit proved that
  22 selects missing `h21` and is a geometry no-op; the current builder derives
  actual targets from GLB metadata and permits Basis/value 1 plus named values
  2 through 21.
- The female PWA core exports 105 named targets, including all five `h21`
  variants, so creator values 1 through 22 are mechanically verified for the
  female-average profile. A full isolated build exported and rebuilt the four
  selected female head meshes as CR2W, and the generated female `.ent` and
  `.app` passed a WolvenKit deserialize/serialize round trip.
- The local WebGL UI renders the active frame's real morph-target head, applies
  all five facial controls immediately, and preserves Blender for the final
  bake only. It accepts a reviewed server-side manifest through `--manifest`;
  the default remains Patch. The male default preview is the 25.7-MiB core
  head; optional layers are loaded only on request.
- The installed-game path index currently contains 4,965 records from base and
  EP1: 1,329 clothing, 1,528 hair, 1,772 head, 144 body, and 192 player-item
  appearance resources. The UI searches slot/frame/family/path metadata and
  successfully uncooked Patch's military boot to an isolated GLB preview. PMA
  torso, legs, and feet primary meshes are selectable for Patch, while PWA
  torso and legs are selectable for the female catalog. The UI reads real
  appearances from the cooked mesh, records a frame-constrained canonical
  indexed override, and the generator updates both appearance component copies.
  PWA feet remain preview-only until a suitable garment anchor is validated.
  Live QA assigned Patch's military boot `black_red` appearance and passed full
  manifest validation.
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
- `source/characters/female-example.character.json` and its dedicated catalog
  now provide a checked female-average authoring fixture. Generation clones the
  35-component tutorial `casual` appearance, rewrites 18 numeric tutorial mesh
  IDs to explicit character-owned paths, and stages those meshes plus four
  texture dependencies. The full-body mesh still embeds the original tutorial
  texture namespace, the root retains EP1 dependencies, and the resulting NPC
  has not been validated in game; do not treat this fixture as shipping content.
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
  - `mod\gq000\phases\gq000_delivery.questphase`
- `gq000.questphase` is now the staged root flow:
  `input -> phone start guard -> Patch phone message -> phone choice group ->
  wait for On my way reply -> meet objective/description/mappin ->
  gq000_patch_meet phase -> accepted-state check -> gq000_post_accept phase ->
  gq000_delivery phase`.
- The root phase no longer starts the meeting objective from the bridge trigger
  and no longer sets `gq000_done`. Current staged facts include
  `gq000_phone_start_sent`, `gq000_phone_reply_on_my_way`,
  `gq000_job_accepted`, `gq000_02_started`, `gq000_cache_acquired`, the
  engine-owned deposit fact `gq000_datacache`, `gq000_cache_delivered`, and
  `gq000_completed`.
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
- `gq000_post_accept.questphase` is now a generated 43-node, 44-edge cache
  flow. It activates the reach objective and mappin, disables the relay,
  activates the whole Tyger Claw community, waits until the entire community
  is spawned, then waits for V at the site. The 25-unit arrival gate succeeds
  the reach objective and swaps to the extraction objective while also fanning
  into an independent, vanilla-`mq022` hostility branch. That branch resolves
  each named guard, applies the same `neutral -> hostile` attitude transition,
  assigns V as the immediate combat target, and explicitly injects V as the
  combat threat. A dedicated quest
  mappin targets the relay's live `UI_Interaction` slot while the phase enables
  the relay and waits for native
  breach success, immediately sets `gq000_cache_acquired`, uses a one-second
  presentation delay instead of a UI-visibility gate, disables the relay,
  succeeds extraction, hides the terminal pin, activates and grants both Quiet
  Spine shards plus `Items.gq000_datacache`, tracks a leave-area objective, and
  deactivates surviving guards after V leaves the larger cleanup radius.
- `gq000_delivery.questphase` is a generated 25-node, 25-edge delivery and
  debrief flow. It confirms the package is present, fires the vanilla
  `ReserveItemToThisDropPoint` contract at live Kabuki `drop_point_009`, waits
  for the package `friendlyName` fact `gq000_datacache`, closes the delivery
  objective, sets `gq000_cache_delivered`, runs both Morrow reply branches,
  waits for the final message, grants `QuestRewards.gq000_completion`, sets
  `gq000_completed`, and succeeds the quest root.
- Guard kills are not a gate. Stealth and combat are both valid. Activation
  uses vanilla `None`/`None` whole-community semantics plus an explicit
  readiness gate; cleanup deactivates the same whole community. The hostility
  side branch also does not gate objective progression if a guard has already
  died or cannot be resolved.

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
  that order; runtime testing confirms the repaired five-label result.
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
  - extraction objective
    `quests/minor_quest/gq000/gq000_02/gq000_02_obj_extract_cache`
  - extraction quest map pin
    `quests/minor_quest/gq000/gq000_02/gq000_02_obj_extract_cache/gq000_02_qmp_extract_cache`,
    targeting `#gq000_02_ap_cache` slot `UI_Interaction`
  - leave-area objective
    `quests/minor_quest/gq000/gq000_02/gq000_02_obj_leave_area`
  - phase `quests/minor_quest/gq000/gq000_03`
  - delivery objective
    `quests/minor_quest/gq000/gq000_03/gq000_03_obj_deliver_cache`
  - delivery description
    `quests/minor_quest/gq000/gq000_03/gq000_03_obj_deliver_cache/gq000_03_desc_deliver_cache`
  - delivery map pin
    `quests/minor_quest/gq000/gq000_03/gq000_03_obj_deliver_cache/gq000_03_qmp_drop_point`,
    targeting Ghostline's always-loaded `#gq000_03_mp_drop_point` marker at
    live Kabuki `drop_point_009`; it uses yellow `DefaultQuestVariant`
  - archived conversations
    `onscreens/emails/quests/minor_quest/gq000/shards/quiet_spine_01` and
    `onscreens/emails/quests/minor_quest/gq000/shards/quiet_spine_02`
  - Patch contact thread `contacts/patch/gq000_01_start` with message
    `01_msg_patch_bridge`, choice group `02_ch_meet_patch`, and reply choice
    `02a_ch_on_my_way`
  - Morrow contact thread `contacts/morrow/gq000_04_delivery` with two opening
    messages, two V choices, their branch-specific replies, and final
    `05_msg_more_work`
- Quest onscreen localization exists at
  `mod\gq000\localization\en-us\onscreens\gq000.json`.
- Journal references in the questphase and scene use full journal paths rather
  than bare leaf IDs.
- The quest map pin and POI mappin have been moved to dedicated always-loaded
  marker `#gq000_01_mp_patch_bridge`. Vanilla files confirm this must stay
  separate from scene marker `#gq000_01_sm_patch_bridge`. Runtime testing
  confirmed the meeting tracker/mappin path and its cleanup; explicit map-screen
  and POI presentation still need focused validation.
- The next objective uses Ghostline-owned always-loaded marker
  `#gq000_02_mp_cache` at the selected Watson/Kabuki cabinet relay.
- The delivery objective also uses a Ghostline-owned always-loaded marker,
  `#gq000_03_mp_drop_point`, colocated with the live deposit machine. ArchiveXL
  logged that it could not resolve the direct cooked cross-world mappin; the
  generated phase still reserves the item to the native device itself.
- Runtime testing confirmed acceptance clears the meeting flow, activates
  `Go to the cache coordinates.`, and displays the cache marker at about 275
  metres from the bridge.

### World Placement And Community

- Generated raw and packed world resources exist for:
  - `mod\gq000\world\gq000_patch_meet.streamingsector`
  - `mod\gq000\world\gq000_always_loaded.streamingsector`
  - `mod\gq000\world\gq000_patch_meet.streamingblock`
  - `mod\gq000\world\gq000_custom_devices.devices`
- The world spec uses captured origin `(-795.7447, 390.34177, 17.272781)`.
  Yaw remains provisional because the captured `ToVector4` did not include
  actor heading.
- The streaming block contains a Quest descriptor for the quest sector and an
  AlwaysLoaded descriptor for the always-loaded sector. The quest descriptor
  binds `questPrefabNodeRef: $/mod/gq000/#gq000_pr_patch_meet`.
- The quest sector contains six trigger areas, one native access-point device,
  five AI spots, and two streamable community areas.
- The four meeting trigger areas use 12-unit-tall volumes centered around the
  captured bridge origin. Their restored footprint radii are 90 for setup, 10
  for engage, 60 for bridge-case mood, and 20 for someone-coming. Prior
  testing showed that raising/centering the volumes fixed bridge-height misses;
  restoring the smaller horizontal radii prevents the nearby fast-travel point
  from immediately entering setup.
- The always-loaded sector contains the community registry and concrete marker
  nodes needed for early NodeRef resolution: `#gq000_01_sm_patch_bridge`,
  `#gq000_01_mp_patch_bridge`, `#gq000_02_mp_cache`, and
  `#gq000_03_mp_drop_point`.
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
- The cache site adds dormant device `#gq000_02_ap_cache`, a 25-unit arrival
  trigger, a 75-unit cleanup trigger, and three inactive-on-start Watson/Kabuki
  Tyger Claw entries. The streamable guard community is cache-local and uses
  verified records from `ma_wbr_jpn_013_claws_com.community`; activation is
  whole-community followed by a whole-community `CharacterSpawned > 0`
  readiness gate. Runtime proved all three records spawn and that the short
  patrol works, but the prior border-patrol-derived threat node left them
  passive because it did not name a target. The arrival trigger now uses the
  per-entry `mq022_combat.questphase` sequence and explicitly targets `#player`.
  All three
  initial placements are within 4.85–6.66 units on the cabinet's exterior side;
  one gunner cycles two finite sequenced workspots and two guards remain close
  sentries. The relay mount remains `(-1000.02, 1497.2208, 8.3)` and now uses
  absolute yaw `178.6`, exactly a `-90` degree shortest-path change from the
  visibly perpendicular `-91.4` runtime build. Runtime has now confirmed the
  transform, patrol route, and explicit-player aggression setup.
- The access point reuses the vanilla physical access-point entity and native
  `AccessPointControllerPS`. Its instance starts `OFF`, autoscales, and uses a
  file-unique RedPackage buffer ID. A minimal Ghostline `.devices` registry is
  patched into Night City's global device registry for controller lookup. A
  `.psrep` persistence resource is optional and deferred; no sector
  persistent-state clone or custom controller is needed.
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

- Decide whether the currently unreachable non-accept `end` scene branch is
  required. Both exit points exist and the phase handles `end`, but active
  dialogue progression currently reaches only `job_accept`.
- Rebuild the scene marker under a vanilla-style scene-prefab child path when
  fresh world/scene tooling replaces the current generated shape.
- Recover or deliberately choose Patch's eyes, nose, mouth, jaw, and ears
  creator indices before regenerating his real head. Resolve the documented
  option-22 versus missing-`h21` mismatch rather than treating the shape-22
  toolchain smoke test as a face build.
- Enrich the path-only installed-game catalog through TweakDB/item records,
  root `.ent` mappings, `.app` appearances, component/control entities, chunk
  masks, visual tags, dependencies, and material graphs. Exact mesh appearance
  enumeration, provisional PMA torso/legs/feet assignment, and provisional PWA
  torso/legs assignment are implemented; complete bundle resolution is not.
  The audit bounds the effective wardrobe at 158 controller apps, 5,031
  appearance definitions, 12,850 components, and 739 referenced meshes; use a
  long-lived WolvenKit-backed C# helper rather than thousands of CLI launches.
- Add whole-character preview composition and RED material handling. Current
  item previews are neutral-material individual meshes and do not prove NPC
  garment fit or runtime deformation.
- Validate the female example in game: appearance/material resolution, facial
  animation, LODs, streaming, and PWA garment deformation. Patch or custom-path
  the tutorial full-body mesh's internal texture references before treating the
  original tutorial namespace as removable, and review a valid PWA feet anchor
  before enabling indexed female footwear assignment.
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

### 1. Preserve The Stable Meeting Scene

- Runtime testing now confirms custom Patch visibility, both choice groups,
  subtitles/VO, `job_accept`, journal cleanup, and the cache handoff.
- Decide later whether the non-accept `end` branch needs different quest
  behavior; it is no longer part of the cache-encounter test gate.
- Continue using `tools/generate_scene.py` and the audited scene spec as source
  of truth rather than patching packed scene CR2W manually.
- Keep failed probe workarounds in `docs/crash-investigation.md` as historical
  context only.

### 2. Validate Meeting-Location World Data

- The full Judy route and subsequent custom Patch route confirmed that
  ArchiveXL loads the streaming block and that the active community, scene
  marker, four meeting triggers, meeting mappin, and cache handoff resolve in
  game.
- Validate explicit map-screen/POI presentation and the future nested
  scene-marker hierarchy separately from the already working HUD route.
- Tune Patch yaw, workspot placement, and trigger radii against the real
  location geometry.

### 3. Build The Character Pipeline And Validate Patch

- Schema-v1 male/female frame validation, separate vetted roots and catalogs,
  isolated source and template-asset staging, semantic Patch baseline
  comparison, the complete headless head build, live morphable frame-specific
  head preview, archive-derived path index, on-demand mesh preview, real
  mesh-appearance enumeration, provisional indexed PMA torso/legs/feet and PWA
  torso/legs selection, and local web UI are implemented and covered by
  regression tests.
- Enrich the provisional primary-mesh selections into complete selectable
  bundles, add indexed hair/head/arms/item support, compose compatible
  body/head/clothing layers in one viewport, add material conversion, and add a
  fresh-character bootstrap command.
- Recover or choose Patch's real head-shape values, resolve the head-import
  garment warning, then eliminate Patch's global `base\...` head overrides.
- Run the generated female fixture in game, resolve its inherited EP1/tutorial
  texture dependencies, and validate a PWA feet garment anchor before promoting
  it into a reusable shipping-character template.
- TweakXL 1.11.3, the applied generated appearance, and the restored
  `Character.GhostlinePatch` registry are installed and runtime-confirmed.
- Continue custom-pathing or replacing Patch dependencies only if missing
  resource hashes change or Patch-specific crashes remain.

### 4. Extend The Quest Beyond Acceptance

- The first cache slice after `job_accept` is implemented through native breach
  success, readable-shard grants, `gq000_cache_acquired`, a visible leave-area
  beat, and delayed guard cleanup.
- Runtime testing confirms all three guards spawn, the native breach succeeds,
  both readable shards and Journal entries work, and the leave-area transition
  completes. The final guard test also confirmed close placement, finite patrol,
  proximity hostility, absolute yaw `178.6`, terminal-specific extract pin,
  and surviving-guard cleanup together.
- Kabuki `drop_point_009`, the separate quest package, native reservation and
  deposit fact, yellow delivery UI marker, Morrow thread, completion reward,
  and quest success are implemented and runtime-confirmed. The prior target
  was physically occluded, and ArchiveXL could not resolve its direct cooked
  mappin. The first successful complete route exposed only presentation state:
  the custom pin rendered near the entity root and a stale dotted GPS leg
  continued toward the bridge. The next candidate uses the native two-unit
  interaction height and clears previous mappins when delivery activates.
- Keep prefab NodeRef lifecycle aligned with the resolved model in
  `docs/world-references.md`.

### 5. Validate Audio Packaging

- All 13 current subtitles, VO-map entries, and `.wem` assets played correctly
  in the stable meeting route. Revalidate that alignment after future dialogue,
  scene-line, or audio-map edits.
- Add Ghostline-owned lipsync resources if the final scene presentation needs
  them.

### 6. Pack And Test In Game

- The 2026-07-23 delivery GPS/height candidate is generated, deserialized,
  byte-identical after CR2W round trips, packed, extracted, payload-verified,
  installed, and wrapped in a verified seven-file ZIP. All 103 tests pass.
  Relative to the complete runtime-confirmed route, exactly the delivery phase
  and journal changed: delivery activation now clears stale mappin/GPS state,
  and the yellow pin uses the native two-unit interaction height. Installed
  archive SHA-256 is
  `7C3BB9844EE0DD8BC65C1883D61AD0307E89593DFBFC69A8EFF2B7C504D93590`;
  ZIP SHA-256 is
  `92B71E698F9C4BE9EAF58597463B3A9BC931A84540EF2EE18C411F10CA95771C`.
  Evidence is retained at
  `H:\Ghostline-builds\gps-marker-fix-20260723-002208` and
  `H:\Ghostline-audits\gps-marker-fix-roundtrip-20260723-002032`; the replaced
  install is backed up at
  `H:\Ghostline-backups\pre-gps-marker-fix-20260723-002543`.
- The preceding accessible `drop_point_009` candidate is generated,
  deserialized, byte-identical after CR2W round trips, packed, extracted,
  payload-verified, installed, and wrapped in a verified seven-file ZIP. All
  103 tests pass. All 175 archive entries match `source/archive`, and all seven
  ZIP/installed files match `packed`. Relative to the preceding delivery
  candidate, exactly the delivery phase, journal, and always-loaded marker
  sector changed. Installed archive SHA-256 is
  `1C669335E83C93F714455D24743C7F03E34F2FA381A60ABB9E8F35A85375EDCC`;
  ZIP SHA-256 is
  `D3F32A60C789030FB47BA9C3C06C9E48DBB7097F2F786EB858EF8551D3764275`.
  Evidence is retained at
  `H:\Ghostline-builds\drop-point-009-yellow-20260722-234109` and
  `H:\Ghostline-audits\drop-point-009-roundtrip-20260722-233650`; the replaced
  install is backed up at
  `H:\Ghostline-backups\pre-drop-point-009-20260722-234356`.
- The 2026-07-22 delivery/debrief candidate is generated, deserialized,
  byte-identical after CR2W round trips, packed, extracted, payload-verified,
  installed, and wrapped in a verified seven-file ZIP. All 98 tests pass. The
  175-entry archive matches all packable payloads from the 178-file
  `source/archive` tree; only the known Patch `.tmp` and two head readmes are
  excluded. Relative to the runtime-confirmed hostility build, exactly four
  payloads changed (`gq000.questphase`, `gq000_post_accept.questphase`, the
  journal, and quest onscreen localization) and one payload was added
  (`gq000_delivery.questphase`). All ZIP and installed files match `packed`.
  Installed archive SHA-256 is
  `0F971F97877421C181C5D4B114F5090D015DEE97B3FE7FFCF9091F57FD476158`;
  ZIP SHA-256 is
  `03BF484092377E5B022B9BE4867B1383544B46B24BA4769291904EC93395FBBB`.
  Evidence is retained at
  `H:\Ghostline-builds\delivery-morrow-20260722-224211`; the replaced install
  is backed up at
  `H:\Ghostline-backups\pre-delivery-morrow-20260722-224211`.
- The 2026-07-22 explicit-player hostility candidate is generated,
  deserialized, packed, extracted, payload-verified, installed, and wrapped in
  a verified seven-file ZIP. It preserves the runtime-proven patrol, terminal,
  breach, shard, and cleanup resources byte-for-byte, changing only
  `gq000_post_accept.questphase` from the preceding test build. The new
  43-node/44-edge phase applies the per-entry vanilla `mq022` hostility
  sequence and explicitly targets `#player`. All 88 tests pass, the changed
  CR2W round-trips byte-identically, all 174 archive payloads match
  `source/archive`, and all seven ZIP/installed files match `packed`. Installed
  archive SHA-256 is
  `18D56C1F20C3600AFBA385BE4F6678D58825D0E29E5A350C72FA48FF4227B3E2`;
  ZIP SHA-256 is
  `D5FAC9FE9CE7DA060CDA3CA79114552D89D9D6BF7C2ED7699D999DBD65645674`.
  Evidence is retained at
  `H:\Ghostline-builds\guard-hostility-mq022-20260722-214120`; the replaced
  install is backed up at
  `H:\Ghostline-backups\pre-guard-hostility-mq022-20260722-214120`.
- The preceding hostile-guard/patrol candidate remains at
  `H:\Ghostline-builds\cache-encounter-hostile-patrol-20260722-205717`.
  Runtime confirmed every intended world/presentation change but proved its
  null-target border-patrol threat pulse did not make the guards aggressive.
- The 2026-07-22 cache-encounter candidate has been generated, deserialized,
  structurally round-trip checked, packed, extracted, payload-verified,
  installed, and wrapped in a verified six-file ZIP. Installed archive SHA-256
  is `888E678162D6086124E1CC8AE3CDB39D58697129289A24C5E9DC15B53EEF2D05`;
  ZIP SHA-256 is
  `D4628E6652567DFE46CF9E1D707D002F5B436515F7C4ACE8D544AA3900CF8A69`.
  Build evidence is retained at
  `H:\Ghostline-builds\cache-encounter-candidate-20260722`, and the previous
  installation is backed up at
  `H:\Ghostline-backups\pre-cache-encounter-20260722-191442`.
- The 2026-07-22 custom Patch build has been deserialized, structurally or
  byte-for-byte round-trip checked, packed, extracted, payload-verified,
  installed, and wrapped in a
  verified six-file ZIP. Installed archive SHA-256 is
  `40148CE9F102C5CF77BEA31C1D9043FB20F53B8937873235BDBE3D1A82EF6786`.
- The subsequent cache runtime-fix candidate corrects the guard-community
  streaming origin and relay yaw, adds the minimal device registry and readable
  shard items, and makes `gq000_cache_acquired` precede presentation cleanup.
  The final installed revision also disables Patch's inherited `t0_peen` and
  `t0_pubic_hair` components in both appearance copies; `patch.app` is its only
  archive delta from the otherwise identical cache candidate. All 75 automated
  tests pass. Its 174-entry archive was extracted and matched
  byte-for-byte against the intended `source/archive` payloads; all seven ZIP
  and installed payloads match the staged tree. Installed archive SHA-256 is
  `2C5179349DBD1AFF5A5A01123F83FF1DC76D8D91E45FE946CEA4DCAF0166BF80`,
  and ZIP SHA-256 is
  `73B3C28C525DF298878FA011D5B8D9E79AF03C4FB35CAC740E8064A96CBDAB7C`.
  Evidence is retained at
  `H:\Ghostline-builds\patch-genital-visibility-20260722-202817`, with the
  underlying cache round trips at
  `H:\Ghostline-builds\cache-runtime-fix-20260722-201715`; the replaced
  installation is backed up at
  `H:\Ghostline-backups\pre-patch-genital-visibility-20260722-202817`.
- Test the delivery/debrief candidate from a pre-Ghostline save. After leaving
  the relay area, confirm the Kabuki drop-point objective and marker appear,
  the machine offers the datacache deposit, deposit removes the package and
  advances the quest, Morrow sends both opening messages, either V reply gets
  only its matching response, the final message and completion reward arrive,
  and `GHOSTLINE` moves to Completed.
