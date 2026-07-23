# Typed Quest Manifest

`tools/quest_compiler.py` defines the first high-level composition layer for
Ghostline quests. It compiles the linear orchestration graph and its child
questphases. Runtime-proven meeting, hacking, and delivery phases are
instantiated from raw CR2W-JSON templates with exact scalar bindings. Phone
conversation phases are generated directly from typed fields. Scene, world,
journal, and localization resources remain separate authored products.

This boundary makes a quest reviewable before every asset exists without
pretending that a planned scene is playable. A `planned` stage is permitted by
validation and shown in the generated build plan, but ordinary compilation
rejects it. `--allow-planned` emits a non-shipping prototype orchestration
phase for graph inspection.

`tools/quest-schema-v1.json` is the editor-facing JSON Schema. The compiler
also performs its own strict validation so command-line builds do not depend on
an editor or an optional schema library.

## Stage Types

| Type | Required typed fields |
| --- | --- |
| `phone_job_offer` | `contact`, `message`, `choice_group`, `accept_choice`, `start_fact`, `accepted_fact` |
| `meet_contact` | `contact`, `scene`, `community`, `objective`, `description_entry`, `mappin` |
| `hack_access_point` | `device`, `success_fact` |
| `deliver_drop_point` | `item`, `drop_point`, `deposit_fact` |
| `phone_conversation` | `contact`, `thread`, `messages`, `choice_group`, `choices`, `final_message` |

Every stage also requires:

- a unique lowercase `id`;
- a `status` of `ready` or `planned`; and
- a child `phase_resource` exposing conventional `In1` and `Out1` sockets.

`required_assets` provides additional depot paths that must exist before a
ready stage can compile. Missing resources are errors for `ready` stages and
warnings for `planned` stages.

Meeting, hacking, and delivery stages currently declare `phase_template` and
`template_bindings`. Bindings replace complete scalar values only; substring
rewrites are intentionally forbidden. Compilation rejects a binding that was
not found in the template, duplicate `HandleId` values, and dangling
`HandleRefId` values. This preserves the proven graph topology while making
quest-local facts, journal paths, scene paths, actor names, NodeRefs, and
completion state explicit in the manifest. A post-build contract check also
requires every typed runtime identifier (contact, scene, community, device,
success fact, grants, item, drop point, and deposit fact as applicable) to be
present in the generated child, preventing descriptive manifest fields from
silently drifting away from template behavior.

Phone choices are objects with paired `choice` and `reply` journal paths. The
generated graph activates the initial messages in order, waits on every choice
branch, joins the selected reply, sends `final_message`, waits until it has
been visited, optionally sets `completion_fact`, and exits through `Out1`.
`source/quests/examples/phone_conversation.quest.json` is the standalone
authoring example.

The first compiler slice is intentionally linear. Dialogue choices remain
inside scene or phone blocks; combat, breach outcomes, and deposit completion
remain inside their child phases. Future schema versions can add named stage
outcomes and conditional edges without changing existing manifests.

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
