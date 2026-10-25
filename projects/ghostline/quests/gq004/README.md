# Love, Actually.exe

Ghostline side quest · Velvet Kade · target length 10-15 minutes.

Velvet's stolen Heartbreaker Protocol has become a Tyger Claw product. The
original interrupts abusive behavioural conditioning. The stolen fork disables
its watchdog and traps victims in affective feedback. V must recover the live
signing key, revoke the stolen batch, and distribute Velvet's corrected build.

The final `love-actually-736fbdd18ed4` package is **playtested complete**. On
2026-10-25 the user confirmed a successful playthrough of about ten minutes,
including driving. All sixteen captured placements are applied. The dedicated
`love-actually` profile activates GQ004 independently of the main story profile.
See the [sprint retrospective](RETROSPECTIVE.md) for lessons and follow-ups.

## Quest flow

1. **An unexpected admirer - 2-3 minutes.** Velvet's text leads V to a public
   Kabuki meeting. She flirts to cover her anxiety. Optional questions explain
   the exploit, the need to preserve its signing key, and her branding. Accepting
   advances the quest; walking away must leave the offer available.
2. **Follow the hearts - 3-4 minutes.** A small Claw resale operation has three
   guards and a broker's remote terminal. A visible approach offers combat;
   a side entrance permits stealth. No kill count gates progress. Read the
   sales ledger, original research archive, and deployment instructions.
3. **Heartbreaker Protocol - 3-4 minutes.** Recover the prototype and signing
   key to isolated storage first. Verify the copy, then upload the correction
   through a separate distribution endpoint. Pink pixel hearts and tiny black
   holographic bows accompany a bounded interruption of combat systems. The
   correction restores emotional autonomy; it never makes anyone love V.
   Break contact safely and leave while the gang recovers.
4. **A little vulnerability - 2-3 minutes.** Back at the same safe meeting spot,
   Velvet explains the friend whose partner used a mood regulator to punish
   anger. Her friend left; Velvet supplied a tool, not the decision. V can be
   sincere, tease the hearts-and-ribbons branding, or ask after the friend.
   The reward does not depend on flirting, V's gender, or a romance flag.
5. **Attachments - under a minute.** Velvet sends the closing message and its
   detaching joke after completion. The debrief delivers the same quickhack
   regardless of the optional phone reply.

## Dialogue

The [complete dialogue flow](implementation/DIALOGUE-FLOW.md) includes all
choices, shards, messages, and delivery order. The [readable script](script/dialogue.md)
and three machine manifests share
stable unsigned FNV-1a line IDs. There are 43 spoken lines, with separate
female/male V audio paths, and nine unvoiced scene choices. Phone and terminal
text lives in [quest.json](implementation/quest.json).

The briefing and debrief have native scene specs and generated raw scenes.
Field VO uses eight native scenes within an audio-only call from operation
arrival until departure; the briefing and debrief bring the total to ten.
Scene timings use the longest measured selected take across player genders.
Remeasure them after replacing a take.

## Velvet's appearance

[Velvet's character manifest](../../characters/velvet.character.json) uses the
female-average NPV tooling and an installed-database wardrobe: Bara Kaika
black/red bustier, black Maelstrom syn-leather trousers, a black/purple cropped
Lavender Galaxy bolero, and glossy black biker exo-jacks. The
[wardrobe manifest](../../characters/velvet.wardrobe.json) retains the exact item
records, player-frame meshes, appearances, and companion component metadata.
The [offline review](../../characters/velvet.review.json) records front and
three-quarter silhouette checks, the corrected bustier chunk mask, and the
remaining runtime fit limits. Screenshots are in the character preview's
`review` directory. All 59 character and face-preview tests pass after visibility and
browser layout fixes.

Velvet now uses golden-blonde twin buns with their native rig, animation graph
and NPC shadow, green eyes, rose gloss, no freckles and a separate face
sculpt (eyes 12, nose 6, mouth 6, jaw 7, ears 2). This follows the revised blonde
direction rather than reusing Goth Baddie's hair and head values. Satin bows,
pink flyaways, a pink-lined jacket, exact tattoos, heart charm, and reference-specific
implants are a custom-asset backlog. Head parameters are an initial sculpt
direction, not a claim of a finished likeness. Clothing fit, foot state, and
deformation still need runtime review. The NPV root requires Phantom Liberty.
The revised head shapes have been baked into four meshes using the relocated
game install. The current `head-build-report.json` records the selected shapes,
commands and output hashes. WolvenKit garment-support warnings remain a runtime
validation item. The earlier cache-reuse receipt describes the superseded head.

## Build and playtest

The standalone native playtest package is installed in `K:/Cyberpunk 2077`.
Restart the game, then load a save from before accepting Velvet’s job to exercise the revised meeting lifecycle. Velvet's phone
message starts the quest. Follow [the test route](implementation/PLAYTEST.md).
The main story profile still activates GQ001/GQ002; this separate profile adds
only GQ004. It ships no REDscript, runtime CET or Audioware files. The CET scout
remains an authoring tool and is unnecessary for playing the quest.

All sixteen captures are applied. Fourteen phases, ten scenes, world resources,
cloned controllers, journal/localization and lipmap passed native authored-field
readback: 44 resources. Sixty reviewed WEMs and 86 cooked lipsync variants are
included, with ten approved Velvet take revisions. Archive and ZIP verification
passed; all seven installed files matched their package hashes. See the tracked
[install receipt](implementation/install-receipt.json) for the final package.

Rebuild from the repository root:

```powershell
.venv/Scripts/python.exe projects/ghostline/quests/gq004/implementation/prepare_runtime.py
.venv/Scripts/python.exe projects/ghostline/quests/gq004/implementation/compile_native.py
.venv/Scripts/python.exe tools/package_project.py --project ghostline --profile love-actually --install --game 'K:/Cyberpunk 2077'
```

Recovery grants the sales ledger first; later shards follow each preceding read
and conversation. Read objectives wait on the onscreen entry becoming visited.
Reading cannot commit either personal-link transfer. Both sockets use
the stock personal-link controller with minigame skipping, so a cyberdeck is not
required. Each five-second transfer runs in a child phase with terminating
success/retry exits. A disconnect cancels the pending timer. Recovery retains
the verified local copy; upload commits only after its separate transfer.

The corrected upload applies the native six-second blindness/hearts/bows effects
to the three named quest guards without a kill requirement. Guard cleanup waits
until V leaves the outer area. Deferring the briefing retains the meeting.
The debrief grants the Tier 5/Iconic Heartbreaker Protocol item, verifies it in
inventory, and completes the journal. The quickhack menu displays Velvet Crash.
Closing messages follow independently after 45 seconds. Velvet remains until
the player leaves her meeting area; returning after deferral skips the intro.

## Runtime evidence and remaining scope

The final playthrough confirms the user's complete route, with earlier reports
confirming body rendering, progression, reward, and visible quickhack FX. Final
feedback accepted the audio call, return behavior, socket and icon polish.
Exhaustive coverage of both V voices, all save/load states, stealth/combat
branches, and clothing deformation remains separate from that confirmation.
Reference-specific hair bows, charms and tattoos remain a cosmetic backlog.
The quickhack's native heart/bow effects are included. Temporary link diagnostics
are disabled in the optional scout; captures and logs remain available.

See [the runtime contract](implementation/runtime.json) and
[voice production notes](voice/README.md) for build evidence.
