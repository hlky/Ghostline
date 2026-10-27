# Building workstations and quest bindings

The Building Lab exports native office fixtures alongside the architectural
shell. AKPP Logistics is the first fixture: desk, chair, a generic worker in
an infinite static chair workspot, and a native Computer device. It is a
reusable encounter component, not a complete story quest.

## Authoring and placement

`layout.workstations` names placed `desk` and `chair` module IDs. The curated
prop catalogue is `reference/world/building-props-catalog.json`; records carry
measured bounds, source/preview hashes and a desk/chair type contract.

The actor's `record`, `appearance`, `workspot`, `active_on_start`, `offset` and
`yaw_offset` configure the community. Actor placement follows the chair.
The computer's offset and yaw offset follow the desk. Offsets are rotated in
the parent's local frame. References and the read fact remain stable when
furniture moves. The worker can later be replaced with an office manager by
changing both the record and its matching root entity appearance mapping.

The editor's **Quest workstation** panel edits the worker binding and initial
activation. **Quest block bindings** shows exact community, entry, phase,
workspot, computer and completion fact values. Plan markers show the seat
anchor; they are not a skeletal animation preview. Furniture and terminal
geometry use neutral preview materials.

For AKPP, `Character.WorkerSpecialistMale` exists in the installed base TweakDB;
its entity contains `service__worker_ma_generic_worker_01`. The chair workspot
is `base\workspots\common\chair\generic__sit_chair__sit_around__01.workspot`.
The computer uses `computer_1.ent` / `computer_computer_1`. Its root is at the
screen centre; the fixture offsets it 1.011 m above the desk's floor anchor
and rotates it 90 degrees so its screen faces the worker. Monitor geometry
bottom clears the desk top. Final seated alignment still needs a live check.

## Native export and quest ownership

The existing world generator supplies the AI spot, compiled community area,
always-loaded community registry and an office-area trigger.
The fixture sector must use `Exterior`, level 0, with a zero descriptor
`questPrefabNodeRef`, because the building has no quest enabling a prefab.
The shared world generator's default `Quest` sector (level 255) is suitable
for quest-owned activation and must be adapted for standalone building fixtures.
The always-loaded registry alone cannot make an unloaded AI spot or computer
appear. The descriptor bounds include all fixture placements with 80 m padding.

A separate sparse
ComputerControllerPS registry is patched into Night City's global device
registry. The fixture strips all old donor emails, files, facts and device
connections. Its single test document sets a fixture-owned read fact.

Exports also contain:

- `quest-bindings.json`: exact native identities and activation defaults.
- `quest-block-fragment.json`: actor bindings, area trigger, terminal stage
  fields and cleanup communities for an owning quest.

The fragment's terminal stage uses the existing `read_terminal_document`
block. The owning quest must supply its phase path, objective/journal entry,
activation, transitions and completion lifecycle. Regression tests compile
that block using the generated computer reference/read fact. An offline block
build does not prove the terminal emits its fact in game.

For an encounter owned by a quest, disable `active_on_start`, activate the
community through the quest's lifecycle, and wait for CharacterSpawned before
starting a scene. Acquire entry `worker` in phase `default`; keep the exported
community identity stable. The owning quest controls deferral, return, death,
save/load and community cleanup. Initial-state edits do not replace an
explicit migration/cleanup policy for an already-running quest.

The first fixture spawns directly into its assigned chair spot. It does not
claim live NPC walking/navigation through the office or out to the street;
native navigation export remains disabled. The 5 cm office floor cap and
retained street geometry remain as authored.

## Playtest route

Use the named package and an existing city save at AKPP. Walk inside and check
that exactly one generic worker appears seated at the chair, facing the desk,
without sinking, floating or intersecting the table. Leave the area and return,
then save/load to check duplication and persistence. Approach the terminal,
open its desktop and read **Office workstation test**. Confirm the native fact
`akpp_logistics_open_shell_office_file_read` changes through the quest system.
Check door swing, entry step, street pavement and the retained Ru Lai boundary.
Record those as separate live results against the installation receipt.
