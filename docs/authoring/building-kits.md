# Vanilla building kits and module library

The prepared catalogue covers every mesh referenced by the surveyed Night City
architecture corpus: **9,859 CMesh resources across 111 geometry families**.
This includes all **30 common interior families**, plus district and specialist
groups. It contains 9,833 `.mesh` resources and 26 `.w2mesh` resources that were
confirmed to contain CMesh data. There are 41,879 appearance entries across the
meshes; repeated names such as `default` are included in that count.

The room builder has **15 presets**: the original three and twelve additional
geometry-checked wall/doorway combinations. Every prepared resource is also
available for free placement at its original dimensions.

The earlier broad discovery count of 400 groups included material/reference
paths. The 111 count groups actual mesh resources at a consistent family depth.
Neither count is an official CDPR kit count. This corpus is not an exhaustive
inventory of every base-game or Dogtown architecture asset.

## Use a room preset

Select a construction kit in the sidebar and draw rooms normally. New presets
include apartments, motel/corridor interiors, Arasaka interiors, offices, metro
walls and Kabuki architecture. They share the common floor and ceiling modules;
they are not complete reproductions of every floor, trim or roof in the family.

Each added preset records source hashes, measured dimensions and per-piece pivot
offsets. Promotion requires matching family/name stems, compatible heights and
appearances, sampled closed-wall coverage, and a centred 1.5 × 2.4 m aperture
checked against projected render-triangle intersections. Thin obstructions between
sample rays also reject a doorway. The existing three manual presets retain
their original reviewed contracts.

Successful geometry checks do not certify live collision, native door fitting,
lighting or material dependencies. The independent native verification writes
and reads back **60 resources for all 15 presets**, using the two-storey stair
and door example. Results are in `generated/building-editor/kit-verification`.

## Use any prepared module

1. Open **Browse all kits and modules**.
2. Search by asset/path, select a family, or filter by piece type. Type labels
   are search hints inferred from names; actual geometry determines suitability.
3. Select a result to see its real mesh, measured dimensions, depot path and
   available appearances. Previews use neutral materials.
4. Choose **Place on plan**, then click the plan. Placement initially snaps to
   the room grid. The module inspector allows precise X/Y/Z and yaw edits.
5. Use **Base centre** to rotate/place around the measured bottom centre, or
   **Vanilla pivot** to preserve the original authoring origin. No automatic
   resizing is applied. Plan and 3D framing include large and distant modules.
6. Select a module in the plan or sidebar to edit its appearance or remove it.
   Undo/redo, JSON save/load and native project export retain module selections.
   Module positions are local metres; floor membership controls visibility.
   Changing the room kit does not reposition existing modules.

Library modules are visual by default. Optional **Solid bounding box** collision
is limited to reviewed wall/floor/ceiling/structural pieces and fills the entire
bounding volume, including holes. It does not copy the vanilla physics shapes.
Such boxes carve existing generated room navigation where they intersect the
agent, including across floors. They do not add new walkable navmesh surfaces.

For the common interior wall, the main painted face is at native Y=0.20 m;
the full 0.23 m bounds include projecting trim. `wall_facing_depth` controls
reverse-facing placement independently of collision `wall_thickness`. Using
the full trim bounds for both caused inside-corner gaps. Solid common wall
skins overlap by 1 mm at their ends to tolerate quantized mesh vertices. Do
not add separate corner columns to hide a panel-placement mismatch.

A static staircase, doorway or shutter mesh does not automatically gain stair
access, a floor cutout, interactive behaviour or NPC navigation. Use the room
builder's stairs/devices for those contracts and survey replacement collision
for custom assemblies. Static mesh appearance selection is preserved in game;
material rendering is not reproduced by the neutral preview.

`motel-modules.building.json` is an additional example containing a new motel
room preset, the standard guarded stair/native door setup, and a freely placed
native handrail. That handrail is deliberately visual only. It is not a physical
guard or a navigation obstacle.

## Rebuild the catalogue and previews

Configure the game and ghostline-red paths in `toolchain.local.json`, build the
current native CLI, and run from the repository root:

```powershell
uv run python -B tools/building_library.py plan
uv run python -B tools/building_library.py measure --resume --threads 4
uv run python -B tools/building_library.py preview --resume --threads 4
uv run python -B tools/building_library.py catalog
uv run python -B tools/building_kit_recipes.py
uv run python -B tools/building_builder.py prepare-assets
uv run python -B tools/verify_building_kits.py
```

The checked catalogue supplies resource paths when the original generated corpus
scan is absent. Preparation reads vanilla content archives and retries expansion
resources from the installed `ep1` archive directory; it does not index installed
mod overrides. Failed resources remain explicit catalogue records. Resume checks
that cached outputs can be parsed, rather than accepting a file solely because
it exists. Omit `--resume` to refresh source measurements after a game update.

The native `mesh-export-batch --geometry-only` mode skips material dependency
decoding and sidecars. It keeps per-resource geometry errors. Other workflows
retain their existing material-export behaviour. Catalogue geometry readiness
does not imply that all material dependencies were independently validated.

Source buffers, GLBs, sidecars and verification projects stay under ignored
`generated/building-editor`. The checked catalogue contains measurements,
appearances, source/content/preview hashes and coverage metadata. It does not
contain the vanilla mesh buffers. Module manifests pin canonical resource-content
and preview hashes; a changed source requires reselection/review.

The remaining 294 non-mesh references comprise 47 entities and 247 material,
mask and multilayer-setup resources. They remain listed in the catalogue for
discovery and are not falsely exposed as static mesh modules.

The checked [verification receipt](../../reference/world/building-kit-verification.json)
records catalogue hashes, the 60 native preset resources, the legacy mesh
reference check, test results and the verified motel playtest package. The
package is staged for a dedicated test save and has not been installed.

See [Building Lab](building-editor.md) for export and shell entrance work, and
[Building navigation](building-navigation.md) for the live NPC proof procedure.
