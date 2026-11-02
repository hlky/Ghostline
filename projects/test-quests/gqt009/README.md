# GQT009: Arroyo Industrial Run

Current installed candidate: `gqt009-44ac4936ca41`. Its archive, registration
and tweak hashes match the verified package in `K:/Cyberpunk 2077`.

The post-finish vehicle-forbidden zone has been removed entirely, including
its generated node, variant and quest references. The user reported the
preceding `gqt009-48c661794b95` build was otherwise working.

The corrected 57-point route and GPS remain unchanged. Checkpoint placement
now uses distance along the route (`checkpoint_spacing_m: 125`), giving nine
intermediate gates plus the finish; spline vertices no longer add gates.
Vanilla MQ056 checkpoint instances retain directional/finish sign overrides
and per-attempt sign-component rearming. Checkpoint registration now belongs
to the ordered quest trigger areas: each outside/inside crossing sets the
shared HUD counter to its station number. Stock entity triggers stay disabled
to prevent duplicate counting; there is no device-action/fact-callback gate. No custom entity templates or
CET/REDscript diagnostics are packaged.

Normal finish cleanup no longer stops V's vehicle workspot. It releases the
owned car's brake and uses native `ResetInteractions`, `ForceUnlock` and
front-door `EnableInteraction` operations so V can exit and enter normally.
The former `EnableAllInteractions` action is not a native door-state enum.
The opponent's spline, community area and home/finish spots now use long-range
streaming instead of point-sized 120 m placement limits. The user confirmed full-route opponent visibility on the preceding
`gqt009-8db810f972ad` candidate. That candidate stalled at the first checkpoint
(0/10); this revision replaces its device-driven registration path.
Johnny's authored start is (-898.53406, -1094.5117, 12.168755), yaw 55.253258.

Six focused checks, native CR2W readback, archive/ZIP extraction and payload
hash verification passed. These establish authored-data and installed-byte
integrity, not observed gameplay or PS5/mod.io acceptance. Retest the complete
race, opponent retention past the former third gate, finish seating, and car
exit/re-entry; also verify replay resets and the new HUD total of 10.

Package/evidence: `generated/packages/gqt009-44ac4936ca41/` contains
`Ghostline_GQT009.zip`, `verification.json` and `installation.json`.
Earlier generated entities and tracing sources are preserved under
`generated/vanilla-checkpoint-migration/`; installed diagnostic helpers were
previously removed. The candidate and crash details below are historical.

Independent race preview. The source survey and builder inputs are in
`implementation/`; the previous survey snapshot preserves the original capture
evidence for the copied marks. The activation is on pavement beside the grid.

The 2026-11-01 road survey replaces the sparse route with 57 road-surface
centerline samples, including the street around the shop block and multiple
points through the corners. Checkpoints, finish direction and GPS follow that
line. The complete corrected route was traversed again at vehicle height;
`implementation/route-review.json` retains the camera-route evidence. The
survey remains point-to-point. The authored world retains the finish cleanup areas; the separately surveyed
post-finish vehicle-forbidden stopping area was removed after playtest. These updated
builder inputs were published with `--publish --deserialize` after discovering
that the earlier install had packaged the old project sources instead of the
corrected preview. The historical candidate details below predate this revision.

Build and verify CR2W resources from the repository root:

```powershell
.venv/Scripts/python.exe -B tools/race_builder.py build --spec projects/test-quests/gqt009/implementation/builder.spec.json --publish --deserialize
```

Candidate `gqt009-0d18ea1953b9` is installed and its archive and ArchiveXL
registration hashes match the verified package. It has not been playtested.
The race builder generates every resource directly, without templates. Its CR2W
resources were written and readback-verified by ghostline-red, then packed and
extraction-verified by WolvenKit. The activation graph declares only the start
and end nodes that it creates (55 and 161); the stale vanilla boundary entries
that could crash scene loading on approach are removed. The full race
registration replaces the world-only diagnostic.

The 10:51:12 crash persisted after repairing the graph boundary lists. Its dump
shows acquisition indexing the second actor slot while the scene has only one
actor. The generated player now occupies actor slot 0, and section, transition
and debug-symbol references use actor 0 / performer 1. Previously they retained
actor 1 / performer 257 despite there being no NPC in slot 0. The builder checks
contiguous actor slots and matching actor/performer references. Approach from the opposite pavement
at (-912.66, -1081.73, 12.18), yaw 55, remains the required runtime retest.

The subsequent 10:59:03 crash reached choice node 119 and dereferenced a null
interaction parameter. The direct generator now supplies the world choice's
shape, look-at and mappin handles and its on-foot/out-of-combat conditions.
It omits the unnamed `scnEventType` property, as the vanilla binary does; all
nine final resources decode through WolvenKit without warnings or errors.
The phase fixes also make player unmount detection independent of the lost
mounted-vehicle reference, cancel and rearm the off-course timer on return,
route opponent driving-command failures to failure cleanup, and preserve a
pending abort request. The complete graph audit resolves all 26 world aliases,
both community entries, journal paths, scene/phase sockets and connections.
The current root has 50 reachable nodes; the attempt has 97 reachable nodes.
The install receipt is `generated/full-audit/final-install.json`; the independent
readback log is `generated/full-audit/final-wkit-readback.log`. In-game behavior
of this candidate has not been confirmed. No computer control was used to
launch or test this candidate.
Restart the game and use a save from before this race was registered. At the
starting-grid pavement near world position (-896.12, -1091.03, 12.19), select
the wait interaction and then start the race. Check the standing workspot and
camera recovery, route and opponent driving, checkpoints, cleanup, and elapsed
time in game. ArchiveXL is required. The race is a single attempt and its facts
persist in saves; restarting the game does not reset an already completed race.
