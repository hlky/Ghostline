# Runtime NPC experiment

This is the first feasibility milestone: one isolated Patch clone, three native
dialogue choices, and two existing reviewed voice lines played from a reusable
loose Audioware WAV slot. Facial curves and subtitles are supplied at runtime.
It also includes one fixed data-theft runtime executor. There is no LLM or
runtime TTS; the job records save-specific outcomes for later NPC memory.

The experiment has unique entity, appearance and graph depot paths under
`mod/npc_runtime`. It uses Patch's supporting assets through an explicit shared
runtime dependency. It activates no quest and does not change the story Patch's
face graph. The harness creates a nonpersistent NPC only when its spawn hotkey
is pressed.

## Build and package

From the repository root:

```powershell
py -B projects/experiments/npc-runtime/implementation/build.py
py -B tools/package_project.py --project npc-runtime --plan
py -B tools/package_project.py --project npc-runtime
```

The build extracts the installed base facial graph and rig into this project's
ignored `generated/references`, clones the packed Patch baseline, exports the
utterances through the existing lipsync synthesis operation, and verifies that
all runtime graph inputs survive CR2W serialization. WolvenKit writes the new
graph layout; the native template writer handles the cloned entity/appearance.
`--game`, `--wolvenkit` and `--references` override build inputs.

`implementation/utterances.json` pins the reviewed WAVs and the cached authoring
alignments. Those historical reports had no WAV digest: the initial selection
was checked by filename and duration, and each new utterance pins the current
WAV digest. The learned template model remains reproducible ignored output at
`generated/lipsync-corpus/templates/lipsync-templates.json`.

The package verification receipt is under `generated/packages`. It proves
archive extraction and ZIP hashes, not successful game loading. The packager's
explicit `include_loose` list includes only this experiment's scripts and audio;
it does not sweep in the shared runtime's quest scripts or tweaks.

## Runtime prerequisites

