"""Frozen pre-migration contracts for the three legacy test-quest builders.

Goldens were captured before migration under generated/quest-migration/legacy-baseline.
They cover normalized inputs, complete phase graphs, world/device payloads, journal
paths/content, and localization. Headers and journal handle allocation are excluded;
phone entry order is checked separately because it controls the displayed thread.
Approved corrections to the captured compiler baseline: GQT001/GQT004 child
prefab scopes match reviewed raw resources, and GQT004's live cleanup vehicle
token resolves to the reviewed record. All other artifact fields stay exact.
"""

from __future__ import annotations

import copy
from contextlib import redirect_stdout
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from quest_authoring import normalize_spec, resolve_bindings
from tests.test_quest_authoring import journal_contract, onscreen_contract

NAMES = {
    "gqt001": "gqt001_signal_delay",
    "gqt002": "gqt002_quiet_install",
    "gqt004": "gqt004_vehicle_lab",
}
MANIFEST_HASHES = {
    "gqt001": "167e9b17e3a36a0fb0b63f81a5c426e35027c5fd9efecbe6d1ba54175f932e50",
    "gqt002": "29ac485c7d464c81cde6bca1dcd3da52ad98d7c212f294b3b91f66d48d2c0f55",
    "gqt004": "e4786bd5ed4227d52744b88b1136a48bda84e4adef3b360413679a8c8a80af13",
}
EXPECTED = {
    "gqt001": {
        "mod/gqt001/journal/gqt001.journal": "ca4eb4d52c11ecc8fbd53fe427939db6943a6eea2751f9ed2035e56d2312a59a",
        "mod/gqt001/localization/en-us/onscreens/gqt001.json": "45b09cdf74cfc8fa638313805e6c8f09849814fb484094ea0bde0838f296d01d",
        "mod/gqt001/phases/gqt001_confirm_result.questphase": "6e0f9cad27d0dee1e99f853b054a874a8613a6d97ca6fd51b7d6b62652a1499b",
        "mod/gqt001/phases/gqt001_reach_terminal.questphase": "92108ce8931db3788a1b7a75ba4cf3f6ad3480feac6c27d3eb0ad42ef4baa27c",
        "mod/gqt001/phases/gqt001_read_diagnostic.questphase": "a5c3334c138c90ce04b5e147be93c9a5c080c486a52fbff03ac3c1f41b004672",
        "mod/gqt001/phases/gqt001_signal_delay.questphase": "07d5df8c613ab68fe12462bb8ff22878a200a3b3d7dd3d38553d8ac5d6cb0665",
        "mod/gqt001/phases/gqt001_wait_for_reply.questphase": "618e62b1bcb21060f84953cec386fa6cf16ea0486c73a6c90ddf1878271bbee1",
        "mod/gqt001/world/gqt001_custom_devices.devices": "3e3d9a591d78b51d991ee29090e05d3680fa62c3c260367079127704eb9c0010",
        "mod/gqt001/world/gqt001_laptop_instance.streamingsector": "9f1b900739b252aa69ba191fca3eb9fc3fc2579fe8f2a59dd3f1d51142dc2526",
        "mod/gqt001/world/gqt001_signal_delay.streamingblock": "5f9f6b258f337fc9a9a303d1dcbdde8a86141aeacd14e18860629334ee474c96",
    },
    "gqt002": {
        "mod/gqt002/journal/gqt002.journal": "25f43ca4ce30db02ed02f6f02d92cbabbb4f49127df52bbd8b844c6a1de771b9",
        "mod/gqt002/localization/en-us/onscreens/gqt002.json": "1a1ee10fe40b6fcddb19f3234d193c1f9238bcd9ce88f72f8dec6358c7eade04",
        "mod/gqt002/phases/gqt002_detect_guards.questphase": "d36633b3e4cef7b14f0deb102c16750b5fc4f8c7d25d80bd247000410714c6dc",
        "mod/gqt002/phases/gqt002_plant_keylogger.questphase": "67ed1c70c239f93b4bd501e6b73608b80b6a785d80d39365f5b8fc3929d1990b",
        "mod/gqt002/phases/gqt002_quiet_install.questphase": "3dd1391bba4e5f61257f53c7b256f61e5e4fc213126a52b25771eed7b1ef7b06",
        "mod/gqt002/phases/gqt002_remain_undetected.questphase": "b77f41b060e96f49fc27b20a9f34db74b63d1d0018786dbdd8aac4bd7a6f3f8f",
        "mod/gqt002/templates/gqt002_guarded_plant.questphase": "4c34369806083e6cce1a6a5b05a9fad43faf2b21719d6f48d1fd0ba4d610889a",
        "mod/gqt002/world/gqt002_always_loaded.streamingsector": "7df3fcb150d736004ccbf8ce4931e4b1297c87e210ac20ffa0e100de345c078e",
        "mod/gqt002/world/gqt002_custom_devices.devices": "fe4962388bed9bc8e5230e3a2b110e3ad0351ac20e36aa8fb102af0a074741d8",
        "mod/gqt002/world/gqt002_laptop_instance.streamingsector": "f1327be58d700b80ffa6d1d431f913ef8de6ef73c9ced63780b4ac05f3fc0c9e",
        "mod/gqt002/world/gqt002_quiet_install.streamingblock": "9f8dd4ed84df21d9ce6aeda690dd769378b255e469ddaa2197f59241bff9ac7f",
        "mod/gqt002/world/gqt002_quiet_install.streamingsector": "e55d25a5f520621e1e931b4228bc5c3e8a9f05704a9d474ca5186ef32c4128eb",
        "mod/gqt002/world/gqt002_security.streamingsector": "50daf833f86e621bd4228a43f38b84d54a7476ea86a1e4fe4e40f18e02c5b4d7",
    },
    "gqt004": {
        "mod/gqt004/journal/gqt004.journal": "ca29a982bd18a864913b08c24e8c68b999fc9e93723244afc303444412cc8007",
        "mod/gqt004/localization/en-us/onscreens/gqt004.json": "a1d876c5306552766eb15cd2835f6b7ada3b426905dcbde4029c1434974b21f2",
        "mod/gqt004/phases/gqt004_cleanup_test_vehicle.questphase": "6b522014ed954de294e82b2c780da8a5508143e41154db8c956f59b56b6491aa",
        "mod/gqt004/phases/gqt004_deliver_test_vehicle.questphase": "8b4a76f3887cd64e9a4dc680e1a2cbf0935bf0e725d48ef4e3e353535bf8b917",
        "mod/gqt004/phases/gqt004_drive_contact_to_destination.questphase": "b224800392837f302fdb4ef4c6aab842ecfbe11d6ca8f66ca23e283a583fced3",
        "mod/gqt004/phases/gqt004_enter_contact_vehicle.questphase": "62822b1099268a2d6cca05b5d1db9c17480506d61ac3601a5439993a00ac5cbb",
        "mod/gqt004/phases/gqt004_ride_with_patch.questphase": "48bb87b1b02c5f25084ba6d5cbcdde592a6c2f8fd76b5be1b1c7439c10a47272",
        "mod/gqt004/phases/gqt004_steal_test_vehicle.questphase": "6481a956169138c9521d8c0529229376191a0a7d72ce15efd2a892df0a71fed7",
        "mod/gqt004/phases/gqt004_vehicle_lab.questphase": "36ca5faeac17b12d73d418a196cb038e07aba25304c7c5d4f56e3cb790d797ef",
        "mod/gqt004/templates/gqt004_final_cleanup.questphase": "ce5dc31518e9097e4d1725fb8c43d8297c7f1fa8c96e98d54046c6185b7c7166",
    },
}


