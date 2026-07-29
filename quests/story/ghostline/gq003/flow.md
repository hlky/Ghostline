# Black Lantern Runtime Flow

## Canonical Runtime Flow

| # | Act | Stage ID | Block | Player-facing objective | Completion or state |
| ---: | --- | --- | --- | --- | --- |
| 1 | I | `patch_job_offer` | `phone_job_offer` | Respond to Patch. | Sets offer/reply state; does not yet set `gq003_job_accepted`. |
| 2 | I | `meet_iris_briefing` | `meet_contact` | Meet Iris. | Scene exit `job_accept` sets `gq003_job_accepted`. |
| 3 | I | `read_reconstruction_report` | `read_terminal_document` | Read Iris's reconstruction report. | Sets `gq003_report_read`. |
| 4 | I | `wait_for_transfer_window` | `time_gate` | Wait for the Black Lantern transfer window. | Sets `gq003_transfer_window_open`; initial implementation uses an elapsed game-time delay, not an absolute clock check. |
| 5 | I | `receive_yard_identifier` | `phone_conversation` | Read Patch's message. | Supplies yard alias, access phrase, and mappin activation. |
| 6 | II | `reach_freight_yard` | `reach_area` | Reach the Black Lantern freight yard. | Starts the yard compound root. |
| 7 | II | `remain_undetected` | `stealth_monitor` | Optional: Remain undetected. | Runs parallel to stages 8-12; sets exactly one stealth outcome when stopped. |
| 8 | II | `investigate_yard` | `investigate_clues` | Investigate the transfer yard. | Three clues; restraint case grants `Items.GhostlineBlackLanternRouteAuth`. |
| 9 | II | `read_expedited_handoff` | `read_shard` | Read the archived conversation. | Sets `gq003_yard_shard_read`. |
| 10 | II | `plant_routing_beacon` | `plant_item` | Install the routing beacon. | Sets `gq003_beacon_planted`. |
| 11 | II | `breach_dispatch_relay` | `hack_access_point` | Breach the dispatch relay. | Identifies carrier `PAIR 07-B`; sets `gq003_dispatch_breached`. |
| 12 | II | `leave_freight_yard` | `leave_area` | Leave the freight yard. | Sets `gq003_yard_cleared`, stops the monitor, and cleans up the yard community outside the larger boundary. |
| 13 | II | `clinic_location_call` | `phone_conversation` | Talk to Iris. | Confirms the clinic; opens on clean/detected branch. Patch reaction is a non-blocking companion message. |
| 14 | III | `reach_memory_clinic` | `reach_area` | Reach the memory clinic. | Activates clinic encounter state. |
| 15 | III | `clear_clinic_security` | `combat_encounter` | Neutralize the clinic security. | All authored guards defeated or incapacitated; nonlethal allowed. |
| 16 | III | `disable_neural_jammer` | `interact_device` | Disable the neural jammer. | Sets `gq003_jammer_disabled`; Iris can resolve Mara's implant. |
| 17 | III | `release_mara` | `release_or_rescue_npc` | Release Mara. | Sets `gq003_mara_released`; Mara community remains active. |
| 18 | III | `escort_mara` | `escort_npc` | Escort Mara out of the clinic. | Three ordered route gates; sets `gq003_mara_escorted`. |
| 19 | III | `stabilize_mara` | `defend_target` | Protect Mara while Iris stabilizes her implant. | Timed fixed-attacker hold; success sets `gq003_mara_stabilized`. Failure sets transient `gq003_mara_lost` and reloads the pre-defense checkpoint. |
| 20 | III | `meet_iris_safe_site` | `meet_contact` | Meet Iris at the safe site. | Second Iris scene; Mara remains staged nearby. Sets `gq003_safe_site_briefed`. |
| 21 | IV | `patch_confession` | `phone_conversation` | Talk to Patch. | Patch admits what he withheld and sends the temporary vehicle. |
| 22 | IV | `enter_patch_vehicle` | `enter_vehicle` | Get in Patch's vehicle. | Activates compatible temporary player-vehicle lifecycle. |
| 23 | IV | `ride_with_patch` | `ride_with_contact` | Wait for Patch. | Patch joins as passenger; ambient route dialogue begins. |
| 24 | IV | `drive_patch_to_interchange` | `drive_to` | Drive to the freight interchange. | Sets `gq003_patch_ride_complete`. |
| 25 | IV | `steal_pair_07b` | `steal_vehicle` | Steal the Black Lantern carrier. | Sets `gq003_carrier_stolen`. |
| 26 | IV | `drive_carrier_to_relay` | `drive_to` | Drive the carrier to the reconstruction relay. | Sets `gq003_carrier_arrived`. |
| 27 | IV | `cleanup_patch_vehicle` | `vehicle_cleanup` | Exit the carrier. | Removes only the temporary Patch vehicle after arrival; the stolen carrier remains staged for investigation. |
| 28 | IV | `enter_reconstruction_relay` | `reach_area` | Enter the reconstruction relay. | Activates relay encounter and interior objective. |
| 29 | V | `defeat_retrieval_team` | `combat_encounter` | Defeat Morita's retrieval team. | All authored hostiles resolved; nonlethal allowed. |
| 30 | V | `investigate_reconstruction_relay` | `investigate_clues` | Investigate the reconstruction relay. | Carrier rack grants `Items.GhostlineBlackLanternCipher`; core and ledger complete the evidence set. |
| 31 | V | `argue_relay_outcome` | `phone_conversation` | Talk to Ghostline. | Morrow and Iris present sequential arguments inside one conceptual stage. |
| 32 | V | `choose_relay_outcome` | `choice_gate` | Decide what survives. | Sets one choice fact and reconverges. |
| 33 | V | `operate_reconstruction_core` | `interact_device` | Jack in to the reconstruction core. | Selected fact controls authored device result; common completion signal sets one route-outcome fact. |
| 34 | V | `leave_reconstruction_relay` | `leave_area` | Leave the reconstruction relay. | Sets `gq003_relay_cleared`; cleans up retrieval community after V clears the site. |
| 35 | VI | `deliver_black_lantern_package` | `deliver_drop_point` | Deposit the Black Lantern package. | Preserved route deposits cipher; burned route deposits signed receipt. Sets `gq003_cipher_delivered`. |
| 36 | VI | `black_lantern_debrief` | `phone_conversation` | Respond to Ghostline. | Outcome and yard-stealth opening branches, reward, `gq003_completed`, quest success. |

