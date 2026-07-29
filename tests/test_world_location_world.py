from __future__ import annotations

import base64
import copy
import json
import struct
import tempfile
import unittest
from pathlib import Path

from tools.world_location_world import (
    AABB,
    BLENDER_WOLVENKIT_COMPAT_VERSION,
    GEOMETRY_POLICY_DETAILED,
    GEOMETRY_POLICY_PROXY_ONLY,
    TileSectorOverlap,
    VariantKey,
    WorldLocationWorldError,
    WorldSectorIndex,
    WorldStateSelector,
    complete_blender_sector_defaults,
    parse_streaming_block,
    stage_streaming_sector,
)


PREFAB_REF = "$/03_night_city/test/location"
MORNING = VariantKey(PREFAB_REF, 7, "morning")
NIGHT = VariantKey(PREFAB_REF, 7, "night")


def typed(value: object) -> dict[str, object]:
    return {"$value": value}


def box(
    minimum: tuple[float, float, float], maximum: tuple[float, float, float]
) -> dict:
    return {
        "$type": "Box",
        "Min": {
            "$type": "Vector4",
            "X": minimum[0],
            "Y": minimum[1],
            "Z": minimum[2],
            "W": 0,
        },
        "Max": {
            "$type": "Vector4",
            "X": maximum[0],
            "Y": maximum[1],
            "Z": maximum[2],
            "W": 0,
        },
    }


def variant(
    name: str,
    range_index: int,
    *,
    variant_id: int = 7,
    enabled: bool = False,
) -> dict:
    return {
        "$type": "worldStreamingSectorVariant",
        "nodeRef": typed(PREFAB_REF),
        "variantId": typed(str(variant_id)),
        "parentVariantID": 0,
        "name": typed(name),
        "rangeIndex": range_index,
        "enabledByDefault": 1 if enabled else 0,
    }


def descriptor(
    path: str,
    minimum: tuple[float, float, float],
    maximum: tuple[float, float, float],
    *,
    variants: list[dict] | None = None,
    ranges: int = 1,
    category: str = "Exterior",
    level: int = 0,
) -> dict:
    return {
        "$type": "worldStreamingSectorDescriptor",
        "data": {"DepotPath": typed(path), "Flags": "Soft"},
        "streamingBox": box(minimum, maximum),
        "questPrefabNodeRef": typed("0"),
        "numNodeRanges": ranges,
        "variants": variants or [],
        "level": level,
        "category": category,
    }


def block_document(descriptors: list[dict]) -> dict:
    return {
        "Header": {"ArchiveFileName": "base\\worlds\\test\\all.streamingblock"},
        "Data": {
            "Version": 195,
            "BuildVersion": 0,
            "RootChunk": {"$type": "worldStreamingBlock", "descriptors": descriptors},
            "EmbeddedFiles": [],
        },
    }


def mesh_node(
    handle_id: str,
    name: str,
    resource: str,
    *,
    node_type: str = "worldStaticMeshNode",
) -> dict:
    return {
        "HandleId": handle_id,
        "Data": {
            "$type": node_type,
            "debugName": typed(name),
            "mesh": {"DepotPath": typed(resource), "Flags": "Soft"},
        },
    }


def node_data(node_index: int, position: tuple[float, float, float]) -> dict:
    return {
        "Id": str(node_index + 100),
        "NodeIndex": node_index,
        "Position": {
            "$type": "Vector4",
            "X": position[0],
            "Y": position[1],
            "Z": position[2],
            "W": 0,
        },
    }


def embedded(path: str, dependency: str | None = None) -> dict:
    content: dict = {"$type": "CMesh", "marker": path}
    if dependency is not None:
        content["dependency"] = {"DepotPath": typed(dependency), "Flags": "Soft"}
    return {"FileName": typed(path), "Content": content}


