# Automated Testing

Run tests from the repository root. The full Python gate is:

```powershell
py -B -m unittest discover -s tests -v
```

Quest READMEs list the focused test modules for their generators and runtime
resources:

- [`gq000`](../../quests/story/ghostline/gq000/README.md)
- [`gq001`](../../quests/story/ghostline/gq001/README.md)
- [`gq002`](../../quests/story/ghostline/gq002/README.md)
- [`gq003`](../../quests/story/ghostline/gq003/README.md)

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
