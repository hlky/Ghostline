# ghostline-red Topology-Write Handoff

## Summary

`ghostline-red cr2w-deserialize` can currently return success while silently
retaining the smaller topology of its binary template. The resulting CR2W is
syntactically readable, but authored graph nodes or world-buffer entries are
missing.

This was discovered while generating `gqt004_vehicle_lab`. The first native
candidate crashed Cyberpunk 2077 reproducibly while loading a save:

- `C:\Users\user\AppData\Local\REDEngine\ReportQueue\Cyberpunk2077-20260724-231359-25132-23564`
- `C:\Users\user\AppData\Local\REDEngine\ReportQueue\Cyberpunk2077-20260724-231503-28748-1336`

Both reports contain the same `EXCEPTION_ACCESS_VIOLATION (0xC0000005)`,
reading `0xFFFFFFFFFFFFFFFF`. ArchiveXL, TweakXL, and REDscript loaded the
registered GQT004 resources without reporting an authoring error.

The affected native command did not fail. Only serializing its output back to
JSON exposed that the requested topology had not been written.

## Environment

- Ghostline repository: `H:\projects\Ghostline`
- ghostline-red submodule: `H:\projects\Ghostline\tools\ghostline-red`
- Schema: `H:\projects\Ghostline\red-schema.json`
- WolvenKit oracle: `H:\projects\Ghostline\WolvenKit`
- Bad native archive:
  `H:\Ghostline-builds\gqt004-20260724-230339\archive.archive`
- Bad archive SHA-256:
  `355C442781509F69B61745AF0889CDD32EEA825BA0E480AAD97A8DAF2CCE90BE`
- Corrected archive:
  `H:\Ghostline-builds\gqt004-crashfix-20260724-231914\archive.archive`
- Corrected archive SHA-256:
  `BA94F1F88E91DA2E5C1E15D956E1AE867048029F4894C65F0A7B6DA6403436C1`

The checked-in `source/raw` files are the authored JSON inputs. The current
`source/archive` GQT004 binaries were rebuilt with WolvenKit and are useful as
the correct-output oracle.

## Reproduction 1: root quest graph loses phase nodes

Input:

```text
source\raw\mod\gqt004_vehicle_lab\phases\gqt004_vehicle_lab.questphase.json
```

The authored root contains:

- one input node;
- one output node;
- seven `questPhaseNodeDefinition` stage nodes.

Expected total: nine graph nodes, including seven phase nodes.

The template originally used by generation was copied from:

```text
source\archive\mod\gqt001_signal_delay\phases\gqt001_signal_delay.questphase
```

After a successful native write and serialize-back, the result contained only
four `questPhaseNodeDefinition` nodes. Three authored stages were silently
missing.

## Reproduction 2: ride phase loses a newly added assignment node

Input:

```text
source\raw\mod\gqt004\phases\gqt004_ride_with_patch.questphase.json
```

Template:

```text
source\archive\mod\ghostline\quest_blocks\templates\ride_with_contact.questphase
```

Expected graph: eight nodes, including the added vehicle-character assignment
operation represented by `questVehicleNodeDefinition` with
`questAssignCharacter_NodeType`.

After a successful native write and serialize-back, the result contained seven
nodes and omitted that assignment node.

## Reproduction 3: world sector loses spawn-set mappings

Input:

```text
source\raw\mod\gqt004\world\gqt004_always_loaded.streamingsector.json
```

The authored sector contains three community registries and two
`gameCommunitySpawnSetNameToIDEntry` mappings:

```text
#gqt004_ride_vehicle
#gqt004_theft_vehicle
```

The template was based on the smaller GQT001 always-loaded sector.

After a successful native write and serialize-back, the result contained no
named spawn-set mappings. This demonstrates that the issue is not limited to
quest graph node arrays; it also affects topology growth in typed world-node
buffers.

## Reproduction 4: bound RedPackage scalar values remain placeholders

After the topology-corrected candidate loaded without crashing, GQT004 still
did not appear in the Journal and neither vehicle appeared. Serializing the
packed child phases exposed a second silent-write mode: the CLI had returned
success while retaining literal template strings instead of the bound values
present in authored JSON.

Affected packed phases included:

```text
mod\gqt004\phases\gqt004_enter_contact_vehicle.questphase
mod\gqt004\phases\gqt004_drive_contact_to_destination.questphase
mod\gqt004\phases\gqt004_cleanup_contact_vehicle.questphase
mod\gqt004\phases\gqt004_steal_test_vehicle.questphase
mod\gqt004\phases\gqt004_deliver_test_vehicle.questphase
mod\gqt004\phases\gqt004_cleanup_test_vehicle.questphase
```

The serialized packed output still contained combinations of:

```text
{{objective}}
{{vehicle}}
{{destination_1}}
{{completion_fact}}
{{player_vehicle_record}}
```

For example, authored
`gqt004_enter_contact_vehicle.questphase.json` contains:

```text
quests/minor_quest/gqt004/gqt004_01/gqt004_01_obj_enter_vehicle
#gqt004_ride_vehicle
```

but the successful native binary serialized back as `{{objective}}` and
`{{vehicle}}`. The first child consequently could not activate a valid journal
objective or resolve its designated vehicle.

Rebuilding those six resources with WolvenKit preserved the authored values.
The resulting installed candidate is:

```text
H:\Ghostline-builds\gqt004-scalar-fix-20260724-233038\archive.archive
SHA-256 B5C9527AEAC233D3D9885B276E4898EE67114CA0FBDE3A7EBC57413EC06AB04A
```

This case must be covered independently of array/topology growth: a write that
does not change the graph shape can still silently retain template scalar
payloads inside a `RedPackage`.

## Minimal command-level reproduction

Build the current submodule and schema:

