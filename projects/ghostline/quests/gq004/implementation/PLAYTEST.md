# Love, Actually.exe: installed native playtest

Build: `love-actually-67f29359f709`, installed in `K:/Cyberpunk 2077`.
The archive, extracted payloads, ZIP and six installed files are hash-verified.
Goth Baddie, Heartbreaker, Velvet Crash and NPC Runtime are disabled with
hash-verified backups. Love, Actually is the only active Ghostline package.
See `goth-baddie-disabled.json` and `isolation-receipt.json` for restoration paths.
`install-receipt.json` identifies this build. The first build produced the issues recorded in `PLAYTEST-REPAIRS.md`; this repaired build has not yet been tested in game.

Skin rendering, intro distance and Velvet retention were confirmed. The trace
confirms recovery and upload commits. This candidate fixes reward definition and
delivery, adds shard-read progression, separates the two progress labels and
completes the quest independently of the optional closing text. Captured positions are unchanged.

Restart Cyberpunk so it discovers the updated archive. For this test, load a save
from before approaching the operation so its device conditions initialize again.
A save before accepting the job is also suitable. No location recapture is needed.
Required foundations are ArchiveXL, TweakXL and Phantom Liberty for Velvet's NPV
entity. The quest has no REDscript, runtime CET, Audioware or worker dependency.

Before the route below, test direct fast travel to Kabuki Market while the
meeting objective is active. Approach within 3 m; dialogue must start even if V
arrived inside the setup area. Aim at Velvet: native friendly weapon safety
should apply. Check incidental damage protection on a disposable save. Defer,
remain beside her, then step away and return: no immediate greeting loop.
Repeat the direct-arrival check for the debrief.

1. Receive Velvet's message and reply **Send the location.** Confirm the meeting
   objective and one map destination. Check the phone contact name.
2. Visit the captured meeting spot. Confirm blonde hair, no freckles, clothing,
   standing height and facing. Check that exposed torso skin renders normally. The greeting should start within 3 m; inspect lip motion.
3. Choose the defer response. Step away and return; the job must remain
   available. Accept, then confirm that the relay objective replaces the meeting
   objective and that no old route remains. Velvet should remain visible as you leave.
4. Approach the operation. Confirm three guards, both sockets, facing and
   collision. Try stealth first: no kill count or forced combat target should
   prevent recovery. Also test the combat route on a separate save.
5. Use **Recover Heartbreaker + archived messages** on the recovery socket.
   Check the native personal-link animation and five-second progress bar.
   Disconnect or leave during transfer, then retry. No recovery flag or upload
   objective should appear until a full transfer succeeds.
6. After recovery, V confirms the copy. Follow the three read objectives in
   Shards: wholesale terms, conditioning-interrupt research, then deployment
   instructions. Comments must follow reading the relevant file. Upload must
   remain unavailable until all three are read. Test both pickup preview and
   opening the full Shards menu; also test reading the files out of order.
   Velvet must not appear beside V during the remote exchanges.
7. Use **Upload Velvet Crash** on the separate distribution socket. Interrupt
   and retry again. The verified local copy must remain available. Successful
   upload should produce hearts, black bows and roughly six seconds of optical
   interruption on the quest guards. Dead or absent guards must not stall it.
8. Leave the outer operation boundary. Confirm the guards are released only
   after leaving, and the objective points back to Velvet. Return, play each
   debrief tone on separate saves, and check her face and both V voices.
9. Confirm one **Heartbreaker Protocol** item after the debrief. Its quickhack
   action should display **Velvet Crash**. Check Tier 5 and Iconic presentation.
   The journal must finish after reward verification, with no phone reply
   required. The closing text should arrive about 45 seconds later; either
   reply remains available after quest completion.
10. Save/load after acceptance, recovery, interrupted upload, committed upload,
    debrief and completion. A partial transfer must restart; a committed one
    must stay committed. Completed quests must not re-offer or award another
    quickhack. Check the installed ArchiveXL/TweakXL logs for new errors.

Record observations against this build ID. Conversion verifies resource values;
the checks above establish actual engine behaviour, placement and appearance.

Current repair checks: upload must display **Velvet Crash** and finish with a
successful outro. The native unplug animation may still take time. Load an
already completed save that missed the reward: one Heartbreaker Protocol should
be delivered automatically. Save/reload again and confirm no duplicate. For
shard/dialogue sequencing, use a save before the recovery transfer. No recapture
is needed. Detailed flow and remaining spoken wording: `DIALOGUE-REVIEW.md`.

Current candidate: all three read-objective strings are present in the packed
localization input. Check for readable text instead of LocKey hashes. Upload
listener retirement now happens in the parent before unplug. Check that no
failed outro follows completion. Test the Heartbreaker reward on a live human
NPC for pink hearts/black bows. The read-only helper logs status dispatch and
whether that target has the native FX component, plus completion facts globally.
Existing saved item quality may need checking separately from a fresh reward.

