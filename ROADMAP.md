# Ghostline Roadmap

Last audited: 2026-07-24

This file tracks the current state and the next work needed to turn `gq000`
from a dialogue prototype into a playable quest slice. The current 2026-07-22
delivery/debrief candidate builds on the runtime-proven repaired world,
mq003-sequenced meeting lifecycle, visible custom Patch, sorted choice locStore,
and explicit-player Tyger Claw combat setup. The bridge meeting, all dialogue
labels, VO/subtitles, job acceptance, cache handoff, guard spawn/patrol/aggression,
terminal transform and marker, native breach, readable shards, leave-area beat,
and cleanup are confirmed. The active package extends that baseline with a
native Kabuki drop-point deposit, Morrow's two-choice phone debrief, a standard
completion reward, and quest success.
Detailed command usage, runtime flow, crash conclusions,
world-reference notes, and packaging instructions now live in focused docs:

- `docs/quest-scene-flow.md`
- `docs/quest-design.md`
- `docs/tooling.md`
- `docs/testing.md`
- `docs/scene-authoring-rules.md`
- `docs/crash-investigation.md`
- `docs/world-references.md`
- `docs/drop-points.md`
- `docs/packaging.md`

## Current Status

### Native archive and CR2W tooling

- `tools/ghostline-red` is the focused Rust replacement for
  WolvenKit's command-line archive and CR2W conversion path. Its first working
  slice reads archive indexes, resolves depot paths from `source/archive`, and
  inspects CR2W headers plus string, name, import, export, and buffer tables.
- The current 301-entry `packed` archive is parsed with every path resolved.
  Its schema-driven CR2W codec now consumes the complete 80-resource authored
  corpus, including typed RedPackage buffers and the required custom
  appendices. Binary-to-native-JSON round trips are byte-identical. The writer
  supports new CName/import entries and template-class handle exports; novel
  class layouts and package topology changes intentionally remain
  template-bound.
- Native `pack` and `extract` commands now reproduce the current archive's 301
  entries and 1,048 CR2W segments. A full native pack/extract returns all 301
  payloads byte-identically, and WolvenKit independently extracts the native
  archive with the same result. Hardened Kraken compression uses the exact
  WolvenKit capacity formula, validates every compressed payload by
  decompression, and runs two-payload bounded workers in parallel so a native
  heap failure cannot corrupt the parent packer. The performance pass reduced
  warm native packing from roughly 3.06 seconds to 2.72 seconds while retaining
  a roughly 68.53 MiB archive versus WolvenKit's 68.41 MiB.
- A base-game `03_night_city.streamingworld` compatibility fixture round-trips
  byte-identically from both native and WolvenKit JSON. Native serialize and
  deserialize average 85.5 ms and 81.2 ms versus WolvenKit's 18.69 s and
  17.81 s on the same machine.

### GQT001 — Signal Delay building-block test

- `source/quests/tests/gqt001_signal_delay.quest.json` is the first isolated
  advanced-block runtime harness: reach a Ghostline-owned Kabuki laptop, open a
  quest-owned diagnostic file, wait ten seconds, and complete a two-choice
  Patch phone exchange.
- The selected native `laptop_1` has empty Files and Mails arrays. Its
  authoritative `ComputerControllerPS` is the outer sector node's
  `instanceData`. The test now uses a one-node ArchiveXL patch matched by
  compiled `globalNodeID`; only that laptop's instance data is replaced.
- Quest root/child phases, journal, onscreen localization, marker/trigger
  world resources, and the native-laptop sector patch are generated and
  deserialize successfully. The typed manifest is shipping-valid and the
  repository gate passes 179 tests plus 139 subtests.
- The corrected candidate is retained at
  `H:\Ghostline-builds\gqt001-inline-content-fix-20260724`. The first runtime
  pass proved the sector patch loaded but exposed a copied vanilla
  `fileEntryIndex: 7`; ArchiveXL-added onscreen entries resolve through the
  custom journal index `1`. A second pass still showed an empty Files menu:
  the instance's `DeviceContentAssignment.kabuki_generic` was replacing the
  injected inline Files array during initialization. The current override
  clears that assignment only on the selected laptop. When that still produced
  an empty menu, the isolation candidate switched the same injected slot to a
  known vanilla `gameJournalFile` while retaining Ghostline's completion fact.
  This distinguishes device-slot rejection from unresolved custom journal
  content. All 301 extracted archive payloads match `source/archive`; current
  diagnostic archive SHA-256 is
  `2FC11C9D767981A04E92D77894E7594358675E525E683AA5C30E0C01F368CBE7`.
  Its nine staged files are installed byte-identically under
  `H:\Cyberpunk 2077`, with the preceding install backed up at
  `H:\Ghostline-backups\pre-gqt001-signal-delay-20260724`.
- Repeated runtime passes proved that the outer
  `exterior_-18_28_0_0.streamingsector` instance-data edit was not the
  laptop's authoritative runtime content. The selected laptop is instantiated
  from cooked inplace resource
  `bd21168eed6c6d62.streamingsector_inplace`; its embedded
  `ComputerControllerPS.computerSetup` contains the actual empty Files and
  Mails arrays. ArchiveXL resource patching supports global `.devices` and
  `.psrep` resources but does not merge `streamingsector_inplace`, so the
  focused harness now directly overrides that exact cooked resource and no
  longer ships the ineffective outer-sector override.
- The resulting installed candidate is retained at
  `H:\Ghostline-builds\gqt001-cooked-computer-fix-20260724`. The cooked
  resource round-trip contains the custom file entry and
  `gqt001_document_read` fact, all 179 tests plus 139 subtests pass, all 301
  extracted archive payloads match `source/archive`, and the installed archive
  SHA-256 is
  `4B56BD1955E138C0EC9CE850F4B18FA648752EBB1C01D1D3615CEE0283767008`.
  The preceding install is backed up at
  `H:\Ghostline-backups\pre-gqt001-cooked-computer-fix-20260724`.
- The local ArchiveXL dependency was updated from 1.26.2 to 1.27.0 for this
  pass. Its upstream changes do not include a computer-content fix; the prior
  installation is backed up at
  `H:\Ghostline-backups\ArchiveXL-1.26.2-pre-1.27.0-20260724`.
- Runtime of the first cooked-resource candidate showed only the Net tab. The
  cooked file slot was present, but its custom journal-backed
  `gameJournalFile` had never been activated, so the computer UI filtered the
  entry and hid the empty Files tab. `read_terminal_document` is now a direct
  generated building block that activates an optional `document_entry` before
  the objective, then waits on the file's vanilla `questInfo.factName`.
- The rebuilt and installed candidate is retained at
  `H:\Ghostline-builds\gqt001-document-activation-20260724`. The packed
  read-document phase round-trips with the diagnostic journal activation first,
  all 179 tests plus 137 subtests pass, all 301 extracted payloads match
  `source/archive`, and the installed archive SHA-256 is
  `8FCE8971F4C4F842E99E45225BBAF6AC30141B7894C528A2E44AF611C16ED0D8`.
  The preceding archive is backed up at
  `H:\Ghostline-backups\pre-gqt001-document-activation-20260724`.
- ArchiveXL 1.27.0 has been extended locally with a
  `worldStreamingSectorInplaceContent` resource-patch merger. It replaces or
  appends embedded resources by depot path and honors the existing
  `props: [inplaceResources]` schema. The source patch and build notes are in
  `tools/archive-xl/inplace-resource-patching.patch` and
  `docs/archivexl-inplace-resource-patching.md`. The custom DLL is retained at
  `H:\Ghostline-builds\archivexl-inplace-patch-20260724` (SHA-256
  `6241B51528B8FCBF97ABB84EF5447C95FFFBF8AA96B90532F5756D7156C98781`);
  the official 1.27.0 DLL is backed up at
  `H:\Ghostline-backups\ArchiveXL-1.27.0-official-20260724`.
- The current archive is retained at
  `H:\Ghostline-builds\gqt001-archivexl-inplace-20260724`. It contains 301
  verified payloads, includes
  `mod\gqt001\world\gqt001_laptop.streamingsector_inplace`, excludes the old
  `base\...\bd21168eed6c6d62.streamingsector_inplace` override, and has SHA-256
  `6A8894CF3B9617EEFC4D968E14C4A9CEA4096DAB372D17F2AD6FF1F0D36BCC53`.
  The full repository gate passes 181 tests.
- The current candidate replaces the earlier coarse inplace-resource attempt.
  ArchiveXL applies `props: [instanceData]` after sector `PostLoad`, while the
  retained `inplaceResources` merger remains available for genuinely embedded
  template targets. The generated patch round-trips as one
  `worldStreamingSector` node with the `gqt001_document_read` fact, and the
  full repository gate passes 181 tests.
- The verified and installed instance-specific candidate is retained at
  `H:\Ghostline-builds\gqt001-instance-patch-20260724-172832`. Its 301
  extracted payloads match `source/archive`; archive SHA-256 is
  `92CBF34ACF38CB169DCF7550A7AB580AB3D3B2D00403A4C7C16CE999A39226CC`.
  The first instance-specific DLL incorrectly installed a second hook on
  `StreamingSector::PostLoad`; ArchiveXL logged a WorldStreaming hook failure,
  the laptop remained unchanged, and the game later crashed while exiting.
  The corrected build invokes resource patches from ArchiveXL's existing
  WorldStreaming callback and uses exact ID or transform/type node matching.
  Its installed SHA-256 is
  `DD6CE8A76E7321DE1B430F3B4A4DED28836DCDF3B5D73BB83B4FE584E9F868FC`.
