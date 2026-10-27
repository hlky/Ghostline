# Building Lab

This project owns plain parametric building layouts under `buildings/` and the
`mod/building_lab/` depot namespace. The local editor and compiler live under the
repository's `tools` directory. See
[Building Lab authoring](../../../docs/authoring/building-editor.md).

The [complete discovered kit library](../../../docs/authoring/building-kits.md)
contains 9,859 measured CMesh modules and 15 room presets. `motel-modules` is an
additional example using a new preset and a freely placed native handrail.

Export each layout into an ignored `generated` directory. Each export is a
self-contained WolvenKit project with its own raw and binary resources,
ArchiveXL registration and package profile. This authoring container is not a
ready-to-install runtime project. `navigation-lab.building.json` demonstrates two storeys, guarded stairs and two
interactive doors at the isolated test anchor `(100, 100, 700)`. Its native
navigation remains experimental until live NPC traversal passes. See
[Building navigation](../../../docs/authoring/building-navigation.md).


## Rancho shell retrofit

`rancho-retrofit` adds an 18 m² lined room with a 3.5 m ceiling, using the
existing white fake-door aperture on the long brick façade. The first side
entrance test exposed the sliding leaf outside the corner; that entrance is
reverted. The original side wall and stand generator are retained again.

The replacement uses vanilla `single_door_hinged.ent`, appearance
`doors_single_hinged_h`: the same leaf and casing meshes as the original static
door. Its casing centre is aligned to the surveyed original frame and its stock
+90 degree motion swings into the room. The generated collision lintel is at
2.5 m to clear this taller leaf. The old static leaf/casing and selected casing
and door-bay collision actors are replaced; generated jambs/header and the
native physical casing/leaf supply replacement collision.

The active source selection is `surveys/rancho-original-door.json`; older front
and side proposals remain as history. Source snapshots in
`generated/rancho-retrofit/evidence/current-game` were freshly extracted from
the full installed archive/pc set and pinned by SHA-256. Base-content-only
sector indices differ. Re-create and verify these game-owned reference caches
before exporting from a fresh clone.

Export with `tools/building_builder.py export` using the repository-root path
to the layout, `--serialize`, and an output project under `generated`. Package
that project with `tools/package_project.py --profile building-lab-test`.
The current installed candidate is `building-lab-test-b72cb3881408` under
`generated/rancho-door-collision/generated/packages`. Receipts and prior-file
backups live under `generated/runtime-installs/20261026-104335-rancho-door-collision`.
All isolated Building Lab tests use the same archive/CET names.

Load a city test save. In CET Building Lab choose **Street approach** as start
and **Rancho interior** as end, then **Teleport V to start**. Test the original
white door as V first: check closed alignment, inward opening, threshold, room
lining and return crossing. Then spawn/bind an NPC, **Bring NPC to start**,
**Run native query**, and **Walk NPC to end** when the query passes. Reverse
start/end and repeat. Use **Return V** and clean up the test NPC afterwards.

48 building tests, native resource readback, package extraction/hash checks,
and eight unlocked/locked bidirectional Detour controls pass. The controls cover
both overlapping interior surface selections. Live door fit, collision,
occlusion, streaming and NPC traversal remain pending for this revision.

The native door opened in the first original-door playtest, but V was blocked.
The current revision additionally removes the original fake leaf's separate
fixed box: placement 850, actor 123, shape 0 in `exterior_-2_-3_0_3`.
Its bounds cover the full entrance. Crossing is pending a new live test.


## Rancho residential house — previous ground-floor test

`buildings/rancho-residential-house.building.json` owns the first playable
180 m² ground floor: entrance hall, living room, kitchen/dining, two bedrooms,
bathroom, utility and study. It has seven native hinged doors and eight warm
point lights. Rooms are unfurnished. The existing porch, short staircase,
exterior shell, pitched roof and balcony remain. Upstairs and the rear exterior
route are outside this ground-floor test.

Candidate `building-lab-test-a3f424928a7f` is under
`generated/residential-house-visual-fix/generated/packages`. It replaces the earlier
small Rancho lab in the same archive/CET slots. Backup/receipt:
`generated/runtime-installs/20261026-120133-house-visual-fix`.

The sealed decorative front door (placement 212 in `exterior_0_-34_0_0`) and
its proxy (placement 98 in `exterior_0_-17_0_1`, owner
15517176256055994014) are replaced. Their surveyed native template/owner and
source hashes are checked before export. The porch and stair collision stay.
Four manually surveyed nav triangles follow the retained porch and upper
steps, with a short Floor connection to the street.

The expansion's `navigation_0_-9_0_3` supplies retained Human ground beneath
part of the house. The `navigation.terrain_mask` replaces only placement 2,
resource `navigation_0_-14_0.navmesh`, with a mod-owned copy preserving all 25
tile buffers, topology and connection metadata. Only the flags for 43 triangles
wholly inside the shell and near ground-floor height are cleared. Boundary
crossing polygons and Vehicle navigation are retained. `building_nav_mask.py`
verifies that no other byte changes. Source selection was checked against the
installed expansion/mod/hot archive indexes and extracted with WolvenKit from
`ep1_1_nightcity.archive`; the base-content copy is superseded.

Evidence: `generated/residential-house/evidence`. 53 building tests, Ruff,
five-resource native readback, package extraction/hash checks and 64 street ↔
room route controls pass. Controls cover all eight rooms, both load orders and
locked/unlocked front door. The previous build passed live Street approach →
Bathroom query and observed NPC movement without teleporting (14.12 seconds,
15.44 m). Other individual routes are not recorded as live passes.

The first house playtest exposed severe camera-dependent disappearance and
door-frame seams. The current revision removes only this house's three
instanced occluder groups (eight matrices): placement 425 in
`exterior_0_-17_0_1`, 524 in `exterior_0_-5_0_3`, and 571 in
`exterior_0_-9_0_2`. Adjacent house groups remain. Source hashes/counts and
explicit whole-group acknowledgements guard the selections; ArchiveXL does
not offer individual occluder-instance deletion. See
`surveys/rancho-residential-house-occlusion.json`. Door casings are centred
in the 17.5 cm wall volume so their 26 cm depth covers both facings.
Both navigation resources are byte-identical to the NPC-tested build.
New visual behaviour needs an in-game approach/room/angle test.

Relaunch Cyberpunk, load a city save, select **Street approach → Entrance hall**
in CET Building Lab, then **Teleport V to start**. Test the steps/front door
and every room as V, including door swings, seams, lighting and collision.
Then spawn/bind an NPC, **Bring NPC to start**, **Run native query**, and
**Walk NPC to end** when it passes. Reverse the route and repeat. Test each
named room, especially Rear bedroom, Utility room and Study, where retained
terrain previously won nearest-surface queries. Inspect observed movement,
not just the query result. Clean up the test NPC and use **Return V** afterwards.


## Two-storey house — previous test

Supersedes the ground-floor handoff above. Candidate
`building-lab-test-95a71d2619cb` is under
`generated/residential-house-upstairs/generated/packages`. Backup/receipt:
`generated/runtime-installs/20261026-122603-house-upstairs`.

