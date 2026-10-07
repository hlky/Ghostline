from __future__ import annotations

import contextlib
import io
import importlib.util
import json
from pathlib import Path
import struct
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import package_manifest as manifests
import package_project as packages


def cr2w(*references: str) -> bytes:
    strings = "\0".join(references).encode("utf-8") + b"\0"
    header = bytearray(160)
    header[:4] = b"CR2W"
    struct.pack_into("<II", header, 40, 160, len(strings))
    return bytes(header) + strings


class ProfileFixture:
    def __init__(self, root: Path):
        self.root = root
        self.config = json.loads(
            (manifests.ROOT / "packaging/profiles.json").read_text(encoding="utf-8")
        )
        from project_layout import project_root
        self.config = {"schema_version": 1, "profiles": {
            name: json.loads((project_root(route["project"]) / "packaging/profiles.json").read_text())["profiles"][name]
            for name, route in self.config["profiles"].items()
        }}
        self.resources = root / "source/resources"
        self.resources.mkdir(parents=True)
        self.quests = {
            quest
            for profile in self.config["profiles"].values()
            for quest in profile["active_quests"] + profile.get("support_quests", [])
        } | {"gq003"}
        self.document = {
            "quest": {"phases": []},
            "journal": [],
            "localization": {"onscreens": {"en-us": []}},
            "streaming": {"blocks": []},
        }
        for quest in sorted(self.quests):
            phase = f"mod/{quest}/phases/{quest}.questphase"
            self.write(phase, cr2w())
            self.document["quest"]["phases"].append(
                {"path": phase, "parent": "base/quest/cyberpunk2077.quest"}
            )
            for field, suffix in (
                ("journal", "journal"),
                ("streaming", "streamingblock"),
            ):
                path = f"mod/{quest}/{quest}.{suffix}"
                self.write(path, cr2w())
                target = self.document[field]
                (target["blocks"] if field == "streaming" else target).append(path)
            locale = f"mod/{quest}/localization/en-us/onscreens/{quest}.json"
            self.write(locale, cr2w())
            self.document["localization"]["onscreens"]["en-us"].append(locale)
        shared = "mod/ghostline/localization/en-us/onscreens/ghostline.json"
        self.write(shared, cr2w())
        self.document["localization"]["onscreens"]["en-us"].append(shared)
        for name in {"patch", "iris", "cinder", "goth_baddie"}:
            prefix = f"mod/ghostline/characters/{name}"
            self.write(f"{prefix}/{name}.ent", cr2w(f"{prefix}/{name}.app"))
            self.write(f"{prefix}/{name}.app", cr2w(f"{prefix}/body.mesh"))
            self.write(f"{prefix}/body.mesh", cr2w("base/characters/body.mi"))
            raw = self.root / "source/raw" / f"{prefix}/body.mesh.json"
            raw.parent.mkdir(parents=True, exist_ok=True)
            raw.write_text("{}", encoding="utf-8")
            self.write(f"{prefix}/unused.mesh", b"unused export")
        for name in {
            tweak
            for profile in self.config["profiles"].values()
            for tweak in profile.get("tweaks", [])
        }:
            path = self.resources / f"r6/tweaks/ghostline/{name}.yaml"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("Fixture.Record: {}\n", encoding="utf-8")
        self.write("tutorial/unused.mesh", b"tutorial")
        self.write("base/characters/unvalidated.mesh", b"base override")
        self.save()

    def write(self, depot: str, data: bytes) -> Path:
        path = self.root / "source/archive" / depot
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        return path

    def save(self) -> None:
        (self.root / "packaging").mkdir(exist_ok=True)
        (self.root / "packaging/profiles.json").write_text(
            json.dumps(self.config), encoding="utf-8"
        )
        (self.resources / "Ghostline.archive.xl").write_text(
            yaml.safe_dump(self.document), encoding="utf-8"
        )

    def build(self, name: str = "story", **kwargs):
        return manifests.build_manifest(name, root=self.root, **kwargs)


class ManifestTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.fixture = ProfileFixture(Path(self.temporary.name))

    def test_named_profiles_filter_registration_and_unused_assets(self):
        for name in ("story", "gqt005", "gqt006", "gqt007"):
            with self.subTest(profile=name):
                result = self.fixture.build(name)
                profile = self.fixture.config["profiles"][name]
                active = profile["active_quests"]
                owners = set(active + profile.get("support_quests", []))
                self.assertEqual(
                    {
                        phase["path"].split("/")[1]
                        for phase in result.registration["quest"]["phases"]
                    },
                    set(active),
                )
                for path in manifests.resource_strings(result.registration):
                    if path.startswith("mod/") and not path.startswith(
                        "mod/ghostline/"
                    ):
                        self.assertIn(path.split("/")[1], owners)
                for path in result.payloads:
                    self.assertFalse(path.startswith(("tutorial/", "base/characters/")))
                    self.assertFalse(path.endswith("unused.mesh"))
                    if path.startswith("mod/gq"):
                        self.assertIn(path.split("/")[1], owners)
                self.assertEqual(
                    {path.stem for path in result.loose_files.values()},
                    set(profile["tweaks"]),
                )

    def test_development_includes_tests_but_excludes_incomplete_story(self):
        result = self.fixture.build("development")
        self.assertIn("tutorial/unused.mesh", result.payloads)
        self.assertIn("mod/gqt001/phases/gqt001.questphase", result.payloads)
        self.assertFalse(any(path.startswith("mod/gq003/") for path in result.payloads))
        self.assertFalse(
            any(
                path.startswith("mod/gq003/")
                for path in manifests.resource_strings(result.registration)
            )
        )

    def test_duplicate_registration_cannot_mask_missing_active_quest(self):
        phases = self.fixture.document["quest"]["phases"]
        phases[:] = [phase for phase in phases if "/gq002/" not in phase["path"]]
        phases.append(
            next(phase.copy() for phase in phases if "/gq001/" in phase["path"])
        )
        self.fixture.save()
        with self.assertRaises(manifests.PackageError):
            self.fixture.build()

    def test_transitive_dependencies_and_missing_owned_paths(self):
        extra = "mod/shared/extra.app"
        leaf = "mod/shared/extra.mesh"
        self.fixture.write("mod/gq001/phases/gq001.questphase", cr2w(extra))
        self.fixture.write(extra, cr2w(leaf, "ep1/characters/external.mesh"))
        source = self.fixture.write(leaf, cr2w())
        result = self.fixture.build()
        self.assertEqual(
            set(result.audit["dependency_additions"]) & {extra, leaf}, {extra, leaf}
        )
        self.assertIn(
            "ep1/characters/external.mesh", result.audit["external_game_dependencies"]
        )
        source.unlink()
        with self.assertRaisesRegex(
            manifests.PackageError, "Missing owned depot dependency"
        ):
            self.fixture.build()

    def test_excluded_and_forbidden_dependencies_fail(self):
        cases = [
            (
                "development",
                "mod/gq001/phases/gq001.questphase",
                "mod/gq003/gq003.journal",
            ),
            ("gqt006", "mod/gqt006/phases/gqt006.questphase", "tutorial/unused.mesh"),
        ]
        for profile, phase, reference in cases:
            with self.subTest(profile=profile):
                self.fixture.write(phase, cr2w(reference))
                with self.assertRaises(manifests.PackageError):
                    self.fixture.build(profile)
                self.fixture.write(phase, cr2w())

    def test_raw_dependencies_extend_but_cannot_remove_packed_dependencies(self):
        phase = "mod/gq001/phases/gq001.questphase"
        packed = "mod/shared/packed.ent"
        authored = "mod/shared/authored.ent"
        self.fixture.write(phase, cr2w(packed))
        self.fixture.write(packed, cr2w())
        self.fixture.write(authored, cr2w())
        raw = self.fixture.root / "source/raw" / (phase + ".json")
        raw.parent.mkdir(parents=True)
        raw.write_text(json.dumps({"Data": {"reference": authored}}), encoding="utf-8")
        result = self.fixture.build()
        self.assertTrue({packed, authored} <= set(result.payloads))
        self.assertIn(phase, result.audit["authored_dependency_sources"])
        (self.fixture.root / "source/archive" / authored).unlink()
        with self.assertRaisesRegex(
            manifests.PackageError, "Missing owned depot dependency"
        ):
            self.fixture.build()

    def test_mesh_aliases_have_identical_bytes_and_closed_references(self):
        result = self.fixture.build()
        aliases = result.audit["mesh_aliases"]
        self.assertEqual(len(aliases), 1)
        aliased_paths = {path for paths in aliases.values() for path in paths}
        self.assertEqual(len(aliased_paths), 3)
        for canonical, paths in aliases.items():
            for path in paths:
                self.assertNotIn(path, result.payloads)
                self.assertEqual(
                    result.payloads[canonical].read_bytes(),
                    (self.fixture.root / "source/archive" / path).read_bytes(),
                )
        for source in result.payloads.values():
            for reference in manifests.cr2w_dependencies(source):
                if reference.startswith("mod/"):
                    self.assertIn(reference, set(result.payloads) | aliased_paths)
        plain = self.fixture.build(deduplicate=False)
        self.assertEqual(plain.audit["mesh_aliases"], {})
        self.assertTrue(aliased_paths <= set(plain.payloads))

    def test_alias_cannot_replace_different_existing_resource(self):
        mesh = (
            self.fixture.root
            / "source/archive/mod/ghostline/characters/patch/body.mesh"
        )
        canonical = f"mod/ghostline/shared/{manifests.sha256(mesh)}.mesh"
        self.fixture.write(canonical, b"different existing shared asset")
        self.fixture.write("mod/gq001/phases/gq001.questphase", cr2w(canonical))
        with self.assertRaises(manifests.PackageError):
            self.fixture.build()

    def test_localized_lipsync_soft_reference_requires_registered_map(self):
        soft = "mod/gq001/scenes/lipsync/en/dialogue.anims"
        concrete = "base/localization/en-us/lipsync/mod/gq001/scenes/dialogue.anims"
        lipmap = "mod/gq001/localization/en-us/gq001.lipmap"
        self.fixture.write("mod/gq001/phases/gq001.questphase", cr2w(soft))
        self.fixture.write(concrete, cr2w())
        self.fixture.write(lipmap, cr2w(concrete))
        with self.assertRaises(manifests.PackageError):
            self.fixture.build()
        self.fixture.document["localization"]["lipmaps"] = {"en-us": [lipmap]}
        self.fixture.save()
        result = self.fixture.build()
        self.assertEqual(result.audit["localized_lipsync_references"], {soft: concrete})
        self.assertIn(concrete, result.payloads)

    def test_unsafe_depot_paths_rejected(self):
        for path in (
            "../escape.mesh",
            "/absolute.mesh",
            "C:/escape.mesh",
            "mod//x.mesh",
            "mod/./x.mesh",
            "mod/../x.mesh",
            "mod/x:stream",
            "mod/x?.mesh",
            "mod/x\n.mesh",
        ):
            with self.subTest(path=path), self.assertRaises(manifests.PackageError):
                manifests.depot_path(path)
        self.assertEqual(
            manifests.depot_path("MOD\\Quest\\FILE.Mesh"), "mod/quest/file.mesh"
        )


