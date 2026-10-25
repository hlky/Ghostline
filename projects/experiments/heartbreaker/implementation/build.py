"""Author and verify native Heartbreaker FX; run from the repository root."""
from __future__ import annotations

import argparse
import base64
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import random
import re
import shutil
import struct
import subprocess
import sys

from PIL import Image, ImageDraw
import yaml

PROJECT = Path(__file__).resolve().parents[1]
REPO = PROJECT.parents[2]
sys.path.insert(0, str(REPO / "tools"))
from artifact_io import atomic_write_json  # noqa: E402
from toolchain import default_tool_path  # noqa: E402

PREFIX = "mod/heartbreaker"


def validate_tweaks(document: dict) -> None:
    """Check case-sensitive flats against the checked-out WolvenKit RTTI."""
    bases = {"BaseStatusEffect.BaseBlindUI": "StatusEffectUIData",
             "BaseStatusEffect.QuickHackBlind": "StatusEffect", "BaseStatusEffect.ShortBlind": "StatusEffect",
             "Interactions.BlindHack": "InteractionBase", "QuickHack.BlindHack": "ObjectAction",
             "Items.BlindProgram": "Item", "ItemAction.Eat": "ItemAction",
             "Items.LowQualityFood1": "ConsumableItem", "Vendors.wat_lch_netrunner_01": "Vendor"}
    types_root = REPO / "WolvenKit/WolvenKit.RED4/Types"
    cache = {}
    def fields(type_name):
        if type_name in cache:
            return cache[type_name]
        declaration = types_root / "Classes" / (type_name + ".cs")
        if not declaration.is_file():
            raise ValueError(f"Unknown TweakDB record type: {type_name}")
        extension = types_root / "ClassesExt/Tweak" / (type_name + ".cs")
        result = set(re.findall(r'\[RED\("([^"]+)"\)\]', extension.read_text() if extension.is_file() else ""))
        parent = re.search(rf'class {type_name}\s*:\s*(\w+)', declaration.read_text())
        if parent and parent[1].startswith("gamedata"):
            result.update(fields(parent[1]))
        cache[type_name] = result
        return result
    def record_type(name):
        if name in bases:
            return bases[name]
        value = document[name]
        return value["$type"] if "$type" in value else record_type(value["$base"])
    for name, record in document.items():
        allowed = fields("gamedata" + record_type(name) + "_Record")
        invalid = set(record) - allowed - {"$base", "$type"}
        if invalid:
            raise ValueError(f"{name}: Unknown case-sensitive TweakDB flats: {sorted(invalid)}")


def cname(value: str) -> dict:
    return {"$type": "CName", "$storage": "string", "$value": value}


def reference(path: str) -> dict:
    return {"DepotPath": {"$type": "ResourcePath", "$storage": "string", "$value": path.replace("/", "\\")}, "Flags": "Default"}


def uid(name: str) -> str:
    # Stable, mod-specific identities, kept as unsigned decimal strings.
    return str(int.from_bytes(hashlib.sha256(("ghostline.heartbreaker." + name).encode()).digest()[:8], "little"))


def document(root: dict, depot: str) -> dict:
    return {"Header": {"WolvenKitVersion": "8.17.4", "WKitJsonVersion": "0.0.9", "GameVersion": 2310,
                       "ExportedDateTime": "1970-01-01T00:00:00Z", "DataType": "CR2W",
                       "ArchiveFileName": str(PROJECT / "source/archive" / depot)},
            "Data": {"Version": 195, "BuildVersion": 0, "RootChunk": root}}


def run(command: list[str], log: Path, *, folder_import_count: int | None = None) -> None:
    log.parent.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(command, cwd=REPO, capture_output=True, text=True, encoding="utf-8", errors="replace")
    log.write_text(result.stdout + result.stderr, encoding="utf-8")
    # WolvenKit 8.17.4 ImportTaskInner inverts ImportFolder's success bool.
    # Accept its folder-only exit 3 solely with the exact complete import count;
    # the caller also checks every XBM and the verifier re-reads every texture.
    imported_all = (folder_import_count is not None and result.returncode == 3
                    and f"Imported {folder_import_count}/{folder_import_count} file(s)" in result.stdout)
    if (result.returncode and not imported_all) or " Error       ]" in result.stdout:
        raise RuntimeError(f"Command failed ({result.returncode}); see {log}")