- Runtime validation remains: confirm the native combat-event laptop is
  available from a clean save, the five-metre reach trigger and GPS marker are
  useful, the file sets its fact exactly once, the elapsed-time gate advances,
  and both phone choices complete the harness.
- Runtime confirmed the instance patch reaches the exact intended node and
  creates the Files menu, but the journal-backed element was filtered from the
  list. The current candidate supplies native inline title/body fallback data
  and deep-copies the `entEntityInstanceData` buffer rather than sharing the
  patch resource's handle, addressing the repeatable exit-time crash. It is
  retained at `H:\Ghostline-builds\gqt001-inline-file-deepcopy-20260724`;
  archive SHA-256 is
  `23A1F56163D58E975873E5D517802FA9EA9F050A0F895770574D9E2AE0518471`
  and custom ArchiveXL SHA-256 is
  `741803BB0866407CA7A5007150EBFDA26069154398C8BC664C1DE41B91D53E5A`.
- Runtime disproved that deep-copy candidate: both handle assignment and raw
  `RedPackage` buffer copying caused repeatable exit-time DEP crashes. The
  official ArchiveXL 1.27.0 DLL is restored. GQT001 now registers a complete
  Ghostline-owned laptop sector instead of patching vanilla persistent state.
  For rapid validation, its laptop, trigger, and marker are aligned near the
  corrected tabletop test position at
  `(-1058.3098, 1316.1430, 5.9833)`. The verified
  301-entry candidate is retained at
  `H:\Ghostline-builds\gqt001-owned-laptop-spawn-20260724`; all extracted
  payloads match source, all 181 tests plus 137 subtests pass, and archive
  SHA-256 is
  `6E630A53EFDF52CD2E0201AEED7D78D07817F21EA47A02C208113B90AD46A686`.
- Runtime confirmed the owned laptop is visible and usable at the tabletop
  position. The absent Files tab exposed an authoring bug: journal
  `fileEntryIndex` is the path-component index of the containing file entry,
  not a document-array index. Both the device content path and activation
  phase now use `5` for
  `onscreens/emails/quests/minor_quest/gqt001/files/diagnostic`. The installed
  diagnostic candidate is retained at
  `H:\Ghostline-builds\gqt001-journal-path-fix-20260724-185927` with archive
  SHA-256
  `060E81FD7174C88701F4FB78FE4CE92EAE53845545343DCD5F74CFA3EEA3978E`.
- A full vanilla comparison against SQ021 Randy's quest laptop found that a
  working quest computer carries two `ComputerControllerPS` chunks (raw
  fallback plus journal-backed content) and a
  `gameScanningComponentPS`, while the first Ghostline-owned candidates
  carried only one sparse controller. GQT001 now derives its owned laptop from
  that SQ021 node topology, supplies the diagnostic in both controllers,
  preserves the journal path in the journal-backed copy, and sets the
  standalone device on without relying on SQ021's scene activation event. The
  installed runtime candidate is retained at
  `H:\Ghostline-builds\gqt001-sq021-laptop-20260724-192838`; candidate and
  installed archive SHA-256 are
  `41CA8192553DCE4FFA47F7879E6CD6C3CBD6B852972365EF756E8ADBD8559AFB`.
- Runtime still omitted the Files tab with the SQ021 package topology. The
  remaining difference was the global persistent-device registry: like
  GQ000's access point, a streamed device may render and expose Use while its
  authored controller remains unresolved. GQT001 now emits
  `gqt001_custom_devices.devices` with the owned laptop's verified NodeRef
  hash (`3885000984853365008`), `ComputerControllerPS`, and world position;
  ArchiveXL merges it into Night City's global `03_night_city.devices`.
  The installed candidate is retained at
  `H:\Ghostline-builds\gqt001-device-registry-20260724-193826`; archive
  SHA-256 is
  `7183AB6D48A162B91A797C8A83F9B245F67B8590632F909AC11C1CFD2C4128E9`.
- The completed SQ021 trace disproved the device-registry hypothesis for
  Files content. Randy's laptop is sector-instance-backed and is absent from
  Night City's `.devices` and direct `.psrep` values. Its active
  `ComputerControllerPS` binds to `laptop_1.ent` through component CRUID
  `1131680419258347532`; the scanner binds through
  `1131680419258347552`. Earlier Ghostline generation replaced those IDs, so
  the visible and usable laptop silently fell back to the entity template's
  empty controller. Preserving the complete three-chunk SQ021 package and its
  CRUID dictionary made the custom Files entry work in game.
- The first successful runtime inherited SQ021's nine messages from the copied
  controller package. GQT001 now clears mail, internet, newsfeed, and SQ021
  scanner content from both controller variants and uses fresh NodeRef
  `#gqt001_terminal_laptop_r2`, because streamed device state is persisted in
  saves. The Files-only candidate is retained at
  `H:\Ghostline-builds\gqt001-files-only-r2-20260724-201904`; all 302
  extracted payloads match `source/archive`, all 181 repository tests pass,
  and candidate plus installed archive SHA-256 are
  `791ED71FB1B443734153304DB609961D193BF7ECEE300CD09818BEEE10D5C166`.
  The full vanilla chain and reusable authoring contract are documented in
  `docs/vanilla-sq021-computer-flow.md`.
- Runtime confirmed the `_r2` laptop exposes only its authored Files tab and
  opening SIGNAL DELAY advances the quest through the document-read fact. The
  remaining test failure was a manifest omission: the Patch phone phase set
  `gqt001_completed` and terminated without succeeding the quest journal
  entry. It now explicitly succeeds `quests/minor_quest/gqt001` before its
  output. The verified and installed completion candidate is retained at
  `H:\Ghostline-builds\gqt001-completion-20260724-221150`; all 302 extracted
  payloads match `source/archive`, all 181 repository tests pass, and candidate
  plus installed archive SHA-256 are
  `49410EDCC82EFFC054D1D2A83DA8C9EFDDE5B83EE41A3139E30BBEECF4B78669`.

### GQ002 — The Machine Stops

- `source/quests/gq002.quest.json` is an eleven-stage, shipping-valid typed
  manifest covering Patch's phone offer, Cinder's meeting scene, area entry,
  three ordered investigation clues, a readable shard, forced-hostile Tyger
  Claw security, a phone choice, a fact-backed outcome gate, relay operation,
  cleanup, and an outcome-aware Cinder debrief.
- The compiler now directly generates variable-size `investigate_clues`,
  `combat_encounter`, and `interact_device` phases. Phone choices may set
  branch facts, and `opening_branches` provides fact-conditioned outcome
  messages before a shared phone response group. Generated direct phases also
  reject forward handle references that WolvenKit cannot deserialize.
- Cinder's custom character resources, TweakXL record, scene, journal,
  onscreen localization, subtitle map, VO map, Kabuki world resources, and all
  eleven phase resources exist under their final `source/raw` and
  `source/archive` depot paths. The scene audit passes, the world inspector
  reports Cinder plus three security entries, all journal localization keys
  resolve, and the full 158-test repository suite passes.
- The selected native relay anchor is
  `Devices.Antenna_AP` at `(-1111.06006, 1456.39990, 16.359997)`. Two nearby
  native antenna access points provide the other scan targets. The reusable
  indexes contain 82 small access points, 161 large antennas, and 387
  decorative dishes. Loot containers are documented as deterministic sampling
  anchors for future pseudo-random character and encounter locations.
- Voice generation and selection are complete. The retained 72-WAV audition
  bank contains three V takes per line from the existing `v.pt`, three Cinder
  voice designs with three takes per spoken Cinder line, three reusable Cinder
  embeddings, and three design references. The selected Cinder design is
  `cinder-a-grounded-medic`; all eleven chosen takes are recorded with source
  path, measured duration, and SHA-256 in
  `source/raw/gq002_01_voice_selection.json`. The measured durations were
  written back to the dialogue manifest, the scene was regenerated, all eleven
  WEMs were converted successfully, and subtitle/VO coverage has no gaps or
  duplicate IDs.
- The final GQ002 static gate passes: all 21 CR2W resources serialize, all 158
  repository tests pass, and the scoped 278-entry archive extracts with every
  payload byte-identical to `source/archive`. The verified archive and
  nine-file ZIP are retained at
  `H:\Ghostline-builds\gq002-machine-stops-20260723`; archive SHA-256 is
  `783A11CF8FF248FEDFC3CC190BDE357B9D4309B2DEBE0D13A95BC5E0D15251EA`.
  The nine staged files are installed byte-identically under
  `H:\Cyberpunk 2077`, with the previous install backed up at
  `H:\Ghostline-backups\pre-gq002-machine-stops-20260723`.
- The remaining gate is an in-game run from a clean/pre-GQ002 save. World
  coordinates are extracted evidence and still require terrain, navmesh,
  interaction, combat, branch, journal, VO, and completion validation.
- The first runtime pass found Cinder intersecting rooftop geometry and exposed
  a generated-phase lifecycle defect: active journal and mappin nodes were also
  being used as completion signals, which immediately revealed later
  objectives and reached Cinder's relay decision before the relay work. The
  direct `reach_area`, `investigate_clues`, `read_shard`, `combat_encounter`,
  `interact_device`, `leave_area`, and `acquire_item` builders now serialize
  activation, the real condition, and separate completion-state nodes in strict
  order. Cinder's anchor was moved into the open rooftop area.
- The corrected 2026-07-23 runtime candidate is retained at
  `H:\Ghostline-builds\gq002-sequencing-fix-20260723`. Its 278 extracted
  payloads match `source/archive`, all 158 tests plus 80 subtests pass, and the
  archive SHA-256 is
  `E5BAA7FE06E2BBD85A6D094C897F1BF847C4B3076B57C0A8CE8749138E5A4D77`.
  All nine staged files are installed byte-identically; the preceding install
  is backed up at
  `H:\Ghostline-backups\pre-gq002-sequencing-fix-20260723`.
