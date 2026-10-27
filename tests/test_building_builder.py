"""Geometry contracts for the parametric building compiler."""
import base64
import copy
import json
import math
from pathlib import Path
import struct
import sys
import threading
import unittest
from http.client import HTTPConnection
from http.server import ThreadingHTTPServer

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from building_builder import BuildingError, collision_node, compile_layout, native_documents
from building_ui import BuildingHandler


class BuildingTests(unittest.TestCase):
    def setUp(self):
        self.layout = json.loads((Path(__file__).resolve().parents[1] / "projects/experiments/building-lab/buildings/workshop.building.json").read_bytes())

    def test_shared_wall_is_emitted_once(self):
        scene = compile_layout(self.layout)
        shared = [e for e in scene["edges"] if e["shared"]]
        self.assertEqual(len(shared), 2)
        self.assertEqual(scene["stats"]["walls"], 16)
        self.assertEqual(len({i["id"] for i in scene["instances"]}), len(scene["instances"]))
        self.assertEqual(scene, compile_layout(copy.deepcopy(self.layout)))

    def test_doorway_has_clear_player_aperture(self):
        scene = compile_layout(self.layout)
        parts = [s for s in scene["solids"] if s["edge"] == "0:x:1:0"]
        self.assertEqual(len(parts), 3)
        # The player-facing opening at X=4.5, Z=1.2 is outside all boxes.
        for part in parts:
            self.assertFalse(all(abs(v - c) < size / 2 for v, c, size in zip([4.5, .115, 1.2], part["center"], part["size"])))
        self.layout["openings"]["0:x:1:0"] = "passage"
        opened = compile_layout(self.layout)
        self.assertFalse(any(s["edge"] == "0:x:1:0" for s in opened["solids"]))
        self.assertFalse(any(i["edge"] == "0:x:1:0" for i in opened["instances"]))

    def test_reconcile_requires_explicit_opt_in(self):
        self.layout["openings"]["0:x:99:99"] = "doorway"
        with self.assertRaises(BuildingError):
            compile_layout(self.layout)
        result = compile_layout(self.layout, reconcile=True)
        self.assertEqual(result["removed_openings"], ["0:x:99:99"])
        self.assertEqual(len(result["layout"]["openings"]), 2)
        self.assertIn("0:x:99:99", self.layout["openings"])

    def test_world_anchor_rotates_visuals_and_physics_together(self):
        self.layout["origin"] = {"x": 100, "y": -200, "z": 40, "yaw": 90}
        result = compile_layout(self.layout)
        for item in result["instances"] + result["solids"]:
            point = item.get("position", item.get("center"))
            world = item.get("world_position", item.get("world_center"))
            for actual, expected in zip(world, [100 - point[1], -200 + point[0], 40 + point[2]]):
                self.assertAlmostEqual(actual, expected)
            self.assertEqual(item["world_yaw"], item["yaw"] + 90)

    def test_collision_buffer_decodes_to_world_box(self):
        self.layout["origin"] = {"x": 100, "y": -200, "z": 40, "yaw": 90}
        solid = compile_layout(self.layout)["solids"][0]
        node = collision_node(solid, 1)
        raw = base64.b64decode(node["compiledData"]["Bytes"])
        self.assertEqual(len(raw), 101)
        actor = struct.unpack_from("<4i4fHHhhQ", raw)
        for actual, expected in zip(actor[:3], solid["world_center"]):
            self.assertAlmostEqual(actual / 131072, expected, places=5)
        self.assertAlmostEqual(actor[6], math.sqrt(.5), places=6)
        self.assertEqual(actor[8:11], (0, 1, -1))
        half = struct.unpack_from("<3f", raw, 48)
        for actual, expected in zip(half, solid["size"]):
            self.assertAlmostEqual(actual * 2, expected)

    def test_upper_floor_and_native_counts(self):
        self.layout["rooms"][1]["level"] = 1
        self.layout["openings"] = {}
        result = compile_layout(self.layout)
        upper = [i for i in result["instances"] if i["level"] == 1 and i["role"] == "floor"]
        self.assertEqual(len(upper), 4)
        self.assertTrue(all(i["position"][2] == 4.2 for i in upper))
        sector, block, _ = native_documents(result, Path("test-output"))
        root = sector["Data"]["RootChunk"]
        self.assertEqual(len(root["nodes"]), len(result["instances"]) + len(result["solids"]) + 2)
        self.assertEqual(len(root["nodes"]), len(root["nodeData"]["Data"]))
        self.assertEqual(len(block["Data"]["RootChunk"]["descriptors"]), 1)

    def test_invalid_layouts_are_rejected(self):
        for field, value in (("x", True), ("width", 4), ("depth", float("nan")), ("level", 1.5), ("x", 60)):
            with self.subTest(field=field, value=value):
                layout = copy.deepcopy(self.layout)
                layout["rooms"][0][field] = value
                with self.assertRaises(BuildingError):
                    compile_layout(layout)
        self.layout["rooms"][1]["x"] = 0
        with self.assertRaises(BuildingError):
            compile_layout(self.layout)

    def test_http_compile_and_request_boundaries(self):
        server = ThreadingHTTPServer(("127.0.0.1", 0), BuildingHandler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            connection = HTTPConnection("127.0.0.1", server.server_port)
            connection.request("POST", "/api/compile", json.dumps({"layout": self.layout}), {"Content-Type": "application/json"})
            response = connection.getresponse()
            self.assertEqual(response.status, 200)
            self.assertEqual(json.loads(response.read())["stats"]["area"], 90)
            connection.request("POST", "/api/compile", "[]", {"Content-Type": "application/json"})
            response = connection.getresponse()
            self.assertEqual(response.status, 422)
            response.read()
            connection.request("POST", "/api/save", json.dumps({"layout": self.layout}), {"Content-Type": "application/json", "Origin": "https://example.invalid"})
            response = connection.getresponse()
            self.assertEqual(response.status, 422)
            self.assertIn("local editor", json.loads(response.read())["error"])
            connection.request("GET", "/%2e%2e/building_builder.py")
            response = connection.getresponse()
            self.assertEqual(response.status, 404)
            response.read()
            connection.close()
        finally:
            server.shutdown()
            server.server_close()
            thread.join()


if __name__ == "__main__":
    unittest.main()
