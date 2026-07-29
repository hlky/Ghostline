from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "quest_compiler", ROOT / "tools/quest_compiler.py"
)
assert SPEC and SPEC.loader
quest_compiler = importlib.util.module_from_spec(SPEC)
sys.modules["quest_compiler"] = quest_compiler
SPEC.loader.exec_module(quest_compiler)


class TestQuestManifestTests(unittest.TestCase):
    def test_signal_delay_has_the_expected_linear_contract(self) -> None:
        path = (
            ROOT
            / "quests/tests/gqt001_signal_delay.quest.json"
        )
        spec, diagnostics = quest_compiler.load_spec(path)
        self.assertIsNotNone(spec)
        assert spec is not None
        self.assertFalse(
            [diagnostic for diagnostic in diagnostics if diagnostic.level == "error"]
        )
        self.assertEqual(
            [stage.type for stage in spec.stages],
            [
                "reach_area",
                "read_terminal_document",
                "time_gate",
                "phone_conversation",
            ],
        )
        self.assertNotIn("output_socket", spec.stages[1].data)
        self.assertEqual(
            spec.stages[1].data["completion_fact"],
            "gqt001_document_read",
        )
        self.assertEqual(
            spec.stages[-1].data["complete_quest"],
            "quests/minor_quest/gqt001",
        )

    def test_signal_delay_is_ready_for_runtime_validation(self) -> None:
        path = (
            ROOT
            / "quests/tests/gqt001_signal_delay.quest.json"
        )
        spec, _ = quest_compiler.load_spec(path)
        assert spec is not None
        self.assertEqual(
            [stage.status for stage in spec.stages],
            ["ready", "ready", "ready", "ready"],
        )

    def test_signal_delay_uses_a_minimal_laptop_instance_patch(self) -> None:
        path = (
            ROOT
            / "source/raw/mod/gqt001/world"
            / "gqt001_laptop_instance.streamingsector.json"
        )
        resource = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(
            resource["Data"]["RootChunk"]["$type"],
            "worldStreamingSector",
        )
        self.assertEqual(len(resource["Data"]["RootChunk"]["nodes"]), 1)
        self.assertEqual(len(resource["Data"]["RootChunk"]["nodeData"]["Data"]), 1)
        self.assertEqual(len(resource["Data"]["EmbeddedFiles"]), 0)
        node = resource["Data"]["RootChunk"]["nodes"][0]["Data"]
        package = node["instanceData"]["Data"]["buffer"]["Data"]
        self.assertEqual(
            package["CruidDict"],
            {
                "0": "1108512084555509772",
                "1": "1131680419258347532",
                "2": "1131680419258347552",
            },
        )
        controllers = [
            chunk["persistentState"]["Data"]
            for chunk in package["Chunks"]
            if chunk["persistentState"]["Data"]["$type"]
            == "ComputerControllerPS"
        ]
        self.assertEqual(len(controllers), 2)
        for controller in controllers:
            setup = controller["computerSetup"]
            self.assertEqual(setup["mailsMenu"], 0)
            self.assertEqual(setup["mailsStructure"], [])
            self.assertEqual(setup["internetMenu"], 0)
            self.assertEqual(setup["internetSubnet"]["startingPage"], "")
            self.assertEqual(setup["newsFeedMenu"], 0)
            self.assertEqual(setup["newsFeed"], [])
            self.assertEqual(
                setup["filesStructure"][0]["content"][0]["questInfo"][
                    "factName"
                ]["$value"],
                "gqt001_document_read",
            )
        scanners = [
            chunk
            for chunk in package["Chunks"]
            if chunk["$type"] == "gameScanningComponent"
        ]
        self.assertEqual(len(scanners), 1)
        self.assertEqual(scanners[0]["clues"], [])

    def test_signal_delay_registers_owned_laptop_sector(self) -> None:
        config = (
            ROOT / "source/resources/Ghostline.archive.xl"
        ).read_text(encoding="utf-8")
        self.assertNotIn(
            r"mod\gqt001\world\gqt001_laptop_instance.streamingsector:",
            config,
        )

        block = json.loads(
            (
                ROOT
                / "source/raw/mod/gqt001/world"
                / "gqt001_signal_delay.streamingblock.json"
            ).read_text(encoding="utf-8")
        )
        paths = [
            descriptor["data"]["DepotPath"]["$value"]
            for descriptor in block["Data"]["RootChunk"]["descriptors"]
        ]
        self.assertIn(
            r"mod\gqt001\world\gqt001_laptop_instance.streamingsector",
            paths,
        )

        sector = json.loads(
            (
                ROOT
                / "source/raw/mod/gqt001/world"
                / "gqt001_laptop_instance.streamingsector.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(
            sector["Data"]["RootChunk"]["nodeRefs"][0]["$value"],
            "$/mod/gqt001/#gqt001_pr_signal_delay/#gqt001_terminal_laptop_r2",
        )


if __name__ == "__main__":
    unittest.main()
