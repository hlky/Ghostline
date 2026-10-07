from __future__ import annotations

import copy
import base64
import json
from pathlib import Path
import struct
import sys
import tempfile
import unittest
from unittest import mock
import zlib

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from cr2w_validation import canonical_document, compare_documents
import cr2w_validation
import quest_build
from quest_compiler import PhaseGraphBuilder, input_node, output_node, phase_document


SCHEMA = {
    "Probe": {
        "base": "Base",
        "properties": {
            "precise": {"cs_type": "CDouble"},
            "defaultValue": {"cs_type": "CInt32"},
        },
    },
    "Base": {"properties": {"value": {"cs_type": "CFloat"}}},
    "questQuestPhaseResource": {
        "properties": {"phasePrefabs": {"cs_type": "CArray<questQuestPrefabEntry>"}}
    },
    "BloomAreaSettings": {"properties": {"enable": {"cs_type": "CBool"}}},
}


def document(**values):
    return {"Header": {}, "Data": {"RootChunk": {"$type": "Probe", **values}}}


def phase():
    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    builder.connect(start, end)
    return phase_document(builder, Path("probe.questphase"))


class Cr2wComparisonTests(unittest.TestCase):
    def test_handle_reallocation_preserves_graph_and_socket_order_matters(self):
        original = phase()
        changed = copy.deepcopy(original)

        def remap(value):
            if isinstance(value, dict):
                for key, child in value.items():
                    if key in {"HandleId", "HandleRefId"} and int(child) >= 0:
                        value[key] = str(int(child) + 100)
                    else:
                        remap(child)
            elif isinstance(value, list):
                for child in value:
                    remap(child)

        remap(changed)
        self.assertEqual(canonical_document(original), canonical_document(changed))
        node = changed["Data"]["RootChunk"]["graph"]["Data"]["nodes"][0]["Data"]
        node["sockets"].reverse()
        self.assertFalse(compare_documents(original, changed, schema=SCHEMA).ok)

    def test_dropped_populated_prefab_array_is_never_a_default(self):
        expected = phase()
        expected["Data"]["RootChunk"]["phasePrefabs"] = [
            {
                "$type": "questQuestPrefabEntry",
                "prefabNodeRef": {
                    "$type": "NodeRef",
                    "$storage": "string",
                    "$value": "#probe",
                },
            }
        ]
        actual = copy.deepcopy(expected)
        actual["Data"]["RootChunk"]["phasePrefabs"] = []
        result = compare_documents(
            expected, actual, schema=SCHEMA, fresh_wolvenkit_defaults=actual
        )
        self.assertFalse(result.ok)
        self.assertIn("$.root.phasePrefabs", [error["path"] for error in result.errors])

    def test_float_rounding_requires_reflected_float32_and_equal_bits(self):
        rounded = struct.unpack("<f", struct.pack("<f", 0.92))[0]
        self.assertTrue(
            compare_documents(
                document(value=0.92), document(value=rounded), schema=SCHEMA
            ).ok
        )
        self.assertFalse(
            compare_documents(
                document(precise=0.92), document(precise=rounded), schema=SCHEMA
            ).ok
        )
        self.assertFalse(
            compare_documents(
                document(value=0.92), document(value=0.921), schema=SCHEMA
            ).ok
        )

    def test_tweak_identity_is_verified_and_cannot_hide_extra_fields(self):
        name = "Items.GhostlineQuietSpine01"
        identifier = zlib.crc32(name.encode()) + (len(name) << 32)
        left = {"$type": "TweakDBID", "$storage": "string", "$value": name}
        right = {"$type": "TweakDBID", "$storage": "uint64", "$value": str(identifier)}
        self.assertTrue(
            compare_documents(
                document(item=left), document(item=right), schema=SCHEMA
            ).ok
        )
        right["$value"] = str(identifier + 1)
        self.assertFalse(
            compare_documents(
                document(item=left), document(item=right), schema=SCHEMA
            ).ok
        )
        right["$value"] = str(identifier)
        left["unexpected"] = True
        self.assertFalse(
            compare_documents(
                document(item=left), document(item=right), schema=SCHEMA
            ).ok
        )

    def test_added_defaults_require_pinned_values_reflection_and_fresh_writer(self):
        expected, actual = document(value=1), document(value=1, defaultValue=0)
        self.assertFalse(compare_documents(expected, actual, schema=SCHEMA).ok)
        self.assertFalse(
            compare_documents(
                expected, actual, schema=SCHEMA, fresh_wolvenkit_defaults=actual
            ).ok
        )
        expected = document(settings={"$type": "BloomAreaSettings"})
        actual = document(settings={"$type": "BloomAreaSettings", "enable": 1})
        self.assertTrue(
            compare_documents(
                expected, actual, schema=SCHEMA, fresh_wolvenkit_defaults=actual
            ).ok
        )
        with mock.patch.object(cr2w_validation, "_scene_defaults", return_value={}):
            self.assertFalse(
                compare_documents(
                    expected, actual, schema=SCHEMA, fresh_wolvenkit_defaults=actual
                ).ok
            )
        unknown = document(value=1, inventedDefault=0)
        self.assertFalse(
            compare_documents(
                expected, unknown, schema=SCHEMA, fresh_wolvenkit_defaults=unknown
            ).ok
        )
        self.assertFalse(
            compare_documents(
                actual, expected, schema=SCHEMA, fresh_wolvenkit_defaults=expected
            ).ok
        )

    def test_graph_socket_metadata_membership_and_connection_order_are_checked(self):
        builder = PhaseGraphBuilder()
        start, first = input_node(builder), output_node(builder)
        second = builder.node(
            2, "questOutputNodeDefinition", input_names=("In",), output_names=()
        )
        builder.connect(start, first)
        builder.connect(start, second)
        original = phase_document(builder, Path("probe.questphase"))
        for change in (
            "remove_membership",
            "reverse_fanout",
            "socket_type",
            "connection_metadata",
        ):
            with self.subTest(change=change):
                altered = copy.deepcopy(original)
                nodes = altered["Data"]["RootChunk"]["graph"]["Data"]["nodes"]
                wrappers = []

                def collect(value):
                    if isinstance(value, dict):
                        wrappers.append(value)
                        for child in value.values():
                            collect(child)
                    elif isinstance(value, list):
                        for child in value:
                            collect(child)

                collect(altered)
                definitions = {
                    item["HandleId"]: item["Data"]
                    for item in wrappers
                    if "HandleId" in item
                }
                socket = next(
                    definitions[item.get("HandleId", item.get("HandleRefId"))]
                    for item in nodes[0]["Data"]["sockets"]
                    if len(
                        definitions[item.get("HandleId", item.get("HandleRefId"))].get(
                            "connections", []
                        )
                    )
                    == 2
                )
                if change == "reverse_fanout":
                    socket["connections"].reverse()
                elif change == "socket_type":
                    socket["$type"] = "WrongSocketClass"
                elif change == "connection_metadata":
                    connection = next(
                        item
                        for item in definitions.values()
                        if item.get("$type") == "graphGraphConnectionDefinition"
                    )
                    connection["unexpected"] = 1
                else:
                    incoming = next(
                        definitions[item.get("HandleId", item.get("HandleRefId"))]
                        for item in nodes[1]["Data"]["sockets"]
                        if definitions[
                            item.get("HandleId", item.get("HandleRefId"))
                        ].get("connections")
                    )
                    incoming["connections"] = []
                self.assertFalse(compare_documents(original, altered, schema=SCHEMA).ok)

    def test_embedded_files_and_unrequested_nonempty_arrays_cannot_disappear(self):
        expected = document(value=1)
        expected["Data"]["EmbeddedFiles"] = [
            {"FileName": "owned.bin", "content": "aGVsbG8="}
        ]
        self.assertFalse(
            compare_documents(expected, document(value=1), schema=SCHEMA).ok
        )
        expected = phase()
        expected["Data"]["RootChunk"].pop("phasePrefabs", None)
        actual = copy.deepcopy(expected)
        actual["Data"]["RootChunk"]["phasePrefabs"] = [{"prefabNodeRef": "#unexpected"}]
        self.assertFalse(
            compare_documents(
                expected, actual, schema=SCHEMA, fresh_wolvenkit_defaults=actual
            ).ok
        )

    def test_broken_handle_references_fail_closed(self):
        with self.assertRaisesRegex(ValueError, "Unresolved"):
            canonical_document(document(value={"HandleRefId": "77"}))

    def test_shared_value_aliasing_fails_closed_instead_of_collapsing_identity(self):
        shared = document(
            first={"HandleId": "1", "Data": {"$type": "State", "value": 7}},
            second={"HandleRefId": "1"},
        )
        split = copy.deepcopy(shared)
        split["Data"]["RootChunk"]["second"] = {
            "HandleId": "2",
            "Data": {"$type": "State", "value": 7},
        }
        for expected, actual in ((shared, split), (split, shared), (shared, shared)):
            with self.subTest(expected=expected):
                with self.assertRaisesRegex(ValueError, "Unsupported shared"):
                    compare_documents(expected, actual, schema=SCHEMA)

    def test_area_outline_retains_packed_geometry_and_bound_reader_defaults(self):
        points = [(0, 0, 0), (4, 0, 0), (0, 4, 0)]
        packed = struct.pack("<I", len(points))
        packed += b"".join(struct.pack("<4f", *point, 0) for point in points)
        packed += struct.pack("<f", 8)
        outline = {
            "$type": "AreaShapeOutline",
            "buffer": base64.b64encode(packed).decode(),
            "points": [
                {"$type": "Vector3", **dict(zip(("X", "Y", "Z"), point))}
                for point in points
            ],
            "height": 8,
        }
        reader = copy.deepcopy(outline)
        reader["points"] = [
            {"$type": "Vector3", "X": x, "Y": y, "Z": 0}
            for x, y in [(-1, -1), (1, -1), (1, 1), (-1, 1)]
        ]
        reader["height"] = 2
        result = compare_documents(
            document(outline=outline), document(outline=reader), schema=SCHEMA
        )
        self.assertTrue(result.ok)
        self.assertEqual(len(result.normalizations), 2)
        with mock.patch.object(
            cr2w_validation, "_source_evidence_current", return_value=False
        ):
            with self.assertRaisesRegex(ValueError, "source evidence is stale"):
                compare_documents(
                    document(outline=outline), document(outline=reader), schema=SCHEMA
                )
        changed_buffer = copy.deepcopy(reader)
        changed_buffer["buffer"] = base64.b64encode(
            packed[:-4] + struct.pack("<f", 9)
        ).decode()
        self.assertFalse(
            compare_documents(
                document(outline=outline),
                document(outline=changed_buffer),
                schema=SCHEMA,
            ).ok
        )
        for change in ("points", "height", "truncated", "count"):
            with self.subTest(change=change):
                malformed = copy.deepcopy(outline)
                if change == "points":
                    malformed["points"][1]["X"] = 99
                elif change == "height":
                    malformed["height"] = 99
                elif change == "truncated":
                    malformed["buffer"] = base64.b64encode(packed[:-1]).decode()
                else:
                    malformed["buffer"] = base64.b64encode(
                        struct.pack("<I", 99) + packed[4:]
                    ).decode()
                # Validation must also run before equal-document fast paths.
                with self.assertRaises(ValueError):
                    compare_documents(
                        document(outline=malformed),
                        document(outline=malformed),
                        schema=SCHEMA,
                    )


