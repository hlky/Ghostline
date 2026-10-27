# Location selection and environment preflight

Only the AKPP hub is selected. No delivery site coordinates are invented here.
Use logical slots until each site has an actual world survey and approach test.

| Slot | Needed space | Encounter | Selection status |
| --- | --- | --- | --- |
| hub_akpp | Existing small office, desk, terminal, seated manager | Offer, pickup, settlement | Existing retrofit in Building Lab |
| residential_a | Lobby, security desk, controlled entrance, two nearby apartment doors | A and C; obvious repeated approach | User supplied Allen-sign Kabuki candidate; exterior imported, interior pending |
| residential_b | Distinct entrance, broken passenger lift, short accessible stairs, penthouse/service landing | Drinks delivery and optional kitchen drop | Survey pending |

## Route requirements

Candidate captured 2026-10-26: the Allen-sign building near entrance
`[-1063.446533,1782.144653,28.415075]`. Building Lab contains a source-pinned
three-level exterior reference under `kabuki-allen-residential-shell`. See
`projects/experiments/building-lab/surveys/kabuki-allen-residential.md` for exact
matches and limits. This is a candidate for A/C; usable floor area, ownership,
entrance cut and stair route have not yet been validated. Do not mark the site
runtime-ready based on its reconstructed exterior.

An interior authoring draft now exists as
`projects/experiments/building-lab/buildings/allen-street-residential-retrofit.building.json`:
security lobby, two return stair connections, Adrian on the first floor and Niko
on the second. Both destinations pass offline connectivity. Retained entrance/
shop collision, an upper unit-box collision and occlusion need review before
installation. The original building name remains unknown; Allen is the street
sign's entity identity.

Prefer Kabuki or nearby Watson so AKPP remains a believable local depot. A and
B should be far enough apart that returning to A is irritating and legible,
but not a driving marathon. Target 30–60 seconds each way at ordinary movement,
then tune from an actual playthrough. V should recognise building A on return.

Find A before B. Its two doors must visibly share the same landing or corridor;
avoid a nominal shared address that feels like two unrelated locations. An
existing lobby retrofit is enough. B may use another building or another
approach to the same complex only if the A → B → A waste remains clear.

## What to capture from the game

For each candidate: one exterior screenshot identifying the building, entrance
door node identity and transform, player position on the public approach, and
views of the intended interior volume. An inspector node's pivot is not proof
of a clear walkable space. Record mesh, sector, placement/instance, appearance,
collision actor and bounds when available.

For A additionally capture guard desk position/facing, access barrier, landing
position, both recipient doors, and the safe conversation areas. For B capture
stairs at base/top, each stair turn, lift door, landing, optional kitchen drop
and any intervening collision. Record floor elevation and ceiling clearance.

No need to gather every wall immediately: start with entrance and usable volume,
then request exact obstruction data only where the survey reveals a problem.

## Before committing a retrofit

- Confirm it is not an active vanilla quest/gig set, vendor route or essential
  NPC path. Preserve neighbouring interiors and public pavement.
- Identify shared meshes, collision groups, occluders, portals and distance/LOD
  behaviour. Scope changes to surveyed placements, not whole shared resources.
- Test visibility from inside/outside and both sides of every patched opening.
- Prove collision and floor joins while walking, not only with FreeFly.
- Reserve interaction spaces and door swings before furnishing. Keep a return
  path clear while actors stand, talk and enter idle workspots.
- Verify ordinary approach, leaving/returning, save/load, fast-travel arrival
  and streamed-out/streamed-in actor recovery.
- Agree on available vanilla navigation before relying on walking NPCs. Use
  stationary doorstep/intercom interactions for the first route if necessary.

## Existing AKPP contract

The Allen Street residential retrofit now has a separate installed walkthrough
candidate, `building-lab-91ebe95eaefa`, with a security lobby and two residential
landings connected by return stairs. See
`projects/experiments/building-lab/surveys/allen-street-residential-retrofit.md`
for its receipt, entrance coordinates and focused playtest. It is provisional:
no recipient actors or GQ005 quest progression ship in this package. Live
clearance, visibility and vanilla quest ownership must pass before committing
the delivery encounters.

