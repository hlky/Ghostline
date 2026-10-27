#!/usr/bin/env python3
"""Continuously batch source-bound workspot videos with vLLM's offline chat API."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time

from workspot_caption import parse_caption, sha256


def messages(row, root):
    video = (root / row["video"]).resolve()
    context = {key: row[key] for key in ("limitations", "source_duration_seconds", "context") if key in row}
    # Shared clips can have hundreds of workspot associations. Preserve every
    # association in the stored input, but bound the metadata sent to the model.
    if isinstance(context.get("context"), dict):
        supplied = context["context"]
        spots = supplied.get("workspots", [])
        selected, used = [], 0
        for spot in spots:
            length = len(json.dumps(spot, ensure_ascii=False))
            if len(selected) >= 4 or used + length > 6000:
                break
            selected.append(spot)
            used += length
        context["context"] = {**supplied, "workspots": selected,
                              "additional_workspot_associations_omitted": len(spots) - len(selected)}
    text = row["prompt"] + "\nReturn concise JSON only.\nSource data: " + json.dumps(context, ensure_ascii=False)
    return [{"role": "user", "content": [
        {"type": "video_url", "video_url": {"url": video.as_uri()}},
        {"type": "text", "text": text},
    ]}]


def completed(row, records, model, revision, frames, max_new_tokens=1024):
    return any(r.get("status") == "captioned" and r.get("input") == row
               and r["settings"]["model"] == model and r["settings"]["revision"] == revision
               and r["settings"]["frames"] == frames
               and r["settings"]["max_new_tokens"] == max_new_tokens for r in records)


def load_jobs(path, root):
    jobs = [json.loads(s) for s in path.read_text().splitlines() if s.strip()]
    for row in jobs:
        video = (root / row["video"]).resolve()
        if not video.is_relative_to(root) or sha256(video) != row["media_sha256"][video.name]:
            raise ValueError(f"Invalid or changed video {row['id']}")
    return jobs


def job_identity(row):
    return hashlib.sha256(json.dumps(row, sort_keys=True).encode()).hexdigest()


def uploads_complete(marker_path, jobs_path, count):
    if not marker_path.exists():
        return False
    marker = json.loads(marker_path.read_text())
    if marker.get("jobs_sha256") != sha256(jobs_path) or marker.get("count") != count:
        raise ValueError("Upload completion marker does not match the final manifest")
    return True


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--jobs", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--model", default="Qwen/Qwen3.8-27B")
    p.add_argument("--revision", required=True)
    p.add_argument("--batch-size", type=int, default=8)
    p.add_argument("--benchmark-size", type=int, default=4)
    p.add_argument("--frames", type=int, default=24)
    p.add_argument("--max-new-tokens", type=int, default=1024)
    p.add_argument("--follow", action="store_true", help="Read atomic manifest updates between upload batches")
    p.add_argument("--complete-marker", type=Path)
    p.add_argument("--idle-timeout", type=float, default=300)
    p.add_argument("--tune-batches", default="", help="Comma-separated request batch sizes; engine capacity is --batch-size")
    p.add_argument("--tune-size", type=int, default=32)
    args = p.parse_args(argv)
    if args.batch_size < 1 or args.frames < 2 or args.max_new_tokens < 1 or args.benchmark_size < 0:
        p.error("Invalid batch, frame or token setting")
    if args.follow and (args.complete_marker is None or args.idle_timeout <= 0):
        p.error("Follow mode requires a completion marker and positive idle timeout")
    tune_batches = [int(s) for s in args.tune_batches.split(",") if s]
    if any(n < 1 or n > args.batch_size for n in tune_batches) or args.tune_size < 1:
        p.error("Tuning sizes must be positive and within engine batch capacity")
    root = args.jobs.parent.resolve()
    jobs = load_jobs(args.jobs, root)
    existing = [json.loads(s) for s in args.output.read_text().splitlines()] if args.output.exists() else []
    by_id = {}
    for row in existing:
        by_id.setdefault(row["id"], []).append(row)
    remaining = [r for r in jobs if not completed(r, by_id.get(r["id"], []), args.model, args.revision, args.frames, args.max_new_tokens)]
    if not remaining and not args.benchmark_size:
        return 0

    import vllm
    import torch
    from vllm import LLM, SamplingParams

    settings = {"backend": "vllm", "model": args.model, "revision": args.revision,
                "dtype": "bfloat16", "frames": args.frames, "batch_size": args.batch_size,
                "max_new_tokens": args.max_new_tokens, "enable_thinking": False,
                "temperature": 0, "max_model_len": 8192, "gpu_memory_utilization": 0.90,
                "flashinfer_sampler": os.environ.get("VLLM_USE_FLASHINFER_SAMPLER", "auto"),
                "omp_num_threads": os.environ.get("OMP_NUM_THREADS"),
                "context_policy": "first_4_associations_max_6000_characters_complete_input_retained",
                "follow_uploads": args.follow,
                "engine_max_num_seqs": args.batch_size,
                "video_size": {"shortest_edge": 4096, "longest_edge": args.frames * 640 * 360},
                "vllm": vllm.__version__, "torch": torch.__version__,
                "runner_sha256": sha256(Path(__file__)), "helper_sha256": sha256(Path(__file__).with_name("workspot_caption.py"))}
    started = time.monotonic()
    llm = LLM(model=args.model, revision=args.revision, dtype="bfloat16",
              max_model_len=8192, gpu_memory_utilization=0.90,
              max_num_seqs=args.batch_size, max_num_batched_tokens=8192,
              allowed_local_media_path=str(root),
              limit_mm_per_prompt={"image": 0, "video": {"count": 1, "num_frames": args.frames, "width": 640, "height": 360}},
              media_io_kwargs={"video": {"num_frames": args.frames}},
              mm_processor_kwargs={"size": settings["video_size"], "do_sample_frames": False})
    print(json.dumps({"loaded_seconds": time.monotonic() - started, "settings": settings}), flush=True)
    params = SamplingParams(temperature=0, max_tokens=args.max_new_tokens)
    args.output.parent.mkdir(parents=True, exist_ok=True)

    def run(rows, path, phase):
        started = time.monotonic()
        try:
            outputs = llm.chat([messages(row, root) for row in rows], sampling_params=params,
                               chat_template_kwargs={"enable_thinking": False}, use_tqdm=True)
        except ValueError as error:
            # Isolate an invalid media/context request without losing its neighbors.
            # Engine/runtime errors propagate so the supervisor can shut the GPU down.
            if len(rows) > 1:
                middle = len(rows) // 2
                run(rows[:middle], path, phase)
                run(rows[middle:], path, phase)
            else:
                row = rows[0]
                with path.open("a", encoding="utf-8") as target:
                    target.write(json.dumps({"id": row["id"], "variant": row["variant"], "input": row,
                                             "settings": settings, "status": "failed", "error": str(error),
                                             "review_status": "model_suggested_unreviewed"}, ensure_ascii=False) + "\n")
                print(json.dumps({"phase": phase, "id": row["id"], "error": str(error)}), flush=True)
            return
        elapsed = time.monotonic() - started
        if len(outputs) != len(rows):
            raise RuntimeError("Output count differs from input count")
        accepted = 0
        with path.open("a", encoding="utf-8") as target:
            for row, output in zip(rows, outputs, strict=True):
                answer = output.outputs[0]
                result = {"id": row["id"], "variant": row["variant"], "input": row,
                          "input_identity": hashlib.sha256(json.dumps({"job": row, "settings": settings}, sort_keys=True).encode()).hexdigest(),
                          "settings": settings, "batch_ids": [r["id"] for r in rows],
                          "request_batch_size": len(rows),
                          "batch_seconds": elapsed, "seconds": elapsed / len(rows),
                          "raw_response": answer.text, "output_tokens": len(answer.token_ids),
                          "input_tokens": len(output.prompt_token_ids), "finish_reason": answer.finish_reason,
                          "review_status": "model_suggested_unreviewed"}
                try:
                    if answer.finish_reason == "length":
                        raise ValueError("Generation reached token limit")
                    result.update(caption=parse_caption(answer.text), status="captioned")
                    accepted += 1
                except ValueError as error:
                    result.update(status="failed", error=str(error))
                target.write(json.dumps(result, ensure_ascii=False) + "\n")
                target.flush()
        print(json.dumps({"phase": phase, "clips": len(rows), "accepted": accepted,
                          "batch_seconds": elapsed, "amortized_seconds": elapsed / len(rows),
                          "output_tokens": sum(len(r.outputs[0].token_ids) for r in outputs)}), flush=True)

    if args.benchmark_size:
        run(jobs[:args.benchmark_size], args.output.with_name("vllm-benchmark.jsonl"), "benchmark")
    if tune_batches:
        sample = jobs[:args.tune_size]
        # One warmup excludes first-request overhead from the measured comparison.
        run(sample[:min(4, len(sample))], args.output.with_name("tuning-warmup.jsonl"), "tuning_warmup")
        measurements = []
        for size in tune_batches:
            # The same clips repeat across rounds. Clear prompt and multimodal
            # caches so larger batches do not receive a warmed-input advantage.
            if not llm.reset_prefix_cache():
                raise RuntimeError("Could not reset prefix cache before tuning round")
            llm.reset_mm_cache()
            target = args.output.with_name(f"tuning-batch-{size}.jsonl")
            if target.exists():
                target = target.with_name(f"tuning-batch-{size}-{int(time.time())}.jsonl")
            started = time.monotonic()
            for start in range(0, len(sample), size):
                run(sample[start:start + size], target, f"tuning_{size}")
            elapsed = time.monotonic() - started
            records = [json.loads(s) for s in target.read_text().splitlines()]
            accepted = sum(r["status"] == "captioned" for r in records)
            memory = subprocess.run(["nvidia-smi", "--query-gpu=memory.used", "--format=csv,noheader,nounits"], capture_output=True, text=True, check=True)
            measurement = {"batch_size": size, "clips": len(sample), "accepted": accepted,
                           "seconds": elapsed, "seconds_per_clip": elapsed / len(sample),
                           "output_tokens_per_second": sum(r.get("output_tokens", 0) for r in records) / elapsed,
                           "device_memory_used_mib": int(memory.stdout.strip().splitlines()[0]),
                           "results": target.name}
            measurements.append(measurement)
            print(json.dumps({"tuning_result": measurement}), flush=True)
        valid = [m for m in measurements if m["accepted"] == len(sample)]
        if not valid:
            raise RuntimeError("No tuning batch passed every caption validation")
        chosen = min(valid, key=lambda m: m["seconds_per_clip"])
        args.batch_size = chosen["batch_size"]
        settings["batch_size"] = args.batch_size
        settings["selected_by_tuning"] = True
        report = {"measurements": measurements, "chosen_batch_size": args.batch_size,
                  "engine_max_num_seqs": settings["engine_max_num_seqs"], "sample_ids": [r["id"] for r in sample],
                  "cache_policy": "prefix_and_multimodal_caches_reset_before_each_round"}
        args.output.with_name("batch-tuning.json").write_text(json.dumps(report, indent=2))
        print(json.dumps({"selected_batch_size": args.batch_size}), flush=True)
    remaining_keys = {job_identity(row) for row in remaining}
    attempted = {job_identity(row) for row in jobs} - remaining_keys
    idle_since = time.monotonic()
    while True:
        for start in range(0, len(remaining), args.batch_size):
            chunk = remaining[start:start + args.batch_size]
            run(chunk, args.output, "batch")
            attempted.update(job_identity(row) for row in chunk)
            idle_since = time.monotonic()
        if not args.follow:
            break
        jobs = load_jobs(args.jobs, root)
        remaining = [row for row in jobs if job_identity(row) not in attempted]
        if remaining:
            continue
        if uploads_complete(args.complete_marker, args.jobs, len(jobs)):
            print(json.dumps({"upload_complete": True, "jobs": len(jobs)}), flush=True)
            break
        if time.monotonic() - idle_since >= args.idle_timeout:
            raise TimeoutError("No new uploaded jobs before idle timeout; exit for pod shutdown")
        time.sleep(5)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
