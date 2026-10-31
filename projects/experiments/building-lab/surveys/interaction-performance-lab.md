# Interaction performance sky lab

Created and saved through Building Lab on 2026-10-27 for the occupied-NPC →
conversation → return-to-activity test. This is a new isolated layout, separate
from the earlier navigation lab and city retrofits.

Source: [interaction-performance-lab.building.json](../buildings/interaction-performance-lab.building.json).
Open **Interaction performance · sky lab** in the Building UI's saved layouts.

The quest-owned playable candidate is now [GQT008](../../../test-quests/gqt008/README.md).
It copies this room geometry into its own namespace and supplies a compatible
Barry actor and native lifecycle. Its geometry copy omits the workstation
terminal. Use the GQT008 package by itself for that test; installing both area
variants would overlap rooms at the same coordinates. Runtime validation is pending.

## Layout

- Industrial kit, single floor, world anchor `(140, 100, 700)`, yaw 0.
- Two 12 × 6 m rooms: **Approach and return**, then **Conversation and activity**.
- Two adjacent open bays form a broad passage; no doors or stairs in this test.
- Desk, contact chair, visitor chair, paperwork and mug; native computer fixture.
- 144 m², 59 mesh placements, 50 collision boxes.
- Experimental Human navigation on layer **241**, one tile, 12 faces, one island.

The five authored furniture/prop modules preserve their measured vanilla sizes
and source/preview hashes. Library furniture does not acquire its original
physics collision automatically. Approach routes are clear of the desk/chairs;
visual fit and physical obstruction still need an installed check.

The editor preview uses neutral materials. Final lighting, streaming, floor
contact and native NPC navigation are not established by that preview.

## Quest bindings

The exported `quest-bindings.json` and `quest-block-fragment.json` retain:

| Binding | Value |
| --- | --- |
| Area trigger | `$/mod/building_lab/#interaction-performance-lab_content/#office_area` |
| Contact community | `$/mod/building_lab/#interaction-performance-lab_content/#contact_community` |
| Entry / phase | `worker` / `default` |
| Chair workspot | `$/mod/building_lab/#interaction-performance-lab_content/#contact_seat` |
| Computer | `$/mod/building_lab/#interaction-performance-lab_content/#contact_computer` |
| Computer read fact | `interaction_performance_lab_contact_file_read` |

The default fixture binds `Character.WorkerSpecialistMale`, appearance
`service__worker_ma_generic_worker_01`, and
`base\workspots\common\chair\generic__sit_chair__sit_around__01.workspot`.
**The community is inactive on start.** The area-only package will not spawn
the contact until an owning quest activates it and waits for CharacterSpawned.
This fixture is not a completed interaction quest.

When adding the new performance blocks, select a compatible actor/rig for the
donor animation set. The worker binding is not evidence that Barry's male_big
performance presets have been retargeted or visually accepted on this actor.
The scene owns speech, reactions and activity transitions; its phase owns
activation, readiness, interruption/return state and departure cleanup.

## Verification and artifacts

The UI export `generated/building-editor/exports/80159134383e` passed native
readback for seven resources, including geometry, content/community/device
resources and the embedded navigation sector. Its editable-project ZIP is
`generated/building-editor/exports/80159134383e.zip`, SHA-256
`1c8dc1d390c5e3bfecc2c4323a0f43f4aa7c36dc5596d694c568196c333c7755`.

The normal packager produced **building-lab-7324de9d6e0c**:

`generated/building-editor/exports/80159134383e/generated/packages/building-lab-7324de9d6e0c/ghostline_interaction_lab.zip`

Package ZIP SHA-256:
`db7fc85920e9b14afea0d03471fd15f70707da702a0442809febc316a7b8d8a7`.
Package extraction/payload verification passed. The archive and registration
names are `ghostline_interaction_lab.archive` and
`ghostline_interaction_lab.archive.xl`; the package was **not installed**.

Offline routes pass in both directions between local `(3,2,0)` and `(7,7,0)`,
and from `(3,2,0)` to `(9.8,9,0)`. These checks establish surface connectivity,
not live actor traversal. A convenient player arrival point is approximately
world `(143,102,701)`, above the approach-room floor.

Local evidence is under `generated/interaction-performance`: compiler/route
verification, package log, exported bindings/report snapshots and `editor.png`.
Generated exports are reproducible staging, not authoring source.

## First installed route to prove

1. Load the area and verify floor collision, furniture, computer and visibility.
2. Activate the contact through the test quest; confirm exactly one actor at
   the intended activity and wait for readiness before starting speech.
3. Approach from the first room; verify acknowledgement, gaze and activity-to-
   conversation transition with the selected compatible actor/performance.
4. Leave before engagement, leave during speech, and return. Check deliberate
   resume behavior and retirement of old movement/performance commands.
5. Complete the exchange, restore the activity, and test departure-owned cleanup.
6. Repeat after save/load. Record visual alignment, movement and each lifecycle
   result against the actual installed package and save state.
