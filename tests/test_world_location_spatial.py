from __future__ import annotations

import json
import tempfile
import unittest
from dataclasses import dataclass
from pathlib import Path

from tools.world_location_spatial import (
    Bounds3D,
    SpatialIndexError,
    build_sector_spatial_index,
    snapshot_sector_json_roots,
)


def typed(value: object) -> dict[str, object]:
    return {"$type": "fixtureScalar", "$value": value}


def position(x: object, y: object, z: object) -> dict[str, object]:
    return {"Position": {"X": x, "Y": y, "Z": z, "W": 1}}


def sector_document(
    positions: list[dict[str, object] | object],
    *,
    archive_name: object | None = r"base\worlds\test\fixture.streamingsector",
    category: object = "Exterior",
    level: object = 0,
    direct_node_data: bool = False,
) -> dict[str, object]:
    header = {} if archive_name is None else {"ArchiveFileName": archive_name}
    node_data: object = (
        positions if direct_node_data else {"Data": positions, "BufferId": "0"}
    )
    return {
        "Header": header,
        "Data": {
            "RootChunk": {
                "$type": "worldStreamingSector",
                "category": category,
                "level": level,
                "nodeData": node_data,
            }
        },
    }


def write_sector(path: Path, document: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(document, sort_keys=True), encoding="utf-8")


@dataclass(frozen=True)
class ForeignBounds:
    min_x: float
    min_y: float
    min_z: float
    max_x: float
    max_y: float
    max_z: float


