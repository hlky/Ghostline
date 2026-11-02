# GQT010 — Pacifica Coast Run

Independent point-to-point race, 3,153.93 metres. Starts on the city streets,
turns through the next block, descends through the coastal tunnel and finishes
beside Pacifica's Ferris wheel and Caliente stand. Target duration is roughly
3–4 minutes; actual driving time is not yet measured.

The 139-point road-surface survey includes multiple points around the corners.
The entire course was physically followed in both directions with the camera;
the final race-direction review covered every section. At the user's request,
camera height increased to about four metres to avoid traffic collisions.
Road geometry remained surface-raycast based.

The race has ten intermediate checkpoints and a finish, vanilla MQ056 checkpoint
entities and signs, native replay reset, and no vehicle diagnostics or authored
post-finish vehicle-forbidden area. Finish parking and courier departure use
separate surveyed paths beyond the finish.

## Playable candidate

Activation position: `(-1882.1812, -508.9289, 7.8384)`, facing 270 degrees.
Approach the race marker with an owned car, use the waiting interaction, mount
the car and follow the countdown. Drive all eleven gates in order. Winning pays
the native 10,000 eddies and enables the separate reward pickup. The availability
phase handles the native replay cooldown and resets the checkpoint counter.

Authoring: `implementation/builder.spec.json`, `implementation/race-plan.json`,
and `implementation/world.json`. `implementation/survey-review.json` records
the camera review and the final Game Scout export. Build with `--publish
--deserialize` before packaging the `gqt010` profile.

The user reports the race, route and curves work well. Part of the divided-road
section deliberately remains against traffic, as accepted after the playtest.
The user confirmed opponent cleanup works. The courier arrival clearance gate
prevented delivery, so that gate is removed and the original immediate courier
flow restored. Courier and bike now spawn on surveyed pavement to the right of
the road. Their departure uses a surveyed gap between bollards.

Four opponents use database-selected Caliburn, Outlaw, Javelina and Coyote
records, with individual grids and finish parking splines. The activation and
all eight crew positions were resurveyed to leave V's view clear. A player pose
reset runs before fade-in to restore the activation heading. These latest
changes need a fresh playtest; the main race spline remains unchanged.
Actual duration, abort/prevention, save/load and replay also remain unverified.

Installed candidate: `gqt010-5fca6322381d`. Archive, registration and tweak hashes
match the verified package. See `implementation/install-receipt.json`.

No changes to GQT009 are part of this race.