- The second runtime pass found Cinder and two security actors on invalid
  surfaces, six-metre contact volumes still too permissive, scan targets
  lacking vanilla quest highlighting, the shard activation swallowed by the
  final clue, and the terminal phone phase exiting without succeeding the root
  journal quest. The next candidate moves Cinder back onto the captured roof
  plane, reduces her engage/awareness radii to three metres, places all guards
  on the estimated walking plane around the relay, uses vanilla
  `SetDefaultHighlightEvent`/`QUEST` outline data with `Finished` scan
  conditions, activates the shard in its own stage, and explicitly succeeds
  `quests/minor_quest/gq002` after the final message.
- That candidate is retained at
  `H:\Ghostline-builds\gq002-runtime-fixes-20260723`. All 278 archive payloads
  match `source/archive`, 159 tests plus 80 subtests pass, and archive SHA-256
  is `F8738A94773AFFD415BEEA2C6A77CB21C22CF3B375ECAB88DC0E1C3CE2B98BC7`.
  The previous install is backed up at
  `H:\Ghostline-backups\pre-gq002-runtime-fixes-20260723`.
- The third runtime pass showed the original Kabuki rooftop remains unsuitable
  as a contact location, the second clue's extracted mappin transform is not a
  useful visual locator, shard journal activation alone does not produce the
  expected acquisition notice, and security must wait until V returns from the
  remote third clue. Cinder now uses the separately runtime-proven GQ001
  contact pad, the second clue relies on its quest outline without an offset
  pin, the last scan grants a real readable
  `Items.GhostlineHostageCircuit` shard, and combat is gated by a dedicated
  ten-metre trigger at the target relay. The guards are restored to the visible
  rooftop plane at `z=16.36` using the tighter horizontal cluster.
- The resulting candidate is retained at
  `H:\Ghostline-builds\gq002-location-combat-fix-20260723`. Its 278 payloads
  match `source/archive`; the source gate remains 159 tests plus 80 subtests.
  Archive SHA-256 is
  `34A7F1024B0BB5913F437CF63DEA9783E2636A064722D0E8A3416B0BEA20D0DF`,
  and the previous install is backed up at
  `H:\Ghostline-backups\pre-gq002-location-combat-fix-20260723`.
- The fourth runtime pass confirmed the real shard item and pickup
  notification, but exposed an incorrect `fileEntryIndex: 5` in the subsequent
  visited condition. `onscreens/...` paths use their top-level journal file
  entry at index `1`. The second relay pin is restored by binding its journal
  mappin directly to the native access-point NodeRef instead of the offset
  custom static marker. Every investigation clue now sends paired vanilla
  `SetDefaultHighlightEvent` reveal/conceal events around its completed scan.
- The resulting candidate is retained at
  `H:\Ghostline-builds\gq002-journal-highlight-fix-20260723`. All 278 extracted
  payloads match `source/archive`; 160 tests pass. Archive SHA-256 is
  `50134BD2F8BD116BA133F4AD456DD877562CDBCE97C290D600FB615710535328`,
  and the prior install is backed up at
  `H:\Ghostline-backups\pre-gq002-journal-highlight-fix-20260723`.
- Runtime clarified that opening a readable item from its pickup-notification
  overlay does not set the journal `visited` flag that the full Journal reader
  sets. GQ002 now explicitly accepts that preview route: it ensures the shard
  entry is active without a second notification, waits three seconds for the
  presentation, and completes the read stage from item ownership. Investigation
  highlight concealment is delayed one second beyond the device scan's
  `Finished` event so the vanilla device handler cannot immediately overwrite
  it. The second clue keeps a world/map icon but disables its misleading GPS
  projection to the native device's remote gameplay proxy.
- This candidate is retained at
  `H:\Ghostline-builds\gq002-preview-highlight-delay-20260723`. Its 278
  extracted payloads match `source/archive`; 160 tests pass. Archive SHA-256
  is `B2F418B7A80BA2950BC2A42C924A3D71061C45E0C55B2A0764935D835EC3C31D`.
- Runtime proved that the delayed conceal still leaves Ghostline's yellow
  quest highlight active on native antenna devices. The current candidate
  removes the custom `SetDefaultHighlightEvent` layer entirely and relies on
  the antennas' native blue scanner outline; `questScan Finished` remains the
  clue-completion condition. The readable-shard stage now waits on ownership
  of the real item instead of the Journal reader's visited flag, since the
  pickup-notification overlay does not emit that full-reader state.
- The verified and installed candidate is retained at
  `H:\Ghostline-builds\gq002-native-scanner-20260723`. All 278 extracted
  payloads match `source/archive`, all 160 tests pass, and the archive SHA-256
  is `9291927EAF3059628AC57A97AB71C65D2424652258BEFD86B90025A546395DDC`.
  The preceding nine-file install is backed up at
  `H:\Ghostline-backups\pre-gq002-native-scanner-20260723`.
- Runtime then proved that the readable shard's secondary action consumes it
  into the Journal, so an inventory-count condition still cannot complete the
  read stage. The current graph instead uses the final scan's
  `gq002_clue_invoice_scanned` acquisition fact, waits three seconds for the
  pickup presentation, succeeds the objective, and sets
  `gq002_shard_read`. It deliberately does not claim to detect whether the
  pickup overlay itself was read.
- The verified and installed replacement is retained at
  `H:\Ghostline-builds\gq002-shard-fact-20260723`. All 278 extracted payloads
  match `source/archive`, all 160 tests pass, and the archive SHA-256 is
  `82C221619EBA15D39D5F82D53B9CCE86AEEB9107AEC15166718143043284B312`.
  The preceding install is backed up at
  `H:\Ghostline-backups\pre-gq002-shard-fact-20260723`.
- Runtime confirms that replacement advances beyond the shard objective, but
  exposed the next security trigger waiting silently below the rooftop. Its
  centre was four metres beneath the native relay's `z=16.36` walking plane,
  leaving V on the boundary of the eight-metre-tall volume. The security
  trigger is now centred on the relay anchor and is ten metres tall.
- The verified and installed correction is retained at
  `H:\Ghostline-builds\gq002-security-trigger-20260723`. All 278 extracted
  payloads match `source/archive`, all 161 tests pass, and the archive SHA-256
  is `8FF1835A73F93B032FC4E1602FA1CC80234779706B085C385EBB7DFB91CE945B`.
  The preceding install is backed up at
  `H:\Ghostline-backups\pre-gq002-security-trigger-20260723`.
- Runtime confirms that entering the corrected trigger activates the security
  encounter and that the remainder of the quest works, but the trigger wait
  left the tracker blank after the shard stage. A dedicated generated
  `reach_area` stage now activates `Return to the target relay.` and a yellow
  GPS-enabled relay pin, succeeds and clears both on trigger entry, then hands
  off to the trigger-free security phase.
- The verified and installed navigation correction is retained at
  `H:\Ghostline-builds\gq002-return-relay-20260723`. All 279 extracted payloads
  match `source/archive`, all 162 tests pass, and the archive SHA-256 is
  `8F84793C62FF446B5A54E30429B03FD3C5E483AE0998D78372B596B407D1BF50`.
  The preceding install is backed up at
  `H:\Ghostline-backups\pre-gq002-return-relay-20260723`.

### Recovered Quest Design

- The original narrative brief has been recovered and normalized in
  `docs/quest-design.md`. It defines Ghostline, Morrow, Iris, Patch, the Tyger
  Claw/Arasaka-adjacent laundering route, the bridge-to-cache-to-drop flow,
  two archived conversations, and Morrow's delivery thread.
- `Quiet Spine` is the selected data-courier network name. Four unused names
  and alternate writing variants remain documented for later quests.
- The extraction and leave-area objectives, both archived-conversation journal
  entries, two matching readable shard items, and the separate datacache package
  are live. The active native deposit target is map-labelled Kabuki
  `drop_point_009` at `(-1168.66333, 1309.51709, 19.9768238)`, about 252.7
  units from the relay. Morrow's complete post-delivery phone conversation and
  both V response branches are wired into the generated delivery phase.
- The intended cabinet-style cache visual is baked into a larger recycling
  station proxy. Its inspected collision is actor 36 of 64 in
  `NormalCollisionNode_087`, source prefab hash `8325780084261042030`, rather
  than a standalone entity. The cache should therefore use a Ghostline-owned
  device/interaction overlay while preserving the vanilla mesh and collision.

### Meeting And Patch Baseline

- The early synchronized raw build crashed first near the bridge and then at
  whichever boundary launched the scene. The mq003-shaped lifecycle and a
  shared lipsync slot isolated the failure to scene initialization and produced
  the first stable end-to-end meeting run. Detailed crash evidence and failed
  probes remain in `docs/crash-investigation.md`.
- A custom Patch initially stayed invisible because the community requested
  the `.app` definition name instead of the root entity's exposed appearance.
  The live community now requests `ghostline_patch_default`, which maps to
  internal appearance `default`.
- Numeric sorting within each embedded locStore locale block repaired the
  blank/stale dialogue labels. Runtime testing confirms all three first-group
  labels and both second-group labels, along with Patch visibility, animation,
  subtitles, VO, acceptance, and journal cleanup.
- The stable world baseline keeps 12-unit-tall meeting triggers with horizontal
  radii `90/10/60/20` and a distinct always-loaded registry node ID. The current
  cache and delivery work deliberately preserves that meeting lifecycle.
