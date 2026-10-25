# Velvet Crash

A native Cyberpunk 2077 2.31 control quickhack: black pixel-art bows and pink
hearts bob and glitch for six seconds, then explode into tumbling confetti
and pink streaks over 0.8 seconds. The existing electronic cue
`ui_fx_hacking_glitch_fullscreen_low` plays once at the start of the outro.

The native item is `Items.GhostlineVelvetCrashProtocol`. It retains Reboot
Optics-derived blindness, targeting, RAM cost and upload behavior. V can consume
`Items.GhostlineVelvetCrashSelfTest` to experience the screen presentation.
The default V layout is six bows and six hearts; NPCs get three of each,
attached to the Head slot. Eight authored motion frames repeat over 0.8 seconds.
These are native texture/particle tracks, with baked motion and confetti rather
than independently simulated 3D fragments.

Version 0.1.1 separates bows and hearts into synchronized particle layers with
independent material instances and colour/opacity textures. Bows use
non-additive, full-opacity settings with stronger pink rims. Hearts use additive
settings and a higher colour multiplier for glow. The same split continues
through the confetti outro. Exact colour, contrast and alpha behavior still
need runtime checking; offline settings alone do not establish visibility.

This is an independent project with unique depot paths, TweakDB records,
localization keys, effect names, spawner names and event IDs. It can be installed
alongside Heartbreaker. Its reviewed generator/donor snapshots are recorded in
`implementation/base-prototype.json` and `implementation/donors/catalog.json`.
Heartbreaker is not a build or runtime dependency.

Runtime dependencies are RED4ext, ArchiveXL and TweakXL. There is no custom
REDscript or Lua in the native package. An optional CET helper under
`testing/cet/velvet_crash_test` has four manual hotkeys: give items, apply to V,
apply to the looked-at NPC, and clear statuses to test early cancellation.
Its callback IDs and status records are separate from Heartbreaker's helper.

The quickhack and ten self-tests are added to the Little China netrunner's
vendor stock. Inventory refresh remains subject to the game's vendor behavior.
The helper can add the items directly. ArchiveXL patches fourteen V templates,
244 reviewed vanilla humanoid NPC templates (128 base and 116 Phantom Liberty
replacement templates), and the optional Goth Baddie entity. The EP1 replacements
also serve ordinary Night City gangs and police when Phantom Liberty is installed.
The runtime trace confirmed that targeting only the legacy base paths left the
actual Tyger Claw, NCPD and Maelstrom targets without an FX spawner. All 116
additional templates were decoded from the installed archive and checked for
NPCPuppet plus a Head attachment slot; see `implementation/npc-target-audit.json`.
Other custom NPCs, bosses, robots and lightweight crowd templates are outside
the reviewed target list. This prototype does not assign the hack to enemy AI.

Run from the repository root:

```powershell
.venv/Scripts/python.exe projects/experiments/velvet-crash/implementation/build.py
.venv/Scripts/python.exe projects/experiments/velvet-crash/implementation/verify.py
.venv/Scripts/python.exe tools/check_project.py
.venv/Scripts/python.exe tools/package_project.py --project velvet-crash --install --game 'H:/Cyberpunk 2077'
```

`velvet_crash.fx.json` controls colours, density, sizes, motion and timing.
Authored assets live under `source/raw`, compiled CR2W under `source/archive`,
and loose registrations/tweaks under `source/resources`. Generated GIFs under
`generated/previews` show authored motion/outro frames against a dark background;
they do not simulate the game shader.

After a full game restart, bind the four **Velvet Crash** CET hotkeys. Test V
and Goth Baddie, then a supported vanilla NPC. Confirm black bow interiors stay
visible, pink hearts move, the six-second blindness ends, confetti fades cleanly,
and the electronic cue plays once. Also clear early and reapply to check that
no particles or audio remain stuck. Offline verification establishes resource
and package integrity. The user's October 11 clips of 0.1.0 show hearts and
confetti rendering while bow silhouettes read mostly as faint outlines. That
candidate already serialized `AdditiveAlphaBlend = 0`, so an enabled additive
flat was not established as the cause. The 0.1.1 split allows each glyph type
to be tuned independently. Both supplied MP4s have video-only streams, so they
provide no audio verification. The revised candidate awaits an in-game retest.
