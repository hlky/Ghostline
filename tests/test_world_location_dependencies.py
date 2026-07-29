from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools.world_location_dependencies import (
    ArchiveDependencyResolver,
    BatchInvocation,
    BatchRunResult,
    DependencyStagingError,
    classify_resource,
    complete_blender_dependency_defaults,
    compute_state_closures,
    extract_depot_paths,
    install_dependency_jsons,
    resource_type,
)


ENTITY = r"base\characters\fixture.ent"
APPEARANCE = r"base\characters\fixture.app"
MESH = r"base\characters\fixture.mesh"
RED_APPEARANCE = r"base\characters\fixture_red.app"
BLUE_APPEARANCE = r"base\characters\fixture_blue.app"
RED_MESH = r"base\characters\fixture_red.mesh"
RED_UNUSED_MESH = r"base\characters\fixture_red_unused.mesh"
BLUE_MESH = r"base\characters\fixture_blue.mesh"
COMMON_MESH = r"base\characters\fixture_common.mesh"
PROXY_MESH = r"base\worlds\fixture\_external\proxy\fixture.mesh"
NESTED_ENTITY = r"base\characters\nested.ent"
NESTED_APPEARANCE = r"base\characters\nested.app"
NESTED_MESH = r"base\characters\nested.mesh"
NESTED_UNUSED_MESH = r"base\characters\nested_unused.mesh"


def depot(path: str) -> dict[str, object]:
    return {"DepotPath": {"$storage": "string", "$value": path}}


def document(*references: str) -> dict[str, object]:
    return {
        "Header": {"ArchiveFileName": "fixture"},
        "Data": {
            "RootChunk": {
                "$type": "fixtureResource",
                "references": [depot(reference) for reference in references],
            }
        },
    }


def cname(value: str) -> dict[str, str]:
    return {"$type": "CName", "$storage": "string", "$value": value}


def entity_appearance(
    name: str, appearance_resource: str, appearance_name: str
) -> dict[str, object]:
    return {
        "$type": "entTemplateAppearance",
        "name": cname(name),
        "appearanceResource": depot(appearance_resource),
        "appearanceName": cname(appearance_name),
    }


def selective_entity_document(
    *,
    default: str = "blue_root",
    nested_entity: str | None = None,
) -> dict[str, object]:
    root: dict[str, object] = {
        "$type": "entEntityTemplate",
        "defaultAppearance": cname(default),
        "commonResource": depot(COMMON_MESH),
        "appearances": [
            entity_appearance("red_root", RED_APPEARANCE, "red_internal"),
            entity_appearance("blue_root", BLUE_APPEARANCE, "blue_internal"),
        ],
    }
    if nested_entity is not None:
        root["nestedEntity"] = depot(nested_entity)
    return {
        "Header": {"ArchiveFileName": "fixture.ent"},
        "Data": {"RootChunk": root},
    }


def selective_appearance_document(
    *definitions: tuple[str, str],
) -> dict[str, object]:
    return {
        "Header": {"ArchiveFileName": "fixture.app"},
        "Data": {
            "RootChunk": {
                "$type": "appearanceAppearanceResource",
                "appearances": [
                    {
                        "HandleId": str(index),
                        "Data": {
                            "$type": "appearanceAppearanceDefinition",
                            "name": cname(name),
                            "components": [depot(mesh)],
                            "proxyMesh": depot(PROXY_MESH),
                        },
                    }
                    for index, (name, mesh) in enumerate(definitions)
                ],
            }
        },
    }


class FixtureBatchRunner:
    def __init__(
        self,
        documents: dict[str, dict[str, object]],
        failures: dict[str, str] | None = None,
    ) -> None:
        self.documents = {key.casefold(): value for key, value in documents.items()}
        self.failures = {
            key.casefold(): value for key, value in (failures or {}).items()
        }
        self.invocations: list[BatchInvocation] = []

    def __call__(self, invocation: BatchInvocation) -> BatchRunResult:
        self.invocations.append(invocation)
        outcomes = []
        for job in invocation.jobs:
            error = self.failures.get(job.resource)
            if error is None:
                job.output.parent.mkdir(parents=True, exist_ok=True)
                job.output.write_text(
                    json.dumps(self.documents[job.resource], sort_keys=True),
                    encoding="utf-8",
                )
            outcomes.append(
                {
                    "resource": job.resource,
                    "output": str(job.output.resolve()),
                    "error": error,
                }
            )
        invocation.report_path.parent.mkdir(parents=True, exist_ok=True)
        invocation.report_path.write_text(
            json.dumps(list(reversed(outcomes)), indent=2),
            encoding="utf-8",
        )
        return BatchRunResult(
            returncode=1 if any(outcome["error"] for outcome in outcomes) else 0
        )


