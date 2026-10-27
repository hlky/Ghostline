"""Bound Blender threads and PNG compression without changing scene or samples."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess

from artifact_io import atomic_write_json
from workspot_catalog import ROOT, digest, read


def producer_files():
    return {str(p): digest(p) for p in (Path(__file__), ROOT / "tools/workspot_preview_fast_blender.py")}


def render(job, preview, output, blender):
    from PIL import Image, ImageDraw
    folder = output / job["id"]
    folder.mkdir(parents=True, exist_ok=True)
    settings = {"factory_startup": True, "blender_threads": 2, "png_compression": 0}
    identity = hashlib.sha256(json.dumps([job, preview["provenance"], preview["skin_manifest"], settings, producer_files()], sort_keys=True).encode()).hexdigest()
    receipt = folder / "render.json"
    if receipt.is_file():
        old = read(receipt)
        if old.get("identity") == identity and len(old.get("outputs", {})) == 2 and all((folder / n).is_file() and digest(folder / n) == h for n, h in old["outputs"].items()):
            return old
    atomic_write_json(folder / "decoded.json", preview)
    frames = folder / "frames"
    frames.mkdir(exist_ok=True)
    command = [str(blender), "--background", "--factory-startup", "--threads", "2", "--python-exit-code", "1", "--python", str(ROOT / "tools/workspot_preview_fast_blender.py"),
               "--", "--input", str(folder / "decoded.json"), "--video", str(folder / "preview.mp4"), "--frames-dir", str(frames)]
    with (folder / "blender.log").open("w") as log:
        subprocess.run(command, check=True, stdout=log, stderr=subprocess.STDOUT)
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        raise ValueError("ffmpeg is required")
    with (folder / "ffmpeg.log").open("w") as log:
        subprocess.run([ffmpeg, "-y", "-threads", "2", "-framerate", str(preview["fps"]), "-start_number", "1", "-i", str(frames / "frame_%04d.png"),
                        "-frames:v", str(preview["frame_count"]), "-c:v", "libx264", "-threads", "2", "-crf", "20", "-pix_fmt", "yuv420p", str(folder / "preview.mp4")],
                       check=True, stdout=log, stderr=subprocess.STDOUT)
    sheet = Image.new("RGB", (960, 408), "#111820")
    draw = ImageDraw.Draw(sheet)
    for index in range(6):
        sample = round(index * (preview["frame_count"] - 1) / 5)
        with Image.open(frames / f"frame_{sample + 1:04d}.png") as picture:
            sheet.paste(picture.resize((320, 180)), ((index % 3) * 320, (index // 3) * 204))
        draw.text(((index % 3) * 320 + 8, (index // 3) * 204 + 183), f"t={preview['provenance']['sample_times_seconds'][sample]:.2f}s", fill="white")
    sheet.save(folder / "contact.png")
    result = {"identity": identity, "id": job["id"], "status": "rendered_proxy", "renderer": "skinned_source_mesh", "render_settings": settings,
              "outputs": {n: digest(folder / n) for n in ("preview.mp4", "contact.png")}, "provenance": preview["provenance"], "limitations": preview["limitations"]}
    atomic_write_json(receipt, result)
    return result