- Historical build hashes and isolation packages are retained in
  `docs/testing.md`; the active delivery/debrief package and evidence are in
  `Next Milestones -> Pack And Test In Game` below.
- The archive still carries unvalidated `base\...` global overrides and 26
  valid WEM files while the VO map references 13. The overrides remain a
  packaging risk pending validation.
- The local game install has ArchiveXL and official TweakXL 1.11.3. Patch, the
  Ghostline faction, and both readable-shard records are runtime-confirmed;
  the separate datacache package and completion reward are part of the active
  delivery/debrief test.

### Project Registration

`source/resources/Ghostline.archive.xl` currently registers:

- `mod\gq000\phases\gq000.questphase` as a root questphase under
  `base\quest\cyberpunk2077.quest`.
- `mod\gq000\journal\gq000.journal`.
- Generic onscreen localization at
  `mod\ghostline\localization\en-us\onscreens\ghostline.json`.
- Quest onscreen localization at
  `mod\gq000\localization\en-us\onscreens\gq000.json`.
- Subtitle map `mod\gq000\localization\en-us\subtitles\gq000_01_subtitles_map.json`.
- VO map `mod\gq000\localization\en-us\vo\gq000_01.json`.
- Streaming block `mod\gq000\world\gq000_patch_meet.streamingblock`.
- Minimal device registry `mod\gq000\world\gq000_custom_devices.devices`,
  resource-patched into
  `base\worlds\03_night_city\_compiled\default\03_night_city.devices` so the
  custom relay's `AccessPointControllerPS` can be resolved reliably.

### Patch Character

- Patch has packed resources under
  `source/archive/mod/ghostline/characters/patch`, including `patch.ent`,
  `patch.app`, body/head meshes, textures, and morphtargets.
- Editable raw files exist for the root entity and appearance:
  - `source/raw/mod/ghostline/characters/patch/patch.ent.json`
  - `source/raw/mod/ghostline/characters/patch/patch.app.json`
- `source/resources/r6/tweaks/ghostline/character_patch.yaml` defines
  `Character.GhostlinePatch` with `entityTemplatePath:
  mod\ghostline\characters\patch\patch.ent`, display names using
  `gq_npc_patch`, `Factions.Ghostline`, and `voiceTag: gq_patch`.
- `source/resources/r6/tweaks/ghostline/faction_ghostline.yaml` defines
  `Factions.Ghostline`.
- `patch.ent` appearance `ghostline_patch_default` maps `appearanceName:
  default` to `mod\ghostline\characters\patch\patch.app`.
- Patch's `.app` head/body mesh components now point at real
  `mod\ghostline\characters\patch\...` depot paths instead of unresolved
  numeric `ResourcePath` IDs. The optional `h0_cyberware_face` mesh is disabled
  because its numeric mesh ID did not resolve to any packed game or mod
  resource.
- Patch's root mapping is named `ghostline_patch_default` and selects internal
  `.app` definition `default`. Runtime communities and `defaultAppearance`
  must use the root mapping name. The first custom run requested the internal
  name and produced an invisible but scene-acquirable puppet; generator/world
  regressions now enforce the correct namespace.
- Runtime retest of the corrected build confirms Patch renders at the bridge
  with the reviewed hair and outfit, participates in the scene, and presents
  all three first-menu labels correctly.
- Patch's root entity was compared with the downloaded NPV male template on
  2026-07-22. Both have the same 110 root components and, after excluding the
  intended appearance/default and export-timestamp fields, only those excluded
  fields differ. Treat the root as a versioned generator template rather than
  character-authored data.
- The downloaded female NPV root is now pinned separately as checked
  CR2W-JSON. It has 116 root components and its appearance uses
  `baseEntityType: WomanAverage`; it must not be synthesized from the
  110-component male root. Schema-v1 frame profiles now bind the root, entity
  type, PMA/PWA token, head preview, and creator range together, and validation
  rejects cross-frame templates, catalogs, and indexed overrides.
- The NPV template's Blender file contains import, shape-key application, and
  export scripts. Blender 5.1 has Cyberpunk IO Suite 1.8.0 installed locally,
  and the complete headless round trip is now scripted and smoke-tested. The
  Patch subset exported 13 morphtarget GLBs, requested temporary shape value
  22, exported 13 mesh GLBs, rebuilt 13 CR2W meshes, and verified every header
  and hash in isolated temporary output. A later target-name audit proved that
  22 selects missing `h21` and is a geometry no-op; the current builder derives
  actual targets from GLB metadata and permits Basis/value 1 plus named values
  2 through 21.
- The female PWA core exports 105 named targets, including all five `h21`
  variants, so creator values 1 through 22 are mechanically verified for the
  female-average profile. A full isolated build exported and rebuilt the four
  selected female head meshes as CR2W, and the generated female `.ent` and
  `.app` passed a WolvenKit deserialize/serialize round trip.
- The local WebGL UI renders the active frame's real morph-target head, applies
  all five facial controls immediately, and preserves Blender for the final
  bake only. It accepts a reviewed server-side manifest through `--manifest`;
  the default remains Patch. The male default preview is the 25.7-MiB core
  head; optional layers are loaded only on request.
- Iris now has a reviewed female-average character manifest at
  `source/characters/iris.character.json`. The creator pass selects face values
  `8/5/10/3/2`, the complete merlot tutorial hair bundle, a blue-pattern
  high-collar shirt, black/white ninja trousers, and tutorial boots. Her
  isolated source generation and four-mesh head bake pass; generated `.ent`,
  `.app`, localization, TweakXL, body, and head resources have been applied
  under `mod\ghostline\characters\iris`. Runtime spawn, animation, garment fit,
  materials, LODs, and streaming remain unvalidated.
- The installed-game path index currently contains 4,965 records from base and
  EP1: 1,329 clothing, 1,528 hair, 1,772 head, 144 body, and 192 player-item
  appearance resources. The UI searches slot/frame/family/path metadata and
  successfully uncooked Patch's military boot to an isolated GLB preview. PMA
  torso, legs, and feet primary meshes are selectable for Patch, while PWA
  torso and legs are selectable for the female catalog. The UI reads real
  appearances from the cooked mesh, records a frame-constrained canonical
  indexed override, and the generator updates both appearance component copies.
  PWA feet remain preview-only until a suitable garment anchor is validated.
  Live QA assigned Patch's military boot `black_red` appearance and passed full
  manifest validation.
- Patch's reviewed design manifest now selects the black-carbon `hh_146` dread
  undercut, a `quest005_grey` high-collar shirt, `camo_black` computer cargo
  trousers, and the existing black/red military boots and braindance specs.
  The look follows the quest's low-profile signal-broker characterization:
  practical dark layers with the existing spiral eyes, magenta/rose face
  details, gold hardware, and red accents providing the deliberate flair.
- The curated `hh_146` option carries its vanilla animgraph, dangle rig, NPC
  shadow, component-class change, skinning target, and parent bindings. New
  binding handles are allocated after the template maximum; browser and CLI
  generation agree, and the resulting 105 handle IDs are unique. An isolated
  WolvenKit CR2W round trip preserved the complete bundle topology. The
  original Patch selections remain covered by a semantic-equivalence
  regression test.
- This reviewed design has been applied to `source/raw`, rebuilt into
  `source/archive`, packed, and installed. The indexed shirt and trousers still
  retain their original curated cuff/shadow companions, and the complete look
  needs focused in-game tests for fit, animation, LODs, scene use, and
  streaming.
- The 17 `ep1\...` string occurrences in Patch's root entity are identical to
  the downloaded male template. Resolve this at the reusable template layer or
  declare Phantom Liberty as a generated-character dependency.
- `source/characters/female-example.character.json` and its dedicated catalog
  now provide a checked female-average authoring fixture. Generation clones the
  35-component tutorial `casual` appearance, rewrites 18 numeric tutorial mesh
  IDs to explicit character-owned paths, and stages those meshes plus four
  texture dependencies. The full-body mesh still embeds the original tutorial
  texture namespace, the root retains EP1 dependencies, and the resulting NPC
  has not been validated in game; do not treat this fixture as shipping content.
- `docs/character-creation-pipeline.md` defines the manifest-driven generator,
  machine-readable catalogs, validation boundary, current local UI, and Patch
  migration plan.
- Packaging still has a risk: `source/archive/base` contains copied
  `base\characters\head\player_base_heads\player_man_average\...` resources
  that should not ship as global base-path overrides unless validated.

### Quest Phases

- Packed and raw questphase resources exist for:
  - `mod\gq000\phases\gq000.questphase`
  - `mod\gq000\phases\gq000_patch_meet.questphase`
  - `mod\gq000\phases\gq000_post_accept.questphase`
  - `mod\gq000\phases\gq000_delivery.questphase`
- `gq000.questphase` is now the staged root flow:
  `input -> phone start guard -> Patch phone message -> phone choice group ->
  wait for On my way reply -> meet objective/description/mappin ->
  gq000_patch_meet phase -> accepted-state check -> gq000_post_accept phase ->
  gq000_delivery phase`.
- The root phase no longer starts the meeting objective from the bridge trigger
  and no longer sets `gq000_done`. Current staged facts include
  `gq000_phone_start_sent`, `gq000_phone_reply_on_my_way`,
  `gq000_job_accepted`, `gq000_02_started`, `gq000_cache_acquired`, the
  engine-owned deposit fact `gq000_datacache`, `gq000_cache_delivered`, and
  `gq000_completed`.
- The Patch phone message has been confirmed to trigger in game when tested
  from a fresh save.
