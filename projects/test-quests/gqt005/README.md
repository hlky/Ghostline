# GQT005 Braindance Analysis

The [quest manifest](gqt005_braindance_analysis.quest.json) owns the journal,
onscreen text, objective counter, facts, and shared NodeRefs. Stage references
use composition bindings so the approach, Patch meeting, and braindance review
share the same objective. The meeting retains that objective until the review
finishes; the counter matches the three declared clue facts.

The [build entry point](implementation/build.py) combines the shared compiler
artifacts with its custom launch scene, authored RID links, clue assets, and
scene-marker world data. `build_artifacts()` constructs the complete raw set in
memory. The shared `quest_build.publish_build` publishes it together, and stages
all requested conversions plus the prebuilt RID before replacing destinations.

```powershell
py .\projects\test-quests\gqt005\implementation\build.py --out-root .\generated\quest-migration\gqt005
```

The [performance spec](braindance/gqt005_braindance_analysis.json) belongs to
this project. The existing animation prerequisites are still required under
`projects/test-quests/gqt005/.tmp/braindance/gqt005` (from the repo root): `gqt005_braindance_analysis.scenerid.json` and
`gqt005_braindance_analysis.handoff.json`. Use `--rid-json`, `--handoff`, and
`--scene-template` for explicit inputs. Binary builds additionally require the
prebuilt RID selected by `--rid-binary`.

Add `--deserialize` to convert into the same isolated output tree. The existing
`--serializer wolvenkit|native` and `--wolvenkit` options remain available.
Omitting `--out-root` intentionally publishes into the project source tree.
This command does not install the quest or generate its animation prerequisites.

`tests/test_modern_quest_migration.py` checks all four phase resources, journal
fields, localization text, launch-scene data, and world data against captured
pre-migration baselines. These are build and structural checks; runtime
braindance playback still needs an in-game test.