```powershell
Set-Location 'H:\projects\Ghostline'

cargo build --release --manifest-path `
  '.\tools\ghostline-red\Cargo.toml'

$red = '.\tools\ghostline-red\target\release\ghostline-red.exe'

& $red schema-generate `
  '.\WolvenKit' `
  '.\red-schema.json'
```

Use an isolated output directory. Do not overwrite the current WolvenKit-built
oracle:

```powershell
$repro = 'H:\Ghostline-audits\ghostline-red-topology-repro'
New-Item -ItemType Directory -Force $repro | Out-Null

& $red cr2w-deserialize `
  '.\source\raw\mod\gqt004_vehicle_lab\phases\gqt004_vehicle_lab.questphase.json' `
  (Join-Path $repro 'root.questphase') `
  --template `
  '.\source\archive\mod\gqt001_signal_delay\phases\gqt001_signal_delay.questphase' `
  --schema '.\red-schema.json'

& $red cr2w-serialize `
  (Join-Path $repro 'root.questphase') `
  (Join-Path $repro 'root.roundtrip.json') `
  --schema '.\red-schema.json'
```

Repeat for the ride phase:

```powershell
& $red cr2w-deserialize `
  '.\source\raw\mod\gqt004\phases\gqt004_ride_with_patch.questphase.json' `
  (Join-Path $repro 'ride.questphase') `
  --template `
  '.\source\archive\mod\ghostline\quest_blocks\templates\ride_with_contact.questphase' `
  --schema '.\.red-schema.json'

& $red cr2w-serialize `
  (Join-Path $repro 'ride.questphase') `
  (Join-Path $repro 'ride.roundtrip.json') `
  --schema '.\.red-schema.json'
```

Extract the original bad archive to recover the exact smaller templates used
by the first native generation:

```powershell
& $red extract `
  'H:\Ghostline-builds\gqt004-20260724-230339\archive.archive' `
  -o (Join-Path $repro 'bad-extracted') `
  --paths-root '.\source\archive'
```

Then repeat the write using each bad resource as its own known-truncated
template. For the always-loaded sector:

```powershell
& $red cr2w-deserialize `
  '.\source\raw\mod\gqt004\world\gqt004_always_loaded.streamingsector.json' `
  (Join-Path $repro 'always_loaded.streamingsector') `
  --template `
  (Join-Path $repro 'bad-extracted\mod\gqt004\world\gqt004_always_loaded.streamingsector') `
  --schema '.\red-schema.json'

& $red cr2w-serialize `
  (Join-Path $repro 'always_loaded.streamingsector') `
  (Join-Path $repro 'always_loaded.roundtrip.json') `
  --schema '.\red-schema.json'
```

The same exact-template method can be applied to the root and ride resources:

```powershell
--template (Join-Path $repro `
  'bad-extracted\mod\gqt004_vehicle_lab\phases\gqt004_vehicle_lab.questphase')

--template (Join-Path $repro `
  'bad-extracted\mod\gqt004\phases\gqt004_ride_with_patch.questphase')
```

Serialize the three extracted resources and compare them with the authored
`source/raw` files and current corrected `source/archive` binaries.

## Expected behavior

One of the following is acceptable:

1. Write the complete authored topology, including all newly appended graph
   nodes, exports, handles, registries, and typed buffer entries.
2. Reject the operation with a precise nonzero error identifying the first
   unsupported structural change.

Returning success with a structurally smaller result is not acceptable.

At minimum, `cr2w-deserialize` should verify its own output before returning
success:

- serialize the produced CR2W back into the same reflected model;
- compare topology-bearing arrays and handle/export identities against the
  requested JSON;
- report missing, duplicated, reordered, or aliased entries;
- delete or clearly mark the invalid output on verification failure.

Byte equality is not expected after an intentional edit, but semantic
topology equality is required.

## Likely implementation area

The failure pattern suggests that template-backed collection reconstruction
still uses the template's original cardinality or object graph in some paths.
Audit all code paths that:

- grow handle arrays;
- allocate new exports from a class exemplar;
- rebuild `HandleId` / `HandleRefId` relationships;
- write nested `RedPackage` chunks;
- write typed world-node buffers;
- preserve unknown template data while replacing known reflected values.

The writer already handles many topology-growth cases. The important question
is why unsupported growth can fall through to a successful write that retains
only the template subset.

## Relation to the earlier journal limitation

This is related to, but more serious than, the earlier explicit error:

```text
unsupported template-backed write: conflicting handle data
```

The journal-array expansion that originally triggered that error has since
been improved. A separate journal-completion cleanup case may still lack a
compatible class-layout exemplar.

The GQT004 issue documented here is different because the CLI reports success.
Any fix should therefore add regression tests for both:

- supported topology growth produces the complete requested structure;
- unsupported topology growth fails loudly and never emits a silently
  truncated resource.

## Acceptance tests

Add fixtures or integration tests that assert:

1. The GQT004 root round-trip has nine graph nodes and seven phase nodes.
2. The ride phase round-trip has eight nodes and retains
   `questAssignCharacter_NodeType`.
3. The always-loaded sector retains all three registries and both named
   spawn-set mappings.
4. Every `HandleRefId` resolves to exactly one compatible `HandleId`.
5. No authored graph socket connection points to an omitted node.
6. The CLI exits nonzero if any requested topology cannot be represented.
7. The generated resources can be independently serialized by WolvenKit.
8. No serialized production output contains unresolved `{{...}}` template
   tokens unless those exact strings were explicitly requested by the input.
9. Every changed reflected scalar in the requested JSON equals the
   corresponding value in serialized output.

The corrected WolvenKit-built resources under `source/archive` satisfy the
first three structural expectations and produced the installed crash-fix
candidate.
