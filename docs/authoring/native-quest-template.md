# Native meeting and personal-link quest template

The [template manifest](../../quests/templates/native-personal-link/template.json)
builds a small native quest route: protected meeting, recover/upload transfers,
debrief reward, inventory-confirmed completion, and departure cleanup. It is
extracted from playtested GQ004. Each new binding set still needs scene/world
integration and an in-game test.

## Build an isolated preview

Run from the repository root:

```powershell
.venv/Scripts/python.exe tools/native_quest_template.py `
  --spec quests/templates/native-personal-link/template.json `
  --out-root generated/native-personal-link-preview

# Convert and verify native CR2W with the shared staged build workflow.
.venv/Scripts/python.exe tools/native_quest_template.py `
  --spec quests/templates/native-personal-link/template.json `
  --out-root generated/native-personal-link-native --deserialize

.venv/Scripts/python.exe -m unittest tests.test_native_quest_template tests.test_love_actually -q
```

The default example emits twelve resources under the preview's `source/raw`:
eight questphases, two cloned device entities, a journal and onscreen localization.
`--deserialize` also produces their binaries under that preview's `source/archive`
after typed readback. The build does not register or install the quest. Output
inside a real project's source tree, or at a project/repository root, is rejected.

`native-contract.json` lists required world references, scene entries/exits,
device-to-entity mappings, facts, reward, optional call/epilogue, an ArchiveXL
registration fragment, and the package profile's additional root phases.

## Runtime ownership

| Resource | Owns |
| --- | --- |
| Root | Runs meet, transfers in order, and return; retains world prefabs/community until the player is outside the cleanup trigger. Already-completed quests exit immediately. |
| Meet | Activates the community, waits for spawn readiness, applies friendly attitude/invulnerability, starts the scene from an already-inside setup gate, handles acceptance and immediate deferred re-entry. |
| Transfer attempt | Strict personal link, connection wait, timed native progress, disconnect listener, optional connected scene, terminating success/retry exits. |
| Transfer parent | Objective and device activation, optional instructions/retry/success scenes, commit fact, two-tick child retirement, forced unplug, device disable and objective cleanup. |
| Return | Protected meeting and debrief exit, then item grant. |
| Finish root | Waits for debrief, settles two ticks, queries current inventory or waits for delivery, marks reward verified/granted, completes journal/fact, then optionally runs delayed epilogue. |
| Optional repair root | For explicitly enabled migrations: checks completed/debrief facts, exits when delivery was already verified, otherwise confirms existing inventory or grants and verifies the missing reward. |

The finish root is registered alongside the main root, so keeping the contact
visible does not hold the quest open. A completed-fact branch prevents a fresh
attachment from replaying the route or finish. The optional repair's verified
flag prevents regranting after an item has subsequently been consumed or sold.

## Bind the template to a quest

Copy the JSON into the consuming quest's authoring directory and set:

- `namespace` and `title`: namespace owns emitted depot paths, facts and
  generated localization IDs. Use a distinct namespace for each quest.
- `phase_prefabs`: world prefabs retained by the root, including the holocall
  studio if the optional call/scenes need it.
- `giver`: community NodeRef/entry, scene origin, setup/rearm/cleanup triggers,
  and the meeting/return scene resources. Appearance and character record are
  supplied by the world community registry.
- `objectives`: exactly `meet`, `return`, and each transfer ID. Each supplies
  text, description and a dedicated marker NodeRef. Journal paths are composed
  automatically with `quest_authoring`; callers do not duplicate them.
- `transfers`: one to sixteen distinct IDs and devices, visible progress label,
  and positive integer `duration_seconds`. The example has recover and upload.
- `reward`: an existing `Items.*` record, positive quantity, and an explicit
  `repair_completed_saves` Boolean. The template does not define the item's
  gameplay effect, rarity, icon or tooltip.

Each transfer may add `intro_scene`, `retry_scene`, `success_scene`, and
`connected_scene`. These use `{scene, origin, entry, exit}` objects. Instructions
finish before the device is armed. The connected scene starts only after the
actual link connects; success waits for both the timer and that scene. A
terminating retry cancels its timer/scene branch. Scene authors must gate their
speakers on spawn readiness, including the first time-zero line.

