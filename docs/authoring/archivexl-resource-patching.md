# ArchiveXL World Resource Patching

This is a focused authoring note, not the general packaging guide.

> Status: experimental and not installed. Runtime teardown testing proved that
> assigning or raw-copying an existing device's `RedPackage` instance-data
> buffer is unsafe and causes exit-time DEP crashes. GQT001 currently uses a
> Ghostline-owned laptop sector with official ArchiveXL 1.27.0.

Ghostline's `read_terminal_document` test uses an existing Kabuki laptop. The
selected `worldEntityNode` stores its authoritative `ComputerControllerPS` in
the outer sector's `instanceData`:

```text
base\worlds\03_night_city\_compiled\default\exterior_-18_28_0_0.streamingsector
```

Replacing either the full sector or its embedded laptop template is too broad.
The local ArchiveXL extension therefore supports an instance-specific sector
patch in addition to its reusable inplace-resource merger.

## Instance-specific extension

For `worldStreamingSector` patches with `props: [instanceData]`, the extension
runs after sector `PostLoad`, matches patch nodes to target nodes by compiled
`globalNodeID`, and replaces only the matching `worldEntityNode.instanceData`.
The patch sector may therefore contain a single node.

```yaml
resource:
  patch:
    mod\gqt001\world\gqt001_laptop_instance.streamingsector:
      props:
      - instanceData
      targets:
      - base\worlds\03_night_city\_compiled\default\exterior_-18_28_0_0.streamingsector
```

`source/raw/mod/gqt001/world/gqt001_laptop_instance.streamingsector.json`
contains the selected node, its original NodeRef/transform identity, and a
replacement `ComputerControllerPS` with the SIGNAL DELAY file. It does not
replace the laptop entity template or any other node.

## Inplace-resource extension

The local ArchiveXL extension in
`tools/archive-xl/inplace-resource-patching.patch` also adds a type-specific
`inplaceResources` merger. It remains useful when an embedded resource itself
is the intended patch target, but GQT001 no longer uses it. For each embedded
resource in the patch:

1. Match the target's embedded `Ref<CResource>` by depot path.
2. Replace the matching reference, preserving the patch resource's embedded
   token and content.
3. Append the reference when no matching depot path exists.

This is embedded-resource replacement, not field-level merging. Multiple
patches compose when they target different embedded depot paths. If multiple
patches replace the same embedded path, normal ArchiveXL patch order applies.

Do not restore the full base-path override under `source/archive/base/worlds`.

## Local Build

The tested source base is ArchiveXL 1.27.0. After cloning with submodules:

```powershell
$env:CC = 'cl.exe'
$env:CXX = 'cl.exe'
xmake f -m releasedbg -y
xmake -y
```

The explicit compiler selection is required on the current development
machine because its global `CC` and `CXX` point to LLVM while the dependency
recipes pass MSVC flags.

The official 1.27.0 DLL backup is retained under
`H:\Ghostline-backups\ArchiveXL-1.27.0-official-20260724`, the previous 1.26.2
install is retained separately, and the local extension build is retained under
`H:\Ghostline-builds\archivexl-inplace-patch-20260724` (SHA-256
`DD6CE8A76E7321DE1B430F3B4A4DED28836DCDF3B5D73BB83B4FE584E9F868FC`).
