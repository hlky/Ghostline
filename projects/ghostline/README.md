# Ghostline Story Project

Open `Ghostline.cpmodproj` in WolvenKit. This project owns the connected story
series under [quests](quests/README.md), Iris/Cinder authoring, its source trees,
and the `story` and `development` package profiles. Both profiles activate only
story quests. The shared runtime dependency supplies Patch and GQ000 support.

From the repository root:

```powershell
uv run python -B projects/ghostline/quests/gq001/implementation/build.py
uv run python -B tools/package_project.py --project ghostline --plan
```

See [project layout](../../docs/reference/project-layout.md) for source ownership
and dependencies, and the [build guide](../../docs/workflows/build-and-package.md)
for verified packing and installation.
