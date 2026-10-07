#!/usr/bin/env python3
"""Retarget an offline NVIDIA Kimodo BVH into a Ghostline BD actor.

This wrapper deliberately keeps generated motion outside the checked scene
specification.  It can rebuild the deterministic base scene, apply a Kimodo
clip to one existing actor, and rebake the normal braindance handoff manifest.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

from toolchain import default_tool_path, resolve_tool

from braindance_scene import DEFAULT_SPEC


ROOT = Path(__file__).resolve().parents[1]
BLENDER_RUNNER = Path(__file__).with_name("kimodo_braindance_blender.py")
SCENE_TOOL = Path(__file__).with_name("braindance_scene.py")
DEFAULT_BLENDER = default_tool_path("blender")

JOINT_RE = re.compile(r"^\s*(?:ROOT|JOINT)\s+([^\s{]+)")
FRAMES_RE = re.compile(r"^\s*Frames:\s*(\d+)\s*$", re.IGNORECASE)


class KimodoRetargetError(RuntimeError):
    """Raised when a Kimodo-to-braindance retarget cannot be prepared."""


def inspect_bvh(path: Path) -> tuple[tuple[str, ...], int]:
    """Return declared joint names and frame count from a text BVH file."""
    try:
        lines = path.read_text(encoding="utf-8", errors="strict").splitlines()
    except FileNotFoundError as exc:
        raise KimodoRetargetError(f"BVH does not exist: {path}") from exc
    joints: list[str] = []
    frame_count: int | None = None
    for line in lines:
        joint_match = JOINT_RE.match(line)
        if joint_match:
            joints.append(joint_match.group(1))
        frame_match = FRAMES_RE.match(line)
        if frame_match:
            frame_count = int(frame_match.group(1))
    if not joints:
        raise KimodoRetargetError(f"BVH declares no ROOT or JOINT entries: {path}")
    if frame_count is None or frame_count <= 0:
        raise KimodoRetargetError(f"BVH has no positive Frames declaration: {path}")
    return tuple(joints), frame_count


def load_spec(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise KimodoRetargetError(f"Braindance spec does not exist: {path}") from exc
    except json.JSONDecodeError as exc:
        raise KimodoRetargetError(f"Invalid braindance spec {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise KimodoRetargetError(f"Braindance spec root must be an object: {path}")
    return value


def resolve_repo_path(value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else ROOT / path


def find_actor(spec: dict, actor_id: str) -> dict:
    actors = spec.get("actors", [])
    matches = [actor for actor in actors if isinstance(actor, dict) and actor.get("id") == actor_id]
    if len(matches) != 1:
        raise KimodoRetargetError(
            f"Spec must contain exactly one actor with id {actor_id!r}; found {len(matches)}"
        )
    return matches[0]


def build_blender_command(
    blender: Path,
    *,
    blend: Path,
    output_blend: Path,
    bvh: Path,
    actor: str,
    start_frame: int,
    end_frame: int,
    blend_in: int,
    blend_out: int,
    report: Path,
) -> list[str]:
    return [
        str(blender),
        "--background",
        str(blend),
        "--python",
        str(BLENDER_RUNNER),
        "--",
        "--bvh",
        str(bvh),
        "--actor",
        actor,
        "--start-frame",
        str(start_frame),
        "--end-frame",
        str(end_frame),
        "--blend-in",
        str(blend_in),
        "--blend-out",
        str(blend_out),
        "--output-blend",
        str(output_blend),
        "--report",
        str(report),
    ]


def run_checked(command: list[str], *, marker: str | None = None) -> None:
    completed = subprocess.run(
        command,
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if completed.stdout:
        print(completed.stdout, end="")
    if completed.stderr:
        print(completed.stderr, end="", file=sys.stderr)
    if completed.returncode != 0 or (marker and marker not in completed.stdout):
        raise KimodoRetargetError(
            f"Command failed with exit code {completed.returncode}: {' '.join(command)}"
        )


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--spec", type=Path, default=DEFAULT_SPEC)
    parser.add_argument("--bvh", type=Path, required=True)
    parser.add_argument("--actor", default="patch")
    parser.add_argument("--start-frame", type=int, default=0)
    parser.add_argument("--end-frame", type=int)
    parser.add_argument("--blend-in", type=int, default=8)
    parser.add_argument("--blend-out", type=int, default=15)
    parser.add_argument("--blender", type=Path, default=DEFAULT_BLENDER)
    parser.add_argument("--output-blend", type=Path)
    parser.add_argument("--report", type=Path)
    parser.add_argument(
        "--build-before",
        action="store_true",
        help="Rebuild the deterministic base .blend before applying Kimodo motion",
    )
    parser.add_argument(
        "--bake-after",
        action="store_true",
        help="Rebake the existing spec outputs and handoff after retargeting",
    )
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        spec_path = args.spec.resolve()
        spec = load_spec(spec_path)
        find_actor(spec, args.actor)
        bvh = args.bvh.resolve()
        joints, frame_count = inspect_bvh(bvh)
        required_source = {"Hips", "Spine1", "LeftArm", "RightArm", "LeftLeg", "RightLeg"}
        missing_source = sorted(required_source - set(joints))
        if missing_source:
            raise KimodoRetargetError(
                "BVH is not the expected Kimodo SOMA hierarchy; missing: "
                + ", ".join(missing_source)
            )
        outputs = spec.get("outputs", {})
        if not isinstance(outputs, dict) or not isinstance(outputs.get("blend"), str):
            raise KimodoRetargetError("Spec outputs.blend must be a path")
        blend = resolve_repo_path(outputs["blend"]).resolve()
        output_blend = (args.output_blend or blend).resolve()
        if args.bake_after and output_blend != blend:
            raise KimodoRetargetError(
                "--bake-after requires output to overwrite the spec's existing .blend"
            )
        report = (
            args.report.resolve()
            if args.report
            else output_blend.with_suffix(".kimodo.json")
        )
        scene_start = int(spec.get("frames", {}).get("start", 0))
        scene_end = int(spec.get("frames", {}).get("end", 0))
        start_frame = args.start_frame
        end_frame = args.end_frame
        if end_frame is None:
            end_frame = min(scene_end, start_frame + frame_count - 1)
        if start_frame < scene_start or end_frame > scene_end or end_frame < start_frame:
            raise KimodoRetargetError(
                f"Destination range {start_frame}..{end_frame} is outside scene "
                f"{scene_start}..{scene_end}"
            )
        destination_count = end_frame - start_frame + 1
        if destination_count > frame_count:
            raise KimodoRetargetError(
                f"Destination needs {destination_count} frames but BVH has {frame_count}"
            )
        if min(args.blend_in, args.blend_out) < 0:
            raise KimodoRetargetError("Blend lengths cannot be negative")
        if args.blend_in + args.blend_out >= destination_count:
            raise KimodoRetargetError("Blend-in plus blend-out must be shorter than the clip")
        try:
            blender = resolve_tool("blender", args.blender)
        except (OSError, ValueError) as exc:
            raise KimodoRetargetError(str(exc)) from exc

        base_build = [
            sys.executable,
            str(SCENE_TOOL),
            "build",
            "--spec",
            str(spec_path),
            "--blender",
            str(blender),
        ]
        retarget = build_blender_command(
            blender,
            blend=blend,
            output_blend=output_blend,
            bvh=bvh,
            actor=args.actor,
            start_frame=start_frame,
            end_frame=end_frame,
            blend_in=args.blend_in,
            blend_out=args.blend_out,
            report=report,
        )
        bake = [
            sys.executable,
            str(SCENE_TOOL),
            "bake",
            "--spec",
            str(spec_path),
            "--blender",
            str(blender),
        ]
        plan = {
            "spec": str(spec_path),
            "actor": args.actor,
            "bvh": str(bvh),
            "source_frames": frame_count,
            "destination_frames": [start_frame, end_frame],
            "blend": str(blend),
            "output_blend": str(output_blend),
            "report": str(report),
            "commands": ([base_build] if args.build_before else [])
            + [retarget]
            + ([bake] if args.bake_after else []),
        }
        if args.dry_run:
            print(json.dumps(plan, indent=2))
            return 0
        if args.build_before:
            run_checked(base_build)
        if not blend.is_file():
            raise KimodoRetargetError(
                f"Base blend does not exist: {blend}; pass --build-before"
            )
        run_checked(retarget, marker="GHOSTLINE_KIMODO_RETARGET_COMPLETE ")
        if args.bake_after:
            run_checked(bake)
        print(json.dumps({"ok": True, **plan}, indent=2))
        return 0
    except KimodoRetargetError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