The vanilla shell has two storeys with differently pitched roof wings. The
surveyed upper floor is at local Z=4.0 m, matching the original balcony and
upper-wall bases. Current layout has 171 m² downstairs and 54 m² upstairs,
12 rooms total. A guarded 1.2 m wide, 6 m run stair has 1.5 m landings and a
separate corridor alongside. Upstairs contains a landing, bedroom and bathroom.
The lower kitchen and rear bedroom were resized to make room for the flight.
The rear bedroom is now X=6..9, Y=-12..-6, beyond roof edge placement 125;
its ceiling remains 3.5 m. Ground V/NPC routes from the older layout are
historical evidence, not runtime passes for this changed plan.

Plain door surrounds use measured full-wall plaster sections instead of the
stock exterior doorway's recessed orange trim. Exact shaft cuts split slabs
within a 3 m tile, preserving the corridor floor and avoiding ceiling/floor
faces through the flight. All generated door endpoints and physical guards
are included in native and offline checks.

Two fixed windows are fitted: ground Utility room and Upstairs bedroom.
The original window material renders a fake parallax room. A mod-owned mesh
clone redirects only the glass slot to vanilla `window_generic_glass.mi`
(`glass.mt`); all 501 vertices / 458 triangles match the measured original,
and native render-buffer bytes are preserved. Ground facade placement 399
instance 1 is replaced in place. Upper facade placement 387 instances 6/7
are replaced with a window and measured filler sections. Other instances and
original window/wall collision remain. Windows do not provide walking routes.
The upper window lines up with the bedroom's generated aperture. Actual glass
appearance and visibility still require the live test.

Survey: `surveys/rancho-residential-house-upstairs.json`. 55 building tests,
Ruff, six native resource readbacks, package extraction/hash checks and 112
offline controls pass. Controls cover street ↔ every room and stair landing,
both tile load orders and locked/unlocked front door. No live pass is claimed
for the new stairs or windows.

Relaunch with a city test save. In CET Building Lab choose **Street approach →
Upstairs bedroom**, **Teleport V to start**, and first walk the route as V.
Inspect the revised rear bedroom, plain wall joins, both window views, stair
headroom, landings and guard seams. Then spawn/bind the NPC, **Bring NPC to
start**, **Run native query**, and **Walk NPC to end**. Swap start/end for the
return/downstairs route. **house stairs foot → house stairs top** isolates the
flight; both points are ready in the dropdowns. Test the Upstairs bathroom too.

## House entrances and balcony — previous test

The exterior walk-around supersedes the previous two-storey plan. Candidate
`building-lab-test-d1bce9cb9d42` is installed from
`generated/residential-house-access/generated/packages`. Receipt and previous
payload backup: `generated/runtime-installs/20261026-132337-house-access`.
Installed with Cyberpunk closed at 2026-10-26 13:23 UTC. Four installed payload
hashes match the verified WolvenKit package.

The house has two usable storeys: 197 m² downstairs and 90 m² upstairs,
14 rooms including measured annexes. The low wing is a garage workshop at
local Z=-0.6 m, connected by physical steps into the Living room. The original
garage shutter is removed with only its dedicated collision; the frame stays.
This test uses a fixed-open bay. The actual rear porch door opens into a rear
vestibule connected to the stair hall. A new Upstairs lounge follows the
higher front strip of the low roof wing and opens onto the original wraparound
balcony through its surveyed side door. Three stacked clutter objects were
cleared from the balcony route; the barrel remains with a conservative
approximate keepout that needs live checking.

The stair foot now faces the front circulation route; the top opens onto the
rear landing. Riser heights, ramps, low-end guards and runtime probes reverse
together. Downstairs wall caps stop below the upper slab, upper wall foundations
start at floor level, and floor lips are normalized to eliminate overlapping
tile faces. The exact roof support instance protruding through the upstairs
landing was shortened to end before the lining, with its collision replaced.
Native hinged door leaves reserve their measured fully-open footprint plus
agent clearance, including the garage landing. This must still be observed
in game while the door animates and the NPC approaches.

58 building tests, Ruff, six native resource readbacks, package extraction/hash
checks and 176 offline route controls pass. Controls use generated tiles and
the retained vanilla Human tile in both load orders/directions, with every
interior entrance locked as a negative control. The rear porch mask now
disables 51 polygons while preserving all 25 buffers and changing only flags.
These are offline results; this revision has no live pass yet.

Survey: `surveys/rancho-residential-house-access.json`. Ten supplied screenshots,
geometry bounds, navigation controls and installation receipt are saved in
`generated/residential-house-access/evidence`.

Relaunch with a city test save. Walk as V through the front, rear porch and
garage entrances; inspect the garage step-up, upstairs floor joins, landing
wall and stair clearances. From Upstairs lounge, open the side door and walk
the balcony around its corner. Then use Building Lab points **Street approach**,
**Garage workshop**, **Rear vestibule**, **Rear porch**, **Upstairs lounge**,
**Balcony doorway** and **Balcony front**. Bring NPC to start, run the native
query and observe the walk. Reverse each route. Watch the front hinged leaf
and balcony clutter closely. **house stairs foot → house stairs top**, then
reverse, isolates the flight. Successful queries alone do not prove traversal.

## House floor-plan revision — previous installed test

Candidate `building-lab-test-cfeba1bd6c30`, installed 2026-10-26 13:52 UTC
with the game closed. Receipt and previous payloads:
`generated/runtime-installs/20261026-135203-house-plan/installation.json`.
Project/package: `generated/residential-house-plan/generated/packages`.
All four installed payload hashes match the verified WolvenKit package.

The prior garage opening was wrong: the source frame is scaled X=1.4773,
Z=1.2457, while the lining used an unscaled 3 m opening. It now uses a 4.3 m
aperture and the scaled native `shutter_window_w300_h250.ent` automatic door,
including its actual controller CRUID `1563417374541762560`. Original static
frame/panel and their exact fixed collision are removed. The device owns its
frame and moving panel. The garage finish rises to Z=-0.35 above retained
terrain and has a physical 0.35 m step-up to the main house.

Ground floor is reorganized around front entry/dining, open living circulation,
window-side kitchen, utility/mudroom, rear bedroom and measured rear entry.
The rear entry joins circulation along the stair's west side; the immediate
opposing internal door is removed. Fewer partitions replace the small-room maze.
Upstairs remains within the higher roof strips, with lounge/balcony access,
landing, bedroom and en-suite bathroom. Total is 11 rooms / 287 m².

A compact return stair replaces the long flight: two parallel 1.2 m flights,
3 m run each, 2 m rise per flight, 1.2 m turning landing. Both foot and top
face the front circulation space. Shaft subtraction includes the turn and
individual guard footprints; the upper exit meets physical floor without a
12 cm overcut. Native walk surfaces include both ramps and the shared turn.

60 tests, Ruff, JavaScript syntax checks, six native resource readbacks and
152 adapted-Detour route controls pass. Controls include both directions/load
orders and locked front/rear/garage entries. The smaller control count reflects
fewer rooms/probes. Runtime behaviour is unverified for this revision.

