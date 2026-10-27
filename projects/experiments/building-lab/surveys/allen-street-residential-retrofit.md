# Allen Street residential retrofit — interior draft

Continues the [exterior survey](kabuki-allen-residential.md). The `{AllenSt}`
street-sign entity in `exterior_-17_27_0_0`, placement 2192, establishes the sign
as a street label. It is not a building name.

Open **Allen Street · residential retrofit draft** in Building Lab. Source:
`../buildings/allen-street-residential-retrofit.building.json`. The original
shell survey remains a separate saved layout. First-walkthrough candidate
`building-lab-627d0f1ee2f0` is now installed as `Ghostline_AllenResidential`.

## Layout

| Floor | Authored spaces | Quest use |
| --- | --- | --- |
| Ground | Security lobby, desk/chair, utility/parcel room, stair hall | Entry and access-code encounter |
| First, +4 m | Stair hall, delivery landing, Adrian's apartment, neighbouring apartment | Delivery A |
| Second, +8 m | Stair hall, delivery landing, Niko's apartment, neighbouring apartment | Delivery C |

Two 1.2 m-wide return flights per stair rise 4 m via an intermediate landing.
The two storey connections use offset shafts rather than overlapping them.
Each return stair has a 4.5 m run and 1.5 m landings. The plan reserves a
continuous route from the entrance to both delivery rooms. Apartments are
provisional spaces; furnishing and recipient actors are not authored yet.

Interior extent is local X 3–18, Y 3–15. Rear Y >15 and the west/south strips
remain outside the new rooms. The new interior comprises 11 room/hall volumes
and 540 m² across three floors; this is authored area, not surveyed usable area.
The original decorative double door and its two exact proxies are replaced by
an interactive door with the same orange/purple appearance and transform. The
shop facade remains intact: 42 render-triangle rays across the entrance width
and height found no backing mesh blocking the aperture. An inset interior liner
fits the original ungridded doorway.

## Evidence and limits

The four primary fresh sectors contain two rear homeless workspots near world
`[-1080.13,1789.81,28.95]` and `[-1077.52,1790.09,28.95]`. Preserve these
activities and their approach; the rear-strip reservation is provisional until
their actual navigation and animation extents are checked.

Actor-pivot inventory found 11 collision actors inside the broad planned volume:
eight near the roof, the shop facade, an entrance candidate, and the previously
captured upper unit box. A pivot inventory does not detect mesh shapes whose
pivots lie outside the volume. Full report:
`../generated/allen-residential-survey/interior-collision-candidates.json`.

Important candidates:

- `exterior_-5_6_0_2`, placement 2722, actor 99: entrance collision near local
  `[17.80,9.44,0.028]`; removed individually for the new door.
- Same sector, placement 2722, actor 28: shop backing retained. Public pavement
  and the rest of its collision group are retained.
- Same sector, placement 2776, actor 104: unit half-extents scaled by
  `[8.97694,10.50757,2.00007]`, with shape offset Z=1. This solid fills the upper
  storey from world Z≈36.498 to 40.498. Only this actor is removed; authored
  peripheral boxes preserve its outside bounds around the interior, and a
  20 cm roof slab retains support at the top. The new interior supplies its own
  floor and wall collision. This corrects the earlier unscaled 2 m assessment.
- Same sector, placement 2128: all four occluder matrices belong to this
  building. That exact group is removed so the new interior can remain visible.

Offline compilation produces one connected navigation island and routes from
the inside entrance to both delivery rooms. This covers authored rooms, stairs
and desk collision only. It does not establish clearance through retained
vanilla collision, occluders, door proxies or live NPC navigation. Native
navigation export is disabled. Live collision and visibility remain untested.

## First walkthrough handoff

Installed 2026-10-26 with Cyberpunk closed. Receipt:
`../generated/runtime-installs/20261026-225613-allen-first-walk/installation.json`.
All three native resources passed readback and archive extraction/hash checks;
83 Python building tests and 12 frontend tests pass. The six installed AKPP and
Rancho files retain their previous hashes. Package integrity is verified;
gameplay is not. No delivery recipients or quest progression are installed.

