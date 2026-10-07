# Vanilla Quest Reference

These files are generated research material. Regenerate them offline from
the checked index snapshot; do not maintain individual quest entries by hand.

IGN's walkthrough indexes provide the curated quest lists and source URLs.
The local `H:\projects\quest.json` export provides the exact vanilla
journal paths, hashes, descriptions, objectives, and map-pin references.

Generated files:

- [Main Jobs](main-jobs.md): 57 matched quests
- [Side Jobs](side-jobs.md): 85 matched quests
- [Gigs](gigs.md): 85 matched quests

Machine-readable linkage:
[`reference/quests/ign-link-map.json`](../../../reference/quests/ign-link-map.json).
The linkage records SHA-256 identities for the journal, index snapshot, and generator.
Snapshot provenance: [`reference/quests/README.md`](../../../reference/quests/README.md).

Regenerate:

```powershell
py -B .\tools\build_quest_reference.py --quest-json H:\projects\quest.json
```

The default command uses no network. `--refresh-indexes` explicitly fetches
new index links and replaces the snapshot; review that input change first.

The generated pages summarize local journal data and link to IGN. They
do not mirror or reproduce IGN walkthrough articles.
