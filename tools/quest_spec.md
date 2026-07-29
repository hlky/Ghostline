# Typed Quest Manifest

`tools/quest_compiler.py` defines the first high-level composition layer for
Ghostline quests. It compiles the linear orchestration graph and its child
questphases. Runtime-proven meeting, hacking, and delivery phases are
instantiated from raw CR2W-JSON templates with exact scalar bindings. Phone
conversation, device interaction, combat, and variable-size investigation
phases are generated directly from typed fields. Scene, world, journal, and
localization resources remain separate authored products.

This boundary makes a quest reviewable before every asset exists without
pretending that a planned scene is playable. A `planned` stage is permitted by
validation and shown in the generated build plan, but ordinary compilation
rejects it. `--allow-planned` emits a non-shipping prototype orchestration
phase for graph inspection.

`tools/quest-schema-v1.json` is the editor-facing JSON Schema. The compiler
also performs its own strict validation so command-line builds do not depend on
an editor or an optional schema library.

## Stage Types and implementation boundary

| Type | Implementation | Required typed fields |
| --- | --- | --- |
| `phone_job_offer` | generated | `contact`, `message`, `choice_group`, `accept_choice`, `start_fact`, `accepted_fact` |
| `phone_conversation` | generated | `contact`, `thread`, `messages`, `choice_group`, `choices`, `final_message` |
| `reach_area` | generated | `trigger`, `objective`, `description_entry`, `mappin` |
| `leave_area` | generated | `trigger`, `objective`, `description_entry` |
| `acquire_item` | generated | `item`, `source` |
| `read_shard` | generated | `item`, `journal_entry`, `file_entry_index`; use `acquisition_fact` for readable shards that are consumed into the Journal and `presentation_delay_seconds` when the pickup overlay needs time |
| `meet_contact` | template | `contact`, `scene`, `community`, `objective`, `description_entry`, `mappin` |
| `hack_access_point` | template or generated | `device`, `success_fact`; adding the device action/condition fields selects the generated form |
| `deliver_drop_point` | template or generated | `item`, `drop_point`, `deposit_fact`; two `item_branches` select outcome-dependent inventory |
| `interact_device` | generated | `device`, `controller_class`, `action`, `completion_function` |
| `combat_encounter` | generated | `community`, `entries`, `hostility`, `completion` |
| `cyberpsycho_encounter` | generated | `community`, `boss_entry`, `boss_character`, `activation_trigger`, `reveal`, `resolution` |
| `investigate_clues` | generated | `objective`, `description_entry`, `clues` |
| `optional_condition` | template | `objective`, `condition`, `success_fact`, `failure_fact`, `evaluation` |
| `choice_gate` | template | `gate_kind`, `branches`, `join` |
| `escort_npc` | template | `community`, `entry`, three `destinations`, `objective`, `mappin`, optional three `route_mappins`, `completion_fact` |
| `carry_npc` | template | `community`, `entry`, `destination`, `objective` |
| `deliver_vehicle` | template | `vehicle`, `destination`, `objective` |
| `time_gate` | generated | A non-zero combination of `days`, `hours`, `minutes`, and `seconds`; optional `completion_fact` |
| `read_terminal_document` | template | `computer`, `completion_fact`, `objective`; optional `scene`, `output_socket`, `document_entry` |
| `stealth_monitor` | template | `objective`, `failure_fact`, `success_fact`, `stop_fact` |
| `plant_item` | template | `item`, device action/condition fields, `completion_fact`, `objective` |
| `defend_target` | template | `community`, `entry`, `completion_fact`, `failure_fact`, `objective`; `block_on_failure` selects the retry-safe variant |
| `release_or_rescue_npc` | template | target fields, device action/condition fields, `completion_fact`, `objective` |
| `enter_vehicle` | template | `vehicle`, `objective` |
| `ride_with_contact` | template | `vehicle`, `contact_community`, `contact_entry`, `objective` |
| `drive_to` | template | `vehicle`, `destination`, `completion_fact`, `objective` |
| `steal_vehicle` | template | `vehicle`, `objective`, `completion_fact` |
| `vehicle_cleanup` | template | `player_vehicle_record`, `completion_fact` |
| `braindance_analysis` | template | `scene`, `scene_origin`, safe `player_anchor`, `player_replacer`, three `clue_facts`, `objective`, `completion_fact` |

`generated` means the compiler constructs the complete child graph from typed
fields. `template` means it resolves a reduced raw CR2W-JSON template,
performs exact scalar replacement, validates the handle graph, and checks the
typed contract after instantiation. The thirteen advanced complex blocks resolve
Ghostline-owned built-in templates automatically; authors normally provide
only the typed fields shown above. An explicit `phase_template` plus
`template_bindings` can override the built-in for an advanced shape.
Template-backed does **not** mean that an arbitrary whole vanilla phase is
reusable. The research corpus and provenance map live under
`reference/vanilla_quest_blocks`.

