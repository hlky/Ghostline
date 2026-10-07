# Quest composition

Declare repeated authoring data in a quest manifest's `composition` object.
`tools/quest_authoring.py` expands it into the existing stage format and builds
journal and onscreen CR2W-JSON from the reviewed `quest_content` donors. The
compiler includes those documents in its normal staged artifact publication.

All ten active quest manifests use this system: GQ001–GQ003 and GQT001–GQT007.
The [GQT003 manifest](../../projects/test-quests/gqt003/gqt003_extract_and_hold.quest.json)
demonstrates actor transfer and explicit routes; the
[GQ001 manifest](../../projects/ghostline/quests/gq001/implementation/quest.json)
demonstrates preserved story journal IDs and phone threads. The GQ000 prototype
remains a preserved runtime baseline and donor source. Composition adoption
does not change a quest's readiness or establish a new in-game pass.

## Declare once, reference by alias

```json
{
  "schema_version": 1,
  "id": "gq_relay",
  "title": "Follow the Signal",
  "description": "Find the relay that sent the message.",
  "composition": {
    "locations": {
      "relay": {"ref": "#gq_relay_marker", "trigger": "#gq_relay_trigger"}
    },
    "facts": {"accepted": null},
    "objectives": {
      "reach": {
        "text": "Reach the relay.",
        "mappins": {"relay": {"ref": "@locations.relay.ref", "text": "Relay"}}
      }
    }
  },
  "stages": [{
    "id": "reach",
    "type": "reach_area",
    "status": "planned",
    "trigger": "@locations.relay.trigger",
    "objective": "@objectives.reach.path",
    "description_entry": "@objectives.reach.description_entry",
    "mappin": "@objectives.reach.mappin"
  }]
}
```

Aliases replace complete values. `@objectives.reach.path` resolves to a string;
`@clues.relay` can resolve to an entire typed clue object. Text containing an
alias in the middle remains literal. A leading `@@` escapes a literal `@`.
Missing names, cycles, duplicate stage/journal IDs, and conflicting localization
keys fail before publication. Inputs are copied; normalization does not rewrite
the authoring manifest.

| Declaration | Useful bindings |
| --- | --- |
| `objectives.<name>` | `.path`, `.description_entry`, `.mappin`, `.route_mappins`, `.mappins.<pin>.path`, `.completion_fact` |
| `locations.<name>` | `.ref`, plus explicitly supplied fields such as `.trigger` or `.marker` |
| `clues.<name>` | Whole typed clue, or `.object_ref` and `.completion_fact` |
| `contacts.<name>` | `.contact` for the phone journal ID; explicit actor `.community`, `.entry`, `.appearance`, `.scene` |
| `contacts.<name>.threads.<thread>` | `.path`, `.message`, `.messages`, `.choice_group`, `.accept_choice`, `.choices`, `.final_message` |
| `contacts.<name>.threads.<thread>.entries.<entry>` | `.path`; choice groups additionally expose `.entries.<choice>.path` |
| `readables.<name>` | `.path`, `.title_key`, `.text_key` |
| `facts.<name>` | Explicit fact name, or `<namespace>_<name>` when declared as `null` |
| `quest` | `.id`, `.path`, `.title_key` |
| `resources` | `.journal`, `.onscreens` archive depot paths |

Thread convenience bindings depend on the selected shorthand or explicit entry
form; use exact `.entries` paths when a conversation has several choice groups.

The namespace defaults to the quest ID. It controls the generated depot paths,
facts and localization keys. Set `composition.namespace` when an existing
manifest ID differs from its resource namespace, as in GQT003.
`composition.quest` can override the journal `title`, its `localization_key`,
and native quest `type`. For example, GQT006 preserves `CyberPsycho`. A type
override does not move the quest from its `quests/minor_quest/<namespace>` path.

Objective phase IDs derive from names rather than position, so inserting an
unrelated objective does not rename existing paths. Explicit `phase_id`, `id`,
`description_id`, `localization_key`, and `description_key` retain legacy IDs.
Several objectives can share a `phase_id`; each keeps its own objective ID and
path. `optional` is a Boolean and `counter` is a nonnegative integer written to
the journal objective. These are journal metadata; stage behavior still owns
objective state changes and counting signals.
Map pins accept explicit `id`, `ref`, `text`, `localization_key`, `gps_disabled`,
`debug_caption`, and `variant`. `points_of_interest` contains optional `{id, ref}` records
for quest-linked world-map markers. Extra localization entries can be declared
under `text`. All generated onscreen entries use `primaryKey: "0"` and unique
secondary keys.