Floor plan: `surveys/rancho-residential-house-plan.png`; measurements and source
pins: `surveys/rancho-residential-house-plan.json`. Five new screenshots and
native shutter template/appearance evidence are in
`generated/residential-house-plan/evidence`.

Relaunch with a city test save. As V, inspect the shutter's entire width and
motion, garage floor/threshold/internal steps, rear entry route and return
stair turn/headroom/upper exit. Then NPC Street approach ↔ Garage workshop,
Rear vestibule, Upstairs bedroom and Balcony front. Foot/top probes isolate
the stairs; observe both directions and physical door avoidance.

The Building Lab server was restarted after an old process rejected 3 m runs
using the former 6..15 m straight-flight rule. GET house and POST compile both
return HTTP 200 with the return stair and one connected island. Refresh the
browser to load the updated return-stair plan drawing and measured annexes.

Editor visual follow-up: ground and upper floors were opened in the live
browser after reload. Measured shell ceilings now follow the Roof toggle;
plan lines show annex walls and surveyed device openings. Ground room count
includes garage/rear entry (seven), and the stair hint describes the actual
two-flight return form. Screenshot:
`generated/residential-house-plan/evidence/editor-ground.png`.
These editor-only corrections require a browser refresh and do not rebuild
the installed game package. JavaScript syntax checks passed. The available
runtime report is dated 12:34:58 UTC, before the current install; its old NPC
pass is historical evidence only. This revision still needs the live shutter,
return stair, room circulation and balcony checks above.


## Corner stair and expanded garage — previous installed test

Candidate `building-lab-test-779affa2310c`, installed 2026-10-26 14:58 UTC
with the game closed. Project: `generated/residential-house-corner-stair`.
Receipt and prior payloads:
`generated/runtime-installs/20261026-145855-house-corner-stair/installation.json`.
All four installed payloads match the verified WolvenKit package.

The single 6 m stair runs along the garage wall inside Entrance/Dining, with
an enclosed ground-floor surround and an upper landing in the lounge. A clear
corridor keeps the balcony route. The garage gains a 1.2 × 6 m side bay up to
the stair end; its original rear notch remains. The old utility partition is
removed and the remaining 1.8 × 6 m joins the living room. Both rear returns
are closed. The internal garage door is on the new side wall, with a 0.35 m
step-up into the living extension, clear of the stair foot.

The garage frame is scaled through its mesh component, the moving panel through
a mod-owned skeleton root, and its player blocker through matching dimensions.
Skinned components do not support `visualScale`; entity node scale alone did
not resize the previous game assembly. Native readback checks all three.
Wall-body facing offsets now use the measured 15 cm depth. Window cuts include
the full frame and have inner reveals. Different ceiling heights meet with
bulkheads. Rear and balcony hinged doors reserve their open leaf footprints.

61 tests, Ruff, JavaScript syntax, seven native resource readbacks, verified
archive extraction, and 160 bidirectional unlocked/sealed Detour controls pass.
Evidence and editor screenshots: `generated/residential-house-corner-stair/evidence`.
Survey: `surveys/rancho-residential-house-corner-stair.json`.

Live test: V through front/rear, garage shutter, new garage side door/steps,
corner stair both ways and balcony. Then repeat with an NPC and inspect open
leaf avoidance, shutter motion, collision, headroom, joins and window reveals.
This revision has no live pass. Terrain grass in the garage is still a follow-up;
no terrain foliage mask was modified.


## Open plan and right return stair — previous installed test

Candidate `building-lab-test-0fc96f67909d`, installed 2026-10-26 15:57 UTC
with Cyberpunk closed. Project: `generated/residential-house-open-plan`.
Source: `buildings/rancho-open-plan-right-stair.building.json`.
Receipt and rollback payloads:
`generated/runtime-installs/20261026-155742-house-open-plan/installation.json`.
All four installed files match the verified WolvenKit package. The previous
runtime report was archived with the rollback files; this candidate has no live
result yet.

Both floors preserve the user's open partitions. A return stair occupies the
right wing within the existing full upper-storey footprint: two 1.2 m flights,
3.2 m runs, a 1.2 m turning landing and a 2.55 m overall width. The upper exit
joins the open upper floor. Ground entrance circulation remains clear.
Garage east wall moves to x=-3 to align with its original bottom corner;
the side extension/notch is removed. Its internal doorway remains on the
north/back wall near the west end, with the 0.35 m step-up repositioned to
match. The measured liner now has the same opening as the visible grid bay.
The garage's former side-door device is absent.

61 Python tests, four wall-control JavaScript tests, seven native resource
readbacks, WolvenKit archive/ZIP hash verification and 160 native Detour route
controls pass. Controls cover both directions/load orders and unlocked/sealed
external doors. Offline navigation is one connected island. Evidence:
`generated/residential-house-open-plan/evidence/route-verification.json`.
Editor ground/upper screenshots and the pre-edit user layout are retained in
`generated/right-stair-design`.

Relaunch with the existing city test save and revisit the house. As V, walk
front entry -> right stair -> upper landing -> balcony, then reverse. Check
the turning landing, headroom, upper-floor edge guards and ceiling cutout.
Walk garage shutter -> back-wall doorway/steps -> main house and rear porch.
Inspect the moved garage wall's corners and both sides of every threshold.
Then repeat with the Building Lab NPC, including **right-return stairs foot**
and **right-return stairs top** where listed by the test overlay.

Known from the previous live screenshots: the garage moving panel remained
smaller than its scaled frame, despite successful skeleton readback. This
candidate retains that assembly; it does not claim a shutter fix. Ceiling
joins, roof visibility, terrain grass and all new physical stair clearances
also require live inspection before rooms are added.


## Open plan with fitted garage surround — previous installed test

Candidate `building-lab-test-3e19a079c292`, installed 2026-10-26 16:25 UTC
with the game closed. Project: `generated/residential-house-open-plan-surround`.
Receipt/rollback files:
`generated/runtime-installs/20261026-162541-house-open-plan-surround/installation.json`.
All four installed hashes match the verified WolvenKit package.

The user's working native garage door is preserved. Its frame is now native
size and the surrounding wall aperture is 2.9 m wide by 2.24 m high, centred
on the stock device. The opening begins at the garage floor Z=-0.35;
the device retains Z=-0.605653763. This fits inside the measured stock panel
X=-1.50446..1.49186, Z=-0.000086..2.65950 and the stock frame bounds.
The wall infill has both decorated faces. No custom garage mesh, skeleton,
animation or component size overrides are packaged. Earlier mesh/animation
experiments were discarded before this build; none were installed.

Ceiling strips close the rear vestibule's lower 2.7 m ceiling against the
main 3.5 m ceiling on both its north and east joins. They cover partial bays,
meet existing walls without duplicate facings, and preserve the open route
below. The editor/server also use this correction.

63 Python tests, four wall-control JavaScript tests, Ruff, six native resource
readbacks, 160 unlocked/sealed route controls and package extraction/ZIP/hash
verification pass. Evidence: `generated/residential-house-open-plan-surround/evidence`.
This is package/offline verification; this candidate has no in-game pass yet.

