# Black Lantern World

## Location Selection And World Origins

The typed manifest is complete with explicit placeholder NodeRefs. Select and
review locations before promoting or registering runtime resources. Use the
opening Iris site again as the later safe site so the quest has five principal
sites plus one drop point. Each chosen site becomes a world origin; all
Ghostline-owned triggers, devices, communities, markers, routes, and scene
placements use relative offsets.

| Origin | Required catalog evidence | Runtime review |
| --- | --- | --- |
| Iris briefing and safe site | Reuse established Iris site or `loot_anchor` plus `npc_staging_candidate`, with road access and room for Mara. | Confirm scene approach lifecycle, retained Mara staging, temporary vehicle placement, and whether the Iris community can be safely reactivated. |
| Freight yard | `vehicle` or `loot_anchor`, with nearby `terminal`, `plant_target`, and `access_point`. | Three-guard routes, stealth exits, vertical trigger coverage, and no vanilla quest-state ownership. |
| Memory clinic | `door_lock` plus `release_target_candidate`, with three pedestrian gates and defense anchors. | Mara navmesh continuity, cover, fixed-attacker paths, checkpoint safety. |
| Freight interchange | `vehicle` plus `parking_anchor_candidate`. | Drivable approach and departure, compatible player-vehicle entry, no obstructed theft animation. |
| Reconstruction relay | `access_point` or `antenna`, carrier parking, combat and three clue anchors. | Device interaction, retrieval-team staging, cleanup boundary, drop-point route. |
| Delivery | Kabuki `drop_point_009` unless a reviewed alternative is better. | Native reserve/deposit support and outcome-dependent item reservation. |

## In-Game Scout

The standalone **Ghostline: Black Lantern Scout** CET mod groups **40 distinct
quest placement targets** under the six reusable sites above: six explicit
world origins plus 34 initial sublocations. The checklist now additionally has
25 supporting targets (65 total), including separate Iris setup triggers and
NPC spots, Mara's initial spawn, Patch staging, repeatable guard/attacker spawn
and patrol points, drive routes, and per-site mappin captures. Label repeated
captures with the actor/objective and route order; a captured target is not proof
that every point in a patrol or encounter has been reviewed. The targets cover both Iris
scenes and supporting placements; the yard approach, encounter, clues, devices,
and exit; the clinic encounter, Mara release, three escort gates, and defense;
both vehicle stops and routes; the relay encounter, clues, core, and exit; and
final delivery.

The **Suggested exploration destinations** section offers eight provisional
presets across the six sites. The anonymous Northside yard and Ebunike docks
are separate alternatives; the elevated ship landmark is labelled separately.
Other presets cover the earlier Iris, medical-site, Arroyo interchange, relay,
and Kabuki delivery leads. Each includes review notes. These are exploration
coordinates, not approved origins or guaranteed standing positions. Teleporting
does not add a capture; use Capture after finding the desired position, and
Return to revisit the position before teleporting.

Saving retains numbered `.bak.N` copies of previous logs. Failed replacement
keeps the `.tmp` recovery payload and attempts to restore the original. A
malformed or inaccessible log blocks capture/save; repair or restore the log
and reload CET before continuing. Keep recovery files until the imported log
has been checked.

Captures can additionally be tagged as origins, approaches, triggers, devices,
clues, NPC staging, patrol points, route gates, vehicle placements, scenes,
cleanup boundaries, or miscellaneous anchors. Each record persists its site
and exact target together with player XYZ, yaw and forward vector, runtime
district/interior labels, notes, review state, and the current RedHotTools World
Inspector target when that optional mod is present. It can revisit a candidate
by teleport and return to the previous position.

Install it into an existing Cyber Engine Tweaks installation:

```powershell
py -B .\tools\gq003_black_lantern_scout.py install-cet `
  --game-root "H:\Cyberpunk 2077"
```

Open the CET overlay and use **Ghostline: Black Lantern Scout**. The capture,
teleport, and return actions are also assignable in CET's Bindings tab. The mod
writes `black-lantern-locations.json` beside its installed `init.lua`; reinstall
does not overwrite that log.

After a scouting session, validate and import the log into the quest package:

```powershell
py -B .\tools\gq003_black_lantern_scout.py import-log `
  --game-root "H:\Cyberpunk 2077"
```

The default reviewed source is `implementation/world-candidates.json`.
Import deliberately refuses to replace it unless `--force` is supplied.
