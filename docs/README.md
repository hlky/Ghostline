# Ghostline Documentation

This directory contains cross-cutting engineering documentation. Story design,
dialogue, quest state, and quest-specific build commands belong with the quest
under [`quests/story/ghostline`](../quests/story/ghostline/README.md).

## First Steps

1. Read the repository [README](../README.md).
2. Follow the [development workflow](workflows/development.md).
3. Open the owning quest README or authoring guide before changing generated
   resources.
4. Run the [automated test gate](workflows/automated-testing.md).
5. Follow [build and packaging](workflows/build-and-package.md) before
   installing a candidate.

## Workflows

- [Development](workflows/development.md) — normal edit, generate, validate,
  convert, test, and package loop.
- [Automated testing](workflows/automated-testing.md) — full and focused test
  commands.
- [Build, package, and install](workflows/build-and-package.md) — source
  boundaries, archive verification, loose-resource staging, and runtime logs.
- [Runtime testing and evidence](workflows/runtime-testing.md) — current
  candidate followed by dated historical baselines.
- [Test quests](workflows/test-quests.md) — isolated `gqt###` building-block
  conventions.

## Authoring Guides

- [Scenes](authoring/scenes.md)
- [World resources and NodeRefs](authoring/world-resources.md)
- [World asset discovery](authoring/world-assets.md)
- [World location database](authoring/world-locations.md)
- [Drop-point selection](authoring/drop-points.md)
- [Characters](authoring/characters.md)
- [Items and equipment](authoring/items-and-equipment.md)
- [Braindance](authoring/braindance.md)
- [ArchiveXL resource patching](authoring/archivexl-resource-patching.md)

## Reference

- [Tool catalog](reference/tool-catalog.md) — exhaustive command and helper
  reference.
- [Vanilla quest index](reference/vanilla-quests/README.md) — generated quest
  research.
- [Vanilla Cyberpsycho encounters](reference/vanilla-cyberpsycho-encounters.md)
- [SQ021 computer/file-read flow](reference/vanilla-sq021-computer-flow.md)

Reference documents describe observed game patterns or generated catalogs.
They are evidence for authoring decisions, not automatically current Ghostline
build instructions.

## History

- [Crash investigation](history/crash-investigation.md)
- [`ghostline-red` topology-write handoff](history/ghostline-red-topology-handoff.md)

History preserves dated failures, probes, and implementation handoffs. Use the
current workflow and authoring guides for new work unless a history document is
explicitly linked as supporting evidence.

## Documentation Ownership

- Keep current commands in `workflows`.
- Keep reusable construction rules in `authoring`.
- Keep observed vanilla behavior and generated catalogs in `reference`.
- Keep dated investigations in `history`.
- Keep quest-specific content beside its quest.
- Keep `modding_docs` untouched; it is a reference submodule, not Ghostline
  documentation.
