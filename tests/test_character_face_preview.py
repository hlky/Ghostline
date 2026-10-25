from __future__ import annotations

import copy
import sys
import tempfile
import unittest
from unittest import mock
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import character_builder as builder
import character_face_preview as face


class CharacterFacePreviewTests(unittest.TestCase):
    def test_hair_profile_gradients_are_attached_to_every_matching_material(self):
        profile = r"base\characters\common\hair\textures\hair_profiles\blonde_golden.hp"
        models = [{"materials": [{"Data": {"HairProfile": profile}}, {"Data": {"HairProfile": profile}}]}]
        gradient = [{"value": 0, "color": {"Red": 90, "Green": 70, "Blue": 50}},
                    {"value": 1, "color": {"Red": 234, "Green": 220, "Blue": 198}}]
        def export(command, _label):
            jobs = builder.read_json(Path(command[2]))["jobs"]
            self.assertEqual(len(jobs), 1)
            self.assertEqual(jobs[0]["resource"], profile)
            builder.write_json(Path(jobs[0]["output"]), {
                "Data": {"RootChunk": {"$type": "CHairProfile", "gradientEntriesRootToTip": gradient}}})
        with tempfile.TemporaryDirectory() as directory, mock.patch.object(face.full, "run_checked", side_effect=export):
            face.attach_hair_profiles(models, Path(directory), Path(directory))
        for material in models[0]["materials"]:
            self.assertEqual(material["Data"]["HairProfileGradient"], gradient)

    def test_goth_baddie_has_no_tattoos_in_any_component_copy(self):
        manifest = builder.load_manifest(ROOT / "projects/test-quests/gqt006/characters/goth_baddie.character.json")
        catalog = builder.load_catalog(manifest)
        entity, app, *_ = builder.generate_documents(manifest, catalog)
        self.assertTrue(builder.validate_generated(manifest, entity, app).ok)
        for appearance in builder.appearance_data(app):
            for components in builder.components_by_name(appearance):
                self.assertEqual(components["h0_tattoo"]["isEnabled"], 0)
                self.assertEqual(components["hx_makeup_eyes"]["isEnabled"], 1)
        layers = face.face_layers(manifest, app)
        self.assertNotIn("h0_tattoo", [v["component"] for v in layers])
        self.assertIn("he_eyes", [v["component"] for v in layers])
        self.assertEqual(next(v for v in layers if v["component"] == "h0_head")["mesh_appearance"], "02_ca_limestone")

    def test_exact_material_appearance_and_wolvenkit_ordinal(self):
        document = {"Appearances": {"black_050": ["b", "a"], "black_051": ["a"]},
                    "Materials": [{"Name": "a"}, {"Name": "b"}]}
        self.assertEqual(face.selected_materials(document, "black_050"), [{"Name": "b"}, {"Name": "a"}])
        with self.assertRaises(builder.CharacterBuildError):
            face.selected_materials(document, "black_05")
        document["Appearances"].pop("black_051")
        self.assertEqual(face.selected_materials(document, "black_05"), [{"Name": "b"}, {"Name": "a"}])
        with self.assertRaises(builder.CharacterBuildError):
            face.selected_materials(document, "unknown")

    def test_tattoo_can_be_restored_through_catalog(self):
        manifest = builder.load_manifest(ROOT / "projects/test-quests/gqt006/characters/goth_baddie.character.json")
        restored = copy.deepcopy(manifest)
        for appearance in restored["appearances"]:
            appearance["selections"]["face_tattoos"] = "tutorial_tattoo"
        _, app, *_ = builder.generate_documents(restored, builder.load_catalog(restored))
        for appearance in builder.appearance_data(app):
            for components in builder.components_by_name(appearance):
                self.assertEqual(components["h0_tattoo"]["isEnabled"], 1)


if __name__ == "__main__":
    unittest.main()
