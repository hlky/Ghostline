#!/usr/bin/env python3
"""Import vanilla-only layout fragments into the owned BD scene template.

This is a template-maintenance command, not part of normal quest generation.
Normal generation consumes ``braindance/templates`` without opening a
vanilla scene.
"""

from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TEMPLATE = (
    ROOT / "braindance/templates/braindance_analysis.scene.json"
)
DEFAULT_DONOR = (
    ROOT / ".tmp/vanilla-braindance/sq012_02a_braindance.scene.json"
)
RENDER_PRESET = (
    ROOT / "braindance/render_presets/q004_outdoor_bdview.json"
)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def walk(value: Any):
    yield value
    if isinstance(value, dict):
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def remap_handles(value: Any, first_id: int) -> None:
    next_id = first_id
    for item in walk(value):
        if isinstance(item, dict) and "HandleId" in item:
            item["HandleId"] = str(next_id)
            next_id += 1


def destination(node_id: int, *, ordinal: int = 1) -> dict[str, Any]:
    return {
        "$type": "scnInputSocketId",
        "isockStamp": {
            "$type": "scnInputSocketStamp",
            "name": 0,
            "ordinal": ordinal,
        },
        "nodeId": {"$type": "scnNodeId", "id": node_id},
    }


def prune_render_settings(preset: dict[str, Any]) -> dict[str, Any]:
    authored_fields = {
        "BloomAreaSettings": {
            "luminanceThresholdMax",
            "sceneColorScale",
            "bloomColorScale",
        },
        "ChromaticAberrationAreaSettings": {
            "chromaticAberrationEnabled",
            "chromaticAberrationSize",
            "chromaticAberrationExp",
        },
        "ColorGradingAreaSettings": {
            "saturation",
            "gammaValue",
            "gain",
            "ldrLut",
            "hdrLut",
            "forceHdrLut",
        },
        "ImageBasedFlareAreaSettings": {"scale"},
        "VolumetricFogAreaSettings": {
            "albedo",
            "range",
            "fogHeight",
            "density",
            "absorption",
            "ambientScale",
            "globalLightScale",
            "globalLightAnisotropy",
            "localLightRange",
        },
    }
    result = {"override": 1}
    for perspective in ("renderSettingsFPP", "renderSettingsTPP"):
        settings = copy.deepcopy(preset[perspective])
        for wrapper in settings["areaParameters"]:
            data = wrapper["Data"]
            keep = authored_fields[data["$type"]]
            wrapper["Data"] = {
                key: value
                for key, value in data.items()
                if key == "$type" or key in keep
            }
        result[perspective] = settings
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument("--donor", type=Path, default=DEFAULT_DONOR)
    args = parser.parse_args()

    document = load(args.template)
    donor = load(args.donor)
    root = document["Data"]["RootChunk"]
    graph = root["sceneGraph"]["Data"]["graph"]
    cleanup_ids = {527, 28, 34}
    graph[:] = [
        item
        for item in graph
        if item["Data"]["nodeId"]["id"] not in cleanup_ids
    ]
    donor_graph = donor["Data"]["RootChunk"]["sceneGraph"]["Data"]["graph"]
    by_id = {item["Data"]["nodeId"]["id"]: item for item in graph}
    donor_by_id = {
        item["Data"]["nodeId"]["id"]: item for item in donor_graph
    }

    cleanup = [
        copy.deepcopy(donor_by_id[node_id])
        for node_id in (527, 28, 34)
    ]
    max_handle = max(
        int(item["HandleId"])
        for item in walk(document)
        if isinstance(item, dict) and "HandleId" in item
    )
    remap_handles(cleanup, max_handle + 1)
    cleanup_by_id = {
        item["Data"]["nodeId"]["id"]: item["Data"] for item in cleanup
    }
    by_id[4576]["Data"]["outputSockets"][0]["destinations"] = [
        destination(527)
    ]
    cleanup_by_id[527]["outputSockets"][0]["destinations"] = [
        destination(28)
    ]
    cleanup_by_id[28]["outputSockets"][0]["destinations"] = [
        destination(34)
    ]
    cleanup_by_id[34]["outputSockets"][0]["destinations"] = [
        destination(2, ordinal=0)
    ]
    graph[-1:-1] = cleanup

    render = prune_render_settings(load(RENDER_PRESET))
    max_handle = max(
        int(item["HandleId"])
        for item in walk(document)
        if isinstance(item, dict) and "HandleId" in item
    )
    remap_handles(render, max_handle + 1)
    rewindable = by_id[20]["Data"]
    bdview = next(
        event["Data"]
        for event in rewindable["events"]
        if event["Data"].get("$type")
        == "scneventsBraindanceVisibilityEvent"
        and event["Data"]["performerId"]["id"] == 258
    )
    bdview.update(render)

    args.template.write_text(
        json.dumps(document, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "template": str(args.template.resolve()),
                "nodes": len(graph),
                "cleanup": [4576, 527, 28, 34, 2],
                "donor_used_only_for_import": str(args.donor.resolve()),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
