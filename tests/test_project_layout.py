"""Project ownership, build isolation, and explicit package dependencies."""
from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from project_layout import project_root, resource_project, project_sources
from package_manifest import PackageError, build_manifest, package_inputs
from quest_compiler import QuestArtifact, resource_paths
from quest_build import publish_build


def write_json(path: Path, document: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(document), encoding="utf-8")


class ProjectLayoutTests(unittest.TestCase):
    def test_resources_route_to_their_owners_without_changing_depot_names(self):
        cases = {
            r"mod\gq001\phases\gq001.questphase": "projects/ghostline",
            r"mod\gqt006\scenes\gqt006_goth_doggy_20s.scene": "projects/test-quests/gqt006",
            r"mod\ghostline\characters\goth_baddie\goth_baddie.ent": "projects/test-quests/gqt006",
            r"mod\ghostline\characters\cinder\cinder.ent": "projects/ghostline",
            r"mod\ghostline\characters\patch\patch.ent": "projects/shared/ghostline-runtime",
            r"mod\gq000\phases\gq000_delivery.questphase": "projects/shared/ghostline-runtime",
            r"mod\ghostline\quest_blocks\templates\braindance_analysis.questphase": "quests/templates",
        }
        for depot, relative in cases.items():
            with self.subTest(depot=depot):
                owner = ROOT / relative
                self.assertEqual(resource_project(depot), owner)
                raw, archive = resource_paths(depot)
                self.assertEqual(archive.relative_to(owner / "source/archive").as_posix(), depot.replace("\\", "/"))
                self.assertEqual(raw, owner / "source/raw" / (depot.replace("\\", "/") + ".json"))

    def test_projects_are_openable_and_only_own_their_declared_depots(self):
        for project_id in ("ghostline", "ghostline-runtime", *(f"gqt{i:03}" for i in range(1, 8))):
            project = project_root(project_id)
            with self.subTest(project=project_id):
                descriptors = list(project.glob("*.cpmodproj"))
                self.assertEqual(len(descriptors), 1)
                self.assertEqual(project_root(descriptors[0]), project)
                self.assertTrue((project / "source/resources").is_dir())
                for binary in (project / "source/archive").rglob("*"):
                    if binary.is_file():
                        self.assertEqual(resource_project(binary.relative_to(project / "source/archive").as_posix()), project)
        self.assertFalse((ROOT / "source").exists())

    def test_test_packages_activate_only_their_own_quest(self):
        for name in (f"gqt{i:03}" for i in range(1, 8)):
            with self.subTest(project=name):
                manifest = build_manifest(project=name)
                self.assertEqual(manifest.audit["active_quests"], [name])
                self.assertEqual(len(manifest.registration["quest"]["phases"]), 1)
                self.assertFalse(any(path.startswith("mod/gqt") and path.split("/")[1] != name for path in manifest.payloads))
                self.assertNotIn(str(ROOT / "projects/ghostline"), manifest.audit["source_projects"])
                if name in {"gqt001", "gqt002"}:
                    self.assertIn(f"mod\\{name}\\world\\{name}_custom_devices.devices", manifest.registration["resource"]["patch"])

    def test_story_development_excludes_test_assets_and_activation(self):
        manifest = build_manifest("development", project="ghostline")
        self.assertEqual(manifest.audit["active_quests"], ["gq001", "gq002"])
        self.assertFalse(any(path.startswith("mod/gqt") for path in manifest.payloads))
        self.assertFalse(any("/gqt" in path for path in manifest.loose_files))

    def test_default_publication_and_preview_stay_in_the_owning_project(self):
        project = project_root("gqt007")
        with tempfile.TemporaryDirectory() as directory:
            preview = Path(directory)
            raw, archive = resource_paths(r"mod\gqt007\migration_probe.questphase")
            item = QuestArtifact(raw, archive, {"Header": {"ArchiveFileName": str(archive)}, "Data": {"value": "probe"}})
            output = publish_build([item], namespace="gqt007", output_root=preview)
            self.assertEqual(output, [(preview / "source/raw/mod/gqt007/migration_probe.questphase.json", preview / "source/archive/mod/gqt007/migration_probe.questphase")])
            self.assertFalse(raw.exists())
            self.assertTrue((preview / "generated/quest-builds/gqt007/outputs.json").is_file())
            with self.assertRaisesRegex(ValueError, "source tree"):
                publish_build([item], namespace="gqt007", output_root=project / "source/raw/preview")


class ProjectDependencyTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.owner = self.root / "quest"
        self.shared = self.root / "shared"
        self.sibling = self.root / "unrelated"
        for path in (self.owner, self.shared, self.sibling):
            write_json(path / "project.json", {"schema_version": 1, "id": path.name, "dependencies": []})
        write_json(self.owner / "project.json", {"schema_version": 1, "id": "quest", "dependencies": ["../shared"], "default_profile": "quest"})
        write_json(self.owner / "packaging/profiles.json", {"schema_version": 1, "profiles": {"quest": {
            "archive_name": "Fixture", "active_quests": ["fixture"], "tweaks": [], "deduplicate_meshes": False,
        }}})
        registry = self.owner / "source/resources/Fixture.archive.xl"
        registry.parent.mkdir(parents=True)
        registry.write_text(yaml.safe_dump({"quest": {"phases": [{"path": "mod/fixture/root.questphase", "parent": "base/quest/cyberpunk2077.quest"}]}}))
        # These opaque payloads have no CR2W imports; registration supplies the
        # dependency edge, so this test exercises source scope rather than codecs.
        for project, depot in ((self.owner, "mod/fixture/root.questphase"), (self.shared, "mod/shared/asset.wem"), (self.sibling, "mod/fixture/unrelated.wem")):
            path = project / "source/archive" / depot
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(b"fixture")

    def test_dependency_registration_is_composed_and_siblings_are_not_inventoried(self):
        registry = self.shared / "source/resources/Shared.archive.xl"
        registry.parent.mkdir(parents=True)
        registry.write_text(yaml.safe_dump({"resource": {"patch": {"mod/shared/asset.wem": ["base/shared/asset.wem"]}}}))
        # Include the shared namespace as explicit support for this fixture.
        config_path = self.owner / "packaging/profiles.json"
        config = json.loads(config_path.read_text())
        config["profiles"]["quest"]["support_quests"] = ["shared"]
        write_json(config_path, config)
        manifest = build_manifest(root=self.owner)
        self.assertEqual(set(manifest.payloads), {"mod/fixture/root.questphase", "mod/shared/asset.wem"})
        self.assertEqual(manifest.audit["source_projects"], [str(self.shared), str(self.owner)])
        self.assertIn("mod/shared/asset.wem", manifest.registration["resource"]["patch"])

    def test_undeclared_sibling_cannot_satisfy_a_dependency(self):
        registry = self.owner / "source/resources/Fixture.archive.xl"
        value = yaml.safe_load(registry.read_text())
        value["journal"] = ["mod/fixture/unrelated.wem"]
        registry.write_text(yaml.safe_dump(value))
        with self.assertRaisesRegex(PackageError, "Missing owned depot dependency"):
            build_manifest(root=self.owner)

    def test_duplicate_depot_owners_and_dependency_cycles_fail(self):
        path = self.shared / "source/archive/mod/fixture/root.questphase"
        path.parent.mkdir(parents=True)
        path.write_bytes(b"fixture")
        with self.assertRaisesRegex(PackageError, "Multiple owners"):
            package_inputs(self.owner)
        write_json(self.shared / "project.json", {"schema_version": 1, "id": "shared", "dependencies": ["../quest"]})
        with self.assertRaisesRegex(ValueError, "cycle"):
            project_sources(self.owner)


if __name__ == "__main__":
    unittest.main()
