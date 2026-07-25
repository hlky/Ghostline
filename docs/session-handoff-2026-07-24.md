# Ghostline session handoff — 2026-07-24

## Immediate status

The active task is runtime validation of the second building-block harness:
`gqt004_vehicle_lab`.

The latest candidate is packed and installed:

```text
Build:
H:\Ghostline-builds\gqt004-scalar-fix-20260724-233038\archive.archive

Installed:
H:\Cyberpunk 2077\archive\pc\mod\Ghostline.archive

SHA-256:
B5C9527AEAC233D3D9885B276E4898EE67114CA0FBDE3A7EBC57413EC06AB04A

Previous-install backup:
H:\Ghostline-backups\pre-gqt004-scalar-fix-20260724-233038
```

The user has not tested this latest scalar-fix build yet. The next action is to
ask for or receive that runtime result.

Expected behavior on save load:

1. Quest `Vehicle Lab` activates immediately.
2. Journal/tracker shows the first objective to enter the contact vehicle.
3. The contact vehicle, theft vehicle, and Patch are placed in the Kabuki test
   area.

The first placement pass is deliberately provisional. Expect to adjust vehicle
position, orientation, road/nav placement, triggers, Patch placement, or
vehicle lifecycle behavior after the test.

## Why the preceding builds failed

### First candidate: crash on save load

Bad build:

```text
H:\Ghostline-builds\gqt004-20260724-230339\archive.archive
SHA-256 355C442781509F69B61745AF0889CDD32EEA825BA0E480AAD97A8DAF2CCE90BE
```

It crashed reproducibly:

```text
C:\Users\user\AppData\Local\REDEngine\ReportQueue\Cyberpunk2077-20260724-231359-25132-23564
C:\Users\user\AppData\Local\REDEngine\ReportQueue\Cyberpunk2077-20260724-231503-28748-1336
```

Both were `EXCEPTION_ACCESS_VIOLATION`, reading
`0xFFFFFFFFFFFFFFFF`.

Serializing the successful `ghostline-red` outputs back to JSON revealed
silent topology loss:

- the seven-stage root retained only four phase nodes;
- `gqt004_ride_with_patch` omitted the newly added vehicle assignment node;
- `gqt004_always_loaded.streamingsector` omitted both named vehicle spawn-set
  mappings.

The root, ride phase, quest sector, always-loaded sector, and streaming block
were rebuilt with WolvenKit. That stopped the load crash.

### Crash-fix candidate: no quest or vehicles

Crash-fix build:

```text
H:\Ghostline-builds\gqt004-crashfix-20260724-231914\archive.archive
SHA-256 BA94F1F88E91DA2E5C1E15D956E1AE867048029F4894C65F0A7B6DA6403436C1
```

It loaded, but the user saw no quest in the Journal and no vehicles.

ArchiveXL logs confirmed that all registrations merged:

- `mod\gqt004\journal\gqt004.journal`
- `mod\gqt004_vehicle_lab\phases\gqt004_vehicle_lab.questphase`
- `mod\gqt004\world\gqt004_vehicle_lab.streamingblock`

The packed first child phase nevertheless still contained literal template
tokens:

```text
{{objective}}
{{vehicle}}
```

Six packed child phases contained combinations of:

```text
{{objective}}
{{vehicle}}
{{destination_1}}
{{completion_fact}}
{{player_vehicle_record}}
```

Their authored `source/raw` JSON was correct. `ghostline-red` had again
returned success while retaining template values inside the packed
`RedPackage`.

Those six phases were rebuilt with WolvenKit:

```text
gqt004_enter_contact_vehicle.questphase
gqt004_drive_contact_to_destination.questphase
gqt004_cleanup_contact_vehicle.questphase
gqt004_steal_test_vehicle.questphase
gqt004_deliver_test_vehicle.questphase
gqt004_cleanup_test_vehicle.questphase
```

`gqt004_ride_with_patch.questphase` had already been rebuilt correctly.

All seven production child phases now serialize with no unresolved template
tokens. The complete Python suite passes: 181 tests.

## ghostline-red handoff

The detailed upstream handoff is:

```text
docs/ghostline-red-topology-handoff.md
```

It documents:

- exact bad and corrected archive fixtures;
- three topology-loss cases;
- the separate scalar-placeholder retention case;
- reproduction commands;
- expected fail-loudly behavior;
- semantic post-write verification;
- acceptance tests.

The user is taking that handoff to `hlky/ghostline-red` and will report when
the writer is fixed.

Until then:

- `ghostline-red` is fine for pack/extract/list and ordinary verified work;
- never trust a successful template-backed CR2W write without serializing it
  back and comparing semantic structure and values;
- use WolvenKit for GQT004 CR2W writes that grow topology or bind
  `RedPackage` template values.

## GQT004 sources

Primary authored inputs:

```text
source/quests/tests/gqt004_vehicle_lab.quest.json
tools/gqt004_vehicle_lab.world.json
tools/generate_gqt004_content.py
source/resources/r6/tweaks/ghostline/gqt004_vehicles.yaml
```

Generated raw resources:

```text
source/raw/mod/gqt004_vehicle_lab/
source/raw/mod/gqt004/
```

Packed resources:

```text
source/archive/mod/gqt004_vehicle_lab/
source/archive/mod/gqt004/
```

Registrations:

```text
source/resources/Ghostline.archive.xl
```

The typed flow is:

