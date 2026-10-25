# Heartbreaker Protocol native prototype

Independent WolvenKit project, game-data baseline **Cyberpunk 2077 2.31**.
Runtime dependencies: RED4ext, ArchiveXL and TweakXL compatible with your game.
The native ZIP contains no Lua or REDscript. CET is optional for testing.

## What is built

- **NPC quickhack:** `Items.GhostlineHeartbreakerProtocol`, based on Reboot
  Optics. It applies six seconds of native blindness and a pink holographic
  heart cluster attached to the target's Head slot.
- **V presentation:** transparent screen particles draw twelve pink hearts by
  default, with configurable rows, columns and screen scale.
  `Items.GhostlineHeartbreakerSelfTest` is a consumable that applies the same
  native status to V through the inventory action.
- **Motion:** eight native texture tracks loop over 0.8 seconds. Individual
  pixel-art hearts bob, sway and pulse at different phases, with brief displaced
  horizontal strips and small pixel accents. The NPC cluster uses six hearts
  with varied sizes. Motion is baked into authored frames; the native timeline
  plays them without a runtime script.
- **Outro:** twelve native texture tracks scatter the heart pixels and fade
  them away over 0.6 seconds after the effect loop breaks. These are authored
  frame sequences, rather than independently simulated fragment particles.
- **Sound:** the existing one-shot `ui_fx_hacking_glitch_fullscreen_low` event
  plays at the start of the outro. No replacement audio bank is needed.
- **Registration:** a separately named effect spawner is appended to 14 V
  templates (including the EP1 FPP/TPP variants) and 128 regular human NPC
  templates, plus an optional patch for the installed Goth Baddie custom entity.
  Vanilla status-effect components are retained. Other story-specific NPCs,
  bosses, robots and lightweight crowds are outside this target list.
- **Acquisition:** native vendor stock is appended to
  `Vendors.wat_lch_netrunner_01` (Little China); vendor inventory refresh and
  actual availability must be checked in game. The CET helper can give the
  items directly to avoid waiting on vendor stock.

The V self-test exercises the incoming visual presentation. This prototype
does not assign the new hack to enemy AI. The quickhack keeps vanilla upload,
RAM cost and ordinary human targeting behavior; spread and boss/chimera
variants are omitted for this fixed-tier test.

## Rebuild and verify

Run from the repository root with the configured WolvenKit and native toolchain:

```powershell
.venv/Scripts/python.exe projects/experiments/heartbreaker/implementation/build.py
.venv/Scripts/python.exe projects/experiments/heartbreaker/implementation/verify.py
.venv/Scripts/python.exe tools/check_project.py
.venv/Scripts/python.exe tools/package_project.py --project heartbreaker
```

`heartbreaker.fx.json` owns the glyph seed, pink tint, brightness, opacity,
timing, motion amplitude, density, screen/billboard sizes and donor paths.
Change these authoring settings and rebuild to tune them; they are not live
game settings. `v_columns` and `v_rows` set V's heart count (their product).
`source/raw` contains the authored CR2W-JSON and PNG inputs. Donor hashes and
provenance are under `implementation/donors`; a changed cooked particle buffer
fails instead of guessing its offsets. WolvenKit serializes the new particle, effect and entity layouts, imports
textures and packs the final archive. The pinned native writer produced invalid
material import indices on a read-back check for these new resources; the
prototype therefore uses WolvenKit writes and native round-trip reads.

The verifier reads every compiled resource back into CR2W-JSON and checks
event RUID placement bindings, cooked particle sizes/lifetimes, renderer types,
material tint, texture references, outro timing, localization and package
dependency closure. Tweak field names are checked case-sensitively against the
WolvenKit type definitions, including inherited record fields. Package
verification separately lists/extracts the archive,
compares payload hashes and checks all ZIP entries against the install tree.

WolvenKit 8.17.4's folder importer reports exit 3 even on complete success due
to an inverted boolean in `ImportTaskInner`. The build accepts that code only
with the exact complete import count (currently `Imported 42/42 file(s)`) and
verifies every produced XBM.

## Optional CET test harness

After installing the native ZIP, copy the **folder**
`testing/cet/heartbreaker_test` to
`Cyberpunk 2077/bin/x64/plugins/cyber_engine_tweaks/mods/heartbreaker_test`.
Reload CET mods or restart, then assign its four hotkeys in CET's Bindings tab:

1. **Give items:** adds the quickhack and ten optical self-test consumables.
2. **Apply to V:** triggers the two native status records on V directly.
3. **Apply to looked-at NPC:** triggers the same records on the human NPC under
   your crosshair. Use a normal gang member for the first world-effect test.
4. **Clear:** removes only Heartbreaker statuses from V and the last tested
   target, to exercise early cancellation and the native outro.

The helper prints whether the native Heartbreaker spawner is present, the
runtime VFX array length, and whether the status system accepted each application. A
successful application is not proof that a missing effect spawner rendered.
It does not define TweakDB records, replace assets or render the hearts itself.
Remove the helper folder after testing; the native package does not need it.

## Runtime acceptance checks

**Offline verification is not in-game validation.** Check these on the exact
candidate whose package receipt you retain:

1. Confirm both item names/descriptions resolve and equip the quickhack in a
   cyberdeck. Use it through the scanner on a supported hostile NPC.
2. Confirm blindness lasts about six seconds, the pink cluster follows the
   NPC's head, and hearts break into pixels once when the status ends.
3. Consume a self-test on V. Confirm a transparent pink screen overlay and a
   clean return to vision after the breakup; test both body variants.
4. Listen for the electronic cue once on expiry. Check its volume and whether
   the UI event remains audible for NPC effects; spatial audio is unverified.
5. Clear early with the helper, reapply, move away, kill the target and save/
   reload after expiry. Confirm no looping sound or stranded particles.
6. Inspect `red4ext/plugins/ArchiveXL/ArchiveXL.log` and TweakXL's log for
   missing patches, invalid records or unresolved localization.

`generated/previews/*-motion.gif` and `*-outro.gif` preview authored texture frames against a dark
background. It is not a captured game render. The native material adds tint
and brightness; screen sizing, occlusion and placement need runtime tuning.

Reference: ArchiveXL's [player scope definitions](https://github.com/psiberx/cp2077-archive-xl/blob/main/bundle/source/resources/PlayerBaseScope.xl)
provide the player template paths. Local custom FX and ArchiveXL notes plus the
installed 2.31 resources supply the status lifecycle and placement contracts.

## First runtime feedback and correction (0.1.1)

The first installed candidate added the item correctly, but V showed the
vanilla white blindness screen, and Goth Baddie was blinded without hearts.
TweakXL logged unknown `sfx` and `onEquip` properties. The game fields are
case-sensitive: the corrected tweak uses `VFX`, `SFX`, and `OnEquip`. The
original lowercase VFX override is now rejected by the build-time type check.

Goth Baddie's entity was outside the original base-game NPC target list. Version
0.1.1 explicitly patches `mod\ghostline\characters\goth_baddie\goth_baddie.ent`
as an optional integration target. Heartbreaker does not ship or replace the
Goth Baddie assets or activate its quest. Restart the game after installing
0.1.1 so both the changed TweakDB record and entity patch reload. Retest the
existing V/NPC hotkeys; the new helper diagnostics distinguish a missing
spawner from a failed status application. This corrected candidate still
was confirmed working by the user's V/NPC screenshots on October 11, 2026.
Both presentations and the pixel outro are visible, including on Goth Baddie.
The screenshots do not establish audio or cancellation behavior.

## Pixel-art refinement (0.1.2)

The working 0.1.1 captures showed oversized, cropped V hearts and a tint that
read red. Version 0.1.2 changes the screen size from 3.3 to 1.05, uses twelve
hearts by default, and shifts the tint to stronger magenta-pink while lowering
the material multiplier from 1.7 to 1.15. The NPC billboard is slightly smaller
(1.25 instead of 1.4), with stronger size variation and independent bobbing.
Both presentations now use sharp pixel glyphs, a stepped motion loop, stronger
glitch slicing and small accent pixels. The finite 0.6-second breakup and
one-shot electronic outro cue remain in the native timeline.

The known-good 0.1.1 package and receipt are retained under
`generated/packages/heartbreaker-030753a50e0d`. The refined candidate still needs
in-game confirmation of screen fit, colour and animation continuity. Restart
the game after installation and use the existing V/NPC test hotkeys; the CET
helper has no changed behavior and is not part of the native ZIP.