The neutral access-point donor uses `Interactions.ConnectPersonalLink`.
`interaction_record` can select another existing `Interactions.*` record; the
consumer then owns that record and its caption localization. Progress labels
are independent of the interaction caption. The cloned controllers preserve
the disabled `HackingSkillCheck`, personal-link slot, strict control, and
minigame-skip settings that fixed GQ004's inert prompt.

Optional `epilogue` is `{phase, delay_seconds}` for a separately authored native
phase. It follows journal completion and cannot name a generated route phase.
Use it for optional texts; it supplies no completion or reward side effects.

Optional `audio_call` is `{caller, addressee, prefab, start_before, end_before}`.
Caller/addressee are full contact journal paths, not display names. Start/end
must refer to ordered route stages, and the prefab must be retained. This
provides an audio-only call lifecycle; it does not spawn dialogue actors or
generate contacts. Supply those resources in the consuming quest.

## Integrate and validate

Supply the world community, trigger volumes, scene markers and mappins from the
contract. Place each emitted device entity at its declared NodeRef and register
it in Night City's actual `.devices` registry. Keep access-point local `+X`
facing and wall placement conventions from [world authoring](world-resources.md#location-capture-and-wall-mounts).
Derive interaction markers from final device transforms.

The meeting scene needs `start` and `resume` entries and `job_accept`/`end`
exits. `resume` restores choices without replaying the introduction. The return
scene needs `start` with the same exits. Scenes own inner proximity/combat
conditions; the meeting phase owns spawn and broad setup. Use the existing
scene generator and the [scene lifecycle contract](scenes.md#progression-and-speaker-lifecycle).

Move reviewed authoring outputs to the owning project's source trees through
its build, declare its depot ownership, and merge the registration fragment.
List finish (and optional repair) in that profile's `additional_root_phases`.
Supply item, character, world streaming/device registration, scene VO/lipmaps
and call contacts as required before packaging. The generated contract is an
integration checklist, not a complete release registration. No CET, REDscript,
or Audioware runtime is introduced by this template.

Run the [playtest handoff scenarios](../workflows/runtime-testing.md#playtest-handoff-contract).
This extraction proves authoring invariants and GQ004 graph parity; it does not
grant new in-game evidence to the demonstration quest.

## Source and extraction evidence

`tools/quest_native_lifecycle.py` owns reusable builders. GQ004's `phases.py`
is now a content adapter for meeting, attempt, root, completion and repair;
its shard sequencing, guard FX, arrival behavior and epilogue dispatch remain
quest-owned. The generic transfer parent uses the same attempt/unplug boundary
but has optional scene hooks instead of GQ004's story-specific shard/FX code.

The seven pre-extraction GQ004 graphs are pinned by canonical JSON hashes in
[the baseline](../../quests/templates/native-personal-link/gq004-graph-baseline.json).
Tests check exact parity, branch ports, namespaces, retry retirement, inventory
verification, optional call/epilogue/repair, device settings and output isolation.
GQ004's compatibility adapters retain its existing root/finish guards exactly;
new template bindings use immediate completed-fact exits.

Access-point raw/binary snapshots are pinned in
[the donor catalog](../../quests/templates/donors/catalog.json). The binary is
derived from the playtested recovery controller. The neutral snapshot uses the
stock personal-link record and was round-tripped through WolvenKit to pin its
constructor defaults explicitly in raw source.
Builds read these template-owned snapshots, never the current GQ004 assets.
Donor files are compiler inputs and are not shipped as runtime dependencies.

Device conversion opts into `access_point_values` for these clones only. It
expands serializer-coalesced inline value handles while retaining typed values
and wrapper metadata, and rejects duplicate, cyclic or unresolved handles. The
shared build API accepts this adapter per artifact; other resources retain the
default strict shared-handle policy. Tests confirm that altered controller
values still fail comparison. This is the reusable equivalent of GQ004's
controller-specific readback handling.