class ResolverFixture:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.cache = root / "cache"
        self.archives = root / "game/archive/pc"
        self.archives.mkdir(parents=True)
        self.tool = root / "ghostline-red.exe"
        self.tool.write_bytes(b"fixture ghostline-red v1")
        self.schema = root / "red-schema.json"
        self.schema.write_text('{"fixture":1}', encoding="utf-8")

    def resolver(
        self,
        runner: FixtureBatchRunner,
        *,
        game_identity: str = "fixture-game-v1",
    ) -> ArchiveDependencyResolver:
        return ArchiveDependencyResolver(
            cache_root=self.cache,
            ghostline_red=self.tool,
            schemas=self.schema,
            archives_root=self.archives,
            game_identity=game_identity,
            threads=3,
            runner=runner,
            cwd=self.root,
        )


class WorldLocationDependencyTests(unittest.TestCase):
    def test_resolves_ent_app_mesh_closure_and_installs_cached_json(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            fixture = ResolverFixture(Path(temporary))
            runner = FixtureBatchRunner(
                {
                    ENTITY: document(APPEARANCE),
                    APPEARANCE: document(MESH),
                }
            )

            closure = fixture.resolver(runner).resolve([ENTITY])

            self.assertEqual((ENTITY,), closure.roots)
            self.assertEqual(
                [APPEARANCE, ENTITY, MESH],
                [resource.resource for resource in closure.resources],
            )
            self.assertEqual(
                {
                    ENTITY: (APPEARANCE,),
                    APPEARANCE: (MESH,),
                    MESH: (),
                },
                closure.graph,
            )
            self.assertEqual([], list(closure.failures))
            self.assertEqual(
                {ENTITY, APPEARANCE}, closure.successful_json_sources().keys()
            )
            self.assertEqual(
                document(APPEARANCE), closure.successful_documents()[ENTITY]
            )
            self.assertEqual("entity", classify_resource(ENTITY).kind)
            self.assertTrue(classify_resource(APPEARANCE).serializable)
            self.assertEqual("mesh", classify_resource(MESH).kind)
            self.assertEqual("mesh", resource_type(MESH))

            # The recursive frontier makes one native batch for the entity and
            # another for the newly discovered appearance.
            self.assertEqual(2, len(runner.invocations))
            self.assertEqual(
                (ENTITY,), tuple(job.resource for job in runner.invocations[0].jobs)
            )
            self.assertEqual(
                (APPEARANCE,),
                tuple(job.resource for job in runner.invocations[1].jobs),
            )
            command = runner.invocations[0].command
            self.assertIn("cr2w-serialize-batch", command)
            self.assertEqual("3", command[command.index("--threads") + 1])
            self.assertEqual(
                str(fixture.archives.resolve()),
                command[command.index("--archives-root") + 1],
            )

            entity_target = (
                fixture.root / "project/raw/base/characters/fixture.ent.json"
            )
            appearance_target = (
                fixture.root / "project/raw/base/characters/fixture.app.json"
            )
            entity_target.parent.mkdir(parents=True)
            entity_target.write_text("stale", encoding="utf-8")
            installed = install_dependency_jsons(closure, fixture.root / "project/raw")
            self.assertEqual(2, len(installed))
            actions = {record.resource: record.action for record in installed}
            self.assertEqual("replaced", actions[ENTITY])
            self.assertIn(actions[APPEARANCE], {"hardlinked", "copied", "generated"})
            self.assertTrue(entity_target.is_file())
            self.assertTrue(appearance_target.is_file())
            staged_entity = json.loads(entity_target.read_text())
            self.assertEqual(
                [APPEARANCE],
                [
                    value["DepotPath"]["$value"]
                    for value in staged_entity["Data"]["RootChunk"]["references"]
                ],
            )
            self.assertEqual([], staged_entity["Data"]["RootChunk"]["appearances"])
            self.assertEqual([], staged_entity["Data"]["RootChunk"]["components"])
            self.assertIsNone(staged_entity["Data"]["RootChunk"]["compiledData"])
            self.assertEqual(
                "None",
                staged_entity["Data"]["RootChunk"]["defaultAppearance"]["$value"],
            )
            self.assertTrue(
                staged_entity["Header"]["WolvenKitVersion"].startswith("8.17")
            )

            # A new resolver with the same content identities consumes both
            # cached JSON files and invokes no native process.
            cache_only_runner = FixtureBatchRunner({})
            cached = fixture.resolver(cache_only_runner).resolve([ENTITY])
            self.assertEqual((), tuple(cache_only_runner.invocations))
            self.assertTrue(
                all(
                    resource.cache_hit
                    for resource in cached.resources
                    if resource.serializable
                )
            )
            self.assertEqual(0, cached.to_report()["summary"]["batch_invocations"])

    def test_content_identity_changes_resource_cache_fingerprint(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            fixture = ResolverFixture(Path(temporary))
            documents = {ENTITY: document()}
            first_runner = FixtureBatchRunner(documents)
            first = fixture.resolver(first_runner).resolve([ENTITY])
            first_fingerprint = first.resources[0].cache_fingerprint

            fixture.schema.write_text('{"fixture":2}', encoding="utf-8")
            second_runner = FixtureBatchRunner(documents)
            second = fixture.resolver(second_runner).resolve([ENTITY])

            self.assertEqual(1, len(second_runner.invocations))
            self.assertNotEqual(
                first_fingerprint,
                second.resources[0].cache_fingerprint,
            )

            third_runner = FixtureBatchRunner(documents)
            third = fixture.resolver(
                third_runner, game_identity="fixture-game-v2"
            ).resolve([ENTITY])
            self.assertEqual(1, len(third_runner.invocations))
            self.assertNotEqual(
                second.resources[0].cache_fingerprint,
                third.resources[0].cache_fingerprint,
            )

    def test_blender_dependency_defaults_complete_sparse_entities_only(self) -> None:
        sparse = {
            "Header": {"WolvenKitVersion": "0.1.0"},
            "Data": {
                "RootChunk": {
                    "$type": "entEntityTemplate",
                    "compiledData": {"Data": {"Chunks": []}},
                }
            },
        }

        staged, inserted = complete_blender_dependency_defaults(sparse, ".ent")
        root = staged["Data"]["RootChunk"]

        self.assertEqual([], root["appearances"])
        self.assertEqual([], root["components"])
        self.assertEqual([], root["resolvedDependencies"])
        self.assertEqual("None", root["defaultAppearance"]["$value"])
        self.assertEqual({"Data": {"Chunks": []}}, root["compiledData"])
        self.assertEqual("0.1.0", staged["Header"]["GhostlineOriginalExporterVersion"])
        self.assertIn("entEntityTemplate.appearances", inserted)
        self.assertNotIn("entEntityTemplate.compiledData", inserted)
        self.assertNotIn("appearances", sparse["Data"]["RootChunk"])

    def test_failure_is_reported_and_strict_install_refuses_partial_closure(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            fixture = ResolverFixture(Path(temporary))
            runner = FixtureBatchRunner(
                {ENTITY: document(APPEARANCE)},
                failures={APPEARANCE: "archive resource was not found"},
            )

            closure = fixture.resolver(runner).resolve([ENTITY])

            self.assertEqual(1, len(closure.failures))
            failure = closure.failures[0]
            self.assertEqual(APPEARANCE, failure.resource)
            self.assertEqual("failed", failure.status)
            self.assertEqual("archive resource was not found", failure.error)
            self.assertEqual((APPEARANCE,), closure.batches[-1].failures)
            with self.assertRaisesRegex(
                DependencyStagingError, "archive resource was not found"
            ):
                closure.raise_for_failures()
            with self.assertRaisesRegex(DependencyStagingError, "Cannot install"):
                install_dependency_jsons(closure, fixture.root / "strict/raw")

            installed = install_dependency_jsons(
                closure,
                fixture.root / "partial/raw",
                fail_on_errors=False,
            )
            self.assertEqual([ENTITY], [record.resource for record in installed])
            report = closure.to_report()
            self.assertEqual(1, report["summary"]["failures"])
            self.assertEqual(APPEARANCE, report["resources"][0]["resource"])
            self.assertEqual(
                "archive resource was not found", report["resources"][0]["error"]
            )

    def test_state_appearance_selections_prune_ent_and_app_definitions(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            fixture = ResolverFixture(Path(temporary))
            runner = FixtureBatchRunner(
                {
                    ENTITY: selective_entity_document(),
                    RED_APPEARANCE: selective_appearance_document(
                        ("red_internal", RED_MESH),
                        ("unused_internal", RED_UNUSED_MESH),
                    ),
                    BLUE_APPEARANCE: selective_appearance_document(
                        ("blue_internal", BLUE_MESH)
                    ),
                }
            )

            states = fixture.resolver(runner).resolve_states(
                {"blue-state": [ENTITY], "red-state": [ENTITY]},
                state_appearance_selections={
                    "blue-state": {ENTITY: ["blue_root"]},
                    "red-state": {ENTITY: ["red_root"]},
                },
            )

            self.assertEqual(
                (ENTITY, BLUE_APPEARANCE, BLUE_MESH, COMMON_MESH),
                states.state_resources["blue-state"],
            )
            self.assertEqual(
                (ENTITY, COMMON_MESH, RED_APPEARANCE, RED_MESH),
                states.state_resources["red-state"],
            )
            self.assertNotIn(RED_UNUSED_MESH, states.closure.graph)
            self.assertNotIn(PROXY_MESH, states.closure.graph)
            self.assertEqual(
                ("red_root",),
                states.appearance_selections["red-state"][ENTITY],
            )
            self.assertEqual(
                ("red_internal",),
                states.appearance_selections["red-state"][RED_APPEARANCE],
            )
            self.assertEqual({}, states.unmatched_appearance_selections["red-state"])
            report = states.to_report()
            red_report = next(
                state for state in report["states"] if state["state_key"] == "red-state"
            )
            self.assertEqual(
                [
                    {"resource": ENTITY, "names": ["red_root"]},
                    {
                        "resource": RED_APPEARANCE,
                        "names": ["red_internal"],
                    },
                ],
                red_report["appearance_selections"],
            )

            # Calling the legacy resolver without a selection map keeps the
            # original full-closure behavior, including unused definitions
            # and the streaming proxy paths omitted by the LOD0 POC policy.
            legacy = fixture.resolver(FixtureBatchRunner({})).resolve([ENTITY])
            self.assertIn(RED_UNUSED_MESH, legacy.graph)
            self.assertIn(PROXY_MESH, legacy.graph)

    def test_default_selection_and_nested_entities_use_authored_defaults(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            fixture = ResolverFixture(Path(temporary))
            nested_document = {
                "Header": {"ArchiveFileName": "nested.ent"},
                "Data": {
                    "RootChunk": {
                        "$type": "entEntityTemplate",
                        "defaultAppearance": cname("nested_default_root"),
                        "appearances": [
                            entity_appearance(
                                "nested_default_root",
                                NESTED_APPEARANCE,
                                "nested_default_internal",
                            ),
                            entity_appearance(
                                "nested_unused_root",
                                NESTED_APPEARANCE,
                                "nested_unused_internal",
                            ),
                        ],
                    }
                },
            }
            runner = FixtureBatchRunner(
                {
                    ENTITY: selective_entity_document(nested_entity=NESTED_ENTITY),
                    BLUE_APPEARANCE: selective_appearance_document(
                        ("blue_internal", BLUE_MESH)
                    ),
                    NESTED_ENTITY: nested_document,
                    NESTED_APPEARANCE: selective_appearance_document(
                        ("nested_default_internal", NESTED_MESH),
                        ("nested_unused_internal", NESTED_UNUSED_MESH),
                    ),
                }
            )

            states = fixture.resolver(runner).resolve_states(
                {"state": [ENTITY]},
                state_appearance_selections={"state": {ENTITY: ["default"]}},
            )

            resources = states.state_resources["state"]
            self.assertIn(BLUE_APPEARANCE, resources)
            self.assertIn(BLUE_MESH, resources)
            self.assertNotIn(RED_APPEARANCE, resources)
            self.assertIn(NESTED_ENTITY, resources)
            self.assertIn(NESTED_APPEARANCE, resources)
            self.assertIn(NESTED_MESH, resources)
            self.assertNotIn(NESTED_UNUSED_MESH, resources)
            self.assertEqual(
                ("blue_root",), states.appearance_selections["state"][ENTITY]
            )
            self.assertEqual(
                ("nested_default_root",),
                states.appearance_selections["state"][NESTED_ENTITY],
            )

    def test_default_selection_without_authored_appearance_keeps_embedded_content(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            fixture = ResolverFixture(Path(temporary))
            runner = FixtureBatchRunner(
                {ENTITY: selective_entity_document(default="None")}
            )

            states = fixture.resolver(runner).resolve_states(
                {"state": [ENTITY]},
                state_appearance_selections={"state": {ENTITY: ["default"]}},
            )

            self.assertEqual((ENTITY, COMMON_MESH), states.state_resources["state"])
            self.assertEqual({}, states.unmatched_appearance_selections["state"])

    def test_shared_app_selection_does_not_leak_between_states(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            fixture = ResolverFixture(Path(temporary))
            entity_document = selective_entity_document()
            appearances = entity_document["Data"]["RootChunk"]["appearances"]
            appearances[0]["appearanceResource"] = depot(APPEARANCE)
            appearances[1]["appearanceResource"] = depot(APPEARANCE)
            runner = FixtureBatchRunner(
                {
                    ENTITY: entity_document,
                    APPEARANCE: selective_appearance_document(
                        ("red_internal", RED_MESH),
                        ("blue_internal", BLUE_MESH),
                    ),
                }
            )

            states = fixture.resolver(runner).resolve_states(
                {"blue-state": [ENTITY], "red-state": [ENTITY]},
                state_appearance_selections={
                    "blue-state": {ENTITY: ["blue_root"]},
                    "red-state": {ENTITY: ["red_root"]},
                },
            )

            self.assertIn(BLUE_MESH, states.state_resources["blue-state"])
            self.assertNotIn(RED_MESH, states.state_resources["blue-state"])
            self.assertIn(RED_MESH, states.state_resources["red-state"])
            self.assertNotIn(BLUE_MESH, states.state_resources["red-state"])
            self.assertEqual((BLUE_MESH, RED_MESH), states.closure.graph[APPEARANCE])

    def test_state_closures_are_deterministic_and_keep_leaf_resources(self) -> None:
        graph = {
            ENTITY.upper(): [APPEARANCE, APPEARANCE.upper()],
            APPEARANCE: [MESH],
            MESH: [],
        }

        closures = compute_state_closures(
            graph,
            {
                "state-b": [MESH],
                "state-a": [ENTITY],
            },
        )

        self.assertEqual(["state-a", "state-b"], list(closures))
        self.assertEqual((APPEARANCE, ENTITY, MESH), closures["state-a"])
        self.assertEqual((MESH,), closures["state-b"])

    def test_extracts_nested_typed_depot_paths_and_rejects_unsafe_paths(self) -> None:
        value = {
            "one": depot(ENTITY.upper().replace("\\", "/")),
            "two": [depot(APPEARANCE), depot(ENTITY)],
        }
        self.assertEqual((APPEARANCE, ENTITY), extract_depot_paths(value))
        with self.assertRaisesRegex(DependencyStagingError, "Unsafe"):
            classify_resource(r"base\characters\..\fixture.ent")

    def test_missing_native_report_is_a_hard_error(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            fixture = ResolverFixture(Path(temporary))

            def missing_report(_invocation: BatchInvocation) -> int:
                return 7

            resolver = ArchiveDependencyResolver(
                cache_root=fixture.cache,
                ghostline_red=fixture.tool,
                schemas=fixture.schema,
                archives_root=fixture.archives,
                game_identity="fixture-game-v1",
                runner=missing_report,
            )
            with self.assertRaisesRegex(
                DependencyStagingError, "required CR2W batch report"
            ):
                resolver.resolve([ENTITY])


if __name__ == "__main__":
    unittest.main()
