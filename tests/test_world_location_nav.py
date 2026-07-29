from __future__ import annotations

import base64
import json
import math
import struct
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import world_location_nav as nav  # noqa: E402


NO_FACE = 0x7FFF


def make_vnav(
    vertices: list[tuple[float, float, float]],
    faces: list[tuple[int, int, int]],
    *,
    connections: list[tuple[int, int, int]] | None = None,
    tile_x: int = 7,
    tile_y: int = 9,
    include_auxiliary_records: bool = False,
) -> bytes:
    connections = connections or [(NO_FACE, NO_FACE, NO_FACE) for _ in faces]
    counts = (1, 1, 1, 1, 1, 1) if include_auxiliary_records else (0, 0, 0, 0, 0, 0)
    header = struct.pack(
        "<15I",
        int.from_bytes(nav.VNAV_MAGIC, "little"),
        11,
        tile_x,
        tile_y,
        12,
        13,
        len(faces),
        len(vertices),
        counts[0],
        counts[1],
        counts[2],
        counts[3],
        counts[4],
        counts[5],
        14,
    )
    body = bytearray()
    body.extend(struct.pack("<3f", 1.0, 2.0, 3.0))
    body.extend(struct.pack("<3f", -10.0, -20.0, -30.0))
    body.extend(struct.pack("<3f", 100.0, 200.0, 300.0))
    body.extend(struct.pack("<f", 4.5))
    for vertex in vertices:
        body.extend(struct.pack("<3f", *vertex))
    for face_index, indices in enumerate(faces):
        body.extend(struct.pack("<I", face_index))
        body.extend(struct.pack("<3H", *indices))
        body.extend(struct.pack("<3H", *connections[face_index]))
        body.extend(struct.pack("<HBB", 3, 3, 0xA0 + face_index))
    if include_auxiliary_records:
        body.extend(struct.pack("<2Q", 21, 22))
        body.extend(struct.pack("<3I", 31, 32, 33))
        body.extend(struct.pack("<3f", 41.0, 42.0, 43.0))
        body.extend(struct.pack("<I", 51))
        for value, flag in ((-1, 1), (-2, 2), (-3, 3), (-4, 4), (-5, 5), (-6, 6)):
            body.extend(struct.pack("<2b", value, flag))
        body.extend(struct.pack("<I", 61))
        body.extend(struct.pack("<3f", 71.0, 72.0, 73.0))
        body.extend(struct.pack("<3f", 74.0, 75.0, 76.0))
        body.extend(struct.pack("<f3I", 77.0, 78, 79, 80))
    return header + bytes(body)


def source(
    name: str, buffer_index: int = 0, *, z_variant: int | None = None
) -> nav.NavigationSource:
    variants = () if z_variant is None else (z_variant,)
    return nav.NavigationSource(
        source_path=f"fixture/{name}.json",
        resource_path=f"base/world/{name}.navmesh",
        buffer_index=buffer_index,
        agent_size="Human",
        active_variant_ids=variants,
        all_variant_ids=variants,
    )


