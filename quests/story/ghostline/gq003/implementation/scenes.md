# Black Lantern Scenes

## Scene And Tooling Decisions

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

### Small extensions or custom phases

1. **Multi-contact phone stage:** stage 31 needs fixed sequential messages from
   Morrow and Iris. Stage 36 needs a required Morrow thread plus optional Iris
   and Patch postscripts. Extend `phone_conversation` with per-message contacts,
   or implement quest-local custom phases. Fallback: put the entire required
   exchange under Morrow and deliver Iris/Patch as non-blocking companion
   messages before and after it.
2. **Outcome-dependent drop-point item:** stage 35 must reserve either the
   cipher or the receipt. Extend `deliver_drop_point` with fact-selected item
   branches, or create a quest-local delivery phase. Fallback: convert both
   outcomes into one neutral `Items.GhostlineBlackLanternPackage` record after
   stage 33.
3. **Safe-site staging:** retain Mara through stage 20 while independently
   activating and acquiring Iris. Keep the formal scene two-performer for the
   first implementation. A speaking Mara inside the scene would require a
   multi-community spawn rendezvous and three-performer scene spec.
4. **Transfer window semantics:** the current `time_gate` represents elapsed
   game time. If the objective must open at a specific hour of night, add an
   absolute time-of-day contract instead of describing a fixed delay as a clock
   deadline.
5. **Mara failure:** confirm that the fixed-attacker defense template can route
   failure into checkpoint reload. Do not allow its ordinary failure socket to
   continue into the safe-site scene.
