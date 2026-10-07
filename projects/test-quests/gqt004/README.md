# GQT004 — Vehicle Lab

[The quest manifest](gqt004_vehicle_lab.quest.json) owns the five objectives,
markers, Patch and vehicle aliases, localization, and facts. Explicit identifiers
preserve the existing journal hierarchy and phase paths.

The [build entrypoint](implementation/build.py) compiles the root, six child
phases, journal, and onscreen localization together. It retains the final cleanup
template, which despawns the player vehicle, records completion, and succeeds
the quest. That template is supplied to the compiler in memory, so compilation
does not depend on a separately refreshed raw template.

From the repository root, stage editable output for review:

```powershell
uv run python -B projects/test-quests/gqt004/implementation/build.py `
  --out-root generated/quest-migration/gqt004
```

The candidate contains 10 resources under `source/raw`. Omitting `--out-root`
publishes editable resources to the project. `--deserialize` also produces
candidate binaries through the shared build helper; it does not pack or install
an archive. Use the [build workflow](../../../docs/workflows/build-and-package.md)
for packaging. The separate [world spec](implementation/world/vehicle-lab.world.json)
continues to own vehicle placement.

`tests/test_legacy_quest_migration.py` compares all 10 resource payloads and every
normalized manifest field with their pre-migration contracts. The migration was
validated offline; fresh gameplay validation is a separate step.
