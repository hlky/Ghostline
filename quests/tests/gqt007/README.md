# GQT007 Barry Lipsync A/B

GQT007 is a runtime integration fixture for the localized dialogue-animation
round trip. It spawns vanilla `Character.mq010_barry`, injects Barry's vanilla
voice tag, and opens a repeatable two-option scene:

- **Play vanilla lipsync** selects `f_7D78942678897A4F`.
- **Play modified lipsync** selects `f_C39ACEAEFDC26A07`.

The two screenplay lines have distinct locstring IDs. GQT007 supplies its own
subtitle map and VO map, with both VO entries pointing to the same quest-owned
Wwise external-source conversion of Barry's vanilla **Who is it?** recording.
The matching animation names are derived from those IDs. The diagnostic modified clip forces both `jaw_mid_open` and the baked
`jaw_mid_openLipsyncPoseOutput` to `1.0`; it is intentionally exaggerated so
the result is unambiguous in game.

The scene points at a Ghostline-owned logical lipsync path. The corresponding
English localized asset is:

```text
source/archive/base/localization/en-us/lipsync/mod/gqt007/scenes/
  gqt007_barry_lipsync/civ_low_m_11_enus_40_fat.anims
```

This does not replace the vanilla Happy Together animset.

## Generate

```powershell
py .\quests\tests\gqt007\implementation\build.py
py .\quests\tests\gqt007\implementation\build.py --deserialize `
  --wolvenkit H:\WolvenKit.Console-8.17.4\WolvenKit.CLI.exe
```

The test site is centred at `(-1068.2563, 1313.9362, 5.174843)`, a short
distance east of the existing GQT005 outdoor test site. The registered quest
adds a **Barry lipsync test** mappin. Entering the 12-metre setup trigger
activates Barry's community, waits for him to spawn, and starts the choice
scene.

## Rebuild The Comparison Animset

Export the vanilla Barry animset through WolvenKit, then duplicate and alter
the target clip:

```powershell
py .\tools\make_lipsync_ab_glb.py `
  .\export\civ_low_m_11_enus_40_fat.anims.glb `
  .\rebuild\stage-one.glb `
  --source f_1897CF05B3627000 `
  --name f_7D78942678897A4F `
  --copy-only

py .\tools\make_lipsync_ab_glb.py `
  .\rebuild\stage-one.glb `
  .\rebuild\civ_low_m_11_enus_40_fat.anims.glb `
  --source f_1897CF05B3627000 `
  --name f_C39ACEAEFDC26A07 `
  --track '^(jaw_mid_open|jaw_mid_openLipsyncPoseOutput)$' `
  --value 1.0
```

Place a copy of the original `.anims` in `rebuild` beside the modified GLB,
build `tools/WolvenKit.AnimImport`, and import it with the installed game root
so WolvenKit can resolve Barry's facial rig:

```powershell
dotnet build .\tools\WolvenKit.AnimImport\WolvenKit.AnimImport.csproj -c Release
& .\tools\WolvenKit.AnimImport\bin\Release\net8.0\WolvenKit.AnimImport.exe `
  'H:\Cyberpunk 2077' `
  '.\rebuild\civ_low_m_11_enus_40_fat.anims.glb' `
  '.\rebuild'
```

Re-export the rebuilt `.anims` and inspect both clips before copying it into
the localized source path.