class VNAVDecodeTests(unittest.TestCase):
    def test_decodes_wolvenkit_layout_and_adjacency_metadata(self) -> None:
        payload = make_vnav(
            [(0, 0, 0), (10, 0, 0), (0, 10, 0)],
            [(0, 1, 2)],
            connections=[(0x8000 | 17, NO_FACE, 3)],
            include_auxiliary_records=True,
        )
        decoded = nav.decode_vnav_buffer(
            base64.b64encode(payload).decode("ascii"), source=source("a")
        )

        self.assertEqual(b"VAND", payload[:4])
        self.assertEqual(nav.VAND_MAGIC, decoded.header.magic)
        self.assertEqual((7, 9), (decoded.header.tile_x, decoded.header.tile_y))
        self.assertEqual(nav.Vec3(10.0, 0.0, 0.0), decoded.vertices[1])
        self.assertEqual((0, 1, 2), decoded.faces[0].vertex_indices)
        self.assertEqual(
            nav.FaceConnection(17, True, 0x8011), decoded.faces[0].connected_faces[0]
        )
        self.assertEqual(
            (21, 22), (decoded.zero_pairs[0].unknown_1, decoded.zero_pairs[0].unknown_2)
        )
        self.assertEqual(32, decoded.index_records[0].index)
        self.assertEqual(nav.Vec3(41.0, 42.0, 43.0), decoded.unknown_vectors[0])
        self.assertEqual(51, decoded.flags[0])
        self.assertEqual((-1, 1), decoded.info_records[0].values[0])
        self.assertEqual(80, decoded.bounds_records[0].unknown_6)

    def test_rejects_bad_magic_truncation_and_bad_vertex_index(self) -> None:
        valid = make_vnav([(0, 0, 0), (1, 0, 0), (0, 1, 0)], [(0, 1, 2)])
        with self.assertRaisesRegex(nav.NavigationFormatError, "magic"):
            nav.decode_vnav_buffer(b"NOPE" + valid[4:])
        with self.assertRaisesRegex(nav.NavigationFormatError, "magic"):
            nav.decode_vnav_buffer(b"VNAV" + valid[4:])
        with self.assertRaisesRegex(nav.NavigationFormatError, "truncated"):
            nav.decode_vnav_buffer(valid[:-1])

        bad_face = make_vnav([(0, 0, 0), (1, 0, 0), (0, 1, 0)], [(0, 1, 9)])
        with self.assertRaisesRegex(nav.NavigationFormatError, "outside"):
            nav.decode_vnav_buffer(bad_face)


class NavigationSectorTests(unittest.TestCase):
    def test_loads_only_human_tile_data_and_preserves_variants(self) -> None:
        human = make_vnav([(0, 0, 0), (1, 0, 0), (0, 1, 0)], [(0, 1, 2)], tile_x=2)
        vehicle = make_vnav([(0, 0, 0), (2, 0, 0), (0, 2, 0)], [(0, 1, 2)], tile_x=3)
        document = {
            "Header": {
                "ArchiveFileName": r"base\worlds\03_night_city\navigation.navmesh"
            },
            "Data": {
                "RootChunk": {
                    "$type": "worldNavigationTileResource",
                    "agentSize": "AgentSize_Count",
                    "localBoundingBox": {
                        "Min": {"X": -1, "Y": -2, "Z": -3, "W": 1},
                        "Max": {"X": 4, "Y": 5, "Z": 6, "W": 1},
                    },
                    "tilesData": [
                        {
                            "tileX": 2,
                            "tileY": 4,
                            "tileIndex": 6,
                            "bufferIndex": 0,
                            "agentSize": {"$value": "Human"},
                            "tileRef": 100,
                            "activeVariantIDs": [11],
                            "allVariantIDs": {"Data": [11, 12]},
                        },
                        {
                            "tileX": 3,
                            "tileY": 5,
                            "tileIndex": 7,
                            "bufferIndex": 1,
                            "agentSize": "Vehicle",
                            "tileRef": 101,
                            "activeVariantIDs": [],
                            "allVariantIDs": [],
                        },
                    ],
                    "tileBuffers": {
                        "Data": [
                            {
                                "BufferId": "0",
                                "Bytes": base64.b64encode(human).decode("ascii"),
                            },
                            {
                                "BufferId": "1",
                                "Data": {
                                    "Bytes": base64.b64encode(vehicle).decode("ascii")
                                },
                            },
                        ]
                    },
                }
            },
        }

        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "navigation.navmesh.json"
            path.write_text(json.dumps(document), encoding="utf-8")
            sector = nav.load_navigation_sector(path)

        self.assertEqual("Human", sector.agent_size)
        self.assertEqual(1, len(sector.buffers))
        metadata = sector.buffers[0].source
        self.assertEqual(0, metadata.buffer_index)
        self.assertEqual(
            (2, 4, 6, 100),
            (metadata.tile_x, metadata.tile_y, metadata.tile_index, metadata.tile_ref),
        )
        self.assertEqual((11,), metadata.active_variant_ids)
        self.assertEqual((11, 12), metadata.all_variant_ids)
        self.assertEqual(
            -3.0, sector.local_bounds.minimum.z if sector.local_bounds else None
        )


