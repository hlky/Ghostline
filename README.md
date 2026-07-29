# Ghostline

Ghostline is a connected Cyberpunk 2077 quest-mod series built as a WolvenKit
project. Its quests follow a covert broker collective uncovering Quiet Spine,
an identity-laundering network that treats memories, bodies, and civic
infrastructure as interchangeable parts.

## Quest Series

| Quest | Title | Status |
| --- | --- | --- |
| [`gq000`](quests/story/ghostline/gq000/README.md) | Original prototype | Superseded story; reusable runtime baseline |
| [`gq001`](quests/story/ghostline/gq001/README.md) | Ghostline | First canonical quest; extends and replaces `gq000` |
| [`gq002`](quests/story/ghostline/gq002/README.md) | The Machine Stops | Canonical |
| [`gq003`](quests/story/ghostline/gq003/README.md) | Black Lantern | Canonical preproduction |

The [series index](quests/story/ghostline/README.md) owns story order, shared
cast, voice design, continuity, and the template for future quests. Each quest
README owns its build and focused test commands.

## Start Here

Clone the repository with its submodules, then work from the repository root:

```powershell
git submodule update --init --recursive
py -B -m unittest discover -s tests -v
```

The normal development loop is:

1. Change plain authoring inputs under `quests`, `characters`, or
   `braindance`, or edit CR2W-JSON under `source/raw`.
2. Run the owning generator and focused tests documented by the relevant
   quest or authoring guide.
3. Validate generated raw resources before converting them to packed CR2W.
4. Build the complete archive from `source/archive`.
5. Stage the loose files from `source/resources` beside the archive.
6. Install and record runtime evidence on a suitable save.

See the [development workflow](docs/workflows/development.md) for the common
commands and the [build/package guide](docs/workflows/build-and-package.md)
before producing an installable archive.

## Documentation

- [Documentation map](docs/README.md) — choose a guide by task.
- [Quest series](quests/story/ghostline/README.md) — narrative and per-quest
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
| `quests/story/ghostline` | Series bible, quest design, scripts, compiler manifests, and per-quest build commands |
| `quests/examples`, `quests/tests` | Generic compiler examples and isolated `gqt###` test quests |
| `characters` | Character manifests and catalogs, neutral frame shells, and tooling-owned component libraries |
| `braindance` | Performance specs, rig contracts, templates, and render presets |
| `source/raw` | Editable CR2W-JSON for packed resources |
| `source/archive` | Packed/game-ready CR2W resources; never edit these binaries as text |
| `source/resources` | Loose ArchiveXL, TweakXL, REDscript, and configuration resources |
| `docs` | Cross-cutting workflows, authoring guides, references, and history |
| `reference` | Local serialized game references and generated selection indexes |
| `tools` | Generators, validators, explorers, and the pinned `ghostline-red` submodule |
| `generated` | Ignored reproducible build, audition, and preview output |
| `converted`, `packed`, `.tmp` | Ignored build and staging outputs |
| `modding_docs` | Read-only local modding reference submodule |

## Source Rules

- Do not edit `source/archive` resources as text, including binary resources
  whose depot names end in `.json`.
- Edit `source/raw` when changing a packed CR2W resource. Convert and verify the
  result with the native template-backed workflow or WolvenKit where required.
- Plain manifests under `quests`, `characters`, and `braindance` are authoring
  inputs, not packed resources.
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
