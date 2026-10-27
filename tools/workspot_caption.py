#!/usr/bin/env python3
"""Run auditable Qwen video caption jobs on the remote GPU; retain review state."""
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
from pathlib import Path
import time


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_caption(text):
    value = text.strip()
    if value.startswith("```"):
        value = value.split("\n", 1)[1].rsplit("```", 1)[0].strip()
    result = json.loads(value)
    required = {"observed_motion", "inferred_context", "unverified", "uncertainties"}
    if not isinstance(result, dict) or not required.issubset(result):
        raise ValueError("Caption lacks required evidence/inference fields")
    if not isinstance(result["observed_motion"], dict) or not isinstance(result["inferred_context"], dict):
        raise ValueError("Motion and context must be separate objects")
    return result


def prepare_inputs(processor, rows, root, frames):
    if isinstance(rows, dict):
        rows = [rows]
    conversations = []
    for row in rows:
        video = (root / row["video"]).resolve()
        context = {key: row[key] for key in ("limitations", "source_duration_seconds", "context") if key in row}
        text = row["prompt"] + "\nReturn concise JSON only.\nSource data: " + json.dumps(context, ensure_ascii=False)
        conversations.append([{"role": "user", "content": [{"type": "video", "path": str(video)}, {"type": "text", "text": text}]}])
    return processor.apply_chat_template(
        conversations, tokenize=True, padding=True, add_generation_prompt=True, enable_thinking=False,
        return_dict=True, return_tensors="pt", do_sample_frames=True, num_frames=frames, fps=None)


def semantic_identity(row, settings):
    """Reuse completed inputs across batch sizes while retaining original receipts."""
    keys = ("model", "revision", "dtype", "attention", "frames", "max_new_tokens", "enable_thinking", "do_sample", "video_size")
    data = {"job": row, "settings": {key: settings[key] for key in keys}}
    return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()


