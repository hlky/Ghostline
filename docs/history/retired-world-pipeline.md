# Retired world discovery and offline database pipeline

Commit `2f8f7b7f85b1f4c0d62deb67aa60bcf96d9abc11` removed the old
`world_asset_catalog`, `world_location_database`, `world_location_dependencies`,
`world_location_direct`, six-tile proof-of-concept manifest, and Godot renderer.
That retirement removed 8,131 lines but left three importing test modules and
the old catalog schemas/commands. The September 2026 maintainability cleanup
removes those unsupported interfaces' remaining tests, schemas and active
instructions. Their historical implementations and tests remain available in
Git; they are not restored merely to make obsolete imports pass.

Current authoring uses:

- `tools/world_location_capture.py` and `tools/world_locations` for the in-game
  location database, capture evidence, planning and export;
- `tools/index_world_assets.py` for exact-resource placement indexes;
- `tools/index_drop_points.py` for reviewed delivery locations;
- `tools/indoor_location_candidates.py` and the Black Lantern scout for
  offline candidates and manually reviewed quest locations;
- the independent world geometry/navigation helpers and prepared-project
  Blender renderer where their existing contracts are useful.

The deleted pipeline's binary category discovery, automatic dependency-staged
six-tile database, and Godot rendering are retired capabilities. The current
commands do not claim to reproduce them. Existing reference catalogs and
curation are historical research inputs and are preserved until their source
and consumers are independently reviewed.

The active capture, index, geometry, navigation, renderer, scout and collision
tests remain in the regular suite. No active test was removed to hide a failed
assertion.