- The current raw `gq000_patch_meet.questphase` is a 10-node, 10-edge flow:
  input -> activate community `patch/default` -> wait for `CharacterSpawned`
  on `#gq000_01_com_patch_bridge` -> wait for `#gq000_01_tr_setup` ->
  checkpoint -> start
  `mod\gq000\scenes\gq000_patch_meet.scene` at
  `#gq000_01_sm_patch_bridge`.
- Scene exit `end` terminates the meeting phase without acceptance. Scene exit
  `job_accept` succeeds `gq000_01_obj_meet_patch`, disables
  `gq000_01_qmp_patch_bridge`, sets `gq000_job_accepted = 1`, and then
  terminates. The root phase's accepted-state check then starts the current
  post-accept cache phase.
- `gq000_post_accept.questphase` is now a generated 43-node, 44-edge cache
  flow. It activates the reach objective and mappin, disables the relay,
  activates the whole Tyger Claw community, waits until the entire community
  is spawned, then waits for V at the site. The 25-unit arrival gate succeeds
  the reach objective and swaps to the extraction objective while also fanning
  into an independent, vanilla-`mq022` hostility branch. That branch resolves
  each named guard, applies the same `neutral -> hostile` attitude transition,
  assigns V as the immediate combat target, and explicitly injects V as the
  combat threat. A dedicated quest
  mappin targets the relay's live `UI_Interaction` slot while the phase enables
  the relay and waits for native
  breach success, immediately sets `gq000_cache_acquired`, uses a one-second
  presentation delay instead of a UI-visibility gate, disables the relay,
  succeeds extraction, hides the terminal pin, activates and grants both Quiet
  Spine shards plus `Items.gq000_datacache`, tracks a leave-area objective, and
  deactivates surviving guards after V leaves the larger cleanup radius.
- `gq000_delivery.questphase` is a generated 25-node, 25-edge delivery and
  debrief flow. It confirms the package is present, fires the vanilla
  `ReserveItemToThisDropPoint` contract at live Kabuki `drop_point_009`, waits
  for the package `friendlyName` fact `gq000_datacache`, closes the delivery
  objective, sets `gq000_cache_delivered`, runs both Morrow reply branches,
  waits for the final message, grants `QuestRewards.gq000_completion`, sets
  `gq000_completed`, and succeeds the quest root.
- Guard kills are not a gate. Stealth and combat are both valid. Activation
  uses vanilla `None`/`None` whole-community semantics plus an explicit
  readiness gate; cleanup deactivates the same whole community. The hostility
  side branch also does not gate objective progression if a guard has already
  died or cannot be resolved.

### Scene

- Packed and raw scene resources exist at
  `mod\gq000\scenes\gq000_patch_meet.scene`.
- The current raw scene is generated from
  `tools/gq000_patch_meet.scene-spec.json`. It contains 15 graph nodes, 16
  edges, 13 spoken lines, two choice nodes, two end nodes, and four
  scene-local quest nodes.
- The screenplay store contains exactly the five connected choices:
  `What's the job?`, `Ghostline?`, `Why me?`, `I'm in.`, and
  `Who's behind it?`. The three orphaned options from the crashed current-raw
  build are gone.
- Community activation and `CharacterSpawned` readiness are owned by the
  meeting questphase. At setup range the scene starts Puppet AI in parallel
  with the ordered bridge-case-mood -> someone-coming -> opening-line ->
  engage -> first-choice path. This matches `mq003`'s division of lifecycle
  ownership and avoids registering the 60- and 20-unit waits only after the
  player is already inside the 10-unit engage trigger.
- Exit points `end` and `job_accept` are both declared. Acceptance reaches
  `job_accept` through end node 19; end node 18 is currently not reached by an
  active dialogue branch, so the non-accept fallback still needs runtime/design
  validation.
- All five choice locstrings have the audited vanilla-style
  `db_db`/`pl_pl`/`en_us` locStore descriptor coverage. Runtime testing proved
  that locale grouping alone is insufficient: every locale block must also be
  numerically sorted by `locstringId`, as it is in all four audited vanilla
  scenes. The generator, validator, and checked-in-raw regression now enforce
  that order; runtime testing confirms the repaired five-label result.
- Questphase journal paths follow the journal file-entry index rule: phone
  contact paths use `fileEntryIndex: 1`, while quest objective, description,
  and quest map pin paths under `quests/minor_quest/gq000` use
  `fileEntryIndex: 2`.
- The generator/spec pins `Header.ExportedDateTime`, emits multiple configured
  end nodes, and uses full unsigned 64-bit FNV output for event and locStore
  IDs. Raw validation now passes with no drift errors.
- Runtime testing confirmed the previous `INT63_MASK` probe was the approach
  crash source. Scene event RUIDs and locStore variant IDs must keep the full
  unsigned 64-bit FNV output; do not mask them down to signed 63-bit values.
- The current shared-slot diagnostic scene assigns both the Patch-role actor
  and V `lipsyncAnimSet.id: 0` and contains exactly one
  generic lipsync resource reference. The previous scene assigned V slot `1`
  while both raw slots used
  the same depot path; its packed import table and runtime lookup exposed only
  one distinct resource before the engine requested index `1`. The shared-slot
  build completed the full meeting route without a crash, strongly confirming
  that cardinality mismatch as the scene-start failure.
- The previous installed 14-node scene and late-gated meeting phase remain
  recoverable from
  `H:\Ghostline-backups\pre-mq003-sequence-20260721-233546`; see
  `docs/testing.md` for the historical baseline.

### Dialogue Localization And VO

- Subtitle and VO map raw resources for `gq000_01` are aligned by string ID.
- `source/raw/gq000_01_manifest.json` contains 13 spoken records with key,
  string ID, speaker/addressee, text, audio path, and duration, plus five choice
  records with key, string ID, and text only.
- The `gq000_01` spoken locstring IDs were regenerated across the manifest, raw
  subtitles, raw VO map, and generated scene during the intro-choice semantics
  probe. Choice locstring IDs remain scene-embedded and do not belong in the
  subtitle or VO maps.
- The VO map points at 13 current `.wem` paths under `source/archive`.
  `generated` retains those 13 authored WAVs plus 13 byte-identical legacy
  hash-name duplicates; the manifest-filtered converter selects only the
  current basenames.
- A subtitle map resource now registers the subtitle entries with ArchiveXL.
- Runtime testing confirmed every spoken subtitle and VO line in the meeting
  scene plays correctly.
- The manifest-filtered Wwise 2025.1.7 conversion pass processes exactly 13
  active WAVs; a `-NoCopy` verification regenerated all 13 current WEMs
  byte-identically. It intentionally does not remove the 13 legacy WEM names
  retained for candidate-archive parity.
- The scene still uses a base generic facial lipsync animset as a placeholder;
  Ghostline-owned lipsync `.anims` files have not been integrated.

### Journal And Quest UI

- Packed and raw `gq000` journal resources exist at
  `mod\gq000\journal\gq000.journal`.
- The journal defines:
  - quest root `quests/minor_quest/gq000`
  - phase `quests/minor_quest/gq000/gq000_01`
  - objective `quests/minor_quest/gq000/gq000_01/gq000_01_obj_meet_patch`
  - description
    `quests/minor_quest/gq000/gq000_01/gq000_01_obj_meet_patch/gq000_01_desc_meet_patch`
  - quest map pin
    `quests/minor_quest/gq000/gq000_01/gq000_01_obj_meet_patch/gq000_01_qmp_patch_bridge`
  - point of interest
    `points_of_interest/minor_quests/gq000_01_poi_patch_bridge`
  - phase `quests/minor_quest/gq000/gq000_02`
  - objective `quests/minor_quest/gq000/gq000_02/gq000_02_obj_reach_cache`
  - description
    `quests/minor_quest/gq000/gq000_02/gq000_02_obj_reach_cache/gq000_02_desc_reach_cache`
  - quest map pin
    `quests/minor_quest/gq000/gq000_02/gq000_02_obj_reach_cache/gq000_02_qmp_cache`
  - extraction objective
    `quests/minor_quest/gq000/gq000_02/gq000_02_obj_extract_cache`
  - extraction quest map pin
    `quests/minor_quest/gq000/gq000_02/gq000_02_obj_extract_cache/gq000_02_qmp_extract_cache`,
    targeting `#gq000_02_ap_cache` slot `UI_Interaction`
  - leave-area objective
    `quests/minor_quest/gq000/gq000_02/gq000_02_obj_leave_area`
  - phase `quests/minor_quest/gq000/gq000_03`
  - delivery objective
    `quests/minor_quest/gq000/gq000_03/gq000_03_obj_deliver_cache`
  - delivery description
    `quests/minor_quest/gq000/gq000_03/gq000_03_obj_deliver_cache/gq000_03_desc_deliver_cache`
  - delivery map pin
    `quests/minor_quest/gq000/gq000_03/gq000_03_obj_deliver_cache/gq000_03_qmp_drop_point`,
    targeting Ghostline's always-loaded `#gq000_03_mp_drop_point` marker at
    live Kabuki `drop_point_009`; it uses yellow `DefaultQuestVariant`
  - archived conversations
    `onscreens/emails/quests/minor_quest/gq000/shards/quiet_spine_01` and
    `onscreens/emails/quests/minor_quest/gq000/shards/quiet_spine_02`
  - Patch contact thread `contacts/patch/gq000_01_start` with message
    `01_msg_patch_bridge`, choice group `02_ch_meet_patch`, and reply choice
    `02a_ch_on_my_way`
  - Morrow contact thread `contacts/morrow/gq000_04_delivery` with two opening
    messages, two V choices, their branch-specific replies, and final
    `05_msg_more_work`
