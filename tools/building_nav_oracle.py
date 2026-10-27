"""Load generated VAND tiles with an explicitly adapted upstream Detour oracle.

Requires a local official recastnavigation checkout and clang++. The checkout
is read-only: headers/sources are copied into generated build output. Adaptations
are polygon capacity 3, version 8, 64-bit poly refs and 64-bit offmesh user IDs.
Success is offline compatibility evidence, not game AI integration evidence.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
from pathlib import Path
import shutil
import subprocess

from artifact_io import atomic_write_json
from building_builder import CACHE, ROOT, compile_layout, world_point
from building_navigation import navigation_resource


def build_oracle(source, build):
    source, build = Path(source).resolve(), Path(build).resolve()
    build.mkdir(parents=True, exist_ok=True)
    for name in ("Include", "Source"):
        shutil.copytree(source / "Detour" / name, build / name, dirs_exist_ok=True)
    header = build / "Include/DetourNavMesh.h"
    text = header.read_text(encoding="utf-8")
    for before, after in (("DT_VERTS_PER_POLYGON = 6", "DT_VERTS_PER_POLYGON = 3"),
                          ("DT_NAVMESH_VERSION = 7", "DT_NAVMESH_VERSION = 8")):
        if before not in text:
            raise ValueError("Unexpected upstream Detour constants; inspect this revision before adapting it")
        text = text.replace(before, after)
    start, end = text.index("struct dtOffMeshConnection"), text.index("struct dtMeshHeader")
    part = text[start:end]
    if "unsigned int userId;" not in part:
        raise ValueError("Unexpected upstream offmesh user ID layout")
    text = text[:start] + part.replace("unsigned int userId;", "uint64_t userId;") + text[end:]
    header.write_text(text, encoding="utf-8")
    executable = build / "building-nav-oracle.exe"
    compiler = shutil.which("clang++")
    if not compiler:
        raise ValueError("clang++ was not found")
    subprocess.run([compiler, "-std=c++17", "-O2", "-DDT_POLYREF64=1", "-I" + str(build / "Include"),
                    str(ROOT / "tools/building_nav_oracle.cpp"), *map(str, sorted((build / "Source").glob("*.cpp"))),
                    "-o", str(executable)], check=True, capture_output=True, text=True, timeout=180)
    revision = subprocess.run(["git", "-C", str(source), "rev-parse", "HEAD"], check=True, capture_output=True, text=True).stdout.strip()
    atomic_write_json(build / "oracle-build.json", {"upstream": "https://github.com/recastnavigation/recastnavigation", "revision": revision,
                      "adaptations": ["DT_VERTS_PER_POLYGON=3", "DT_NAVMESH_VERSION=8", "DT_POLYREF64=1", "dtOffMeshConnection.userId=uint64_t"],
                      "executable_sha256": hashlib.sha256(executable.read_bytes()).hexdigest(), "compiler": compiler})
    return executable


def check(executable, scene, start, end, output, extra_tiles=()):
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    resource = navigation_resource(scene)
    paths = []
    for index, buffer in enumerate(resource["tileBuffers"]):
        path = output / f"tile-{index}.vand"
        path.write_bytes(base64.b64decode(buffer["Bytes"]))
        paths.append(path)
    from world_location_nav import decode_vnav_buffer
    for path in extra_tiles:
        decode_vnav_buffer(Path(path).read_bytes())
        paths.append(Path(path).resolve())
    world_start, world_end = [world_point(point, scene["layout"]["origin"]) for point in (start, end)]
    coordinates = [v for p in (world_start, world_end) for v in (p[0], p[2], p[1])]
    result = subprocess.run([str(executable), str(len(paths)), *map(str, paths), *map(str, coordinates)], check=True, capture_output=True, text=True, timeout=30)
    report = {**json.loads(result.stdout), "runtime_verified": False, "method": "adapted upstream Detour", "tiles": len(paths), "start": start, "end": end}
    atomic_write_json(output / "result.json", report)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("layout", type=Path)
    parser.add_argument("--recast-source", type=Path, required=True)
    parser.add_argument("--start", nargs=3, type=float, required=True)
    parser.add_argument("--end", nargs=3, type=float, required=True)
    parser.add_argument("--out", type=Path, default=CACHE / "oracle")
    parser.add_argument("--extra-tile", action="append", type=Path, default=[])
    args = parser.parse_args()
    executable = build_oracle(args.recast_source, args.out / "build")
    scene = compile_layout(json.loads(args.layout.read_bytes()))
    print(json.dumps(check(executable, scene, args.start, args.end, args.out / "check", args.extra_tile), indent=2))


if __name__ == "__main__":
    main()
