# Allen Street versus a vanilla residential corridor

Comparison and first test, 2026-10-27. This test supplies the missing ambient
layer; it does not establish that nearby encounter dialogue will be muffled.

## Evidence

Vanilla donor: `exterior_4_-29_-1_0.streamingsector.json`, definitions 76
(`{amb_int_main_upper_}01`) and 77 (`{amb_int_main_ground}`). The reviewed local
source is under `converted/world-location-database/full-world/serialized-sectors/
base/worlds/03_night_city/_compiled/default/`. Source SHA-256:
`a2a2b960f9e508ae6593de21c7f2b1016cc3f1cc1f75e0dc0bb0be5a5d1be2b6`.

Allen baseline: `building-lab-91ebe95eaefa`, including decorations and the
top-floor passage repair. The existing exported sector has eleven
`worldTriggerAreaNode` volumes carrying `worldInteriorAreaNotifier` with
`treatAsInterior=1`, no gameplay restrictions and `setTier2=0`. It has no
`worldAmbientAreaNode`, acoustic zone, outdoorness area or custom acoustic graph.
The gameplay interior requests still need runtime verification; the specialised
`worldInteriorAreaNode` class used by the vanilla scouting index is not used here.

| Audio setting | Vanilla donor | Allen baseline | First test |
| --- | --- | --- | --- |
| Ambient-area notifier | `audioAmbientAreaNotifier` | Absent | One area per floor |
| Channel | `TC_SoundAmbientArea` | Absent | Same |
| Metadata parent | `amb_area_int_default_corridors` | Absent | Same |
| Priority | 10 | Absent | Same |
| `amb_interior` | Ground 0.98, upper 0.9 | Absent | Same native float values |
| Reverb | `revb_interior_room_medium` | Absent | Same |
| Ground room tone | `amb_int_roomtone_apartment_large_warm_airy_01` | Absent | Same |
| Upper room tone | `amb_int_roomtone_appartment_med_warm_02` | Absent | Same |
| Notifier occlusion | Enabled | Absent | Enabled for the new areas |
| Physics-obstruction override | Not explicitly enabled | Absent | Not added |
| Acoustic graph | Separately generated vanilla world data | Vanilla world data only | Unchanged |
| Acoustic outdoorness override | No such node in this donor sector | None added | Unchanged |

The new notifier's occlusion flag does not prove that other emitters or NPC
dialogue become occluded. `amb_interior` responses depend on sound-bank routing.
Room tone or reverb becoming audible would prove only that the area is active.

## Test boundaries and isolation

Three authored `audio_areas` use the same building anchor and yaw as the mesh.
Their local XY footprint is X=3.2..17.8, Y=3.2..14.8. Floor bases are Z=0,4,8;
heights are 3.7,3.7,3.4. No quest-prevention, vehicle-forbidden, combat or time-skip
restrictions are copied from vanilla. No NPC or encounter edits, voice replacement,
global volume reduction, outdoorness override or graph relocation are included.

`generated/allen-interior-audio/comparison-verification.json` records donor
identity and confirms prior geometry, collision, doors, lights, navigation and
retrofit patches are unchanged. It also verifies the new settings match the
vanilla settings verbatim. Native readback checks the area outline, notifier,
event names, metadata parent, reverb and parameter values.

## Playtest

Use the usual Allen Street test save with the yard encounter still active.
Compare the same NPC exchange outside and inside. Enter the lobby, pause for
the audio transition, then listen from both apartment corridors. Check for
room tone and changed reverb separately from dialogue volume and clarity.
Leave the building and confirm exterior sound returns normally. If ambience
changes but dialogue remains clear, the next test should inspect the dialogue
emitter and obstruction query, then outdoorness or graph behaviour separately.

The technical basis for separating obstruction, graph occlusion and room sound
is CDPR's presentation:
https://media.gdcvault.com/gdc2023/Slides/pop_bielawski_marek.pdf

Package integrity and live audio acceptance are separate; installation receipts
and observed listening results must identify the tested candidate.


Installed test candidate: `building-lab-be9d407396c0`. All 95 building tests and native/package/install checks pass. Receipt: `generated/runtime-installs/20261027-093909-allen-interior-audio/installation.json`. Only Allen enabled; gameplay listening test pending.


### Audio test outcome and rollback (2026-10-27)

User reports outside NPC encounter dialogue remains audible with audio candidate
`building-lab-be9d407396c0`, plus possible radio disabling. Ambient-area matching
alone did not achieve the intended muffling. Radio causality is unconfirmed;
no claim that the corridor preset is solely responsible. Removed `audio_areas`
from active authoring layout and restored exact verified pre-audio candidate
`building-lab-91ebe95eaefa` while game closed. Geometry, decorations, passage repair
and original gameplay-interior requests retained. Six post-capture archive files,
including disabled quest packages, remain byte-identical. Failed audio archive
backed up in the rollback receipt folder. Restart test should check radio first,
then whether it still stops specifically during the vanilla yard dialogue.
No graph, outdoorness, NPC, global volume or capture changes made.
Receipt: `generated/runtime-installs/20261027-094915-allen-audio-rollback/installation.json`.