- Quest onscreen localization exists at
  `mod\gq000\localization\en-us\onscreens\gq000.json`.
- Journal references in the questphase and scene use full journal paths rather
  than bare leaf IDs.
- The quest map pin and POI mappin have been moved to dedicated always-loaded
  marker `#gq000_01_mp_patch_bridge`. Vanilla files confirm this must stay
  separate from scene marker `#gq000_01_sm_patch_bridge`. Runtime testing
  confirmed the meeting tracker/mappin path and its cleanup; explicit map-screen
  and POI presentation still need focused validation.
- The next objective uses Ghostline-owned always-loaded marker
  `#gq000_02_mp_cache` at the selected Watson/Kabuki cabinet relay.
- The delivery objective also uses a Ghostline-owned always-loaded marker,
  `#gq000_03_mp_drop_point`, colocated with the live deposit machine. ArchiveXL
  logged that it could not resolve the direct cooked cross-world mappin; the
  generated phase still reserves the item to the native device itself.
- Runtime testing confirmed acceptance clears the meeting flow, activates
  `Go to the cache coordinates.`, and displays the cache marker at about 275
  metres from the bridge.

### World Placement And Community

- Generated raw and packed world resources exist for:
  - `mod\gq000\world\gq000_patch_meet.streamingsector`
  - `mod\gq000\world\gq000_always_loaded.streamingsector`
  - `mod\gq000\world\gq000_patch_meet.streamingblock`
  - `mod\gq000\world\gq000_custom_devices.devices`
- The world spec uses captured origin `(-795.7447, 390.34177, 17.272781)`.
  Yaw remains provisional because the captured `ToVector4` did not include
  actor heading.
- The streaming block contains a Quest descriptor for the quest sector and an
  AlwaysLoaded descriptor for the always-loaded sector. The quest descriptor
  binds `questPrefabNodeRef: $/mod/gq000/#gq000_pr_patch_meet`.
- The quest sector contains six trigger areas, one native access-point device,
  five AI spots, and two streamable community areas.
- The four meeting trigger areas use 12-unit-tall volumes centered around the
  captured bridge origin. Their restored footprint radii are 90 for setup, 10
  for engage, 60 for bridge-case mood, and 20 for someone-coming. Prior
  testing showed that raising/centering the volumes fixed bridge-height misses;
  restoring the smaller horizontal radii prevents the nearby fast-travel point
  from immediately entering setup.
- The always-loaded sector contains the community registry and concrete marker
  nodes needed for early NodeRef resolution: `#gq000_01_sm_patch_bridge`,
  `#gq000_01_mp_patch_bridge`, `#gq000_02_mp_cache`, and
  `#gq000_03_mp_drop_point`.
- The community registry maps entry `patch/default` to source object id
  `7897875840529598144` and spot NodeRef
  `$/mod/gq000/#gq000_pr_patch_meet/#gq000_01_spot_patch_bridge`.
- The separate always-loaded registry node now has global ID
  `7571954536596633334`. It no longer collides with the streamed community
  area's global/source ID `7897875840529598144`; generator tests reject any
  future collision.
- The active world spec now uses `Character.GhostlinePatch` and exposed root
  appearance `ghostline_patch_default` for the `patch/default` entry. The
  preceding Judy route remains the stable lifecycle baseline.
- The cache site adds dormant device `#gq000_02_ap_cache`, a 25-unit arrival
  trigger, a 75-unit cleanup trigger, and three inactive-on-start Watson/Kabuki
  Tyger Claw entries. The streamable guard community is cache-local and uses
  verified records from `ma_wbr_jpn_013_claws_com.community`; activation is
  whole-community followed by a whole-community `CharacterSpawned > 0`
  readiness gate. Runtime proved all three records spawn and that the short
  patrol works, but the prior border-patrol-derived threat node left them
  passive because it did not name a target. The arrival trigger now uses the
  per-entry `mq022_combat.questphase` sequence and explicitly targets `#player`.
  All three
  initial placements are within 4.85–6.66 units on the cabinet's exterior side;
  one gunner cycles two finite sequenced workspots and two guards remain close
  sentries. The relay mount remains `(-1000.02, 1497.2208, 8.3)` and now uses
  absolute yaw `178.6`, exactly a `-90` degree shortest-path change from the
  visibly perpendicular `-91.4` runtime build. Runtime has now confirmed the
  transform, patrol route, and explicit-player aggression setup.
- The access point reuses the vanilla physical access-point entity and native
  `AccessPointControllerPS`. Its instance starts `OFF`, autoscales, and uses a
  file-unique RedPackage buffer ID. A minimal Ghostline `.devices` registry is
  patched into Night City's global device registry for controller lookup. A
  `.psrep` persistence resource is optional and deferred; no sector
  persistent-state clone or custom controller is needed.
- See `docs/world-references.md` for the resolved prefab/NodeRef model and
  current world findings.

### Generated And Editor Support Data

- Prefer `source/raw` over `generated` when preparing CR2W assets for use.
- `generated` contains older generated CR2W snapshots. Its temporary exception
  is the tracked authored WAV bank: use the current manifest and conversion
  helper rather than treating every WAV there as active.
- `GraphEditorStates` contains WolvenKit editor support data only. Do not
  treat it as packed asset source of truth.

## Open Blockers

- Decide whether the currently unreachable non-accept `end` scene branch is
  required. Both exit points exist and the phase handles `end`, but active
  dialogue progression currently reaches only `job_accept`.
- Rebuild the scene marker under a vanilla-style scene-prefab child path when
  fresh world/scene tooling replaces the current generated shape.
- Recover or deliberately choose Patch's eyes, nose, mouth, jaw, and ears
  creator indices before regenerating his real head. Resolve the documented
  option-22 versus missing-`h21` mismatch rather than treating the shape-22
  toolchain smoke test as a face build.
- Enrich the path-only installed-game catalog through TweakDB/item records,
  root `.ent` mappings, `.app` appearances, component/control entities, chunk
  masks, visual tags, dependencies, and material graphs. Exact mesh appearance
  enumeration, provisional PMA torso/legs/feet assignment, and provisional PWA
  torso/legs assignment are implemented; complete bundle resolution is not.
  The audit bounds the effective wardrobe at 158 controller apps, 5,031
  appearance definitions, 12,850 components, and 739 referenced meshes; use a
  long-lived WolvenKit-backed C# helper rather than thousands of CLI launches.
- Add whole-character preview composition and RED material handling. Current
  item previews are neutral-material individual meshes and do not prove NPC
  garment fit or runtime deformation.
- Validate the female example in game: appearance/material resolution, facial
  animation, LODs, streaming, and PWA garment deformation. Patch or custom-path
  the tutorial full-body mesh's internal texture references before treating the
  original tutorial namespace as removable, and review a valid PWA feet anchor
  before enabling indexed female footwear assignment.
- Determine whether WolvenKit's garment-support warnings during head mesh
  re-import are harmless for these resources or require adjusted import
  settings before using generated heads in game.
- Decide whether `source/archive/base` resources are still required. They
  should be excluded from normal install archives unless their impact is
  validated.
- Move the 13 current authored WAVs to an explicit source-audio directory, then
  retire the 13 legacy hash-name WAV/WEM duplicates. Until then, the converter
  must keep filtering through `source/raw/gq000_01_manifest.json`.
- Audit remaining `ep1\...` animation/effect dependencies in Patch's entity or
  explicitly require Phantom Liberty if Patch still crashes when streamed.

## Next Milestones

### 1. Preserve The Stable Meeting Scene

- Runtime testing now confirms custom Patch visibility, both choice groups,
  subtitles/VO, `job_accept`, journal cleanup, and the cache handoff.
- Decide later whether the non-accept `end` branch needs different quest
  behavior; it is no longer part of the cache-encounter test gate.
- Continue using `tools/generate_scene.py` and the audited scene spec as source
  of truth rather than patching packed scene CR2W manually.
- Keep failed probe workarounds in `docs/crash-investigation.md` as historical
  context only.

### 2. Validate Meeting-Location World Data

- The full Judy route and subsequent custom Patch route confirmed that
  ArchiveXL loads the streaming block and that the active community, scene
  marker, four meeting triggers, meeting mappin, and cache handoff resolve in
  game.
- Validate explicit map-screen/POI presentation and the future nested
  scene-marker hierarchy separately from the already working HUD route.
- Tune Patch yaw, workspot placement, and trigger radii against the real
  location geometry.

### 3. Build The Character Pipeline And Validate Patch

- Schema-v1 male/female frame validation, separate vetted roots and catalogs,
  isolated source and template-asset staging, semantic Patch baseline
  comparison, the complete headless head build, live morphable frame-specific
  head preview, archive-derived path index, on-demand mesh preview, real
  mesh-appearance enumeration, provisional indexed PMA torso/legs/feet and PWA
  torso/legs selection, and local web UI are implemented and covered by
  regression tests.
- Enrich the provisional primary-mesh selections into complete selectable
  bundles, add indexed hair/head/arms/item support, compose compatible
  body/head/clothing layers in one viewport, add material conversion, and add a
  fresh-character bootstrap command.
- Recover or choose Patch's real head-shape values, resolve the head-import
  garment warning, then eliminate Patch's global `base\...` head overrides.
- Run the generated female fixture in game, resolve its inherited EP1/tutorial
  texture dependencies, and validate a PWA feet garment anchor before promoting
  it into a reusable shipping-character template.
- TweakXL 1.11.3, the applied generated appearance, and the restored
  `Character.GhostlinePatch` registry are installed and runtime-confirmed.
