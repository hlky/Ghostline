from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

from tests import test_braindance_rid as rid_fixtures


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
MODULE_SPEC = importlib.util.spec_from_file_location(
    "braindance_pipeline", TOOLS / "braindance_pipeline.py"
)
assert MODULE_SPEC is not None
pipeline = importlib.util.module_from_spec(MODULE_SPEC)
assert MODULE_SPEC.loader is not None
MODULE_SPEC.loader.exec_module(pipeline)


def scene_template(handoff: dict[str, object]) -> dict[str, object]:
    events: list[dict[str, object]] = []
    for actor in handoff["actors"]:
        events.append(
            {
                "$type": "scnPlaySkAnimEvent",
                "performer": {
                    "$type": "scnPerformerId",
                    "id": actor["performer_id"],
                },
                "duration": 1,
                "animName": {
                    "HandleId": str(len(events) + 1),
                    "Data": {
                        "$type": "scnAnimName",
                        "type": "direct",
                        "unk1": [],
                        "unk2": [],
                    },
                },
                "rootMotionData": {
                    "$type": "scnPlaySkAnimRootMotionData",
                    "enabled": 0,
                    "originMarker": {
                        "$type": "scnMarker",
                        "nodeRef": {
                            "$type": "NodeRef",
                            "$storage": "string",
                            "$value": "#old",
                        },
                    },
                    "originOffset": {},
                    "trajectoryLOD": [],
                },
            }
        )
        for channel, component in (
            ("facial", "head"),
            ("cyberware", "cyberware"),
        ):
            if actor.get(channel) is not None:
                events.append(
                    {
                        "$type": "scnPlayRidAnimEvent",
                        "performer": {
                            "$type": "scnPerformerId",
                            "id": actor["performer_id"],
                        },
                        "actorComponent": {
                            "$type": "CName",
                            "$storage": "string",
                            "$value": component,
                        },
                        "duration": 1,
                        "animResRefId": {
                            "$type": "scnRidAnimationSRRefId",
                            "id": 99,
                        },
                    }
                )
    events.extend(
        [
            {
                "$type": "scneventsPlayRidCameraAnimEvent",
                "duration": 1,
                "animSRRefId": {
                    "$type": "scnRidCameraAnimationSRRefId",
                    "id": 99,
                },
                "animOriginMarker": {
                    "$type": "scnMarker",
                    "nodeRef": {
                        "$type": "NodeRef",
                        "$storage": "string",
                        "$value": "#old",
                    },
                },
            },
            {
                "$type": "scneventsBraindanceVisibilityEvent",
                "performerId": {"$type": "scnPerformerId", "id": 258},
            },
            {
                "$type": "scneventsBraindanceVisibilityEvent",
                "performerId": {"$type": "scnPerformerId", "id": 2},
            },
            {
                "$type": "scneventsClueEvent",
                "layer": "Visual",
                "clueEntity": {
                    "dynamicEntityUniqueName": {
                        "$value": "p_test_encrypted_shard"
                    },
                    "reference": {"$value": "0"},
                    "names": [],
                },
            },
            {
                "$type": "scneventsClueEvent",
                "layer": "Audio",
                "clueEntity": {
                    "dynamicEntityUniqueName": {"$value": "0"},
                    "reference": {"$value": "#guard"},
                    "names": [],
                },
            },
            {
                "$type": "scneventsClueEvent",
                "layer": "Thermal",
                "clueEntity": {
                    "dynamicEntityUniqueName": {"$value": "0"},
                    "reference": {"$value": "#guard"},
                    "names": [],
                },
            },
        ]
    )
    return {
        "Header": {"DataType": "CR2W"},
        "Data": {
            "RootChunk": {
                "$type": "scnSceneResource",
                "actors": [
                    {
                        "$type": "scnActorDef",
                        "actorId": {
                            "$type": "scnActorId",
                            "id": actor["actor_id"],
                        },
                        "actorName": actor["display_name"],
                        "animSets": [],
                        "facialAnimSets": [],
                        "cyberwareAnimSets": [],
                    }
                    for actor in handoff["actors"]
                ],
                "props": [
                    {
                        "$type": "scnPropDef",
                        "propId": {"$type": "scnPropId", "id": 0},
                        "propName": "test_bdview",
                    },
                    {
                        "$type": "scnPropDef",
                        "propId": {"$type": "scnPropId", "id": 1},
                        "propName": "test_bdfog",
                    },
                    {
                        "$type": "scnPropDef",
                        "propId": {"$type": "scnPropId", "id": 2},
                        "propName": "encrypted_shard",
                        "spawnDespawnParams": {
                            "dynamicEntityUniqueName": {
                                "$value": "p_test_encrypted_shard"
                            }
                        },
                    },
                ],
                "resouresReferences": {},
                "ridResources": [],
                "exitPoints": [{"name": "out"}],
                "interruptionScenarios": [{"name": "interrupt"}],
                "sceneGraph": {
                    "HandleId": "100",
                    "Data": {
                        "$type": "scnSceneGraph",
                        "graph": [
                            {
                                "HandleId": "101",
                                "Data": {
                                    "$type": "scnRewindableSectionNode",
                                    "events": [
                                        {"HandleId": str(200 + i), "Data": event}
                                        for i, event in enumerate(events)
                                    ],
                                },
                            }
                        ],
                    },
                },
            }
        },
    }


