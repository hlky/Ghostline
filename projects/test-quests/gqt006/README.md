# GQT006 Cyberpsycho encounter authoring

The [quest manifest](gqt006_goth_baddie_cyberpsycho.quest.json) owns the
objectives, Regina conversation, readable shard, localization text, facts,
NodeRefs, and cyberpsycho marker variants. Explicit IDs preserve existing
journal paths, choice branches, localization keys, and game-state references.

Regina's contact, conversation, and opening brief use the reviewed
`regina_cyberpsycho` journal donor. The manifest retains her external localized
name, the brief's quest attachment and importance, and player attribution for
the three outcome messages. These fields are data in the composition rather
than mutations in a quest-specific journal generator.

The [build entry point](implementation/build.py) retains the custom challenge
phase and placed world. The encounter's existing scene assets, animation and
voice workflows remain separate authored prerequisites. `build_artifacts()`
collects the seven phases, journal, onscreens, and three world documents in
memory; the shared publisher writes the complete set together.

```powershell
py .\projects\test-quests\gqt006\implementation\build.py --out-root .\generated\quest-migration\gqt006
```

Add `--deserialize` to stage and convert all resources into that output tree.
`--serializer wolvenkit|native` and `--wolvenkit` retain their existing meanings.
The native path falls back to WolvenKit for layouts absent from its template.
Omitting `--out-root` intentionally publishes into the project source tree.
The build does not install or package a release.

`tests/test_modern_quest_migration.py` preserves every normalized stage field,
all seven phase graphs, meaningful journal metadata, onscreen keys and text,
and world documents. It also checks Regina's ordered messages, attachment,
importance, and sender metadata directly. These checks do not establish new
in-game evidence. The release-page draft remains in [RELEASE.md](RELEASE.md).
