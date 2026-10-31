# Reduction plan for Ghostline

This began as a design result of the [all-quest research](all-quests-method.md).
The first [owned lifecycle implementation](../../../authoring/owned-lifecycle-blocks.md)
now covers these compositions through opt-in stages and the shared compiler.
It is an experimental authoring implementation, with no installed acceptance
or template/runtime promotion claimed. Existing stage names below are confirmed in
`tools/quest_stages.py`; registry presence does not establish support for the
entire proposed lifecycle or an installed test result.

| Proposed composition | Inputs and owned state | Outputs and completion boundary | Source example | Existing seam |
| --- | --- | --- | --- | --- |
| Acquire or use existing | Item/quantity, initial inventory policy, discovery/acquisition/application milestones | Existing-item route or acquisition route; application remains separate | Hippocratic Oath h234 / 35,34,17,38,39 | `acquire_item`, `interact_device` |
| Adaptive deferred timer | Clock, eligibility/difficulty branch, ordered weights/durations, deferral predicate, maximum deferral, cancellation owner | Ready only after selected wait and permitted deferral; cancelled route retires the action | q305 bunker hunt timing h0 / 3,7,8,73,74 | `time_gate`, optional/parallel orchestration |
| Resolve and report target | Explicit target set, lethal/unconscious/defeated policy, independent later-death observation, contact/report state | Resolved, killed observation, report outcome and reward commit remain separate | Bloody Ritual h0 / 253,208,78,246,207,80 | `cyberpsycho_encounter`, `combat_encounter`, phone stages |
| Contact with fallback | Contact, mute/busy/eligibility policy, scene outputs, message identity, once-only state | Connected, rejected, deferred or message-delivered; notifications are distinct from phase termination | Chapel h0 / 60,44,61,47,1 | `phone_conversation`, `phone_job_offer` |
| Restore an owned scope | Weather source, prefab variants, restrictions, original/target state, restoration order | Final restoration acknowledgment after all required operations; intermediate facts retain their meaning | Courier introduction h56 / 12,11,13,1 | Lifecycle cleanup and `vehicle_cleanup`; environment policy needs explicit composition |
| Reconcile entitlement and retire an offer | Vehicle entitlement predicate, availability facts, old objective/message identities, silent retirement policy | Reconciled state and retired offer; payment/delivery are independent | Vehicles metaquest new h21 / 103,131 and 176,189,251 | Vehicle stages plus a separate persistent-state migration contract |
| Encounter-controlled world variants | Entry role, registered prefab/variant bindings, combat/attack/despawn predicates, restart and cancellation | Restart or committed termination with listeners retired and presentation restored | q305 hiding-spot controller h0 / 4,11,0,5,10,9 | `world_variant` and `retire_branch` mechanism candidates |

## Concrete overlap and limits

`build_acquire_item_phase` already sequences optional objective/description/
mappin setup, optional grant, inventory observation, objective completion,
mappin retirement and an optional acquisition fact. The Hippocratic Oath
example contributes a distinct initial inventory branch and separate use
milestone. Do not replace existing verified behavior merely to copy a donor.

`build_cyberpsycho_encounter_phase` already composes activation/readiness,
reveal, combat/hostility, killed/spared/player-defeat routes, resolution and
cleanup. The new research calls for checking the *reporting and later lethal
observation boundaries* against that implementation. It does not establish
that Ghostline lacks a cyberpsycho encounter stage.

The existing native lifecycle helpers also separate attempt cancellation,
transfer, reward/completion and epilogue behavior. Reuse those ownership seams
where their contracts match. The source research supports refining contracts
and adding policies, rather than introducing a separate stage for every
vanilla resource name.

## Promotion criteria

For each composition, select a concrete connected occurrence, preserve every
boundary socket and inspect its setup/cleanup neighbors. Replace donor facts,
actors, world references, item/reward records and scene interfaces with explicit
bindings. Separate quest-public outcomes from internal presentation state.

Before declaring a reusable implementation, prove ordinary completion and
each alternate route, already-satisfied predicates, interruption and return,
both event orders at a join, save/load, actor loss and once-only reward/outcome
commitment. For timers include skip/load/cancel; for contact include busy,
muted and rejected cases; for cleanup include cancellation during each step.
Follow the repository's quest-production workflow for new runtime behavior.
None of those installed acceptance cases is claimed by this research pass.
