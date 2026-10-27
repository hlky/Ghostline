# Building Lab

For a visual introduction, open the [screenshot walkthrough](building-ui-walkthrough.html),
which tours the workspace, room and object inspectors, module library, quest
bindings, project files, world placement, validation and export review.

Building Lab is a local room layout editor for assembling Cyberpunk interiors
from a measured vanilla architecture kit. Draw rooms on a plan, place openings,
and inspect the same compiled geometry and collision that the exporter uses.
World Builder is optional for subsequent placement and dressing.

The expanded [kit and module library](building-kits.md) provides 15 room presets
and 9,859 measured mesh modules across all 111 discovered geometry families.
Use the kit selector for rooms, or **Browse all kits and modules** for native-size
specialist pieces, complete family contents and exterior architecture.

This is an architecture prototype. Exports pass serialization and package
verification; player collision, streaming and interior transitions still require
an in-game playtest at the intended location.

## Start the editor

Run from the repository root:

```powershell
uv sync --extra dev --extra building
npm ci --prefix tools/building_ui --ignore-scripts
npm run build --prefix tools/building_ui
uv run python -B tools/building_builder.py prepare-assets
uv run python -B tools/building_ui.py
```

Open <http://127.0.0.1:8792>. Asset preparation reads the configured game archives
and caches the kit GLBs under `generated/building-editor/assets`. It requires the
local native mesh exporter and configured game path. It does not modify the game.
The server listens only on loopback and loads its scripts locally.

The editor now uses React, strict TypeScript and Tailwind through Vite. The
Python server serves the production bundle from `tools/building_ui/dist` and
keeps ownership of compilation, validation, source saving and native export.
Rebuild after frontend changes. For hot reload, leave the Python backend on
8792 and run `npm run dev --prefix tools/building_ui` on loopback port 5174.
Vite proxies the existing APIs and prepared geometry to the local backend;
the backend's Host/Origin checks stay enabled.

Use the **Build**, **Objects**, **Quest** and **Project** panels on the left.
The right inspector edits the current selection. **Objects** opens the module
library; **Project** contains saved layouts and JSON transfer. Shell references
are grouped separately from authored objects. Quest bindings and experimental
navigation are disclosed only when needed. Inputs commit on blur or Enter;
Escape cancels an uncommitted field edit. Invalid compilation retains the last
valid layout and Undo history.

Frontend ownership, checks and the migration audit are documented in
[the frontend README](../../tools/building_ui/README.md) and
[the UX review](building-editor-ux-review.md).

## Build a layout

1. Choose **Draw room**, then drag on the grid. Rooms snap to 3 m modules.
2. Use **Select** to move a room or drag its highlighted corner to resize it.
   The inspector also accepts exact position and dimensions.
3. Draw adjacent rooms to produce a shared partition. Use **Doorway** on a wall
   to replace one bay with a door aperture; **Open bay** removes the whole bay.
   Click again with the same tool to restore the wall.
4. Use the floor selector for up to four storeys. Draw rooms on both floors,
   then choose **Stairs** and click the south-west corner of a 3 by 9 m flight.
   Each end needs a 3 m landing inside the room. The compiler cuts the shaft,
   builds steps and guard walls, and connects the navigation surfaces.
   The current flight rises north; lifts are not generated.
5. Inspect the cutaway, roof and collision views. The preview uses vanilla mesh
   geometry with neutral materials. Finish selections are exported as native
   mesh appearances, rather than rendered as final game materials.
6. Set **World anchor** to the intended game position and yaw. The example's
   origin of zero is a provisional anchor, not a reviewed Night City location.
7. **Auto door** and **Manual door** place vanilla door devices in a bay.
   With Select active, click the device doorway to set its initial state.
   Closed unlocked doors have navigation links; locked doors block the offline
   route and start with a disabled native link. Live door behaviour needs testing.
8. Use **Save layout** to write the owning project's plain authoring JSON.
   **Open saved layout** reloads it. Browser storage preserves a local draft;
   JSON import/download supports moving layouts between machines.

Undo and redo operate on room, opening, finish and anchor changes. Resizing or
moving a room can remove openings whose original wall no longer exists. The
status message reports this, and Undo restores the earlier layout.

Shortcuts: `1` select, `2` draw, `3` doorway, `4` open bay, `5` automatic door, `6` manual door, `7` stairs, `Delete` selected
room, `Ctrl+Z` undo, `Ctrl+Shift+Z` redo, `Ctrl+S` save.

## Export and package

**Export project** creates a self-contained WolvenKit project ZIP. Each export
also remains in `generated/building-editor/exports/<export-id>`. It contains:

- The editable `.building.json` authoring layout.
- Authored CR2W JSON under `source/raw/mod/building_lab`.
- Serialized streaming sector and block under `source/archive/mod/building_lab`.
- ArchiveXL registration under `source/resources`.
- Project metadata, package profile and a verification report with binary hashes.

WolvenKit creates fresh binaries. The independent native reader checks placement
counts and transforms, mesh references, appearances and collision buffer bytes.
Template-based native writing is unsuitable here: growing sector buffers can
retain previous placements, and block templates can retain stale imports.

