# Generated quest-block migration

All 40 registered stage types now have generated defaults. The remaining
template paths were converted in this order: condition/monitor/plant/rescue;
vehicles; carrying and passengers; meetings and braindance. The standard
escort, defense and choice shapes now generate as well, while their existing
extended builders continue to handle variable structures and outcome policies.
Single-item drop-point delivery also has a generated path; generated access
points continue using the shared device builder with explicit device bindings.

The new builders in `tools/quest_generated_blocks.py` construct typed nodes and
edges directly. They read no CR2W-JSON template and perform no placeholder
substitution. Actor, mounting, device, inventory, journal and scene primitives
remain shared with the established builders. The original template generators
and all template resources remain intact for regression and explicit overrides.

## Compatibility

Default configurations preserve the original typed graph: node IDs, socket
names/order, connections, predicates, effects and ownership boundaries. Tests
compare the canonical complete graphs against every retained built-in fixture,
including the defense retry variant. A frozen GQ000 meeting graph is retained
under `tests/fixtures/quest_blocks/gq000_meet_contact.questphase.json` with its
original source fixture identity. Formatting, envelope export timestamps and
handle placement do not establish behavior and are normalized by the comparison.
The source/fixture hashes are recorded in the adjacent provenance JSON.

Existing manifests with `phase_template` and `template_bindings` keep using
their explicit graph. Former built-ins selected through an explicit bindings
dictionary also retain that path. The explicit in-memory `template_documents`
build API remains supported. GQT005's normal build now uses the generated
braindance builder; supplying an explicit template document still overrides it.
The story manifests and their specialized explicit graphs remain unchanged.
Legacy scene exit supersets remain optional listeners. Explicitly configured
scene ports are checked against the bound scene; global interruption/return
sockets do not require a scene exit-point declaration.

New generated meetings need `setup_trigger`, `scene_origin` and `accepted_fact`.
Generated access points need `controller_class`, `action` and
`completion_function`. Missing world/device/scene bindings are not inferred
from a naming convention. Planned meetings retain a warning for missing new
bindings; they cannot be built until those bindings exist. An existing explicit
template remains a valid alternative.

## Configurable behavior

| Block | Generated options beyond the fixed fixture |
| --- | --- |
| `optional_condition` | `evaluation: on_entry` snapshots a fact once; the legacy `at_exit` behavior remains the default when authored. |
| `stealth_monitor` | `additional_failure_facts` lets multiple external detection/alarm producers fail the monitor. |
| `plant_item` | `consume_item: false` retains the item and checks its inventory presence after device completion. |
| `release_or_rescue_npc` | `additional_entries` waits for every explicitly named rescued actor in the same community. |
| `enter_vehicle`, `steal_vehicle` | `player_role` selects Invalid/Driver/Passenger explicitly. |
| `drive_to` | Ordered `waypoints` precede the final destination and completion fact. |
| `deliver_vehicle` | Optional `require_stop`, explicit `require_player_exit`, description, mappin and completion fact. An already-outside player bypasses the unmount-event wait. |
| `vehicle_cleanup` | `cleanup_communities` deactivates only explicitly bound communities before the cleanup fact. |
| `carry_npc` | Ordered carried-body `waypoints`, description, optional mappin and completion fact. Every gate requires both carrying the named actor and being inside its trigger. |
| `ride_with_contact` | `additional_passengers` with distinct actor/seat bindings, `contact_slot`, player/contact roles and optional `wait_for_contacts`. Every required mounting signal must join. |
| `meet_contact` | Scene entry/accept/defer ports, community phase, checkpoint label and optional `defer_policy: rearm` with explicit outside trigger. |
| `braindance_analysis` | 1–32 distinct clue facts, explicit scene entry/exit sockets, and millisecond-resolution teardown, settle and exit-enable delays. |
| `escort_npc`, `defend_target`, `choice_gate` | Their existing arbitrary-count, lifecycle, duration, branch and outcome options remain available; fixed shapes now generate too. |

