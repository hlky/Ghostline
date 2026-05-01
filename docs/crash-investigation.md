# Crash Investigation Findings

Extracted from the 2026-04-29/30 probe work. This file preserves useful
runtime observations only. It is not the target specification for fresh scene
creation tooling.

For target scene structure, use `docs/scene-authoring-rules.md`. Vanilla
patterns override failed Ghostline probe results. If a vanilla pattern crashed
in a probe, assume the Ghostline implementation was incomplete or malformed.

## Current Read

The restored intro choice scene worked when approached slowly but crashed on a
normal-speed approach. Adding a pre-scene `CharacterSpawned` gate for the Patch
community fixed the fast-approach crash in game.

Vanilla reference scenes and `modding_docs` use `questCharacterSpawned`
`PauseCondition` gates before letting conversations proceed. Ghostline now uses
the same immediate pre-scene gate in `gq000_patch_meet.questphase`:

```text
#gq000_01_tr_engage -> CharacterSpawned #gq000_01_com_patch_bridge -> scene start
```

The older conclusion that actor acquisition and scene startup were fully ruled
out is now too broad. The direct start-to-end probe only proved that the scene
resource can enter and exit when startup timing is favorable.

The temporary crash-isolation setup uses `Character.Judy` in the `patch/default`
community entry. That keeps the world/community path independent of Patch's
custom entity while the scene path is being stabilized.

The current packed/raw questphase and scene resources are a reduced
crash-surface build refreshed from WolvenKit-edited CR2W on 2026-05-01:

- root `gq000.questphase` routes successful `gq000_patch_meet` completion
  directly to `gq000_done` and output;
- the previous failed-output route through the logical hub and fallback phase is
  disconnected;
- `gq000_patch_meet.questphase` exits on scene socket `end` instead of
  `job_accept`;
- scene journal description node `n16` routes directly to first choice node
  `n8`;
- scene mappin node `n17` remains present but has no incoming or outgoing
  connection.

This is an isolation shape, not yet the final target scene/quest structure.

## Useful Findings

- Excluding `source/archive/base` did not stop the crash. Base-path overrides
  are still a shipping risk, but they are not the sole cause of the current
  runtime crash.
- Earlier `Engine/LoadExports` hashes resolved to built-in always-loaded
  sectors, pointing back at the always-loaded streaming merge shape rather than
  only at copied base character files.
- Replacing the registration-only mappin row with a concrete always-loaded
  `worldStaticMarkerNode` resolved the cooked mappin hash path and allowed the
  later world/community isolation to proceed.
- Missing RedHotTools hashes `14413217326793937713` (`0xC80608CB520ED331`) and
  `16106537288591666266` (`0xDF85EA53F016EC5A`) do not match FNV1A64 hashes of
  Ghostline raw `ResourcePath`, `NodeRef`, or string values, including expanded
  `$/mod/gq000/#gq000_pr_patch_meet/#...` NodeRefs. They also were not found in
  local base, EP1, or installed mod archives. Treat them as runtime-generated
  dependency hashes until proven otherwise.
- After the fixed always-loaded marker shape, Judy spawned from the Ghostline
  community spot. That isolates the community registry, streamable community
  area, and AI spot as functional.
- Rewiring `#gq000_01_tr_engage` directly to phase output avoided the crash.
  The world/community/trigger path before scene startup is therefore safe.
- Rewiring the scene start directly to scene end worked. That proves the scene
  resource can enter and exit, but it does not prove community actor readiness
  is stable under a fast approach.
- Direct-dialogue crashes continued after VO registration and after subtitle
  map registration was corrected. The active crash is not missing subtitle/VO
  registration.
- Response line text and VO can play when a response payload is routed through
  the known-good intro section shell. This rules out response locstring/VO
  payloads as the main fault.
- Fast approach crashing while slow approach worked was consistent with a
  spawn-readiness race. Waiting on `questCharacterSpawned_ConditionType` for the
  community NodeRef immediately before scene start fixed the issue.
- `Ghostline?` displaying as `Db-db` was caused by the generated compact
  locStore shape, not by `scnChoiceNodeOption.caption`. Vanilla-style choice
  locStores use locale blocks and two `db_db` descriptors per choice: a blank
  fallback and a source text payload.
- The current reduced build deliberately removes scene-local mappin execution
  and acceptance-socket branching from the active path. Treat any resulting
  stability as evidence about those surfaces before restoring them one at a
  time.

## Discarded Probe Conclusions

These probe conclusions contradict audited vanilla patterns. They are preserved
only so future docs and tooling do not accidentally re-promote them:

- Discard: `persistentLineEvents` must be empty.
- Discard: legacy generated choice socket stamps should be preserved.
- Discard: optional choices must not use `isSingleChoice: 0`.
- Discard: `db_db` locStore records should be replaced with `en_us`.
- Discard: spoken screenplay item IDs `1 + 256n` are unsafe.
- Discard: `Xor` nodes should be avoided categorically.
- Discard: `entryActiveOnStart: 0` is confirmed vanilla lifecycle.

Use the vanilla target rules in `docs/scene-authoring-rules.md` instead.
