# Quest blocks, evidence, and scenarios

The block registry in `tools/quest_stages.py` joins the editor schema to the
compiler's implementation policy. Generate its catalog instead of maintaining
another list of supported fields:

```powershell
py -B tools/quest_catalog.py catalog --format markdown --output generated/quest-catalog/blocks.md
py -B tools/quest_catalog.py catalog --format json --output generated/quest-catalog/blocks.json
```

Each entry lists required and optional fields, their JSON Schema definitions
in the JSON output, default input and outcome aliases, builder/template choice,
unsupported fields in the default template, and checked-in manifest examples.
Example status is an authoring declaration. It does not establish a successful
build or game run. A block with an available builder may still need valid world
resources, scene exits, actor lifecycle setup, and journal paths.

See [quest composition](quest-composition.md) for recipes and authoring commands,
and [runtime flow](../../projects/ghostline/quests/gq000/implementation/runtime-flow.md)
for the proven ownership boundary between a root phase, child phase, and scene.

## Current adoption

GQ001–GQ003 and GQT001–GQT007 all use the shared registry/compiler, composition
declarations, and build publication layer. The GQ000 prototype is preserved as
the runtime baseline; it is not another migrated authoring manifest.

Adoption does not require every quest to use every block feature. GQT003
demonstrates explicit success/failure routes and follower transfer from escort
to timed defense. GQT005 declares the meeting-to-braindance objective handoff.
The story migrations preserve existing stage behavior and parallel groups;
GQ003 remains planned until its world and runtime integration is complete.

Use each quest's `implementation/build.py` for its complete artifact set.
The shared `quest_build` API publishes phases and composed content together;
specialized quest builders add scene, world, or braindance resources where
needed. See [composition build commands](quest-composition.md#inspect-and-generate)
for scratch roots and staged conversion. This rollout establishes shared
authoring and build ownership; the evidence requirements below still apply to
each claimed runtime behavior.

## What counts as evidence

Catalog evidence has two separate levels:

- `build`: an actual structural compilation of the listed example. The receipt
  records generated raw graph hashes and hashes of its manifest, compiler,
  schema, and template inputs. This proves that configuration compiled with
  those inputs. It does not prove native serialization, resource/world audit,
  archive packaging, installation, or engine behavior.
- `in_game`: a recorded run with concrete observations, a hash-bound run
  report, and the exact tested packed resources or archive. The catalog checks
  those bindings. It does not independently authenticate the run or generalize
  its result to every configuration of the block.

Every bound file must still exist and match its SHA-256. A changed manifest,
compiler, template, tested resource, or run report makes its evidence stale.
Missing files also invalidate evidence. Stale and malformed entries remain
visible with their reasons, but grant no current pass status. A record of a
failed run never grants pass status.

Record a real structural build without writing generated resources into
`source/raw` or `source/archive`:

```powershell
py -B tools/quest_catalog.py record-build `
  --manifest quests/examples/direct_building_blocks.quest.json `
  --output projects/test-quests/evidence/quest-blocks.json
```

This command replaces that evidence document with one build receipt. Use a
separate output document for each additional example, then pass multiple
`--evidence` arguments to the catalog. The default document is
`projects/test-quests/evidence/quest-blocks.json`. Generated outputs are built in memory;
their unique keys in the receipt identify artifacts, not published game resources.
The first root graph is keyed `$root`; child phases, journal, and localization
documents retain distinct output paths. Imported local builder code and
composition donor files are included in the input bindings.

In-game evidence is authored after observing an actual run. Its document has
`schema_version: 1` and an `entries` array. Each entry needs `id`, `level`,
`passed`, `stage_types`, `summary`, and `resources` (repository-relative POSIX
paths mapped to SHA-256 values). A game entry additionally needs `run_report`
bound in `resources`, nonempty `observations`, and at least one tested file
under `source/archive` or a tested `.archive`. Include date, game/mod versions,
save/start conditions, the tested route, interruption behavior, and repeat/load
conditions in the run report. Bind supporting logs or captures when available.
Do not manufacture a passing game receipt from a compiler or scenario report.

## Preview the route

```powershell
py -B tools/quest_scenarios.py `
  --manifest quests/examples/direct_building_blocks.quest.json `
  --graph generated/quest-catalog/direct-routing.md
```

The command uses the compiler's plan and renders a Markdown Mermaid graph.
Edges show outcome aliases and their targets, including `$end`. Input/output
socket aliases come from the same plan. Unknown targets, inconsistent outcomes,
and compiler errors are rejected before a preview is written.

## Exercise a structural scenario

```powershell
py -B tools/quest_scenarios.py `
  --plan projects/test-quests/scenarios/contract-routing.plan.json `
  --scenarios projects/test-quests/scenarios/contract-routing.scenarios.json `
  --output generated/quest-catalog/scenarios.json `
  --graph generated/quest-catalog/routing.md
```

The checked-in plan is explicitly synthetic: its three-output encounter is a
routing fixture, not evidence that a particular engine phase exports those
sockets. Its scenarios cover success, failure, interruption, repeated/inactive
signals, and returning to a saved checkpoint. Replace `--plan` with `--manifest`
to exercise routes produced by the compiler for an authored quest.

GQT003 also has scenarios bound to its actual manifest, covering success,
escort/defense failure, duplicate events, and model restore after a failed hold:

```powershell
py -B tools/quest_scenarios.py `
  --manifest projects/test-quests/gqt003/gqt003_extract_and_hold.quest.json `
  --scenarios projects/test-quests/scenarios/gqt003.scenarios.json `
  --output generated/quest-blocks/gqt003-scenarios.json `
  --graph generated/quest-blocks/gqt003-routing.md
```

Each scenario needs a unique `id`, nonempty `steps`, and a final `expect` object.
A step contains exactly one of `event`, `save`, or `load`, plus an optional
`expect`. An event names `event_id`, `stage`, and `outcome`. Assertions can inspect
`active_stage`, `terminal_outcome`, and a step's `result`:

```json
{
  "event": {"event_id": "relay-arrived-1", "stage": "reach_relay", "outcome": "success"},
  "expect": {"result": "advanced", "active_stage": "acquire_datacache"}
}
```

The model has one active stage. It consumes each event ID once; a repeated ID
with identical content returns `duplicate`, and reuse for different content is
an error. A signal from an inactive stage returns `inactive`; after `$end`, new
signals return `terminal`. Ignored signals are recorded, so they cannot become
new signals after a later transition. These are explicit harness policies,
not guarantees about REDengine signal delivery.

Snapshots preserve the event journal and bind the routing contract, port
aliases, and declared dependencies by hash. Restoring a snapshot checks its
journal against its state and rejects a changed contract. Loading an earlier
snapshot discards events that happened after it, as a model of restoring that
point in the test. It does not read or write Cyberpunk saves.

Reports keep a trace and assertion failures for every scenario. Exit status is
`0` when all scenarios pass, `1` for failed scenarios, and `2` for invalid input.
The first version deliberately rejects parallel groups rather than silently
applying sequential routing to them. It does not simulate fact values,
conditions, actors, devices, scenes, native interruption/cut behavior, or engine
save persistence; those need compiler checks and hash-bound game evidence.