Generated replacements support named start/success sockets and applicable
objective entry/success retention. Stealth also supports failure retention.
Use an [owned scope](owned-lifecycle-blocks.md) around a child when cancellation,
ordered restoration or durable commitment belongs to its parent. Extended
escort and defense keep their existing cancellation/outcome builders.
Custom templates own their own lifecycle unless the established meeting or
braindance adapter explicitly implements the requested retention.

Omitted `require_player_exit` preserves legacy vehicle delivery, which did not
wait for exit; the old editor default was corrected to false. Explicit true now
implements that check. Omitted `require_stop` preserves the zero-speed gate.
Vehicle cleanup still avoids the global player-vehicle despawn operation; the
legacy `player_vehicle_record` is retained for manifest compatibility and does
not imply a purchase, delivery or global cleanup.

`placement_slot` still requires an explicit custom template: observing a carried
NPC's delivery does not place/drop that NPC automatically. Similarly,
`allow_combat_interrupt` still needs a custom escort implementation. Generated
optional conditions accept fact predicates; other condition labels require an
explicit template. Unsupported policies fail validation instead of being ignored.

Meeting UI activation remains root-owned. The child activates its community,
waits for spawn readiness, enters the broad setup gate and starts the scene.
Acceptance succeeds the objective, clears the pin and writes its fact. Default
deferral terminates without acceptance, exactly as in the fixture; optional
rearm waits for departure and approach before starting the bound entry again.
It repeats that entry deliberately; no resume entry or dialogue rewrite is
invented. A scene owns its inner proximity and dialogue behavior.

Braindance clue completion and scene termination remain separate. All clue
facts join before the completion fact; every bound scene exit restores the
player and then ends the phase. An early scene exit can end the phase without
the completion fact. A quest requiring solved evidence must check that fact
before progressing, as with the preserved template behavior.

## Verification and reproduction

The default examples are in
`quests/examples/generated-building-blocks.quest.json`. They are a catalog of
complete typed configurations with planned scene/world placeholders, not a
playable route. Build them into an isolated preview:

```powershell
python tools/build_lifecycle_preview.py --spec quests/examples/generated-building-blocks.quest.json --out-root generated/generated-blocks-preview --deserialize
python tools/build_lifecycle_preview.py --spec quests/examples/generated-block-variants.quest.json --out-root generated/generated-variants-preview --deserialize
python -m unittest discover -s tests -p test_generated_quest_blocks.py -v
python tools/check_project.py --python-only
```

Tests preserve all fixture graphs and explicit overrides, and exercise ordered
waypoints, passenger joins in all 24 event orders, multiple rescue/detection
inputs, fact snapshots, deferred meeting return and variable braindance clues.
Early braindance exit must restore the player without falsely committing evidence.
The independent graph model injects native predicate acknowledgments; it does
not simulate native mounting, AI, streaming, scenes, saves or checkpoint recovery.

Typed conversion/readback and the broader story/test-quest migration suite
are separate gates. Generated preview reports bind source and output hashes;
publication is refused if source changes during conversion or readback differs.
The templates are never regenerated or deleted by this build.

The migration's 2026-10-27 verification includes 19 default artifacts and 12
configuration-variant artifacts converted to CR2W and read back through
WolvenKit, with all source/output hashes checked against the final compiler.
The 16 focused regression tests cover fixture parity, compatibility, validation
and graph scenarios. The catalog contains 40 generated defaults and no example
errors; the original template source/archive trees remain unchanged.
The full Python offline gate passed 1,069 tests and Ruff; schema synchronization
and the offline dependency-lock check also passed.

Installed acceptance remains configuration-specific. For each adopted binding
set, follow [quest production](../workflows/quest-production.md) and the
[playtest handoff contract](../workflows/runtime-testing.md#playtest-handoff-contract):
name the package/install hashes and pre-registration save, then test the full
route, interruption/return, simultaneous events, actor loss and save/load.
Vehicle tests need actual seats, mounting and already-stopped/outside entry;
meeting tests need already-inside setup and rapid defer/return; braindance tests
need early exit and complete clues in different orders with player restoration.
No new in-game result is claimed by this migration.
