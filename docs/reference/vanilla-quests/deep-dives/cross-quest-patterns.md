# Compositions emerging from the larger corpus

These are research reductions, not new compiler stage types. The full
[catalogue](catalogue/README.md) supplies source-node locators, neighboring
sockets, explicit predicates, scene contracts and fact dependencies for each
journal quest. The [expanded contracts](expanded-blocks.md) describe the smaller
mechanisms to compose. An example can share resources with other quests.

## Weapon progress and milestone transitions

[Machine Gun](catalogue/base-mq007_smartgun.md) demonstrates why embedded graphs
must be inspected even when they contain no journal updates. In
`mq007.questphase`, embedded graph h606:

- Node 70 waits for `mq007_skippy_enemies_non_lethal >= 50`, then writes the
  maimed milestone at 75.
- Node 71 combines `mq007_skippy_enemies_lethal >= 50` with an option fact,
  then writes the lethal/mode milestone at 74.
- A separate convergence reaches node 34, which writes the defeated milestone.

The proposed composition is **progress inputs → policy-specific milestone →
conversation/mode consequence**. Bind the producer and reset policy of the raw
counters explicitly. A milestone fact writer is not itself the telemetry
source. Preserve lethal/nonlethal and mode conditions rather than substituting
one generic kill-count threshold.

Acceptance cases: both progress policies, mode changes, an already-satisfied
counter, milestone arrival during dialogue, and load after a milestone but
before its consequence.

## Collection of child jobs and individual encounter contracts

[Beat on the Brat](catalogue/base-mq025_psycho_brawl.md) and its district jobs
share an umbrella family but expose separate journal objectives and outcomes.
The corpus includes district encounter phases, the finale, and the shared
`q001_fistfight_tutorial.questphase`. Likewise,
[Epistrophy](catalogue/base-sq025_delamain.md) and its vehicle-specific entries
share orchestration and repair resources.

The reusable composition should distinguish **collection orchestration** from
**one child encounter**: eligibility, individual outcome, collection progress,
finale unlock and retirement. A shared family file is not proof that each child
has the same mechanics. The catalogue traces each child's own journal targets
and connected signals rather than assigning all family nodes to every job.

Acceptance cases: arbitrary child order, returning to a resolved child,
interrupted parent contact, partial collection save/load and a failed child
that must not incorrectly count as a successful encounter.

## Race lifecycle versus ordinary vehicle travel

[The Beast in Me](catalogue/base-07_nc_underground.md), its race journals and
[The Distance](catalogue/base-mq056_race_replay.md) combine vehicle state,
countdown, course-related conditions, outcome and cleanup. This exceeds a
single destination-trigger block.

Concrete difference: `sq024_02_pacifica_race.questphase` h901 nodes 28/32 and
`sq024_03_badlands_race.questphase` h1070 nodes 28/32 inspect
`RacePlayerDistanceFromSpline`, with different authored values/comparisons.
The current corpus also contains explicit race cleanup, mounted/inside-car,
start and opponent-finish facts. Omitted comparisons remain RED defaults.

A proposed race composition needs course/spline ownership, entrants and seats,
staging/countdown, course violation handling, finish ordering, outcome commit
and restart/cleanup. Do not reduce these to `drive_to` merely because both
involve a vehicle reaching an area.

Acceptance cases: late mounting, leaving the course, abandoning or restarting,
opponent finishing first, destroyed vehicle, and load during countdown/finish.

## Terminal discovery, reading and analysis

[The Hunt](catalogue/base-sq021_sick_dreams.md) provides a concrete device/UI
boundary. In `sq021_randys_room.questphase`, h237 node 191 writes
`sq021_thisisfucked_read`, and 192 observes it. Nearby waits 145/176 inspect
`sq021_randy_pc_webfile_found`. The computer scene's named page-selection
output is the bridge described by the existing
[terminal block extraction](../../../../reference/vanilla_quest_blocks/EXTRACTION-NOTES.md).

Keep **device availability**, **document discovery**, **actual selection/read
signal**, and **quest interpretation** separate. The Hunt's braindance scenes
add rewindable sections and analysis-layer behavior; they do not turn every
computer document into a braindance or every inventory shard into a read event.

Acceptance cases: revisit the document, discover before the objective starts,
leave the computer, interrupt the commentary, replay analysis, and load after
read but before interpretation.

## Consequences as a separate phase family

Phantom Liberty supplies clear orchestration examples:

- [Dazed and Confused](catalogue/ep1-mq303_addict.md) has separate hook,
  mansion/combat, finale, messages, consequences and epilogue-message phases.
- [Shot by Both Sides](catalogue/ep1-mq305_combat_zone_report.md) separates hook,
  apartment, bunker exploration, confrontation and outcome, with corresponding
  setup/repair files. Its confrontation h72 node 69 writes
  `mq305_both_killed`; conditions in that graph and h0 inspect
  `mq305_bree_dead`. This already exceeds a two-output dialogue-choice model.
- [No Easy Way Out](catalogue/ep1-mq306_dumpster.md) separates intro,
  tech-expo/combat and later meeting phases. Root embedded graphs h63 / 15
  and h509 / 5 test the committed `mq306_aaron_path == 1`.

The proposed composition is **encounter outcome commit → consequence selection
→ later contact/world staging → deferred cleanup**. Persist outcome separately
from whether presentation has played. Keep subsequent messages independently
retirable; their existence is not the success signal for the preceding stage.

Acceptance cases: every committed outcome, multiple participants defeated,
departure during an ending, delayed contact while another scene owns the
speaker, and save/load between outcome commit and presentation.

## Contact availability as a dependency

[Balls to the Wall](catalogue/ep1-mq301_bomb.md) contains distinct initiation,
frame, drive, contacts and ending phases. In
`mq301_06_contacts.questphase` h0 node 107 checks
`mq301_03_river_help >= 1`. The larger family also contains distinct help facts
and scene-controlled branches.

This supports a **contact-assistance gate** composition: resolve contact/story
availability, offer eligible alternatives, commit the selected help route, then
continue its own contact and outcome lifecycle. A named help fact alone does
not establish the complete eligibility rule; inspect its producer and the
choice gate in the dossier.

Acceptance cases: unavailable contact, several eligible contacts, refusal,
interrupted call, repeated request and loading after assistance is committed.

## What should become compiler functionality first

The strongest cross-cutting improvements remain:

1. Validate actual scene entries, exit consumers, notification semantics and
   actor/world bindings.
2. Make concurrent branch ownership, joins and retirement explicit, including
   embedded graphs without journal nodes.
3. Extend investigation event/order/bypass policies without weakening existing
   tested shapes.
4. Separate authoritative state commit from consequence presentation and
   delayed cleanup.
5. Keep vehicle/race, braindance and world-set-piece behavior as explicitly
   bound compositions until their dependencies and recovery cases are isolated.

The structural expansion does not change the proof status of existing Ghostline
templates and does not replace per-instantiation installed tests.