def sector_document() -> dict:
    resources = {
        "default": "base/world/test/keep.mesh",
        "remote": "base/world/test/remote.mesh",
        "morning": "base/world/test/morning.mesh",
        "night": "base/world/test/night.mesh",
        "unused": "base/world/test/unused.mesh",
    }
    embedded_files = [
        embedded(resources["default"], "base/world/test/keep_texture.xbm"),
        embedded("base/world/test/keep_texture.xbm"),
        embedded(resources["remote"]),
        embedded(resources["morning"]),
        embedded(resources["night"]),
        embedded(resources["unused"]),
    ]
    return {
        "Header": {
            "ArchiveFileName": "base\\world\\test.streamingsector",
            "marker": "preserve",
        },
        "Data": {
            "Version": 195,
            "BuildVersion": 0,
            "RootChunk": {
                "$type": "worldStreamingSector",
                "category": "Exterior",
                "level": 0,
                "nodes": [
                    mesh_node("10", "default", resources["default"]),
                    mesh_node(
                        "11",
                        "remote",
                        resources["remote"],
                        node_type="worldStaticMarkerNode",
                    ),
                    mesh_node(
                        "12",
                        "morning",
                        resources["morning"],
                        node_type="worldStaticMarkerNode",
                    ),
                    mesh_node(
                        "13",
                        "night",
                        resources["night"],
                        node_type="worldStaticMarkerNode",
                    ),
                    mesh_node("14", "unused", resources["unused"]),
                ],
                "nodeData": {
                    "BufferId": "0",
                    "Flags": 0,
                    "Type": "worldNodeDataBuffer",
                    "Data": [
                        node_data(0, (0, 0, 0)),
                        node_data(1, (1000, 0, 0)),
                        node_data(2, (10, 0, 0)),
                        node_data(2, (70, 0, 0)),
                        node_data(3, (20, 0, 0)),
                    ],
                },
                "nodeRefs": [],
                "variantIndices": [0, 2, 4],
                "persistentNodeIndex": 0,
                "persistentNodes": [],
                "variantNodes": [[], []],
                "localInplaceResource": [
                    {"DepotPath": item["FileName"], "Flags": "Soft"}
                    for item in embedded_files
                ],
            },
            "EmbeddedFiles": embedded_files,
        },
    }