class WorldLocationSpatialTests(unittest.TestCase):
    def test_indexes_typed_and_plain_positions_and_queries_in_three_dimensions(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            write_sector(
                root / "near.streamingsector.json",
                sector_document(
                    [
                        position(1, typed("2.5"), typed(3)),
                        position(9, 8, 7),
                        {"NodeIndex": 2},
                        position("not-a-number", 4, 5),
                    ],
                    archive_name=typed(r"BASE/worlds/test/near.streamingsector"),
                    category=typed("Quest"),
                    level=typed("2"),
                ),
            )
            write_sector(
                root / "high.streamingsector.json",
                sector_document(
                    [position(2, 2, 100)],
                    archive_name="base/worlds/test/high.streamingsector",
                ),
            )

            index = build_sector_spatial_index(root)

            self.assertEqual(2, len(index.records))
            near = index.for_depot_path(r"base\worlds\test\near.streamingsector")[0]
            self.assertEqual(Bounds3D(1, 2.5, 3, 9, 8, 7), near.bounds)
            self.assertEqual(4, near.node_count)
            self.assertEqual(2, near.located_node_count)
            self.assertEqual(2, near.unlocated_node_count)
            self.assertEqual(
                ((1.0, 2.5, 3.0), (9.0, 8.0, 7.0)), near.placement_positions
            )
            self.assertEqual("quest", near.category)
            self.assertEqual(2, near.level)
            self.assertEqual("near.streamingsector.json", near.source.relative_path)
            self.assertEqual(64, len(near.source.sha256))

            # A six-tuple, pair of triples, and unrelated bounds dataclass are
            # accepted without importing the staging module's AABB type.
            self.assertEqual((near,), index.query((0, 0, 0, 10, 10, 10)))
            self.assertEqual((near,), index.query(((9, 8, 7), (9, 8, 7))))
            self.assertEqual((near,), index.query(ForeignBounds(0, 0, 0, 10, 10, 10)))
            self.assertEqual((), index.query((0, 0, 20, 10, 10, 90)))

    def test_exact_placement_query_rejects_empty_space_inside_sparse_bounds(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            write_sector(
                root / "sparse.streamingsector.json",
                sector_document(
                    [position(-100, 0, 0), position(100, 0, 0)],
                    category="Quest",
                ),
            )

            index = build_sector_spatial_index(root)

            middle = (-5, -5, -5, 5, 5, 5)
            self.assertEqual(1, len(index.query(middle)))
            self.assertEqual((), index.query_placements(middle))
            self.assertEqual(
                index.records,
                index.query_placements((-101, -1, -1, -99, 1, 1)),
            )

    def test_no_position_sector_is_preserved_but_never_spatially_selected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            write_sector(
                root / "quest" / "empty.streamingsector.json",
                sector_document(
                    [{"NodeIndex": 0}, "invalid-node"],
                    archive_name=None,
                    category="Quest",
                    direct_node_data=True,
                ),
            )

            index = build_sector_spatial_index(root)

            self.assertEqual(1, len(index.unlocated_records))
            record = index.unlocated_records[0]
            self.assertIsNone(record.bounds)
            self.assertEqual(2, record.node_count)
            self.assertEqual(0, record.located_node_count)
            self.assertEqual(2, record.unlocated_node_count)
            self.assertEqual(r"quest\empty.streamingsector", record.depot_path)
            self.assertEqual((), index.query((-1e9, -1e9, -1e9, 1e9, 1e9, 1e9)))

    def test_absolute_audit_header_uses_depot_relative_source_path(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            root = workspace / "vanilla-quest-sectors-20260726"
            relative = Path(
                "base/worlds/03_night_city/_compiled/default/"
                "quest_00ec92ff68f21ce9.streamingsector.json"
            )
            write_sector(
                root / relative,
                sector_document(
                    [position(-1500.0, 800.0, 25.0)],
                    archive_name=(
                        r"H:\Ghostline-audits\vanilla-quest-sectors-20260726"
                        r"\base\worlds\03_night_city\_compiled\default"
                        r"\quest_00ec92ff68f21ce9.streamingsector"
                    ),
                    category="Quest",
                ),
            )

            index = build_sector_spatial_index(root)

            depot_path = (
                r"base\worlds\03_night_city\_compiled\default"
                r"\quest_00ec92ff68f21ce9.streamingsector"
            )
            record = index.for_depot_path(depot_path)[0]
            self.assertEqual(depot_path, record.depot_path)
            self.assertEqual(relative.as_posix(), record.source.relative_path)
            self.assertEqual(
                (record,),
                index.query((-1501.0, 799.0, 24.0, -1499.0, 801.0, 26.0)),
            )

    def test_records_are_deterministic_across_root_order(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            alpha = workspace / "alpha"
            beta = workspace / "beta"
            write_sector(
                alpha / "z.streamingsector.json",
                sector_document(
                    [position(0, 0, 0)], archive_name=r"base\z.streamingsector"
                ),
            )
            write_sector(
                beta / "a.streamingsector.json",
                sector_document(
                    [position(1, 1, 1)], archive_name=r"base\a.streamingsector"
                ),
            )

            forward = build_sector_spatial_index([alpha, beta])
            reverse = build_sector_spatial_index([beta, alpha])

            self.assertEqual(forward.snapshot, reverse.snapshot)
            self.assertEqual(forward.records, reverse.records)
            self.assertEqual(
                [r"base\a.streamingsector", r"base\z.streamingsector"],
                [record.depot_path for record in forward.records],
            )

    def test_cache_is_reused_and_invalidated_by_root_snapshot(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            root = workspace / "serialized"
            cache = workspace / "cache" / "sector-spatial-index.json"
            source = root / "fixture.streamingsector.json"
            write_sector(source, sector_document([position(1, 2, 3)]))

            first = build_sector_spatial_index(root, cache_path=cache)
            first_cache_bytes = cache.read_bytes()
            first_snapshot = snapshot_sector_json_roots(root)
            second = build_sector_spatial_index(root, cache_path=cache)

            self.assertFalse(first.cache_hit)
            self.assertTrue(second.cache_hit)
            self.assertEqual(first_snapshot, second.snapshot)
            self.assertEqual(first_cache_bytes, cache.read_bytes())

            write_sector(
                source, sector_document([position(1, 2, 3), position(100, 200, 300)])
            )
            third = build_sector_spatial_index(root, cache_path=cache)

            self.assertFalse(third.cache_hit)
            self.assertNotEqual(first_snapshot, third.snapshot)
            self.assertEqual(2, third.records[0].node_count)
            self.assertEqual(Bounds3D(1, 2, 3, 100, 200, 300), third.records[0].bounds)

    def test_rejects_invalid_roots_and_bounds(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            with self.assertRaises(SpatialIndexError):
                build_sector_spatial_index([])
            with self.assertRaises(SpatialIndexError):
                build_sector_spatial_index(root / "missing")
            with self.assertRaises(SpatialIndexError):
                Bounds3D(2, 0, 0, 1, 1, 1)


if __name__ == "__main__":
    unittest.main()
