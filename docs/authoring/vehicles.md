# Vehicle database

`tools/vehicle_database.py` builds a local, searchable vehicle catalog using
the same installed-game authoring approach as the item database. The gallery
is currently served at [localhost port 8768](http://127.0.0.1:8768).

The initial local build contains 1,281 vehicle records and 958 game previews,
including previews for all 88 records with `_player` in their IDs. Records
include base, NPC, quest, debug and player variants; they are not a count of
distinct car models or proof that every variant is suitable for race AI.

## Build and browse

Run from the repository root using the existing development environment:

```powershell
.venv/Scripts/python.exe -B tools/vehicle_database.py build
.venv/Scripts/python.exe -B tools/vehicle_database.py previews
.venv/Scripts/python.exe -B tools/vehicle_database.py serve --port 8768 --open
```

Use global `--gamepath` and `--output` options before the subcommand to select
another installation or output directory. Outputs default to ignored
`converted/vehicle-database`:

- `vehicles.sqlite3`: records and independently attached preview metadata.
- `catalog.json`: portable vehicle metadata with source-file hashes.
- `previews/`: cropped native previews and imported studio renders.
- `cache/previews/`: extracted atlas/texture resources and source receipts.
- `preview-report.json`: successful previews, missing art and extraction errors.

The build reads base REDmod `.tweak` sources, followed by ep1 overrides. It
resolves record inheritance, inline engine structures, gear arrays, and array
replacement/addition. It joins English localization from the existing item
database cache when present. For a fresh installation:

```powershell
.venv/Scripts/python.exe -B tools/vehicle_database.py build --extract-localization
```

Explicit `build --localization <serialized-onscreens.json>` arguments can
select another language or a reviewed localization snapshot. Without localization,
record-derived names remain searchable and unavailable text stays empty.

## Browse and compare

Search titles, descriptions, record IDs, manufacturers, tags, appearances and
entity paths. Filter by recorded vehicle type, manufacturer, player variants
or preview availability. Sort by name, horsepower, UI mass or calculated HUD top speed.
The gallery shows individual authored entity appearances. Select up to four
appearances to compare across result pages. Copy the exact record/appearance
pair from a card for spawn authoring. A record without an explicit appearance
exposes every authored entity appearance rather than one representative paint.

The player filter uses `_player` in the record name as an authoring convention;
it does not check unlock conditions or current player ownership. Details retain
the exact entity path, requested appearance, parent, source file, tags, armor,
weapon references, gear parameters and preview binding. A blank appearance
means the record does not specify one, not that an arbitrary paint is validated.

## Performance data

Horsepower, production year, drivetrain and UI mass come from resolved
`vehicleUIData`. Physical mass comes separately from `vehDriveModelData`.
Engine torque and RPM come from `vehEngineData`. UI specifications can differ
from simulation values; both masses remain distinguishable.

The cards and comparison table display **calculated top speeds in mph and
km/h**, with the HUD reading separated from world-space speed. The build decodes
the speedometer curve and every referenced engine-torque curve directly from
installed archives. The decoded data and resource hashes are saved in
`cache/performance/curves.json` and recorded in catalog provenance.

The gearing calculation selects the highest positive forward-gear `maxSpeed`;
gear index zero is reverse and cannot set the forward ceiling. For that limit
`v`, the calculations are:

```text
world_mph = v × 3600 / 1609.344
world_kmh = v × 3.6
HUD_mph   = v × vehicle_ui.speed_to_multiplier(v)
HUD_kmh   = HUD_mph × 1.60934
```

The main vehicle HUD's `OnSpeedValueChanged` method in the installed script
bundle establishes the last two operations. The curve comes from
`base/gameplay/curves/vehicle/vehicle_ui.curveset`. Its cubic Bezier handles are
evaluated as actual control points: solve the Bezier time coordinate, then
evaluate its value coordinate. Linear interpolation between the handles would
give incorrect readings. Interior dashboard controllers can have their own
display rules; these values reproduce the main vehicle HUD conversion.

For example, the current authored Caliburn player record has a forward limit
of 45: **207 mph / 333 km/h on the main HUD**, versus **100.7 mph / 162 km/h in
world-space units**. The Porsche 911 Turbo's 40.8 limit gives approximately
**162 mph / 261 km/h on the main HUD**. These are calculated gearing ceilings,
not a simulation of drag-limited sustained speed. Torque curves are decoded
and their endpoint values retained, but are not presented as a complete
traction/drag simulation. Slopes, race AI and runtime changes can alter achieved
speed. Per-gear conversions and the raw source limit remain available in details.

The curve structure is cross-checked against WolvenKit's
`CurveEditorViewModel.RecalculateControlPoints`, which identifies every second
and third cubic point as a control handle. The
[vehicle tuning guide](https://github.com/CDPR-Modding-Documentation/Cyberpunk-Modding-Docs/blob/main/modding-guides/vehicles/changing-handling-and-speed-for-modded-vehicles.md)
also describes the forward/reverse gear layout and authored speed limits.
No missing performance number is replaced with a guessed zero.

These are the installed **REDmod authoring sources**, not a live TweakDB dump.
Changes made by installed TweakXL/REDscript/CET mods and runtime racing
rubber-banding are not reflected. The catalog records individual source and
localization hashes so its snapshot is identifiable.

## Preview provenance and studio renders

Game previews follow `Vehicle.icon` → `UIIcon` → `atlasResourcePath` and
`atlasPartName`. The extractor uses the highest-resolution populated atlas slot,
decodes the bitmap with WolvenKit, and crops the authored UV rectangle with
Pillow. Source archives, serializer/schema/tool identities and the crop binding
are retained. Provider selection is limited to vanilla content/ep1 archives;
installed mod archives are not silently mixed into these previews.

Vanilla record icons are retained in the record API for reference. They often
repeat across paints and equipment variants, so the appearance gallery never
uses them as variant previews. Each appearance has its own render association;
pending or failed renders show a placeholder rather than another paint.

Generate real multi-angle renders directly from the installed game models:

```powershell
# Default: explicit player appearances. --all includes every indexed appearance.
.venv/Scripts/python.exe -B tools/vehicle_database.py render
.venv/Scripts/python.exe -B tools/vehicle_database.py render --all
.venv/Scripts/python.exe -B tools/vehicle_database.py render --record Vehicle.v_sport1_rayfield_caliburn_player --resolution 1024
```

The pipeline resolves `entityTemplatePath` → exact entity appearance binding →
appearance definition → **full-detail component meshes**. It resolves mesh path
hashes from WolvenKit's resource dictionary, assembles panels, wheels and glass
using the vehicle rig and slot hierarchy, respects chunk masks and omits
distance proxies, shadow shells and effect-only cutouts.

The vehicle path uses the existing WolvenKit material export flow and
`tools/item_render_blender.py`: the same Cyberpunk material importer, multilayer
mask repair, studio scene, cameras, rendering and diagnostics used by the item
renderer. Only the rig/slot assembly is vehicle-specific. Original material
graphs and texture resolutions are preserved. Long texture paths are staged
under short names for Blender's Windows image loader. CrystalDome glazing has
an offline approximation; its animated overlay and other runtime effects are
absent. The detailed Caliburn assembly contains roughly 134,000 vertices,
compared with 833 in its unsuitable traffic proxy.
Unsupported or ambiguous appearances remain visibly incomplete. They cannot
fall back to another appearance's materials or vanilla record icon.

Individual render requests default to four 1536×960 views: three-quarter front,
front, rear and side. Bulk `--all` requests default to one hero view per
appearance, prioritizing complete variant coverage before extra angles.
Use `--views hero,left` to select views. The gallery
has a **3D renders only** filter, view buttons and click-to-enlarge images.
`renders/variants/` stores PNGs and per-appearance render receipts;
`variant-render-progress.json` lists coverage and explicit failures.
`variant-index-report.json` records unavailable source bindings.
`cache/variant-renders/` and the short-path `converted/vr/` cache hold serialized
resources, GLBs, material dependencies and exporter/Blender logs. Mesh exports
can be cached across appearances, but each appearance is rendered separately.
Completed images are reused only for the same exact entity/appearance identity.
Rendering reads the installed archive tree, including installed resource
overrides, whose file identities participate in the cache key. It does not
modify the game installation. This is separate from the vanilla-only icon
extraction described above.

Existing externally produced studio images can also be attached:

```powershell
.venv/Scripts/python.exe -B tools/vehicle_database.py attach-preview --record Vehicle.v_sport1_rayfield_caliburn_player --image H:/renders/caliburn.png
```

This validates and copies the image into the catalog, recording its source.
Rebuilding records or refreshing game previews preserves an attached record
render. Record attachments do not override appearance-specific gallery renders.
Only PNG, JPEG and WebP are served. The gallery binds to loopback and
serves no arbitrary filesystem paths.

## Verification

```powershell
.venv/Scripts/python.exe -B -m unittest tests.test_vehicle_database tests.test_vehicle_performance tests.test_vehicle_studio tests.test_vehicle_variants tests.test_item_render_cache -v
```

Targeted coverage includes inherited/inline performance values, localization,
missing data, array semantics, atlas UV orientation, labeled model fallbacks,
studio-image preservation, queries, pagination and HTTP path containment.
Performance tests cover nonlinear Bezier timing, segment boundaries, both unit
systems, reverse exclusion, malformed curves, missing inputs and persisted
calculation provenance.