Relaunch with the existing city test save. First inspect the closed garage
surround from inside and outside, then open/close it and walk/drive through.
Inspect the rear ceiling joins from below. Walk the right turning stair both
ways and check the turn, headroom, upper exit and guards. Follow the open
upper floor to the balcony and back. Repeat the garage/stair/balcony routes
with the NPC helper after V's physical walk-through.


## Windows, stair enclosure and wall joins — previous installed test

Candidate `building-lab-test-ff082e3f926b`, installed 2026-10-26 16:56 UTC
with the game closed. Project: `generated/residential-house-join-fixes`.
Receipt and rollback payloads:
`generated/runtime-installs/20261026-165642-house-join-fixes/installation.json`.
All four installed hashes match the verified WolvenKit package.

This addresses the seven screenshot reports from the prior build:

1. Ground window: matching complete Rancho window module faces inside with
   the plaster finish; the extra generated reveals/double trim are removed.
2. Stair gaps: right flight ends at the outside wall's inner face; the stair
   surround meets the back wall and continuous upper guards.
3. Ground wall joins: measured shell walls now use the same 15 cm body depth
   as regular walls. Resized wall UVs retain floor-relative paint height.
4. Garage: a native automatic hinged_h door is restored at the back-wall
   opening, with its own gated off-mesh connection. The previous ungated
   landing link is removed; locking the door blocks the indoor route.
5. Stair walls: the exposed stepped outer guard becomes a full enclosure;
   guard faces use plaster wall geometry instead of stretched slab sides.
6. Upper window: matching native inner frame replaces added reveals. The
   shorter module gets infill above it; its paint uses the same UV correction.
7. Upper joins: aligned finishes/depths and removal of the added shortened
   roof-support module eliminate the protruding beam fragment.

UV variants alter texture coordinates only. Quantized positions, topology,
materials and source buffers are retained except for the UV streams. Both
texture coordinate channels are corrected using face derivatives, including
rotated mask islands. Export owns the 18 derived mesh variants under the
candidate's source/raw and source/archive trees. The schematic editor uses
neutral materials and cannot prove the final in-game paint appearance.

65 Python tests, Ruff, 24 native resource readbacks, package extraction/ZIP
hash checks and 160 Detour route controls pass. Offline surfaces form one
island. Prior screenshots are retained in this project's evidence/feedback.
There is no live pass for this candidate yet.

Relaunch the existing city test save. Inspect both window frames and paint
bands, the ground rear-entry corner and upstairs balcony-passage join. Walk
through the internal garage door in both directions. Walk both stair flights,
the turn and upper exit; inspect enclosure seams from below and upstairs.
Confirm the stock external garage shutter remains functional. Then repeat
with the NPC helper, including a locked internal-garage-door check.


## Rear ceiling corner — previous installed test

Candidate uilding-lab-test-0ff23881fba9, installed 2026-10-26 17:11 UTC with the game closed.
Project: generated/residential-house-ceiling-corner. Receipt and rollback:
generated/runtime-installs/20261026-171155-house-ceiling-corner/installation.json.

User reports the preceding build is generally good, with one remaining vertical
slit beside the rear vestibule bulkhead. Perpendicular wall thickness was being
subtracted from the infill span, leaving the opposite corner face uncovered.
Only parallel walls now suppress infill; perpendicular corners overlap.
The 2.7 m ceiling remains: surveyed retained roof placement 125 reaches local
Z 3.127 over the vestibule, below the proposed 3.5 m ceiling.

65 Python tests, Ruff, 24 native readbacks, 160 Detour route controls and package
extraction/ZIP hashes pass. All four installed payload hashes match. No live
pass yet: relaunch the existing city test save and inspect both faces of the
rear ceiling corner, including the narrow slit shown in the latest screenshots.


## Garage shutter closing — previous installed test

Candidate `building-lab-test-aadd1e1b6ed1`, installed 2026-10-26 17:20 UTC,
game closed. Project: `generated/residential-house-shutter-close`.
Rollback receipt: `generated/runtime-installs/20261026-172022-house-shutter-close/installation.json`.

User confirms shutter opens on approach and stays open after walking away.
Exported DoorSetup already enables automatic closing. Saved PS overriding
this is a hypothesis, not a confirmed runtime cause. The exact garage door
opts into one restoration per streamed entity via the existing CET helper:
SetCloseItself(true), then native DoorTriggerDelayedEvent if already open.
The native handler checks nearby authorized occupants before closing.
Later intentional quickhacks on that streamed instance are left alone.
No global door changes, force-close loop or animation replacement.

A state-change diagnostic `garage-door-report.json` in the installed CET mod
folder captures the original auto-close flag, restored flag, open/busy/power
state and trigger occupancy. It does not count as a gameplay pass.
66 Python/Lua tests, Ruff, 24 native readbacks, 160 offline Detour controls,
package extraction/ZIP hashes and all four installed hashes pass.

Relaunch the city test save, approach the garage shutter, then walk at least
6 metres away and wait. Repeat from inside and outside; verify it stays open
with V or the NPC in the doorway. If it stays open, inspect the diagnostic
record before changing further settings. Root cause and live cycle unverified.


## Stair/bulkhead bridge — current installed test

Candidate `building-lab-test-2feba2564432`, installed 2026-10-26 17:28 UTC
with game closed. Project: `generated/residential-house-stair-bulkhead-bridge`.
Rollback: `generated/runtime-installs/20261026-172831-house-stair-bulkhead-bridge/installation.json`.

Two new live screenshots show the remaining slit from both sides. The prior
perpendicular-wall subtraction fix did not close the offset between bulkhead
ending x6 and stair enclosure beginning x6.18 (outer edge x6.3). Add a raised
double-sided liner from [6,-9,2.7] to [6.3,-9,2.7], height .9. It meets both
wall volumes above the lower ceiling, without closing the passage below.
Shell liner validation now permits short raised bulkheads (minimum .1 m).
Regression probes both faces across x5.99..6.29 at three visible heights.

67 Python/Lua tests, Ruff, 24 native readbacks, 160 offline Detour controls,
package extraction/ZIP hashes and all four installed hashes pass. One nav
island remains. Live gap closure still needs verification after relaunch.
Latest screenshots and previous shutter diagnostic are in evidence/feedback.
The latter records open=false, auto_close=true, trigger_occupants=0 at
17:23:19 UTC; it is a state observation, not proof of a full closing cycle.

Relaunch the city test save and inspect the same bulkhead corner from both
sides, including the lower lip and ceiling junction. Walk beneath it and
through both stair flights; check that the infill has no exposed corner slit.


## AKPP Logistics shell starter — editor only

`buildings/akpp-logistics-open-shell.building.json` is loaded in Building Lab.
One 6 by 6 m ground-floor room; twelve pinned retained-shell reference modules.
Import specification: `surveys/akpp-logistics-shell-import.json`.
Site/door/rear-wall evidence: `surveys/akpp-logistics-site.json`.
Verification and editor screenshot: `generated/akpp-shell-import`.

Ru Lai's back wall matches the retained west boundary. No Ru Lai, Rancho,
collision or game installation changes. All installed payloads still match
`building-lab-test-2feba2564432`. 69 tests, Ruff, exact imported world pivots,
reference omission from native nodes and browser save/reload checks pass.
This is a design starting point, not a playable entrance or complete interior.


