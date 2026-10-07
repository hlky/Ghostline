# World Asset Discovery

Use `tools/index_world_assets.py` to index exact resource placements from
serialized sectors. It records node identity, transforms and depot paths;
it does not certify accessibility or quest safety.

```powershell
uv run python -B tools/index_world_assets.py --help
uv run python -B tools/index_world_assets.py build --help
uv run python -B tools/index_world_assets.py list --help
```

Use the [world-location capture workflow](world-locations.md) for deterministic
in-game destinations, runtime metadata, screenshots and review evidence.
The drop-point and indoor-candidate tools in the
[tool catalog](../reference/tool-catalog.md) provide focused research queries.
Preserve the source sector and node identity in the owning quest's world spec
when adopting a location; validate reachability and lifecycle in game.

The former `world_asset_catalog.py` sampled-catalog and offline direct/Godot
pipeline was retired. Its retained catalog and curation snapshots are historical
research, with the transition documented in
[retired world pipeline](../history/retired-world-pipeline.md). They are not
automatically regenerated or selected by the current tools.
