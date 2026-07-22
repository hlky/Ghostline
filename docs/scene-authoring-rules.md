# Vanilla Scene Authoring Rules

These are the target rules for fresh `gq000` scene creation tooling. They are
based on local vanilla extracts under `reference/vanilla_extract_json` and
world/journal references under `reference/world` and `reference/journal`.

For the concrete Ghostline root phase, meeting phase, scene, trigger, exit, and
localization handoff, read `docs/quest-scene-flow.md` first.

If a vanilla pattern crashes in a Ghostline probe, assume the Ghostline
implementation was incomplete or malformed. Do not replace a vanilla pattern
with a workaround from a bad probe unless a matching vanilla counterexample has
been found.

## Source Of Truth

- Fresh scene tooling should emit editable CR2W-JSON under `source/raw`.
- Packed `source/archive` CR2W resources should be produced by WolvenKit from
  that raw source. Do not text-edit packed archive resources.
- `generated` snapshots and old probe-built scene shapes are not valid inputs
  for new scene tooling unless a specific field has been revalidated against a
  vanilla extract.
- Use local vanilla extracts as structural templates. Prefer cloning and
  adapting complete vanilla node/section/choice shapes over reconstructing
  hidden fields from memory.
- Keep WolvenKit graph/editor state separate from packable scene data.

## Audited References

- `reference/vanilla_extract_json/mq003/mq003_01_homeless.scene.json`
- `reference/vanilla_extract_json/mq003/mq003_03_orbital_pod.scene.json`
- `reference/vanilla_extract_json/mq007/mq007_01_gun_found.scene.json`
- `reference/vanilla_extract_json/mq010/mq010_02_barry_talk.scene.json`
- `reference/world/000`
- `reference/journal/quests.minor_quest.mq003_orbitals.journal.json`
- `reference/journal/points_of_interest.minor_quests.journal.json`

## Minimum Fresh Tooling Contract

A fresh `gq000_patch_meet.scene` generator should produce a complete,
vanilla-shaped scene resource with:

- root scene metadata, resource references, and debug symbols;
- actor definitions for Patch and V;
- entry, section, choice, optional-branch, and output graph nodes;
- graph sockets and edges copied from compatible vanilla patterns;
- screenplay lines and options using vanilla item ID patterns;
- section events and timing copied from coherent vanilla section shells;
- choice locStore descriptors with vanilla multi-locale coverage;
- valid journal paths and world NodeRefs for any optional scene-local
  journal/mappin nodes;
- raw output under `source/raw`, followed by WolvenKit deserialization to
  `source/archive`.

The current production meeting scene intentionally contains no journal or
mappin nodes. Acceptance objective, mappin, and fact side effects belong to the
meeting questphase after the named `job_accept` exit.

The generator should fail closed when a required vanilla-shaped structure is
unknown. Do not fill unknown structural fields with placeholders just to make a
CR2W-JSON file deserialize.

Current implementation:

- `tools/generate_scene.py` is the fresh scene generator.
- `tools/gq000_patch_meet.scene-spec.json` is the first production fixture.
- `tools/scene_spec.md` documents the supported v1 spec fields.
- V1 covers dialogue scenes, actor acquisition, choice locStore coverage,
  scene-local journal/mappin/trigger/AI quest nodes, validation, and optional
  WolvenKit deserialization. It intentionally does not author animation-heavy
  cinematic events or rewrite world marker hierarchy.

## Root Scene Shape

- Use `version: 5`.
- Use `cookingPlatform: PLATFORM_PC`.
- Use `sceneCategoryTag: minorQuests` for `gq000` unless a closer vanilla
  Ghostline target proves another category.
- Use a stable `Header.ExportedDateTime` from the scene spec so regenerated
  raw CR2W-JSON and deserialized CR2W outputs are reproducible.
- Keep `debugSymbols.performersDebugSymbols`.
- Actor debug symbols use `actorID * 256 + 1`.
- Prop debug symbols use `propID * 256 + 2`.
- Entry point socket names must match the questphase scene node input. The
  current questphase starts the meeting scene through `start`.
- Do not inherit unrelated template resource references. Resource tables should
  contain only resources actually referenced by actors/events in the scene.

Current Ghostline generated scene follows these root values: `version: 5`,
`cookingPlatform: PLATFORM_PC`, and `sceneCategoryTag: minorQuests`.

