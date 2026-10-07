"""Run the offline project gate; game, Blender, Wwise and GPU jobs stay explicit."""

from __future__ import annotations

import argparse
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--python-only", action="store_true", help="Omit the Rust voice gate")
    args = parser.parse_args()
    commands = [[sys.executable, "-B", "-m", "unittest", "discover", "-s", "tests", "-v"]]
    commands.append([sys.executable, "-m", "ruff", "check", "tools", "tests", "quests", "projects"])
    if not args.python_only:
        commands.append(["cargo", "test", "--manifest-path", "tools/ghostline-voice/Cargo.toml", "--locked", "--no-default-features"])
    for command in commands:
        try:
            result = subprocess.run(command, cwd=ROOT, check=False)
        except FileNotFoundError as error:
            print(f"Required check tool missing: {error}", file=sys.stderr)
            return 2
        if result.returncode:
            return result.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