The command-line equivalent is:

```powershell
py -B tools/building_builder.py validate projects/experiments/building-lab/buildings/workshop.building.json
py -B tools/building_builder.py export projects/experiments/building-lab/buildings/workshop.building.json --out projects/experiments/building-lab/generated/export --serialize
py -B tools/package_project.py --project projects/experiments/building-lab/generated/export --plan
py -B tools/package_project.py --project projects/experiments/building-lab/generated/export
```

The normal packager verifies the archive and ZIP. Building and exporting do not
install the layout. Review the anchor and playtest the resulting package before
using it for a quest. Export projects share the Building Lab archive name; package
the intended layout snapshot rather than installing several competing snapshots.

## Kits and compiler contracts

Choose the room preset in the sidebar. All room presets use measured 3 m bays
and shared common floor/ceiling modules. The module library preserves other sizes.
The original three presets are listed below; twelve additional presets and the
complete family catalogue are covered in [Building kits](building-kits.md).

| Kit | Wall height | Storey spacing | Wall finishes |
| --- | --- | --- | --- |
| Common concrete | 3.8 m | 4.2 m | Six concrete, paint, tile, brick and paper variants |
| Industrial workshop | 4.0 m | 4.4 m | Seventeen industrial, ripperdoc, paint and brick variants |
| Rancho house | 4.0 m | 4.4 m | Eleven brick, cinderblock, plaster and siding variants |

Catalogs live in `tools/building_ui/common-kit.json` and `tools/building_ui/kits`.
The new families include hashes of their freshly serialized vanilla mesh sources.
Door collision leaves a conservative 1.5 m by 2.4 m aperture.

The compiler deduplicates shared walls and emits floor, ceiling and partition
collision. Door apertures use separate jambs and lintel. Stairs use scaled vanilla
floor slabs as treads, solid step collision, ascending parapets and upper shaft
guards. They have at most 20 cm risers and a 35 degree maximum slope. Shafts cannot
cross room partitions or other shafts. A stair and both landings must lie in one
room on each floor. Remove a flight before deleting a room supporting it.

Layouts support rectangular rooms, up to 32 rooms and 600 tiles in a 120 m
workspace. Rooms on the same floor cannot overlap. The native compiler and editor
consume the same scene. RED X/Y remain horizontal and Z remains vertical; only
Three.js display converts axes. Exported door devices use a schematic leaf in
the preview rather than a simulated entity animation.

## Navigation and entrance connections

Enable **Nav** to see generated agent-clearance surfaces. **Routes and entrance
links** checks local X/Y/Z points and highlights a connected polygon route.
The floor topology includes walls, door clearance, guard walls and stair ramps.
A locked device door separates its two sides; NPC-sized polygons do not pass
under a closed/locked leaf through an always-connected floor polygon.

Enable **Export experimental native navigation** to include version 8 VAND tiles,
a Navigation streaming sector with an embedded Human `.navmesh` resource. Choose an
explicit nonzero tile layer. Layer zero is refused for additive export because it
can collide with vanilla tile identities. The isolated navigation lab uses layer
200 at world Z=700, rather than claiming a reviewed city location.

In the route dialog, **Add entrance link** creates a bidirectional Floor off-mesh
connection from a walkable point in the building to a surveyed world navigation
endpoint. Endpoints use local coordinates. The link is limited to 4 m in length
and 0.6 m in height; it does not build a physical bridge or staircase. A target
outside the generated surface cannot pass the offline route check on its own.
Its existing Human coverage must be proved separately.

New layers do not regenerate or carve vanilla navigation. A new room above street
coverage is not automatically connected to it, and walls placed across existing
routes still need a site-specific obstruction check. See
[Building navigation](building-navigation.md) for the format, independent oracle,
vanilla-tile coexistence test and live NPC proof requirements.

The optional **building-lab-test** package profile includes the CET diagnostic UI
and generated room/stair test points. The normal **building-lab** profile excludes
those diagnostics. Use the normal packager rather than a full GUI source-resource
copy when producing a shipping package.

## Retrofitting shells

An interior layout can be positioned inside a vanilla shell using its world
anchor. The entrance workflow now emits ArchiveXL patches for selected visual
placements, individual render instances, collision actors or actor-relative shapes.
It does not perform a Boolean cut through an arbitrary monolithic building mesh.
Choose a separately removable facade bay and replace it with a doorway module;
if its collision spans the whole building, a reviewed replacement collision model
is still required.

Create a source-pinned survey from native CR2W JSON:

```powershell
uv run python -B tools/building_retrofit.py <sector.streamingsector.json> --depot 'base\worlds\03_night_city\_compiled\default\<sector>.streamingsector' --position <world-x> <world-y> <world-z> --radius 8 --out generated/building-editor/entrance.survey.json
```

Open **Shell entrance patches**, import the survey and select facade and collision
candidates. An example survey is in
`projects/experiments/building-lab/surveys/rancho-facade.survey.json`; it contains
candidates but no active removals. It depends on the source-pinned local world
cache named in its `selection.source`. Recreate/review surveys after a source or
game-version change.

