# What all quest types add to Ghostline's building blocks

This is a manually reviewed synthesis of representative source mechanisms
from the [all-quest catalogue](all-quests/README.md). It complements each
entry's structural dossier; it does not claim a manual narrative review of all
416 journal identities. All locators below identify the checked snapshot's
resource / graph / node. Missing RED defaults remain missing.

## Treat a block as a lifecycle with owned boundaries

A portable block needs an entry condition, bound actors/world resources,
normal and alternate outputs, persistent effects, interruption behavior and
cleanup ownership. A node-type inventory supplies mechanisms; a connected
path supplies an extraction seed. Neither proves that the extracted component
is self-contained. The source examples below show why this distinction matters.

## Main quests: adaptive pacing rather than a fixed wait

In `ep1/quest/main_quests/q305/phases/combat/q305_bunker_hunt_timing.questphase`,
graph h0 node 0 enters difficulty gate 7. Gate 8 checks
`q305_outerbunker_robot_random_hunt >= 1`; its False output enters randomizer
3, whose stored weights are `[1,2,2]`. Out1/Out2/Out3 select real-time waits
25/30/35 seconds at nodes 4/5/2. Other difficulty-gated routes use different
stored timing sets. The missing difficulty default is not labelled as an
explicit difficulty setting by this research.

After convergence, node 73 checks `q305_bunker_player_reading`. Its True route
enters node 74, an OR of an authored reading-fact predicate and a 1 minute
30 second real-time delay. Its False route bypasses that additional wait.
This is evidence for **weighted timing plus bounded deferral**, rather than
one generic delay.

Proposed composition: difficulty policy -> weighted duration selection ->
timer -> activity deferral with maximum bound -> ready. Inputs should include
clock domain, ordered weights, delay alternatives and deferral predicate.
Acceptance must cover re-entry, load during the timer, activity beginning near
timer expiry, and cancellation of the deferred action.

The sibling `q305_bunker_hiding_spot_controller.questphase` exposes
`outer_bunker_in`, `inner_bunker_in` and `restart`. Node 11 shows
`var_hiding_spots` on `#q305_outer_bunker_devices`, then starts listeners 0 and
5. Node 0 watches an attack fact or robot combat; node 5 watches the despawn
fact, followed by a variant operation and restart output. The inner entry
has a parallel shape with its own nodes. The variant operation at node 1
omits `show`; this pass does not rewrite that omission as an authored false.

This suggests a separate **encounter-scoped world-state controller**. Its
world bindings, restart semantics and competing listeners must stay visible
when parameterizing the phase.

## Gigs: already-owned items, medical outcomes and departure

In `base/open_world/street_stories/watson/kabuki/sts_wat_kab_02/phases/sts_wat_kab_02_openworld.questphase`,
graph h234 node 35 waits for `kab_02_after_scan_objective_hold >= 1` before
node 34 tests inventory item `137708286854`, quantity `< 1`. True enters
the take-blood fact wait at 17; False activates the injection objective at 9.
After collection-objective activation, node 38 watches quantity `>= 1` and
feeds XOR 39 alongside another route. The graph is not an ordered list of
objectives and that convergence is not an AND join.

Proposed composition: **acquire-or-use-existing-item**, with separate discovery,
inventory acquisition and application milestones. Preserve the comparison,
item binding and actual convergence; do not force a player who already owns
the item through another acquisition interaction.

Graph h893 routes ordinary and `patient_killed` scene exits into the
`kab_02_chester_talk` fact at node 4, while node 42's
`kab_02_operation_performed` write has the ordinary exit as its source.
Conversation completion and operation outcome therefore need separate outputs.

Graph h977 node 83 uses a trigger whose activator is the community entry
`chester`, with `isPlayerActivator:false`; its output fans out into transport
and call facts. Node 20 deactivates `#kab_02_com_chester` and then writes a
fact named `kab_02_lucy_despawned` at 87. The fact's name does not establish
which actor the actual operation targets. Bind behavior from stored entity
references, rather than inferring it from a descriptive fact label.

## Cyberpsycho encounters: completed and killed are separate observations

In `base/open_world/minor_activities/watson/northside/ma_wat_nid_15/ma_wat_nid_15_phase.questphase`,
graph h0 node 253 watches the `psycho` entry of `#ma_wat_nid_15_com` with
explicit `unconscious:false` and `defeated:false`, then writes
`ow_psychos_killed` at node 208. The completion chain separately writes
`ma_nid_15_finished` at 78, clears `ma_nid_15_active` with explicit value 0 at
246, writes `ow_psychos_done` at 207, stops an audio signpost at 255 and
dispatches reward 80. The absent fact-write defaults are not translated into
invented increments or values.

