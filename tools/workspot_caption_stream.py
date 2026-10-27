#!/usr/bin/env python3
"""Upload completed render batches, then supervise captioning with mandatory shutdown."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import tarfile
import time

from artifact_io import atomic_write_json
from workspot_catalog import DEFAULT_OUTPUT, ROOT, digest, read
from workspot_preview_batch import caption_jobs

REMOTE = "/workspace/workspot-full"


def timestamp():
    return datetime.now(timezone.utc).isoformat()


def command(args, timeout=300, check=True):
    return subprocess.run(args, capture_output=True, text=True, timeout=timeout, check=check)


def ssh(alias, script, timeout=300, check=True):
    return command(["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=15", alias, script], timeout, check)


def write_manifest(path, rows):
    temporary = path.with_suffix(".next")
    temporary.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")
    temporary.replace(path)


def upload(args):
    out, alias = args.output.resolve(), args.alias
    folder = out / "full-batch"
    work = folder / "upload"
    work.mkdir(exist_ok=True)
    state = folder / "stream-state.json"
    manifest = folder / "uploaded-jobs.jsonl"
    uploaded = {row["id"]: row for row in (json.loads(s) for s in manifest.read_text(encoding="utf-8").splitlines())} if manifest.exists() else {}
    plan, catalog = read(folder / "plan.json"), read(out / "catalog.json")
    ssh(alias, f"mkdir -p {REMOTE}/inputs")
    try:
        while True:
            results = read(folder / "results.json")
            rows = caption_jobs(plan, results, catalog)
            pending = [r for r in rows if r["id"] not in uploaded]
            for start in range(0, len(pending), args.chunk_size):
                chunk = pending[start:start + args.chunk_size]
                archive = work / "upload-next.tar"
                with tarfile.open(archive, "w") as target:
                    for row in chunk:
                        for name, expected in row["media_sha256"].items():
                            if digest(out / "previews" / row["id"] / name) != expected:
                                raise ValueError(f"Changed render {row['id']}/{name}")
                        target.add(out / "previews" / row["video"], arcname=row["video"])
                    next_uploaded = {**uploaded, **{r["id"]: r for r in chunk}}
                    next_rows = [next_uploaded[j["id"]] for j in plan["jobs"] if j["id"] in next_uploaded]
                    next_manifest = work / "jobs.next.jsonl"
                    write_manifest(next_manifest, next_rows)
                    target.add(next_manifest, arcname=".jobs.next.jsonl")
                atomic_write_json(state, {"stage": "uploading", "updated_at": timestamp(), "uploaded": len(uploaded), "available": len(rows), "chunk": len(chunk)})
                command(["scp", "-q", str(archive), f"{alias}:{REMOTE}/upload-next.tar"], timeout=600)
                ssh(alias, f"tar -xf {REMOTE}/upload-next.tar -C {REMOTE}/inputs && mv {REMOTE}/inputs/.jobs.next.jsonl {REMOTE}/inputs/jobs.jsonl && rm {REMOTE}/upload-next.tar")
                uploaded = next_uploaded
                write_manifest(manifest, next_rows)
                archive.unlink()
                atomic_write_json(state, {"stage": "following_renders", "updated_at": timestamp(), "uploaded": len(uploaded), "available": len(rows), "jobs_sha256": digest(manifest)})
                print(json.dumps({"uploaded": len(uploaded), "available": len(rows)}), flush=True)
            render_state = read(folder / "state.json")
            if render_state["stage"] == "ready_for_captioning":
                # The final state may have appeared after this iteration's older
                # results snapshot. Re-read before sealing the upload manifest.
                final_rows = caption_jobs(plan, read(folder / "results.json"), catalog)
                final_by_id = {row["id"]: row for row in final_rows}
                if any(uploaded.get(key) != row for key, row in final_by_id.items()):
                    continue
                if set(uploaded) != set(final_by_id):
                    raise ValueError("Uploaded manifest differs from final successful render set")
                if len(final_rows) != render_state["caption_jobs"]:
                    raise ValueError("Final render state and result count disagree")
                marker = work / "UPLOAD_COMPLETE"
                atomic_write_json(marker, {"count": len(uploaded), "jobs_sha256": digest(manifest), "render_counts": render_state["counts"]})
                command(["scp", "-q", str(marker), f"{alias}:{REMOTE}/inputs/UPLOAD_COMPLETE.next"])
                ssh(alias, f"mv {REMOTE}/inputs/UPLOAD_COMPLETE.next {REMOTE}/inputs/UPLOAD_COMPLETE")
                atomic_write_json(state, {"stage": "complete", "updated_at": timestamp(), "uploaded": len(uploaded), "jobs_sha256": digest(manifest)})
                return
            if render_state["stage"] == "failed":
                raise RuntimeError(f"Renderer failed: {render_state.get('error')}")
            time.sleep(30)
    except Exception as error:
        atomic_write_json(state, {"stage": "failed", "updated_at": timestamp(), "uploaded": len(uploaded), "error": str(error)})
        raise


def stop_pod(pod_id):
    last_error = None
    for _ in range(3):
        try:
            command(["runpodctl", "pod", "stop", pod_id], timeout=60)
            raw = json.loads(command(["runpodctl", "pod", "get", pod_id, "--output", "json"], timeout=60).stdout)
            safe = {k: raw.get(k) for k in ("id", "desiredStatus", "lastStatusChange", "costPerHr")}
            if safe["desiredStatus"] == "EXITED":
                return safe
            last_error = str(safe)
        except Exception as error:
            last_error = str(error)
        time.sleep(5)
    raise RuntimeError(f"Unable to verify pod stopped: {last_error}")


def supervise(args):
    out, alias = args.output.resolve(), args.alias
    folder = out / "full-batch"
    state = folder / "caption-state.json"
    destination = out / "caption-results/full-run"
    destination.mkdir(parents=True, exist_ok=True)
    errors, status, stopped = [], None, None
    try:
        start_marker = getattr(args, "start_marker", None)
        if start_marker:
            atomic_write_json(state, {"stage": "waiting_for_handoff", "updated_at": timestamp(), "pod_id": args.pod_id})
            for _ in range(180):
                if start_marker.is_file():
                    break
                time.sleep(1)
            else:
                raise TimeoutError("Supervisor handoff marker did not arrive")
        for _ in range(180):
            ready = ssh(alias, f"test -f /workspace/CAPTION_ENV_READY && test -s {REMOTE}/inputs/jobs.jsonl", timeout=30, check=False)
            if ready.returncode == 0:
                break
            atomic_write_json(state, {"stage": "waiting_for_setup_or_upload", "updated_at": timestamp(), "pod_id": args.pod_id})
            time.sleep(10)
        else:
            raise TimeoutError("Caption environment or initial upload not ready after 30 minutes")
        for name in ("workspot_caption.py", "workspot_caption_vllm.py"):
            command(["scp", "-q", str(ROOT / "tools" / name), f"{alias}:{REMOTE}/{name}"])
        runner = (
            "export PATH=/workspace/vllm-venv/bin:/usr/local/cuda/bin:$PATH; "
            "export HF_HOME=/workspace/hf-cache OMP_NUM_THREADS=1 VLLM_USE_FLASHINFER_SAMPLER=0; "
            f"cp /workspace/vllm-requirements.lock.txt {REMOTE}/requirements.lock.txt; "
            f"/workspace/vllm-venv/bin/python -u {REMOTE}/workspot_caption_vllm.py "
            f"--jobs {REMOTE}/inputs/jobs.jsonl --output {REMOTE}/captions.jsonl "
            "--revision 1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0 --benchmark-size 0 "
            f"--batch-size {getattr(args, 'batch_size', 8)} "
            + (f"--tune-batches {args.tune_batches} --tune-size {args.tune_size} " if getattr(args, "tune_batches", "") else "") +
            f"--follow --complete-marker {REMOTE}/inputs/UPLOAD_COMPLETE "
            f"> {REMOTE}/batch.log 2>&1; result=$?; echo $result > {REMOTE}/runner-exit-code; exit $result"
        )
        atomic_write_json(state, {"stage": "captioning", "updated_at": timestamp(), "pod_id": args.pod_id})
        with (destination / "ssh-control.log").open("w") as log:
            process = subprocess.Popen(["ssh", "-o", "BatchMode=yes", "-o", "ServerAliveInterval=30", "-o", "ServerAliveCountMax=3", alias, runner], stdout=log, stderr=subprocess.STDOUT)
            status = process.wait()
        if status:
            errors.append(f"Caption SSH process exited {status}")
    except Exception as error:
        errors.append(str(error))
    finally:
        # Copy attempts are bounded; shutdown is required even if copying fails.
        copy_names = ["captions.jsonl", "batch.log", "requirements.lock.txt", "workspot_caption.py", "workspot_caption_vllm.py", "runner-exit-code"]
        if getattr(args, "tune_batches", ""):
            copy_names.append("batch-tuning.json")
        for name in copy_names:
            try:
                command(["scp", "-q", f"{alias}:{REMOTE}/{name}", str(destination / name)], timeout=90)
            except Exception as error:
                errors.append(f"Copy {name}: {error}")
        try:
            stopped = stop_pod(args.pod_id)
        except Exception as error:
            errors.append(str(error))
        counts = {}
        if (destination / "captions.jsonl").exists():
            for line in (destination / "captions.jsonl").read_text(encoding="utf-8").splitlines():
                record = json.loads(line)
                counts[record["status"]] = counts.get(record["status"], 0) + 1
        report = {"stage": "collected" if stopped and not errors else "needs_attention", "updated_at": timestamp(),
                  "exit_code": status, "counts": counts, "pod": stopped, "errors": errors, "review_status": "model_suggested_unreviewed"}
        atomic_write_json(state, report)
        atomic_write_json(folder / "caption-run-receipt.json", report)
        print(json.dumps(report), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("upload", "supervise"))
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--alias", required=True)
    parser.add_argument("--pod-id")
    parser.add_argument("--chunk-size", type=int, default=512)
    parser.add_argument("--batch-size", type=int, default=8)
    parser.add_argument("--tune-batches", default="")
    parser.add_argument("--tune-size", type=int, default=32)
    parser.add_argument("--start-marker", type=Path)
    args = parser.parse_args()
    if args.chunk_size < 1 or (args.command == "supervise" and not args.pod_id):
        parser.error("Positive chunk size and supervisor pod ID are required")
    upload(args) if args.command == "upload" else supervise(args)


if __name__ == "__main__":
    main()
