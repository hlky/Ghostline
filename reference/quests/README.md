# Quest reference inputs

The [cinematic scene study](../../docs/reference/vanilla-quests/deep-dives/cinematic-scenes/README.md)
adds presentation metrics, per-quest inventories and raw-verified section case
studies. Its compressed analysis and verification records live in
`deep-dives/cinematic-scenes/`.

The [all-quest deep dives](../../docs/reference/vanilla-quests/deep-dives/all-quests/README.md)
cover all 416 exported journal entries, every stored type, plus an inventory of
the extracted implementation families. See the
[method](../../docs/reference/vanilla-quests/deep-dives/all-quests-method.md) and
[manual synthesis](../../docs/reference/vanilla-quests/deep-dives/all-quest-synthesis.md).
Their frozen source selection, compressed graph/pattern evidence and verification
records live in `deep-dives/all-quests/`. Earlier studies below remain separate snapshots.

The first source-backed questphase/scene studies are available in the
[vanilla quest deep dives](../../docs/reference/vanilla-quests/deep-dives/README.md):
Space Oddity (`mq003`) and Happy Together (`mq010`), with a candidate building-block
catalogue. Their machine-readable evidence and provenance live in `deep-dives/`.
These manually reviewed dossiers are separate from the generated journal index.

The [expanded catalogue](../../docs/reference/vanilla-quests/deep-dives/catalogue/README.md)
covers all 130 side/minor journal entries, including Phantom Liberty. See its
[coverage method](../../docs/reference/vanilla-quests/deep-dives/corpus-method.md)
for exact journal links, the POI-only case, unresolved entries and proof limits.
Compressed source evidence and per-resource provenance are in `deep-dives/catalogue/`.

`ign-index-snapshot.json` is the checked input for the offline quest-reference
generator. It retains IGN index titles and URLs only; it contains no walkthrough
article prose. The journal export supplies the quest descriptions and structure.

The snapshot was reconstructed on 2026-09-05 from `ign-link-map.json` at repository
revision `29bdc504cad11fa5e7bcb3e435b93f83eb5f376b` (original file SHA-256
`7392c4a62d81e6e851f0ec62c4bffb002b52a7a95363fea7eee0dd428dacca85`). For each
category, reconstruction combined matched `ign_title`/`ign_url` pairs with
`unmatched_index_links`, deduplicated exact title/URL pairs, and sorted those
pairs. It retained 79 main-job, 94 side-job, and 95 gig links. No network request
was made. The original fetch date is unknown; this reconstruction cannot recover
links that the previous generator discarded, and is not a current IGN scrape.

The local journal input used for this regeneration is `H:\projects\quest.json`,
SHA-256 `b39930c6cdee37f985fd489a511f34dfe0865a00b69ff37a441da307dc41fb28`.
It is an external game-data export, not a checked repository input. Reproducing
the same reference requires the same export; its content hash in the generated
link map detects a different input. `ign-link-map.json` now records the journal,
snapshot, and generator paths and SHA-256 hashes on each run.

Run from the repository root:

```powershell
py -B tools/build_quest_reference.py --quest-json H:\projects\quest.json
```

This uses the checked snapshot without importing network dependencies. To use a
different export or snapshot, supply `--quest-json` or `--index-snapshot`.
`--refresh-indexes` explicitly fetches current IGN index links and replaces the
snapshot before generating the reference; review the snapshot diff when using it.
Keep provenance with a refreshed snapshot instead of presenting its links as the
original reconstruction.
