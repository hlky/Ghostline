# Black Lantern Scenes

## Scene And Tooling Decisions

The two formal scene dialogue sources and generated scene specs now exist at:

- `quests/story/ghostline/gq003/script/gq003_02_manifest.json` for the opening
  Iris briefing;
- `quests/story/ghostline/gq003/script/gq003_20_manifest.json` for the safe-site
  Iris scene.

Their locstring IDs are deterministic FNV-1a values derived from the line keys.
The scene specs generate and validate as `gq003_iris_briefing.scene.json` and
`gq003_iris_safe_site.scene.json`, including embedded choice labels and named
exits. The checked durations and WEM paths remain planning values until voice
production replaces them; no audio asset is implied to exist yet.

### Reuse now

- Use the established mq003-derived `meet_contact` lifecycle for both Iris
  scenes: activate community, wait for spawn, launch from the broad setup gate,
  then let the running scene own mood, awareness, and engage conditions.
- Keep spoken lines in subtitle/VO resources and choice labels in each scene's
  embedded `locStore`, even though voice production is deferred.
- Use the existing `gqt002` compound stealth topology, `gqt003` retained escort
  and fixed-attacker defense topology, and `gqt004` vehicle lifecycle.
- Use `gq002`'s choice-gate followed by one common device operation.
- Use the runtime-confirmed native drop-point reservation and deposit flow.

### Implemented extensions and remaining runtime decisions

1. **Multi-contact phone stages:** implemented. Journal message paths can
   alternate between Morrow and Iris, stage 36 uses two sequential conditional
   groups, and Patch's final message is a non-gating postscript.
2. **Outcome-dependent drop-point item:** implemented. Stage 33 mutates the
   cipher into the receipt only on the burn route; stage 35 reserves the item
   selected by the corresponding route fact. No neutral fallback item is used.
3. **Safe-site staging:** retain Mara through stage 20 while independently
   activating and acquiring Iris. Keep the formal scene two-performer for the
   first implementation. A speaking Mara inside the scene would require a
   multi-community spawn rendezvous and three-performer scene spec.
4. **Transfer window semantics:** the current `time_gate` represents elapsed
   game time. If the objective must open at a specific hour of night, add an
   absolute time-of-day contract instead of describing a fixed delay as a clock
   deadline.
5. **Mara failure:** the root inserts a retry-enabled checkpoint and the
   defense child fails the objective, sets `gq003_mara_lost`, and emits no
   normal exit. Confirm that `retryOnFailure` produces the intended automatic
   reload in game; the fixed attackers and 90-second success signal remain
   encounter-owned.
