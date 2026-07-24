# Building-Block Test Quests

Test quests isolate reusable quest behavior without requiring a coherent story.
They live under `source/quests/tests` and use the `gqt` prefix. A stage remains
`planned` until its journal, scene, world, and localization resources exist and
its selected world location has passed an in-game accessibility and quest-safety
review.

## `gqt001_signal_delay`

Purpose: validate the complete terminal-document boundary rather than only the
reduced questphase template.

The current runtime candidate uses a Ghostline-owned laptop rather than
patching an existing vanilla laptop. Its complete persistent package contains
the diagnostic Files entry. For the focused test it is placed about two metres
from the captured save spawn, with the reach trigger and quest marker moved to
the same location. This isolates computer content authoring from vanilla
persistent-state mutation.

```text
reach terminal
  -> select/read quest-owned computer document
  -> vanilla document questInfo sets gqt001_document_read
  -> wait 10 seconds of elapsed game time
  -> Patch phone conversation
  -> gqt001_completed
  -> succeed quests/minor_quest/gqt001
```

The owned device is derived from SQ021 Randy's laptop. Runtime proved that the
instance package must retain the entity component CRUIDs or the laptop silently
falls back to the empty controller from `laptop_1.ent`. The Files-only revision
also removes SQ021 mail, internet, newsfeed, and scanner content and uses a
fresh NodeRef so an existing save cannot restore the earlier copied device
state. See [SQ021 Computer And File-Read Flow](vanilla-sq021-computer-flow.md).

Next authoring steps:

Runtime validation confirmed the revised laptop exposes only the Files tab,
opening SIGNAL DELAY advances the read stage, and the ten-second gate reaches
Patch's two-choice exchange. The phone stage now explicitly succeeds the
quest journal entry after setting `gqt001_completed`; the remaining runtime
check is that either Patch reply produces the normal quest-complete
presentation and removes SIGNAL DELAY from the active tracker.