Use the current compatible RED4ext, CET, redscript, Codeware and TweakXL stack,
plus [Audioware](https://github.com/cyb3rpsych0s1s/audioware). The prototype uses
dynamic emitter events (introduced in Audioware 1.7.6); the isolated compiler
check used Audioware 1.9.9 sources at commit
`795ce036149e9726d84b6a5c450de68e667c254c` and the locally installed Codeware scripts.
Install Audioware before the prototype's REDscript: its native types must exist
for compilation. Neither the build nor normal package command installs anything.

Once dependencies are installed, the explicit install command is:

```powershell
py -B tools/package_project.py --project npc-runtime --install --game 'H:/Cyberpunk 2077'
```

Restart the game after the one-time installation. Further utterance playback
replaces loose WAV data and does not rebuild an archive.

## First in-game check

1. Load a disposable test save in a quiet, open location. Bind the `NPC Runtime`
   hotkeys in CET, then close the overlay.
2. Spawn the experiment Patch. Run the jaw probe. It requests jaw opening for
   1.5 seconds and releases the gate. **Visible motion and restoration are the
   first unproven engine gate.** Stop here if the face does not respond.
3. Start the slot publisher in a terminal:

   ```powershell
   py -B tools/npc_runtime_slot_worker.py --game 'H:/Cyberpunk 2077'
   ```

4. Open the conversation. Select either spoken response. The worker validates
   the selected WAV digest, replaces the idle slot using `os.replace`, and sends
   a token-matched acknowledgement. Only then does the harness enqueue audio.
5. Listen to both lines and check facial motion and subtitles. Repeat a line;
   confirm the slot changes without repacking or restarting.
6. Interrupt during speech, pause/resume, remove the NPC, load another save and
   enter authored quest dialogue. Confirm subtitles disappear, facial overrides
   release, old worker responses are ignored, and native dialogue regains control.

CET confines file writes to each Lua mod directory, so the harness sends small
request/acknowledgement files there. The external worker publishes audio into
`r6/audioware`; it is intentionally limited to these two fixed line IDs. Opening
the CET overlay cancels the experiment conversation. The NPC is not saved.

The controller polls playback position at most four times per second and
interpolates facial samples between corrections. The first subtitle appears
when playback is confirmed. Start latency, alignment drift and 154-input update
cost still need measurement on the live game. This is not a production timing
implementation.

## Verification and evidence

```powershell
py -B -m unittest discover -s tests -p 'test_runtime_utterance.py'
py -B -m unittest discover -s tests -p 'test_lipsync_command_parity.py'
lua tests/npc_runtime_harness.lua
```

Record the exact package receipt and dependency versions alongside the manual
results in `implementation/runtime-observations.json`. Keep every visual/audio
result marked untested until observed in-game. Offline Lua mocks verify transport
and cleanup decisions; they cannot establish native UI or facial behaviour.

Relevant source precedents: [native dialogue hubs](https://www.nexusmods.com/cyberpunk2077/articles/413),
[Audioware subtitle events](https://github.com/cyb3rpsych0s1s/audioware/blob/795ce036149e9726d84b6a5c450de68e667c254c/crates/audioware/reds/Codeware.reds),
and [dynamic emitter controls](https://cyb3rpsych0s1s.github.io/audioware/DYNAMIC_EMITTERS.html).

## Fixed data-theft job

Bind these additional CET hotkeys:

- **NPC Runtime: offer fixed data-theft job** creates an offer from anywhere.
- **NPC Runtime: open data-theft job choices** shows accept/decline or delivery
  choices, depending on the current state. Close the CET overlay first.
- **NPC Runtime: abandon data-theft job** clears an active job without paying.

Accept **Borrowed Credentials**, follow its temporary map marker to the back-alley
access point in Watson/Little China, and select the extra **Download credentials**
device option. The native personal-link animation connects V; the native HUD
progress bar runs for five unpaused seconds. Disconnecting or leaving range
interrupts the download and allows retry. No breach puzzle is required.
After completion, open the job choices and either deliver the credentials or
deliver them while retaining a copy. Both pay 500 eddies and record distinct
outcome facts and counters. Credentials are represented by job state rather
than an inventory item. Repeat offers are allowed for this test harness.

The target comes directly from `reference/world/antenna-access-points.json`:
`{ma_wat_ich_01_dvc_access_point_backalley}`, position approximately
`(-1527.83, 1809.91, 31.55)`. The executor resolves its absolute catalogue NodeRef;
looking at a device is never used to select or complete the job. An unloaded
target is validated when streamed in. Powered-off, disabled, or quest-controlled
personal links are rejected. A prior breach alone does not disqualify it, and
the tagged transfer bypasses netrunner rewards and normal breach completion.
This candidate's accessibility and prompt visibility still require a live check.

`implementation/jobs/data-theft.quest.json` reuses the existing block schema and
validator: `reach_area -> interact_device -> choice_gate`.
`data-theft.runtime.json` binds those blocks to the extracted target and runtime
settings. `tools/runtime_job_plan.py` rejects unsupported block fields/actions,
ambiguous targets and facts outside this job's namespace, then exports a pinned
plan and matching REDscript config. This narrow adapter implements these three
block semantics in a persistent ScriptableSystem. The manifest's phase, trigger
and journal paths describe contracts; **no job questphase or journal resources
are emitted or activated**. Presentation uses temporary mappins, notifications
and native choices. The executor is not yet a general runtime for every block.

Only `ScriptableDeviceComponentPS` actions for this run's exact target receive
the additional tagged option. Vanilla actions remain available. The normal
personal-link state machine handles connection/animation; the tagged connection
is intercepted before its minigame/reward route. Transfer state requires the
matching run, exact device, range, power and a connected link. Progress UI yields
when another system owns it. Pause/overlay freezes the timer; delivery UI needs
reopening afterward. Save/load recreates the mappin and discards UI callbacks;
an interrupted transfer restarts from zero. The native personal-link save lock
may prevent saving while connected. Completed outcomes/counters remain in the
save. Revision changes invalidate active jobs instead of retargeting them.

The payout guard prevents repeated choices in one loaded run. Persistence and
payment consistency across saves remain live test gates; isolated compilation
and Lua mocks cannot prove them.

Regenerate just the loose job contract, without rebuilding facial archives:

```powershell
py -B projects/experiments/npc-runtime/implementation/build.py --job-only
py -B tools/check_redscript.py --game 'H:/Cyberpunk 2077' --sources projects/experiments/npc-runtime/source/resources/r6/scripts --output projects/experiments/npc-runtime/generated/job-script-check --replace-folder GhostlineNPCRuntime
py -B -m unittest discover -s tests -p 'test_runtime_job_plan.py'
lua tests/npc_runtime_job_harness.lua
```

The compiler uses an isolated cache and disables its error popup; it never
changes the installed game's cache. Script changes require a game restart.

Live checks: verify the selected marker and prompt; disconnect mid-download;
pause/resume; try a different device; complete each delivery outcome; reopen
choices repeatedly; save/load while travelling and before/after payment; load
an earlier save and confirm its own outcomes. Record observations in
`implementation/runtime-observations.json` before marking runtime support proven.

The timed-transfer precedent is GQT002's `generate_guarded_plant` (connection,
five-second `questProgressBar_NodeType`, then disconnect), also seen in extracted
vanilla quest phases such as `sts_wat_lch_01_openworld`.
Native API details were checked against the installed compiler cache and
[personal-link implementation](https://codeberg.org/adamsmasher/cyberpunk/src/commit/a2e6bb31298fc7c613e5bfa3d22d424cdeca3f9a/cyberpunk/devices/core/scriptableDeviceBasePS.swift),
[choice action implementation](https://codeberg.org/adamsmasher/cyberpunk/src/commit/a2e6bb31298fc7c613e5bfa3d22d424cdeca3f9a/cyberpunk/devices/core/baseDeviceActions.swift),
and [native progress UI](https://codeberg.org/adamsmasher/cyberpunk/src/commit/a2e6bb31298fc7c613e5bfa3d22d424cdeca3f9a/cyberpunk/UI/widgets/hud_progress_bar/HUD_progress_bar.swift).