Use an ordinary free-roam save at the surveyed Allen Street entrance, world
`[-1063.447,1782.145,28.415]`. No quest reset is required for this geometry test.
Restart the game after installation. Walk through the orange/purple double
door without FreeFly, climb both stairs and enter both upper delivery rooms,
then return to the street. Check floor joins, headroom, door opening/closing,
and visibility from each side. Walk around the exterior and rear strip to check
the retained pavement and ambient activity. Finally leave the area and return,
then save/load. Record any obstruction with an Inspector capture before adding
recipient encounters. Native NPC navigation and active vanilla quest ownership
still need separate validation before this becomes a quest location.

Optional manual CET shortcut is installed as `ghostline_allen_teleport`, sourced
from `tools/allen_teleport_cet/init.lua`. Open the CET overlay and use **Teleport
outside Allen Street** in **Ghostline - Allen Street teleport**. It targets the
public approach three metres east of the door and remembers one return position
for the current script session. A bindable **Allen Street: teleport outside
entrance** hotkey is also available. Restart or use CET's Reload all mods after
installing the helper. Lua syntax and installed/source hashes are verified;
the landing position still requires an in-game check.

## Preview stall correction

The viewer previously registered a redraw callback for every repeated instance
of a still-loading mesh. Subsequent rebuilds registered those callbacks again,
allowing callback growth during a large floor load. It now requests one refresh
per pending mesh, coalesces refreshes into one animation frame, and caches
reference materials instead of cloning them on every rebuild. Reference meshes
also no longer generate shadow maps. Four regression checks exercise repeated
instances, coalescing/latest floor, failure handling and material reuse.

The corrected app successfully switched from ground to the second upper floor
in browser verification. The prior stalled tab was left untouched; verification
used a fresh tab with the rebuilt frontend.

## First live feedback and seam repair

The user tested the first candidate and supplied seven captures, including
corner gaps, exposed stair panels, top-ceiling intrusions, an angle-dependent
view through the stairwell ceiling, and floating entrance debris. This confirms
the building loads in game; the screenshots do not establish every collision,
return-route or streaming test above.

Repair candidate `building-lab-21e60bd0a457` installed with Cyberpunk closed.
Receipt: `../generated/runtime-installs/20261026-231711-allen-seam-repair/installation.json`.
Previous Allen files were backed up; all six AKPP/Rancho hashes are unchanged.

- Add small overlapping closed columns at perpendicular wall joins, and close
  the open backs of ceiling slabs without filling the stair apertures.
- Add the missing lower right enclosure of each return stair. Extend the upper
  front guard across the centre partition so its end joins the landing guard.
- Lower the top ceiling from 3.7 m to 3.4 m above its floor. Measured transformed
  bounds of rooftop fuse-box attachments reach world Z≈40.113; the old ceiling
  was at Z≈40.115. The new underside is Z≈39.815. Roof equipment stays outside.
- Remove only destructible instances in `exterior_-17_27_0_0`: placement 1640
  instances 0/1/2 (spray cans), 1643 instance 0 (foam lid), and 1644 instance 0
  (drink carton). Mesh identities, source hash and instance counts are pinned.
  ArchiveXL supports these cooked-transform instance deletions; no shared mesh
  resource or entire street prop group is removed.

85 Python building tests pass, including pinned destructible-selection rejection,
ceiling caps and stair-guard joins. Three native resources passed readback and
archive extraction/hash verification. The final offline route remains one
connected island. These repairs still need a live retest: inspect the reported
corners, both stair approaches from several camera angles, top ceiling and the
entrance after restarting. A persisted destructible state in an existing save
may need an area unload/reload to clear; capture any remaining object before
expanding removal scope.

## Parcel-room fuse-box protrusion

The user's `Cyberpunk2077_y4qV0imf8Y.jpg` identifies collision sector
`exterior_-9_13_0_1`, placement 3105/definition 2670, actor 4 of 32. Its exact
world pivot matches static render placement 2511 in `exterior_-17_27_0_0`:
`attachments_fuse_box_g.mesh`, world `[-1063.14502,1776.74683,31.06833]`.
Measured transformed local bounds extend to X≈17.208, inside the parcel-room
wall. This is the rear of a vanilla decorative electrical box, not a generated
wall panel.