`composition.journal_template` selects a reviewed donor from `quest_content`.
Objectives and mappins can select a specific donor entry with `template`:
an entry ID string uses that journal donor, while
`{"donor": "gq000_shapes", "id": "gq000_02_obj_extract_cache"}` selects both.
Fields outside the authored overrides remain inherited, including mappin
offsets and native metadata. Inspect the donor when migrating an existing shape.

Stage fields remain ordinary compiler fields. An explicit `phase_resource`
overrides its generated `mod\<namespace>\phases\<namespace>_<stage>.questphase`
default. Actor/objective lifecycle policies, outcomes, routing, and contracts
are preserved through expansion; they do not receive hidden defaults here.

## Contacts and phone threads

A contact can supply actor aliases without adding a phone journal entry.
Contacts with `threads` generate phone journal entries. The shorthand declares
`title`, a `messages` map of message ID to text, a `choices` map, and an optional
`final_message`. A choice is text alone for an offer, or `{text, reply}` for a
conversation. The normal conversation block requires at least two choices
with replies; an offer can use a single acceptance choice. IDs `choices` and
`final` are reserved within a thread.

New contact IDs default to `<namespace>_<alias>` to avoid overwriting an existing
phone contact. Set `id` explicitly when extending a deliberately shared contact.
Without `name`, an explicit `localization_key` references existing localization
without generating replacement text. This preserves shared contact names,
including the story quests' external character keys.

For existing or more complex conversations, use an ordered `entries` map instead
of `messages`, `choices`, and `final_message`. Each map key is a safe alias;
explicit IDs may retain digit prefixes and other legacy journal identifiers.
The following is a thread fragment:

```json
{
  "id": "gq_relay_offer",
  "title": "Relay Work",
  "title_key": "gl_gq_relay_offer_title",
  "entries": {
    "offer": {
      "type": "message", "id": "01_offer",
      "text": "Meet me at the relay.", "localization_key": "gl_gq_relay_offer",
      "sender": "NPC", "delay": 1, "important": true
    },
    "response": {
      "type": "choice_group", "id": "02_response",
      "entries": {
        "accept": {"id": "02a_accept", "text": "On my way."}
      }
    }
  }
}
```

Messages support `sender: "NPC"` or `"Player"`, nonnegative `delay`, Boolean
`important`, and an `attachment` journal path. An attachment requires a selected
message donor that already has a journal-path attachment field. Contacts,
threads, messages, choice groups, and choices accept `template` selectors in
the same string or `{donor, id}` form; their default donor is `gq001_shapes`.
Contact defaults use its `morrow` entry. Explicit donor metadata such as avatar,
attachment shape, and message flags remains inherited unless overridden.

## Readable content

`composition.readables` maps aliases to `{kind, group, id, title, text}` records,
with optional `title_key` and `text_key`. `kind: "file"` generates a journal file;
`kind: "onscreen"` generates an onscreen entry. The group defaults to `files`
or `shards` respectively, but its name is independent of the native kind:
GQ003 deliberately keeps onscreen entries under a group named `files`.
Use one kind per group. Only onscreen entries accept `tag`.
Stages and message attachments can reference `@readables.<alias>.path`.

## Recipes

`composition.recipes` appends reusable stage sequences after any explicit
`stages`. A recipe takes `name`, an optional stage-ID `prefix`, and a `steps`
object containing every named slot. Each slot supplies normal stage fields;
explicit IDs, types, paths, and policies override that slot's defaults.

| Recipe | Required slots and expansion |
| --- | --- |
| `offer_meeting_investigation_decision_debrief` | `offer` → `meeting` → `investigation` → `decision` → `debrief` |
| `rescue_escort_defense_extraction` | `rescue` → `escort` → `defense` → `extraction` |
| `encounter_evidence_report_reward` | `encounter` → `evidence` → `report`, with an explicit `reward` record granted after the report's final message |

