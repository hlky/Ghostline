# Black Lantern State

## Fact Model

### Canonical persistent facts

These facts are safe for later quests to import:

| Fact | Meaning |
| --- | --- |
| `gq003_job_accepted` | The opening Iris scene exited through the accepted route. |
| `gq003_stealth_succeeded` | V cleared the freight yard without the monitor observing detection. |
| `gq003_stealth_failed` | The freight-yard monitor observed detection. |
| `gq003_beacon_planted` | Iris's route beacon was installed. |
| `gq003_dispatch_breached` | Pair 07-B was identified in dispatch. |
| `gq003_mara_released` | Mara's restraint was opened. |
| `gq003_mara_escorted` | Mara passed all three ordered escort gates. |
| `gq003_mara_stabilized` | Mara survived stabilization on the completed route. |
| `gq003_carrier_stolen` | V took Pair 07-B's carrier. |
| `gq003_carrier_arrived` | The carrier reached the reconstruction relay. |
| `gq003_choice_preserve` | V selected preservation before operating the core. |
| `gq003_choice_burn` | V selected destruction before operating the core. |
| `gq003_route_preserved` | The core completed the preserve operation. |
| `gq003_route_burned` | The core completed the burn operation. |
| `gq003_cipher_delivered` | The outcome-specific physical package was deposited. |
| `gq003_completed` | Debrief, reward, and quest success completed. |

Exactly one stealth fact and exactly one choice/outcome pair should be set on a
clean completed run.

### Internal orchestration facts

These support restartability and typed-stage handoff but should not be treated
as major imported consequences:

```text
gq003_phone_start_sent
gq003_phone_reply_on_my_way
gq003_report_read
gq003_transfer_window_open
gq003_yard_reached
gq003_clue_board_scanned
gq003_clue_stabilizers_scanned
gq003_clue_restraint_scanned
gq003_yard_investigation_complete
gq003_yard_shard_read
gq003_yard_cleared
gq003_clinic_reached
gq003_clinic_security_resolved
gq003_jammer_disabled
gq003_mara_lost
gq003_safe_site_briefed
gq003_scene_choice_preserve
gq003_scene_choice_burn
gq003_patch_ride_complete
gq003_patch_vehicle_cleaned
gq003_relay_entered
gq003_retrieval_team_resolved
gq003_clue_carrier_rack_scanned
gq003_clue_core_scanned
gq003_clue_ledger_scanned
gq003_relay_investigation_complete
gq003_core_operated
gq003_relay_cleared
```

Do not use `gq003_mara_lost` as a lasting world consequence unless the quest is
expanded with a permanent failure branch.