## Actors

- Community-spawned NPCs should use `acquisitionPlan: community`.
- Community actor definitions should set:
  - `communityParams.reference` to the streamable community area NodeRef.
  - `communityParams.entryName` to the active community entry.
- Questphase flow should not start a dialogue scene that depends on a community
  actor until a `questCharacterSpawned_ConditionType` pause condition has
  passed for that actor/community NodeRef. For multiple required actors, use
  parallel spawn waits and an `And` rendezvous, matching vanilla scene patterns.
- For proximity conversations, follow the `mq003` lifecycle: activate and
  validate the community before proximity, start the scene from the broad setup
  trigger, and keep narrower mood/awareness/engage waits inside the already
  running scene. Do not launch a scene only after every narrower concentric
  trigger is already true; that collapses setup and dialogue into one startup
  tick.
- Player actors should use `findInContext` with
  `Character.Player_Puppet_Base`.
- Keep actor IDs, `performerID` references in sections, and
  `screenplayStore.lines.actorID` references aligned.

## Lipsync Resource References

- An actor's `lipsyncAnimSet.id` indexes
  `resouresReferences.lipsyncAnimSets`; every referenced ID must exist at
  runtime.
- Audited two-performer vanilla scenes normally use separate NPC and V lipsync
  `.anims` resources. Do not create two logical slots by repeating one depot
  path unless a matching cooked vanilla case proves the runtime table remains
  addressable.
- Runtime testing confirmed that Ghostline's shared slot `0` configuration
  stabilizes scene startup and completes the full meeting route. It remains a
  crash-isolation baseline, not final presentation. Replace it with distinct,
  valid NPC/V resources only when both runtime slots remain independently
  addressable after cooking.

## Screenplay IDs

Audited vanilla scenes use this screenplay item pattern:

- Spoken dialogue lines: `1 + 256n`.
- Player choice options: `2 + 256n`.

Fresh tooling should emit that pattern. If changing Ghostline line item `0` to
`1` crashes, treat that as a surrounding scene/section/event mismatch, not as
evidence against the vanilla item ID pattern.

Current Ghostline generated scene uses the `1 + 256n` spoken-line pattern.

## Dialogue Events

- `scnDialogLineEvent` IDs must be normal unique scene event IDs, not generated
  max-int placeholder values.
- Dialogue event performer IDs, screenplay line actor IDs, subtitle string IDs,
  and VO map entries must describe the same speaker/line.
- Do not treat a line payload as bad if it plays correctly in a known-good
  vanilla-shaped section shell. Fix the section/event shell first.

## Sections

- Build section nodes from a known-good vanilla section shape.
- Preserve relevant hidden fields when cloning/adapting section nodes, including
  section duration, output socket shape, actor behavior arrays, event timing,
  and debug symbol references.
- Do not draw broad conclusions from empty or generated sections. Vanilla
  dialogue sections have coherent event arrays and performer references.

## Choice Nodes

Vanilla choice nodes use padded output sockets:

- One option socket for each option:
  - socket stamp `name: 0`
  - ordinal `0..option_count-1`
- Six trailing dummy sockets:
  - socket stamp names `1` through `6`
  - ordinal `0`

Fresh tooling should emit `option_count + 6` output sockets for each choice
node.

Choice options should reference `screenplayOptionId` values from
`screenplayStore.options`, using the vanilla option item ID pattern
`2 + 256n`.

Do not use these as global rules:

- `persistentLineEvents` must be empty.
- Physical option array order cannot change.

Vanilla counterexamples exist:

- `persistentLineEvents` are populated on many vanilla choices.
- Optional/info choices commonly use `type.properties: 0` with
  `isSingleChoice: 0`.
- Required/progression choices commonly use `type.properties: 1`, but special
  interactions use other values such as `257` or `769`.

For new tooling, copy the choice semantics from the closest vanilla case rather
than deriving color, optionality, or progression from one field in isolation.

Current Ghostline production choice shape:

- Choice nodes include six trailing dummy sockets.
- Choice locStore coverage includes `db_db`, `pl_pl`, and `en_us`.
- The first choice group uses `isSingleChoice: 0` for all three options,
  `type.properties: 0` for optional/info branches, and `type.properties: 1`
  for the main progression branch.

