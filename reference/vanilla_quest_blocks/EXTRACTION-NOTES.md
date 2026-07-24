# Extracted Block Notes

These notes record the smallest useful behavior observed in the untouched
vanilla CR2W resources. They define reduction targets, not permission to copy
whole quest-local graphs into Ghostline.

## `read_terminal_document`

Source:
`base\quest\side_quests\sq021\phases\sq021_randys_room.questphase`

The relevant nested computer flow contains:

| Node | Behavior |
| --- | --- |
| 175 | `ComputerManager` enables UI interactivity for `#sq021_randy_pc` |
| 176 | Waits for `sq021_randy_pc_webfile_found > 0` |
| 177 | Disables computer UI interactivity |
| 179 | Re-enables computer UI interactivity for the next document step |
| 182 | Activates `internet_sites/drugs_are_bad/05_secret_page` |
| 191 | Sets `sq021_thisisfucked_read = 1` from the computer-page output |
| 192 | Waits for `sq021_thisisfucked_read > 0` |
| 193 | Sets the next quest fact after the read has been observed |

The important boundary is between the computer UI graph and the quest phase:
the `sq021_04b_randys_pc.scene` node exposes `webfile_out`; that scene output,
not the journal activation nodes, is the meaningful selection/read event. It
sets a dedicated fact which the phase observes. There is no generic
journal-visited condition to substitute.

Proposed typed contract:

```yaml
- type: read_terminal_document
  id: inspect_terminal_record
  computer: "#quest_computer"
  document_entry: internet_sites/ghostline/record
  completion_fact: ghostline_terminal_record_read
  objective: read_terminal_record
```

Reduction requirements:

- Bind an existing computer device or computer-owned graph socket.
- Activate exactly one email/page journal entry.
- Route its selected/read output to `completion_fact`.
- Wait on that fact and complete the objective once.
- Do not award inventory shard loot or use shard pickup/preview state.

## `time_gate`

Sources:

- `base\quest\side_quests\sq011\phases\sq011_concert.questphase`
- `base\quest\side_quests\sq011\phases\sq011_follow_up.questphase`

Observed `questGameTimeDelay_ConditionType` nodes:

| Quest node | Delay | Downstream role |
| --- | --- | --- |
| `sq011_concert` 146 | 23 hours | Continues into a game-manager/contact sequence |
| `sq011_follow_up` 61 | 3 days | Continues into a content-token wait |
| `sq011_follow_up` 87 | 5 hours | Continues into a content-token wait |

Proposed typed contract:

```yaml
- type: time_gate
  id: wait_for_contact
  days: 0
  hours: 6
  minutes: 0
  seconds: 0
```

The block owns only elapsed game time. A following `phone_conversation`,
message activation, journal update, or content-token gate remains a separate
manifest step.

## `stealth_monitor`

Sources:

- `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\phase\sts_wbr_jpn_03_streetstory.questphase`
- `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\phase\sts_wbr_jpn_03_combat.questphase`

The street-story phase activates the optional `stealth` journal objective and
keeps a branch waiting for `jpn_03_stealth_fail == 1`. Journal nodes then
change the optional objective state. The stored fact is also used later to
choose between stealth and non-stealth debrief messages.

Proposed typed contract:

```yaml
- type: stealth_monitor
  id: remain_undetected
  objective: remain_undetected
  failure_fact: ghostline_stealth_failed
  success_fact: ghostline_stealth_succeeded
  stop_fact: ghostline_stealth_monitor_stop
```

Reduction requirements:

- Start the optional objective and failure listener together.
- Allow the main quest flow to proceed independently.
- On failure, set the objective failed once and preserve the failure fact.
- On stop/convergence without failure, complete the optional objective and set
  the success fact.
- Terminate the listener after convergence so later combat cannot change the
  resolved outcome.

This cannot be represented by the current `optional_condition` template,
because that template evaluates a fact only at entry and immediately
converges.

## Remaining advanced reductions

| Block | Reduced reusable topology | Promoted vanilla evidence |
| --- | --- | --- |
| `plant_item` | device action → device condition → remove item → completion fact | `sts_std_arr_05_openworld`, `q108_06b_tower_mainframe` |
| `defend_target` | race encounter-complete fact against named target defeated | `sts_wbr_jpn_09_gameplay`, `sq004_drones` |
| `release_or_rescue_npc` | unlock/release → device condition → named target ready → completion | `sts_wat_kab_02_openworld`, `sq004_03_raffen_shiv_camp` |
| expanded `escort_npc` | gameplay AI tier → three ordered named-actor gates → completion fact | `sq031_rogue` plus existing escort references |
| `enter_vehicle` / `steal_vehicle` | V mounts a referenced vehicle as driver | `sq004_02_drive` |
| `ride_with_contact` | AND join of player and named-contact mount conditions | `sq004_02_drive`, `sq031_rogue` |
| `drive_to` | referenced vehicle enters destination trigger | `sq004_02_drive` |
| `vehicle_cleanup` | despawn a player-vehicle TweakDB record | `sq031_porsche` |

These are orchestration contracts. Workspots, patrol/spline movement, combat
wave production, device controller functions, computer scene sockets, and
arbitrary-world-vehicle despawning remain separately authored.

## Promotion rules

- `cr2w/` files are byte-for-byte extracted game resources.
- `raw/` files are WolvenKit serializations used for inspection.
- Reduced Ghostline templates must use explicit bindings instead of retaining
  vanilla facts, NodeRefs, journal paths, device objects, or community entries.
- Round-trip success proves serialization only. Each instantiated block still
  needs an installed in-game test.