- Continue custom-pathing or replacing Patch dependencies only if missing
  resource hashes change or Patch-specific crashes remain.

### 4. Extend The Quest Beyond Acceptance

- The first cache slice after `job_accept` is implemented through native breach
  success, readable-shard grants, `gq000_cache_acquired`, a visible leave-area
  beat, and delayed guard cleanup.
- Runtime testing confirms all three guards spawn, the native breach succeeds,
  both readable shards and Journal entries work, and the leave-area transition
  completes. The final guard test also confirmed close placement, finite patrol,
  proximity hostility, absolute yaw `178.6`, terminal-specific extract pin,
  and surviving-guard cleanup together.
- Kabuki `drop_point_009`, the separate quest package, native reservation and
  deposit fact, yellow delivery UI marker, Morrow thread, completion reward,
  and quest success are implemented and runtime-confirmed. The prior target
  was physically occluded, and ArchiveXL could not resolve its direct cooked
  mappin. The first successful complete route exposed only presentation state:
  the custom pin rendered near the entity root and a stale dotted GPS leg
  continued toward the bridge. The next candidate uses the native two-unit
  interaction height and clears previous mappins when delivery activates.
- Keep prefab NodeRef lifecycle aligned with the resolved model in
  `docs/world-references.md`.
- Typed quest composition schema v1 now represents linear
  `meet_contact`, `hack_access_point`, `deliver_drop_point`, and
  `phone_conversation` blocks. `tools/quest_compiler.py` validates strict stage
  inputs, resource readiness, duplicate IDs, planned assets, CR2W handle
  uniqueness, and handle resolution. It emits a deterministic orchestration
  questphase, normalized build plan, and child phases. Runtime-proven meeting,
  hacking, and delivery graphs are instantiated from raw templates with strict
  quest-local scalar bindings; phone conversations are generated directly
  from typed messages and paired choice/reply paths. The checked `gq001`
  acceptance manifest represents
  `meet Patch -> hack relay -> meet Iris -> deliver datacache`. Iris's
  character, world placement, journal, scene, selected VO, subtitle/VO maps,
  and phase handoff are now authored. `meet_contact` orchestration now
  activates the contact objective, description, and map pin before launching
  each child phase.
  All four instantiated children, the orchestration graph, and the standalone
  phone example passed isolated WolvenKit deserialize/serialize round trips.
  Evidence is retained at
  `H:\Ghostline-audits\typed-quest-final-20260723`, and the full regression
  suite passes 116 tests.
- A generated vanilla quest research catalog now links IGN's Main Jobs, Side
  Jobs, and Gigs indexes to the exact records in `H:\projects\quest.json`.
  `docs/vanilla-quest-reference` contains structural Markdown for 57 main
  jobs, 85 side jobs, and 85 gigs; `reference/quests/ign-link-map.json`
  preserves the machine-readable IGN URL to journal hash/path mapping.
  Objective text, phase paths, map pins, and inferred reusable building blocks
  can now be searched before opening the corresponding vanilla CR2W resources.
- Typed schema v1 now defines twenty-three additional reusable blocks:
  `reach_area`, `leave_area`, `acquire_item`, `read_shard`,
  `interact_device`, `combat_encounter`, `investigate_clues`,
  `optional_condition`, `choice_gate`, `escort_npc`, `carry_npc`, and
  `deliver_vehicle`, `time_gate`, `read_terminal_document`,
  `stealth_monitor`, `plant_item`, `defend_target`,
  `release_or_rescue_npc`, `enter_vehicle`, `ride_with_contact`, `drive_to`,
  `steal_vehicle`, and `vehicle_cleanup`. The direct blocks have deterministic compiler-generated
  child graphs and handle-integrity tests. Nineteen blocks use strict raw
  phase-template contracts because their device, AI, branching, carry, and
  vehicle behavior must retain proven engine topology. A targeted 28-phase
  vanilla CR2W/JSON corpus with depot-path provenance is stored under
  `reference/vanilla_quest_blocks` to support reducing and validating those
  templates. All nineteen reduced templates are now checked in under
  `source/raw/mod/ghostline/quest_blocks/templates`, resolve automatically
  from ordinary typed manifests, and retain explicit custom-template
  overrides for advanced variants. The original four-stage direct and
  eight-stage template acceptance quests compile with no planned stages.
  Their 14 total
  orchestration/child resources passed WolvenKit deserialize/serialize
  round trips, with evidence at
  `H:\Ghostline-audits\quest-building-blocks-direct-20260723` and
  `H:\Ghostline-audits\quest-building-blocks-template-20260723`. Compiler,
  schema, generator-exact, binding, and handle tests pass as part of the
  full regression suite. Template-backed blocks remain structurally
  validated rather than in-game runtime-proven until used by a playable quest.
- The higher-order vanilla extraction now includes
  `reference/vanilla_quest_blocks`: `sq021_randys_room` for
  `read_terminal_document`, `sq011_concert`/`sq011_follow_up` for
  `time_gate`, and the existing complete `sts_wbr_jpn_03` pair for
  `stealth_monitor`. The extracted evidence establishes that terminal reads
  are computer-graph outputs routed into a dedicated fact, elapsed game time
  is a standalone `questGameTimeDelay_ConditionType` gate, and stealth failure
  must be monitored in parallel with the main flow. Exact nodes, proposed
  contracts, and reduction boundaries are recorded in
  `reference/vanilla_quest_blocks/EXTRACTION-NOTES.md`. They are joined by
  `plant_item`, `defend_target`, `release_or_rescue_npc`, expanded
  `escort_npc`, and five vehicle lifecycle templates. `time_gate` is
  compiler-generated; the other advanced blocks have strict typed contracts
  and Ghostline-owned raw templates. All eleven advanced templates pass
  handle validation and WolvenKit 8.17.4 deserialize/serialize round trips.
  They remain structurally validated rather than in-game runtime-proven.
- Reusable world-location discovery now has an exhaustive binary-sector pass,
  a deterministic WolvenKit serialization stage, a normalized placement
  catalog, and a separate runtime curation layer. The v1 discovery accounts
  for 15,859 of 23,691 extracted exterior sectors across terminals, access
  points, antennas, doors/restraints, plant targets, drop points, loot
  anchors, and vehicles. The bounded detailed catalog contains 10,055
  placements from 760 serialized sectors and supports seeded filtering by
  category, capability tag, district, area, and radius. Default selection
  requires both accessibility and quest safety to be runtime verified; known
  vanilla-owned devices remain searchable but ineligible. The schemas,
  commands, current coverage, and test-quest routing are documented in
  `docs/world-asset-catalog.md`.
- The first isolated runtime harness is now specified as
  `gqt001_signal_delay`: reach a quest-owned computer, read a computer-hosted
  diagnostic through a real scene output, wait ten seconds of elapsed game
  time, and answer Patch by phone. Its Kabuki laptop hit is retained only as
  an unverified placement reference because the native device belongs to
  `sts_wat_kab_101`; the world, terminal scene, journal, and localization
  stages remain explicitly planned until authored and tested.

### 5. Validate Audio Packaging

- All 13 current subtitles, VO-map entries, and `.wem` assets played correctly
  in the stable meeting route. Revalidate that alignment after future dialogue,
  scene-line, or audio-map edits.
- Add Ghostline-owned lipsync resources if the final scene presentation needs
  them.

### 6. Pack And Test In Game

- Patch and Iris now both use six-unit opening-line awareness triggers. Their
  larger setup/mood streaming ranges and final interaction gates are unchanged.
  All 116 tests pass, the 226-entry archive has zero extracted payload
  mismatches, and installed SHA-256 is
  `AA0686E4604F94E4BBA79295041A9643C2D87891581D66CE1D89C743CA96D1E4`.
  Evidence is retained at
  `H:\Ghostline-builds\contact-trigger-6m-20260723-145709`; the preceding
  install is backed up at
  `H:\Ghostline-backups\pre-contact-trigger-6m-20260723-145805`.
- The next runtime candidate reduces Iris's opening-line awareness trigger from
  20 to 12 units while retaining its four-unit vertical band. It also moves the
  custom `drop_point_009` quest marker from the kiosk root to the transformed
  `main_slot/navQuery` approach point, so GPS targets walkable ground in front
  of the machine; the live drop-point NodeRef and deposit flow are unchanged.
  All 116 tests pass, the 226-entry archive has zero extracted payload
  mismatches, and installed SHA-256 is
  `B2917118EF08A865A6A5F2547BF5869514B84F7175ADAD7732F2AF02E7DE368E`.
  Evidence is retained at
  `H:\Ghostline-builds\iris-gps-nav-20260723-143811`; the preceding install is
  backed up at
  `H:\Ghostline-backups\pre-iris-gps-nav-20260723-143913`.
- The 2026-07-23 title/landing-trigger revision restores the displayed quest
  name to `Ghostline` and narrows Iris's awareness and engage triggers from
  12-unit bridge-style vertical columns to four-unit bands centered on the
  upper landing. Setup and mood ranges remain tall for early streaming and
  scene preparation. The 226-entry archive has zero extracted payload
  mismatches, all 116 tests and 9 subtests pass, and installed SHA-256 is
  `DBE3CF8D7C03A3F46854AED7B215C32EDD648E851D092C7F6389A0AA8685D6A1`.
  Evidence is retained at
  `H:\Ghostline-builds\gq001-title-trigger-20260723-141725`.
