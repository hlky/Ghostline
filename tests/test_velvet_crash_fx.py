from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import unittest
import sys

REPO = Path(__file__).resolve().parents[1]
PROJECT = REPO / "projects/experiments/velvet-crash"
IMPORT = importlib.util.spec_from_file_location("velvet_crash_build", PROJECT / "implementation/build.py")
build = importlib.util.module_from_spec(IMPORT)
IMPORT.loader.exec_module(build)


class VelvetCrashTests(unittest.TestCase):
    def test_ep1_replacement_templates_are_patched_for_real_gameplay_targets(self):
        import yaml
        targets = json.loads((PROJECT/'implementation/npc-targets.json').read_text(encoding='utf-8'))
        registration = yaml.safe_load((PROJECT/'source/resources/Ghostline_VelvetCrash.archive.xl').read_text(encoding='utf-8'))
        registered = registration['resource']['patch'][r'mod\velvet_crash\registration\velvet_crash_npc.ent']
        # These replace the legacy templates used by the actual traced records.
        required = {
            r'ep1\characters\entities\gang\gang__ep1_tyger_ma.ent',
            r'ep1\characters\entities\gang\gang__ep1_tyger_wa.ent',
            r'ep1\characters\entities\gang\gang__ep1_maelstrom_ma.ent',
            r'ep1\characters\entities\corpo\corpo__ep1_ncpd_ma.ent',
            r'ep1\characters\entities\corpo\corpo__ep1_ncpd_wa.ent',
        }
        self.assertTrue(required <= set(targets))
        self.assertTrue(set(targets) <= set(registered))
        self.assertEqual(len(targets), len(set(targets)))
        audit = json.loads((PROJECT/'implementation/npc-target-audit.json').read_text(encoding='utf-8'))
        for row in audit['rows']:
            if row['selected']:
                self.assertTrue(row['npc_puppet'] and row['head_slot'])
                self.assertIn(row['path'], registered)

    def test_visible_blinding_payload_owns_cosmetics_without_double_spawning(self):
        sys.path.insert(0, str(REPO / 'tools'))
        from package_manifest import read_tweak_dependencies
        records = read_tweak_dependencies(PROJECT/'source/resources/r6/tweaks/ghostline/velvet_crash_protocol.yaml')
        self.assertEqual(records['BaseStatusEffect.GhostlineVelvetCrashShortBlind']['VFX'],
                         ['GhostlineVelvetCrash.FX'])
        self.assertEqual(records['BaseStatusEffect.GhostlineVelvetCrashVision']['VFX'], [])
        self.assertEqual(records['GhostlineVelvetCrash.ApplyBlind']['statusEffect'],
                         'BaseStatusEffect.GhostlineVelvetCrashShortBlind')
        self.assertIn('GhostlineVelvetCrash.ApplyBlind',
                      records['QuickHack.GhostlineVelvetCrashProtocol']['completionEffects'])

    @classmethod
    def setUpClass(cls):
        cls.spec = json.loads((PROJECT / "velvet_crash.fx.json").read_text())
        cls.donor = json.loads((PROJECT / "implementation/donors/p_blindness.particle.json").read_text())

    def test_black_bow_cores_are_opaque_and_not_additive(self):
        bow = build.bow_glyph(self.spec)
        self.assertEqual(bow.getpixel((9, 7)), tuple(self.spec["black"]))
        emitter = build.particle(self.donor, self.spec, "npc", "hold_00", "bows")["emitters"][0]["Data"]
        values = {key: value for param in emitter["localMaterialInstance"]["Data"]["values"]
                  for key, value in param.items() if key != "$type"}
        self.assertEqual(values["AdditiveAlphaBlend"], 0)
        self.assertEqual(values["Color"]["Red"], 255)
        self.assertTrue(values["AlphaMask"]["DepotPath"]["$value"].endswith("_m.xbm"))
        self.assertNotEqual(values["Diffuse"], values["AlphaMask"])

    def test_colour_frames_contain_opaque_black_bows_and_pink_hearts(self):
        for variant in ("v", "npc"):
            frame = build.cluster_frame(512, variant, self.spec)
            colors = set(frame.getdata())
            self.assertIn(tuple(self.spec["black"]), colors)
            self.assertIn(tuple(self.spec["pink"]), colors)
            self.assertEqual(frame.getpixel((0, 0))[3], 0)
            self.assertEqual(frame.tobytes(), build.cluster_frame(512, variant, self.spec, 1.0).tobytes())
            self.assertNotEqual(frame.tobytes(), build.cluster_frame(512, variant, self.spec, 0.5).tobytes())

    def test_confetti_is_visible_then_fully_transparent(self):
        frame = build.cluster_frame(256, "npc", self.spec)
        confetti = build.fragment_frames(frame, self.spec["outro_frames"], self.spec["seed"])
        self.assertEqual(len(confetti), 16)
        self.assertIsNone(confetti[-1].getchannel("A").getbbox())
        self.assertNotEqual(confetti[3].tobytes(), frame.tobytes())
        self.assertIsNotNone(confetti[3].getchannel("A").getbbox())

    def test_effect_namespaces_are_disjoint_from_installed_heartbreaker(self):
        heartbreaker_path = REPO / "projects/experiments/heartbreaker/implementation/build.py"
        module_spec = importlib.util.spec_from_file_location("heartbreaker_comparison", heartbreaker_path)
        heartbreaker = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(heartbreaker)
        other_spec = json.loads((heartbreaker_path.parents[1] / "heartbreaker.fx.json").read_text())
        fx, events = build.effect(self.spec, "npc")
        _other_fx, other_events = heartbreaker.effect(other_spec, "npc")
        self.assertFalse({item["eventRUID"] for item in events} & {item["eventRUID"] for item in other_events})
        self.assertAlmostEqual(fx["length"], 1.8)
        self.assertEqual(len(events), 51)
        self.assertNotEqual(self.spec["fx_name"], other_spec["fx_name"])

    def test_material_layers_keep_black_out_of_additive_heart_textures(self):
        for variant in ("v", "npc"):
            hearts = build.cluster_frame(512, variant, self.spec, layer="hearts")
            bows = build.cluster_frame(512, variant, self.spec, layer="bows")
            self.assertNotIn(tuple(self.spec["black"]), set(hearts.getdata()))
            self.assertNotIn(tuple(self.spec["pink"]), set(bows.getdata()))
            self.assertIn(tuple(self.spec["black"]), set(bows.getdata()))
            emitter = build.particle(self.donor, self.spec, variant, "hold_00", "hearts")["emitters"][0]["Data"]
            values = {key: value for param in emitter["localMaterialInstance"]["Data"]["values"]
                      for key, value in param.items() if key != "$type"}
            self.assertEqual(values["AdditiveAlphaBlend"], 1)

    def test_both_layers_share_frame_timing_and_have_unique_placement_events(self):
        fx, events = build.effect(self.spec, "v")
        particles = [track["Data"]["items"][0]["Data"] for track in fx["trackRoot"]["Data"]["tracks"]
                     if track["Data"]["items"][0]["Data"]["$type"] == "effectTrackItemParticles"]
        self.assertEqual(len(particles), 50)
        for heart, bow in zip(particles[::2], particles[1::2], strict=True):
            self.assertEqual((heart["timeBegin"], heart["timeDuration"]), (bow["timeBegin"], bow["timeDuration"]))
            self.assertTrue(bow["particleSystem"]["DepotPath"]["$value"].endswith("_bows.particle"))
        self.assertEqual(len({event["eventRUID"] for event in events}), len(events))


if __name__ == "__main__":
    unittest.main()