def trim_generated(tokens, eos_ids):
    for index, token in enumerate(tokens):
        if token in eos_ids:
            return tokens[:index], True
    return tokens, False


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--jobs", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--model", default="Qwen/Qwen3.8-27B")
    parser.add_argument("--revision", required=True, help="Pinned Hugging Face commit")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--frames", type=int, default=24)
    parser.add_argument("--max-new-tokens", type=int, default=1024)
    parser.add_argument("--use-kernels", action="store_true", help="Enable Transformers Hub kernels")
    parser.add_argument("--batch-size", type=int, default=1)
    args = parser.parse_args(argv)
    if args.frames < 2 or args.limit < 0 or args.max_new_tokens < 1 or args.batch_size < 1:
        parser.error("Invalid limit, frame count or token budget")
    jobs = [json.loads(line) for line in args.jobs.read_text(encoding="utf-8").splitlines() if line.strip()]
    if args.limit:
        jobs = jobs[:args.limit]
    # Validate all inputs before downloading or allocating model memory.
    for row in jobs:
        video = (args.jobs.parent / row["video"]).resolve()
        if not video.is_relative_to(args.jobs.parent.resolve()):
            raise ValueError("Video escapes job directory")
        if sha256(video) != row["media_sha256"][video.name]:
            raise ValueError(f"Video changed: {row['id']}")

    import torch
    import transformers
    from transformers import AutoProcessor, Qwen3_5ForConditionalGeneration

    settings = {"model": args.model, "revision": args.revision, "dtype": "bfloat16",
                "attention": "sdpa", "frames": args.frames, "max_new_tokens": args.max_new_tokens,
                "enable_thinking": False, "do_sample": False, "runner_sha256": sha256(Path(__file__)),
                "use_kernels": args.use_kernels,
                "batch_size": args.batch_size,
                "torch": torch.__version__, "transformers": transformers.__version__,
                "accelerate": importlib.metadata.version("accelerate"),
                "av": importlib.metadata.version("av"), "gpu": torch.cuda.get_device_name(0)}
    settings["kernel_packages"] = {}
    for package in ("flash-linear-attention", "fla-core", "causal-conv1d", "kernels"):
        try:
            settings["kernel_packages"][package] = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:
            settings["kernel_packages"][package] = None
    processor = AutoProcessor.from_pretrained(args.model, revision=args.revision)
    processor.tokenizer.padding_side = "left"
    processor.video_processor.size = {"shortest_edge": 4096, "longest_edge": args.frames * 640 * 360}
    settings["video_size"] = processor.video_processor.size
    existing = [json.loads(line) for line in args.output.read_text().splitlines()] if args.output.exists() else []
    done = {semantic_identity(r["input"], r["settings"]) for r in existing if r.get("status") == "captioned"}
    jobs = [row for row in jobs if semantic_identity(row, settings) not in done]
    if not jobs:
        print(json.dumps({"pending": 0}), flush=True)
        return 0
    if jobs:
        # Catch video/backend incompatibilities before allocating the full model.
        prepare_inputs(processor, jobs[:args.batch_size], args.jobs.parent, args.frames)
    started = time.monotonic()
    model = Qwen3_5ForConditionalGeneration.from_pretrained(
        args.model, revision=args.revision, dtype=torch.bfloat16,
        device_map={"": 0}, attn_implementation="sdpa", use_kernels=args.use_kernels)
    model.eval()
    print(json.dumps({"loaded_seconds": time.monotonic() - started, "settings": settings}), flush=True)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    eos_ids = model.generation_config.eos_token_id
    eos_ids = {eos_ids} if isinstance(eos_ids, int) else set(eos_ids or [])
    pending = [jobs[i:i + args.batch_size] for i in range(0, len(jobs), args.batch_size)]
    with args.output.open("a", encoding="utf-8") as output:
        while pending:
            rows = pending.pop(0)
            torch.cuda.reset_peak_memory_stats()
            started = time.monotonic()
            inputs = generated = None
            batch_error = None
            try:
                inputs = prepare_inputs(processor, rows, args.jobs.parent, args.frames).to(model.device)
                with torch.inference_mode():
                    generated = model.generate(**inputs, max_new_tokens=args.max_new_tokens, do_sample=False)
            except (ValueError, RuntimeError, KeyError) as error:
                batch_error = str(error)
            elapsed = time.monotonic() - started
            peak = torch.cuda.max_memory_allocated() / 2**30
            if batch_error and "out of memory" in batch_error.lower() and len(rows) > 1:
                del inputs, generated
                torch.cuda.empty_cache()
                middle = len(rows) // 2
                pending[0:0] = [rows[:middle], rows[middle:]]
                print(json.dumps({"oom_retry_batch_sizes": [middle, len(rows) - middle]}), flush=True)
                continue
            for index, row in enumerate(rows):
                identity = hashlib.sha256(json.dumps({"job": row, "settings": settings}, sort_keys=True).encode()).hexdigest()
                result = {"id": row["id"], "variant": row["variant"], "input_identity": identity,
                          "input": row, "settings": settings, "review_status": "model_suggested_unreviewed",
                          "batch_ids": [r["id"] for r in rows], "batch_seconds": elapsed,
                          "seconds": elapsed / len(rows), "peak_gpu_gib": peak}
                try:
                    if batch_error:
                        raise ValueError(batch_error)
                    trimmed, ended = trim_generated(generated[index, inputs["input_ids"].shape[-1]:].tolist(), eos_ids)
                    raw = processor.decode(trimmed, skip_special_tokens=True)
                    result.update(raw_response=raw, input_tokens=int(inputs["attention_mask"][index].sum()),
                                  padded_input_tokens=inputs["input_ids"].shape[-1], output_tokens=len(trimmed),
                                  video_grid_thw=[inputs["video_grid_thw"][index].tolist()],
                                  token_limit_reached=not ended and len(trimmed) >= args.max_new_tokens)
                    if result["token_limit_reached"]:
                        raise ValueError("Generation reached token limit; review raw response")
                    result["caption"] = parse_caption(raw)
                    result["status"] = "captioned"
                except ValueError as error:
                    result.update(status="failed", error=str(error))
                output.write(json.dumps(result, ensure_ascii=False) + "\n")
            output.flush()
            print(json.dumps({"batch_ids": [r["id"] for r in rows], "batch_seconds": elapsed,
                              "amortized_seconds": elapsed / len(rows), "peak_gpu_gib": peak,
                              "batch_error": batch_error}), flush=True)
            del inputs, generated
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
