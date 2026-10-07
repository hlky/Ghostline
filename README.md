# Ghostline

This repository contains the Ghostline quest-building tools, the connected
Cyberpunk 2077 story mod, and independent runtime test mods. The story quests
follow a covert broker collective uncovering Quiet Spine,
an identity-laundering network that treats memories, bodies, and civic
infrastructure as interchangeable parts.

## Quest Series

| Quest | Title | Status |
| --- | --- | --- |
| [`gq000`](projects/ghostline/quests/gq000/README.md) | Original prototype | Superseded story; reusable runtime baseline |
| [`gq001`](projects/ghostline/quests/gq001/README.md) | Ghostline | First canonical quest; extends and replaces `gq000` |
| [`gq002`](projects/ghostline/quests/gq002/README.md) | The Machine Stops | Canonical |
| [`gq003`](projects/ghostline/quests/gq003/README.md) | Black Lantern | Canonical preproduction |

The [series index](projects/ghostline/quests/README.md) owns story order, shared
cast, voice design, continuity, and the template for future quests. Each quest
README owns its build and focused test commands.

## Start Here

Clone the repository with its submodules, then work from the repository root:

```powershell
git submodule update --init --recursive
uv sync --locked --extra dev
uv run python -B tools/check_project.py
```

The normal development loop is:

1. Change the owning project's authoring inputs or CR2W-JSON under its
   `source/raw`. Shared compiler examples and templates live under `quests`.
2. Run the owning generator and focused tests documented by the relevant
   quest or authoring guide.
3. Validate generated raw resources before converting them to packed CR2W.
4. Build and verify a named release/test/development profile.
5. Stage the matching loose resources with the shared packager.
6. Install and record runtime evidence on a suitable save.

See the [development workflow](docs/workflows/development.md) for the common
commands and the [build/package guide](docs/workflows/build-and-package.md)
before producing an installable archive.

## Documentation

- [Documentation map](docs/README.md) — choose a guide by task.
- [Quest series](projects/ghostline/quests/README.md) — narrative and per-quest
  implementation ownership.
- [Automated testing](docs/workflows/automated-testing.md) — repository and
  focused test gates.
- [Runtime testing](docs/workflows/runtime-testing.md) — current candidates
  and dated in-game evidence.
- [Tool catalog](docs/reference/tool-catalog.md) — complete helper-command
  reference.
- [Agent guide](AGENTS.md) — source-of-truth and task-routing rules.

## Repository Layout

| Path | Ownership |
| --- | --- |
| `projects/ghostline` | Story WolvenKit project, series authoring, Iris/Cinder, source assets, and package profiles |
| `projects/test-quests/gqt###` | One WolvenKit project per test quest, with its manifest, implementation, source, and package profile |
| `projects/shared/ghostline-runtime` | Explicit shared dependency: Patch, common runtime assets, localization, and the GQ000 baseline |
| `projects/catalog.json` | Project IDs and depot ownership routing |
| `quests/examples`, `quests/templates` | Building-system examples, quest/journal templates, and neutral character catalogs/components |
| `braindance` | Performance specs, rig contracts, templates, and render presets |
| `<project>/source/raw` | Editable CR2W-JSON for that project's packed resources |
| `<project>/source/archive` | Packed/game-ready CR2W resources; never edit these binaries as text |
| `<project>/source/resources` | Project-owned ArchiveXL, TweakXL, REDscript, and configuration resources |
| `docs` | Cross-cutting workflows, authoring guides, references, and history |
| `reference` | Local serialized game references and generated selection indexes |
| `tools` | Generators, validators, explorers, and the pinned `ghostline-red` submodule |
| `<project>/generated`, `<project>/packed` | Ignored project build and staging outputs |
| `generated`, `converted`, `packed`, `.tmp` | Tooling scratch and retained earlier build outputs |
| `modding_docs` | Read-only local modding reference submodule |

## Source Rules

`source`, `generated`, and `packed` below refer to the owning project, not the
repository root. See [project layout](docs/reference/project-layout.md) for
dependency ownership and commands.

- Do not edit `source/archive` resources as text, including binary resources
  whose depot names end in `.json`.
- Edit `source/raw` when changing a packed CR2W resource. Convert and verify the
  result with the native template-backed workflow or WolvenKit where required.
- Plain quest/character manifests and braindance specs are authoring inputs,
  not packed resources.
- A scoped archive pack includes `source/archive` only. It does not include
  ArchiveXL, TweakXL, REDscript, or configuration files from
  `source/resources`.
- Search `modding_docs` before guessing at Cyberpunk-specific behavior.
- Treat `GraphEditorStates` as editor support data, not packed source.

## Runtime Dependencies

Ghostline uses ArchiveXL for quest, journal, localization, streaming, and
resource registrations. It uses TweakXL for custom character, faction, item,
and encounter records. Individual quest or character guides document any
additional dependency or expansion requirement.
