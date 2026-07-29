---
name: ghostline-wolvenkit-cr2w
description: Use for Ghostline CR2W/raw conversion and verification. Prefer the pinned ghostline-red submodule; use WolvenKit only for unsupported editor, mesh, or novel-layout work.
---

# Ghostline Native CR2W Workflow

## CLI Setup

Build the pinned submodule and generate the ignored schema when needed:

```powershell
git submodule update --init --recursive .\tools\ghostline-red
cargo build --release --manifest-path .\tools\ghostline-red\Cargo.toml
$red = '.\tools\ghostline-red\target\release\ghostline-red.exe'
& $red schema-generate .\WolvenKit .\red-schema.json
```

`tools/ghostline_red.py` centralizes these paths and generates the schema on
demand for Python generators.

## CR2W To Raw JSON

Use the native serializer and give the complete output filename:

```powershell
& $red cr2w-serialize `
  .\source\archive\mod\gq000\phases\gq000.questphase `
  .\source\raw\mod\gq000\phases\gq000.questphase.json `
  --schema .\red-schema.json
```

For reference world resources, use:

```powershell
.\tools\serialize_reference_world.ps1
```

The meeting scene and world resources are authored through checked-in specs.
Only serialize packed binaries back into `source/raw` when deliberately
importing an editor or runtime-tested binary change.

## Raw JSON To CR2W

Native writes are template-backed. Use the current packed resource as the
template and output target:

```powershell
& $red cr2w-deserialize `
  .\source\raw\mod\gq000\phases\gq000.questphase.json `
  .\source\archive\mod\gq000\phases\gq000.questphase `
  --template .\source\archive\mod\gq000\phases\gq000.questphase `
  --schema .\red-schema.json
```

The writer supports shifted strings and arrays, new CName/import entries,
typed world-node data, RedPackage buffer identity resolution, non-empty
RedPackage array growth, new chunks and nested handles backed by an existing
class template, null/shared handles, and handle/chunk index rebuilding.
Untouched template chunks and metadata are preserved.

Before writing a generated scene or world change, run its audit/dry-run,
validator, explorer checks, and the Python regression suite. A successful CR2W
conversion is not a substitute for graph, handle, NodeRef, or locStore
validation.

## Archive Operations

```powershell
& $red pack .\source\archive -o H:\Ghostline-builds\native-candidate
& $red archive-list H:\Ghostline-builds\native-candidate\archive.archive `
  --paths-root .\source\archive
& $red extract H:\Ghostline-builds\native-candidate\archive.archive `
  -o H:\Ghostline-builds\native-candidate\extracted `
  --paths-root .\source\archive
```

## WolvenKit Fallback Boundary

Keep WolvenKit for:

- the graphical CR2W, graph, scene, and Tweak Browser editors;
- mesh and morphtarget GLB import/export and garment-support rebuilding;
- creating a class layout that has no compatible binary template;
- authoring a non-empty array when the template has no element from which the
  native writer can derive its binary layout;
- comparison/oracle testing when investigating a new RED or Kraken format.

Do not use WolvenKit CLI for routine pack, extract, archive listing, reflected
CR2W serialization, or template-backed deserialization.

## Verification

- A CR2W binary starts with `CR2W`; verify with `Format-Hex -Count 4`.
- Raw CR2W-JSON begins with `{` and contains `Header` and `Data`.
- Compare exact round trips with `Get-FileHash`.
- Keep `Header.ArchiveFileName` pointed at the intended `source/archive`
  target.
- Follow `docs/workflows/build-and-package.md` for isolated pack/extract and
  payload verification.