Every stage also requires:

- a unique lowercase `id`;
- a `status` of `ready` or `planned`; and
- a child `phase_resource` exposing conventional `In1` and `Out1` sockets.

A stage may narrow the quest-level prefab list with `phase_prefabs`; an empty
list deliberately binds no world prefab. `checkpoint` inserts a root checkpoint
immediately before the stage, and `retry_checkpoint: true` sets its
`retryOnFailure` contract. Use the latter with a failure-blocking child rather
than allowing a failed defense to emit normal progression.

`required_assets` provides additional depot paths that must exist before a
ready stage can compile. Missing resources are errors for `ready` stages and
warnings for `planned` stages.

Template bindings replace complete scalar values only; substring rewrites are
intentionally forbidden. Compilation rejects an unused binding, duplicate
`HandleId` values, dangling `HandleRefId` values, or a generated child that
does not contain its typed runtime identifiers. This preserves proven graph
topology while making quest-local facts, journal paths, scene paths, actor
identities, NodeRefs, device actions, AI destinations, and completion state
explicit.

The remaining built-in template shapes are intentionally narrow:

- optional condition is one fact evaluated when the block is reached;
- choice is two fact-backed branches that reconverge;
- escort sets one named companion to gameplay AI and observes exactly three
  ordered trigger gates;
- carrying requires the named NPC mounted to V inside a destination trigger;
- vehicle delivery requires the vehicle inside a destination trigger and
  stopped.

`read_terminal_document` waits on `completion_fact`. A custom computer scene
may expose `output_socket` and route it to that fact. Native computer files can
instead use `gamedeviceDataElement.questInfo.factName`, which is the direct
vanilla document-read signal used by `gqt001_signal_delay`;
the phase cannot infer a read from generic journal state.

`stealth_monitor` and `defend_target` race explicit success/stop and failure
signals and preserve the result. Their surrounding encounter owns those
signals. With `block_on_failure`, the defend child fails the objective and sets
the failure fact but does not emit `Out1`; pair it with a retry-enabled
checkpoint and confirm reload behavior in game. The vehicle lifecycle is split
into mounting, riding with a contact, driving to a trigger, stealing by
mounting and setting its completion fact, and player-vehicle cleanup.
`vehicle_cleanup` uses the `sq031_porsche` player-vehicle record shape and is
not a generic despawner for arbitrary world NodeRefs.

`braindance_analysis` owns the active review objective, rewindable braindance
playback, and completion. It activates `objective` before entering the
recording. The three `clue_facts` correspond to the visual, audio, and thermal
scan branches; all three must be greater than zero before the block succeeds
the objective and sets `completion_fact`. Scene `complete`, `end`, and
interruption exits own cleanup only, so Close cannot falsely complete the
analysis.
Compose it after `meet_contact` when an NPC should offer the recording; the
existing contact block owns community activation, spawn readiness, approach
gating, actor-attached choice presentation, and scene-exit handoff.
The running scene owns interaction distance and presentation instead of
depending on a separate quest trigger. Its `play_braindance` exit
clears the approach map pin and sets the handoff fact without changing the
review objective, then starts the rewindable `scene` at the same origin. The
block does not synthesize a braindance: both `.scene` files, the `.scenerid`,
actor records, and world marker remain explicit stage-owned resources.

`investigate_clues` accepts any positive number of ordered clues. Each clue
has its own object reference and may set a fact, activate a map pin, or reveal
a journal entry; the generated phase joins every required scan before
completing. A partial threshold (`required_count < clue count`) still requires
an explicit custom phase because it changes the graph from an all-of join.

`combat_encounter` activates the whole community, waits for its entries to
spawn, injects the player as a combat threat for every named entry, waits until
all are defeated, and optionally deactivates the community. This is the
runtime-proven hostility pattern used by Ghostline's Tyger Claw encounter.

`cyberpsycho_encounter` is the named single-boss counterpart. It waits for the
outer activation trigger, optionally activates the community, waits for the
declared boss entry, and makes that entry invulnerable while the configured
reveal routes race. Reveal routes may include a dedicated trigger, scanning the
boss, the boss attacking the player, the player hitting the boss, and the boss
seeing the player. After reveal and the optional arena trigger, the phase makes
the boss mortal and injects the player as a combat threat.

Resolution is deliberately nonlethal-aware. A lethal-only
`questCharacterKilled_ConditionType` sets `resolution.killed_fact`; a separate
unconscious-or-defeated condition sets `resolution.spared_fact`. The two routes
rejoin before the optional objective, mappin, completion fact, and cleanup.
`allow_nonlethal` must remain `true`, and the two facts must differ.

