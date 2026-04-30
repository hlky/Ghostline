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
- Scene `locstringIds`, subtitle entries, and voiceover map entries must stay
  aligned. The subtitle String ID is the stable link between on-screen text and
  the voiceover resource.

## Current gq000 Resources

- Main questphase:
  - raw: `source/raw/mod/gq000/phases/gq000.questphase.json`
  - packed: `source/archive/mod/gq000/phases/gq000.questphase`
- Patch meet phase:
  - raw: `source/raw/mod/gq000/phases/gq000_patch_meet.questphase.json`
  - packed: `source/archive/mod/gq000/phases/gq000_patch_meet.questphase`
- Patch meet scene:
  - raw: `source/raw/mod/gq000/scenes/gq000_patch_meet.scene.json`
  - packed: `source/archive/mod/gq000/scenes/gq000_patch_meet.scene`
- Current stage relationship:
  - `gq000.questphase` is the main questphase for `gq000`.
  - `gq000_patch_meet.questphase` is the first stage where the player meets
    Patch.
  - `gq000_patch_meet.scene` is part of `gq000_patch_meet.questphase`.

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
