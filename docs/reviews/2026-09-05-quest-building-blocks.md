# Quest building block improvements

Implemented the six proposed improvements while retaining the existing
manifest shorthand and template paths.

| Area | Result |
| --- | --- |
| Contracts and outcomes | Named input/output aliases, explicit routes, entry selection, terminal quest state, typed fact/scene contracts, reachability and ownership checks. |
| Lifecycle ownership | Generated actor acquisition/retention/release and objective policies; GQT003 escort-to-defense handoff and GQT005 meeting-to-braindance handoff use manifest declarations. |
| Authoring scaffolds | Shared objective/contact/location/clue/fact declarations, stable generated paths and IDs, journal/onscreen generation, explicit overrides, and atomic JSON artifact publication. |
| Variable blocks | Arbitrary escort gates, timed defense with failure/cancellation and checkpoint support, N-way fact choices with fallback, and K distinct clues from N. |
| Reusable compositions | Three parameterized quest recipes, concrete examples, and a decomposed cyberpsycho builder with unchanged generated encounter graphs. |
| Catalog and evidence | Registry-derived catalog, hash-bound build/game evidence, graph previews, and routing scenarios with duplicate-event and snapshot-restore checks. |

The first end-to-end pilot is
[GQT003](../../projects/test-quests/gqt003/gqt003_extract_and_hold.quest.json). Its build command
produces the root, four child phases, journal, and localization as one artifact
set. Custom escort/defense Python builders and repeated journal assembly are
removed. Journal IDs, localized text, and marker meanings remain compatible.
The root now owns final quest success/failure. A
[checkpoint companion](../../quests/examples/timed-defense-retry.quest.json)
exercises failure-blocking native retry setup separately.

[GQT005](../../projects/test-quests/gqt005/gqt005_braindance_analysis.quest.json) uses the common
objective-retention policy instead of its quest-specific graph-rewiring hook.
The receiving braindance stage retains the active objective at entry.

## Verification

The full project gate passes: **612 Python tests**, Ruff, and **6 model-free
Rust tests**. The Python suite completed in 54.494 seconds. The complete log is
`generated/quest-blocks/project-gate.log`.

All **11 GQT003/GQT005 CR2W resources** passed independent WolvenKit round-trip
checks and are published to `source/archive`, with source hashes checked before
publication and rollback backups retained. Nine candidates used the native
writer; escort and defense used the WolvenKit fallback. Typed values, graph
topology, and ordered ports match. The only accepted normalization is an empty
`inplacePhases` array added to GQT003 release and GQT005 review. Separate native
probes for four-way choice and two-of-five investigation also passed using the
WolvenKit fallback.

Conversion receipts and independent WolvenKit comparisons are recorded under
`generated/quest-blocks/native`; `generated/quest-blocks/publication.json`
records the published hashes and backup location. Conversion also exposed a malformed
Boolean debug-step flag: the exact-assignment flag is now `1`, while the integer
step value remains unchanged. A regression checks both fields separately.

Focused checks cover invalid routing, fact producers on every path, parallel
dependencies, actor/objective ownership, real emitted ports, and scene exit
tables. The clue tests evaluate emitted graph behavior for every ordered subset
of five clues and each threshold, including duplicates. GQT003 has five
scenarios against its real compiler plan. Five encounter configurations compare
byte-for-byte with captured pre-refactor output, including GQT006.
The regenerated 30-block catalog has no example or evidence errors and includes
composed recipes and story implementation manifests.

## Scope of the evidence

The scenario harness models sequential signal routing; it does not execute
REDengine conditions or load Cyberpunk saves. Native conversion and resource
round trips establish serialization integrity, not gameplay behavior. No game
installation or gameplay run is part of this change.

Explicit routes and the sequential scenario model do not combine with
`parallel_groups`. Existing all-of groups remain supported; contract reads
inside a branch require a prior writer in that branch or an external
declaration, while the join exposes all branches' writes. Actor lifecycle
policies currently apply to the generated escort/defense blocks. Companion
movement, community placement, scenes, and device resources remain authored
inputs. Existing unrelated workspace edits are preserved.

Use the [composition guide](../authoring/quest-composition.md),
[block catalog and scenarios](../authoring/quest-blocks.md), and
[manifest reference](../../tools/quest_spec.md) for commands and field details.

The follow-up [complete quest migration](2026-09-05-quest-migration.md) extends
the shared authoring and build system to all ten active quests.
