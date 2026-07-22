import unittest

from tools.find_collision_instances import find_matches, fingerprint_hashes


def actor(x, shape_hash):
    return {
        "Position": {
            "x": {"Bits": int(x * 131072)},
            "y": {"Bits": 0},
            "z": {"Bits": 0},
        },
        "Orientation": {"i": 0, "j": 0, "k": 0, "r": 1},
        "Scale": {"X": 1, "Y": 1, "Z": 1},
        "Shapes": [{"ShapeType": "TriangleMesh", "Hash": str(shape_hash)}],
    }


class FindCollisionInstancesTests(unittest.TestCase):
    def setUp(self):
        self.document = {
            "Data": {
                "RootChunk": {
                    "nodes": [
                        {
                            "Data": {
                                "$type": "worldCollisionNode",
                                "debugName": {"$value": "NormalCollisionNode_087"},
                                "sourcePrefabHash": "42",
                                "compiledData": {"Data": {"Actors": [actor(1, 99), actor(2, 100)]}},
                            }
                        },
                        {
                            "Data": {
                                "$type": "worldCollisionNode",
                                "debugName": {"$value": "AnotherNode"},
                                "sourcePrefabHash": "43",
                                "compiledData": {"Data": {"Actors": [actor(3, 99)]}},
                            }
                        },
                    ]
                }
            }
        }

    def test_fingerprint_finds_matching_actors_across_nodes(self):
        hashes = fingerprint_hashes(self.document, "NormalCollisionNode_087", 0, "42")
        self.assertEqual(hashes, {"99"})
        matches = find_matches(self.document, hashes)
        self.assertEqual([row["actor_index"] for row in matches], [0, 0])
        self.assertEqual([row["position"]["x"] for row in matches], [1.0, 3.0])


if __name__ == "__main__":
    unittest.main()
