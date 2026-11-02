# Finish cleanup and courier arrival

User evidence on candidate `gqt010-0c270f5772e9`: route, turns and race work well;
opponent remained after driving far from the finish. Courier persistence after
reward pickup was uncertain. Courier/bike appeared immediately at the finish
and the player collided with the arrival.

Builder findings and changes:

- Opponent community deactivation shared the successful lifecycle's reward-taken
  and courier-finished gates. A separate finish-area exit now retires opponent
  driving/wreck watchers and deactivates the crew after 0.5 seconds, without
  joining the reward branch. The main lifecycle retains its idempotent cleanup.
- The distance helper created an empty `questUniversalRef`. It now uses the
  explicit local-player reference from the native quest pattern, including
  `refLocalPlayer: 1`. Courier fallback and departure checks retain 100/150 m.
- The five-second/eight-metre courier presentation gate prevented delivery in
  the user's playtest. Removed it and its unused marker. Restored the original
  courier/crate presentation flow. Fresh surface raycasts move courier and bike
  onto pavement to the right of the finish road; departure exits between bollards.

Validation: focused lifecycle regression passes; native conversion and semantic
readback pass; package `gqt010-b85a61ba144b` passes extraction/ZIP verification.
Survey input hash remains
`0a543ce1aa0ffb01a6e450f9dc07a61147399d2d0d906a4568b3440d764c48d9`;
the 3.154 km route and eleven gates are unchanged. The user confirmed opponent
cleanup in that candidate; courier arrival failed. The current placement and
four-opponent update is recorded in placement-survey-2026-11-02.json and needs
a fresh race attempt and playtest. No GQT009 package was rebuilt.