def quest_template() -> dict[str, object]:
    return {
        "Header": {"DataType": "CR2W"},
        "Data": {
            "RootChunk": {
                "$type": "questQuestPhaseResource",
                "graph": [
                    {
                        "HandleId": "1",
                        "Data": {
                            "$type": "questSceneNodeDefinition",
                            "sceneFile": {
                                "DepotPath": {
                                    "$type": "ResourcePath",
                                    "$storage": "string",
                                    "$value": "base\\old.scene",
                                },
                                "Flags": "Default",
                            },
                            "sceneLocation": {
                                "$type": "NodeRef",
                                "$storage": "string",
                                "$value": "#old",
                            },
                        },
                    },
                    {
                        "HandleId": "2",
                        "Data": {
                            "$type": "questPauseConditionNodeDefinition",
                        },
                    },
                ],
            }
        },
    }


class BraindancePipelineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        spec = rid_fixtures.braindance_scene.load_json(
            rid_fixtures.SPEC_PATH
        )
        cls.handoff = rid_fixtures.braindance_scene.build_handoff_manifest(
            spec,
            rid_fixtures.SPEC_PATH,
        )
        rid_fixtures.strip_actor_rig_contracts(cls.handoff)
        cls.handoff["animation_samples"] = rid_fixtures.animation_samples()
        cls.rid, _ = rid_fixtures.braindance_rid.compile_rid_document(
            cls.handoff,
            rid_fixtures.template(),
        )

    def test_scene_linker_builds_reference_tables_and_retargets_events(self) -> None:
        linked, report = pipeline.link_scene_document(
            scene_template(self.handoff),
            self.rid,
            self.handoff,
            rid_depot_path=(
                "mod\\gqt005\\braindance\\"
                "gqt005_braindance_analysis.scenerid"
            ),
            scene_origin="#gqt005_bd_origin",
            camera_ref="#gqt005_bd_camera",
        )
        root = linked["Data"]["RootChunk"]
        references = root["resouresReferences"]

        self.assertTrue(report["ok"], report["errors"])
        self.assertEqual(len(references["ridAnimations"]), 2)
        self.assertEqual(len(references["ridAnimSets"]), 2)
        self.assertEqual(len(references["ridCameraAnimations"]), 1)
        self.assertEqual(report["event_counts"]["body"], 2)
        self.assertEqual(report["event_counts"]["camera"], 1)
        actors = linked["Data"]["RootChunk"]["actors"]
        self.assertEqual(
            [actor["animSets"] for actor in actors],
            [
                [{"$type": "scnSRRefId", "id": 0}],
                [{"$type": "scnSRRefId", "id": 1}],
            ],
        )

    def test_scene_linker_adds_untracked_spawn_set_replacer(
        self,
    ) -> None:
        template = scene_template(self.handoff)
        root = template["Data"]["RootChunk"]
        root["playerActors"] = [
            {
                "$type": "scnPlayerActorDef",
                "actorId": {
                    "$type": "scnActorId",
                    "id": 2,
                },
                "playerName": "Player",
            }
        ]
        root["debugSymbols"] = {
            "performersDebugSymbols": [
                {
                    "$type": "scnPerformerSymbol",
                    "performerId": {
                        "$type": "scnPerformerId",
                        "id": 513,
                    },
                }
            ]
        }
        rewindable = root["sceneGraph"]["Data"]["graph"][0]["Data"]
        rewindable["nodeId"] = {"$type": "scnNodeId", "id": 20}
        rewindable["actorBehaviors"] = [
            {
                "$type": "scnSectionInternalsActorBehavior",
                "actorId": {
                    "$type": "scnActorId",
                    "id": actor_id,
                },
                "behaviorMode": "OnlyIfAlive",
            }
            for actor_id in (0, 1, 2)
        ]

        linked, report = pipeline.link_scene_document(
            template,
            self.rid,
            self.handoff,
            rid_depot_path="mod\\gqt005\\braindance\\audit.scenerid",
            scene_origin="#gqt005_bd_origin",
            camera_ref="#gqt005_bd_camera",
            scene_spawn_set_actors=[
                {
                    "actor_name": "bd_replacer",
                    "entry_name": "bd_replacer",
                    "spawn_set_ref": "#gqt005_bd_replacer",
                }
            ],
        )
        root = linked["Data"]["RootChunk"]
        rewindable = root["sceneGraph"]["Data"]["graph"][0]["Data"]
        replacer = next(
            actor
            for actor in root["actors"]
            if actor["actorName"] == "bd_replacer"
        )
        player = root["playerActors"][0]

        self.assertTrue(report["ok"], report["errors"])
        self.assertEqual(
            sorted(
                actor["actorId"]["id"]
                for actor in [*root["actors"], *root["playerActors"]]
            ),
            [0, 1, 2, 3],
        )
        self.assertEqual(replacer["actorId"]["id"], 2)
        self.assertEqual(player["actorId"]["id"], 3)
        self.assertEqual(replacer["acquisitionPlan"], "spawnSet")
        self.assertEqual(
            replacer["spawnSetParams"]["entryName"]["$value"],
            "bd_replacer",
        )
        self.assertEqual(
            replacer["spawnSetParams"]["reference"]["$value"],
            "#gqt005_bd_replacer",
        )
        self.assertEqual(
            replacer["communityParams"]["entryName"]["$value"],
            "None",
        )
        self.assertEqual(
            replacer["communityParams"]["reference"]["$value"],
            "0",
        )
        self.assertEqual(replacer["animSets"], [])
        self.assertEqual(replacer["facialAnimSets"], [])
        self.assertEqual(replacer["cyberwareAnimSets"], [])
        self.assertEqual(
            sorted(
                behavior["actorId"]["id"]
                for behavior in rewindable["actorBehaviors"]
            ),
            [0, 1, 2, 3],
        )
        self.assertEqual(
            report["scene_spawn_set_actors"],
            [
                {
                    "actor_name": "bd_replacer",
                    "actor_id": 2,
                    "performer_id": 513,
                    "spawn_set_ref": "#gqt005_bd_replacer",
                    "entry_name": "bd_replacer",
                    "rewindable_section_ids": [20],
                }
            ],
        )
        self.assertEqual(report["event_counts"]["body"], 2)
        rid_performers = {
            event["Data"].get("performer", {}).get("id")
            for event in rewindable["events"]
            if event["Data"].get("$type")
            in {"scnPlaySkAnimEvent", "scnPlayRidAnimEvent"}
        }
        self.assertNotIn(513, rid_performers)
        replacer_symbol = next(
            symbol
            for symbol in root["debugSymbols"][
                "performersDebugSymbols"
            ]
            if symbol["performerId"]["id"] == 513
        )
        self.assertEqual(
            replacer_symbol["entityRef"]["names"][0]["$value"],
            "bd_replacer",
        )
        self.assertEqual(
            replacer_symbol["entityRef"]["reference"]["$value"],
            "#gqt005_bd_replacer",
        )
        self.assertTrue(
            any(
                symbol["performerId"]["id"] == 769
                for symbol in root["debugSymbols"][
                    "performersDebugSymbols"
                ]
            )
        )

    def test_scene_audit_rejects_unbound_actor_rid_sets(self) -> None:
        linked, _ = pipeline.link_scene_document(
            scene_template(self.handoff),
            self.rid,
            self.handoff,
            rid_depot_path="mod\\gqt005\\braindance\\audit.scenerid",
            scene_origin="#gqt005_bd_origin",
            camera_ref="#gqt005_bd_camera",
        )
        linked["Data"]["RootChunk"]["actors"][0]["animSets"] = []
        report = pipeline.audit_scene_document(linked, handoff=self.handoff)
        self.assertFalse(report["ok"])
        self.assertIn(
            "Actor Patch has no bound RID body set",
            report["errors"],
        )

    def test_scene_audit_rejects_sparse_actor_ids(self) -> None:
        linked, _ = pipeline.link_scene_document(
            scene_template(self.handoff),
            self.rid,
            self.handoff,
            rid_depot_path="mod\\gqt005\\braindance\\audit.scenerid",
            scene_origin="#gqt005_bd_origin",
            camera_ref="#gqt005_bd_camera",
        )
        linked["Data"]["RootChunk"]["actors"][1]["actorId"]["id"] = 9
        report = pipeline.audit_scene_document(linked, handoff=self.handoff)
        self.assertFalse(report["ok"])
        self.assertIn(
            "Scene actor IDs must be dense from zero; found 0, 9",
            report["errors"],
        )
        encoded = json.dumps(linked)
        self.assertIn("#gqt005_bd_origin", encoded)
        self.assertNotIn("#old", encoded)

    def test_scene_audit_rejects_sparse_prop_ids(self) -> None:
        linked, _ = pipeline.link_scene_document(
            scene_template(self.handoff),
            self.rid,
            self.handoff,
            rid_depot_path="mod\\gqt005\\braindance\\audit.scenerid",
            scene_origin="#gqt005_bd_origin",
            camera_ref="#gqt005_bd_camera",
        )
        linked["Data"]["RootChunk"]["props"] = [
            {"propId": {"id": 0}},
            {"propId": {"id": 8}},
        ]
        report = pipeline.audit_scene_document(linked, handoff=self.handoff)
        self.assertFalse(report["ok"])
        self.assertIn(
            "Scene prop IDs must be dense from zero; found 0, 8",
            report["errors"],
        )

    def test_quest_linker_retargets_scene_and_keeps_cleanup_gate(self) -> None:
        linked, report = pipeline.link_quest_document(
            quest_template(),
            scene_depot_path=(
                "mod\\gqt005\\scenes\\"
                "gqt005_braindance_analysis.scene"
            ),
            scene_origin="#gqt005_bd_origin",
        )
        encoded = json.dumps(linked)

        self.assertEqual(report["pause_condition_nodes"], 1)
        self.assertIn("gqt005_braindance_analysis.scene", encoded)
        self.assertIn("#gqt005_bd_origin", encoded)

    def test_quest_linker_retargets_world_marker_node_ref(self) -> None:
        template = quest_template()
        scene = template["Data"]["RootChunk"]["graph"][0]["Data"]
        scene["sceneLocation"] = {
            "$type": "scnWorldMarker",
            "nodeRef": {
                "$type": "NodeRef",
                "$storage": "string",
                "$value": "#old",
            },
            "tag": {
                "$type": "CName",
                "$storage": "string",
                "$value": "None",
            },
            "type": "NodeRef",
        }
        linked, _ = pipeline.link_quest_document(
            template,
            scene_depot_path="mod\\gqt005\\scenes\\test.scene",
            scene_origin="#gqt005_bd_origin",
        )
        location = (
            linked["Data"]["RootChunk"]["graph"][0]["Data"]["sceneLocation"]
        )
        self.assertEqual(location["$type"], "scnWorldMarker")
        self.assertEqual(location["nodeRef"]["$value"], "#gqt005_bd_origin")

    def test_scene_linker_maps_facial_and_cyberware_events(self) -> None:
        handoff = copy.deepcopy(self.handoff)
        for channel, bone_count, track_index in (
            ("facial", 344, 17),
            ("cyberware", 30, None),
        ):
            handoff["actors"][0][channel] = {"armature": f"{channel}Rig"}
            sampled = {
                "armature": f"{channel}Rig",
                "bone_count": bone_count,
                "joints": [],
                "tracks": [],
            }
            if track_index is not None:
                sampled["tracks"] = [
                    {
                        "index": track_index,
                        "samples": [
                            {"frame": frame, "value": frame / 360.0}
                            for frame in range(361)
                        ],
                    }
                ]
            else:
                sampled["joints"] = [
                    {
                        "index": 3,
                        "name": "cyber_joint",
                        "samples": [
                            {
                                "frame": frame,
                                "translation": [0.0, 0.0, frame / 3600.0],
                                "rotation": [0.0, 0.0, 0.0, 1.0],
                                "scale": [1.0, 1.0, 1.0],
                            }
                            for frame in range(361)
                        ],
                    }
                ]
            handoff["animation_samples"]["actors"][0][channel] = sampled
        rid, _ = rid_fixtures.braindance_rid.compile_rid_document(
            handoff,
            rid_fixtures.template(),
        )

        linked, report = pipeline.link_scene_document(
            scene_template(handoff),
            rid,
            handoff,
            rid_depot_path="mod\\gqt005\\braindance\\full.scenerid",
            scene_origin="#gqt005_bd_origin",
            camera_ref="#gqt005_bd_camera",
        )

        references = linked["Data"]["RootChunk"]["resouresReferences"]
        self.assertEqual(report["event_counts"]["facial"], 1)
        self.assertEqual(report["event_counts"]["cyberware"], 1)
        actor = linked["Data"]["RootChunk"]["actors"][0]
        self.assertEqual(
            actor["facialAnimSets"],
            [{"$type": "scnRidFacialAnimSetSRRefId", "id": 0}],
        )
        self.assertEqual(
            actor["cyberwareAnimSets"],
            [{"$type": "scnRidCyberwareAnimSetSRRefId", "id": 0}],
        )
        self.assertEqual(len(references["ridFacialAnimSets"]), 1)
        self.assertEqual(len(references["ridCyberwareAnimSets"]), 1)

    def test_package_and_runtime_evidence_are_hash_bound(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            temp = Path(directory)
            source = temp / "asset.scenerid"
            source.write_bytes(b"CR2W authored test")
            depot = temp / "archive"
            package = pipeline.package_assets(
                [
                    (
                        source,
                        "mod\\gqt005\\braindance\\asset.scenerid",
                    )
                ],
                depot_root=depot,
            )
            evidence = pipeline.init_runtime_evidence(
                name="gqt005_braindance_analysis",
                package_manifest=package,
            )
            pending = pipeline.verify_runtime_evidence(
                evidence,
                depot_root=depot,
            )
            self.assertFalse(pending["ok"])
            for case in pipeline.RUNTIME_CASES:
                evidence = pipeline.record_runtime_case(
                    evidence,
                    case=case,
                    passed=True,
                    notes=f"Verified {case} in a clean save",
                )
            verified = pipeline.verify_runtime_evidence(
                evidence,
                depot_root=depot,
            )
            self.assertTrue(verified["ok"], verified["errors"])
            self.assertEqual(
                verified["passed_cases"],
                len(pipeline.RUNTIME_CASES),
            )

    def test_package_rejects_paths_outside_depot(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            temp = Path(directory)
            source = temp / "asset.scene"
            source.write_bytes(b"CR2W")
            with self.assertRaises(pipeline.BraindancePipelineError):
                pipeline.package_assets(
                    [(source, "..\\outside.scene")],
                    depot_root=temp / "archive",
                )

    def test_package_accepts_asset_already_at_its_depot_target(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            depot = Path(directory) / "archive"
            source = depot / "mod" / "gqt005" / "asset.scene"
            source.parent.mkdir(parents=True)
            source.write_bytes(b"CR2W")

            report = pipeline.package_assets(
                [(source, "mod\\gqt005\\asset.scene")],
                depot_root=depot,
            )

            self.assertEqual(report["entries"][0]["sha256"], pipeline.file_sha256(source))


if __name__ == "__main__":
    unittest.main()
