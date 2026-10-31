"""Build an isolated performance-block catalogue preview; never install it."""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path

from generate_scene import build_scene, validate_scene
from scene_performance import CATALOG


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--spec", type=Path, default=Path("quests/examples/interaction-performance.scene-spec.json"))
    parser.add_argument("--out-root", type=Path, default=Path(".tmp/scene-performance-preview"))
    parser.add_argument("--deserialize", action="store_true")
    args = parser.parse_args()
    out = args.out_root.resolve()
    from project_layout import catalog
    repo = Path.cwd().resolve()
    layout = catalog(repo)
    if out == repo:
        raise ValueError("Repository root is not a preview project")
    for directory in [*layout.get("projects", {}).values(), *layout.get("template_roots", [])]:
        if out.is_relative_to((repo / directory / "source").resolve()):
            raise ValueError("Performance preview cannot write inside project or template source")
    spec = json.loads(args.spec.read_text(encoding="utf-8"))
    raw = out / "source/raw/mod/performance_preview/scenes/meeting.scene.json"
    binary = out / "source/archive/mod/performance_preview/scenes/meeting.scene"
    spec.update(raw_path=str(raw), archive_path=str(binary))
    scene = build_scene(spec)
    errors = validate_scene(scene, spec)
    if errors:
        raise ValueError("\n".join(errors))
    raw.parent.mkdir(parents=True, exist_ok=True)
    raw.write_text(json.dumps(scene, indent=2) + "\n", encoding="utf-8")
    if args.deserialize:
        from quest_build import convert_resource
        binary.parent.mkdir(parents=True, exist_ok=True)
        convert_resource(raw, binary, None, serializer="wolvenkit", wolvenkit=None)
    root = scene["Data"]["RootChunk"]
    events = Counter(e["Data"]["$type"] for n in root["sceneGraph"]["Data"]["graph"] for e in n["Data"].get("events", []))
    report = {"status": "structural-preview; not installed or runtime accepted", "spec": args.spec.as_posix(),
        "spec_sha256": sha(args.spec), "catalog_sha256": sha(CATALOG), "builder_sha256": sha(Path(__file__)),
        "validation_errors": errors, "events": dict(events), "nodes": len(root["sceneGraph"]["Data"]["graph"]),
        "cinematic_sets": len(root["resouresReferences"]["cinematicAnimSets"]),
        "raw": str(raw), "raw_sha256": sha(raw), "converted_and_typed_readback_verified": args.deserialize}
    if args.deserialize:
        report.update(binary=str(binary), binary_sha256=sha(binary))
    (out / "report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