- The corrected `gq001` replacement candidate now starts with a generated
  `phone_job_offer` child matching the proven `gq000` opening lifecycle:
  Patch's message and choice group activate, the phase waits for “On my way,”
  and only then does the reusable `meet_contact` block activate the bridge
  objective, description, and mappin. The complete five-stage flow is
  `phone offer -> meet Patch -> hack relay -> meet Iris -> deliver cache`.
  The 226-entry archive was extracted with zero payload mismatches, all 116
  tests and 9 subtests pass, and the installed SHA-256 is
  `418815B8890300BC1F2880094223BCF81EE60A2E352C5FD8F3D9B0F0F25A55C3`.
  Evidence is retained at
  `H:\Ghostline-builds\gq001-phone-iris-20260723-135831`; the preceding install
  is backed up at
  `H:\Ghostline-backups\pre-gq001-phone-20260723-135908`.
- The first complete `gq001` Iris candidate was compiled, deserialized, packed,
  extracted, payload-verified, and installed on 2026-07-23. It contains 225
  archive entries with no payload mismatches and activates only the `gq001`
  root while retaining `gq000` shared Patch/cache registrations. All 116 tests
  and 9 subtests pass. Installed archive SHA-256 is
  `456604460AAAC6FD8A209EB40AAE09E3D0AC1E2DA8992F96E545E5E7B89E9EDE`.
  Evidence is retained at
  `H:\Ghostline-builds\gq001-iris-20260723-133033`; the replaced install is
  backed up at
  `H:\Ghostline-backups\pre-gq001-iris-20260723-133135`.
- The 2026-07-23 delivery GPS/height candidate is generated, deserialized,
  byte-identical after CR2W round trips, packed, extracted, payload-verified,
  installed, and wrapped in a verified seven-file ZIP. All 103 tests pass.
  Relative to the complete runtime-confirmed route, exactly the delivery phase
  and journal changed: delivery activation now clears stale mappin/GPS state,
  and the yellow pin uses the native two-unit interaction height. Installed
  archive SHA-256 is
  `7C3BB9844EE0DD8BC65C1883D61AD0307E89593DFBFC69A8EFF2B7C504D93590`;
  ZIP SHA-256 is
  `92B71E698F9C4BE9EAF58597463B3A9BC931A84540EF2EE18C411F10CA95771C`.
  Evidence is retained at
  `H:\Ghostline-builds\gps-marker-fix-20260723-002208` and
  `H:\Ghostline-audits\gps-marker-fix-roundtrip-20260723-002032`; the replaced
  install is backed up at
  `H:\Ghostline-backups\pre-gps-marker-fix-20260723-002543`.
- The preceding accessible `drop_point_009` candidate is generated,
  deserialized, byte-identical after CR2W round trips, packed, extracted,
  payload-verified, installed, and wrapped in a verified seven-file ZIP. All
  103 tests pass. All 175 archive entries match `source/archive`, and all seven
  ZIP/installed files match `packed`. Relative to the preceding delivery
  candidate, exactly the delivery phase, journal, and always-loaded marker
  sector changed. Installed archive SHA-256 is
  `1C669335E83C93F714455D24743C7F03E34F2FA381A60ABB9E8F35A85375EDCC`;
  ZIP SHA-256 is
  `D3F32A60C789030FB47BA9C3C06C9E48DBB7097F2F786EB858EF8551D3764275`.
  Evidence is retained at
  `H:\Ghostline-builds\drop-point-009-yellow-20260722-234109` and
  `H:\Ghostline-audits\drop-point-009-roundtrip-20260722-233650`; the replaced
  install is backed up at
  `H:\Ghostline-backups\pre-drop-point-009-20260722-234356`.
- The 2026-07-22 delivery/debrief candidate is generated, deserialized,
  byte-identical after CR2W round trips, packed, extracted, payload-verified,
  installed, and wrapped in a verified seven-file ZIP. All 98 tests pass. The
  175-entry archive matches all packable payloads from the 178-file
  `source/archive` tree; only the known Patch `.tmp` and two head readmes are
  excluded. Relative to the runtime-confirmed hostility build, exactly four
  payloads changed (`gq000.questphase`, `gq000_post_accept.questphase`, the
  journal, and quest onscreen localization) and one payload was added
  (`gq000_delivery.questphase`). All ZIP and installed files match `packed`.
  Installed archive SHA-256 is
  `0F971F97877421C181C5D4B114F5090D015DEE97B3FE7FFCF9091F57FD476158`;
  ZIP SHA-256 is
  `03BF484092377E5B022B9BE4867B1383544B46B24BA4769291904EC93395FBBB`.
  Evidence is retained at
  `H:\Ghostline-builds\delivery-morrow-20260722-224211`; the replaced install
  is backed up at
  `H:\Ghostline-backups\pre-delivery-morrow-20260722-224211`.
- The 2026-07-22 explicit-player hostility candidate is generated,
  deserialized, packed, extracted, payload-verified, installed, and wrapped in
  a verified seven-file ZIP. It preserves the runtime-proven patrol, terminal,
  breach, shard, and cleanup resources byte-for-byte, changing only
  `gq000_post_accept.questphase` from the preceding test build. The new
  43-node/44-edge phase applies the per-entry vanilla `mq022` hostility
  sequence and explicitly targets `#player`. All 88 tests pass, the changed
  CR2W round-trips byte-identically, all 174 archive payloads match
  `source/archive`, and all seven ZIP/installed files match `packed`. Installed
  archive SHA-256 is
  `18D56C1F20C3600AFBA385BE4F6678D58825D0E29E5A350C72FA48FF4227B3E2`;
  ZIP SHA-256 is
  `D5FAC9FE9CE7DA060CDA3CA79114552D89D9D6BF7C2ED7699D999DBD65645674`.
  Evidence is retained at
  `H:\Ghostline-builds\guard-hostility-mq022-20260722-214120`; the replaced
  install is backed up at
  `H:\Ghostline-backups\pre-guard-hostility-mq022-20260722-214120`.
- The preceding hostile-guard/patrol candidate remains at
  `H:\Ghostline-builds\cache-encounter-hostile-patrol-20260722-205717`.
  Runtime confirmed every intended world/presentation change but proved its
  null-target border-patrol threat pulse did not make the guards aggressive.
- The 2026-07-22 cache-encounter candidate has been generated, deserialized,
  structurally round-trip checked, packed, extracted, payload-verified,
  installed, and wrapped in a verified six-file ZIP. Installed archive SHA-256
  is `888E678162D6086124E1CC8AE3CDB39D58697129289A24C5E9DC15B53EEF2D05`;
  ZIP SHA-256 is
  `D4628E6652567DFE46CF9E1D707D002F5B436515F7C4ACE8D544AA3900CF8A69`.
  Build evidence is retained at
  `H:\Ghostline-builds\cache-encounter-candidate-20260722`, and the previous
  installation is backed up at
  `H:\Ghostline-backups\pre-cache-encounter-20260722-191442`.
- The 2026-07-22 custom Patch build has been deserialized, structurally or
  byte-for-byte round-trip checked, packed, extracted, payload-verified,
  installed, and wrapped in a
  verified six-file ZIP. Installed archive SHA-256 is
  `40148CE9F102C5CF77BEA31C1D9043FB20F53B8937873235BDBE3D1A82EF6786`.
- The subsequent cache runtime-fix candidate corrects the guard-community
  streaming origin and relay yaw, adds the minimal device registry and readable
  shard items, and makes `gq000_cache_acquired` precede presentation cleanup.
  The final installed revision also disables Patch's inherited `t0_peen` and
  `t0_pubic_hair` components in both appearance copies; `patch.app` is its only
  archive delta from the otherwise identical cache candidate. All 75 automated
  tests pass. Its 174-entry archive was extracted and matched
  byte-for-byte against the intended `source/archive` payloads; all seven ZIP
  and installed payloads match the staged tree. Installed archive SHA-256 is
  `2C5179349DBD1AFF5A5A01123F83FF1DC76D8D91E45FE946CEA4DCAF0166BF80`,
  and ZIP SHA-256 is
  `73B3C28C525DF298878FA011D5B8D9E79AF03C4FB35CAC740E8064A96CBDAB7C`.
  Evidence is retained at
  `H:\Ghostline-builds\patch-genital-visibility-20260722-202817`, with the
  underlying cache round trips at
  `H:\Ghostline-builds\cache-runtime-fix-20260722-201715`; the replaced
  installation is backed up at
  `H:\Ghostline-backups\pre-patch-genital-visibility-20260722-202817`.
- Test the delivery/debrief candidate from a pre-Ghostline save. After leaving
  the relay area, confirm the Kabuki drop-point objective and marker appear,
  the machine offers the datacache deposit, deposit removes the package and
  advances the quest, Morrow sends both opening messages, either V reply gets
  only its matching response, the final message and completion reward arrive,
  and `GHOSTLINE` moves to Completed.
- The 2026-07-23 GQ002 final-polish candidate is built, payload-verified, and
  installed. It moves the obstructed melee guard onto the open relay floor,
  makes the final relay phase observe the native breach result without sending
  a second `ToggleON` action, adds a visible `Respond to Cinder` objective
  across the debrief exchange, and grants
  `QuestRewards.gq002_completion` before quest completion. All 165 tests pass;
  all 279 extracted archive payloads match `source/archive`; all nine staged,
  ZIP, and installed files match. Installed archive SHA-256 is
  `E37C3498B0AF0EE01697C4542D579252DE844E4D529F6381EDAF0D0CFCA1BF94`;
  ZIP SHA-256 is
  `AD8E9A0735F1F3984ABAAF503596A80756F39535119B74D3412C5E4D55C2939C`.
  Evidence is retained at
  `H:\Ghostline-builds\gq002-final-polish-20260723`; the replaced install is
  backed up at
  `H:\Ghostline-backups\pre-gq002-final-polish-20260723`.
