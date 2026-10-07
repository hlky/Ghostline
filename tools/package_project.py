"""Build a named profile, verify its archive and ZIP, then optionally install it."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import uuid
import zipfile

import yaml

from artifact_io import atomic_write_json
from package_manifest import PackageError, PackageManifest, build_manifest, depot_path, path_component, sha256
from toolchain import resolve_tool


def run_tool(command: list[str], log: Path) -> str:
    result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace")
    log.write_text(result.stdout + result.stderr, encoding="utf-8")
    if result.returncode:
        raise PackageError(f"Command failed ({result.returncode}); see {log}")
    return result.stdout


def verify_payloads(expected: dict[str, Path], extracted: Path) -> None:
    actual = {depot_path(path.relative_to(extracted).as_posix()): path for path in extracted.rglob("*") if path.is_file()}
    if set(actual) != set(expected):
        raise PackageError(f"Archive path mismatch; missing={sorted(set(expected)-set(actual))}, unexpected={sorted(set(actual)-set(expected))}")
    for depot, source in expected.items():
        if source.stat().st_size != actual[depot].stat().st_size or sha256(source) != sha256(actual[depot]):
            raise PackageError(f"Extracted payload differs from its staged input: {depot}")


def verify_archive(candidate: Path, expected: dict[str, Path], wolvenkit: Path, build: Path) -> dict:
    listing = run_tool([str(wolvenkit), "archive", str(candidate), "-l", "-v", "Quiet"], build / "archive-list.txt")
    paths = [depot_path(line.strip()) for line in listing.splitlines() if line.strip()]
    if len(paths) != len(set(paths)) or set(paths) != set(expected):
        raise PackageError("Archive listing does not match the selected profile; see archive-list.txt")
    extracted = build / "verified-extracted"
    extracted.mkdir()
    run_tool([str(wolvenkit), "extract", str(candidate), "-o", str(extracted), "-v", "Quiet"], build / "extract.log")
    verify_payloads(expected, extracted)
    return {"archive_sha256": sha256(candidate), "payloads": {name: sha256(path) for name, path in sorted(expected.items())}}


def package_profile(manifest: PackageManifest, *, output: Path, wolvenkit: Path) -> dict:
    path_component(manifest.profile)
    path_component(manifest.archive_name)
    payloads = {depot_path(name): source for name, source in manifest.payloads.items()}
    loose_files = {depot_path(name): source for name, source in manifest.loose_files.items()}
    if len(payloads) != len(manifest.payloads) or len(loose_files) != len(manifest.loose_files):
        raise PackageError("Package has colliding path names")
    output.mkdir(parents=True, exist_ok=True)
    build = output / f"{manifest.profile}-{uuid.uuid4().hex[:12]}"
    archive_input = build / "archive"
    archive_input.mkdir(parents=True)
    expected = {}
    for depot, source in payloads.items():
        destination = archive_input / depot
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        expected[depot] = destination
    # Freeze loose inputs before packing, so later source edits cannot mix the set.
    loose_input = build / "loose"
    loose_input.mkdir()
    for depot, source in loose_files.items():
        destination = loose_input / depot_path(depot)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
    atomic_write_json(build / "selection.json", manifest.audit)
    run_tool([str(wolvenkit), "pack", str(archive_input), "-o", str(build)], build / "pack.log")
    candidate = build / "archive.archive"
    if not candidate.is_file():
        raise PackageError(f"Packer did not create {candidate}")
    evidence = verify_archive(candidate, expected, wolvenkit, build)
    install = build / "install-candidate"
    shutil.copytree(loose_input, install)
    archive_directory = install / "archive/pc/mod"
    archive_directory.mkdir(parents=True, exist_ok=True)
    staged_archive = archive_directory / f"{manifest.archive_name}.archive"
    shutil.copy2(candidate, staged_archive)
    registration = archive_directory / f"{manifest.archive_name}.archive.xl"
    registration.write_text(yaml.safe_dump(manifest.registration, sort_keys=False, allow_unicode=True), encoding="utf-8")
    staged = {path.relative_to(install).as_posix(): path for path in install.rglob("*") if path.is_file()}
    archive_zip = build / f"{manifest.archive_name}.zip.candidate"
    with zipfile.ZipFile(archive_zip, "w", compression=zipfile.ZIP_DEFLATED) as zipped:
        for name, source in sorted(staged.items()):
            zipped.write(source, name)
    extracted_zip = build / "verified-zip"
    with zipfile.ZipFile(archive_zip) as zipped:
        if set(zipped.namelist()) != set(staged) or len(zipped.namelist()) != len(staged):
            raise PackageError("ZIP entry mismatch")
        zipped.extractall(extracted_zip)
    verify_payloads({depot_path(name): source for name, source in staged.items()}, extracted_zip)
    install_hashes = {name: sha256(path) for name, path in sorted(staged.items())}
    install.rename(build / "install")
    install = build / "install"
    archive_zip.rename(build / f"{manifest.archive_name}.zip")
    archive_zip = build / f"{manifest.archive_name}.zip"
    staged_archive = install / "archive/pc/mod" / f"{manifest.archive_name}.archive"
    receipt = {**manifest.audit, **evidence, "build": str(build), "install_stage": str(install),
               "archive": str(staged_archive), "zip": str(archive_zip), "zip_sha256": sha256(archive_zip),
               "install_payloads": install_hashes,
               "verified": True, "runtime_tested": False}
    atomic_write_json(build / "verification.json", receipt)
    return receipt


def install_verified(receipt: dict, game: Path) -> None:
    """Publish verified install files with rollback if any replacement fails."""
    game = resolve_tool("game", game)
    stage = Path(receipt["install_stage"])
    expected = receipt["install_payloads"]
    if not receipt.get("verified") or any(sha256(stage / path) != digest for path, digest in expected.items()):
        raise PackageError("Install stage changed after verification")
    with tempfile.TemporaryDirectory(dir=game, prefix=".ghostline-install.") as directory:
        temporary = Path(directory)
        replaced: list[tuple[Path, Path | None]] = []
        try:
            for name in expected:
                relative = depot_path(name)
                target = game / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                backup = temporary / "backup" / relative if target.exists() else None
                if backup:
                    backup.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(target, backup)
                pending = temporary / "pending" / relative
                pending.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(stage / name, pending)
                pending.replace(target)
                replaced.append((target, backup))
                if sha256(target) != expected[name]:
                    raise PackageError(f"Installed file hash mismatch: {name}")
        except BaseException:
            for target, backup in reversed(replaced):
                if backup:
                    backup.replace(target)
                else:
                    target.unlink(missing_ok=True)
            raise


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", help="Project ID, directory, or .cpmodproj path")
    parser.add_argument("--profile", help="Project package profile; defaults to the project's default profile")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--wolvenkit", type=Path)
    parser.add_argument("--game", type=Path)
    parser.add_argument("--plan", action="store_true", help="Audit selection without running the packer")
    parser.add_argument("--keep-duplicate-meshes", action="store_true", help="Build without ArchiveXL mesh aliases for runtime comparison")
    parser.add_argument("--install", action="store_true")
    args = parser.parse_args()
    if not args.project and not args.profile:
        parser.error("Supply --project or --profile")
    manifest = build_manifest(args.profile, project=args.project, deduplicate=False if args.keep_duplicate_meshes else None)
    if args.plan:
        print(json.dumps(manifest.audit, indent=2))
        return 0
    output = args.output or Path(manifest.audit["project_root"]) / "generated/packages"
    receipt = package_profile(manifest, output=output.resolve(), wolvenkit=resolve_tool("wolvenkit", args.wolvenkit))
    if args.install:
        install_verified(receipt, resolve_tool("game", args.game))
    print(json.dumps(receipt, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
