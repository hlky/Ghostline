"""Verify/package the optional manual CET helper, and install when requested."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import zipfile

PROJECT = Path(__file__).resolve().parents[1]
REPO = PROJECT.parents[2]
sys.path.insert(0, str(REPO / "tools"))
from artifact_io import atomic_write_json  # noqa: E402
from package_project import install_verified  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--install", action="store_true")
    parser.add_argument("--game", type=Path, default=Path("H:/Cyberpunk 2077"))
    args = parser.parse_args()
    source = PROJECT / "testing/cet/velvet_crash_test/init.lua"
    subprocess.run(["luac", "-p", str(source)], check=True)
    relative = "bin/x64/plugins/cyber_engine_tweaks/mods/velvet_crash_test/init.lua"
    work = PROJECT / "generated/testing"
    stage = work / "install"
    target = stage / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    archive = work / "VelvetCrash_CET_TestHelper.zip"
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as output:
        output.write(target, relative)
    with zipfile.ZipFile(archive) as output:
        if output.namelist() != [relative] or hashlib.sha256(output.read(relative)).hexdigest() != digest:
            raise ValueError("Test-helper ZIP differs from reviewed source")
    receipt = {"version": "0.1.0", "install_stage": str(stage), "install_payloads": {relative: digest},
               "zip": str(archive), "zip_sha256": hashlib.sha256(archive.read_bytes()).hexdigest(),
               "verified": True, "runtime_tested": False, "native_dependency": False}
    if args.install:
        install_verified(receipt, args.game)
        receipt.update(installed=True, game_root=str(args.game.resolve()))
    atomic_write_json(work / "verification.json", receipt)
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
