"""Evidence boundary regressions for cinematic research."""
import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from analyze_cinematic_scenes import metrics
from verify_cinematic_scenes import resolve, rid_binding


class CinematicEvidenceTests(unittest.TestCase):
    def test_sections_do_not_become_one_timeline_and_omission_is_preserved(self):
        record = {"raw_sha256": "raw", "binary_sha256": "binary", "screenplay_lines": [],
            "interruption_scenarios": [], "events": [
                {"node": "1", "handle": "10", "pointer": "/a", "data": {"$type": "scnDialogLineEvent"}},
                {"node": "2", "handle": "11", "pointer": "/b", "data": {"$type": "scnPlaySkAnimEvent", "startTime": 0}},
            ]}
        result = metrics(record)
        self.assertEqual(result["section_capabilities"], {"1": ["speech"], "2": ["skeletal_animation"]})
        self.assertEqual(result["explicit_event_fields"], {"startTime": 1})
        self.assertNotIn("duration", record["events"][0]["data"])

    def test_rid_reference_index_is_not_resource_id_or_serial_number(self):
        root = {"resouresReferences": {"ridAnimations": [
            {"resourceId": {"id": 400}, "animationSN": {"serialNumber": 19}}]},
            "ridResources": [{"id": {"id": 400}, "ridResource": {"DepotPath": {"$value": "test.scenerid"}}}]}
        binding = rid_binding(root, {"$type": "scnPlayRidAnimEvent", "animResRefId": {"id": 0}})
        self.assertEqual((binding["index"], binding["resource_id"], binding["serial_number"]), (0, 400, 19))

    def test_pointer_preserves_escaped_keys_and_list_indices(self):
        self.assertEqual(resolve({"a/b": [{"~x": 7}]}, "/a~1b/0/~0x"), 7)


if __name__ == "__main__":
    unittest.main()