Node 317 also checks several reasons to defer/bypass a briefing, including
holocall setup facts, phone mute group, player mounting, content lock and
objective state. The parent cannot treat a briefing scene as always available.

Proposed composition: **target-resolution policy + independent lethal
observation + encounter completion + report/reward lifecycle**. Preserve those
as distinct states. Test defeat followed by later death, early investigation,
skipped/rejected contact, save/load and repeated completion signals.

## Contracts: early notification, cancellation and contact fallback

In `base/open_world/minor_activities/heywood/glen/ma_hey_gle_02/ma_hey_gle_02_phase.questphase`,
graph h0 node 47 is a permanent cut control. It cuts node 43 and fans out
to POI handling, an embedded phase and output 1. Output 1 is explicitly
`NonTerminating`. That notification does not prove that the child has ended
or all cleanup has finished.

Actor-readiness wait 51 precedes loot injection 52. Phone gate 60 routes a
muted dispatcher to journal message 61; the scene's rejected output also
activates that message. Save-lock gates 56 and 57 govern checkpoint-related
routes. The source supports a reusable **contact attempt with message
fallback**, alongside independent spawn/loot and checkpoint policies.

The export's Contract journal identity for this encounter and its current POI
identity are distinct evidence. A matching POI does not establish activation
of that historical-looking quest-journal entry.

## Vehicle quests: availability, ownership and retiring old objectives

In `base/open_world/vendors/vehicles_metaquest/phases/vehicles_metaquest_new.questphase`,
graph h21 node 103 checks availability of
`Vehicle.v_standard2_archer_quartz_player`; True writes `archer_quartz_owned`
at 131. Other embedded graphs write availability facts separately.

The same resource's nodes 176 -> 189 -> 251 deactivate an Archer Bandit
purchase objective, write `vehicle_metaquest_archer_bandit_deactivated`, and
deactivate a dealership notification. These are reconciliation/retirement
operations, not evidence that this chain performs a purchase.

Proposed composition: **availability reconciliation and obsolete-offer
retirement**, separate from payment, vehicle entitlement and delivery. An
inventory/journal snapshot can contain an older offer that current graphs
explicitly deactivate. This is another reason to retain journal identities
and avoid counting each one as a distinct current playable job.

## Courier work: an intermediate cleanup fact is not a completion fence

In `ep1/openworld/sandbox_activities/courier_spot/introduction_quest/sa_ep1_courier_introduction_spot_logic.questphase`,
graph h0's In1 writes the introduction-active fact and explicitly resets
`sa_ep1_courier_intro_cleanup_done` to 0. In embedded graph h56, node 12
resets weather using source `courier_cleanup`; node 11 then writes the
cleanup-done fact, and node 13 subsequently shows the `courrier_path` prefab
variant before the graph output. The spelling `courrier_path` is the stored
binding and should not be silently corrected.

Proposed composition: **owned environment restoration**, with a completion
output after the entire required restoration chain. Reusing the earlier fact
as that completion output would change the stored ordering.

## Taxonomy and discovery lessons

Two gaps in the original side/minor pass are resolved by expanding beyond the
expected quest directories. Murk Man Returns Again Once More Forever links
exactly from `ma_bls_ina_se1_40_phase.questphase`; Dressed to Kill links from
`ma_bls_ina_se1_44_phase.questphase` and a regional repair graph. Both production
phases live under `base/open_world/minor_activities/badlands/inland_avenue_se1/`.
Directory-family matching alone would miss those implementations.

The journal export contains both a CyberPsycho and a Contract identity titled
Cyberpsycho Sighting: On Deaf Ears. The current
`ma_cct_dtn_03_phase.questphase` references the `quests/minor_quest/...`
identity and its POI, while the Contract identity uses
`quests/minor_activities/city_center/downtown/...`. Similar title/leaf names
are discovery hints, not sufficient evidence to merge the paths or transfer
an activation claim between them.

The 803 resource families also expose implementations outside the exported
quest list, including shared systems, ambient encounters, launch configurations
and test/repair resources. Their inventory is useful for discovering additional
mechanisms, but the family count is not a count of quests.

For Ghostline, the immediate design result is a layered library: primitive
conditions/actions; connected patterns with their boundary ports; lifecycle
compositions with owned state and cleanup; and content bindings for the actual
quest. Promote each layer only as far as its source and installed evidence
supports. This research supplies implementation candidates and acceptance
cases; it does not change Ghostline runtime behavior.
The [reduction plan](ghostline-block-roadmap.md) maps these compositions onto
the current compiler/lifecycle seams and identifies what must be tested before
promotion.