def wkit_json(value):
    # WolvenKit's CBool reader requires numeric 0/1, unlike native JSON.
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, dict):
        return {key: wkit_json(child) for key, child in value.items()}
    if isinstance(value, list):
        return [wkit_json(child) for child in value]
    return value


def heart_mask(size: int, variant: str, spec: dict, phase: float = 0.0) -> Image.Image:
    """Owned pixel glyphs; bake independent bobbing and glitches into native frames."""
    from math import sin, pi
    grid = spec["pixel_grid"]
    image = Image.new("RGBA", (grid, grid))
    if variant == "v":
        columns, rows = spec["v_columns"], spec["v_rows"]
        centres = [((i + 0.5) / columns + 0.012 * sin(i + j * 2),
                    (j + 0.5) / rows + 0.012 * sin(i * 2 + j),
                    0.12 + 0.025 * ((i + j * 2) % 3))
                   for j in range(rows) for i in range(columns)]
    else:
        centres = [(0.50, 0.47, 0.25), (0.24, 0.24, 0.13), (0.75, 0.23, 0.18),
                   (0.22, 0.60, 0.10), (0.79, 0.63, 0.16), (0.46, 0.80, 0.12)]
    glyph = ("01110001110", "11111011111", "11111111111", "11111111111",
             "11111111111", "01111111110", "00111111100", "00011111000",
             "00001110000", "00000100000")
    base = Image.new("RGBA", (11, 10))
    for y, row in enumerate(glyph):
        for x, pixel in enumerate(row):
            if pixel == "1":
                edge = any(nx < 0 or nx >= 11 or ny < 0 or ny >= 10 or glyph[ny][nx] == "0"
                           for nx, ny in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)))
                value = 255 if edge else (180 if y % 3 else 105)
                base.putpixel((x, y), (value, value, value, 255 if edge else 220))
    tick = int((phase % 1.0) * spec["hold_frames"] + 1e-6)
    for index, (cx, cy, radius) in enumerate(centres):
        angle = 2 * pi * phase + index * 1.7
        cx += 0.012 * sin(angle + 0.6)
        cy += spec[f"{variant}_bob_amplitude"] * sin(angle)
        width = max(9, round(radius * grid * (1.0 + 0.1 * sin(angle + 1.2))))
        heart = base.resize((width, round(width * 10 / 11)), Image.Resampling.NEAREST)
        # Two short glitch beats per cycle, offset across hearts. Only a narrow
        # strip moves: silhouettes stay readable and individual motion is visible.
        if (tick + index) % 4 == 2:
            y = heart.height // 2
            strip = heart.crop((0, y, heart.width, y + 2))
            heart.paste((0, 0, 0, 0), (0, y, heart.width, y + 2))
            heart.alpha_composite(strip, (3 if index % 2 else -3, y))
        x, y = round(cx * grid - heart.width / 2), round(cy * grid - heart.height / 2)
        image.alpha_composite(heart, (x, y))
        draw = ImageDraw.Draw(image)
        ax = round((cx + radius * 0.65 + 0.018 * sin(angle + 2)) * grid)
        ay = round((cy - radius * 0.35 + 0.015 * sin(angle - 1)) * grid)
        draw.rectangle((ax, ay, ax+1, ay+1), fill=(255, 255, 255, 210 if tick % 3 else 125))
    return image.resize((size, size), Image.Resampling.NEAREST)


