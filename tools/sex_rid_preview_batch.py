"""Resumably decode and render the vanilla sex RID review catalog."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Any

import sex_rid_preview as preview
from sex_rid_catalog import preview_slug


def _read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise preview.RidPreviewError(f"Expected a JSON object in {path}")
    return value


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, required=True)
    parser.add_argument("--rid-json-root", type=Path, required=True)
    parser.add_argument("--skeleton", type=Path, default=preview.DEFAULT_SKELETON)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--blender", type=Path)
    parser.add_argument("--family", action="append", default=[])
    parser.add_argument("--limit", type=int)
    parser.add_argument("--decode-only", action="store_true")
    parser.add_argument("--force", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    catalog = _read_json(args.catalog.resolve())
    skeleton = _read_json(args.skeleton.resolve())
    rid_root = args.rid_json_root.resolve()
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    entries = [
        entry
        for entry in catalog.get("entries", [])
        if not args.family or entry.get("inferred", {}).get("family") in args.family
    ]
    if args.limit is not None:
        entries = entries[: args.limit]
    report: dict[str, Any] = {
        "schema_version": 1,
        "kind": "ghostline_sex_rid_preview_batch",
        "jobs": [],
    }
    report_path = output_dir / "batch-report.json"

    for index, entry in enumerate(entries, start=1):
        rid_id = entry["id"]
        slug = preview_slug(rid_id)
        data_path = output_dir / f"{slug}.preview.json"
        video_path = output_dir / f"{slug}.mp4"
        contact_sheet_path = output_dir / f"{slug}.jpg"
        source_path = rid_root / Path(rid_id.replace("\\", "/") + ".json")
        job: dict[str, Any] = {
            "id": rid_id,
            "source": str(source_path),
            "status": "pending",
        }
        report["jobs"].append(job)
        try:
            if not source_path.is_file():
                raise preview.RidPreviewError(f"Missing serialized RID {source_path}")
            document = _read_json(source_path)
            actors = preview.select_human_actor_signatures(document, rid_id)
            job["actors"] = actors
            if not actors:
                job["status"] = "no_body_tracks"
                print(f"[{index}/{len(entries)}] no body tracks: {rid_id}", flush=True)
                preview._write_json(report_path, report)
                continue
            if (
                not args.force
                and data_path.is_file()
                and (
                    args.decode_only
                    or (video_path.is_file() and contact_sheet_path.is_file())
                )
            ):
                job["status"] = "ready" if video_path.is_file() else "decoded"
                print(f"[{index}/{len(entries)}] resume: {rid_id}", flush=True)
                preview._write_json(report_path, report)
                continue
            data = preview.build_preview_data(
                document, skeleton, rid_id, actor_signatures=set(actors)
            )
            preview._write_json(data_path, data)
            job["diagnostics"] = data["diagnostics"]
            job["status"] = "decoded"
            print(
                f"[{index}/{len(entries)}] decoded {rid_id} ({' + '.join(actors)})",
                flush=True,
            )
            if not args.decode_only:
                preview.render_preview(
                    data_path,
                    video_path,
                    contact_sheet_path,
                    blender=args.blender.resolve() if args.blender else None,
                )
                job["status"] = "ready"
                print(f"[{index}/{len(entries)}] rendered {rid_id}", flush=True)
        except (
            OSError,
            json.JSONDecodeError,
            preview.RidPreviewError,
            subprocess.CalledProcessError,
        ) as exc:
            job["status"] = "failed"
            job["error"] = str(exc)
            print(f"[{index}/{len(entries)}] failed {rid_id}: {exc}", flush=True)
        finally:
            preview._write_json(report_path, report)

    failed = sum(job["status"] == "failed" for job in report["jobs"])
    ready = sum(job["status"] in {"ready", "decoded"} for job in report["jobs"])
    print(f"Completed {ready}/{len(report['jobs'])} job(s); {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