The large HUD overlay is not a quest node. It is the standard boss health bar
raised for a hostile tracked NPC whose character record has
`rarity: NPCRarity.Boss`. The same record should explicitly carry the
`Cyberpsycho` tag, Cyberpsycho modifier groups, combat nameplate, scanner, and
target-tracking presets. Add optional `authoring.world_spec` and
`authoring.tweak_file` workspace-relative paths to make the compiler audit the
community/entry, inactive-on-start lifecycle, encounter NodeRefs, boss rarity,
tag, modifier groups, and HUD/scanner presets before a ready build.

The generated block owns only the fight lifecycle. Evidence collection, fixer
reporting, reward, journal completion, and delayed cleanup remain later
composable stages. See
`quests/examples/cyberpsycho_encounter.quest.json` and
`docs/reference/vanilla-cyberpsycho-encounters.md`.

`read_shard` deliberately completes from ownership of the readable item, not
from a journal `visited` condition. Vanilla minor activities with objectives
named `read_shard` (`ma_wat_lch_03`, `ma_wat_lch_05`, and `ma_wat_lch_15`)
likewise use inventory, loot, or interaction state and do not wait for
`questJournalEntryVisited_ConditionType`. The pickup-notification preview and
the full Journal reader are separate UI paths; only the latter reliably sets
the visited state. Computer pages and emails can use device/UI-specific
progress signals and should be represented by a separate terminal-reading
block rather than this inventory-shard block.

Use an explicit custom template for broader variants. Companion movement AI,
community/world placement, device setup, carry interactions, and vehicle
spawning remain separate authored assets rather than hidden compiler behavior.

Phone choices are objects with paired `choice` and `reply` journal paths. The
generated graph activates the initial messages in order, waits on every choice
branch, optionally sets the choice's `set_fact`, joins the selected reply,
sends `final_message`, waits until it has been visited, optionally sets
`completion_fact`, and exits through `Out1`.
An optional `opening_branches` array can insert fact-conditioned message
sequences between the common opening messages and the response group. This is
the generated pattern for outcome-specific debriefs: each branch contains a
unique `condition` fact and one or more journal `messages`, and all branches
reconverge before the shared choices.
`conditional_message_groups` generalizes this to multiple sequential
fact-conditioned groups, avoiding a cross-product for independent outcomes.
`postscript_messages` activates additional messages after the required final
message without making them separate progression gates. Journal paths may
belong to different contacts, so alternating Morrow/Iris exchanges do not
require a custom child phase.
`quests/examples/phone_conversation.quest.json` is the standalone
authoring example.

`quests/examples/direct_building_blocks.quest.json` exercises the
general generated blocks, and
`quests/examples/cyberpsycho_encounter.quest.json` demonstrates the
specialized boss lifecycle. `quests/examples/template_building_blocks.quest.json`
compiles the original eight building-block stages without author-written
template paths or placeholder maps. The advanced-template regression suite
instantiates every built-in template, including the thirteen advanced blocks.

The orchestration layer is linear except for declared `parallel_groups`. Each
group replaces one contiguous stage span with two or more ordered branches and
joins every branch through a logical all-of before progression resumes. A
stage may belong to only one group; meeting stages, checkpoints, and debug-fact
instrumentation are intentionally rejected inside a group.
`choice_gate` is a converging child block: its alternatives must rejoin
before `Out1`.
`optional_condition` evaluates inside its child phase rather than running as a
parallel monitor. Dialogue choices remain inside scene or phone blocks;
combat, breach outcomes, and deposit completion remain inside their child
phases. `interact_device.outcome_branches` can perform fact-selected inventory
mutations and set outcome facts after one common device completion.

## Commands

```powershell
py -B .\tools\quest_compiler.py validate `
  .\quests\story\ghostline\gq001\implementation\quest.json

py -B .\tools\quest_compiler.py compile `
  .\quests\story\ghostline\gq001\implementation\quest.json `
  --out .\converted\quests\gq001\gq001.questphase.json
```

The compiler writes:

- a deterministic orchestration `.questphase.json`; and
- generated child `.questphase.json` files under a neighboring `children/`
  tree matching their depot paths; and
- a neighboring `.questphase.plan.json` containing normalized stage order,
  node IDs, typed inputs, diagnostics, and shipping readiness.

Generated prototype output stays under ignored `converted/`. Moving an
orchestration phase into `source/raw`, deserializing it, or registering it with
ArchiveXL is a separate explicit promotion step after every stage is ready.

## Current Acceptance Manifest

`quests/story/ghostline/gq001/implementation/quest.json` represents:

```text
meet Patch -> hack relay -> meet Iris -> deliver datacache
```

It instantiates the three runtime-proven `gq000` block topologies with
`gq001`-local facts, journal paths, scene paths, actor identity, and completion
state. The Iris scene, world placement, journal tree, and localization are now
authored. `gq001` extends and replaces the `gq000` prototype as the first
canonical Ghostline story quest.
