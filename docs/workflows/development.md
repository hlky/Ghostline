# Development Workflow

Ghostline has several authoring pipelines rather than one global regeneration
command. Start from the owning quest README or authoring guide and run only the
generators for the resources you changed.

## 1. Choose The Source Of Truth

| Change | Edit |
| --- | --- |
| Quest structure or story | `quests/story/ghostline/gq###` |
| Character design | `characters` |
| Braindance performance | `braindance` |
| Existing packed CR2W resource | Matching JSON under `source/raw` |
| ArchiveXL, TweakXL, REDscript, or config | `source/resources` |

Never text-edit CR2W binaries under `source/archive`.

## 2. Generate And Inspect

Use the command in the owning quest README or authoring guide. Before opening a
large CR2W-JSON document, use the focused explorers listed in the
[tool catalog](../reference/tool-catalog.md).

Generators should write authored CR2W-JSON to `source/raw` or isolated output
to `converted`/`.tmp`. Do not promote isolated output into shipping source
without review.

## 3. Test

Run the focused tests named by the owning guide, then the repository gate:

```powershell
py -B -m unittest discover -s tests -v
```

See [automated testing](automated-testing.md) for narrower commands and test
ownership.

## 4. Convert CR2W-JSON

Use the pinned native `ghostline-red` workflow for supported template-backed
resources. Use WolvenKit for editor work, meshes, morphtargets, unsupported
layouts, or oracle comparison.

Build the native tool and schema when needed:

```powershell
git submodule update --init --recursive .\tools\ghostline-red
cargo build --release --manifest-path .\tools\ghostline-red\Cargo.toml
$red = '.\tools\ghostline-red\target\release\ghostline-red.exe'
& $red schema-generate .\WolvenKit .\red-schema.json
```

Before writing a generated scene or world resource, run its audit or dry run,
validator, focused explorer checks, and tests. Successful serialization alone
does not validate graph topology, NodeRefs, handles, or localization.

## 5. Package And Install

Follow [build, package, and install](build-and-package.md). In particular:

- pack only `source/archive`;
- verify the resulting archive by listing and extracting it;
- stage `source/resources` separately;
- do not treat `packed` as authored source.

## 6. Record Runtime Evidence

Install on the intended dependency baseline, test from a suitable clean save,
and record exact results in [runtime testing](runtime-testing.md). Keep dated
investigation detail out of the current workflow unless it changes an active
rule.