class WorldLocationWorldTests(unittest.TestCase):
    def test_blender_adapter_fills_only_importer_required_defaults(self) -> None:
        document = {
            "Header": {"WolvenKitVersion": "ghostline-red 0.1.0"},
            "Data": {
                "RootChunk": {
                    "$type": "worldStreamingSector",
                    "nodes": [
                        {
                            "Data": {
                                "$type": "worldStaticDecalNode",
                                "alpha": 0.4,
                            }
                        },
                        {"Data": {"$type": "worldEntityNode"}},
                        {
                            "Data": {
                                "$type": "worldInstancedMeshNode",
                                "worldTransformsBuffer": {"numElements": 2},
                            }
                        },
                        {
                            "Data": {
                                "$type": "worldFoliageNode",
                                "populationSpanInfo": {"cketCount": 1},
                            }
                        },
                    ],
                }
            },
        }

        inserted = complete_blender_sector_defaults(document)

        self.assertEqual(
            BLENDER_WOLVENKIT_COMPAT_VERSION,
            document["Header"]["WolvenKitVersion"],
        )
        self.assertEqual(
            "ghostline-red 0.1.0",
            document["Header"]["GhostlineOriginalExporterVersion"],
        )
        nodes = document["Data"]["RootChunk"]["nodes"]
        self.assertEqual(0.4, nodes[0]["Data"]["alpha"])
        self.assertEqual(0, nodes[0]["Data"]["horizontalFlip"])
        self.assertEqual(0, nodes[0]["Data"]["verticalFlip"])
        self.assertEqual("default", nodes[1]["Data"]["appearanceName"]["$value"])
        self.assertEqual(0, nodes[2]["Data"]["worldTransformsBuffer"]["startIndex"])
        self.assertEqual(0, nodes[3]["Data"]["populationSpanInfo"]["cketBegin"])
        self.assertEqual(0, nodes[3]["Data"]["populationSpanInfo"]["stancesBegin"])
        self.assertNotIn("worldStaticDecalNode.alpha", inserted)

    def setUp(self) -> None:
        repeated_variants = [
            variant("morning", 1, enabled=True),
            variant("morning", 1, enabled=True),
            variant("night", 2),
        ]
        self.block = block_document(
            [
                descriptor(
                    "BASE/world/tiles/primary.streamingsector",
                    (-10, -10, -10),
                    (10, 10, 10),
                    variants=repeated_variants,
                    ranges=3,
                ),
                descriptor(
                    "base/world/tiles/repeated.streamingsector",
                    (70, -10, -10),
                    (80, 10, 10),
                    variants=[variant("morning", 1, enabled=True)],
                    ranges=2,
                    level=1,
                ),
                descriptor(
                    "base/world/tiles/far.streamingsector",
                    (150, -10, -10),
                    (160, 10, 10),
                    category="Navigation",
                ),
                descriptor(
                    "base/world/tiles/outside.streamingsector",
                    (300, -10, -10),
                    (310, 10, 10),
                ),
            ]
        )
        self.index = WorldSectorIndex(
            parse_streaming_block(self.block, source_block="fixture")
        )
        self.primary = next(
            row
            for row in self.index.descriptors
            if row.depot_path.endswith("primary.streamingsector")
        )

    def test_parses_normalized_descriptors_and_groups_repeated_variants(self) -> None:
        self.assertEqual(
            "base\\world\\tiles\\primary.streamingsector", self.primary.depot_path
        )
        self.assertEqual("exterior", self.primary.category)
        self.assertEqual(0, self.primary.level)
        self.assertEqual(AABB(-10, -10, -10, 10, 10, 10), self.primary.bounds)

        morning_group = next(
            group for group in self.index.variant_groups if group.key == MORNING
        )
        self.assertEqual(3, len(morning_group.occurrences))
        self.assertEqual(
            [1, 1, 1], [item.range_index for item in morning_group.occurrences]
        )
        self.assertTrue(morning_group.enabled_by_default)

        same_id_groups = [
            group.key
            for group in self.index.variant_groups
            if group.key.variant_id == 7
        ]
        self.assertEqual([MORNING, NIGHT], same_id_groups)

    def test_variant_may_legitimately_reference_default_range_zero(self) -> None:
        default_alias = variant("", 0, variant_id=99, enabled=True)
        document = block_document(
            [
                descriptor(
                    "base/world/tiles/default_alias.streamingsector",
                    (-1, -1, -1),
                    (1, 1, 1),
                    variants=[default_alias],
                    ranges=1,
                )
            ]
        )
        index = WorldSectorIndex(parse_streaming_block(document))
        parsed = index.descriptors[0]
        key = VariantKey(PREFAB_REF, 99, "")
        self.assertEqual(0, parsed.variants[0].range_index)
        selector = WorldStateSelector.defaults(index)
        self.assertEqual((0,), selector.selected_ranges(parsed))
        self.assertEqual((key,), selector.active_variants(parsed))

        default_alias["rangeIndex"] = -1
        with self.assertRaisesRegex(WorldLocationWorldError, "cannot be negative"):
            parse_streaming_block(document)

    def test_tile_overlap_is_deterministic_and_marks_far_as_proxy_only(self) -> None:
        tile, overlaps = self.index.query_tile((0, 0, 0))
        self.assertEqual(-64, tile.core.min_x)
        self.assertEqual(128, tile.near.max_x)
        self.assertEqual(256, tile.far.max_x if tile.far else None)
        self.assertEqual(
            [
                ("primary.streamingsector", "core", GEOMETRY_POLICY_DETAILED),
                ("repeated.streamingsector", "near", GEOMETRY_POLICY_DETAILED),
                ("far.streamingsector", "far", GEOMETRY_POLICY_PROXY_ONLY),
            ],
            [
                (
                    item.descriptor.depot_path.rsplit("\\", 1)[-1],
                    item.distance_band,
                    item.geometry_policy,
                )
                for item in overlaps
            ],
        )

        _, without_far = self.index.query_tile((0, 0, 0), far_size=None)
        self.assertEqual(["core", "near"], [item.distance_band for item in without_far])

    def test_world_state_includes_defaults_and_rejects_mutually_exclusive_choices(
        self,
    ) -> None:
        default = WorldStateSelector.defaults(self.index)
        self.assertEqual((0, 1), default.selected_ranges(self.primary))
        self.assertEqual((MORNING,), default.active_variants(self.primary))

        night = WorldStateSelector(self.index, [NIGHT])
        self.assertEqual((0, 2), night.selected_ranges(self.primary))
        self.assertEqual((NIGHT,), night.active_variants(self.primary))

        with self.assertRaisesRegex(WorldLocationWorldError, "Mutually exclusive"):
            WorldStateSelector(self.index, [MORNING, NIGHT])

    def test_staging_filters_ranges_clips_instances_and_remaps_nodes(self) -> None:
        source = sector_document()
        untouched = copy.deepcopy(source)
        clip = AABB(-64, -64, -5, 64, 64, 5)
        staged = stage_streaming_sector(
            source,
            self.primary,
            WorldStateSelector.defaults(self.index),
            tile_id="alley",
            clip_bounds=clip,
        )
        root = staged.document["Data"]["RootChunk"]

        self.assertEqual(untouched, source)
        self.assertEqual(["10", "12"], [item["HandleId"] for item in root["nodes"]])
        self.assertEqual(
            [0, 1], [item["NodeIndex"] for item in root["nodeData"]["Data"]]
        )
        self.assertEqual(
            [0, 10], [item["Position"]["X"] for item in root["nodeData"]["Data"]]
        )
        self.assertEqual("0", root["nodeData"]["BufferId"])
        self.assertEqual([0], root["variantIndices"])
        self.assertEqual([], root["variantNodes"])
        self.assertEqual([], root["persistentNodes"])

        retained_embedded = [
            item["FileName"]["$value"]
            for item in staged.document["Data"]["EmbeddedFiles"]
        ]
        self.assertEqual(
            [
                "base/world/test/keep.mesh",
                "base/world/test/keep_texture.xbm",
                "base/world/test/morning.mesh",
            ],
            retained_embedded,
        )
        self.assertEqual(3, len(root["localInplaceResource"]))

        manifest = staged.manifest_row
        self.assertEqual("alley", manifest["tile_id"])
        self.assertEqual(5, manifest["source_instance_count"])
        self.assertEqual(4, manifest["variant_retained_instance_count"])
        self.assertEqual(1, manifest["dropped_variant_instance_count"])
        self.assertEqual(2, manifest["dropped_spatial_instance_count"])
        self.assertEqual(0, manifest["conservative_spatial_retained_instance_count"])
        self.assertEqual([], manifest["conservative_spatial_retained_node_types"])
        self.assertEqual(2, manifest["retained_instance_count"])
        self.assertEqual(5, manifest["source_node_count"])
        self.assertEqual(2, manifest["retained_node_count"])
        self.assertEqual(3, manifest["dropped_node_count"])
        self.assertEqual({"0": 0, "2": 1}, manifest["node_index_remap"])
        self.assertEqual(6, manifest["source_embedded_file_count"])
        self.assertEqual(3, manifest["retained_embedded_file_count"])
        self.assertEqual(64, manifest["clip_bounds"]["max"]["x"])
        self.assertEqual("point_origin_safe_only_v1", manifest["spatial_clip_policy"])
        self.assertEqual(64, len(manifest["staged_sector_fingerprint"]))

    def test_spatial_clip_retains_large_and_unknown_geometry_nodes(self) -> None:
        document = block_document(
            [
                descriptor(
                    "base/world/tiles/large_geometry.streamingsector",
                    (-10, -10, -10),
                    (10, 10, 10),
                )
            ]
        )
        index = WorldSectorIndex(parse_streaming_block(document))
        geometry_types = [
            "worldStaticMeshNode",
            "worldTerrainMeshNode",
            "worldBendedMeshNode",
            "worldRoadProxyMeshNode",
            "worldInstancedMeshNode",
            "worldFutureGeometryNode",
        ]
        nodes = [
            mesh_node(
                "drop-point",
                "point marker",
                "base/world/test/point.mesh",
                node_type="worldStaticMarkerNode",
            ),
            *[
                mesh_node(
                    f"keep-{node_index}",
                    node_type,
                    f"base/world/test/{node_index}.mesh",
                    node_type=node_type,
                )
                for node_index, node_type in enumerate(geometry_types, start=1)
            ],
            mesh_node(
                "keep-inside-point",
                "inside point marker",
                "base/world/test/inside.mesh",
                node_type="worldStaticMarkerNode",
            ),
        ]
        records = [
            node_data(node_index, (1000, 0, 0)) for node_index in range(len(nodes) - 1)
        ]
        records.append(node_data(len(nodes) - 1, (0, 0, 0)))
        sector = {
            "Header": {
                "ArchiveFileName": "base\\world\\large_geometry.streamingsector"
            },
            "Data": {
                "Version": 195,
                "BuildVersion": 0,
                "RootChunk": {
                    "$type": "worldStreamingSector",
                    "nodes": nodes,
                    "nodeData": {
                        "BufferId": "0",
                        "Flags": 0,
                        "Type": "worldNodeDataBuffer",
                        "Data": records,
                    },
                    "variantIndices": [0],
                    "persistentNodeIndex": 0,
                    "persistentNodes": [],
                    "variantNodes": [],
                    "localInplaceResource": [],
                },
                "EmbeddedFiles": [],
            },
        }

        staged = stage_streaming_sector(
            sector,
            index.descriptors[0],
            WorldStateSelector.defaults(index),
            clip_bounds=AABB(-64, -64, -5, 64, 64, 5),
        )
        root = staged.document["Data"]["RootChunk"]

        self.assertEqual(
            [*[f"keep-{index}" for index in range(1, 7)], "keep-inside-point"],
            [node["HandleId"] for node in root["nodes"]],
        )
        self.assertEqual(
            list(range(7)),
            [record["NodeIndex"] for record in root["nodeData"]["Data"]],
        )
        self.assertEqual(
            {str(old): old - 1 for old in range(1, 8)},
            staged.manifest_row["node_index_remap"],
        )
        self.assertEqual(1, staged.manifest_row["dropped_spatial_instance_count"])
        self.assertEqual(
            6,
            staged.manifest_row["conservative_spatial_retained_instance_count"],
        )
        self.assertEqual(
            sorted(geometry_types),
            staged.manifest_row["conservative_spatial_retained_node_types"],
        )
        self.assertEqual(7, staged.manifest_row["retained_instance_count"])

    def test_staging_expands_native_instanced_transform_buffers(self) -> None:
        world_bytes = b"".join(
            [
                struct.pack(
                    "<4i4f3fi",
                    131_072,
                    -262_144,
                    65_536,
                    99,
                    0.1,
                    0.2,
                    0.3,
                    0.9,
                    2.0,
                    3.0,
                    4.0,
                    77,
                ),
                struct.pack(
                    "<4i4f3fi",
                    -65_536,
                    32_768,
                    0,
                    -1,
                    0.0,
                    0.0,
                    0.0,
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    -2,
                ),
            ]
        )
        cooked_bytes = struct.pack("<8f", 1.25, -2.5, 3.75, 0.0, -0.1, 0.2, -0.3, 0.9)

        def shared_buffer(handle_id: str, payload: bytes) -> dict:
            return {
                "HandleId": handle_id,
                "Data": {
                    "$type": "worldSharedDataBuffer",
                    "buffer": {
                        "BufferId": "8",
                        "Flags": 4063232,
                        "Bytes": base64.b64encode(payload).decode("ascii"),
                    },
                },
            }

        nodes = [
            {
                "HandleId": "100",
                "Data": {
                    "$type": "worldInstancedMeshNode",
                    "mesh": {
                        "DepotPath": typed("base/world/test/owner.mesh"),
                        "Flags": "Soft",
                    },
                    "worldTransformsBuffer": {
                        "sharedDataBuffer": shared_buffer("101", world_bytes),
                        "startIndex": 0,
                        "numElements": 1,
                    },
                },
            },
            {
                "HandleId": "102",
                "Data": {
                    "$type": "worldInstancedMeshNode",
                    "mesh": {
                        "DepotPath": typed("base/world/test/reference.mesh"),
                        "Flags": "Soft",
                    },
                    "worldTransformsBuffer": {
                        "sharedDataBuffer": {"HandleRefId": "101"},
                        "startIndex": 1,
                        "numElements": 1,
                    },
                },
            },
            {
                "HandleId": "200",
                "Data": {
                    "$type": "worldInstancedDestructibleMeshNode",
                    "mesh": {
                        "DepotPath": typed("base/world/test/destructible.mesh"),
                        "Flags": "Soft",
                    },
                    "cookedInstanceTransforms": {
                        "sharedDataBuffer": shared_buffer("201", cooked_bytes),
                        "startIndex": 0,
                        "numElements": 1,
                    },
                },
            },
        ]
        sector = {
            "Header": {"ArchiveFileName": "base\\world\\instanced.streamingsector"},
            "Data": {
                "Version": 195,
                "BuildVersion": 0,
                "RootChunk": {
                    "$type": "worldStreamingSector",
                    "nodes": nodes,
                    # The inline buffer owner deliberately has no nodeData. It
                    # still has to survive compaction for HandleRefId 101.
                    "nodeData": {
                        "BufferId": "0",
                        "Flags": 0,
                        "Type": "worldNodeDataBuffer",
                        "Data": [node_data(1, (0, 0, 0)), node_data(2, (0, 0, 0))],
                    },
                    "variantIndices": [0],
                    "persistentNodeIndex": 0,
                    "persistentNodes": [],
                    "variantNodes": [],
                    "localInplaceResource": [],
                },
                "EmbeddedFiles": [],
            },
        }
        document = block_document(
            [
                descriptor(
                    "base/world/tiles/instanced.streamingsector",
                    (-10, -10, -10),
                    (10, 10, 10),
                )
            ]
        )
        index = WorldSectorIndex(parse_streaming_block(document))

        staged = stage_streaming_sector(
            sector,
            index.descriptors[0],
            WorldStateSelector.defaults(index),
        )
        staged_nodes = staged.document["Data"]["RootChunk"]["nodes"]
        self.assertEqual(
            ["100", "102", "200"], [node["HandleId"] for node in staged_nodes]
        )
        self.assertEqual(1, staged.manifest_row["dependency_retained_node_count"])

        world_buffer = staged_nodes[0]["Data"]["worldTransformsBuffer"][
            "sharedDataBuffer"
        ]["Data"]["buffer"]
        self.assertEqual(
            base64.b64encode(world_bytes).decode("ascii"), world_buffer["Bytes"]
        )
        self.assertIn("WorldTransformsBuffer", world_buffer["Type"])
        world_transforms = world_buffer["Data"]["Transforms"]
        self.assertEqual(2, len(world_transforms))
        self.assertEqual(
            {"$type": "Vector3", "X": 1.0, "Y": -2.0, "Z": 0.5},
            world_transforms[0]["translation"],
        )
        self.assertEqual(
            {"$type": "Vector3", "X": 2.0, "Y": 3.0, "Z": 4.0},
            world_transforms[0]["scale"],
        )
        self.assertEqual(
            "101",
            staged_nodes[1]["Data"]["worldTransformsBuffer"]["sharedDataBuffer"][
                "HandleRefId"
            ],
        )
        self.assertNotIn(
            "Data",
            staged_nodes[1]["Data"]["worldTransformsBuffer"]["sharedDataBuffer"],
        )

        cooked_buffer = staged_nodes[2]["Data"]["cookedInstanceTransforms"][
            "sharedDataBuffer"
        ]["Data"]["buffer"]
        self.assertIn("CookedInstanceTransformsBuffer", cooked_buffer["Type"])
        cooked = cooked_buffer["Data"]["Transforms"][0]
        self.assertEqual(
            {"$type": "Vector4", "W": 0.0, "X": 1.25, "Y": -2.5, "Z": 3.75},
            cooked["position"],
        )
        expansion = staged.manifest_row["blender_transform_buffer_expansion"]
        self.assertEqual(1, expansion["decoded_world_buffers"])
        self.assertEqual(2, expansion["decoded_world_transforms"])
        self.assertEqual(1, expansion["decoded_cooked_buffers"])
        self.assertEqual(1, expansion["decoded_cooked_transforms"])

    def test_staging_rejects_malformed_native_transform_buffer(self) -> None:
        document = block_document(
            [
                descriptor(
                    "base/world/tiles/malformed.streamingsector",
                    (-10, -10, -10),
                    (10, 10, 10),
                )
            ]
        )
        index = WorldSectorIndex(parse_streaming_block(document))
        sector = {
            "Header": {"ArchiveFileName": "base\\world\\malformed.streamingsector"},
            "Data": {
                "Version": 195,
                "BuildVersion": 0,
                "RootChunk": {
                    "$type": "worldStreamingSector",
                    "nodes": [
                        {
                            "HandleId": "10",
                            "Data": {
                                "$type": "worldInstancedMeshNode",
                                "worldTransformsBuffer": {
                                    "sharedDataBuffer": {
                                        "HandleId": "11",
                                        "Data": {
                                            "$type": "worldSharedDataBuffer",
                                            "buffer": {
                                                "Bytes": base64.b64encode(
                                                    b"short"
                                                ).decode("ascii")
                                            },
                                        },
                                    },
                                    "numElements": 1,
                                },
                            },
                        }
                    ],
                    "nodeData": {"Data": [node_data(0, (0, 0, 0))]},
                    "variantIndices": [0],
                    "persistentNodeIndex": 0,
                },
                "EmbeddedFiles": [],
            },
        }

        with self.assertRaisesRegex(WorldLocationWorldError, "multiple of 48"):
            stage_streaming_sector(
                sector,
                index.descriptors[0],
                WorldStateSelector.defaults(index),
            )

    def test_clip_margin_and_explicit_variant_are_reflected_in_manifest(self) -> None:
        clip = AABB(-64, -64, -5, 64, 64, 5)
        default = stage_streaming_sector(
            sector_document(),
            self.primary,
            WorldStateSelector.defaults(self.index),
            clip_bounds=clip,
            clip_margin=10,
        )
        self.assertEqual(3, default.manifest_row["retained_instance_count"])
        self.assertEqual(1, default.manifest_row["dropped_spatial_instance_count"])
        self.assertEqual(74, default.manifest_row["effective_clip_bounds"]["max"]["x"])

        night = stage_streaming_sector(
            sector_document(),
            self.primary,
            WorldStateSelector(self.index, [NIGHT]),
            clip_bounds=clip,
        )
        root = night.document["Data"]["RootChunk"]
        self.assertEqual(["10", "13"], [item["HandleId"] for item in root["nodes"]])
        self.assertEqual(
            [0, 1], [item["NodeIndex"] for item in root["nodeData"]["Data"]]
        )
        self.assertEqual([0, 2], night.manifest_row["selected_range_indices"])
        self.assertEqual([NIGHT.as_dict()], night.manifest_row["active_variants"])
        self.assertNotEqual(
            default.manifest_row["world_state_fingerprint"],
            night.manifest_row["world_state_fingerprint"],
        )

        far = stage_streaming_sector(
            sector_document(),
            self.primary,
            WorldStateSelector(self.index, [NIGHT]),
            overlap=TileSectorOverlap(
                self.primary,
                "far",
                GEOMETRY_POLICY_PROXY_ONLY,
            ),
            clip_bounds=clip,
        )
        self.assertEqual("far", far.manifest_row["distance_band"])
        self.assertEqual(
            GEOMETRY_POLICY_PROXY_ONLY, far.manifest_row["geometry_policy"]
        )

    def test_staged_output_and_fingerprints_are_deterministic(self) -> None:
        kwargs = {
            "source": sector_document(),
            "descriptor": self.primary,
            "selector": WorldStateSelector.defaults(self.index),
            "clip_bounds": AABB(-64, -64, -5, 64, 64, 5),
        }
        first = stage_streaming_sector(**kwargs)
        second = stage_streaming_sector(**kwargs)
        self.assertEqual(first.document, second.document)
        self.assertEqual(first.manifest_row, second.manifest_row)

        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "tile" / "primary.streamingsector.json"
            row = first.write(output)
            self.assertEqual(
                first.document, json.loads(output.read_text(encoding="utf-8"))
            )
            self.assertEqual(str(output), row["staged_path"])


if __name__ == "__main__":
    unittest.main()
