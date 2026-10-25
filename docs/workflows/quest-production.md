# Quest production

Use this workflow when starting a quest or planning substantial new quest
behavior. [Development](development.md) owns the edit/build commands;
[runtime testing](runtime-testing.md) owns evidence and test handoffs. The
[GQ004 retrospective](../../projects/ghostline/quests/gq004/RETROSPECTIVE.md)
records the experience behind this sequence.

## Establish the environment

Resolve the owning project, game installation, tool paths, and package profile.
Check existing reviewed artifacts and compatible versions before building
replacements. Run a short voice synthesis and playback check before a full
batch; use the [voice environment workflow](voice-environment.md).

For local character/item tools, verify the expected application, active game
root, and index provenance before interpreting missing assets. A cached page
or stale index can imitate an authoring defect. Use focused explorer/API output
for inspection and the browser for visual decisions; avoid repeated full UI
tree dumps when a small query will answer the question.

## Review the player experience

Maintain a readable walkthrough beside the quest, covering objectives, every
dialogue choice, shard contents, messages, reward, and ending. Review it before
bulk VO and update it when sequencing changes. For each exchange, identify:

- the player action that triggers it and what the player knows at that point;
- required actor readiness, file-read state, and preceding dialogue;
- interruption, deferral, return, and retry behavior;
- objective/mappin changes, reward confirmation, and cleanup ownership.

Let dialogue explain the immediate action and stakes. Put optional technical
detail in readable material when that improves clarity. A downloaded shard
does not establish that the player has read it.

## Prove a complete route early

Build an installed route from acceptance through the main interaction, return,
reward, and journal completion using provisional presentation. Choose locations
early enough to validate approach and interaction geometry. Full appearance,
voice, and FX production can follow this proof rather than delaying it.

For behavior with a native precedent, inspect the local modding docs, then
working Ghostline/vanilla resources before adding runtime scripts or audio
frameworks. Preserve the requested interaction, including whether it has a
minigame. If native behavior cannot meet a requirement, record that concrete
limitation and the fallback's lifecycle/dependencies.

For a meeting/transfer/reward route, use the extracted
[native quest template](../authoring/native-quest-template.md). It supplies
the shared lifecycle and an isolated preview builder with explicit integration
contracts. GQ004's [dialogue flow](../../projects/ghostline/quests/gq004/implementation/DIALOGUE-FLOW.md)
remains the story example; its shard/guard logic is quest-owned.

## Exercise transitions before presentation polish

Test the applicable alternate paths while the route is small: arrival inside
setup after fast travel, rapid defer/return, guard deaths, transfer interruption,
leaving during speech, and save/load between stages. Follow the
[runtime handoff contract](runtime-testing.md#playtest-handoff-contract).

Separate three kinds of evidence:

| Evidence | Establishes |
| --- | --- |
| Authoring tests and native readback | Authored graph/data invariants and serialization preservation. |
| Archive/ZIP/install verification | Selected payload and installed-byte integrity. |
| Named in-game scenario | Behavior actually observed on that package and save state. |

A passing lower layer does not establish a higher one. Report the first
unverified boundary explicitly. During diagnosis, distinguish the observation,
suspected cause, evidence to discriminate it, and confirmed result. Compare the
last working package before attributing a regression to an unchanged resource.

## Finish and hand off

After the route works, complete appearance, approved performances, lipsync,
effects, descriptions, and icons. Inspect the actual game display contexts;
offline fit and valid atlas bindings cannot establish runtime presentation.

Use a named final package for the full route and requested duration check.
Keep test results and remaining gaps alongside the quest. Update its README,
state, walkthrough, and install receipt when feedback supersedes candidate
status. Disable temporary diagnostic hooks in source and the installed helper,
preserve evidence/captures, and state whether a restart is needed to unload
callbacks. The final package should declare its actual runtime dependencies.
