# Shared Ghostline Runtime

This project owns Patch, reusable character assets, common localization/faction
records, and the GQ000 runtime baseline. Story/test projects declare it as a
dependency in their `project.json`. Their packager includes the required shared
assets and registrations in the resulting package.

Neutral character shells, catalogs, and component libraries are building-system
inputs under `quests/templates/characters` at the repository root. The GQ000
prototype narrative lives in `projects/ghostline/quests/gq000`.

Use the consuming project's package command documented in
[project layout](../../../docs/reference/project-layout.md); its verified package
already includes the shared resources it needs.
