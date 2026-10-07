from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import package_manifest as package
from tests.test_package_project import ProfileFixture, cr2w


class PackageDependencyTests(unittest.TestCase):
    def test_authored_numeric_resource_paths_resolve_owned_payloads(self):
        path = "mod/ghostline/characters/patch/head/h0_000_pma_c__basehead.mesh"
        resource_hash = package.depot_hash(path)
        self.assertEqual(resource_hash, package.depot_hash(path.upper().replace("/", "\\")))
        with tempfile.TemporaryDirectory() as directory:
            raw = Path(directory) / "character.app.json"
            raw.write_text(json.dumps({"Data": {"nested": [
                {"DepotPath": {"$type": "ResourcePath", "$storage": "uint64", "$value": str(resource_hash)}},
                {"DepotPath": {"$type": "ResourcePath", "$storage": "uint64", "$value": "123"}},
                {"DepotPath": {"$type": "ResourcePath", "$storage": "uint64", "$value": "0"}},
                {"$type": "TweakDBID", "$storage": "uint64", "$value": "456"},
                {"DepotPath": {"$type": "ResourcePath", "$storage": "string", "$value": "mod/test/dependency.ent"}},
            ]}}), encoding="utf-8")
            unknown = set()
            dependencies = package.authored_dependencies(raw, {resource_hash: path}, unresolved=unknown)
            self.assertEqual(dependencies, {path, "mod/test/dependency.ent"})
            self.assertEqual(unknown, {123})

    def test_patch_entrypoint_includes_its_hashed_custom_meshes(self):
        manifest = package.build_manifest("gqt005", deduplicate=False)
        # These owned paths are numeric references inside Patch's embedded
        # appearance buffer, absent from the packed top-level string table.
        expected = {
            "mod/ghostline/characters/patch/head/h0_000_pma_c__basehead.mesh",
            "mod/ghostline/characters/patch/body/t0_000_pma_base__full.mesh",
            "mod/ghostline/characters/patch/body/a0_000_pma_base__nails_l.mesh",
        }
        self.assertTrue(expected.issubset(manifest.payloads))
        self.assertTrue(expected.issubset(manifest.audit["dependency_additions"]))
        self.assertIn("mod/ghostline/characters/patch/patch.app", manifest.audit["authored_dependency_sources"])
        self.assertIn(
            "mod/ghostline/characters/patch/body/textures/t0_000_pma_base__full/t0_000_ma__c_base_d03_naked.xbm",
            manifest.payloads,
        )
        self.assertIn("patch", manifest.audit["character_bundle_fallbacks"])

    def test_transitively_selected_mesh_retains_its_owner_bundle_and_follows_new_dependencies(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = ProfileFixture(Path(directory))
            owner = "mod/ghostline/characters/secondary"
            mesh, texture = f"{owner}/body.mesh", f"{owner}/textures/body.xbm"
            fixture.write("mod/gq001/phases/gq001.questphase", cr2w(mesh))
            fixture.write(mesh, cr2w())
            fixture.write(texture, cr2w("mod/shared/material.mi"))
            fixture.write("mod/shared/material.mi", cr2w())
            manifest = fixture.build()
            self.assertTrue({mesh, texture, "mod/shared/material.mi"}.issubset(manifest.payloads))
            fallback = manifest.audit["character_bundle_fallbacks"]["secondary"]
            self.assertEqual(fallback["meshes_without_raw"], [mesh])
            self.assertEqual(fallback["retained_file_count"], 2)

    def test_development_excludes_unfinished_quest_records_and_registration(self):
        manifest = package.build_manifest("development")
        self.assertNotIn("r6/tweaks/ghostline/gq003_black_lantern.yaml", manifest.loose_files)
        self.assertFalse(any("/gq003/" in path for path in package.resource_strings(manifest.registration)))
        self.assertFalse(any(path.startswith("mod/gq003/") for path in manifest.payloads))

    def test_current_profiles_close_authored_paths_and_custom_tweak_references(self):
        root = package.ROOT
        registry = {key for path in (root / "projects").glob("**/source/resources/r6/tweaks/ghostline/*.yaml")
                    for key in yaml.safe_load(path.read_text(encoding="utf-8"))}

        def values(document):
            if isinstance(document, str):
                yield document
            elif isinstance(document, dict):
                for child in document.values():
                    yield from values(child)
            elif isinstance(document, list):
                for child in document:
                    yield from values(child)

        for profile in ("story", "gqt005", "gqt006", "gqt007", "development"):
            with self.subTest(profile=profile):
                manifest = package.build_manifest(profile)
                inventory, raw_inventory, _, _ = package.package_inputs(Path(manifest.audit["project_root"]))
                known_hashes = package.inventory_hashes(inventory)
                available = set(manifest.payloads) | {
                    path for aliases in manifest.audit["mesh_aliases"].values() for path in aliases
                }
                self.assertFalse(manifest.audit["unresolved_numeric_resource_paths"])
                expected_bundles = {
                    "story": {"patch", "iris", "cinder"}, "gqt005": {"patch"},
                    "gqt006": {"goth_baddie"}, "gqt007": set(),
                    "development": {"patch", "iris", "cinder"},
                }
                self.assertEqual(set(manifest.audit["character_bundle_fallbacks"]), expected_bundles[profile])
                referenced_records = set()
                defined_records = set()
                for path in manifest.loose_files.values():
                    if path.suffix in (".yaml", ".yml"):
                        document = yaml.safe_load(path.read_text(encoding="utf-8"))
                        defined_records.update(document)
                        referenced_records.update(value for value in values(document) if value in registry)
                for depot in available:
                    raw = raw_inventory.get(depot)
                    if raw is None or not raw.is_file():
                        continue  # Binary-only coverage is explicitly separate.
                    references = package.authored_dependencies(raw, known_hashes)
                    missing = {
                        path for path in references if path.startswith(("mod/", "tutorial/"))
                        and path not in available and path not in manifest.audit["localized_lipsync_references"]
                    }
                    self.assertFalse(missing, f"{depot} needs {sorted(missing)}")
                    document = json.loads(raw.read_text(encoding="utf-8"))
                    referenced_records.update(value for value in values(document) if value in registry)
                self.assertFalse(referenced_records - defined_records)


if __name__ == "__main__":
    unittest.main()