class NavigationIslandTests(unittest.TestCase):
    def test_maps_vand_component_order_to_world_coordinates(self) -> None:
        self.assertEqual(
            nav.Vec3(2452.0, -731.0, 64.0),
            nav.vand_position_to_world(nav.Vec3(2452.0, 64.0, -731.0)),
        )

    def test_joins_resources_at_shared_3d_edges_but_preserves_stacked_level(
        self,
    ) -> None:
        lower_a = nav.decode_vnav_buffer(
            make_vnav([(0, 0, 0), (10, 0, 0), (0, 10, 0)], [(0, 1, 2)]),
            source=source("lower_a"),
        )
        lower_b = nav.decode_vnav_buffer(
            make_vnav([(10.01, 0, 0), (10, 10, 0), (0.01, 10, 0)], [(0, 1, 2)]),
            source=source("lower_b", z_variant=23),
        )
        upper = nav.decode_vnav_buffer(
            make_vnav([(0, 0, 5), (10, 0, 5), (0, 10, 5)], [(0, 1, 2)]),
            source=source("upper"),
        )

        islands = nav.reconstruct_navigation_islands(
            [upper, lower_b, lower_a], edge_quantization_m=0.05
        )

        self.assertEqual([1, 2], sorted(len(island.faces) for island in islands))
        lower = next(island for island in islands if len(island.faces) == 2)
        self.assertAlmostEqual(100.0, lower.metrics.surface_area_m2, places=1)
        self.assertAlmostEqual(0.0, lower.metrics.z_range_m)
        self.assertAlmostEqual(10.0, lower.metrics.approximate_width_m, places=1)
        self.assertIn(lower.faces[1].ref, lower.faces[0].neighbors)

    def test_follows_valid_explicit_face_adjacency(self) -> None:
        payload = make_vnav(
            [(0, 0, 0), (1, 0, 0), (0, 1, 0), (20, 0, 0), (21, 0, 0), (20, 1, 0)],
            [(0, 1, 2), (3, 4, 5)],
            connections=[(1, NO_FACE, NO_FACE), (0, NO_FACE, NO_FACE)],
        )
        decoded = nav.decode_vnav_buffer(payload, source=source("explicit"))
        islands = nav.reconstruct_navigation_islands([decoded])
        self.assertEqual(1, len(islands))
        self.assertEqual(2, len(islands[0].faces))

    def test_sampling_is_deterministic_spaced_and_carries_camera_provenance(
        self,
    ) -> None:
        payload = make_vnav(
            [(0, 0, 0), (100, 0, 0), (0, 10, 0), (100, 10, 0)],
            [(0, 1, 2), (1, 3, 2)],
            connections=[(1, NO_FACE, NO_FACE), (0, NO_FACE, NO_FACE)],
        )
        decoded = nav.decode_vnav_buffer(
            payload, source=source("corridor", z_variant=42)
        )
        island = nav.reconstruct_navigation_islands([decoded])[0]

        first = nav.sample_navigation_islands(
            [island], spacing_m=25, camera_height_m=1.65, seed=17
        )
        second = nav.sample_navigation_islands(
            [island], spacing_m=25, camera_height_m=1.65, seed=17
        )

        self.assertEqual(first, second)
        self.assertGreaterEqual(len(first), 3)
        for sample in first:
            self.assertAlmostEqual(
                1.65, sample.camera_position.z - sample.surface_position.z
            )
            self.assertGreater(sample.local_width_m, 0.0)
            self.assertEqual("navmesh_farthest", sample.provenance.method)
            self.assertEqual((42,), sample.provenance.active_variant_ids)
        for index, one in enumerate(first):
            for two in first[index + 1 :]:
                distance = math.sqrt(
                    one.surface_position.distance_squared(two.surface_position)
                )
                self.assertGreaterEqual(distance + 1e-7, 25.0)


if __name__ == "__main__":
    unittest.main()
