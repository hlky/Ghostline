# Projects And Building Tools

The repository root owns reusable tools, Python/Rust tests, documentation,
references, and compiler examples/templates. It is not a WolvenKit project.

```text
projects/
├── catalog.json
├── ghostline/
│   ├── Ghostline.cpmodproj
│   ├── project.json
│   ├── quests/                  # Series bible and gq000–gq003 authoring
│   ├── characters/              # Iris and Cinder authoring
│   ├── packaging/profiles.json  # story and story-only development
│   ├── source/{raw,archive,resources}/
│   ├── generated/
│   └── packed/
├── test-quests/
│   └── gqt001/ … gqt007/        # Each is a separate project
│       ├── GQT###.cpmodproj
│       ├── project.json
│       ├── *.quest.json
│       ├── implementation/
│       ├── packaging/profiles.json
│       └── source/{raw,archive,resources}/
└── shared/ghostline-runtime/
    ├── Ghostline_Runtime.cpmodproj
    ├── project.json
    ├── characters/              # Patch and reusable character authoring
    └── source/{raw,archive,resources}/
```

The prototype GQ000's narrative and implementation documentation remain in the
story project. Its reusable packed/raw runtime resources belong to the shared
runtime project. GQT003 also declares GQ000 as package support because its
existing packed phases reference the baseline. GQT005 borrows the shared GQ000
lipsync animation. GQT006 owns Goth Baddie's character and custom assets.
GQT007 has no shared runtime dependency.

`quests/templates` owns reusable phase/journal shapes and neutral character
catalogs/components. Its `source` trees contain compiler inputs. Those inputs
are not a runtime dependency and are not automatically shipped with a project.
`braindance` remains a building-system library of rigs, presets, and examples.
GQT005's performance spec lives in its own project's `braindance` directory.
GQT002's binary serialization donors and laptop shape are reviewed snapshots
in `quests/templates/source`, with provenance and hashes in
`quests/templates/donors/catalog.json`. Its build does not read another story
or test project's current outputs to obtain those templates.

## Project Configuration

Each `project.json` declares a stable ID, the depot prefixes it owns, and paths
to its dependencies relative to that project directory. Runtime projects also
declare their ArchiveXL registration filename and default package profile.
`projects/catalog.json` maps IDs to repository-relative project directories.

Tools resolve game depot identities such as `mod\gqt006\scenes\example.scene`
separately from filesystem locations. Longest matching depot prefixes select
the owner. Keep depot paths unchanged when moving workspace files: the game
does not know about `projects/`.

Packaging inventories only the selected project and its declared dependency
closure. Missing dependencies, cycles, and duplicate depot/loose-file owners
fail the build. The dependency's required runtime assets and registrations are
included in the consuming package; a separate dependency install is unnecessary.
Use the shared packager for this composition. A direct WolvenKit build of one
project sees that project's own source tree only.

## Commands

Run tools from the repository root:

```powershell
# Build story authoring, or produce an isolated preview.
uv run python -B projects/ghostline/quests/gq001/implementation/build.py
uv run python -B projects/test-quests/gqt006/implementation/build.py --out-root projects/test-quests/gqt006/generated/preview

# Inspect each project's package selection without packing or installing.
uv run python -B tools/package_project.py --project ghostline --plan
uv run python -B tools/package_project.py --project gqt006 --plan

# Pack, extract, compare hashes, and verify the project package.
uv run python -B tools/package_project.py --project gqt006
uv run python -B tools/package_project.py --project ghostline --profile development

# World output and registration default to the spec's owning project.
uv run python -B tools/generate_world.py generate --spec projects/test-quests/gqt006/implementation/world/goth-baddie-cyberpsycho.world.json --dry-run
```

`--project` accepts an ID, directory, or `.cpmodproj` path. Legacy
`--profile story`, `--profile development`, and `--profile gqt###` commands are
routed by the root `packaging/profiles.json`; actual selections are project-owned.
Package runs default to `<project>/generated/packages`. Explicit output overrides
remain supported. Preview builds use `source/raw` and `source/archive` relative
to their preview root, and may not write previews inside any project's source.

Open the owning `.cpmodproj` in WolvenKit. Editor state belongs to that project
and is not packed asset source. Repo-level earlier `generated`, `converted`,
`packed`, and `.tmp` directories are retained scratch, not current source.

## Adding A Project

Create its `.cpmodproj`, `project.json`, `source` trees, authoring manifest, and
`packaging/profiles.json`. Register its ID in `projects/catalog.json` and declare
its unique depot prefixes and dependencies. Keep quest-specific generators next
to that project's authoring inputs and reusable helpers under `tools`.