## Compound And Failure Topology

### Freight yard

Stages 7-12 use the `gqt002` compound-root topology:

```text
reach yard
  -> start stealth monitor ------------------------------+
  -> investigate -> shard -> plant -> breach -> leave ---+-> stop monitor
                                                             -> continue
```

`gq003_stealth_failed` is sticky once detection occurs. When
`gq003_yard_cleared` stops the monitor, the monitor sets
`gq003_stealth_succeeded` only if failure is still zero. Detection changes
dialogue and debrief tone but never blocks progression.

### Mara survival

Mara cannot be permanently lost on the canonical route because stages 20-36
depend on her stabilization and testimony. `gq003_mara_lost` is therefore a
transient failure signal used to fail the defense objective and reload the
checkpoint before stage 19. It is not imported by later quests.

If a future design wants Mara's death to be a lasting branch, it needs a second
Act III-VI route, alternate safe-site dialogue, another source for the vehicle
location, and replacement final consequences. That is outside this version.

### Final operation

The choice and device action remain separate:

```text
Morrow and Iris argue
  -> preserve choice -> gq003_choice_preserve = 1 --+
  -> burn choice ----> gq003_choice_burn = 1 -------+-> common core interaction
                                                         +-> preserved fact and intact cipher
                                                         +-> burned fact and signed receipt
```

The interact stage waits for one common device completion event. Choice facts
select presentation, inventory mutation, and the final route fact; they do not
create two unrelated interaction stages.
