# GQT002 — Quiet Install

[The quest manifest](gqt002_quiet_install.quest.json) owns the optional stealth
objective, plant objective and marker, localized UI text, location aliases, and
facts. The plant item is declared with its target and shared by the stage and the
quest-specific item-grant logic.

The [build entrypoint](implementation/build.py) uses the shared compiler for the
two child phases, journal, and onscreen localization. It supplies its root graph
through `root_override`: guard activation and spawn wait, attitude setup, item
grant, the parallel detector/monitor/plant branch, three-input join, community
cleanup, and quest completion keep their existing ordering. The guarded-plant
template is supplied in memory before child compilation.

The laptop, device registry, security sector, and streaming-block logic remain
quest-specific. Existing generated world sectors are retained as inputs. All
13 resources publish through one transaction after collection and validation.

From the repository root, stage editable output for review:

```powershell
uv run python -B projects/test-quests/gqt002/implementation/build.py `
  --out-root generated/quest-migration/gqt002
```

The candidate contains 13 resources under `source/raw`. Omitting `--out-root`
publishes editable resources to the project. `--deserialize` also produces
candidate binaries through the shared build helper; it does not pack or install
an archive. Use the [build workflow](../../../docs/workflows/build-and-package.md)
for packaging.

`tests/test_legacy_quest_migration.py` checks the complete root and child graphs,
optional-objective flag, localization, world/device payloads, and failure before
publication. The migration preserves the existing behavior and has been checked
offline; fresh gameplay validation is a separate step.