Authoring source:
`projects/experiments/building-lab/buildings/akpp-logistics-open-shell.building.json`.
Its origin is a surveyed layout anchor, not the manager's feet or scene pivot.
Derive the manager spawn from the workstation transform. Retain Ru Lai, street
geometry, the repaired doorway and current cabinet orientations.

Before installation choose one owner for the manager and terminal. The existing
Building Lab content sector owns a generic seated worker and a test computer
fact. A quest integration must replace/rebind that worker and add quest-specific
terminal readables; leaving two communities active would duplicate occupancy.
Do not assume the office test file proves the new policy has been read.


Allen stair-back follow-up (2026-10-27): installed `building-lab-5ca1bfd10661`; duplicate concrete rear panels removed, both turning landings extend to existing grey walls. All 93 building tests, native geometry and package checks pass; live stair-back retest pending. Decorations remain authored separately. Receipt: `projects/experiments/building-lab/generated/runtime-installs/20261027-005055-allen-stair-backs/installation.json`.


First-floor shared stair partition (2026-10-27): installed `building-lab-f7c5f529385e`; lower upper-right guard and next full-height enclosure now share one face, with the overlapping guard omitted above the floor. Both delivery routes, all 93 building tests, native and package checks pass. Live test pending; decorations remain excluded. Receipt: `projects/experiments/building-lab/generated/runtime-installs/20261027-005336-allen-shared-stair-wall/installation.json`.


Stair shaft slab seams (2026-10-27): installed `building-lab-d7ce5db68282`; coincident floor/ceiling lips removed along both room-provided stair side walls, stacked wall faces meet without vertical overlap. 228 wall-only probes, both delivery routes and all 93 tests pass. Native/package/install verified; live flicker and seam retest pending. Decorations excluded. Receipt: `projects/experiments/building-lab/generated/runtime-installs/20261027-005749-allen-stair-slab-seams/installation.json`.


Combined Allen decoration test (2026-10-27): installed `building-lab-21e988389558` with all latest stair/slab fixes unchanged, plus 68 vanilla decoration modules and 15 warm native lights. Both delivery routes and native/package/install checks pass. Live lighting, materials, clearance and seam acceptance pending. Receipt: `projects/experiments/building-lab/generated/runtime-installs/20261027-010005-allen-decorated-current/installation.json`.


Allen top-floor passage repair (2026-10-27): installed `building-lab-91ebe95eaefa`; extra anti-flicker cuts now intersect solid wall footprints and preserve the hallway floor beyond the wall end. All decorations retained. Nine native floor probes, both delivery routes, 93 tests and package/install checks pass. Yard voice muffling remains an acoustic-authoring investigation; no NPC/audio edits. Receipt: `projects/experiments/building-lab/generated/runtime-installs/20261027-011203-allen-floor-passage/installation.json`.


Allen interior audio test (2026-10-27): installed `building-lab-be9d407396c0`; three native residential ambient areas supply corridor metadata, amb_interior, warm room tone and medium-room reverb. Prior geometry/decorations/lights/navigation unchanged; no graph, outdoorness or gameplay restriction edits. Only Allen enabled after capture; other disabled packages preserved. All 95 tests and native/package/install checks pass; NPC dialogue muffling unconfirmed. Comparison: `projects/experiments/building-lab/surveys/allen-interior-audio-comparison.md`.


Allen audio-test rollback (2026-10-27): outside NPC dialogue remained audible and user observed possible radio disabling. Restored verified `building-lab-91ebe95eaefa`, removed three ambient audio areas from active source, preserved decorations/geometry and disabled quest packages. Radio causality unconfirmed; restart retest pending. Receipt: `projects/experiments/building-lab/generated/runtime-installs/20261027-094915-allen-audio-rollback/installation.json`.