Candidate `building-lab-aa87592cd5b5` removes only that render placement and
collision actor 4. Nearby fuse box 2517, cabling and the other 31 collision
actors remain. No generated room geometry, collision or navigation changed;
all three native resource content hashes match the preceding candidate.
Selection evidence: `../generated/allen-parcel-fusebox/selection-verification.json`.

Installed with Cyberpunk closed, previous Allen files backed up, all six
AKPP/Rancho payload hashes preserved. Receipt:
`../generated/runtime-installs/20261026-233224-allen-parcel-fusebox/installation.json`.
Archive extraction and installed hashes pass. The earlier 85-test result belongs
to unchanged generator code; this selection-only change was checked through
source pinning, exact placement/actor comparison and native readback. Restart
and revisit the parcel room to confirm the protrusion has gone. Other reported
issues and decoration remain separate follow-ups.

## Wall snapping replaces the corner-column workaround

The user identified `corner:0:9:6` in the lobby and requested proper snapping
instead of sealing gaps with strips. All 28 added corner columns and their
colliders are removed. The common wall's actual main decorated triangles lie
at native Y=0.20 m with normal +Y; its full 0.23 m bounds include trim. The old
reverse-facing placement used those full bounds, leaving about 3 cm mismatch
at perpendicular/T joins. `wall_facing_depth: 0.20` now positions reverse
facings, while physical `wall_thickness: 0.23` stays separate. Solid common
wall ends overlap by 1 mm, closing exact-vertex quantization seams. Doorway
meshes and aperture dimensions are unchanged.

Candidate `building-lab-2607fcf86d4f` installed with Cyberpunk closed. Receipt:
`../generated/runtime-installs/20261026-233756-allen-wall-snap/installation.json`.
86 Python building tests pass; 117 one-sided native render-triangle rays across
non-passage room-corner joins find no gaps. Evidence:
`../generated/allen-wall-snap/join-verification.json`. No corner columns remain,
and offline navigation is one island. Three native readbacks, package extraction
and installed hashes pass; AKPP/Rancho payloads are preserved. The ArchiveXL
registration hash matches the previous candidate, retaining the precise vanilla
removals. Restart and check the lobby corner, parcel-room junction and upper
apartment corners from both sides; live material/join acceptance is pending.

## Stair visibility: additional upper-storey occluder

The user supplied `Cyberpunk2077_35npSMsgJb.jpg` and
`Cyberpunk2077_juom0rCui2.jpg`, identifying generated `wall:1:y:1:1:0` and
`tile:1:1:2:ceiling` collision while their render surfaces disappear at certain
angles. The user confirmed these were captured before the latest restart:
Inspector shows the earlier 844-node sector, while the snapping candidate has
760 nodes. Snapping was not assumed to resolve visibility.

A wider spatial search inspected 167 cached overlapping sectors (42 descriptor
sources were uncached). It found a second building-sized occluder in
`exterior_-3_3_0_3`, placement 905/definition 854, with 2094 placements. It is a
single `worldStaticOccluderMeshNode`, defaulting to
`engine\meshes\editor\box_occluder.w2mesh`. Fresh serialization verified the
sector and the default mesh's unit-box bounds. Node scale is approximately
20.661 × 15.485 × 7.584 m, centre
`[-1070.78137,1782.90991,36.52470]`, Z≈32.733–40.316. Both captured missing-piece
collision positions are inside this oriented volume. It is a strong explanation
for culling when looking up across the lobby ceiling into the upper storeys.
The earlier four-matrix group 2128 belongs to another sector and does not remove
this consolidated occluder.

Candidate `building-lab-7235e5877295` removes only placement 905 in that new
source-pinned sector. All geometry, collision, navigation and three native
resource hashes match the snapping candidate; previous exact patches remain.
Evidence: `../generated/allen-stair-visibility/selection-verification.json`.
Installed with Cyberpunk closed; previous Allen payloads backed up and all six
AKPP/Rancho hashes preserved. Receipt:
`../generated/runtime-installs/20261026-234414-allen-stair-visibility/installation.json`.
Native readback, archive extraction and installed hashes pass. The prior
86-test result belongs to unchanged generator code; the new selection is
verified independently against the fresh source. Restart and look up from
both flights/turning landing, rotating and moving through the previous failure
angles, then repeat from upstairs. Live culling correction remains unconfirmed.

