# Allen residential lobby and hallway decoration shortlist

Research for the user's vanilla-location decoration request, 2026-10-26.
The first dressing pass is authored and staged; the installed stair-test candidate remains unchanged until Cyberpunk is closed.
Exact measured resource paths and hashes are in `allen-decoration-palette.json`.
Vanilla placements were discovered in the local serialized Night City corpus;
candidate resources were freshly read from the installed base-game archives.

## Direction

A refurbished Kabuki residential block: warm practical lighting, charcoal and
muted teal accents, a few nicer fittings layered over an older concrete shell.
Repeat the same lighting, signs and wall treatment on both landings. Keep the
lobby more welcoming and the stairwell more utilitarian. Signs should help the
delivery route read clearly, including recognising the building on a return visit.

## First dressing pass

| Element | Vanilla candidate | Fit and use |
| --- | --- | --- |
| Recessed-looking ceiling fixtures | `ceiling_lamp_rectangle_wide_inside_a.mesh` | 1.00 Ã— 0.50 Ã— 0.133 m; verified `Warm_light`, `warm_dim`, `Warm_light_bright` appearances. Seat housings partly into a ceiling reveal; preserve the repaired closed ceiling. Pair visible emitters with native lights. |
| Stair/landing accent light | `rancho_wall_lamp_c_warm.ent` | Contains a real game light, warm pale RGB 255/251/205; donor intensity 1000 and radius 15 m need tuning for these small spaces. Use sparingly by landings. |
| Subtle wall treatment | Common wall `paint_grey`, plus apartment-kit decorative inserts | Keep existing walls and collision; add a small number of shallow, fitted accents. NKT 1 m decorative pieces exist, but some are 20 cm deep and 4 m high: do not place them across a 3.4 m ceiling or beside narrow stair exits unchanged. |
| Apartment numbering | `megabuilding_a_apartment_number_0/1/2_a.mesh` and number case | Genuine illuminated vanilla numbering family. Mesh axes and multi-part assembly require fitting against a real donor before producing compact door labels. Do not infer number spacing from resource names. |
| Directory / floor signs | `signage_blank_panel_thin_21x9.mesh` plus vanilla lettering/arrow assets | Native panel is 2.334 Ã— 1 m, 2.8 cm deep, with green/blue/white and weathered appearances. A small directory needs resizing and authored lettering; a blank panel alone is not a readable directory. Aim for a restrained backlit panel, with floor marker at each stair arrival. |
| Security camera | `corpo_security_camera_b_indoor.mesh` | Compact dome, 19 Ã— 19 Ã— 14 cm. One covers the entrance/security desk, one covers stair circulation. Mesh-only placement is decorative; hacking/detection requires a device entity and network setup. |
| Alternative camera | `corpo_security_camera_a_indoor.mesh` | Larger directional camera, 57 Ã— 18 Ã— 33 cm; use only if the mount and sight line fit. |
| Lobby plants | `small_city_planter_a.mesh`, `small_city_planter_c.mesh` with `yucca_single_low.mesh` | A: about 60 cm wide/59 cm high; C: 48 cm wide/92 cm high. Both have `entropy_clean` and `entropy_painted`. Low yucca foliage spans about 0.9 m: fit roots/pot rim and allow for the leaves. Two plants in lobby corners are sufficient. |
| Waiting seat | `megabuilding_deco_bench_ac.mesh` | About 2.22 Ã— 0.94 Ã— 1.10 m. Better fit than the 4.51 m `aa` bench. Check neutral/default upholstery in game; keep seat front and entry aisle clear. |
| Intercom | `device_kitsch_d_intercom.mesh` | About 44 cm high, narrow wall unit. One near the directory or recipient doors. Static decoration initially; native intercom behavior belongs to quest/device work. |
| Fire equipment | `fire_extinguisher_b.mesh` | About 82 cm high; put at a sensible stair landing with a small identification sign. Static mesh avoids importing the explosive extinguisher device accidentally. |
| Small lived-in details | Kitsch desk pots, parcels, paperwork and a modest notice area | The checked Kitsch pots are only 12â€“20 cm wide: desk accents, not floor planters. Add a few intentional details at reception and one or two doorways rather than cluttering every wall. |

