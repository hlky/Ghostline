# GQT001 — Signal Delay

[The quest manifest](gqt001_signal_delay.quest.json) owns objectives, Patch's
ordered confirmation thread, the diagnostic file, localization, location aliases,
and facts. Explicit journal IDs and localization keys preserve the original
terminal and phone references.

The [build entrypoint](implementation/build.py) compiles the root, four child
phases, journal, and onscreen localization together. It adds the quest-owned
laptop sector, streaming-block entry, and device registry through the same
publication transaction. The laptop's persistent-state layout and placement
remain quest-specific; its document text, journal path, completion fact, and
owned NodeRef come from the manifest bindings.

From the repository root, stage editable output for review:

```powershell
uv run python -B projects/test-quests/gqt001/implementation/build.py `
  --out-root generated/quest-migration/gqt001
```

The candidate contains 10 resources under `source/raw`. Omitting `--out-root`
publishes editable resources to the project. `--deserialize` also produces
candidate binaries through the shared build helper; it does not pack or install
an archive. Use the [build workflow](../../../docs/workflows/build-and-package.md)
for packaging.

`tests/test_legacy_quest_migration.py` compares the entire artifact set with the
pre-migration contracts, including phone entry order, laptop payload, and every
normalized manifest field. The migration was validated offline; fresh gameplay
validation is a separate step.