class FakeWolvenKit:
    def __init__(self, fault: str | None = None):
        self.commands = []
        self.fault = fault
        self.inputs: dict[str, bytes] = {}

    def __call__(self, command, log):
        self.commands.append(command)
        log.write_text("fixture", encoding="utf-8")
        operation = command[1]
        if operation == "pack":
            if self.fault == "pack":
                raise manifests.PackageError("injected pack failure")
            source = Path(command[2])
            self.inputs = {
                path.relative_to(source).as_posix(): path.read_bytes()
                for path in source.rglob("*")
                if path.is_file()
            }
            (Path(command[command.index("-o") + 1]) / "archive.archive").write_bytes(
                b"fake archive"
            )
        elif operation == "archive":
            paths = list(self.inputs)
            if self.fault == "list_missing":
                paths.pop()
            elif self.fault == "list_extra":
                paths.append("mod/unexpected.mesh")
            elif self.fault == "list_duplicate":
                paths.append(paths[0])
            return "\n".join(path.replace("/", "\\") for path in paths)
        elif operation == "extract":
            target = Path(command[command.index("-o") + 1])
            files = dict(self.inputs)
            if self.fault == "extract_missing":
                files.pop(next(iter(files)))
            elif self.fault == "extract_extra":
                files["mod/unexpected.mesh"] = b"extra"
            elif self.fault == "extract_changed":
                name = next(iter(files))
                files[name] = bytes(byte ^ 1 for byte in files[name])
            for name, data in files.items():
                destination = target / name
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_bytes(data)
        else:
            raise AssertionError(command)
        return ""


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.source = self.root / "fixture.ent"
        self.source.write_bytes(cr2w())
        loose = self.root / "fixture.yaml"
        loose.write_text("Fixture: {}", encoding="utf-8")
        self.manifest = manifests.PackageManifest(
            "story",
            "Ghostline",
            {"mod/gq001/fixture.ent": self.source},
            {"r6/tweaks/ghostline/fixture.yaml": loose},
            {"quest": {"phases": []}},
            {"profile": "story", "project_root": str(self.root)},
        )
        self.wolvenkit = self.root / "custom toolkit/WolvenKit.CLI.exe"

    def run_package(self, runner):
        with patch.object(packages, "run_tool", runner):
            return packages.package_profile(
                self.manifest, output=self.root / "packages", wolvenkit=self.wolvenkit
            )

    def test_valid_archive_zip_and_explicit_tool_override(self):
        runner = FakeWolvenKit()
        receipt = self.run_package(runner)
        self.assertTrue(receipt["verified"])
        self.assertFalse(receipt["runtime_tested"])
        self.assertEqual(
            [command[1] for command in runner.commands], ["pack", "archive", "extract"]
        )
        self.assertTrue(
            all(command[0] == str(self.wolvenkit) for command in runner.commands)
        )
        with zipfile.ZipFile(receipt["zip"]) as archive:
            self.assertEqual(set(archive.namelist()), set(receipt["install_payloads"]))
            self.assertIn("archive/pc/mod/Ghostline.archive.xl", archive.namelist())
            self.assertIn("r6/tweaks/ghostline/fixture.yaml", archive.namelist())
        self.assertTrue((Path(receipt["build"]) / "verification.json").is_file())

    def test_failed_archive_checks_prevent_install_stage_and_zip(self):
        for fault in (
            "pack",
            "list_missing",
            "list_extra",
            "list_duplicate",
            "extract_missing",
            "extract_extra",
            "extract_changed",
        ):
            with self.subTest(fault=fault):
                with self.assertRaises(manifests.PackageError):
                    self.run_package(FakeWolvenKit(fault))
        output = self.root / "packages"
        self.assertFalse(list(output.rglob("install")))
        self.assertFalse(list(output.rglob("*.zip")))
        self.assertFalse(list(output.rglob("verification.json")))

    def test_failed_zip_verification_has_no_verification_receipt(self):
        verify = packages.verify_payloads

        def fail_zip(expected, extracted):
            if extracted.name == "verified-zip":
                raise manifests.PackageError("injected ZIP content mismatch")
            return verify(expected, extracted)

        with patch.object(packages, "verify_payloads", side_effect=fail_zip):
            with self.assertRaises(manifests.PackageError):
                self.run_package(FakeWolvenKit())
        self.assertFalse(list((self.root / "packages").rglob("verification.json")))
        self.assertFalse(list((self.root / "packages").rglob("install")))
        self.assertFalse(list((self.root / "packages").rglob("*.zip")))

    def test_unsafe_public_manifest_paths_fail_before_tool_execution(self):
        variants = [
            ("story", "Ghostline", {"../escape.ent": self.source}, {}),
            (
                "story",
                "Ghostline",
                {"mod/safe.ent": self.source},
                {"../escape.yaml": self.source},
            ),
            ("story", "../Ghostline", {"mod/safe.ent": self.source}, {}),
            ("../story", "Ghostline", {"mod/safe.ent": self.source}, {}),
        ]
        for profile, archive_name, payloads, loose in variants:
            with self.subTest(
                profile=profile, archive=archive_name, payloads=payloads, loose=loose
            ):
                self.manifest = manifests.PackageManifest(
                    profile, archive_name, payloads, loose, {}, {}
                )
                runner = FakeWolvenKit()
                with self.assertRaises(manifests.PackageError):
                    self.run_package(runner)
                self.assertEqual(runner.commands, [])

    def test_changed_verified_stage_prevents_install(self):
        receipt = self.run_package(FakeWolvenKit())
        stage = Path(receipt["install_stage"])
        (stage / next(iter(receipt["install_payloads"]))).write_bytes(b"tampered")
        game = self.root / "game"
        game.mkdir()
        with patch.object(packages, "resolve_tool", return_value=game):
            with self.assertRaises(manifests.PackageError):
                packages.install_verified(receipt, game)
        self.assertEqual(list(game.iterdir()), [])

    def test_cli_wolvenkit_override_reaches_shared_packager(self):
        with (
            patch.object(
                sys,
                "argv",
                [
                    "package_project.py",
                    "--profile",
                    "story",
                    "--wolvenkit",
                    str(self.wolvenkit),
                ],
            ),
            patch.object(packages, "build_manifest", return_value=self.manifest),
            patch.object(
                packages, "resolve_tool", return_value=self.wolvenkit
            ) as resolve,
            patch.object(
                packages, "package_profile", return_value={"verified": True}
            ) as package,
            contextlib.redirect_stdout(io.StringIO()),
        ):
            self.assertEqual(packages.main(), 0)
        resolve.assert_called_once_with("wolvenkit", self.wolvenkit)
        self.assertEqual(package.call_args.kwargs["wolvenkit"], self.wolvenkit)

    def test_standalone_wrapper_uses_same_profile_packager_and_override(self):
        path = (
            manifests.ROOT / "projects/test-quests/gqt006/implementation/package_standalone.py"
        )
        spec = importlib.util.spec_from_file_location(
            "package_standalone_fixture", path
        )
        standalone = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(standalone)
        with (
            patch.object(sys, "argv", [str(path), "--wolvenkit", str(self.wolvenkit)]),
            patch.object(
                standalone, "build_manifest", return_value=self.manifest
            ) as build,
            patch.object(
                standalone, "resolve_tool", return_value=self.wolvenkit
            ) as resolve,
            patch.object(
                standalone, "package_profile", return_value={"verified": True}
            ) as package,
            patch.object(standalone, "install_verified") as install,
            contextlib.redirect_stdout(io.StringIO()),
        ):
            self.assertEqual(standalone.main(), 0)
        build.assert_called_once_with("gqt006")
        resolve.assert_called_once_with("wolvenkit", self.wolvenkit)
        self.assertEqual(package.call_args.kwargs["wolvenkit"], self.wolvenkit)
        install.assert_not_called()


if __name__ == "__main__":
    unittest.main()