Suggested distribution:

- Lobby: four to six warm fixtures, reception accessories, one directory, one
  dome camera, one waiting seat, two planters, and a compact parcel shelf/notice
  area. Avoid a second full reception desk until the guard interaction is set.
- Each upper hallway: two or three warm fixtures, apartment labels, one floor
  marker with a stair arrow, a restrained wall accent, fire equipment and a
  small variation such as a doormat or parcel beside one recipient door.
- Stairs: practical wall lights and clear floor markers. Preserve headroom,
  guarded edges and the repaired ceiling cuts; avoid overhead hanging clutter.

Use clear warm-white light for navigation and small, cooler directory/number
accents. Final exposure and intensity need a daytime/nighttime game check;
geometry-only GLBs do not preview emissive materials or actual light falloff.
Preserve a continuous clear route of at least 1.2 m and larger waiting/interaction
space at reception and delivery doors. Re-run route/collision checks after
placement, including leaf/branch bounds and bench depth.

## Assembly findings and limits

The entity named `ceiling_lamp_rectangle_wide_inside_a.ent` actually contains
`ceiling_lamp_long_a.mesh` and a greenish RGB 231/253/204 light in the inspected
resource. Its filename is not proof that it matches the shortlisted warm
rectangular housing. Use a reviewed mod-owned light assembly or explicit native
light nodes with the selected housing; do not spawn that donor unchanged.

Directory text, compact number assembly, camera/intercom behavior, actual
materials and light performance are not yet validated. The next useful milestone
is one furnished lobby bay and one labelled apartment-door bay in a separate
candidate, then a live material/light check before repeating them upstairs.


## First pass authored

The residential layout now includes 68 decoration modules and 15 explicit warm
native light nodes, with 4 m falloff radii and initial intensities 32/45. Visible
warm rectangular housings and their covers sit near the ceiling surface.
Reception and the lobby receive five fixtures, parcels one, upper delivery
hallways three each, and clear stair landings one per floor.

Dressing includes a native waiting bench facing into the lobby, two clean
planters with low yucca, a reception desk pot, two shallow green wall accents,
four dome cameras, three static fire extinguishers and a parcel-room intercom.
Door plaques read 101/102 and 201/202, with floor markers 0/1/2. The actual
native number triangles were projected to verify reading direction; native
front is +Y, not +X. Number Y depth is scaled to 0.3, preserving glyph width
and height while recessing the remote support geometry behind the painted
wall. Plaque panels remain in front of the wall. A text directory and smaller
lived-in props can follow the first live material check.

Room/stair definitions, shell patches, entrance door and previous objects are
unchanged. Only three new floor blockers are added for the bench and planters;
planter blockers include foliage spread. Both offline delivery routes remain
reachable on one navigation island. All 88 Python building tests pass,
including explicit light anchoring and invalid-light rejection. Native resource
readback verifies light color, intensity and radius. Runtime light/material
appearance and exposure remain untested. Cameras/intercom are static decor.

Evidence: `../generated/allen-decoration-pass-1/decoration-verification.json`
and `../generated/allen-decoration-pass-1/placement-review.png` (geometry-only,
not an in-game material render). The package is staged separately while the
user tests the installed stair candidate; do not replace an archive held by
the running game. The first package in `packages/` is superseded by the corrected
number orientation in `packages-final/`.

Final staged candidate: `building-lab-3a1d082b6a9b`, verification under
`../generated/allen-decoration-pass-1/project/generated/packages-final/`.
Archive extraction and all staged payload hashes pass. Existing Allen,
AKPP and Rancho installation hashes remain unchanged; game was running at
handoff. After closing the game, install only the two verified Allen payloads
with backups, then restart and check fixtures/materials in day/night, label
reading from both hallway directions, bench facing and planter clearance.


The staged decoration package `building-lab-3a1d082b6a9b` is now superseded:
the subsequent stair test exposed the 20 cm inter-storey wall gap. The authored
layout retains all decoration and adds `join_storey_walls=true`, but the old
frozen decoration package does not include this repair. Rebuild it before
installing decorations; the current seam-repair package intentionally excludes
decorations so the user can continue checking geometry first.
