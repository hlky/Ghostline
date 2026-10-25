"""Round-trip and audit the native VelvetCrash resource graph."""
from __future__ import annotations

import base64
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import struct

from PIL import Image

from build import PREFIX, PROJECT, REPO, frame_tracks, run, validate_tweaks
from artifact_io import atomic_write_json
from package_manifest import build_manifest, read_tweak_dependencies, resource_strings
from toolchain import default_tool_path


def nodes(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from nodes(child)
    elif isinstance(value, list):
        for child in value:
            yield from nodes(child)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def audit(root: Path = PROJECT) -> dict:
    archive = root / "source/archive"
    work = root / "generated/verification"
    work.mkdir(parents=True, exist_ok=True)
    spec = json.loads((PROJECT / "velvet_crash.fx.json").read_text())
    red = default_tool_path("ghostline_red")

    def serialize(path):
        depot = path.relative_to(archive).as_posix()
        output = work / (depot + ".json")
        output.parent.mkdir(parents=True, exist_ok=True)
        run([str(red), "cr2w-serialize", str(path), str(output), "--schema", str(REPO / "red-schema.json")],
            work / (path.name + ".log"))
        return depot, json.loads(output.read_text())["Data"]["RootChunk"]

    with ThreadPoolExecutor(max_workers=3) as pool:
        packed = dict(pool.map(serialize, sorted(archive.rglob("*.*"))))
    sequence = frame_tracks(spec)
    layer_sequence = [(suffix + ("_bows" if layer == "bows" else ""), begin, duration, layer)
                      for suffix, begin, duration in sequence for layer in ("hearts", "bows")]
    require(len(packed) == 12 * len(sequence) + 5, "Missing separate bow/heart frame particles or colour/mask textures")
    for depot, texture in packed.items():
        if not depot.endswith(".xbm"):
            continue
        require(texture["width"] == texture["height"] == spec["texture_resolution"], "Wrong glyph texture dimensions")
        blob = texture["renderTextureResource"]["renderResourceBlobPC"]["Data"]
        pixels = base64.b64decode(blob["textureData"]["Bytes"])
        # WolvenKit imports raw RGBA8 with vertically flipped mip zero.
        with Image.open(root / "source/raw" / (depot.removesuffix(".xbm") + ".png")) as image:
            expected = image.convert("RGBA").transpose(Image.Transpose.FLIP_TOP_BOTTOM).tobytes()
            if depot.endswith("_d.xbm"):
                mask_path = root / "source/raw" / (depot.removesuffix("_d.xbm") + "_m.png")
                with Image.open(mask_path) as mask:
                    require(all(channel.tobytes() == image.getchannel("A").tobytes() for channel in mask.split()),
                            f"Black glyph opacity depends on colour: {depot}")
        require(pixels[:len(expected)] == expected, f"Texture pixels or transparency changed: {depot}")
    for variant in ("v", "npc"):
        fx = packed[f"{PREFIX}/fx/velvet_crash_{variant}.effect"]
        tracks = [n for n in nodes(fx) if n.get("$type", "").startswith("effectTrackItem")]
        require(len(tracks) == len(layer_sequence) + 2, "Missing effect events")
        frames = sorted((n for n in tracks if n.get("$type") == "effectTrackItemParticles"),
                        key=lambda n: (n.get("timeBegin", 0), n["particleSystem"]["DepotPath"]["$value"]))
        require(len(frames) == len(layer_sequence), "Missing separate bow/heart frame track")
        loop = fx["effectLoops"][0]
        require(abs(loop["endTime"] - spec["loop_end_seconds"]) < 1e-5, "Invalid loop boundary")
        require(abs(loop.get("startTime", 0) - spec["loop_start_seconds"]) < 1e-5, "Invalid loop start")
        for frame, (suffix, begin, duration, _layer) in zip(frames, layer_sequence, strict=True):
            require(abs(frame.get("timeBegin", 0) - begin) < 1e-5, "Non-contiguous native animation")
            require(abs(frame["timeDuration"] - duration) < 1e-5, "Wrong native frame duration")
            require(frame["particleSystem"]["DepotPath"]["$value"].replace("\\", "/") == f"{PREFIX}/fx/{variant}_{suffix}.particle", "Motion frame sequence changed")
            require(frame["alpha"]["evaluator"]["Data"].get("value", 1.0) == 1, "Invisible particle track")
        sounds = [n for n in tracks if n.get("$type") == "effectTrackItemSound"]
        require(len(sounds) == 1 and sounds[0]["eventName"]["$value"] == spec["sound_event"], "Wrong vanilla cue")
        require(sounds[0]["timeBegin"] > loop["endTime"], "Outro sound is inside the repeating loop")
        entity = packed[f"{PREFIX}/registration/velvet_crash_{variant}.ent"]
        chunks = entity["compiledData"]["Data"]["Chunks"]
        require(len(chunks) == 2 and chunks[1]["name"]["$value"] == "ghostline_velvet_crash_fx", "Patch replaced vanilla component")
        desc = chunks[1]["effectDescs"][0]["Data"]
        require(desc["effectName"]["$value"] == spec["fx_name"], "Status effect and entity names differ")
        bindings = desc["compiledEffectInfo"]["eventsSortedByRUID"]
        expected = sorted(int(n["ruid"]) for n in tracks if n["$type"] != "effectTrackItemLoopMarker")
        require([int(n["eventRUID"]) for n in bindings] == expected, "Compiled placement event IDs do not match timeline")
        for suffix, _begin, life, layer in layer_sequence:
            particle = packed[f"{PREFIX}/fx/{variant}_{suffix}.particle"]["emitters"][0]["Data"]
            size = spec["v_screen_size"] if variant == "v" else spec["npc_billboard_size"]
            cooked = base64.b64decode(particle["renderResourceBlob"]["Data"]["updaterData"]["data"]["Bytes"])
            require(len(cooked) == 61, "Particle updater layout changed")
            require(all(abs(x-life) < 1e-5 for x in struct.unpack_from("<2f", cooked, 4)), "Cooked lifetime differs from spec")
            require(all(abs(x-size) < 1e-5 for x in struct.unpack_from("<4f", cooked, 16)), "Cooked particle size differs from spec")
            require(particle["emitterLoops"] == 1, "Frame particle can repeat outside its native track")
            info = particle["renderResourceBlob"]["Data"]["header"]["emitterInfo"]
            require(info["emitterLoops"] == 1 and info["lods"][0]["birthRate"] == [0, 0], "Cooked frame emitter can accumulate particles")
            require(particle["particleDrawer"]["Data"]["$type"] == ("CParticleDrawerScreen" if variant == "v" else "CParticleDrawerBillboard"), "Wrong renderer")
            material = particle["localMaterialInstance"]["Data"]
            require(material["baseMaterial"]["DepotPath"]["$value"] == r"engine\materials\particles_generic.remt", "Wrong screen-compatible textured shader")
            values = {key: value for param in material["values"] for key, value in param.items() if key != "$type"}
            require([values["Color"].get(key, 0) for key in ("Red", "Green", "Blue", "Alpha")] == spec["material_tint"], "Neutral colour-texture tint lost on serialization")
            settings = spec["layers"][layer]
            require(values.get("AdditiveAlphaBlend", 0) == settings["additive_blend"], "Bow/heart blending modes diverged from spec")
            require(abs(values["ColorMultiplier"] - settings["color_multiplier"]) < 1e-5, "Layer brightness changed")
            require(abs(values["AlphaGlobal"] - settings["alpha_global"]) < 1e-5, "Layer opacity changed")
            require(values["Diffuse"]["DepotPath"]["$value"].replace("\\", "/") in packed, "Missing glyph texture")
            mask = values["AlphaMask"]["DepotPath"]["$value"].replace("\\", "/")
            require(mask in packed and mask.endswith("_m.xbm"), "Black glyph opacity mask missing")
    strings = packed[f"{PREFIX}/localization/en-us/onscreens/velvet_crash.json"]["root"]["Data"]["entries"]
    require(len(strings) == 4 and len({n["secondaryKey"] for n in strings}) == 4, "Missing UI strings")
    tweak = read_tweak_dependencies(root / "source/resources/r6/tweaks/ghostline/velvet_crash_protocol.yaml")
    validate_tweaks(tweak)
    require(tweak["BaseStatusEffect.GhostlineVelvetCrashVision"]["VFX"] == ["GhostlineVelvetCrash.FX"], "Custom VFX did not replace vanilla blindness")
    require(tweak["BaseStatusEffect.GhostlineVelvetCrashVision"]["SFX"] == [], "Vanilla sound override was not cleared")
    require(tweak["GhostlineVelvetCrash.DurationValue"]["value"] == spec["duration_seconds"], "Gameplay and FX duration diverged")
    manifest = build_manifest("velvet-crash", project="velvet-crash", deduplicate=False)
    require(set(manifest.payloads) == set(packed), "Package selection lost authored FX assets")
    goth_baddie = "mod/ghostline/characters/goth_baddie/goth_baddie.ent"
    patches = manifest.registration["resource"]["patch"]
    require(goth_baddie in resource_strings(patches[r"mod\velvet_crash\registration\velvet_crash_npc.ent"]), "Goth Baddie integration was lost from registration")
    require(manifest.audit["external_patch_targets"] == [goth_baddie], "Unexpected optional mod integration target")
    for depot, chunk in packed.items():
        for dependency in resource_strings(chunk):
            if dependency.startswith("mod/"):
                require(dependency in packed, f"Missing owned dependency in {depot}: {dependency}")
    report = {"resource_round_trips": len(packed), "placement_bindings": 2 * (len(layer_sequence) + 1),
              "independent_material_layers": ["alpha-blended bows", "additive hearts"],
              "motion_frames_per_variant": spec["hold_frames"], "duration_seconds": spec["duration_seconds"],
              "outro_seconds": spec["outro_frames"] * spec["outro_frame_seconds"],
              "custom_scripts": False, "runtime_verified": False}
    atomic_write_json(work / "report.json", report)
    return report


if __name__ == "__main__":
    print(json.dumps(audit(), indent=2))