### AKPP entrance authored

The same saved starter now contains a manual native `hinged_e` door in the
surveyed recess. Its appearance uses the same `door_swinging_e` leaf as the
static door in the screenshot. World root compensates the native component's
-1311/131072 m Z offset so the closed leaf matches the surveyed position.

Only static visual placements 4738/4739 and collision actors 3579:48 and
3526:22 are selected for replacement. Ru Lai's wall 3536:118 remains. These
patches are authored only; no AKPP package is installed. The former starter
had zero active removals; this revision carries two source-pinned sectors.
70 Python/Lua tests, Ruff and three WolvenKit/native readbacks pass. Browser
save verified; screenshot `generated/akpp-shell-import/evidence/editor-entrance.png`.
Manual door mode means interact to open. Live clearance/occlusion and exterior
navigation remain unverified while the game is open.


## AKPP entrance — installed alongside Rancho

Candidate `building-lab-2d171426742a`, installed 2026-10-26 18:12 UTC with the
game closed. Unique archive/registration `Ghostline_AKPPLogistics` contains
only the three AKPP native resources and its two source-pinned sector patches.
Receipt: `generated/runtime-installs/20261026-181215-akpp-entrance/installation.json`.
Both installed hashes match the verified WolvenKit package. The four installed
Rancho payloads remain byte-identical and have preserved rollback copies.

71 Python/Lua tests, Ruff, three native readbacks, archive extraction and ZIP
hash checks pass. No live pass yet. Relaunch the existing city save at AKPP,
interact with the hinged door, walk inside, then close/open it from both sides.
Inspect the threshold, casing, ceiling and preserved Ru Lai rear wall. Check
for invisible collision or disappearing geometry after walking inside and
turning around. This first room is unfurnished and does not export NPC nav.


### AKPP recessed entrance backing — installed

Live feedback confirmed that the hinged door opens, but the original shop
facade has a sealed recess panel behind it. Candidate `building-lab-0eb1d11cc9cb`
replaces only facade placement 4362 with `mod/building_lab/akpp-shop-open.mesh`.
The doorway portion of that panel is opened at all three mesh LODs; adjacent
shutter backing, facade details and Ru Lai rear wall 3536:118 are retained.
The original facade collision actor 3581:121 is replaced by six measured boxes
around the opening. This is an instance-scoped replacement, not a base mesh override.

Installed 2026-10-26 18:39 UTC while the game was closed. Receipt:
`generated/runtime-installs/20261026-183907-akpp-recess-opening/installation.json`.
72 tests, Ruff, four native readbacks, archive extraction/ZIP verification and
installed hashes pass. All four Rancho payload hashes remain unchanged.
Evidence: `generated/akpp-recess-opening/evidence`; verification records live
runtime testing as pending. Door selection in the plan now works above shell
footprints, allowing the entrance's initial state to be edited.

Relaunch the city save, open the AKPP door and walk fully through the recess
into the room. Repeat from inside, close/reopen the door, and check the adjacent
shutter and Ru Lai boundary. Walk away and return to check distant LODs and
culling, then save/reload. No NPC navigation is exported.


### AKPP interior lining and camera-dependent visibility — installed

Candidate `building-lab-b497ea2279bc`, installed 2026-10-26 19:04 UTC with
Cyberpunk closed. Receipt:
`generated/runtime-installs/20261026-190429-akpp-interior-repair/installation.json`.
User confirmed entry after the recess cut, but reported exposed facade backs,
entrance gaps and large camera-dependent disappearance.

Six double-sided common-wall liners now cover the retained exterior backs and
form entrance returns. The measured common wall contract normalizes its 5 mm
end lips and 3.8 m height. The opening remains 1.82 m wide and 2.55 m high.
Occluder group 2521 in `exterior_-9_10_0_1` contains a ground strip crossing
AKPP's new walkable footprint and an upper AKPP volume. Both are removed via
ArchiveXL's whole-group selection; the adjacent Ru Lai group 2518 is retained,
as are Ru Lai's visual/collision boundary nodes. Matrix/source evidence is in
`surveys/akpp-logistics-occlusion.json`. This is a targeted candidate, not a
recorded live occlusion pass.

73 tests, Ruff, four native readbacks, package extraction/ZIP checks and
installed hashes pass. Door-height clearance, facade/header coverage and three
interior-to-entrance route controls pass. All four Rancho payloads are unchanged.
Offline nav has three islands after lining: the usable interior/entrance and
inaccessible strips behind the lining. No native NPC navigation is exported.
Evidence and the editor preview: `generated/akpp-interior-repair/evidence`.

Relaunch the city save at AKPP. Walk the full room perimeter and through the
door in both directions, turning the camera at the positions where the city
previously vanished. Check the lined advert wall, ceiling band, both jambs and
return-wall junctions. Approach from the street, walk away/return, then save
and reload. Verify Ru Lai remains intact. Report any remaining camera-position
failure with the player's XYZ and facing direction.


### AKPP casing seams and original door sticker — installed

Candidate `building-lab-0154671918db`, installed 2026-10-26 19:13 UTC while
Cyberpunk was closed. Receipt:
`generated/runtime-installs/20261026-191339-akpp-casing-seams/installation.json`.
The user accepted the small office footprint and previous lining/occlusion
repair, then reported an inside-only jamb slit, exposed yellow return and a
floating Moon Explorer sticker when the door opens.

The lining aperture is now 1.40 m wide by 2.48 m high, overlapping the fixed
1.50 m casing. Return walls stop at local X=5.075, behind the moving leaf's
closed rear surface and within the casing's depth. Original static sticker
placement 4741 is removed from its pinned source sector. Nearby electronics
stickers remain. Evidence: `generated/akpp-casing-seams/evidence`.

73 tests, Ruff, four native readbacks, package extraction/ZIP verification and
installed hashes pass. Rancho payloads remain unchanged. Live seam closure,
yellow coverage and door swing clearance still need verification. Relaunch the
city save at AKPP, inspect both jambs from inside and outside, then open/close
and walk through the door from both directions. Confirm no sticker floats at
the old closed-door plane. This build does not add office furnishings.


### AKPP retained sidewalk overlap — installed

Candidate `building-lab-49f0a2bdff75`, installed 2026-10-26 19:19 UTC while
Cyberpunk was closed. Receipt:
`generated/runtime-installs/20261026-191957-akpp-floor/installation.json`.
Includes the preceding casing-seam and static-sticker fixes.

Inspector identified sidewalk placement 2582, render instance 5 of 6, in
`exterior_-5_5_0_2`. Its measured transformed bounds cross the office south edge
and extend outside: room-local Y=-2.516..1.171, highest Z=+0.030605 m. Removing
that instance would also remove exterior pavement. No sidewalk node, mesh or
collision is patched. An inset tile cap at X=.43..3.93, Y=.45..5.55, top Z=.05
covers its intersection inside the lined room. Added floor collision matches
the cap; a 5 cm step remains behind the entrance recess, clear of door swing.
Walkable plinth caps must sit on an existing room floor, remain within it and
be at most 20 cm high. Nonwalkable plinth behavior is unchanged.