## Apartment wall: return-stair enclosure overlap

The user's older-build captures `Cyberpunk2077_IxYu51iggf.jpg` and
`Cyberpunk2077_8LTv1pLok9.jpg` identify
`guard:stairs-1-2:enclosure:right` and `wall:1:y:3:1:0`. Checking the current
layout established that snapping alone did not clear it: the stair enclosure
occupied local X=8.90–9.02, crossing the apartment's corrected painted face X=9.

Only the second stair's authored X coordinate changes, 6.30 → 6.25 m. The
enclosure now ends at X=8.97, 3 cm behind the painted face. Steps, guards,
collision, floor/ceiling shaft cuts and navigation are derived from the same
stair transform. Neither the room wall nor its material is replaced. Both
delivery-room routes remain reachable on one offline island, and the 117
render-triangle corner checks still pass. Evidence:
`../generated/allen-stair-wall-fit/fit-verification.json` and
`../generated/allen-stair-wall-fit/join-verification.json`.

Candidate `building-lab-627d0f1ee2f0` installed with Cyberpunk closed; receipt:
`../generated/runtime-installs/20261026-234714-allen-stair-wall-fit/installation.json`.
The frozen preceding layout comparison permits only that one coordinate change.
Three native resource readbacks and archive/install hashes pass; ArchiveXL
registration is unchanged, preserving the latest occluder/fuse-box/debris
repairs. AKPP/Rancho payloads retain their hashes. Restart, inspect the apartment
wall and walk the shifted stair approaches/turning landing. Live fit and stair
clearance remain unconfirmed.


## Top-floor stair: use the existing enclosure walls

Older 844-node captures `Cyberpunk2077_G6VQnsNBRG.jpg`,
`Cyberpunk2077_wSrXTQkPTw.jpg` and `Cyberpunk2077_G9NeZV9k8O.jpg`
show the duplicate upper right stair guard projecting beyond the hallway corner
and through the apartment wall, plus a gap behind the staircase. The earlier
X inset alone did not resolve all three joins.

The second return stair retains X=6.25 and now uses Y=4.8, run=4.55,
`wall_side=right`, `wall_back=true`. Existing room walls provide those two
sides: the duplicate right lower enclosure and upper guard are omitted, and
the rear guard ends at the upper floor. The rear join overlaps the room face
by 2 cm instead of leaving an 18 cm gap. Exposed guards remain. Past the room
wall end, the stair side has at most a 15.4 cm step-down to the upper floor.
The enclosure generator now respects `wall_side` for lower sides as well.

Both delivery routes remain reachable on one offline island. All 86 Python
building tests pass, including the wall-provided enclosure case. Three native
resources and archive extraction/install hashes are verified. Candidate
`building-lab-80bf2e2b5911` installed with the game closed; previous Allen
payloads backed up, all six AKPP/Rancho payload hashes preserved. Receipt:
`../generated/runtime-installs/20261026-235401-allen-stair-wall-join/installation.json`.
ArchiveXL registration is unchanged, retaining all precise vanilla patches.
Fit evidence: `../generated/allen-stair-wall-join/fit-verification.json`.
Restart and walk the second stair, inspect the top landing and apartment wall,
and check the rear join. Live geometry acceptance is pending.


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


## Exposed vertical wall join beside the upper stair

The user tested the previous stair fit and supplied
`Cyberpunk2077_aCCktx8gq5.jpg` and `Cyberpunk2077_NMMaT2iBX3.jpg`.
The visible horizontal opening is a true vertical mismatch: measured native
common walls span Z=0–3.8 m, while this layout's storeys are 4 m apart. Floor
slabs normally mask that difference, but the stair shaft exposes it.

`join_storey_walls=true` now fits existing solid common wall facings to the
next aligned non-passage wall with a 2 mm overlap. The same edge height drives
collision. Top-storey walls, door apertures, room/stair positions and all exact
vanilla patch selections are unchanged. No cover strip or new object is added.
This applies to both stacked wall joins, including the captured upper join.