See the complete [investigation](../../quests/examples/recipes/investigation.quest.json),
[rescue](../../quests/examples/recipes/rescue.quest.json), and
[encounter](../../quests/examples/recipes/encounter.quest.json) examples.
The rescue example declares timed defense and follower transfer explicitly;
its failure/cancellation routes terminate instead of progressing to extraction.
Recipe ordering alone does not supply world resources, scene exits, actor
placement, custom reward records, or event producers. These examples remain
`planned` until those resources and runtime behavior are validated.

## Inspect and generate

```powershell
# Print the expanded stage manifest without writing files.
uv run python -B tools/quest_authoring.py quests/examples/recipes/investigation.quest.json

# Publish reviewable normalized input, bindings, and raw journal/localization.
uv run python -B tools/quest_authoring.py quests/examples/recipes/investigation.quest.json `
  --output generated/quest-authoring/investigation
```

The output contains `quest.json`, `bindings.json`, and editable artifacts under
`source/raw/<depot>.json`. This command does not write packed binaries or register
the quest with ArchiveXL.

For a complete quest build, use the owning quest's build entry point:

```powershell
py -B projects/ghostline/quests/gq001/implementation/build.py `
  --out-root generated/quest-builds/gq001

# Planned GQ003 builds must remain in an isolated output tree.
py -B projects/ghostline/quests/gq003/implementation/build.py `
  --out-root generated/quest-builds/gq003 --allow-planned
```

The shared `quest_build` layer collects the root, children, journal, and onscreen
localization before publication. Specialized builders add their quest-owned
resources to that same set. `--out-root` preserves depot paths beneath a scratch
`source/raw` and `source/archive` tree. Omit it to publish to the repository's
source tree for ready quests. Add `--deserialize` to stage CR2W conversions:
all conversions must succeed before raw and binary outputs are published
together, with rollback on publication failure. The default native serializer
uses existing binary templates and falls back to WolvenKit for unsupported
layouts; `--serializer wolvenkit` selects it explicitly in the shared CLI.
Each candidate is read back through WolvenKit and compared with the requested
typed data, graph connections, and socket order before publication. A native
conversion that loses requested data is retried with the reflected writer;
remaining differences fail the build.
This is a build transaction, not an installation or runtime validation.

The older `--output-root` spelling remains accepted by GQT001, GQT002, and
GQT004; use `--out-root` consistently in new commands.

Owned paths are recorded in `generated/quest-builds/<namespace>/outputs.json`
under the selected output root. Obsolete outputs are reported and retained for
review. Follow the [build workflow](../workflows/build-and-package.md) for
packaging and installation.

The Python API exposes `normalize_spec(raw)` for pure expansion,
`compose(raw)` for expansion plus in-memory documents, and
`artifact_documents(result, output_root)` for publication paths. Build wrappers
can delegate to `quest_build.main(manifest, root_resource, argv=None)`.
Specialized builders use `compile_manifest_artifacts(...)`, append their
`QuestArtifact` resources, and call
`quest_build.publish_build(artifacts, namespace=..., output_root=..., deserialize=...)`.
`relocate_artifacts(artifacts, output_root)` is available when a builder needs
the preview paths before publication; depot paths remain unchanged.
Regression tests cover preserved story content and phases, composition errors,
recipes, complete output sets, and failed conversion/publication.

## Editor validation and schema maintenance

[The quest schema](../../tools/quest-schema-v1.json) accepts both authoring input
and normalized manifests. With `composition`, stage paths can be generated,
fields can contain whole-value aliases, and a nonempty recipe list can supply
all stages. Literal values still retain their usual types, required fields,
ranges, and allowed properties. Recipe slots validate against their default
stage type; an explicit `type` override selects that stage's contract.

After expansion, the same schema selects the canonical branch because the
normalized manifest has no `composition`. The compiler also checks resolved
aliases and semantic contracts. Editor validation cannot prove that an alias
exists or that its eventual value has the required type.

Maintain canonical stages in `$defs.stage` and `$defs.baseStage`; shared top-level
field contracts live in `$defs.manifestFields`. The `authoring` definitions are
generated from those contracts and the recipe registry in `quest_authoring.py`.
Refresh them after adding or changing schema fields:

```powershell
uv run python -B tools/quest_authoring_schema.py
uv run python -B tools/quest_authoring_schema.py --check
```

The tests check generation drift and validate every current manifest both before
and after normalization. No editor plugin or Python process is needed to use the
checked-in JSON schema.
