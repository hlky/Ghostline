# Ghostline Testing

Use a fresh save when validating questphase, scene, journal, or world-trigger
changes. Prefer a manual save made before any version of Ghostline was
installed or registered.

Avoid testing from autosaves or saves made after a failed probe. Quest facts,
journal visited state, active questphase nodes, checkpoints, and scene state can
persist in the save and leave `gq000` waiting in an old graph branch.

The project includes test-time autosave suppression resources:

- `source/resources/engine/config/base/user.ini`
- `source/resources/r6/scripts/Tduality/autosave_is_Not_included.reds`

These reduce accidental save contamination, but they do not clean an already
contaminated save. Keep a known-good pre-Ghostline manual save and return to it
for each start-flow validation pass.