74 tests, Ruff, four native readbacks, archive extraction/ZIP and installed
hash checks pass. Rancho hashes remain unchanged. Offline nav retains the
underlying room plane within 5 cm; native NPC navigation is still disabled.
Evidence: `generated/akpp-floor/evidence`, measurements and source pin in
`generated/akpp-floor/verification.json`. Live results remain pending.

Relaunch the AKPP city save and check the former raised sidewalk strip across
the office floor. Walk the small entry step in both directions, open/close the
door, inspect inside jambs/yellow coverage and confirm no floating sticker.
Check exterior sidewalk continuity on the street side as well.

### AKPP quest workstation — installed

Candidate `building-lab-57414c8c208e`, installed 2026-10-26 20:06 UTC while
Cyberpunk was closed. Receipt:
`generated/runtime-installs/20261026-200639-akpp-office-workstation-final/installation.json`.

Adds an office desk, chair, native infinite seated workspot and generic worker
(`Character.WorkerSpecialistMale`), plus a native interactive computer. The
computer's final height clears the desktop and its screen faces the chair.
The worker can be replaced later with the planned office manager. The editor
shows the worker record, appearance, activation flag and stable quest bindings.
Desk/chair moves carry their computer/workspot anchors with them.

Exports include `quest-bindings.json` and `quest-block-fragment.json`. The
terminal exposes a test file and the fact
`akpp_logistics_open_shell_office_file_read`; a regression test compiles the
existing `read_terminal_document` quest block against these bindings. This is
a quest-ready fixture, not a complete new story quest. See
`docs/authoring/building-workstations.md` for ownership and lifecycle details.

78 building tests, Ruff, eight native resource readbacks, archive/ZIP
verification and installed hashes pass. Rancho's four payload hashes remain
unchanged. Retained street geometry and the Ru Lai boundary are preserved.
Editor proof: `generated/akpp-office-workstation-final/evidence/editor-workstation.png`.

Live results are pending. Relaunch and enter AKPP; check that one worker sits
correctly at the desk. Test the computer and read **Office workstation test**,
then verify its read fact. Leave/return and save/load to check persistence and
duplication. Check entrance clearance and the previous floor/jamb repairs.
Native NPC walking/navigation has not been added.

### AKPP workstation streaming repair — installed

The first workstation playtest showed a reversed chair, no computer and no
NPC. Screenshot supplied by the user: `codex-clipboard-49f61981-122e-4a22-a0b1-e113c5a1cbf0.png`.
Inspection found the fixture sector was `Quest`, level 255, while its block
descriptor was `Quest`, level 0 with a nonzero prefab activation gate. No quest
in this standalone package activates that prefab. Architecture already used
normal Exterior streaming and appeared correctly.

Candidate `building-lab-777aa7c9e429` changes fixture sector/descriptor to
`Exterior`, level 0, with a zero prefab gate and a region enclosing all fixture
placements plus 80 m padding. The community registry remains AlwaysLoaded.
Chair mesh yaw is now 0 instead of 180; actor yaw offset changes to 0 so the
seated workspot keeps facing the desk. Stable NodeRefs and terminal fact remain.
The terminal and community registry payload are otherwise unchanged.

Installed 2026-10-26 20:17 UTC while Cyberpunk was closed. Receipt:
`generated/runtime-installs/20261026-201751-akpp-office-streaming-repair/installation.json`.
79 tests, Ruff, eight native readbacks including streaming category/level/gate,
archive/ZIP checks and installed hashes pass. Rancho's four payload hashes
remain unchanged, and prior AKPP shell/floor repairs are retained.

Live validation remains pending: relaunch the AKPP city save, check chair facing,
one seated worker and the computer. Read **Office workstation test**, then check
the read fact. Leave/return and save/load to check persistence/duplication.

### AKPP furnished logistics office — installed

The user accepted the streaming repair; their screenshot shows the computer and
one generic worker seated at the workstation. Terminal interaction, read fact
and persistence were not separately confirmed. They requested the workstation
on the left wall as seen entering, chair backed toward the wall and desk in
front, and authorized free choice of further decoration.

Candidate `building-lab-f19610ee28f3`, installed 2026-10-26 20:31 UTC with the
game closed. Receipt:
`generated/runtime-installs/20261026-203143-akpp-office-decor/installation.json`.

Workstation moved to local south wall: chair [2.1,1.05,.05], desk [2.1,2,.05].
Facing and relative computer/workspot transforms remain as accepted. Desk
collision moves with this fixture update. Added two tall filing cabinets along
the back/west wall, one low cabinet on the north wall, three closed parcel boxes
(two floor boxes and one stacked), paperwork and a black mug on the desktop.
New prop meshes are measured/hash-pinned in the supplemental prop catalogue.
Cabinet/parcel collision uses reviewed solid bounds; desktop clutter has no
added collision. Nothing is added to the entrance recess or door swing route.

79 tests, Ruff, eight native readbacks, archive/ZIP and installed hash checks
pass. Route test endpoint moves from [3,5,0] (now occupied by the low filing
cabinet) to [3,4,0] in the clear aisle. The three existing approach-route checks
still pass. Retained street, Ru Lai, shell repairs and four Rancho payload
hashes are preserved. Editor evidence:
`generated/akpp-office-decor/evidence/editor-office-decor.png`.

Live placement check pending: relaunch AKPP, inspect moved worker/chair/computer,
cabinet fronts, parcel stack and desktop clutter. Walk the clear central aisle
and verify door clearance. Existing terminal test-file/read-fact and save/load
checks remain relevant; this change adds no new quest behavior.


### AKPP cabinet facing correction — installed

Candidate `building-lab-f99672768181`, installed 2026-10-26 with game closed.
Receipt: `generated/runtime-installs/20261026-212316-akpp-cabinet-facing-fixed/installation.json`.
Mesh geometry inspection confirms drawers face native +Y. Flipped both west
cabinets from yaw 90 to -90 and the north low cabinet from 0 to 180, so all
fronts face into the office. Updated matching collision rotations in both the
building layout and shell import spec. Compared against the previous frozen
layout: only these six yaw values changed; positions and footprints are equal.
Eight native resource readbacks, WolvenKit archive/ZIP verification and installed
hash checks pass; all four Rancho payload hashes preserved. Live cabinet-facing
check remains pending. Existing 79-test result belongs to the previous candidate;
this rotation-only update was verified through export and exact layout comparison.


### Allen Street residential retrofit — first walkthrough installed

Exterior survey and independent interior draft are saved as
`buildings/kabuki-allen-residential-shell.building.json` and
`buildings/allen-street-residential-retrofit.building.json`. See
[survey and layout limits](surveys/allen-street-residential-retrofit.md).
The latter has a security lobby, two offset return stairs and two upper delivery
landings. Both quest destinations pass offline route checks on one connected
island. Candidate `building-lab-c006995da268` is installed separately as
`Ghostline_AllenResidential`. The decorative door and two exact proxies are
replaced by a matching interactive double door. Individual entrance and solid
upper-storey collision actors are replaced, with peripheral/roof support
retained. The exact building occluder group is removed; facade and pavement
remain intact. Forty-two render-aperture rays are clear.