def frame_tracks(spec: dict) -> list[tuple[str, float, float]]:
    """One intro, a gapless animated loop, then a finite fragment outro."""
    start, end = spec["loop_start_seconds"], spec["loop_end_seconds"]
    step = (end - start) / spec["hold_frames"]
    return [("hearts", 0.0, start),
            *[(f"hold_{index:02d}", start + index * step, step) for index in range(spec["hold_frames"])],
            *[(f"burst_{index:02d}", end + index * spec["outro_frame_seconds"], spec["outro_frame_seconds"])
              for index in range(spec["outro_frames"])]]


def preview_frames(output: Path, variant: str, frames: list[Image.Image], spec: dict) -> None:
    """Reproducible art previews, without claiming to simulate the game shader."""
    preview = output / "generated/previews"
    preview.mkdir(parents=True, exist_ok=True)
    colored = []
    for frame in frames:
        tinted = Image.new("RGBA", frame.size)
        tinted.putdata([(r * spec["pink"][0] // 255, g * spec["pink"][1] // 255,
                        b * spec["pink"][2] // 255, a) for r, g, b, a in frame.getdata()])
        canvas = Image.new("RGBA", frame.size, (12, 16, 27, 255))
        canvas.alpha_composite(tinted)
        colored.append(canvas.convert("RGB"))
    colored[0].save(preview / f"{variant}-hearts.png")
    hold_count = spec["hold_frames"]
    hold = colored[1:hold_count+1]
    step_ms = round((spec["loop_end_seconds"] - spec["loop_start_seconds"]) * 1000 / hold_count)
    hold[0].save(preview / f"{variant}-motion.gif", save_all=True, append_images=hold[1:],
                 duration=step_ms, loop=0, disposal=2)
    outro = colored[hold_count+1:]
    outro[0].save(preview / f"{variant}-outro.gif", save_all=True, append_images=outro[1:],
                  duration=round(spec["outro_frame_seconds"] * 1000), loop=0, disposal=2)


def fragment_frames(image: Image.Image, count: int, seed: int) -> list[Image.Image]:
    """A coherent native flip sequence: the same heart pixels break and scatter."""
    rng = random.Random(seed)
    size = image.width
    cell = max(4, size // 64)
    tiles = []
    for y in range(0, size, cell):
        for x in range(0, size, cell):
            tile = image.crop((x, y, x + cell, y + cell))
            if tile.getchannel("A").getbbox():
                vx = (x / size - 0.5) * size * 0.45 + rng.uniform(-size * 0.20, size * 0.20)
                vy = (y / size - 0.5) * size * 0.45 + rng.uniform(-size * 0.20, size * 0.20)
                tiles.append((x, y, vx, vy, tile))
    frames = []
    for index in range(count):
        t = (index + 1) / count
        frame = Image.new("RGBA", image.size)
        for x, y, vx, vy, tile in tiles:
            part = tile.copy()
            part.putalpha(part.getchannel("A").point(lambda a: round(a * (1 - t) ** 0.55)))
            frame.alpha_composite(part, (round(x + vx * t), round(y + vy * t + size * 0.10 * t*t)))
        frames.append(frame)
    return frames


def handle(data: dict, counter: list[int]) -> dict:
    index = counter[0]
    counter[0] += 1
    return {"HandleId": str(index), "Data": data}


def renumber_handles(value: dict) -> dict:
    """Keep all definitions unique and all references resolving backwards."""
    output = deepcopy(value)
    mapping = {}
    def definitions(node):
        if isinstance(node, dict):
            if "HandleId" in node:
                old = node["HandleId"]
                if old in mapping:
                    raise ValueError(f"Duplicate handle definition {old}")
                mapping[old] = str(len(mapping))
                node["HandleId"] = mapping[old]
            for child in node.values():
                definitions(child)
        elif isinstance(node, list):
            for child in node:
                definitions(child)
    def references(node):
        if isinstance(node, dict):
            if "HandleRefId" in node:
                node["HandleRefId"] = mapping[node["HandleRefId"]]
            for child in node.values():
                references(child)
        elif isinstance(node, list):
            for child in node:
                references(child)
    definitions(output)
    references(output)
    return output


def particle(donor: dict, spec: dict, variant: str, frame: int | str | None) -> dict:
    root = deepcopy(donor["Data"]["RootChunk"])
    emitter = root["emitters"][0]["Data"]
    suffix = "hearts" if frame is None else frame if isinstance(frame, str) else f"burst_{frame:02d}"
    life = next(duration for name, _begin, duration in frame_tracks(spec) if name == suffix)
    size = spec["v_screen_size"] if variant == "v" else spec["npc_billboard_size"]
    emitter["editorName"] = f"Heartbreaker {variant} {suffix}"
    emitter["modules"][0]["Data"]["lifeTime"]["Data"]["value"] = life
    initializer = emitter["modules"][1]["Data"]
    initializer["scale"] = 1.0
    initializer["size"]["Data"]["value"] = {"$type": "Vector4", "X": size, "Y": size, "Z": size, "W": 1.0}
    emitter["material"] = reference("engine/materials/particles_generic.remt")
    tex = f"{PREFIX}/textures/{variant}_{suffix}_d.xbm"
    def scalar(name, value): return {"$type": "Float", name: value}
    pink = {"$type": "Color", **dict(zip(("Red", "Green", "Blue", "Alpha"), spec["pink"]))}
    emitter["localMaterialInstance"]["Data"] = {
        "$type": "CMaterialInstance", "baseMaterial": reference("engine/materials/particles_generic.remt"), "resourceVersion": 4,
        "values": [{"$type": "rRef:ITexture", "Diffuse": reference(tex)},
                   {"$type": "rRef:ITexture", "AlphaMask": reference(tex)},
                   {"$type": "Color", "Color": pink}, scalar("ColorMultiplier", spec["color_multiplier"]),
                   scalar("UseAlphaMask", 1.0), scalar("SubUVWidth", 1.0), scalar("SubUVHeight", 1.0),
                   scalar("AdditiveAlphaBlend", 1.0), scalar("DistortAmount", 0.0), scalar("AlphaGlobal", spec["alpha_global"]),
                   scalar("AlphaSoft", 0.5), {"$type": "Vector4", "TexCoordSpeed": {"$type": "Vector4"}}]}
    if variant == "npc":
        emitter["particleDrawer"]["Data"] = {"$type": "CParticleDrawerBillboard"}
    authored_lod = emitter["lods"][0]
    authored_lod["birthRate"]["Data"]["value"] = 0.0
    authored_lod["burstList"] = [{"$type": "ParticleBurst", "spawnCount": 1}]
    emitter["emitterLoops"] = 1
    blob = emitter["renderResourceBlob"]["Data"]
    info = blob["header"]["emitterInfo"]
    info["vertexDrawerType"] = 1 if variant == "v" else 0
    info["emitterLoops"] = emitter["emitterLoops"]
    info["lods"][0]["birthRate"] = [0.0, 0.0]
    info["lods"][0]["burstList"] = [{"$type": "rendParticleBurst", "spawnCount": 1}]
    # This donor has a verified, fixed 61-byte updater layout. Patch only its
    # two lifetime values and four baked XY size endpoints, with exact guards.
    buffer = blob["updaterData"]["data"]
    cooked = bytearray(base64.b64decode(buffer["Bytes"]))
    if len(cooked) != 61 or struct.unpack_from("<2f", cooked, 4) != (3600.0, 3600.0):
        raise ValueError("Unsupported particle lifetime buffer layout")
    expected_size = struct.pack("<4f", *([3.3] * 4))
    if cooked[16:32] != expected_size:
        raise ValueError("Unsupported particle size buffer layout")
    struct.pack_into("<2f", cooked, 4, life, life)
    struct.pack_into("<4f", cooked, 16, size, size, size, size)
    buffer["Bytes"] = base64.b64encode(cooked).decode()
    return root


def effect(spec: dict, variant: str) -> tuple[dict, list[dict]]:
    counter = [0]
    tracks = []
    events = []
    placement_events = []
    def add_track(item):
        item_handle = handle(item, counter)
        tracks.append(handle({"$type": "effectTrack", "items": [item_handle]}, counter))
        events.append({"HandleRefId": item_handle["HandleId"]})
        if item["$type"] != "effectTrackItemLoopMarker":
            placement_events.append({"$type": "worldCompiledEffectEventInfo", "eventRUID": item["ruid"],
                                     "componentIndexMask": "0", "flags": 1, "placementIndexMask": "1"})
    start, end = spec["loop_start_seconds"], spec["loop_end_seconds"]
    add_track({"$type": "effectTrackItemLoopMarker", "timeBegin": start, "timeDuration": end-start, "ruid": uid(variant + ".loop")})
    for suffix, begin, duration in frame_tracks(spec):
        item = {"$type": "effectTrackItemParticles", "timeBegin": begin, "timeDuration": duration,
                "ruid": uid(variant + "." + suffix), "particleSystem": reference(f"{PREFIX}/fx/{variant}_{suffix}.particle"),
                "soundPositionName": cname("glitch")}
        for prop in ("emissionScale", "alpha", "size", "velocity"):
            evaluator = handle({"$type": "CEvaluatorFloatConst", "value": 1.0}, counter)
            item[prop] = {"$type": "effectEffectParameterEvaluatorFloat", "evaluator": evaluator}
        add_track(item)
    add_track({"$type": "effectTrackItemSound", "timeBegin": end + 0.005, "timeDuration": 0.1,
               "ruid": uid(variant + ".sound"), "eventName": cname(spec["sound_event"]), "positionName": cname("glitch"),
               "rtpcValue": handle({"$type": "CEvaluatorFloatConst", "value": 0.0}, counter)})
    root = {"$type": "worldEffect", "cookingPlatform": "PLATFORM_PC",
            "length": end + spec["outro_frames"] * spec["outro_frame_seconds"],
            "trackRoot": handle({"$type": "effectTrackGroup", "tracks": tracks}, counter), "events": events,
            "effectLoops": [{"$type": "effectLoopData", "startTime": start, "endTime": end}]}
    return renumber_handles(root), sorted(placement_events, key=lambda item: int(item["eventRUID"]))


def patch_entity(spec: dict, variant: str, events: list[dict]) -> dict:
    effect_path = f"{PREFIX}/fx/heartbreaker_{variant}.effect"
    desc = {"$type": "entEffectDesc", "id": uid(variant + ".descriptor"), "effectName": cname(spec["fx_name"]),
            "effect": reference(effect_path), "compiledEffectInfo": {"$type": "worldCompiledEffectInfo",
            "placementTags": [cname("Head")], "relativePositions": [{"$type": "Vector3", "X": 0.0, "Y": 0.0, "Z": 0.18 if variant == "npc" else 0.0}],
            "relativeRotations": [{"$type": "Quaternion", "i": 0.0, "j": 0.0, "k": 0.0, "r": 1.0}],
            "placementInfos": [{"$type": "worldCompiledEffectPlacementInfo", "flags": 3, "placementTagIndex": 0,
                                "relativePositionIndex": 0, "relativeRotationIndex": 0}], "eventsSortedByRUID": events}}
    component = {"$type": "entEffectSpawnerComponent", "name": cname("ghostline_heartbreaker_fx"),
                 "id": uid(variant + ".component"), "effectDescs": [{"HandleId": "0", "Data": desc}]}
    # Patch only one independently named component. No player/NPC state or
    # vanilla fx_status_effects component is copied into the patch resource.
    package = {"Version": 4, "Sections": 7, "CruidIndex": 0,
               "CruidDict": {"0": "0", "1": component["id"]},
               "Chunks": [{"$type": "entEntity"}, component]}
    return {"$type": "entEntityTemplate", "cookingPlatform": "PLATFORM_PC",
            "compiledData": {"BufferId": "0", "Flags": 4063232,
              "Type": "WolvenKit.RED4.Archive.Buffer.RedPackage, WolvenKit.RED4, Version=8.17.4.0, Culture=neutral, PublicKeyToken=null",
              "Data": package}, "resolvedDependencies": [reference(effect_path)]}


def author(output: Path, spec: dict, donor: dict, targets: list[str]) -> list[tuple[str, str]]:
    resources = []
    for variant in ("v", "npc"):
        mask = heart_mask(spec["texture_resolution"], variant, spec)
        images = [mask, *[heart_mask(spec["texture_resolution"], variant, spec, index / spec["hold_frames"])
                         for index in range(spec["hold_frames"])],
                  *fragment_frames(mask, spec["outro_frames"], spec["seed"])]
        preview_frames(output, variant, images, spec)
        for (suffix, _begin, _duration), image in zip(frame_tracks(spec), images, strict=True):
            png = output / "source/raw" / PREFIX / "textures" / f"{variant}_{suffix}_d.png"
            png.parent.mkdir(parents=True, exist_ok=True)
            image.save(png)
            depot = f"{PREFIX}/fx/{variant}_{suffix}.particle"
            atomic_write_json(output / "source/raw" / (depot + ".json"), document(particle(donor, spec, variant, suffix), depot))
            resources.append((depot, "particle"))
        root, events = effect(spec, variant)
        depot = f"{PREFIX}/fx/heartbreaker_{variant}.effect"
        atomic_write_json(output / "source/raw" / (depot + ".json"), document(root, depot))
        resources.append((depot, "effect"))
        depot = f"{PREFIX}/registration/heartbreaker_{variant}.ent"
        atomic_write_json(output / "source/raw" / (depot + ".json"), document(patch_entity(spec, variant, events), depot))
        resources.append((depot, "entity"))
    # Explicit paths work even without newer ArchiveXL's player scopes.
    player_targets = [f"base\\characters\\entities\\player\\player_{body}_{view}.ent"
                      for body in ("ma", "wa") for view in ("fpp", "tpp", "tpp_cutscene", "tpp_cutscene_no_impostor", "tpp_reflexion")]
    player_targets.extend(f"ep1\\characters\\entities\\player\\player_{body}_{view}_ep1.ent"
                          for body in ("ma", "wa") for view in ("fpp", "tpp"))
    registration = {"resource": {"patch": {
        r"mod\heartbreaker\registration\heartbreaker_v.ent": player_targets,
        r"mod\heartbreaker\registration\heartbreaker_npc.ent": [*targets, r"mod\ghostline\characters\goth_baddie\goth_baddie.ent"]}},
        "localization": {"onscreens": {"en-us": [r"mod\heartbreaker\localization\en-us\onscreens\heartbreaker.json"]}}}
    path = output / "source/resources/Ghostline_Heartbreaker.archive.xl"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(registration, sort_keys=False), encoding="utf-8")
    return resources


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-root", type=Path, default=PROJECT)
    parser.add_argument("--author-only", action="store_true")
    args = parser.parse_args()
    output = args.out_root.resolve()
    spec = json.loads((PROJECT / "heartbreaker.fx.json").read_text())
    from package_manifest import read_tweak_dependencies
    validate_tweaks(read_tweak_dependencies(PROJECT / "source/resources/r6/tweaks/ghostline/heartbreaker_protocol.yaml"))
    donors = PROJECT / "implementation/donors"
    catalog = json.loads((donors / "catalog.json").read_text())
    for name, entry in catalog.items():
        path = donors / entry["file"]
        if hashlib.sha256(path.read_bytes()).hexdigest() != entry["sha256"]:
            raise ValueError(f"Donor changed: {name}")
    donor = json.loads((donors / "p_blindness.particle.json").read_text())
    targets = json.loads((PROJECT / "implementation/npc-targets.json").read_text())
    resources = author(output, spec, donor, targets)
    if args.author_only:
        print(f"Authored {len(resources)} CR2W documents and {2 * len(frame_tracks(spec))} owned texture frames under {output}")
        return
    wkit = default_tool_path("wolvenkit")
    work = output / "generated/build"
    work.mkdir(parents=True, exist_ok=True)
    groups = {}
    for depot, kind in resources:
        raw = output / "source/raw" / (depot + ".json")
        cooked = output / "source/archive" / depot
        cooked.parent.mkdir(parents=True, exist_ok=True)
        compatible = work / "wkit-input" / (depot + ".json")
        atomic_write_json(compatible, wkit_json(json.loads(raw.read_text())))
        groups.setdefault(cooked.parent, []).append(compatible)
    # These new material import tables failed a native-writer round trip
    # (invalid rRef import indices). Novel effect/entity layouts also need
    # WolvenKit. Batch by destination directory and audit using native reads.
    for destination, inputs in groups.items():
        run([str(wkit), "cr2w", *map(str, inputs), "--deserialize", "-o", str(destination)],
            work / (destination.name + "-compile.log"))
    for depot, _kind in resources:
        cooked = output / "source/archive" / depot
        if not cooked.is_file() or cooked.read_bytes()[:4] != b"CR2W":
            raise RuntimeError(f"Serializer did not produce {cooked}")
    textures = output / "source/raw" / PREFIX / "textures"
    run([str(wkit), "import", str(output / "source/raw"), "-o", str(output / "source/archive")], work / "textures.log",
        folder_import_count=2 * len(frame_tracks(spec)))
    for png in textures.glob("*.png"):
        texture = output / "source/archive" / PREFIX / "textures" / (png.stem + ".xbm")
        if not texture.is_file():
            raise RuntimeError(f"Texture import did not produce {texture}")
    # Onscreen localization needs no binary donor when serialized by WolvenKit.
    entries = [
        ("ghostline_heartbreaker_name", spec["name"]),
        ("ghostline_heartbreaker_description", "Floods optics with pink holographic hearts for 6 seconds. Hearts shatter into pixels as vision returns."),
        ("ghostline_heartbreaker_selftest_name", "Heartbreaker Protocol: Optical Self-Test"),
        ("ghostline_heartbreaker_selftest_description", "Prototype diagnostic. Consume to test Heartbreaker Protocol on V for 6 seconds. Vision clears after a pixel burst.")]
    depot = f"{PREFIX}/localization/en-us/onscreens/heartbreaker.json"
    root = {"$type": "JsonResource", "root": {"HandleId": "0", "Data": {"$type": "localizationPersistenceOnScreenEntries",
        "entries": [{"$type": "localizationPersistenceOnScreenEntry", "primaryKey": "0", "secondaryKey": key,
                     "femaleVariant": text, "maleVariant": text} for key, text in entries]}}}
    raw = output / "source/raw" / (depot + ".json")
    atomic_write_json(raw, document(root, depot))
    destination = output / "source/archive" / depot
    destination.parent.mkdir(parents=True, exist_ok=True)
    run([str(wkit), "cr2w", str(raw), "--deserialize", "-o", str(destination.parent)], work / "localization.log")
    if not destination.is_file():
        raise RuntimeError("Missing compiled onscreen localization")
    if output != PROJECT:
        target = output / "source/resources/r6/tweaks/ghostline/heartbreaker_protocol.yaml"
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(PROJECT / "source/resources/r6/tweaks/ghostline/heartbreaker_protocol.yaml", target)
    report = {"runtime_verified": False, "game_version": spec["game_version"], "npc_targets": len(targets),
              "sound_event": spec["sound_event"], "native_outro_seconds": spec["outro_frames"] * spec["outro_frame_seconds"],
              "resources": {p.relative_to(output / "source/archive").as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                            for p in (output / "source/archive").rglob("*") if p.is_file()}}
    atomic_write_json(work / "build-report.json", report)
    print(json.dumps({"output": str(output), "resource_count": len(report["resources"]), "runtime_verified": False}))


if __name__ == "__main__":
    main()