Sixty one-sided native render-triangle rays through X8.8 at the two seams
find 60 open rays before and zero afterward. Both delivery routes pass offline;
all 89 Python building tests pass, including collision/render top agreement.
Evidence: `../generated/allen-stacked-wall-join/join-verification.json`.
Candidate `building-lab-9170b9b1f3ef` installed with Cyberpunk closed; three
native resources, archive extraction and installed hashes verified. Previous
Allen files backed up and six AKPP/Rancho payload hashes preserved. Receipt:
`../generated/runtime-installs/20261027-001226-allen-stacked-wall-join/installation.json`.
Decorations are excluded for this focused geometry test. The authored decorated
layout retains the join option; its older frozen package is superseded and
must be rebuilt before installation. Restart and inspect the horizontal seam
while ascending/descending and from both adjacent apartments. Live acceptance
remains pending.


## Apartment landing corners: flush the recessed returns

User captures `Cyberpunk2077_HLwnMNPuhm.jpg` and
`Cyberpunk2077_PL4DG4X0pd.jpg` show the short recessed return where the
neighbour-side partition meets the stair-hall wall. Native triangle profiles
confirm a 19.9 cm step at local X8.81–8.95: hallway face Y11.8, short return
Y11.999, on both apartment floors.

Six scoped `wall_extensions` now extend the first solid partition bays toward
X8.8 on both sides of each landing, and the north stair-hall wall toward
Y11.8. Both visual facings and collision follow the same authored start/end
distances. Extensions reject door/passage edges. Doorway centres, stairs,
room definitions and prior exact vanilla patches are unchanged; no strips or
new objects are added. Native face profiles now differ by less than 1 mm.
Both delivery routes pass, along with 90 Python building tests, 117 corner
rays and the earlier 60 vertical seam rays.

Candidate `building-lab-3690bbde4a02` installed with Cyberpunk closed;
previous Allen files backed up and six AKPP/Rancho hashes preserved. Three
native readbacks, archive extraction and installed hashes pass. Receipt:
`../generated/runtime-installs/20261027-001824-allen-apartment-corners/installation.json`.
Evidence in `../generated/allen-apartment-corners/`: `fit-verification.json`,
`corner-rays.json`, `join-verification.json`. Decorations remain excluded.
Restart and inspect both landing corners on both floors, including inside
the apartments, and walk the doorway/stair approaches. Live fit is pending.


## First apartment-floor stair joins A / B / C

User capture `Cyberpunk2077_KR6A2xHQlH.jpg` labels A between the stairs,
B along the rear wall and C along the side room wall. The lower stair now
uses X3.2/Y4.8, width2.8/run4.7, `wall_side=left`, `wall_back=true`.
The second stair shifts X6.25 to X6.2. Existing room walls provide B and C;
the duplicate upper back and left guards are omitted. The lower stair exit
remains Y9.5 and flight widths remain 1.2 m. Its wider central partition is
0.4 m. A's lower-stair upper-right guard overlaps the adjacent stair's left
enclosure by 4 cm instead of leaving an 11 cm slot.

Native render probes show A's former open slot now hits its guard cap;
B and C now hit the room's painted faces at Y3.2 and X3.2, replacing the
setback guard faces at Y3.5 and X3.3. Lower back support ends at the first
apartment floor rather than protruding above it. Generated tread/shaft cuts,
guards and collision follow the stair transforms.

The wall-provided return-stair navigation edges now account consistently for
the common wall's additional 3 cm collision trim beyond its painted face.
Both ground-floor portal attachments and sloped stair triangles use the same
usable flight edges. This preserves a connected route while respecting that
collision margin. All 91 Python building tests pass, including the wall-hugging
two-stair route. Both delivery rooms are reachable on one offline island.
Doorways, wall extensions, vertical wall joins and exact vanilla patches are
retained. Decorations remain excluded. Native fit evidence:
`../generated/allen-stair-abc/fit-verification.json`.


Candidate `building-lab-dacf71c3d925` installed with Cyberpunk closed; three
native resources and archive/install hashes verified. Previous Allen files
backed up; all six AKPP/Rancho payload hashes preserved. Receipt:
`../generated/runtime-installs/20261027-002410-allen-stair-abc/installation.json`.
Restart and check A/B/C from the first apartment landing, then walk both
flights and turning landings. Also inspect the top landing after its 5 cm
stair shift. Live clearance/appearance acceptance remains pending.


