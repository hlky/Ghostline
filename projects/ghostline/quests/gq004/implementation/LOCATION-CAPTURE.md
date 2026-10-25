# Love, Actually.exe: location capture

All 16 targets have been captured and imported. The exact source snapshot is
`world/love-actually.locations.json`; `world/love-actually.world.json` contains
the applied transforms. All four native world resources passed authored-field
readback verification. No recapture is required for this build. The instructions
below remain available for later placement revisions. In-game collision, navmesh
and scene spacing still need review.

The capture helper is installed at:
`K:/Cyberpunk 2077/bin/x64/plugins/cyber_engine_tweaks/mods/ghostline_love_actually_scout`.
Launch the game, load a save, and open CET. If the game was already running when
the helper was updated, restart it before capturing. Find **Love, Actually.exe - locations**.

You need two sites and seven standing positions. Capture on foot.

1. **Velvet's meeting spot in Kabuki.** Choose clear, walkable ground with a
   quiet backdrop and about three metres of unobstructed space in front of her.
   Stand where she should stand and face the direction she should face.
   Click **Record meeting group here (8)**. This sets her standing spot, scene
   anchor, map pin, origin, and four concentric meeting gates.
2. **Centre of the Tyger Claw operation.** Pick a small encounter space with a
   stealth route, two plausible socket mounts, and room for three guards.
   Click **Record operation centres here (3)**. The operation radius is 30 m;
   cleanup radius is 50 m. Keep the sockets and guards inside the inner area.
3. **Recovery socket.** The chooser selects the next missing target automatically.
   Stand at the intended mount's floor position and face out from its wall.
   Its initial height is 1.20 m above your feet. Adjust with **Height +/-0.10 m**
   to put the socket centre at the desired height, then **Record selected position and facing**.
   The importer rotates the socket plate by +90 degrees to match this facing.
   Current mounts also apply a 0.40 m setback toward the wall from your standing
   position; adjust `mount_setback` per device if a future capture is already flush.
4. **Distribution socket.** Repeat for a separate mount. This second device
   receives the corrected upload; it must be distinct from the recovery socket.
5. **Guard 1.** Stand on clear ground where the ranged guard should wait, face
   their watch direction, and record. Height resets to zero for guards.
6. **Guard 2.** Repeat at another ranged guard position.
7. **Guard 3.** Repeat at the melee guard position. Leave a usable route around
   the guards and enough room for them to move.

The counter should read **Saved 16/16**. You can refine any target using
**Previous / Next**; **Next missing** resumes an unfinished pass. Captures
survive game restarts. Group buttons overwrite their group's captures, retaining
the immediately preceding log as `.bak`.

Then return to this chat and say **captured**. No upload is necessary: the log is
local at `K:/Cyberpunk 2077/bin/x64/plugins/cyber_engine_tweaks/mods/ghostline_love_actually_scout/love-actually-locations.json`.

The helper records positions and facing only. It does not spawn quest objects,
teleport V, or activate the placeholder quest. Device mounting, collision,
navmesh, guard behaviour, and scene spacing are checked after coordinates are
imported. The 1.20 m mounting height is an adjustable starting value.

For the build workflow, `scout.py check --game-root 'K:/Cyberpunk 2077'` verifies
the installed helper. `scout.py import-log --input <log>` validates all targets
and generates a separate captured world spec. `--apply` updates the authored
spec only after validation. Trigger captures are ground centres; the importer
lowers their volumes by half their height.
