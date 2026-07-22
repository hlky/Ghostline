---
name: ghostline-quest-journal-scene
description: Use for Ghostline questphase, scene, journal, quest UI, NodeRef, quest fact, and gq000 progression work, including inspecting graph resources and keeping journal/localization paths aligned.
---

# Ghostline Quest, Journal, And Scene Workflow

## Before Editing

- Read `ROADMAP.md` before broad quest, world, journal, scene, or packaging
  work.
- Use `docs/tooling.md` explorer commands before loading full CR2W-JSON files into
  context.
- Check `modding_docs` before guessing at Cyberpunk quest, scene, or journal
  behavior.
- Read `docs/quest-scene-flow.md` before changing the root/child phase handoff,
  meeting lifecycle, trigger ownership, scene exits, or choice localization.
- For fresh scene work, use `docs/scene-authoring-rules.md`. Vanilla patterns
  override failed Ghostline probe results.

Useful docs:

- `modding_docs/for-mod-creators-theory/files-and-what-they-do/file-formats/quests-.scene-files`
- `modding_docs/modding-guides/quest`
- `modding_docs/modding-guides/quest/creating-custom-scenes.md`
- `modding_docs/modding-guides/quest/how-to-add-new-text-messages-thread-to-cyberpunk-2077.md`
- `modding_docs/modding-guides/quest/creating-custom-shards.md`
- `modding_docs/for-mod-creators-theory/files-and-what-they-do/file-formats/translation-files-.json.md`

## Questphase And Scene Rules

- `.questphase` resources are graph-style quest flow files. They can reference
  scenes and other resources through graph nodes, noderefs, sockets, and
  handlerefs. Use WolvenKit's graph editor for structural inspection.
- Quest facts are signed integer state values. They default to `0` until set.
  Prefer `gq000_` prefixes for Ghostline quest facts.
- Fresh `gq000` scene tooling should follow `docs/scene-authoring-rules.md`
  rather than preserving generated-scene probe workarounds.
- Emit editable scene resources under `source/raw` and use WolvenKit to produce
  the matching packed `source/archive` resources.
- For custom scenes built from scratch, include `performersDebugSymbols` in the
  scene `debugSymbols` array.
- Actor debug symbols are `actorID * 256 + 1`; prop debug symbols are
  `propID * 256 + 2`.
- In scene sections, actors are referenced by `performerID`.
- In `screenplayStore -> lines`, dialogue lines are linked by `actorID`.
- Spoken scene-line `locstringIds`, subtitle entries, and voiceover map entries
  must stay aligned. The subtitle String ID is the stable link between spoken
  on-screen text and the voiceover resource.
- Spoken lines and choice labels use different localization paths. Spoken
  lines resolve through subtitle/VO resources; choices resolve through the
  scene's embedded `locStore`. See `docs/quest-scene-flow.md` for the complete
  lookup chains and ID domains.
- Keep the mq003-derived lifecycle boundary: the meeting questphase activates
  the community, waits for `CharacterSpawned`, and starts the scene at the
  broad setup gate; the running scene owns the narrower mood, awareness, and
  engage gates.
- A scene outcome is only persistent when the questphase handles its named
  exit. The current `job_accept` route succeeds the meeting objective, clears
  its mappin, and sets `gq000_job_accepted`; the declared `end` route does none
  of those things.

## Current gq000 Resources

- Main questphase:
  - raw: `source/raw/mod/gq000/phases/gq000.questphase.json`
  - packed: `source/archive/mod/gq000/phases/gq000.questphase`
- Patch meet phase:
  - raw: `source/raw/mod/gq000/phases/gq000_patch_meet.questphase.json`
  - packed: `source/archive/mod/gq000/phases/gq000_patch_meet.questphase`
- Post-accept phase:
  - raw: `source/raw/mod/gq000/phases/gq000_post_accept.questphase.json`
  - packed: `source/archive/mod/gq000/phases/gq000_post_accept.questphase`
- Patch meet scene:
  - raw: `source/raw/mod/gq000/scenes/gq000_patch_meet.scene.json`
  - packed: `source/archive/mod/gq000/scenes/gq000_patch_meet.scene`
- Current stage relationship:
  - `gq000.questphase` is the main questphase for `gq000`.
  - `gq000_patch_meet.questphase` is the first stage where the player meets
    the logical Patch-role community actor. The current registry resolves that
    entry to `Character.GhostlinePatch`; the preceding Judy run is the stable
    lifecycle baseline and Patch itself still needs runtime validation.
  - `gq000_patch_meet.scene` is part of `gq000_patch_meet.questphase`.
  - Scene exit `job_accept` sets the accepted state; the root then starts
    `gq000_post_accept.questphase`, which currently activates only the cache
    objective/description/mappin skeleton and `gq000_02_started`.

## Journal Resources

- `reference/journal` contains serialized `.journal` reference slices.
- Use `py .\tools\explore_journal.py prefixes --with-types` to inspect one
  representative file per first-dot prefix before creating or editing custom
  journal resources.
- For quest UI work, keep `gameJournalPath.realPath` values aligned with the
  computed journal hierarchy, not only the leaf id. Example:
  `quests/minor_quest/gq000/gq000_01/gq000_01_obj_meet_patch`.
- Keep journal path ids separate from localization ids.
- For ArchiveXL-added onscreen localization, set `primaryKey` to `0`, use
  globally unique `secondaryKey` values, and reference those secondary keys
  directly from Ghostline journal localization fields.
- Do not invent numeric primary keys or add `LocKey#` prefixes unless a task
  explicitly requires primary-key lookups.

Known first-dot journal prefixes:

- `briefings`: briefing folders and `gameJournalBriefing` entries with video,
  paper doll, and map sections.
- `codex`: codex categories, groups, codex entries, and codex descriptions.
- `contacts`: phone/message contact entries.
- `internet_sites`: internet site and page entries.
- `onscreens`: onscreen groups and onscreen entries, including shards or
  email-style readable entries.
- `points_of_interest`: POI groups and `gameJournalPointOfInterestMappin`
  entries, usually linked back to a quest path.
- `quests`: quest folders, `gameJournalQuest`, `gameJournalQuestPhase`,
  objectives, descriptions, quest map pins, and codex links.
- `tarots`: tarot group and tarot card entries.

Current `gq000` journal files:

- raw: `source/raw/mod/gq000/journal/gq000.journal.json`
- packed: `source/archive/mod/gq000/journal/gq000.journal`

Current `gq000` quest onscreen localization:

- raw: `source/raw/mod/gq000/localization/en-us/onscreens/gq000.json.json`
- packed: `source/archive/mod/gq000/localization/en-us/onscreens/gq000.json`
