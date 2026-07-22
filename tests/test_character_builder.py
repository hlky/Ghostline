from __future__ import annotations

import copy
import importlib.util
import json
import struct
import sys
import tempfile
import threading
import unittest
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

SPEC = importlib.util.spec_from_file_location("character_builder", TOOLS / "character_builder.py")
assert SPEC is not None
character_builder = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules["character_builder"] = character_builder
SPEC.loader.exec_module(character_builder)

UI_SPEC = importlib.util.spec_from_file_location("character_ui", TOOLS / "character_ui.py")
assert UI_SPEC is not None
character_ui = importlib.util.module_from_spec(UI_SPEC)
assert UI_SPEC.loader is not None
sys.modules["character_ui"] = character_ui
UI_SPEC.loader.exec_module(character_ui)


class CharacterBuilderTests(unittest.TestCase):
    manifest_path = ROOT / "source/characters/patch.character.json"

    def setUp(self) -> None:
        self.manifest = character_builder.load_manifest(self.manifest_path)
        self.catalog = character_builder.load_catalog(self.manifest)

    def test_patch_manifest_and_catalog_validate(self) -> None:
        report = character_builder.validate_manifest(self.manifest, self.catalog)
        self.assertTrue(report.ok, report.errors)
        self.assertEqual(report.details["selections"], 5)
        self.assertEqual(report.details["indexed_overrides"], 2)
        self.assertEqual(len(report.warnings), 7)

    def test_entity_default_uses_the_exposed_root_appearance_name(self) -> None:
        entity, _, _, _, _ = character_builder.generate_documents(
            self.manifest, self.catalog
        )
        root = entity["Data"]["RootChunk"]
        mapping = character_builder.appearance_data(entity)[0]

        self.assertEqual(
            character_builder.typed_value(root["defaultAppearance"]),
            self.manifest["entity"]["root_appearance"],
        )
        self.assertEqual(
            character_builder.typed_value(mapping["name"]),
            self.manifest["entity"]["root_appearance"],
        )
        self.assertEqual(
            character_builder.typed_value(mapping["appearanceName"]),
            self.manifest["entity"]["appearance_name"],
        )

    def test_designed_patch_matches_the_applied_shipping_sources(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            report = character_builder.generate(self.manifest_path, output)
            comparison = character_builder.compare_generated(self.manifest_path, output)

        self.assertTrue(report["validation"]["ok"])
        self.assertEqual(report["validation"]["details"]["app_components"], 47)
        self.assertTrue(comparison["equivalent"], comparison["files"])

    def test_original_patch_selection_remains_semantically_equivalent(self) -> None:
        baseline = copy.deepcopy(self.manifest)
        baseline.pop("_manifest_path", None)
        baseline["appearance"]["selections"]["hair"] = "patch_dual_braids"
        baseline["appearance"]["indexed_overrides"] = {}
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest_path = root / "baseline.character.json"
            manifest_path.write_text(json.dumps(baseline, indent=2) + "\n", encoding="utf-8")
            output = root / "output"
            report = character_builder.generate(manifest_path, output)
            generated_app = character_builder.output_path(
                output, baseline["outputs"]["appearance_raw"]
            )
            original_template = character_builder.repo_path(
                baseline["templates"]["appearance"]
            )
            generated_semantic = character_builder.semantic_value(generated_app)
            template_semantic = character_builder.semantic_value(original_template)

        self.assertTrue(report["validation"]["ok"])
        self.assertEqual(generated_semantic, template_semantic)

    def test_catalog_none_disables_both_component_copies(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["appearance"]["selections"]["hair"] = "none"
        _, app, _, _, _ = character_builder.generate_documents(manifest, self.catalog)
        appearance = character_builder.appearance_data(app)[0]
        expected = {
            "hh_048_ma__dual_braids8777",
            "hair_dangle",
            "hh_048_ma__dual_braids_shadow_npc",
        }
        for components in character_builder.component_sets(appearance):
            selected = {character_builder.component_name(item): item for item in components}
            self.assertEqual({selected[name]["isEnabled"] for name in expected}, {0})

    def test_dread_undercut_rebuilds_the_complete_hair_bundle(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["appearance"]["selections"]["hair"] = "patch_dread_undercut"
        _, app, _, _, warnings = character_builder.generate_documents(manifest, self.catalog)
        appearance = character_builder.appearance_data(app)[0]
        mappings = character_builder.components_by_name(appearance)
        self.assertEqual(len(mappings), 2)

        primary_name = "hh_146_ma__dread_undercut7563"
        shadow_name = "hh_146_ma__dread_undercut_shadow_npc"
        primary_path = (
            r"base\characters\common\hair\hh_146_ma__dread_undercut"
            r"\hh_146_ma__dread_undercut.mesh"
        )
        graph_path = (
            r"base\characters\common\hair\hh_146_ma__dread_undercut"
            r"\hh_146_ma__dread_undercut.animgraph"
        )
        rig_path = (
            r"base\characters\common\hair\hh_146_ma__dread_undercut"
            r"\hh_146_ma__dread_undercut_dangle_skeleton.rig"
        )
        shadow_path = (
            r"base\characters\common\hair\shadow_meshes"
            r"\hh_146_ma__dread_undercut_shadow_npc.mesh"
        )
        for mapping in mappings:
            primary = mapping[primary_name]
            dangle = mapping["hair_dangle"]
            shadow = mapping[shadow_name]
            self.assertEqual(primary["$type"], "entGarmentSkinnedMeshComponent")
            self.assertEqual(primary["mesh"]["DepotPath"]["$value"], primary_path)
            self.assertEqual(primary["meshAppearance"]["$value"], "black_carbon")
            self.assertEqual(dangle["graph"]["DepotPath"]["$value"], graph_path)
            self.assertEqual(dangle["rig"]["DepotPath"]["$value"], rig_path)
            self.assertEqual(shadow["mesh"]["DepotPath"]["$value"], shadow_path)

        normal_primary = mappings[0][primary_name]
        compiled_primary = mappings[1][primary_name]
        normal_dangle = mappings[0]["hair_dangle"]
        compiled_dangle = mappings[1]["hair_dangle"]
        self.assertEqual(
            normal_primary["parentTransform"]["HandleRefId"],
            compiled_primary["parentTransform"]["HandleId"],
        )
        self.assertEqual(
            normal_dangle["parentTransform"]["HandleRefId"],
            compiled_dangle["parentTransform"]["HandleId"],
        )
        self.assertEqual(compiled_primary["parentTransform"]["Data"]["$type"], "entHardTransformBinding")
        self.assertEqual(compiled_dangle["parentTransform"]["Data"]["$type"], "entHardTransformBinding")
        self.assertEqual(
            normal_primary["skinning"]["HandleRefId"],
            compiled_primary["skinning"]["HandleId"],
        )
        self.assertEqual(compiled_primary["skinning"]["Data"]["bindName"]["$value"], "Component")

        source_app = character_builder.read_json(
            character_builder.repo_path(manifest["templates"]["appearance"])
        )
        source_ids = character_builder.handle_ids(source_app)
        generated_ids = character_builder.handle_ids(app)
        added_ids = generated_ids - source_ids
        self.assertEqual(len(added_ids), 2)
        self.assertEqual(len(generated_ids), len(source_ids) + 2)
        self.assertEqual(sorted(generated_ids), list(range(len(generated_ids))))
        self.assertTrue(any("rewires" in item for item in warnings))

    def test_indexed_clothing_overrides_update_both_component_copies(self) -> None:
        cases = (
            (
                "inner_torso",
                r"base\characters\garment\player_equipment\torso\t1_999_test\t1_999_pma_test.mesh",
                "fabric_blue",
                "t1_004_pma_tshirt__longsleeve5383",
            ),
            (
                "legs",
                r"base\characters\garment\player_equipment\legs\l1_999_test\l1_999_pma_test.mesh",
                "denim_black",
                "l1_034_pma_pants__scavenger6036",
            ),
            (
                "feet",
                r"base\characters\garment\player_equipment\feet\s1_999_test\s1_999_pma_test.mesh",
                "black_red",
                "s1_053_pma_boot__military3700",
            ),
        )
        for category, depot_path, mesh_appearance, component_name in cases:
            with self.subTest(category=category):
                manifest = copy.deepcopy(self.manifest)
                manifest["appearance"]["indexed_overrides"] = {
                    category: {
                        "depot_path": depot_path,
                        "mesh_appearance": mesh_appearance,
                    }
                }
                entity, app, _, _, warnings = character_builder.generate_documents(
                    manifest, self.catalog
                )
                appearance = character_builder.appearance_data(app)[0]
                component_copies = character_builder.component_sets(appearance)
                self.assertEqual(len(component_copies), 2)
                for components in component_copies:
                    selected = {
                        character_builder.component_name(item): item for item in components
                    }
                    component = selected[component_name]
                    self.assertEqual(component["mesh"]["DepotPath"]["$value"], depot_path)
                    self.assertEqual(
                        character_builder.typed_value(component["meshAppearance"]),
                        mesh_appearance,
                    )
                    self.assertEqual(component["isEnabled"], 1)
                report = character_builder.validate_generated(manifest, entity, app)
                self.assertTrue(report.ok, report.errors)
                self.assertTrue(any("companion remains provisional" in item for item in warnings))

    def test_indexed_override_supports_renamed_appearance(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["entity"]["appearance_name"] = "custom"
        manifest["appearance"]["name"] = "custom"
        manifest["appearance"]["indexed_overrides"] = {
            "feet": {
                "depot_path": (
                    r"base\characters\garment\player_equipment\feet\test"
                    r"\s1_test_pma.mesh"
                ),
                "mesh_appearance": "black_red",
            }
        }

        entity, app, _, _, _ = character_builder.generate_documents(manifest, self.catalog)
        self.assertEqual(
            character_builder.typed_value(character_builder.appearance_data(app)[0]["name"]),
            "custom",
        )
        self.assertTrue(character_builder.validate_generated(manifest, entity, app).ok)

    def test_indexed_override_requires_both_typed_component_copies(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["appearance"]["selections"]["hair"] = "patch_dual_braids"
        manifest["appearance"]["indexed_overrides"] = {
            "feet": {
                "depot_path": (
                    r"base\characters\garment\player_equipment\feet\test"
                    r"\s1_test_pma.mesh"
                ),
                "mesh_appearance": "black_red",
            }
        }
        app = character_builder.read_json(
            character_builder.repo_path(manifest["templates"]["appearance"])
        )
        appearance = character_builder.appearance_data(app)[0]
        appearance.pop("compiledData")
        character_builder.apply_catalog_selections(app, manifest, self.catalog)
        with self.assertRaisesRegex(character_builder.CharacterBuildError, "both components"):
            character_builder.apply_indexed_overrides(app, manifest, self.catalog)

        entity, generated_app, _, _, _ = character_builder.generate_documents(
            manifest, self.catalog
        )
        generated_appearance = character_builder.appearance_data(generated_app)[0]
        generated_appearance.pop("compiledData")
        report = character_builder.validate_generated(manifest, entity, generated_app)
        self.assertFalse(report.ok)
        self.assertTrue(any("both components" in error for error in report.errors))

    def test_indexed_override_rejects_malformed_cr2w_field_wrappers(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["appearance"]["indexed_overrides"] = {
            "feet": {
                "depot_path": (
                    r"base\characters\garment\player_equipment\feet\test"
                    r"\s1_test_pma.mesh"
                ),
                "mesh_appearance": "black_red",
            }
        }
        app = character_builder.read_json(
            character_builder.repo_path(manifest["templates"]["appearance"])
        )
        appearance = character_builder.appearance_data(app)[0]
        first_copy = character_builder.components_by_name(appearance)[0]
        first_copy["s1_053_pma_boot__military3700"]["meshAppearance"] = "black_red"
        character_builder.apply_catalog_selections(app, manifest, self.catalog)
        with self.assertRaisesRegex(character_builder.CharacterBuildError, "typed CName"):
            character_builder.apply_indexed_overrides(app, manifest, self.catalog)

        entity, generated_app, _, _, _ = character_builder.generate_documents(
            manifest, self.catalog
        )
        generated = character_builder.components_by_name(
            character_builder.appearance_data(generated_app)[0]
        )[0]["s1_053_pma_boot__military3700"]
        generated["mesh"]["DepotPath"]["$type"] = "CName"
        report = character_builder.validate_generated(manifest, entity, generated_app)
        self.assertTrue(any("malformed ResourcePath" in error for error in report.errors))

    def test_indexed_override_rejects_wrong_frame_anchor_and_client_fields(self) -> None:
        base = copy.deepcopy(self.manifest)
        base["appearance"]["indexed_overrides"] = {
            "feet": {
                "depot_path": r"base\characters\garment\player_equipment\feet\test\s1_test_pwa.mesh",
                "mesh_appearance": "default",
            }
        }
        report = character_builder.validate_manifest(base, self.catalog)
        self.assertFalse(report.ok)
        self.assertTrue(any("pma body frame" in error for error in report.errors))

        parent_token_only = copy.deepcopy(self.manifest)
        parent_token_only["appearance"]["indexed_overrides"] = {
            "inner_torso": {
                "depot_path": (
                    r"base\characters\garment\player_equipment\torso"
                    r"\t0_005_pma_body__t_bug\t0_005_pwa_body__t_bug.mesh"
                ),
                "mesh_appearance": "default",
            }
        }
        report = character_builder.validate_manifest(parent_token_only, self.catalog)
        self.assertTrue(any("pma body frame" in error for error in report.errors))

        wrong_anchor = copy.deepcopy(self.manifest)
        wrong_anchor["appearance"]["selections"]["feet"] = "none"
        wrong_anchor["appearance"]["indexed_overrides"] = {
            "feet": {
                "depot_path": r"base\characters\garment\player_equipment\feet\test\s1_test_pma.mesh",
                "mesh_appearance": "default",
            }
        }
        report = character_builder.validate_manifest(wrong_anchor, self.catalog)
        self.assertTrue(any("curated anchor" in error for error in report.errors))

        extra_field = copy.deepcopy(self.manifest)
        extra_field["appearance"]["indexed_overrides"] = {
            "feet": {
                "depot_path": r"base\characters\garment\player_equipment\feet\test\s1_test_pma.mesh",
                "mesh_appearance": "default",
                "component": "untrusted",
            }
        }
        report = character_builder.validate_manifest(extra_field, self.catalog)
        self.assertTrue(any("unsupported fields" in error for error in report.errors))

        non_boolean_requirement = copy.deepcopy(self.manifest)
        non_boolean_requirement["requirements"]["phantom_liberty"] = "false"
        non_boolean_requirement["appearance"]["indexed_overrides"] = {
            "feet": {
                "depot_path": (
                    r"ep1\characters\garment\player_equipment\feet\test"
                    r"\s1_test_pma.mesh"
                ),
                "mesh_appearance": "default",
            }
        }
        report = character_builder.validate_manifest(non_boolean_requirement, self.catalog)
        self.assertTrue(any("JSON boolean" in error for error in report.errors))
        self.assertTrue(any("without declaring Phantom Liberty" in error for error in report.errors))

        repeated_separator = copy.deepcopy(self.manifest)
        repeated_separator["appearance"]["indexed_overrides"] = {
            "feet": {
                "depot_path": (
                    "base\\\\characters\\garment\\player_equipment\\feet\\test"
                    "\\s1_test_pma.mesh"
                ),
                "mesh_appearance": "default",
            }
        }
        report = character_builder.validate_manifest(repeated_separator, self.catalog)
        self.assertTrue(any("normalized game depot path" in error for error in report.errors))

    def test_generated_validation_rejects_new_numeric_resource(self) -> None:
        entity, app, _, _, _ = character_builder.generate_documents(self.manifest, self.catalog)
        appearance = character_builder.appearance_data(app)[0]
        component = appearance["components"][0]
        component["mesh"]["DepotPath"]["$value"] = "99999999999999999999"
        report = character_builder.validate_generated(self.manifest, entity, app)
        self.assertFalse(report.ok)
        self.assertTrue(any("new opaque numeric" in error for error in report.errors))

    def test_head_dry_run_accepts_explicit_shape_overrides(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            report = character_builder.head_build(
                self.manifest_path,
                Path(directory),
                {name: 21 for name in character_builder.SHAPE_NAMES},
                character_builder.DEFAULT_WOLVENKIT,
                character_builder.DEFAULT_BLENDER,
                character_builder.DEFAULT_GAME,
                True,
            )
        self.assertTrue(report["ok"], report["errors"])
        self.assertTrue(report["dry_run"])
        self.assertEqual(set(report["shapes"].values()), {21})

    def test_documented_shape_22_is_blocked_without_a_matching_target(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["head"]["shapes"] = {name: 22 for name in character_builder.SHAPE_NAMES}
        report = character_builder.validate_manifest(manifest, self.catalog)
        self.assertFalse(report.ok)
        self.assertTrue(any("option 22" in error for error in report.errors))

    def test_preview_manifest_uses_target_names_from_the_glb(self) -> None:
        document = {
            "asset": {"version": "2.0"},
            "meshes": [{"extras": {"targetNames": ["h011_eyes", "h205_ear"]}, "primitives": []}],
        }
        encoded = json.dumps(document, separators=(",", ":")).encode("utf-8")
        encoded += b" " * ((4 - len(encoded) % 4) % 4)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "head.morphtarget.glb"
            payload_length = 12 + 8 + len(encoded)
            path.write_bytes(
                struct.pack("<4sII", b"glTF", 2, payload_length)
                + struct.pack("<II", len(encoded), 0x4E4F534A)
                + encoded
            )
            preview = character_builder.build_preview_manifest(self.manifest, [path], root)

        self.assertEqual(preview["morph_mapping"]["eyes"]["targets"]["2"], "h011_eyes")
        self.assertEqual(preview["morph_mapping"]["ears"]["targets"]["21"], "h205_ear")
        self.assertNotIn("22", preview["morph_mapping"]["ears"]["targets"])

    def test_preview_route_rejects_path_traversal(self) -> None:
        with self.assertRaises(character_builder.CharacterBuildError):
            character_ui.preview_file_path("/preview/patch/../outside.glb")

    def test_ui_manifest_cannot_replace_server_owned_build_paths(self) -> None:
        posted = copy.deepcopy(self.manifest)
        posted["templates"]["entity"] = r"C:\untrusted\entity.json"
        posted["head"]["morphtarget_source"] = r"C:\untrusted\morphs"
        posted["head"]["blend_template"] = r"C:\untrusted\payload.blend"
        posted["head"]["morphtargets"] = [r"..\payload.morphtarget"]
        merged = character_ui.editable_manifest(posted)

        self.assertEqual(merged["templates"], self.manifest["templates"])
        self.assertEqual(
            merged["head"]["morphtarget_source"], self.manifest["head"]["morphtarget_source"]
        )
        self.assertEqual(merged["head"]["blend_template"], self.manifest["head"]["blend_template"])
        self.assertEqual(merged["head"]["morphtargets"], self.manifest["head"]["morphtargets"])

    def test_ui_manifest_retains_only_canonical_indexed_override_fields(self) -> None:
        posted = copy.deepcopy(self.manifest)
        posted["appearance"]["indexed_overrides"] = {
            "feet": {
                "depot_path": r"base\characters\garment\player_equipment\feet\test\s1_test_pma.mesh",
                "mesh_appearance": "default",
                "component": "untrusted",
                "source_archive": r"C:\untrusted.archive",
            },
            "head": {
                "depot_path": r"base\characters\garment\player_equipment\head\test.mesh",
                "mesh_appearance": "default",
            },
        }
        merged = character_ui.editable_manifest(posted)

        self.assertEqual(
            merged["appearance"]["indexed_overrides"],
            {
                "feet": {
                    "depot_path": r"base\characters\garment\player_equipment\feet\test\s1_test_pma.mesh",
                    "mesh_appearance": "default",
                }
            },
        )

    def test_ui_only_accepts_loopback_hosts(self) -> None:
        self.assertTrue(character_ui.is_loopback_host("127.0.0.1"))
        self.assertTrue(character_ui.is_loopback_host("::1"))
        self.assertTrue(character_ui.is_loopback_host("localhost"))
        self.assertFalse(character_ui.is_loopback_host("0.0.0.0"))
        self.assertFalse(character_ui.is_loopback_host("192.168.1.20"))

    def test_morphtarget_names_map_to_import_mesh_names(self) -> None:
        self.assertEqual(
            character_builder.mesh_name_for_morphtarget("hb_000_pma__morphs_logan.morphtarget"),
            "hb_000_pma_c__basehead_logan.mesh",
        )

    def test_local_ui_bootstrap_and_validation_api(self) -> None:
        server = ThreadingHTTPServer(("127.0.0.1", 0), character_ui.CharacterUIHandler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            base = f"http://127.0.0.1:{server.server_port}"
            with urllib.request.urlopen(f"{base}/api/bootstrap", timeout=5) as response:
                bootstrap = json.load(response)
            request = urllib.request.Request(
                f"{base}/api/validate",
                data=json.dumps({"manifest": bootstrap["manifest"]}).encode("utf-8"),
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with urllib.request.urlopen(request, timeout=5) as response:
                validation = json.load(response)
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=5)

        self.assertTrue(bootstrap["validation"]["ok"])
        self.assertEqual(len(bootstrap["catalog"]["categories"]), 5)
        self.assertIn("asset_index", bootstrap)
        self.assertTrue(validation["ok"])

    def test_local_ui_serves_allowlisted_preview_and_searches_generated_index(self) -> None:
        original_preview_root = character_ui.PREVIEW_ROOT
        original_index_path = character_ui.ASSET_INDEX_PATH
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            character_ui.PREVIEW_ROOT = root / "characters"
            character_ui.ASSET_INDEX_PATH = root / "assets.json"
            preview = character_ui.PREVIEW_ROOT / "patch" / "preview" / "sample.glb"
            preview.parent.mkdir(parents=True)
            preview.write_bytes(b"glTF-test")
            asset = character_ui.character_asset_index.classify_asset(
                r"base\characters\garment\player_equipment\feet\boots\boots_pma.mesh", "base"
            )
            character_ui.character_asset_index.write_json(
                character_ui.ASSET_INDEX_PATH,
                {"schema_version": 1, "summary": {"total": 1}, "assets": [asset]},
            )
            server = ThreadingHTTPServer(("127.0.0.1", 0), character_ui.CharacterUIHandler)
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            try:
                base = f"http://127.0.0.1:{server.server_port}"
                with urllib.request.urlopen(f"{base}/preview/patch/preview/sample.glb", timeout=5) as response:
                    payload = response.read()
                    content_type = response.headers.get_content_type()
                with urllib.request.urlopen(
                    f"{base}/api/assets?category=clothing&slot=feet&frame=pma&query=boots", timeout=5
                ) as response:
                    search = json.load(response)
            finally:
                server.shutdown()
                server.server_close()
                thread.join(timeout=5)
                character_ui.PREVIEW_ROOT = original_preview_root
                character_ui.ASSET_INDEX_PATH = original_index_path

        self.assertEqual(payload, b"glTF-test")
        self.assertEqual(content_type, "model/gltf-binary")
        self.assertEqual(len(search["assets"]), 1)

    def test_local_ui_assigns_canonical_indexed_clothing_override(self) -> None:
        original_preview_root = character_ui.PREVIEW_ROOT
        original_index_path = character_ui.ASSET_INDEX_PATH
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            character_ui.PREVIEW_ROOT = root / "characters"
            character_ui.ASSET_INDEX_PATH = root / "assets.json"
            depot_path = (
                r"base\characters\garment\player_equipment\feet\boots\s1_test_pma.mesh"
            )
            asset = character_ui.character_asset_index.classify_asset(depot_path, "base")
            character_ui.character_asset_index.write_json(
                character_ui.ASSET_INDEX_PATH,
                {"schema_version": 1, "summary": {"total": 1}, "assets": [asset]},
            )
            preview = {
                "asset": asset,
                "mesh_appearances": ["default", "black_red"],
                "warnings": [],
            }
            with mock.patch.object(
                character_ui.character_asset_index,
                "prepare_mesh_preview",
                return_value=preview,
            ):
                server = ThreadingHTTPServer(("127.0.0.1", 0), character_ui.CharacterUIHandler)
                thread = threading.Thread(target=server.serve_forever, daemon=True)
                thread.start()
                try:
                    request = urllib.request.Request(
                        f"http://127.0.0.1:{server.server_port}/api/assets/assign",
                        data=json.dumps(
                            {
                                "manifest": self.manifest,
                                "depot_path": depot_path,
                                "mesh_appearance": "black_red",
                            }
                        ).encode("utf-8"),
                        headers={"Content-Type": "application/json"},
                        method="POST",
                    )
                    with urllib.request.urlopen(request, timeout=5) as response:
                        assignment = json.load(response)
                finally:
                    server.shutdown()
                    server.server_close()
                    thread.join(timeout=5)
                    character_ui.PREVIEW_ROOT = original_preview_root
                    character_ui.ASSET_INDEX_PATH = original_index_path

        self.assertTrue(assignment["ok"])
        self.assertEqual(assignment["manifest_category"], "feet")
        self.assertEqual(assignment["anchor_option"], "patch_military_boots")
        self.assertEqual(
            assignment["override"],
            {"depot_path": depot_path, "mesh_appearance": "black_red"},
        )

    def test_local_ui_rejects_unindexed_override_before_validate_or_generate(self) -> None:
        original_preview_root = character_ui.PREVIEW_ROOT
        original_index_path = character_ui.ASSET_INDEX_PATH
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            character_ui.PREVIEW_ROOT = root / "characters"
            character_ui.ASSET_INDEX_PATH = root / "assets.json"
            character_ui.character_asset_index.write_json(
                character_ui.ASSET_INDEX_PATH,
                {"schema_version": 1, "summary": {"total": 0}, "assets": []},
            )
            posted = copy.deepcopy(self.manifest)
            posted["appearance"]["indexed_overrides"] = {
                "feet": {
                    "depot_path": (
                        r"base\characters\garment\player_equipment\feet\forged"
                        r"\s1_forged_pma.mesh"
                    ),
                    "mesh_appearance": "default",
                }
            }
            with mock.patch.object(character_ui.character_builder, "generate") as generate:
                server = ThreadingHTTPServer(("127.0.0.1", 0), character_ui.CharacterUIHandler)
                thread = threading.Thread(target=server.serve_forever, daemon=True)
                thread.start()
                try:
                    base = f"http://127.0.0.1:{server.server_port}"
                    for route in ("validate", "generate"):
                        request = urllib.request.Request(
                            f"{base}/api/{route}",
                            data=json.dumps({"manifest": posted}).encode("utf-8"),
                            headers={"Content-Type": "application/json"},
                            method="POST",
                        )
                        with self.subTest(route=route):
                            with self.assertRaises(urllib.error.HTTPError) as raised:
                                urllib.request.urlopen(request, timeout=5)
                            self.assertEqual(raised.exception.code, 400)
                            error = json.load(raised.exception)
                            self.assertIn("not present in the current index", error["error"])
                finally:
                    server.shutdown()
                    server.server_close()
                    thread.join(timeout=5)
                    character_ui.PREVIEW_ROOT = original_preview_root
                    character_ui.ASSET_INDEX_PATH = original_index_path

            generate.assert_not_called()


if __name__ == "__main__":
    unittest.main()
