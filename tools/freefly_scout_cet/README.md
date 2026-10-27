# FreeFly scouting patch

Local patch for the installed keanuWheeze FreeFly CET mod. The original mod is
not distributed here. `patch_freefly_scout.py` checks the expected source shape,
backs up the changed files outside CET's mod directory, installs `scout.lua`,
and enables **No Weapons During Flight**. Existing flight controls are retained.

```powershell
python tools/patch_freefly_scout.py --game 'K:/Cyberpunk 2077'
lua tests/freefly_scout_harness.lua
```

While flying, the patch applies the original movement, zoom, and weapon locks,
adds `Invulnerable` under the unique `GhostlineFreeflyScout` GodMode source, and
calls `PlayerPuppet.SetInvisible(true)` to disable the player's AI visible object.
It removes the original per-frame health refill, so flying no longer heals V.
The radio hook bypasses only `PocketRadioRestrictions.UpperBodyState` while the
patch owns the `GameplayRestriction.NoCombat` effect. Other radio restrictions
remain effective, and the radio's station and on/off choice are not changed.

Landing, session end, and CET shutdown clean up flight-owned effects and named
GodMode/time-dilation sources and restore the previous AI visibility state.
Pre-existing status effects and other GodMode sources are retained. The installed
UI can still toggle the weapon lock during flight.

Native behavior still needs a playtest: start a radio station, toggle flight,
approach guards/cameras, try drawing/firing a weapon, and check incoming damage.
Land and check normal detection, weapon use, and damage again. Test loading a
different save and CET Reload All Mods during flight as well. Existing combat
and scripted encounters are not forcibly cleared; quests and calls can still
restrict the radio.

Originals from the first install are under
`K:/Cyberpunk 2077/ghostline-mod-backups/freefly-scout-20261026-222626-530103`.
To revert with the game closed, copy its `init.lua`, `modules/utils/logic.lua`,
and `config/config.json` back into FreeFly and remove `modules/utils/scout.lua`.
The backed-up config contains the earlier radio workaround (`noWeapon=false`);
enable the original weapon-lock option afterward if desired. Reinstalling or
updating FreeFly may overwrite the patch; source-shape checks must pass before
reapplying it.

API behavior was checked against the installed game's REDmod script sources:
`core/systems/godModeSystem.script`, `core/gameplay/pocketRadio.script`, and
`cyberpunk/player/player.script` (spawn grace, `SetInvisible`, upper-body radio
restriction, and optical-camo behavior).