Departure repair: walk beyond the existing 50 m operation boundary while the
upload exchange is still playing. When the leave phase starts, it must accept
the already-outside state and advance to Return to Velvet. Repeat with a save
made outside while the leave objective is active. No coordinates changed.

FX coverage repair: fully restart, then use Velvet Crash on a live Tyger Claw,
NCPD officer or Maelstrom ganger. Traces confirmed status dispatch but no FX
component on their EP1 templates. These now receive the same native component
as legacy NPCs. Expect six seconds of hearts/bows with existing blindness.
No quest replay or location capture is needed to test the awarded quickhack.

Polish pass: restart and use a save before recovery. Approach marker remains
central; recovery and upload markers must sit at their own wall sockets.
Receive Sales first, then Archive only after the sales read/dialogue, then
Revocation only after archive read/dialogue. Existing saves retain old items.
After debrief, stand beside Velvet: she must remain. Reward/completion should
feel like one ending beat, with only two settling ticks instead of one second.
Community cleanup follows departure beyond the 60 m meeting area.

Custom icon: fully restart, inspect the existing Heartbreaker inventory tile
and Velvet Crash scanner row. Both should show the broken heart and bow glyph
with native UI tint, replacing Reboot Optics. No new item or quest replay needed.

Description repair: restart and hover Heartbreaker. Its bullet should describe
six seconds of optics disruption, pink hearts, tiny bows and glitch confetti.
The scanner uses the same effect text. Existing items require no replacement.

Dialogue pass 02: fully restart and load before meeting Velvet. Choose “I'll
come back”, step just outside 2.5 m and return promptly; repeat after stepping
away during the first two seconds. Choices must reappear. Hear her field
arrival, patch instruction, success and exit lines. These now use the native
hidden studio marker rather than the unstreamed Kabuki actor position.

Upload naming must start when the personal link connects, not when the upload
objective appears. Interrupt the connection during the exchange: it must stop,
then the retry remark must play alone. Reconnect and complete it; success must
follow the naming exchange. Also interrupt recovery while its arrival briefing
is still playing; the retry remark must wait until that briefing ends. Repeat
a second interruption to verify rearming. Kill all guards in a separate run:
the links and scene progression must still work without living FX targets.

The briefing must describe three Claws and two access points. The completion
exchange must distinguish the victims' conditioning from the guards' optics.
The final “Don't sound so brave. They suit you” should use the approved shorter
take without the old long pause. Existing captured locations remain valid.

Success opening/socket/icon repair: restart, load before the second upload,
and listen specifically for “Fix accepted. Stolen copies shut down...” before
V's “Their optics didn't.” The success scene now waits for its newly spawned
remote actor before its time-zero event. Velvet's later exit instruction is
unchanged. Other remote scenes retain their working flow.

Inspect both wall sockets from the side: the rear collider plane should meet
the inspected vanilla wall with 2 mm clearance. Both socket rotations match
the wall normals, and quest markers follow. Coordinates were calculated from
collision actors 28 and 45 in the screenshot-identified sectors. Reimporting
the original captures retains the correction; new captures invalidate these
specific wall anchors and require a new mounting inspection.

Inspect the received-item popup and inventory: a compact cyan chip replaces
the oversized white glyph. Scanner and active-target indicators use a separate
32x32 native glyph at 1080p (64x64 in the higher-resolution atlas slot), so the
quickhack row must retain its usual height. Existing items need no replacement.

Audio-call/resume polish: restart and load before entering the operation to
exercise the new root StartCall node. Expect the standard native audio-call
HUD, without video or an answer prompt, throughout recovery, shard comments
and upload. Leave after the upload: it must hang up before Return to Velvet.
A save already inside an active transfer may have passed this new root hook;
use a pre-arrival save for the call test.

Use a pre-meeting save for the deferred intro: choose “I'll come back”, step
outside 2.5 m and return. Her greeting and job setup must not replay. Choices
must appear when in range and out of combat; accepting from those choices must
finish the meeting as usual. Repeat deferral once more to test the resume loop.

Inventory chip sizing: the actual vanilla 1080p inventory sprite is about
50x65 pixels, measured from item_icons21_1080p.xbm (1012x1020), not 100x128.
The custom inventory part now uses that 50x65 footprint; the working scanner
part remains 32x32. Check the received-item popup, inventory and equipped list.
The first socket is retained at its confirmed-good mount. The second is moved
3 cm into the visual wall relative to its collision-plane mount; inspect its
back edge from the same side view used in the supplied screenshot.

Final feedback (2026-10-25): user reported all good on package
`love-actually-736fbdd18ed4`, with a complete driving-inclusive playthrough
of approximately 10 minutes. Link diagnostics are disabled in the optional
scout entrypoint; location capture UI and prior logs remain available.
