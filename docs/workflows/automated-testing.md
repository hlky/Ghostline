# Automated Testing

Use Python 3.12 and the checked-in environment lock from the repository root:

```powershell
uv sync --locked --extra dev
uv run python -B tools/check_project.py
```

This gate runs the Python suite and model-free Rust voice tests. Use
`--python-only` for the Python layer. Install `--extra capture` for Windows
runtime capture, or `--extra research` for live reference regeneration.
Without uv, `py -m pip install -e ".[dev]"` installs declared version ranges;
the uv lock is the reproducible option. Game, Blender, Wwise and native CR2W
runtime checks are separate from this pure authoring gate.

Tool paths resolve explicit arguments, `GHOSTLINE_*` environment variables,
then `toolchain.local.json`, then discovery. Copy `toolchain.example.json` for
local configuration; never commit workstation-specific overrides.


Run tests from the repository root. The full Python gate is:

```powershell
py -B -m unittest discover -s tests -v
```

Quest READMEs list the focused test modules for their generators and runtime
resources:

- [`gq000`](../../projects/ghostline/quests/gq000/README.md)
- [`gq001`](../../projects/ghostline/quests/gq001/README.md)
- [`gq002`](../../projects/ghostline/quests/gq002/README.md)
- [`gq003`](../../projects/ghostline/quests/gq003/README.md)

## Native Tool

The pinned `ghostline-red` submodule has an independent Rust gate:

```powershell
cargo test --manifest-path .\tools\ghostline-red\Cargo.toml
```

## Test Ownership

- Generator changes require their focused unit tests and output validators.
- Scene changes require scene audit/validation plus localization checks where
  spoken lines or choices changed.
- World changes require dry-run/validation and focused NodeRef or placement
  inspection.
- Character changes require manifest validation, isolated generation, and
  comparison before promotion.
- Packaging changes require an isolated pack, archive listing, extraction, and
  payload comparison.

Passing automated tests does not establish in-game behavior. Record runtime
results separately in [runtime testing](runtime-testing.md).