class ConversionReadBackTests(unittest.TestCase):
    def test_native_magic_success_with_lost_prefabs_uses_verified_wolvenkit(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            raw, candidate, donor, schema = [
                root / name
                for name in (
                    "probe.questphase.json",
                    "probe.questphase",
                    "donor.questphase",
                    "schema.json",
                )
            ]
            expected = phase()
            expected["Data"]["RootChunk"]["phasePrefabs"] = [
                {
                    "$type": "questQuestPrefabEntry",
                    "prefabNodeRef": {
                        "$type": "NodeRef",
                        "$storage": "string",
                        "$value": "#probe",
                    },
                }
            ]
            raw.write_text(json.dumps(expected), encoding="utf-8")
            schema.write_text(json.dumps(SCHEMA), encoding="utf-8")
            donor.write_bytes(b"CR2Wdonor")

            def native(*args, **kwargs):
                candidate.write_bytes(b"CR2Wnative")

            def wolvenkit(command, **kwargs):
                if "-d" in command:
                    candidate.write_bytes(b"CR2Wwolvenkit")
                else:
                    actual = copy.deepcopy(expected)
                    if candidate.read_bytes() == b"CR2Wnative":
                        actual["Data"]["RootChunk"]["phasePrefabs"] = []
                    (Path(command[-1]) / raw.name).write_text(
                        json.dumps(actual), encoding="utf-8"
                    )

            with (
                mock.patch("ghostline_red.ensure_schema", return_value=schema),
                mock.patch.object(
                    quest_build, "native_deserialize", side_effect=native
                ),
                mock.patch.object(
                    quest_build.subprocess, "run", side_effect=wolvenkit
                ) as run,
            ):
                quest_build._convert(
                    raw,
                    candidate,
                    donor,
                    serializer="native",
                    wolvenkit=Path("explicit-wkit"),
                )
            self.assertEqual(candidate.read_bytes(), b"CR2Wwolvenkit")
            self.assertEqual(
                [call.args[0][2] for call in run.call_args_list], ["-s", "-d", "-s"]
            )
            self.assertTrue(
                all(call.args[0][0] == "explicit-wkit" for call in run.call_args_list)
            )

    def test_fresh_wolvenkit_cannot_drop_an_authored_property(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            raw, candidate, schema = (
                root / "one.json",
                root / "one",
                root / "schema.json",
            )
            raw.write_text(json.dumps(document(value=5, required=42)), encoding="utf-8")
            schema.write_text(json.dumps(SCHEMA), encoding="utf-8")

            def wolvenkit(command, **kwargs):
                if "-d" in command:
                    candidate.write_bytes(b"CR2Wbad")
                else:
                    (Path(command[-1]) / raw.name).write_text(
                        json.dumps(document(value=5)), encoding="utf-8"
                    )

            with (
                mock.patch("ghostline_red.ensure_schema", return_value=schema),
                mock.patch.object(quest_build.subprocess, "run", side_effect=wolvenkit),
            ):
                with self.assertRaisesRegex(
                    RuntimeError, "semantic verification failed.*required"
                ):
                    quest_build._convert(
                        raw,
                        candidate,
                        None,
                        serializer="wolvenkit",
                        wolvenkit=Path("wkit"),
                    )


if __name__ == "__main__":
    unittest.main()
