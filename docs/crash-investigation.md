# Crash Investigation Findings

This file preserves dated runtime evidence from the April probes through the
July 2026 stability work. It is an investigation history, not the target
specification or a description of the current candidate unless a section says
so explicitly.

For the current runtime model, use `docs/quest-scene-flow.md`; for target scene
structure, use `docs/scene-authoring-rules.md`. Vanilla patterns override failed
Ghostline probe results. If a vanilla pattern crashed in a probe, assume the
Ghostline implementation was incomplete or malformed.

## 2026-07-21 Fast-Travel Crash

The synchronized current-raw build crashed after this sequence:

```text
load clean save -> receive phone message -> select On my way -> fast travel near bridge -> crash
```

`On my way` accepted the meeting and activated its tracker; job acceptance
would have occurred later through the scene's `job_accept` exit.

The dump recorded `Loading world`, resource throttling in `Flood`, a roughly
990-unit teleport, and an invalid allocator pointer on background dispatcher
thread `redDispatcher20`. ArchiveXL successfully merged the streaming block,
quest phase, journal, localization, and mappin; no plugin log named a failed
Ghostline resource.

The recorded observer position was about 101.5 horizontal units from the
bridge origin. That position was inside the then-current 150-unit setup trigger
and inside community streaming range, but would have remained outside the last
working 90-unit setup trigger.

Two coupled defects were present in that build:

- the current-raw meeting phase started the scene from setup before the
  previously proven phase-level engage and `CharacterSpawned` gates;
- the always-loaded `worldCommunityRegistryNode` reused global node ID
  `7897875840529598144`, already owned by the streamed community area. The
  community area's `sourceObjectId` and registry item's `communityId` should
  share that value, but the separate registry node identity should not.

The next repair changed both surfaces: it restored the `5debf03` phase-owned
spawn-readiness flow and matching 14-node scene, restored horizontal trigger
radii `90/10/60/20` while retaining 12-unit height, and assigned the registry
node distinct global ID `7571954536596633334`. Fast travel then completed, but
because those changes landed together this loading-world crash was not
attributed to one defect in isolation. The crashing archive is retained at
`H:\Ghostline-backups\pre-stability-fix-20260721-224252`.

## 2026-07-21 Engage-Boundary Approach Crash

The repaired world build completed the nearby fast travel, then crashed on a
normal bridge approach. A second attempt paused on the bridge and approached
more slowly, but failed at the same activation point. The two reports are:

- `Cyberpunk2077-20260721-225818-16196-15872`
- `Cyberpunk2077-20260721-230126-18020-10252`

Both dumps fail at `Cyberpunk2077+0x1d173be` on dispatcher threads, at about
10.8 and 10.4 horizontal units from the meeting origin. Loading had finished,
the throttler state was `Stream`, and the dialogue visualizer count was zero.
This is a deterministic scene-start failure at the engage boundary, distinct
from the earlier `Cyberpunk2077+0x19088d0` fast-travel/loading-world crash.

The faulting code reads element 1 from a REDengine dynamic array whose size and
capacity are both 1, copies a shared handle, then faults while incrementing its
garbage reference count. The runtime object contains depot hash
`0x355d4ccf4a70a25f`, the FNV-1a 64 hash of
`mod\gq000\scenes\gq000_patch_meet.scene`, which ties this crash directly to
scene activation. It does not by itself identify which internal array is bad.

Fresh `mq003` comparison exposed the strongest lifecycle mismatch:

- `mq003` activates and validates its whole community before the approach;
- its child phase starts the scene at a broad setup trigger;
- the already-running scene performs setup, then waits internally through
  progressively narrower mood, awareness, and engage gates.

The restored Ghostline flow instead waited until the 10-unit engage trigger to
start the scene. Its 60- and 20-unit scene conditions were therefore already
true, allowing scene setup, Puppet AI, and the opening dialogue path to cascade
in the same startup tick. The identical crash position on both approaches
makes this ordering a stronger lead than trigger geometry.

That mq003-sequenced isolation build used:

```text
phase: activate -> CharacterSpawned -> setup -> checkpoint -> scene start
scene: PuppetAI || case-mood -> someone-coming -> opening line -> engage -> choices
```

Trigger geometry and audio were intentionally unchanged so the then-next test
isolated sequencing. A separate audit confirmed all 13 referenced WEMs are
valid mono 48 kHz Wwise Vorbis, decode fully, and fall within the bitrate range
seen in mono `mq003` dialogue. Audio filename cleanup remains worthwhile but is
not part of this crash-isolation build.

The verified installed archive for this test has SHA-256
`177500B67B2A6B975A597DF5D582797F006643BA6BC975E1D9CFBC66BC498BFD`.
Relative to the replaced installed build, only the meeting phase and scene
payloads changed. The replaced build is backed up at
`H:\Ghostline-backups\pre-mq003-sequence-20260721-233546`.

## 2026-07-21 Setup-Boundary Scene Crash

The mq003-sequenced build moved scene launch from the 10-unit engage trigger to
the 90-unit setup trigger. Report
`Cyberpunk2077-20260721-234436-30228-24592` then crashed at 89.27 horizontal
units from the meeting origin with the same
`Cyberpunk2077+0x1d173be` fault. Loading had finished, the throttler was in
`Stream`, and no dialogue visualizer existed. Moving the crash with the launch
condition shows that the trigger radius is not the cause; scene initialization
is exercising the bad lookup.

The dump requests index `1` from a 16-byte-handle runtime array whose size and
capacity are both `1`. The adjacent out-of-bounds memory contains unrelated
world-node text and is subsequently treated as a reference-count pointer. The
scene's strongest matching cardinality defect is its lipsync table:

