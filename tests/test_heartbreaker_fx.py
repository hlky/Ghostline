from __future__ import annotations

import base64
from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import struct
import sys
import tempfile
import unittest

import yaml

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "tools"))
from package_manifest import read_tweak_dependencies, resource_strings

BUILD_PATH = REPO / "projects/experiments/heartbreaker/implementation/build.py"
IMPORT = importlib.util.spec_from_file_location("heartbreaker_build", BUILD_PATH)
build = importlib.util.module_from_spec(IMPORT)
IMPORT.loader.exec_module(build)


class HeartbreakerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spec = json.loads((BUILD_PATH.parents[1] / "heartbreaker.fx.json").read_text())
        cls.donor = json.loads((BUILD_PATH.parent / "donors/p_blindness.particle.json").read_text())

    def test_cooked_lifetime_and_size_match_both_renderers(self):
        for variant in ("v", "npc"):
            particle = build.particle(self.donor, self.spec, variant, 0)
            emitter = particle["emitters"][0]["Data"]
            cooked = base64.b64decode(emitter["renderResourceBlob"]["Data"]["updaterData"]["data"]["Bytes"])
            self.assertAlmostEqual(struct.unpack_from("<f", cooked, 4)[0], 0.05)
            self.assertAlmostEqual(struct.unpack_from("<f", cooked, 16)[0], self.spec["v_screen_size"] if variant == "v" else self.spec["npc_billboard_size"])
            self.assertEqual(emitter["emitterLoops"], 1)

    def test_changed_donor_buffer_fails_instead_of_guessing_offsets(self):
        donor = deepcopy(self.donor)
        donor["Data"]["RootChunk"]["emitters"][0]["Data"]["renderResourceBlob"]["Data"]["updaterData"]["data"]["Bytes"] = base64.b64encode(bytes(61)).decode()
        with self.assertRaisesRegex(ValueError, "Unsupported particle lifetime"):
            build.particle(donor, self.spec, "v", None)

    def test_outro_binding_and_sound_never_repeat_inside_loop(self):
        for variant in ("v", "npc"):
            fx, bindings = build.effect(self.spec, variant)
            items = [track["Data"]["items"][0]["Data"] for track in fx["trackRoot"]["Data"]["tracks"]]
            sound = next(item for item in items if item["$type"] == "effectTrackItemSound")
            self.assertGreater(sound["timeBegin"], fx["effectLoops"][0]["endTime"])
            self.assertEqual(len(bindings), 2 + self.spec["hold_frames"] + self.spec["outro_frames"])
            self.assertEqual([int(x["eventRUID"]) for x in bindings], sorted(int(x["ruid"]) for x in items if x["$type"] != "effectTrackItemLoopMarker"))
            self.assertAlmostEqual(fx["length"], 1.6)

    def test_pixel_breakup_ends_fully_transparent(self):
        image = build.heart_mask(64, "v", self.spec)
        frames = build.fragment_frames(image, 12, 7319)
        self.assertIsNotNone(image.getchannel("A").getbbox())
        self.assertIsNotNone(frames[0].getchannel("A").getbbox())
        self.assertIsNone(frames[-1].getchannel("A").getbbox())

    def test_motion_is_periodic_and_glitches_do_not_fill_transparent_background(self):
        for variant in ("v", "npc"):
            first = build.heart_mask(512, variant, self.spec, 0.0)
            middle = build.heart_mask(512, variant, self.spec, 0.5)
            wrap = build.heart_mask(512, variant, self.spec, 1.0)
            self.assertNotEqual(first.tobytes(), middle.tobytes())
            self.assertEqual(first.tobytes(), wrap.tobytes())
            for mask in (first, middle):
                alpha = mask.getchannel("A")
                self.assertLess(sum(value > 0 for value in alpha.getdata()), 512 * 512 // 2)
                self.assertEqual(alpha.getpixel((0, 0)), 0)

    def test_native_motion_tracks_have_no_gaps_or_overlap_and_outro_is_outside_loop(self):
        fx, _bindings = build.effect(self.spec, "npc")
        particles = sorted((track["Data"]["items"][0]["Data"] for track in fx["trackRoot"]["Data"]["tracks"]
                            if track["Data"]["items"][0]["Data"]["$type"] == "effectTrackItemParticles"),
                           key=lambda item: item["timeBegin"])
        self.assertEqual(particles[0]["timeBegin"], 0)
        for left, right in zip(particles, particles[1:]):
            self.assertAlmostEqual(left["timeBegin"] + left["timeDuration"], right["timeBegin"])
        hold = [item for item in particles if "hold_" in item["particleSystem"]["DepotPath"]["$value"]]
        outro = [item for item in particles if "burst_" in item["particleSystem"]["DepotPath"]["$value"]]
        self.assertAlmostEqual(hold[0]["timeBegin"], fx["effectLoops"][0]["startTime"])
        self.assertAlmostEqual(hold[-1]["timeBegin"] + hold[-1]["timeDuration"], fx["effectLoops"][0]["endTime"])
        self.assertAlmostEqual(outro[0]["timeBegin"], fx["effectLoops"][0]["endTime"])
        self.assertAlmostEqual(outro[-1]["timeBegin"] + outro[-1]["timeDuration"], fx["length"])

    def test_tweak_tags_keep_nested_depot_dependencies_and_reject_python(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "tweak.yaml"
            path.write_text("Record:\n  scalar: !remove mod/test/a.ent\n  list: !append [mod/test/b.ent]\n  map: !append-once {path: mod/test/c.ent}\n")
            self.assertEqual(resource_strings(read_tweak_dependencies(path)), {"mod/test/a.ent", "mod/test/b.ent", "mod/test/c.ent"})
            path.write_text("!!python/object/apply:os.system ['echo unwanted']")
            with self.assertRaises(yaml.constructor.ConstructorError):
                read_tweak_dependencies(path)
            with self.assertRaises(yaml.constructor.ConstructorError):
                yaml.safe_load("value: !append mod/test/a.ent")

    def test_tweak_contract_rejects_original_wrong_case_fx_and_equip_flats(self):
        document = read_tweak_dependencies(BUILD_PATH.parents[1] / "source/resources/r6/tweaks/ghostline/heartbreaker_protocol.yaml")
        build.validate_tweaks(document)
        for record, correct, wrong in (
            ("BaseStatusEffect.GhostlineHeartbreakerVision", "VFX", "vfx"),
            ("BaseStatusEffect.GhostlineHeartbreakerVision", "SFX", "sfx"),
            ("Items.GhostlineHeartbreakerSelfTest", "OnEquip", "onEquip"),
        ):
            with self.subTest(wrong=wrong):
                broken = deepcopy(document)
                broken[record][wrong] = broken[record].pop(correct)
                with self.assertRaisesRegex(ValueError, "Unknown case-sensitive TweakDB flats"):
                    build.validate_tweaks(broken)