For an area search, use a reference streaming block and the root of cached
serialized sector paths. This writes `index.json` and individual importable
surveys, reporting missing cached sectors and skipped unbounded descriptors:

```powershell
uv run python -B tools/building_retrofit.py --streaming-block .tmp/vanilla-braindance/streamingblocks-json/all.streamingblock.json --sector-root converted/world-location-database/full-world/serialized-sectors --position -692.728 -1415.521 7.553 --radius 8 --out generated/building-editor/rancho-area-survey
```

The concrete Rancho pair is recorded in
`projects/experiments/building-lab/surveys/rancho-entrance-pair.json`:

- Visible wall: `exterior_-11_-23_0_0.streamingsector`, placement 530,
  render instance 0 of 4.
- Collision: `exterior_-2_-3_0_3.streamingsector`, placement 850,
  actor 119 of 128, actor-relative shape 0.
- Both pivots are exactly `(-692.727966, -1415.521240, 7.552643)`.
  The collision is a box about 3 m wide, 4.299 m high and 0.175 m thick;
  collision height exceeds the kit's measured 4 m mesh height.

`rancho-structural-collision.survey.json` supplies the second sector for the UI.
Import each survey and apply the reviewed selections; the editor retains
selections from other sectors. These checked examples do not activate a patch
in the saved layouts. The pair establishes source identity and a precise
removal candidate; doorway alignment, replacement collision, occlusion and a
live walk-through remain necessary.

ArchiveXL deletion indices and `expectedNodes` address `nodeData` placement
entries, not the separate mesh-definition array. Instanced facades require
`expectedInstances` and explicit `instanceDeletions`. Collision requires
`expectedActors` and actor selections; `[actor, shape]` pairs select an
actor-relative shape. Validation rejects changed source hashes/counts/types and
out-of-range or duplicate selections. Actor/shape removal requires ArchiveXL
1.27 or later. The package profile explicitly selects its sector patches so the
packager retains them without importing another project's unrelated edits.

Candidate searches use pivots, not full mesh bounds. Large collision actors may
extend beyond the search radius. Removing visible geometry alone does not remove
its collision or occlusion. Shell previews, arbitrary Boolean cuts, final
lighting/audio/reflections and furnishing remain separate work. An actual shell
entrance still needs a player walk-through, save/load check and native NPC route
query at the chosen site.

See [Buildings and interiors](buildings-and-interiors.md) for the initial vanilla
survey, World Builder limitations and the broader production path.


## Direct wall controls

Use **Walls (8)**, click a wall, then choose **Solid wall**, **Doorway** or
**Open / remove** in Wall Controls. The selected span is highlighted. These
controls cover regular room bays, measured shell sides and custom lining
partitions. Opening a device bay also removes its obsolete door settings and
device; Undo restores the complete previous layout. Disabled custom partitions
appear dashed only while using Walls, so they can be selected and restored.

**Draw partition · two clicks** places an independent Rancho wall between two
points, snapping to 5 cm and constraining it horizontally or vertically. Escape
cancels. Its default height is 3.5 m (limited by storey spacing); inspect low-roof
areas before exporting. Keep **Room zones** checked when editing room rectangles;
uncheck it for a clear plan showing physical walls without zone outlines/labels.

**Save copy** assigns a new layout identity and saves a separate authoring file.
Rename it with Building name. **Save layout** subsequently updates that copy.
The saved **Rancho open-plan starter** (`building_7f30166a.building.json`) keeps
the garage enclosed and removes the ground-floor stair and residential partitions.
It is a design starter, with no stair connecting upstairs, and is not installed.


## Importing an existing shell as one open room

`tools/building_shell_import.py` converts a reviewed selection of source-pinned
static placements and individual render instances into locked editor references.
The import specification supplies the measured room and anchor; the tool does
not infer a building footprint from proximity. It preserves vanilla pivots,
quaternions, scales and source appearances. A source appearance missing from the
mesh is retained as evidence while the neutral preview uses a measured fallback.

```powershell
.venv/Scripts/python.exe -B tools/building_shell_import.py projects/experiments/building-lab/surveys/akpp-logistics-shell-import.json --out projects/experiments/building-lab/buildings/akpp-logistics-open-shell.building.json
```

The AKPP starter contains one 6 by 6 m ground-floor room and twelve reference
pieces across the retained shell. The rear wall is pinned by the user's Ru Lai
interior screenshot: collision placement 3536, actor 118, and matching visual
placement 5860, render instance 0. Ru Lai is outside the editable bay.

Open **AKPP Logistics · open shell** from **Open saved layout**. Dashed plan
outlines and translucent 3D geometry are existing shell references. Their
transforms and finishes are locked in the inspector, and native export excludes
them so existing game geometry is not duplicated. Cutaway hides front/south
reference pieces. Floor selection shows the upper reference modules without
adding an upstairs authoring room. Add partitions inside the ground-floor room.

The starter now includes the matching native hinged_e manual door at the surveyed
recess, plus pinned replacements for the old leaf/casing and their collision
actors. It has no exterior navigation links or installed game package. Surveying
hidden collision/occlusion, playtesting the door and adding finished interior
linings remain separate work.