- Patch used lipsync resource ID `0` and V used ID `1`;
- raw CR2W-JSON emitted two lipsync rows with the same generic depot path;
- the packed scene has only one distinct import for that resource;
- runtime exposed one handle before requesting index `1`.

That slot-0 isolation changed only V's lipsync ID from `1` to `0` and reduced
the lipsync resource array from two duplicate rows to one. Scene graph,
dialogue, timing, questphase, triggers, world resources, and audio remained
unchanged. Shared slot `0` was deliberately diagnostic; final scene authoring
should return to distinct, valid NPC and V lipsync resources if separate
resources can be made addressable and verified.

The verified installed archive has SHA-256
`87956AFFE3C7CD66E16AD8531D0784689B01A24DCA629FAF41C2291C6E70E40D`.
Build evidence is at
`H:\Ghostline-builds\lipsync-slot0-20260722-000338`, and the replaced archive
is backed up at
`H:\Ghostline-backups\pre-lipsync-slot0-20260722-000338`.

## 2026-07-22 Scene-Crash Resolution And Choice-Label Diagnosis

The shared-slot build completed the full route without a crash: phone message,
nearby fast travel, normal approach, all 13 spoken lines with subtitles and VO,
`job_accept`, meeting objective/mappin cleanup, and the cache objective and
marker. This strongly confirms that the remaining setup-boundary crash was the
slot-1 lookup against a one-entry cooked lipsync table.

That run exposed a separate non-crashing ordered-table defect. Two labels in
the first choice group were blank and `Who's behind it?` resolved as stale
`Why me?`. The scene contained every expected payload, but each locale block in
`locStore.vdEntries` retained manifest order instead of ascending numeric
`locstringId` order. All four audited vanilla scenes use sorted locale blocks.

Together, the current generator, validator, and checked-in-raw equality
regression protect:

- contiguous `db_db`, `pl_pl`, and `en_us` blocks;
- unsigned numeric `locstringId` order inside each block;
- the generated adjacent blank-then-source `db_db` mapping (the validator
  checks at least two payloads and a blank payload first);
- full unsigned 64-bit locStore variant and scene event IDs.

The installed sorted-locStore archive changes only the meeting scene from the
successful slot-0 runtime baseline. All-five-label confirmation is still
pending; see `docs/testing.md` for the exact test route and
`docs/quest-scene-flow.md` for the concrete current flow and lookup model.

## Earlier Runtime Read

An earlier probe of the intro choice scene worked when approached slowly but
crashed on a normal-speed approach. At that stage, adding a pre-scene
`CharacterSpawned` gate for the Patch community appeared to fix the
fast-approach crash.

Later bridge testing found the meeting trigger volumes were vertically too
shallow for the bridge's varying height. Raising all four meeting triggers to
12-unit volumes and centering them around the captured bridge origin resolved
the remaining bridge approach crash path.

Vanilla reference scenes and `modding_docs` use `questCharacterSpawned`
`PauseCondition` gates before letting conversations proceed. The restored
14-node build placed that gate immediately before scene start:

```text
#gq000_01_tr_engage -> CharacterSpawned #gq000_01_com_patch_bridge -> scene start
```

The older conclusion that actor acquisition and scene startup were fully ruled
out is now too broad. The direct start-to-end probe only proved that the scene
resource can enter and exit when startup timing is favorable.

The setup originally introduced for crash isolation still uses
`Character.Judy` in the `patch/default` community entry. The scene-start fault
has since been isolated, but keeping Judy in place preserves the runtime-proven
world/community baseline until the sorted-label regression passes, TweakXL is
installed, and custom Patch validation begins.

The following reduced crash-surface shape was tested historically from
WolvenKit-edited CR2W on 2026-05-01:

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

That was an isolation shape, not the current stability baseline or final target
scene/quest structure.

## Useful Findings

- Excluding `source/archive/base` did not stop the crash. Base-path overrides
  are still a shipping risk, but they were not the sole cause of that
  historical runtime crash.
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
  map registration was corrected. The crash active at that stage was not
  missing subtitle/VO registration.
- Response line text and VO can play when a response payload is routed through
  the known-good intro section shell. This rules out response locstring/VO
  payloads as the main fault.
- Fast approach crashing while slow approach worked was consistent with a
  spawn-readiness race. Waiting on `questCharacterSpawned_ConditionType` for the
  community NodeRef repaired that lifecycle gap, but it did not resolve the
  later deterministic scene-start crash; the remaining fault was the lipsync
  slot cardinality mismatch described above.
- `Ghostline?` displaying as `Db-db` was caused by the generated compact
  locStore shape, not by `scnChoiceNodeOption.caption`. Vanilla-style choice
  locStores use locale blocks and two `db_db` descriptors per choice: a blank
  fallback and a source text payload.
- The shared-lipsync-slot build completed the full phone, fast-travel,
  approach, dialogue, acceptance, and cache-objective route without a crash.
  This strongly confirms the scene-start failure was the slot-1 lookup against
  a one-entry runtime lipsync table.
- Runtime screenshots exposed a second ordered-table issue: two first-group
  choices were blank and `Who's behind it?` resolved as stale `Why me?` text.
  Ghostline's locale blocks were grouped but not sorted by `locstringId`; all
  four audited vanilla scenes sort every locale block numerically. The scene
  generator and validator now enforce that invariant.
- The May reduced probe deliberately removed scene-local mappin execution and
  acceptance-socket branching from the active path. Its results remain useful
  evidence about those surfaces, but do not describe the current build.

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
