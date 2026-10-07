"""Semantic baselines captured before the GQT005–GQT007 composition migration.

Digests cover complete typed resource data, not generated headers. Journal
comparisons discard allocator IDs and empty donor folders only; localization
ordering is keyed by its stable secondary key. Phase data stays exact.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import quest_authoring
import quest_build
from quest_content import find_entry, load


EXPECTED = {
    "gqt005": {
        "manifest": "db1c11107b477ebf0c5446e9e98096096b3a05558976c8f17da720c17068434f",
        "journal": "210930de684f9ed74418bf7e5c5e72e082a94469e4074ab918262eb18562f08b",
        "onscreen": "346ce5980c3454c05a6b0071be9a4b7595d7834f411575c4b61caf39ac7762d4",
        "phases": {
            "approach_patch": "fe054c4e64cecd9f443fc605f19a1e4f4ff62cb97a108f9e03237211b159a31a",
            "meet_patch": "00b8f1236b74581bbce40457fcd7b6a350815bea665aed09fea255b4ecb790e0",
            "review_braindance": "f8563fd7ef526d12359dfa62813495c16221ef1f4c595d5c57914f1443c7f175",
            "root": "fd8c2851f767726ad35bd75bf393dd437baa80f9b8537ac1c7bdcfbf88d7be39",
        },
        "special": {
            # The shared Patch donor now includes look-at events; only generated
            # HandleId allocation changes in this launch scene.
            "launch_scene": "3bb0218de667e8ee74988c96859094f5fd82cece8416f3d1ff68ac1cc488de32"
        },
        "world": [
            "bfecc8318d508699bef90ab2d48e4bcb4b5fca25ebe5602412aa3a2d8d518e71",
            "fbb536254d847e6598bdcea692eb2c405674834a7c86ccbfd7c1d54ea31c3ced",
            "35181bc840af0a653ae72c9374a53de453188196395718940940e73a6633a242",
        ],
    },
    "gqt006": {
        "manifest": "0534df46bbb6ce04da154727d6bbd0a9b864b47d2998c8e9b9342390746a02fb",
        "journal": "e6a70945281896f490a67fe1bb1e6a69708778ab3b8535a6645621f11fe5e362",
        "onscreen": "e45303252d5552613f7b8946682214b4d58b3594aafd50a207adbe50458d57e7",
        "phases": {
            "challenge_goth_baddie": "d95ab8c81dd4c8f0460198cb85ac8910ec3652ad81fb6c9f748702aa978bd97c",
            "leave_goth_baddie_site": "1090bc24d197caabdff1703dcef102b01cffa03d0314cc5bea53ec1ceb590285",
            "neutralize_goth_baddie": "ffb59e815e9fca4b0ebc95a14d053a026874d1d342f1072b2e19a147427d1f60",
            "read_goth_baddie_shard": "d44d69baa6c7c75740354e7a65d46bf894fa6f04b2929466f02754272b93e2c3",
            "recover_goth_baddie_shard": "54498241f8651096c7bf4ab6c457375adfca6965f4f8009e21187a5ce04b8e7b",
            "report_goth_baddie_outcome": "7155fa9bfec6255115483601dcd3ce672c9dbf1ef00d8640420aec91e099656d",
            "root": "f10709d24af0066e8fc9094405e66d2627e2d3e188b33e91b16d11217bd6e0a2",
        },
        "special": {},
        "world": [
            "dd3f9001d48715febf3178db033ff8425633d5f79714d28c46e8a87151162f90",
            "12fcbfcfe0e66db2990e2a867b8417bb249fa84ef689bce9a919d7ff6f1b45f5",
            "80404793136afabcbc59625c2019c172410786be0ba17ee384df95c2a6c6dae9",
        ],
    },
    "gqt007": {
        "manifest": "2093987efdc53d9fc24ba7410c9b97d94b27c572a6972ee46739e68cfb3f3dfc",
        "journal": "ad3fe077f18507f9268c8bd5fe8916c29800452dc0542a1e50a7f66e54a9df11",
        "onscreen": "b405444514a3ac2ed4eb6efc7be90ce54a999714501997927ba84a87d88962df",
        "phases": {
            "compare_barry_lipsync": "ee3ca84146c7950f486d5375e2667f8df942617c439dd728f2dc6a6a8702b11e",
            "root": "feb99c8bfd4b09bbe3caa666b45c13d7fac44137671d294ae8f519e4998a840c",
        },
        "special": {
            "scene": "7fc6034c1de51d9b12411d39d82606e6f2822f01dd9095b431b06ebd0381e300",
            "lipmap": "b9d03a70cc37900d68a6a48b593721227a4b7c20ba6e3d1a203f59b122b81e47",
            "subtitles": "2e9aa537014682e7c91243790e1ca11927a671da686096fb1462762883bb81e3",
            "subtitle_map": "180a5bfebaa87f77b518a787e71617c73211e855cd043e16875647765256c15d",
            "vo_map": "c35d5b2336fc78f6c5b3921d4b92ec4e7e8dfd7717d0776253aa33109db12ee2",
        },
        "world": [
            "8dc0e6e35ae03aa458ca6ddbb1e41a9cf051ad178f94b32002268e6089852321",
            "40d5713ce400a23c8815266b6dfd1cae341fe54d677b65144dff85afc51e79a8",
            "eca0ed81d339743cba09991e1ee8ab01f6fe0d2f23949719e864e2d6a6d84eee",
        ],
    },
}

FOLDERS = {
    "gameJournalRootFolderEntry",
    "gameJournalPrimaryFolderEntry",
    "gameJournalFolderEntry",
    "gameJournalOnscreenGroup",
    "gameJournalPointOfInterestGroup",
}


def digest(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def journal_content(value: object) -> object:
    if isinstance(value, list):
        return [
            result for child in value if (result := journal_content(child)) is not None
        ]
    if isinstance(value, dict):
        result = {
            key: journal_content(child)
            for key, child in value.items()
            if key != "HandleId"
        }
        if "Data" in result and result["Data"] is None:
            return None
        if result.get("$type") in FOLDERS and not result.get("entries"):
            return None
        return result
    return value


def onscreen_content(document: dict) -> list[dict]:
    return sorted(
        document["Data"]["RootChunk"]["root"]["Data"]["entries"],
        key=lambda entry: entry["secondaryKey"],
    )


def load_build(namespace: str):
    path = ROOT / f"projects/test-quests/{namespace}/implementation/build.py"
    spec = importlib.util.spec_from_file_location(f"modern_{namespace}", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class ModernQuestMigrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.builds = {name: load_build(name) for name in EXPECTED}

    def test_manifest_aliases_preserve_every_compiler_input(self):
        for name, module in self.builds.items():
            with self.subTest(quest=name):
                raw = load(module.MANIFEST)
                self.assertIn("composition", raw)
                normalized = quest_authoring.normalize_spec(raw)
                # Normalize only the two relocated authoring paths for the
                # historical runtime-contract digest.
                if name == "gqt006":
                    old_paths = {
                        "world_spec": "quests/tests/gqt006/implementation/world/goth-baddie-cyberpsycho.world.json",
                        "tweak_file": "source/resources/r6/tweaks/ghostline/character_goth_baddie.yaml",
                    }
                    for stage in normalized["stages"]:
                        authoring = stage.get("authoring", {})
                        for key, old_path in old_paths.items():
                            if key in authoring:
                                expected = (
                                    old_path.replace("quests/tests/", "projects/test-quests/")
                                    if key == "world_spec"
                                    else "projects/test-quests/gqt006/" + old_path
                                )
                                self.assertEqual(authoring[key], expected)
                                authoring[key] = old_path
                self.assertEqual(
                    digest(normalized),
                    EXPECTED[name]["manifest"],
                )

    def test_all_root_and_child_phase_data_remains_exact(self):
        for name, module in self.builds.items():
            with self.subTest(quest=name):
                phases = {
                    artifact.stage_id or "root": digest(
                        artifact.document["Data"]["RootChunk"]
                    )
                    for artifact in module.quest_artifacts()
                    if artifact.archive_path.suffix == ".questphase"
                }
                self.assertEqual(phases, EXPECTED[name]["phases"])

    def test_journal_retains_all_nonempty_entries_and_typed_metadata(self):
        for name, module in self.builds.items():
            with self.subTest(quest=name):
                content = journal_content(
                    module.generate_journal()["Data"]["RootChunk"]
                )
                self.assertEqual(digest(content), EXPECTED[name]["journal"])

    def test_onscreen_keys_and_text_are_preserved_exactly(self):
        for name, module in self.builds.items():
            with self.subTest(quest=name):
                entries = onscreen_content(module.generate_onscreens())
                self.assertEqual(digest(entries), EXPECTED[name]["onscreen"])
                self.assertEqual(
                    len(entries), len({entry["secondaryKey"] for entry in entries})
                )
                self.assertTrue(all(entry["primaryKey"] == "0" for entry in entries))

    def test_braindance_counter_tracks_the_review_clue_contract(self):
        module = self.builds["gqt005"]
        objective = find_entry(
            module.generate_journal(),
            "gameJournalQuestObjective",
            "gqt005_01_obj_review_braindance",
        )["Data"]
        self.assertEqual(objective["counter"], len(module.review_clue_facts()))
        self.assertEqual(objective["counter"], 3)
        self.assertEqual(
            digest(module.generate_launch_scene()["Data"]["RootChunk"]),
            EXPECTED["gqt005"]["special"]["launch_scene"],
        )

    def test_regina_brief_and_outcome_report_metadata_remains_intact(self):
        document = self.builds["gqt006"].generate_journal()
        contact = find_entry(document, "gameJournalContact", "regina_jones")["Data"]
        self.assertEqual(contact["name"]["unk1"], "1663239980823232512")
        conversation = contact["entries"][0]["Data"]
        self.assertEqual(
            [entry["Data"]["id"] for entry in conversation["entries"]],
            [
                "00_msg_ncpd_brief",
                "01_msg_status",
                "02a_msg_killed",
                "02b_msg_spared",
                "02c_msg_truce",
                "03_ch_response",
                "04a_msg_shard",
                "04b_msg_context",
                "05_msg_complete",
            ],
        )
        brief = conversation["entries"][0]["Data"]
        self.assertEqual((brief["delay"], brief["isQuestImportant"]), (3, 1))
        self.assertEqual(
            brief["attachment"]["Data"]["realPath"], "quests/minor_quest/gqt006"
        )
        for entry_id in ("02a_msg_killed", "02b_msg_spared", "02c_msg_truce"):
            self.assertEqual(
                find_entry(document, "gameJournalPhoneMessage", entry_id)["Data"][
                    "sender"
                ],
                "Player",
            )

    def test_barry_lipsync_subtitle_voice_and_scene_data_remain_exact(self):
        module = self.builds["gqt007"]
        for key, factory in {
            "lipmap": module.generate_lipmap,
            "subtitles": module.generate_subtitles,
            "subtitle_map": module.generate_subtitle_map,
            "vo_map": module.generate_vomap,
            "scene": lambda: module.generate_scene()[0],
        }.items():
            with self.subTest(resource=key):
                self.assertEqual(
                    digest(factory()["Data"]["RootChunk"]),
                    EXPECTED["gqt007"]["special"][key],
                )

    def test_world_documents_remain_exact(self):
        for name, module in self.builds.items():
            with self.subTest(quest=name):
                outputs, documents = module.world_builder.build_world_documents(
                    load(module.WORLD_SPEC),
                    ROOT / "source/raw",
                    ROOT / "source/archive",
                )
                self.assertEqual(
                    [
                        digest(documents[item.raw_path]["Data"]["RootChunk"])
                        for item in outputs
                    ],
                    EXPECTED[name]["world"],
                )

    def test_collectors_build_complete_unique_sets_without_writing(self):
        for name, module in self.builds.items():
            with self.subTest(quest=name), tempfile.TemporaryDirectory() as folder:
                output_root = Path(folder) / "output"
                if name == "gqt005":
                    # RID linking has its own detailed tests. Isolate this collector
                    # contract from external animation-import output under .tmp.
                    placeholder = Path(folder) / "inputs.json"
                    placeholder.write_text("{}", encoding="utf-8")
                    with mock.patch.object(
                        module,
                        "link_scene_document",
                        return_value=(load(module.SCENE_RAW), {"ok": True}),
                    ):
                        artifacts = module.build_artifacts(
                            output_root, rid_json=placeholder, handoff=placeholder
                        )
                else:
                    artifacts = module.build_artifacts(output_root)
                self.assertFalse(
                    output_root.exists(), "Collecting artifacts must not publish files"
                )
                self.assertEqual(
                    len(artifacts), len({artifact.raw_path for artifact in artifacts})
                )
                self.assertTrue(
                    all(
                        artifact.raw_path.is_relative_to(output_root / "source/raw")
                        for artifact in artifacts
                    )
                )
                self.assertTrue(
                    all(
                        artifact.archive_path.is_relative_to(
                            output_root / "source/archive"
                        )
                        for artifact in artifacts
                    )
                )
                names = {artifact.raw_path.name for artifact in artifacts}
                self.assertIn(module.JOURNAL_RAW.name, names)
                self.assertIn(module.ONSCREEN_RAW.name, names)
                self.assertIn(module.ROOT_PHASE_RAW.name, names)
                published = quest_build.publish_build(
                    artifacts, namespace=name, output_root=output_root
                )
                self.assertEqual(len(published), len(artifacts))
                self.assertTrue(
                    all(
                        raw.is_file() and not archive.exists()
                        for raw, archive in published
                    )
                )


if __name__ == "__main__":
    unittest.main()
