# Item And Equipment Authoring

Ghostline can build a searchable, material-aware equipment catalog from the
installed Cyberpunk 2077 data without launching the game. Generated vanilla
metadata, meshes, textures, renders, SQLite files, and caption jobs stay under
ignored `converted/item-database`; they are derived local data, not mod source.

## What It Joins

`tools/item_database.py` keeps gameplay items and render variants separate:

```text
REDmod Items.* record
  -> inherited equipment area, tags, entity name, item type
  -> display/description LocKeys
  -> localized onscreen text
  -> player item-controller .app definition
  -> PMA/PWA component bundle
  -> primary mesh and mesh appearance
  -> material-aware offline render
```

The distinction prevents several frame- or material-specific render variants
from duplicating one item's title and description. Companion components,
including shadows, cuffs, and other mesh pieces, remain attached to the
variant as machine-readable metadata even though the first renderer pass uses
the primary visible mesh.

## Build

First generate the existing installed-game character asset index:

```powershell
py -B .\tools\character_asset_index.py
```

Then extract the 192 player item-controller resources, serialize English
localization, resolve TweakDB inheritance, and build SQLite plus portable JSON:

```powershell
py -B .\tools\item_database.py `
  --output .\converted\item-database `
  build --extract-apps --extract-localization
```

The main outputs are:

- `converted/item-database/items.sqlite3`
- `converted/item-database/catalog.json`
- `converted/item-database/cache/app-metadata`
- `converted/item-database/cache/localization`

Repeatable builds may reuse the serialized cache explicitly:

```powershell
py -B .\tools\item_database.py `
  --output .\converted\item-database `
  build `
  --apps .\converted\item-database\cache\app-metadata `
  --localization .\converted\item-database\cache\localization\base\serialized\onscreens.json.json `
  --localization .\converted\item-database\cache\localization\ep1\serialized\onscreens.json.json
```

## Render

The render command uses the repository's `ghostline-red` submodule to extract
the selected mesh, export native GLB geometry, decode the selected appearance's
materials, textures, and multilayer masks, then bake them to standard glTF PBR
textures. Blender 5.1 imports the result through its native glTF importer for a
deterministic studio render. Neither WolvenKit nor Cyberpunk IO Suite's
material-node builder is used in the normal render path.

```powershell
py -B .\tools\item_database.py `
  --output .\converted\item-database `
  render `
  --item Items.Boots_03_basic_01 `
  --frame pma `
  --views hero,back `
  --resolution 1024
```

Cycles is the default. Use `--samples 256` for a slower final-quality pass.
Images are transparent PNG cutouts with no floor or visible background.

Only the two or three materials referenced by the requested mesh appearance
are exported. Decoded dependencies share
`converted/item-database/material-repo`, and the renderer batches 25 variants
per persistent Blender process. Two processes run concurrently by default;
use `--workers` to tune CPU/GPU contention and `--batch-size` to tune the
process-lifetime boundary. Mesh/material preparation uses 12 concurrent
`ghostline-red` jobs by default on machines with enough logical CPUs; tune it
independently with `--export-workers`.

Use `--reuse-compatible` after a renderer change that affects performance or
diagnostics but not pixels. It reuses the newest complete report with the same
GLB, appearance, engine, resolution, sample count, and ordered views.

Before rendering, the database submits every uncached mesh/appearance pair to
one `ghostline-red mesh-export-batch` process. Game archives are indexed once,
shared textures and multilayer resources are decoded once, and per-item
failures are retained in a machine-readable batch report without discarding
successful exports. Standard PBR bakes are content-addressed, so a material
shared by hundreds of items is generated once and then attached in
milliseconds.

Dependency writes use per-resource locks, allowing unrelated meshes,
materials, and textures to prepare in parallel without corrupting the shared
repository when two appearances reference the same asset.

The native baker handles all 11 templates currently found in the database:
multilayered, metal base, metal-base glitter, mesh decal, emissive mesh decal,
parallax mesh decal, one- and two-sided glass, parallax screen, signage, and
hologram. A malformed or genuinely unsupported material is reported as an
export failure; it is not silently replaced with a gray fallback.

Deterministic export failures are cached against the exporter/schema
fingerprint, so restarting a render does not repeatedly retry the same
unsupported mesh/appearance pairs.

On the development fixture, native Blender import of a six-submesh garment
took about 0.16 seconds, compared with about 0.75 seconds for add-on material
construction. Its first 512-pixel PBR bake took about 1.9 seconds; an identical
material-set cache hit took about 0.02 seconds. These timings are machine- and
cache-dependent.
Asset exports and renders are content-addressed. Changing the game archive,
`ghostline-red`, the RED schema, Blender, renderer script, appearance,
resolution, sample count, or view set creates a new cache entry instead of
silently reusing stale output.

The first pass renders the exact primary mesh and material appearance in its
exported bind pose. The database already retains complete component bundles;
neutral PMA/PWA mannequin composition and multi-component rendering are the
next fidelity stage. Offline rendering is not proof of in-game garment support,
cloth behavior, clipping, animation, LODs, or streaming.

## Gallery

Start the loopback-only gallery:

```powershell
py -B .\tools\item_database.py `
  --output .\converted\item-database `
  serve --open
```

The gallery searches localized titles, descriptions, record IDs, and game
tags. It filters by equipment slot, body frame, and built-in style/faction
tags, and exposes the authoritative record, controller appearance, mesh
appearance, mesh path, and expansion requirement on every card.

## Caption Jobs

Export rendered variants for a vision/captioning model:

```powershell
py -B .\tools\item_database.py `
  --output .\converted\item-database `
  caption-export `
  --file .\converted\item-database\caption-jobs.jsonl
```

Each JSONL row contains the image paths, localized text, frame/slot data,
authoritative game tags, and an empty constrained caption schema for colors,
materials, patterns, silhouette, style, character signals, coverage,
condition, and confidence. Keep model-derived tags separate from `game_tags`
and record the caption model and prompt version when results are imported.

## Validation

Run the focused tests with:

```powershell
py -B -m unittest tests.test_item_database -v
```

Before scaling to every variant, review a shader-validation set spanning
multilayer fabric, leather, metal, emissive, transparent, decal-heavy, and
hair-like materials. The baker preserves the source layers and texture maps,
but REDengine-specific animated and procedural shader behavior is represented
by a deterministic static PBR approximation.
