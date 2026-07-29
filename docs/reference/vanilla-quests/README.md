# Vanilla Quest Reference

These files are generated research material. Regenerate them from their source
indexes; do not maintain individual quest entries by hand.

IGN's walkthrough indexes provide the curated quest lists and source URLs.
The local `H:\projects\quest.json` export provides the exact vanilla
journal paths, hashes, descriptions, objectives, and map-pin references.

Generated files:

- [Main Jobs](main-jobs.md): 57 matched quests
- [Side Jobs](side-jobs.md): 85 matched quests
- [Gigs](gigs.md): 85 matched quests

Machine-readable linkage:
[`reference/quests/ign-link-map.json`](../../../reference/quests/ign-link-map.json).

Regenerate:

```powershell
py -B .\tools\build_quest_reference.py
```

The generated pages summarize local journal data and link to IGN. They
do not mirror or reproduce IGN walkthrough articles.
