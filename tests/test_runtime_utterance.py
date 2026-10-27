from __future__ import annotations

import copy
import importlib.util
import json
import sys
import tempfile
import unittest
import wave
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from runtime_utterance import export_utterance
from npc_runtime_slot_worker import MOD_PATH, SLOT_PATH, process_request


class RuntimeUtteranceTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.audio = self.root / "line.wav"
        with wave.open(str(self.audio), "wb") as output:
            output.setparams((1, 2, 1000, 0, "NONE", "not compressed"))
            output.writeframes(b"\0\0" * 1000)
        self.alignment = {
            "locstring_id": "42", "text": "Hello", "audio_path": "line.wav",
            "audio_duration": 1.0, "phones": ["AA"], "device": "cpu",
            "alignment": [{"phone": "AA", "start": 0.2, "end": 0.8,
                           "score": 0.9, "token_start": 0.2, "token_end": 0.8}],
        }
        self.model = {
            "tracks": ["jaw_mid_openLipsyncPoseOutput"], "phase": [0, 0.5, 1],
            "silence": {"median": [0]},
            "phones": {"AA": {"curves": {"median": [[0], [0.7], [0]]}}},
            "contexts": {"previous": [], "next": []},
            "boundaries": {"AA": {"anticipation_ms": 0, "anticipation_censored": False,
                                    "release_ms": 0, "release_censored": False}},
        }

    def export(self):
        return export_utterance(self.audio, self.alignment, self.model,
                                utterance_id="why_you", npc_id="runtime_patch", audio_file="audio/why_you.wav")

    def test_real_synthesis_has_negative_override_and_releases_at_end(self):
        result = self.export()
        self.assertEqual(result["curves"]["tracks"], ["jaw_mid_openLipsyncPoseOutput", "jaw_mid_openAnimOverrideWeight"])
        matrix = np.asarray(result["curves"]["values"])
        self.assertGreater(matrix[:, 0].max(), 0.5)
        np.testing.assert_allclose(matrix[:, 1], -matrix[:, 0])
        np.testing.assert_allclose(matrix[[0, -1]], 0)
        self.assertEqual(result["curves"]["times"][-1], result["audio"]["duration"])

    def test_rejects_alignment_for_a_different_wave(self):
        self.alignment["audio_duration"] = 2.0
        with self.assertRaisesRegex(ValueError, "duration"):
            self.export()

    def test_slot_publish_validates_audio_before_replacing_placeholder(self):
        utterance = self.export()
        mod = self.root / MOD_PATH
        (mod / "utterances").mkdir(parents=True)
        (mod / "audio").mkdir()
        (mod / "utterances/why_you.json").write_text(json.dumps(utterance))
        (mod / "audio/why_you.wav").write_bytes(self.audio.read_bytes())
        slot = self.root / SLOT_PATH
        slot.parent.mkdir(parents=True)
        slot.write_bytes(b"placeholder")
        request = {"token": "session:turn:1", "utterance_id": "why_you"}
        ready = process_request(self.root, request)
        self.assertEqual(ready["status"], "ready")
        self.assertEqual(slot.read_bytes(), self.audio.read_bytes())
        slot.write_bytes(b"placeholder")
        (mod / "audio/why_you.wav").write_bytes(b"corrupt")
        failed = process_request(self.root, request)
        self.assertEqual(failed["status"], "error")
        self.assertEqual(slot.read_bytes(), b"placeholder")

    def test_slot_rejects_unregistered_line_ids(self):
        response = process_request(self.root, {"token": "1", "utterance_id": "../../elsewhere"})
        self.assertEqual(response["status"], "error")

    def test_graph_preserves_native_branch_and_has_unique_handles(self):
        path = ROOT / "projects/experiments/npc-runtime/implementation/build.py"
        spec = importlib.util.spec_from_file_location("npc_runtime_build", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        document = {"Data": {"RootChunk": {"HandleId": "0", "Data": {
            "$type": "animAnimNode_Sermo", "inputLink": {"$type": "animPoseLink", "node": {
                "HandleId": "1", "Data": {"$type": "animAnimNode_FacialMixerSlot"}}}}}}}
        before = copy.deepcopy(document)
        graph, contract = module.runtime_graph(document, ["jaw_mid_openLipsyncPoseOutput", "jaw_mid_openAnimOverrideWeight"])
        self.assertEqual(document, before)
        nodes = list(module.walk(graph))
        gate = next(n for n in nodes if n.get("$type") == "animAnimNode_Switch")
        self.assertEqual(gate["inputNodes"][0], before["Data"]["RootChunk"]["Data"]["inputLink"])
        handles = [n["HandleId"] for n in nodes if "HandleId" in n]
        self.assertEqual(len(handles), len(set(handles)))
        inputs = {n["name"]["$value"] for n in nodes if n.get("$type") == "animAnimNode_FloatInput"}
        self.assertEqual(inputs, {contract["gate"], *contract["inputs"].values()})


if __name__ == "__main__":
    unittest.main()