## Pavement intruding through the lobby base and threshold

Captures `Cyberpunk2077_3aGF9Vu1oK.jpg`, `Cyberpunk2077_u6mGisC6Iz.jpg`
and `Cyberpunk2077_JhnX9kdm4G.jpg` identify collision placement 3184,
actors 18/17/20 in `exterior_-9_13_0_1`. Surveying matched them to
`worldInstancedMeshNode` placement 2950, instances 1/0/2, mesh
`street_a_sidewalk_blank_c_w300_l300.mesh`. Its fourth instance also reaches
inside at low height; it matches actor 19. Fresh mesh raw/GLB reads establish
a 3×3×0.2 m slab with a corner pivot. The tilted placements reach local
X17.526–17.681 at their inner edges, causing the lobby intrusion.

Only those four render instances and four matched actors are replaced. Each
replacement reduces its native X width until its inner bound is X17.99,
behind the lobby entrance line. All original outer-edge vertices and tilts
remain fixed, retaining the street-side edge and slab planes. This is a scoped
inner-edge trim by per-instance scaling, not a shared mesh override. The
remaining 124 collision actors in the source node are retained.

Matching replacement boxes preserve full local rotation, composed with the
building anchor yaw. Their measured corners match the replacement render
bounds (pre-serialization maximum error <1e-9 m); native collision bytes and
mesh placement/scale/rotation survive readback. Shell collision boxes now
support validated unit quaternions, with the prior yaw-only default retained.
All 93 building tests pass. Both offline delivery routes remain reachable;
prior stairs, doors and patch selections are retained. Decorations excluded.

Installed candidate `building-lab-ba617ae13528` with Cyberpunk closed; native
readbacks, archive extraction and installation hashes verified. Previous Allen
files backed up; all six AKPP/Rancho hashes preserved. Receipt:
`../generated/runtime-installs/20261027-003155-allen-lobby-pavement/installation.json`.
Evidence: `../generated/allen-lobby-pavement/fit-verification.json` plus the
fresh mesh raw/preview reports. Restart and inspect the lobby wall bases and
threshold, then walk across the entrance and along the outside pavement.
Live appearance and street/threshold collision acceptance remain pending.


## Three stair corners and the descending ceiling edge

User captures `Cyberpunk2077_7s4GYtlYhZ.jpg`,
`codex-clipboard-913d8b9b-6261-4d27-bb81-b26904340b24.jpg` and
`codex-clipboard-ced3a611-f1df-4bb1-bbd7-b70315f5c832.jpg` identify the lobby
stair enclosure corner, top guard `guard:stairs-1-2:upper:0`, and
`tile:0:1:3:ceiling:2` viewed while descending.

Return-stair front/back faces now include the side-guard thickness at each
exposed corner. Previously perpendicular boxes met only at a vertical edge,
leaving a 12×12 cm recessed corner square. Existing room-wall sides receive
no extra return. Collision uses the same fitted boxes. Ceiling cuts now stop
at the shaft edge underneath the front guard; the additional guard cut is
retained only for the upper walkable floor. This moves the ceiling edge under
the guard instead of leaving its slab lip exposed at the outside face.

Native rendered-triangle probes verify the lobby outer corner moved X6.0 to
X6.12, the upper outer corner X6.2 to X6.08, and the descending ceiling now
meets at Z3.7 beneath the guard rather than exposing its bottom at Z3.8.
A probe inside the actual stair opening remains clear. Both delivery routes
remain reachable on one island; all 93 building tests pass, including guard
corner dimensions, preserved floor cuts and clear ceiling apertures.
The authored layout, doors and precise retrofit patches are unchanged.
Evidence: `../generated/allen-stair-corners/fit-verification.json`.
Decorations remain excluded. Live corner/headroom checks are pending.


Installed `building-lab-5d267160796e` with Cyberpunk closed; three native
resources, archive extraction and installed hashes pass. Previous Allen
payloads backed up; all six AKPP/Rancho payload hashes preserved. Receipt:
`../generated/runtime-installs/20261027-004657-allen-stair-corners/installation.json`.
Restart and inspect all three reported corners from both sides; descend the
lobby stairs to check the ceiling edge and walk both stair routes. Live
acceptance remains pending.


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
