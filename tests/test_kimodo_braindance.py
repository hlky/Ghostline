from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "tools") not in sys.path:
    sys.path.insert(0, str(ROOT / "tools"))
MODULE_PATH = ROOT / "tools" / "kimodo_braindance.py"
SPEC = importlib.util.spec_from_file_location("kimodo_braindance", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
kimodo = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(kimodo)


class KimodoBraindanceTests(unittest.TestCase):
    def test_inspect_bvh_reads_hierarchy_and_frames(self) -> None:
        content = """HIERARCHY
ROOT Root
{
  JOINT Hips
  {
    JOINT Spine1
    {
    }
  }
}
MOTION
Frames: 150
Frame Time: 0.0333333
"""
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "motion.bvh"
            path.write_text(content, encoding="utf-8")
            joints, frames = kimodo.inspect_bvh(path)
        self.assertEqual(joints, ("Root", "Hips", "Spine1"))
        self.assertEqual(frames, 150)

    def test_build_command_targets_existing_blend(self) -> None:
        command = kimodo.build_blender_command(
            Path("blender.exe"),
            blend=Path("existing.blend"),
            output_blend=Path("existing.blend"),
            bvh=Path("kimodo.bvh"),
            actor="patch",
            start_frame=0,
            end_frame=149,
            blend_in=8,
            blend_out=15,
            report=Path("report.json"),
        )
        self.assertEqual(command[:3], ["blender.exe", "--background", "existing.blend"])
        self.assertIn("patch", command)
        self.assertEqual(command[command.index("--output-blend") + 1], "existing.blend")

    def test_gqt005_patch_actor_exists(self) -> None:
        spec = kimodo.load_spec(ROOT / "projects/test-quests/gqt005/braindance/gqt005_braindance_analysis.json")
        actor = kimodo.find_actor(spec, "patch")
        self.assertEqual(actor["actor_id"], 0)


if __name__ == "__main__":
    unittest.main()
