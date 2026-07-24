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
| `hack_access_point` | template | `device`, `success_fact` |
| `deliver_drop_point` | template | `item`, `drop_point`, `deposit_fact` |
| `interact_device` | generated | `device`, `controller_class`, `action`, `completion_function` |
| `combat_encounter` | generated | `community`, `entries`, `hostility`, `completion` |
| `investigate_clues` | generated | `objective`, `description_entry`, `clues` |
| `optional_condition` | template | `objective`, `condition`, `success_fact`, `failure_fact`, `evaluation` |
| `choice_gate` | template | `gate_kind`, `branches`, `join` |
| `escort_npc` | template | `community`, `entry`, three `destinations`, `objective`, `completion_fact` |
| `carry_npc` | template | `community`, `entry`, `destination`, `objective` |
| `deliver_vehicle` | template | `vehicle`, `destination`, `objective` |
| `time_gate` | generated | A non-zero combination of `days`, `hours`, `minutes`, and `seconds`; optional `completion_fact` |
| `read_terminal_document` | template | `computer`, `completion_fact`, `objective`; optional `scene`, `output_socket`, `document_entry` |
| `stealth_monitor` | template | `objective`, `failure_fact`, `success_fact`, `stop_fact` |
| `plant_item` | template | `item`, device action/condition fields, `completion_fact`, `objective` |
| `defend_target` | template | `community`, `entry`, `completion_fact`, `failure_fact`, `objective` |
| `release_or_rescue_npc` | template | target fields, device action/condition fields, `completion_fact`, `objective` |
| `enter_vehicle` | template | `vehicle`, `objective` |
| `ride_with_contact` | template | `vehicle`, `contact_community`, `contact_entry`, `objective` |
| `drive_to` | template | `vehicle`, `destination`, `completion_fact`, `objective` |
| `steal_vehicle` | template | `vehicle`, `objective` |
| `vehicle_cleanup` | template | `player_vehicle_record`, `completion_fact` |

`generated` means the compiler constructs the complete child graph from typed
fields. `template` means it resolves a reduced raw CR2W-JSON template,
performs exact scalar replacement, validates the handle graph, and checks the
typed contract after instantiation. The eleven advanced complex blocks resolve
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
signals. The vehicle lifecycle is split into mounting, riding with a contact,
driving to a trigger, stealing by mounting, and player-vehicle cleanup.
`vehicle_cleanup` uses the `sq031_porsche` player-vehicle record shape and is
not a generic despawner for arbitrary world NodeRefs.

`investigate_clues` accepts any positive number of ordered clues. Each clue
has its own object reference and may set a fact, activate a map pin, or reveal
a journal entry; the generated phase joins every required scan before
completing. A partial threshold (`required_count < clue count`) still requires
an explicit custom phase because it changes the graph from an all-of join.

`combat_encounter` activates the whole community, waits for its entries to
spawn, injects the player as a combat threat for every named entry, waits until
all are defeated, and optionally deactivates the community. This is the
runtime-proven hostility pattern used by Ghostline's Tyger Claw encounter.

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
`source/quests/examples/phone_conversation.quest.json` is the standalone
authoring example.

`source/quests/examples/direct_building_blocks.quest.json` compiles all four
generated blocks. `source/quests/examples/template_building_blocks.quest.json`
compiles the original eight building-block stages without author-written
template paths or placeholder maps. The advanced-template regression suite
instantiates every built-in template, including the eleven advanced blocks.

The orchestration layer remains intentionally linear. `choice_gate` is a
converging child block: its alternatives must rejoin before `Out1`.
`optional_condition` evaluates inside its child phase rather than running as a
parallel monitor. Dialogue choices remain inside scene or phone blocks;
combat, breach outcomes, and deposit completion remain inside their child
phases. A future schema version can add named stage outcomes and graph edges
without changing these linear manifests.

## Commands

```powershell
py -B .\tools\quest_compiler.py validate `
  .\source\quests\gq001.quest.json

py -B .\tools\quest_compiler.py compile `
  .\source\quests\gq001.quest.json `
  --out .\converted\quests\gq001\gq001.questphase.json `
  --allow-planned
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

`source/quests/gq001.quest.json` represents:

```text
meet Patch -> hack relay -> meet Iris -> deliver datacache
```

It instantiates the three runtime-proven `gq000` block topologies with
`gq001`-local facts, journal paths, scene paths, actor identity, and completion
state. It marks the new Iris meeting as planned because its scene, world
placement, journal tree, and localization are not authored yet. This remains a
composition/tooling fixture rather than a playable second quest, but every
orchestration and child questphase is concrete and WolvenKit-importable.