## Choice Localization

Audited vanilla choice locstrings include embedded locStore descriptor variants
for `db_db`, `pl_pl`, and `en_us`. Choice locStores are grouped by locale block,
not by option, and all four audited scenes sort each block by unsigned numeric
`locstringId`. Ghostline's unsorted build displayed blank and stale labels, so
the current tooling treats numeric block order as required. The sorted
candidate still needs runtime confirmation before that causality is considered
fully isolated. `db_db` usually has two descriptors per choice: a blank
fallback payload and a source text payload.

Fresh tooling should generate the same multi-locale descriptor shape for choice
locstrings. Do not replace `db_db` with `en_us`; add the correct vanilla-style
locale coverage. Validate the checked-in raw scene as well as an in-memory
generator fixture so stale unsorted CR2W-JSON cannot pass the build tests.

`scnChoiceNodeOption.caption` is an authoring/debug label, not the authoritative
display text. The full option-to-payload lookup chain, descriptor/payload
relationship, ID domains, and current sorted Ghostline IDs are documented in
`docs/quest-scene-flow.md`.

Do not truncate generated scene event RUIDs or locStore variant IDs to the
signed 63-bit range. Runtime testing showed `INT63_MASK`-generated scenes crash
on approach while the same scene generated with full unsigned 64-bit FNV RUIDs
is stable.

## Xor And Hub Nodes

Vanilla `mq003_01_homeless.scene` uses `scnXorNode` and `scnHubNode`.

Do not ban `Xor` because a Ghostline probe crashed. A crash means the tested
node or surrounding graph shape was wrong. If a fresh scene needs `Xor` or
`Hub`, copy a verified vanilla-compatible node shape and preserve its socket
structure.

## Journal And Mappin Scene Nodes

- Journal description nodes may depend on preceding objective activation.
  Follow the vanilla quest chain rather than activating description nodes in
  isolation.
- Mappin manager scene nodes are valid when their journal and world references
  are valid.
- Scene-local mappin setup should follow the relevant vanilla quest chain.
- `gameJournalPath.fileEntryIndex` is the zero-based path component index of the
  containing `gameJournalFileEntry`. It is not the leaf index or CR2W handle.
  For `quests/minor_quest/gq000/...`, the containing file entry is
  `gq000` at index `2`, so objectives, descriptions, and quest map pins under
  that quest use `fileEntryIndex: 2`. For
  `points_of_interest/minor_quests/...`, the containing file entry is
  `minor_quests` at index `1`, so POI journal nodes use `fileEntryIndex: 1`.

## World Marker Rules

Vanilla mq003 separates scene markers and map-pin markers:

- Scene marker example:
  `#mq003_pr_homeless/mq003_01_homeless_prefab.../#mq003_01_sm_homeless`
- Map-pin marker example:
  `#mq003_pr_homeless/#mq003_mp_homeless`

Target Ghostline shape:

- Scene marker: keep `#gq000_01_sm_patch_bridge` as the scene marker, but place
  it under a scene-prefab child path when rebuilding world data to match mq003.
- Map-pin marker: keep `#gq000_01_mp_patch_bridge` directly under
  `#gq000_pr_patch_meet` for quest map pin and POI static mappin references.
- Do not point journal mappins at the scene marker.

Current Ghostline mismatch to fix in fresh tooling:

- The current scene marker is registered directly under
  `#gq000_pr_patch_meet`, not under a nested scene prefab path.

## Community Lifecycle

The Object Spawner-style reference uses `entryActiveOnStart: 1`. Ghostline uses
`entryActiveOnStart: 0`; runtime testing confirmed that the meeting phase can
activate the Judy isolation entry, wait for the same community to spawn, and
complete the full route. That result does not by itself make the registry shape
vanilla or validate the custom Patch character.

Fresh tooling should copy a complete vanilla-compatible lifecycle:

- always-loaded registry,
- streamable community area,
- AI spot,
- an explicit questphase decision for activation and eventual
  deactivation/retention,
- scene actor community acquisition.

Do not label `entryActiveOnStart: 0` as vanilla until a matching vanilla quest
registry and activation pair has been extracted and compared.

The current meeting phase has no explicit `Deactivate` action. Final quest
design must decide when the Patch community should be released or retained.
