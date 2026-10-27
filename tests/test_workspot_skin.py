"""Rest-pose, hierarchy and vertex-weight checks for the skinned renderer."""
from pathlib import Path
import sys
import unittest

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import workspot_skin as skin


def bone(name, parent, position):
    return {"name": name, "parent": parent, "model_rest": {"translation": position, "rotation": [0, 0, 0, 1], "scale": [1, 1, 1]}}


class WorkspotSkinTests(unittest.TestCase):
    def test_rest_pose_preserves_vertices_and_auxiliary_rest_offset(self):
        contract = {"bones": [bone("Hips", -1, [0, 0, 1]), bone("helper", 0, [0, .1, 1])]}
        rest = skin.rest_matrix(contract["bones"][0])
        deltas = skin.deformation_deltas({"Hips": rest}, contract)
        for delta in deltas.values():
            np.testing.assert_allclose(delta, np.eye(4))
        rest[0, 3] += 2
        posed = skin.deformation_deltas({"Hips": rest}, contract)
        self.assertEqual(posed["helper"][0, 3], 2)

    def test_weighted_skinning_blends_joint_motion(self):
        part = {"vertices": np.array([[0., 0., 1.]]), "joints": np.array([[0, 1]]), "weights": np.array([[.25, .75]]), "joint_names": ["a", "b"]}
        a, b = np.eye(4), np.eye(4)
        a[0, 3], b[0, 3] = 4, 8
        np.testing.assert_allclose(skin.skin_vertices(part, {"a": a, "b": b}), [[7, 0, 1]])
        with self.assertRaisesRegex(ValueError, "absent from deformation rig"):
            skin.skin_vertices(part, {"a": a})

    def test_head_attachment_uses_rotation_and_translation(self):
        part = {"vertices": np.array([[1., 0., 0.]]), "rigid_head": True}
        matrix = skin.transform([0, 0, 1], [0, 0, np.sqrt(.5), np.sqrt(.5)], [1, 1, 1])
        np.testing.assert_allclose(skin.skin_vertices(part, {}, matrix), [[0, 1, 1]], atol=1e-12)

    def test_named_joint_models_follow_source_hierarchy(self):
        actor = {"bone_names": ["root", "child"], "parents": [-1, 0], "local_translations": [[[2, 0, 0], [0, 0, 1]]], "local_rotations": [[[0, 0, 0, 1], [0, 0, 0, 1]]], "local_scales": [[[1, 1, 1], [1, 1, 1]]]}
        np.testing.assert_allclose(skin.model_matrices(actor, 0)["child"][:3, 3], [2, 0, 1])

    def test_strided_normalized_skin_weights(self):
        document = {"accessors": [{"bufferView": 0, "componentType": 5121, "type": "VEC2", "count": 2, "normalized": True}], "bufferViews": [{"byteOffset": 1, "byteStride": 4}]}
        raw = bytes([0, 255, 0, 99, 99, 0, 255])
        np.testing.assert_allclose(skin.accessor(document, raw, 0), [[1, 0], [0, 1]])
        with self.assertRaisesRegex(ValueError, "exceeds"):
            skin.accessor(document, raw[:-1], 0)


if __name__ == "__main__":
    unittest.main()
