# Ghostline Test Quests

Each `gqt###` directory is an independent WolvenKit project. It owns its
authoring manifest, implementation generator, world specification, runtime
source trees, registration, and package settings:

```text
gqt###/
├── GQT###.cpmodproj
├── project.json
├── descriptive-name.quest.json
├── implementation/
│   ├── build.py
│   └── world/descriptive-name.world.json
├── packaging/profiles.json
└── source/
    ├── raw/
    ├── archive/
    └── resources/
```

Generic compilers and scene/world generators remain under the repository's
`tools`. Shared assets are explicit dependencies in `project.json`; GQT007 is
self-contained. See [project layout](../../docs/reference/project-layout.md).

[GQT008](gqt008/README.md) is the self-contained floating interaction lab:
Barry's seated reactions, native workspot movement, interruption/return and
activity restoration. Its installed behavior is pending validation.

From the repository root, audit a package with
`uv run python -B tools/package_project.py --project gqt006 --plan`.