Receipt: `generated/runtime-installs/20261026-225613-allen-first-walk/installation.json`.
Three native readbacks, archive extraction/hash verification and installed
hashes pass. All six AKPP/Rancho files retain their prior hashes. No recipient
actors or quest progression are included. Gameplay remains untested; follow
the survey's entrance/stairs/return-route handoff before adding encounters.

Fixed repeated async mesh-load redraw subscriptions and reference material
allocation in the 3D viewer. All 12 frontend regression tests, strict TypeScript
and production build pass; all 83 Python building tests pass. A fresh browser
tab running the rebuilt frontend switches to the upper floor successfully.

First live feedback led to installed repair `building-lab-21e60bd0a457`:
closed ceiling backs and corner joints, joined stair enclosure/guard panels,
30 cm lower top ceiling under rooftop attachments, and five exact entrance
debris instance removals. 85 Python building tests and three native resource
readbacks pass; archive/install hashes are verified and AKPP/Rancho preserved.
Receipt: `generated/runtime-installs/20261026-231711-allen-seam-repair/installation.json`.
Live confirmation of those repairs remains pending.

Parcel-room follow-up `building-lab-aa87592cd5b5` is installed: removes only
static fuse box placement 2511 and its matched collision actor 3105:4. Other
31 actors, nearby boxes and cables are retained. Generated geometry/navigation
and all three native payload hashes match the prior candidate; archive/install
verification passes. Receipt:
`generated/runtime-installs/20261026-233224-allen-parcel-fusebox/installation.json`.
Live removal confirmation is pending.

Installed `building-lab-2607fcf86d4f` replaces the corner-column workaround with
measured wall snapping: 20 cm painted-face spacing, separate 23 cm collision
thickness, and 1 mm solid-panel end overlap. All 28 columns are removed. 117
one-sided triangle join rays and 86 Python building tests pass; native/package/
install verification passes. Receipt:
`generated/runtime-installs/20261026-233756-allen-wall-snap/installation.json`.
Existing precise vanilla patches and AKPP/Rancho are preserved. Live join check
is pending.

Stair visibility candidate `building-lab-7235e5877295` is installed. Removes one
additional upper-storey occluder: `exterior_-3_3_0_3`, placement 905. Fresh
resource/box bounds place both user-captured missing wall/ceiling collision
points inside this volume. Geometry and all three native resource hashes match
the snapping candidate; exact selection, archive/install hashes and AKPP/Rancho
preservation are verified. Receipt:
`generated/runtime-installs/20261026-234414-allen-stair-visibility/installation.json`.
Live visibility retest remains pending.

Apartment stair-wall fit `building-lab-627d0f1ee2f0` is installed. Only the
second return stair's X coordinate changes by -5 cm, bringing its outer
enclosure 3 cm behind the apartment's painted wall. Both offline delivery
routes and 117 corner rays pass; native readback/archive/install verification
passes. All prior vanilla patches and AKPP/Rancho are preserved. Receipt:
`generated/runtime-installs/20261026-234714-allen-stair-wall-fit/installation.json`.
Live wall fit and shifted stair clearance require retesting.


Top-floor stair join candidate `building-lab-80bf2e2b5911` is installed.
The existing right/rear room walls now provide the second stair enclosure;
duplicate projecting guards are removed and the rear join mates with 2 cm
overlap. Both offline delivery routes and all 86 Python building tests pass;
native/package/install checks pass. Prior vanilla patches and AKPP/Rancho
are preserved. Receipt:
`generated/runtime-installs/20261026-235401-allen-stair-wall-join/installation.json`.
Live top-landing, apartment-wall and rear-join checks remain pending.


Decoration candidate `building-lab-3a1d082b6a9b` is verified and staged, **not
installed** while the user tests the stair build. Includes 68 vanilla mesh
placements and 15 explicit warm native lights: lobby seating/plants, shallow
wall accents, static cameras/fire equipment/intercom, floor markers and
101/102/201/202 plaques. Existing room/stair geometry and precise vanilla
patches are retained. All 88 Python building tests, three native resource
readbacks, archive extraction and package hashes pass; both delivery routes
remain reachable offline. Current Allen and all AKPP/Rancho installed hashes
are unchanged. Final verification:
`generated/allen-decoration-pass-1/project/generated/packages-final/building-lab-3a1d082b6a9b/verification.json`
(project-relative). See the decoration plan for placement evidence and live
material/exposure checks. The earlier package in `packages/` is superseded.


Installed seam repair `building-lab-9170b9b1f3ef` fits the 3.8 m common walls
to the next 4 m storey where a solid wall continues above. Render and collision
share a 2 mm mating overlap, closing the exposed stair-side band. All 89 Python
tests and 60 native seam rays pass; native/package/install verification passes.
Receipt: `generated/runtime-installs/20261027-001226-allen-stacked-wall-join/installation.json`.
Decorations remain excluded; their old staged package is superseded pending
rebuild with this join repair. Live seam confirmation is pending.


Installed `building-lab-3690bbde4a02` closes the recessed apartment-landing
returns on both floors using six scoped solid wall-end extensions. Both
painted facings and collision meet; native corner profiles differ by <1 mm.
All 90 Python tests, 117 corner rays and 60 stacked seam rays pass; both
routes remain reachable. Native/package/install checks pass and AKPP/Rancho
are preserved. Receipt:
`generated/runtime-installs/20261027-001824-allen-apartment-corners/installation.json`.
Decorations remain on hold; live corner acceptance is pending.


Installed `building-lab-dacf71c3d925` fits the first-floor stair joins A/B/C:
the lower return stair meets the adjacent enclosure with 4 cm overlap and
uses the back/side room walls instead of duplicate upper guards. Both stair
routes pass offline, all 91 building tests pass, and native/package/install
checks pass. Prior patches and AKPP/Rancho are preserved. Receipt:
`generated/runtime-installs/20261027-002410-allen-stair-abc/installation.json`.
Decorations remain excluded; live stair-clearance acceptance is pending.


Installed `building-lab-ba617ae13528` trims the four pavement slab inner edges
back behind the lobby/threshold line, preserving their outer edges and tilts.
Only source mesh2950 instances0–3 and collision3184 actors17/18/20/19 are
replaced; the other124 collision actors remain. Full-rotation replacement
collision matches the render boxes. All93 building tests, both offline routes,
native/package/install verification pass. Receipt:
`generated/runtime-installs/20261027-003155-allen-lobby-pavement/installation.json`.
Decorations remain excluded; live lobby/threshold/street walk retest is pending.


Installed `building-lab-5d267160796e` closes return-stair outer corner squares
and brings the descending ceiling edge beneath the guard footprint. No
layout or door positions change. All93 building tests, native geometry probes,
both delivery routes and package/install checks pass. Receipt:
`generated/runtime-installs/20261027-004657-allen-stair-corners/installation.json`.
Prior repairs and AKPP/Rancho retained; decorations remain excluded. Live
corner/headroom checks are pending.


### Stair backs: use the existing grey room walls (2026-10-27)