def digest(value):
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def payload(depot, document):
    if depot.endswith(".journal"):
        return journal_contract(document)
    if "/onscreens/" in depot:
        return onscreen_contract(document)["Data"]
    return document["Data"]


def publish_candidate(module, output):
    with redirect_stdout(io.StringIO()):
        return module.main(["--output-root", str(output)])


class LegacyQuestMigrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.builders = {}
        for qid in NAMES:
            path = ROOT / f"projects/test-quests/{qid}/implementation/build.py"
            spec = importlib.util.spec_from_file_location(
                f"legacy_migration_{qid}", path
            )
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            cls.builders[qid] = module

    def test_composition_preserves_every_normalized_manifest_field(self):
        for qid, module in self.builders.items():
            with self.subTest(quest=qid):
                raw = json.loads(module.MANIFEST.read_text(encoding="utf-8"))
                self.assertIn("composition", raw)
                self.assertEqual(digest(normalize_spec(raw)), MANIFEST_HASHES[qid])
                self.assertFalse(hasattr(module, "TEXT"))
                self.assertFalse(hasattr(module, "OBJECTIVES"))

    def test_complete_artifact_payloads_preserve_pre_migration_contracts(self):
        for qid, module in self.builders.items():
            with self.subTest(quest=qid):
                artifacts = module.build_artifacts()
                actual = {}
                for artifact in artifacts:
                    depot = artifact.archive_path.relative_to(
                        module.PROJECT / "source/archive"
                    ).as_posix()
                    self.assertNotIn(depot, actual)
                    actual[depot] = digest(payload(depot, artifact.document))
                    self.assertEqual(
                        artifact.raw_path, module.PROJECT / "source/raw" / (depot + ".json")
                    )
                self.assertEqual(actual, EXPECTED[qid])

    def test_explicit_child_prefab_scopes_match_reviewed_sources(self):
        scoped = {
            "gqt001": {
                "reach_terminal",
                "read_diagnostic",
                "wait_for_reply",
                "confirm_result",
            },
            "gqt004": {
                "enter_contact_vehicle",
                "ride_with_patch",
                "drive_contact_to_destination",
                "cleanup_test_vehicle",
            },
        }
        for qid, stage_ids in scoped.items():
            module = self.builders[qid]
            manifest = normalize_spec(
                json.loads(module.MANIFEST.read_text(encoding="utf-8"))
            )
            stages = {stage["id"]: stage for stage in manifest["stages"]}
            artifacts = {
                artifact.stage_id: artifact for artifact in module.build_artifacts()
            }
            for stage_id in stage_ids:
                with self.subTest(quest=qid, stage=stage_id):
                    artifact = artifacts[stage_id]
                    reviewed = json.loads(
                        artifact.raw_path.read_text(encoding="utf-8")
                    )["Data"]["RootChunk"].get("phasePrefabs", [])
                    references = [
                        entry["prefabNodeRef"]["$value"] for entry in reviewed
                    ]
                    self.assertEqual(stages[stage_id]["phase_prefabs"], references)
                    self.assertEqual(
                        artifact.document["Data"]["RootChunk"]["phasePrefabs"], reviewed
                    )

    def test_candidate_publication_writes_all_raw_artifacts_without_touching_archive(
        self,
    ):
        for qid, module in self.builders.items():
            with self.subTest(quest=qid), tempfile.TemporaryDirectory() as directory:
                output = Path(directory)
                artifacts = module.build_artifacts()
                originals = {
                    a.archive_path: a.archive_path.read_bytes()
                    for a in artifacts
                    if a.archive_path.exists()
                }
                self.assertEqual(publish_candidate(module, output), 0)
                emitted = sorted((output / "source/raw").rglob("*.json"))
                self.assertEqual(len(emitted), len(EXPECTED[qid]))
                self.assertFalse((output / "source/archive").exists())
                for path in emitted:
                    depot = path.relative_to(output / "source/raw").as_posix()[:-5]
                    document = json.loads(path.read_text(encoding="utf-8"))
                    self.assertEqual(
                        digest(payload(depot, document)), EXPECTED[qid][depot]
                    )
                    self.assertEqual(
                        Path(document["Header"]["ArchiveFileName"]),
                        output / "source/archive" / depot,
                    )
                self.assertEqual(
                    originals, {path: path.read_bytes() for path in originals}
                )

    def test_collection_failure_preserves_an_existing_candidate(self):
        module = self.builders["gqt002"]
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            publish_candidate(module, output)
            before = {
                path: path.read_bytes() for path in output.rglob("*") if path.is_file()
            }
            with patch.object(
                module,
                "generate_security_sector",
                side_effect=ValueError("invalid security input"),
            ):
                with self.assertRaisesRegex(ValueError, "invalid security input"):
                    publish_candidate(module, output)
            self.assertEqual(
                before,
                {
                    path: path.read_bytes()
                    for path in output.rglob("*")
                    if path.is_file()
                },
            )

    def test_world_logic_uses_shared_readable_and_fact_bindings(self):
        laptop = self.builders["gqt001"]
        bindings = resolve_bindings(
            json.loads(laptop.MANIFEST.read_text(encoding="utf-8"))
        )
        revised = copy.deepcopy(bindings)
        revised["readables"]["diagnostic"]["text"] = "A revised diagnostic."
        revised["facts"]["document_read"] = "gqt001_alternate_read"
        document = laptop.generate_instance_patch(revised)
        serialized = json.dumps(document)
        self.assertIn("A revised diagnostic.", serialized)
        self.assertIn("gqt001_alternate_read", serialized)
        self.assertNotEqual(bindings, revised)

    def test_gqt001_phone_order_and_gqt002_optional_objective_are_preserved(self):
        from quest_content import find_entry

        journal = self.builders["gqt001"].generate_journal()
        thread = find_entry(
            journal, "gameJournalPhoneConversation", "gqt001_03_confirmation"
        )["Data"]
        self.assertEqual(
            [entry["Data"]["id"] for entry in thread["entries"]],
            [
                "01_msg_signal_received",
                "02_ch_response",
                "03a_msg_clean",
                "03b_msg_slow",
                "04_msg_complete",
            ],
        )
        quiet = self.builders["gqt002"].generate_journal()
        objective = find_entry(
            quiet, "gameJournalQuestObjective", "gqt002_01_obj_remain_undetected"
        )["Data"]
        self.assertEqual(objective["optional"], 1)


if __name__ == "__main__":
    unittest.main()
