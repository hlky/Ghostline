"""Snapshot category queues into the next geographically routed camera survey."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import shutil

from world_locations.config import load_config, output_paths
from world_locations.protocol import atomic_write_json
from world_locations.survey import prepare_survey


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-root", type=Path, default=Path("converted/world-location-database/category-runs/survey-v2"))
    parser.add_argument("--config-output", type=Path, default=Path("tools/world-location-capture-survey-v2.json"))
    args = parser.parse_args()
    presets = sorted(p for p in Path("tools").glob("world-location-capture-*-v1.json") if load_config(p).get("workspace", {}).get("active_category"))
    if not presets:
        raise SystemExit("No category presets found")
    configs = [load_config(p) for p in presets]
    paths = [output_paths(c) for c in configs]
    result = prepare_survey(args.output_root.resolve() / "locations.sqlite3", [p["database"] for p in paths], configs[0])
    config = {k: v for k, v in configs[0].items() if not k.startswith("_")}
    config["output_root"] = str(args.output_root).replace("\\", "/")
    config["workspace"] = {"active_category": None, "survey_version": 2, "capture_history": "source snapshots retained", "geometry_policy": "context sweeps and elevated parking; actual camera readback; global route"}
    config["capture"].update(survey_runtime_required=True, loading_wait_seconds=30, readiness_timeout_seconds=40, visual_timeout_seconds=35, scene_stability_threshold=0.04, position_tolerance_m=0.75, angle_tolerance_degrees=2.0)
    config["capture"]["survey"] = {"local_move_maximum_m": 20, "local_move_speed_mps": 10, "near_obstruction_m": 2.5, "maximum_recoveries": 2}
    config["obstruction_recovery"] = {"lateral_offsets_m": [1.5, -1.5, 2.0, -2.0]}
    args.config_output.parent.mkdir(parents=True, exist_ok=True)
    atomic_write_json(args.config_output, config)
    for sub in ("runtime", "reports", "captures", "exports"):
        (args.output_root / sub).mkdir(exist_ok=True)
    descriptor = next((p["runtime"] / "cet-runtime.json" for p in paths if (p["runtime"] / "cet-runtime.json").exists()), None)
    if descriptor:
        shutil.copyfile(descriptor, args.output_root / "runtime/cet-runtime.json")
    atomic_write_json(args.output_root / "capture-config.json", config)
    atomic_write_json(args.output_root / "reports/survey-manifest.json", result)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