Installed `building-lab-5ca1bfd10661` after verifying the game was closed.
Removed both `guard:stairs-*:back` concrete panels and their colliders when
`wall_back` selects a room-provided rear wall. Both turning landings now have
1.6 m depth, reaching local Y=3.2 instead of leaving a 10 cm strip before the
grey wall. Stair runs, exits, doors, previous corner joins and vanilla patch
selections are unchanged. The main decorated authoring layout also retains this
fit; decorations remain excluded from the installed geometry test package.

All 93 building tests pass, both delivery routes remain reachable, and native
mesh probes confirm 18 rear-wall sightlines and six supported landing-edge
points. Three serialized resources, WolvenKit extraction and installed hashes
verified; all six AKPP/Rancho payloads preserved. Gameplay acceptance pending.
Evidence: `generated/allen-stair-backs/fit-verification.json`.
Install receipt: `generated/runtime-installs/20261027-005055-allen-stair-backs/installation.json`.


### First apartment floor: continuous shared stair partition (2026-10-27)

Installed `building-lab-f7c5f529385e` while the game was closed. The lower stair's
upper-right guard and next stair's full-height left enclosure now share the
same local X=6.0..6.2 partition. The guard above Z=4 is omitted where the taller
enclosure supplies that wall; its slab band and the exposed 15 cm front tail
remain. This removes the projecting short wall/cap and the 8 cm change in face
position. Flight widths and authored layouts are unchanged. The generator
matches nearby enclosed Y-axis return stairs on adjacent storeys; standalone
stair sides retain their normal 12 cm walls.

Twenty native triangle probes confirm the continuous face across several
heights and positions; both delivery routes and all 93 building tests pass.
Three native resource readbacks, WolvenKit extraction and installed hashes
verified. Previous fixes retained, decorations excluded, six AKPP/Rancho files
preserved. Live stair-wall acceptance pending.
Proof: `generated/allen-shared-stair-wall/fit-verification.json`.
Receipt: `generated/runtime-installs/20261027-005336-allen-shared-stair-wall/installation.json`.


### Both stair shafts: slab-edge flicker and storey seams (2026-10-27)

Installed `building-lab-d7ce5db68282` with the game closed. Floor and ceiling cuts
now extend through the room-provided side-wall footprint, rather than stopping
at its painted face. This removes the thin internal strips whose vertical slab
lips coincided with grey wall faces at X=3.2 and X=8.8. Eighteen floor/ceiling/cap
pieces previously had triangles on those planes; none do after the change.
The change applies to both return flights, including the lower lobby flight.
Stacked grey wall faces meet exactly at the storey boundary, removing their
previous 2 mm vertical coplanar lap. No cover strips added.

Native wall-only probes checked 228 positions around both storey seams on the
left, right and back solid room walls, excluding the intentional hallway
passages. All were closed without relying on slab lips to hide a gap. Both
delivery routes, all 93 building tests, three native resource readbacks,
WolvenKit extraction and installed hashes pass. Layout, doors, vanilla patch
selections and six AKPP/Rancho payloads preserved. Decorations excluded.
Live flicker/seam acceptance still pending; geometry checks cannot establish
rendering behaviour in motion.
Proof: `generated/allen-stair-slab-seams/fit-verification.json`.
Receipt: `generated/runtime-installs/20261027-005749-allen-stair-slab-seams/installation.json`.


### Combined decorations and latest geometry test (2026-10-27)

Installed `building-lab-21e988389558` with the game closed, at the user's request
to include decorations in this test. This rebuild uses the current authoring
layout and generator; it preserves all geometry, door and retrofit selections
from `building-lab-d7ce5db68282`. Native instance comparison confirms all prior
geometry is unchanged; collision comparison ignores positional shell indexes
and confirms only three furniture/plant blockers were added.

Includes 68 vanilla modules and 15 warm native lights: ceiling practicals,
apartment/floor numbers, bench, plants, wall accents, four static cameras,
three extinguishers and a static parcel intercom. Both offline delivery routes
remain reachable in one navigation island. Prior 93 building tests passed for
this generator. Three native readbacks, WolvenKit extraction, package and
installed hashes verified; six AKPP/Rancho payloads preserved. Live materials,
lighting/exposure, label reading, circulation and stair flicker test pending.
Cameras/intercom are decorative; directory wording is still future work.
Proof and native geometry review: `generated/allen-decorated-current/`.
Receipt: `generated/runtime-installs/20261027-010005-allen-decorated-current/installation.json`.


### Top-floor passage strip and yard audio investigation (2026-10-27)

Installed `building-lab-91ebe95eaefa` with game closed. The previous wall-footprint
slab cut extended through a hallway passage past the end of the solid grey wall.
Now intersect the extra anti-flicker cut with actual solid room-wall footprints;
the original shaft remains cut, while the X8.8..9.0 floor strip at Y9..9.35
returns at the upper stair exit. Nine native downward probes changed from no
floor to Z8. Both delivery routes and all 93 building tests pass, including the
new passage-floor assertion. Layout, decorations, lights, doors and retrofit
selections unchanged. Native resources, WolvenKit extraction and install hashes
verified; six AKPP/Rancho files preserved. Live acceptance pending.
Proof: `generated/allen-floor-passage/fit-verification.json`.
Receipt: `generated/runtime-installs/20261027-011203-allen-floor-passage/installation.json`.

Yard voices: no audio/NPC edits made. Local modding node-type reference describes
`worldAmbientAreaNode` as controlling acoustic environment and interior muffling.
Vanilla research in `docs/authoring/buildings-and-interiors.md` records room-tone
areas and parameters, but explicitly says relocating generated acoustic data is
not established by moving its node. WolvenKit definitions show
`worldAcousticSectorNode.data` references `worldAcousticDataResource`, whose cells
carry deferred compiled buffers; `worldAmbientAreaNode` is a trigger-area subtype.
These establish an investigation path, not a verified selective voice-muffling
implementation. A local interior acoustic/ambient donor needs inspection and
live transition testing before an audio change; deleting the yard community or
globally reducing voices is outside this fix.


### First vanilla residential audio-area test (2026-10-27)

Installed `building-lab-be9d407396c0` with game closed, after capture ended.
Comparison: `surveys/allen-interior-audio-comparison.md`. Allen already requested
gameplay interior state, but lacked the donor's ambient-area setup. Three
`worldAmbientAreaNode` volumes now use the exact reviewed vanilla ground/upper
corridor settings: corridor metadata parent, priority 10, amb_interior 0.98/0.9,
medium-room reverb and warm room tone. Graph, outdoorness, NPCs, gameplay
restrictions, geometry, decorations, lighting, navigation and patches unchanged.

All 95 building tests pass. Three native resource readbacks verify audio event
names, parameters, reverb, notifier and outline. WolvenKit extraction and
installed hashes verified. Only Allen enabled; the post-capture six existing
archive-directory files, including disabled quest packages, retain their hashes.
Initial installer post-copy inventory comparison encountered filename case
normalisation on Windows; payload/preservation hashes had already passed. The
comparison was corrected to case-insensitive paths and the existing install
finalized without another copy. No other capture-disabled packages restored.
Live yard-dialogue muffling, room-tone/reverb and exit transition acceptance
pending. Receipt:
`generated/runtime-installs/20261027-093909-allen-interior-audio/installation.json`.


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