```text
enter contact vehicle
-> assign/mount Patch and ride with contact
-> drive contact vehicle to destination
-> clean up contact vehicle
-> steal designated test vehicle
-> deliver designated vehicle
-> final cleanup and quest success
```

World spec:

- prefab root: `$/mod/gqt004/#gqt004_pr_vehicle_lab`;
- ride vehicle: `#gqt004_ride_vehicle`;
- theft vehicle: `#gqt004_theft_vehicle`;
- contact community: `#gqt004_com_contact`;
- all three communities are `active_on_start: 1`;
- both vehicles currently derive from
  `Vehicle.v_sport2_porsche_911turbo_player`.

## Completed preceding fixture

`gqt001_signal_delay` is runtime-proven:

- Ghostline-owned laptop appears and is usable;
- only the Files tab is shown;
- the `SIGNAL DELAY` file appears;
- opening the file progresses the quest;
- the delay and Patch phone conversation work;
- the final phone response now succeeds the Journal quest.

Important computer-authoring discovery:

- a working SQ021-derived laptop needs the complete controller package;
- the `ComputerControllerPS` component binds through CRUID
  `1131680419258347532`;
- the scanner binds through CRUID `1131680419258347552`;
- changing these CRUIDs makes the visible device fall back to empty entity
  template content;
- multiple laptops are possible, but each instantiated entity must preserve
  the correct component CRUID contract while using distinct world identity and
  persistent NodeRefs.

Full reference:

```text
docs/vanilla-sq021-computer-flow.md
```

## Test-suite sequence

The planned building-block harnesses are:

```text
gqt001_signal_delay       complete/runtime-proven
gqt004_vehicle_lab        installed; latest fix awaiting runtime test
gqt003_extract_and_hold   not yet implemented as a playable test
gqt002_quiet_install      not yet implemented as a playable test
```

After GQT004 is runtime-correct, continue in this order:

1. `gqt003_extract_and_hold`
2. `gqt002_quiet_install`

The stealth harness is last because it requires a compound phase running
`stealth_monitor` in parallel with `plant_item`.

## Repository and Git state

Current branch:

```text
main
```

Current HEAD and remote:

```text
0161b13 (HEAD -> main, origin/main) Add reusable quest blocks and Signal Delay test
```

The worktree is intentionally dirty. It contains both staged prior tooling
conversion work and unstaged/new GQT004 work. Do not reset, discard, or
blindly restage it.

Notable current status:

```text
M  .gitignore
M  .gitmodules
MM ROADMAP.md
M  agent/skills/ghostline-wolvenkit-cr2w/SKILL.md
M  docs/packaging.md
M  docs/tooling.md
 M source/raw/mod/ghostline/quest_blocks/templates/ride_with_contact.questphase.json
 M source/resources/Ghostline.archive.xl
 M tools/generate_advanced_quest_block_templates.py
M  tools/generate_dialogue_localization.py
M  tools/generate_gq001_content.py
M  tools/generate_gq002_content.py
M  tools/generate_gqt001_content.py
M  tools/generate_scene.py
MM tools/generate_world.py
Am tools/ghostline-red
A  tools/ghostline_red.py
M  tools/serialize_reference_world.ps1
M  tools/world_asset_catalog.py
?? docs/ghostline-red-topology-handoff.md
?? source/archive/mod/gqt004/
?? source/archive/mod/gqt004_vehicle_lab/
?? source/quests/tests/gqt004_vehicle_lab.quest.json
?? source/raw/mod/gqt004/
?? source/raw/mod/gqt004_vehicle_lab/
?? source/resources/r6/tweaks/ghostline/gqt004_vehicles.yaml
?? tools/generate_gqt004_content.py
?? tools/gqt004_vehicle_lab.world.json
```

This session did not commit or push GQT004.

## Useful verification commands

Run the complete test suite:

```powershell
Set-Location 'H:\projects\Ghostline'
py -B -m unittest discover -s tests -v
```

Inspect the root:

```powershell
py -B tools/explore_questphase.py `
  -f source/raw/mod/gqt004_vehicle_lab/phases/gqt004_vehicle_lab.questphase.json `
  summary
```

Check source binaries for unresolved template tokens:

```powershell
rg -a -n '\{\{' `
  source/archive/mod/gqt004/phases `
  source/archive/mod/gqt004_vehicle_lab/phases
```

The production paths should produce no matches. The checked template under
`source/archive/mod/gqt004/templates` intentionally retains placeholders and
must not be included in that check.

Confirm the installed archive:

```powershell
Get-FileHash -Algorithm SHA256 `
  'H:\Cyberpunk 2077\archive\pc\mod\Ghostline.archive'
```

Expected:

```text
B5C9527AEAC233D3D9885B276E4898EE67114CA0FBDE3A7EBC57413EC06AB04A
```

## Next-session first response

If the user reports the GQT004 test result, address that result directly.

If the quest and vehicles now appear:

1. record exact placement/lifecycle problems;
2. fix only the relevant raw spec/manifest/generator;
3. use WolvenKit for affected CR2W writes until `ghostline-red` is fixed;
4. serialize every packed output back and compare it;
5. run all tests, pack, install, update `ROADMAP.md`.

If the quest or vehicles are still absent:

1. inspect fresh ArchiveXL, TweakXL, and REDscript logs;
2. inspect quest facts/current quest state if possible;
3. serialize the installed archive's GQT004 root, child phases, journal, block,
   and sectors rather than assuming `source/archive` matches;
4. verify that the save has not persisted a stale test-quest state;
5. compare the runtime-proven GQT001 root activation pattern again.
