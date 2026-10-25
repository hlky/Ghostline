# First playtest repairs — 25 October 2026

Installed candidate: `love-actually-a1053fd8721b`.

User screenshots established black torso skin, Velvet disappearing immediately
after accepting, incorrectly mounted access points, and an inert recovery prompt.
The user also reported the intro playing before turning the corner.

- Skin: the embedded body materials referenced three tutorial textures omitted
  from the isolated package. Goth Baddie's corrected body used character-owned
  texture paths. Velvet now has the equivalent three textures in her own depot
  namespace and editable decoded material references. Package extraction verifies
  all three. `compile_body.py` checks decoded material and mesh parity, excluding
  only derived material byte offsets and sizes changed by shorter depot paths.
- Meeting: removed community deactivation from the acceptance exit. Release now
  occurs when V reaches the distant operation. Awareness radius is 3 m instead
  of 10 m; conversation radius is 2.5 m instead of 6 m.
- Mounts: map captured player local +Y to socket local +X with yaw +90 degrees.
  Apply a 0.4 m setback toward the wall from the captured standing position.
  Importing the original captures again does not accumulate this offset. Exact
  collision and mounting still require visual confirmation.
- Device progression: correct ArchiveXL registry patch target to the compiled
  Night City device registry. Address actions and condition queries to the actual
  AccessPointControllerPS. Replace invalid ForceEnable/ForceDisable names with
  stock ForceON/ForceDisabled. Arrival VO no longer gates device arming.

Validation: 18 quest/import tests, 37 scene tests and 25 package tests passed.
All 37 native quest resources passed authored-field readback. The repaired body
passed decoded readback separately. Archive extraction, ZIP verification and all
six installed file hashes passed. Other Ghostline prototypes remain disabled.

Restart the game and use a save from before accepting Velvet's job to exercise
the revised meeting flow. No save facts have been reset. Check both socket
interactions, personal-link animation, transfer completion/interruption, and
the wall fit. These repairs are not yet verified in game.

## Link-only action repair

Installed candidate: `love-actually-18e9616aea7c`. The player confirmed the
body, intro distance and meeting retention fixes, but recovery remained inert.
The read-only trace showed the custom recovery caption selecting ActionHacking,
not TogglePersonalLink. The device was ON, had its personal-link slot and was
not disrupted. Four clicks never reached a link handler.

The cloned devices now disable HackingSkillCheck (difficulty NONE, inactive).
They retain minigame skipping, forced personal link and the five-second quest
transfer. Fresh `_link` NodeRefs avoid persisted active hacking slots; the scout
keeps its original capture IDs through capture_ref. Coordinates are unchanged.

All 37 native resources passed readback, including the disabled checks in both
cooked devices. Nineteen quest/import regression tests and 25 package tests
passed. Archive extraction, ZIP verification and all six installed hashes passed.
This action repair still needs an in-game retry.

## Fast travel and Velvet protection

The player reported that fast travel into Kabuki Market left the introduction
unstarted and that Velvet could be attacked. Meeting setup and operation arrival
now use IsInside instead of the edge-only Entered condition. Scene mood, awareness
and engagement already use IsInside. The 3 m greeting range is unchanged.
After a defer/end exit, the meeting waits until V leaves greeting range before
rearming, avoiding an immediate repeated greeting while still accepting fast travel.

Velvet now has the native friendly attitude group, which the player weapon
safety check recognizes, plus an Invulnerable tag for damage protection. Both
meeting phases set friendly attitude and Invulnerable mortality after spawn
readiness and before starting the scene. Her manifest owns the protection policy
and prepare_runtime.py regenerates the TweakXL fields. In-game checks pending.

Installed fast-travel/protection candidate: `love-actually-81aeb68b8a08`.
Twenty quest/import tests, 25 package tests, all 37 native resource readbacks,
archive/ZIP extraction and all six installed hashes passed. The final two
meeting phases have a separate scoped rearm readback receipt under generated
gq004-meeting-rearm/validation.json. Runtime validation remains pending.

## Reward, read order and transfer presentation

Installed candidate: `love-actually-48d34bfbd798`. TweakXL logged a failed clone
of Items.GhostlineVelvetCrashProtocol before it existed. Heartbreaker now clones
vanilla BlindProgram directly and explicitly selects the custom action. Normal
delivery waits for inventory confirmation. A separately registered native repair
root grants a missing reward on completed saves once and verifies ownership.

Shard-read visited gates use the Bloody Ritual scene precedent, with explicit
read objectives and separately timed evidence/archive comments. Approved voice
and lipsync stay unchanged. Closing text waits for departure plus 20 seconds.
Upload uses Velvet Crash; successful bars finish their native outro rather than
being forcibly hidden at the timer boundary. Genuine interruptions still cancel.

All 40 native resources passed authored-field readback. All 49 scoped tests
passed. Archive extraction, ZIP and six installed file hashes verified. These
new behaviours still require in-game validation.

## Follow-up: localization, completion and Iconic reward

Installed `love-actually-785a0425e32f`. The user confirmed readable-gate progression
and reward delivery, but reported unresolved read-objective LocKeys, a second
failed outro after upload completed, no visible quickhack cosmetics, and no
closing text or journal completion.

The build had copied stale source localization over the newly generated
onscreens. Staging now preserves compiler-owned gq004 onscreens; all three
read-objective keys survive publication. A regression test covers the overwrite.

Quest completion now belongs to a new native finish root: wait for debrief,
query current inventory after the transaction settles, verify reward, succeed
the journal and set completed. Optional texts follow after 45 seconds, guarded
against repeat dispatch. This root can recover the already-finished debrief
save without relying on the previously blocked parent/streamed trigger.

The parent now waits two ticks AFTER attempt exit before forcing disconnect;
the previous delay inside the attempt could not protect against its remaining
retry listener. HUD outro diagnostics are read-only. Native cosmetics now bind
to the observed custom ShortBlind payload; Vision has no duplicate VFX binding.
This is a candidate correction, not confirmed visual rendering. The logger
records actual target FX-component presence and status dispatch on the next test.

Heartbreaker has Quality.Legendary and an IsItemIconic stat modifier, retaining
the menu name Velvet Crash and six-second effect. It has its own description.
Fresh and existing-instance rarity display still need checking in game.

All 58 scoped tests, 42 native resource readbacks, package extraction/ZIP and
six installed file hashes passed. The three ArchiveXL roots are main, reward
repair and finish/epilogue. No custom REDscript or runtime CET dependency added.

## Leave-operation follow-up

Installed `love-actually-38cf2d7b60c9`. The leave resource had identical SHA-256
(1ff1b6a7e9acf5241ddb8b40750865cdde8c9559391bd05db089848fb72559e5) in
48d34bfbd798 and 785a0425e32f. The upload parent changed in the latter. This
comparison does not prove which timing change triggered the reported stall.
The existing leave gate waited for Exited after upload dialogue, and could
miss an earlier departure. The quest-owned override now uses IsOutside,
preserving node IDs, 50 m boundary, objective/fact/cleanup order and all
shared compiler behavior.

One changed native phase passed authored-field readback; 26 quest tests passed.
The regression covers IsOutside and cleanup ordering. Package extraction, ZIP
and six installed file hashes verified. Scope receipt: generated/gq004-leave-repair/latest.json.
In-game confirmation pending.

## Confirmed missing FX spawners on EP1 replacements

Installed `love-actually-e998fcee1d9b`. The user confirmed the leave repair and reported that
quickhack visuals still did not work. Read-only heartbreaker_vfx events show
accepted custom status dispatch, one configured VFX entry, and has_spawner=false
on all three quest guards, kab_ncpd_constable_melee1_baton_ma and
nid_maelstrom_grunt1_ranged1_copperhead_ma. Local REDmod faction records map
these to ep1 replacement entities; the 128-target patch list contained base
entities only.

Decoded 116 EP1 citizen/corpo/gang/service templates from installed gamedata.
All passed NPCPuppet + Head attachment-slot checks. Added them to the owning
prototype target list and ArchiveXL patch registration; generator consumes the
updated list. Detailed entry SHA-1s and decoded SHA-256s are recorded in
projects/experiments/velvet-crash/implementation/npc-target-audit.json.

Eight FX regressions passed, including actual Tyger/NCPD/Maelstrom replacement
coverage. Package extraction, ZIP and six installed hashes verified. All archive
payload hashes match the preceding build: this repair changes registration
only. Rendering after restart still requires in-game confirmation.

## Final presentation pass

Installed `love-actually-d235fbaccf07`. User confirmed the quickhack FX now works.
Recovery/upload now have separate markers copied from mounted socket
coordinates. The scout ignores derived markers, retaining all 16 original
captures; reimport synchronizes the derived markers after wall offsets.

Only Sales is granted at recovery. Archive is activated/granted after the sales
comment scene ends; Revocation follows the archive comment. Visited gates and
read objectives remain. Already-owned items are not removed from old saves.

The root no longer terminates immediately after return dialogue. It waits
until V leaves the 60 m meeting area, then deactivates Velvet. Cleanup cannot
block independent quest completion. The finish root replaces its one-second
settle with two game ticks, retaining actual inventory verification.

All 62 scoped tests, 42 native readbacks, package extraction/ZIP and six
installed hashes passed. Working FX and voice payload hashes are unchanged.
New presentation changes still need an in-game check from before recovery.

## Custom Heartbreaker icon

Installed `love-actually-8641888e96f2`. build_icon.py authors a monochrome
broken-heart/circuit/bow glyph and native three-resolution atlas, cooks the
RGBA texture, reads both back, compares authored atlas fields and verifies
texture alpha byte-for-byte under normal engine UV orientation. Item icon and
iconPath both reference the custom UIIcon. The scanner follows the existing
shared interaction captionIcon through a custom ChoiceCaptionIconPart. A z_
TweakXL patch applies after the prototype creates that interaction.

29 quest regressions passed. New atlas/texture readback, package extraction/ZIP
and seven installed hashes verified. Every preceding archive payload hash is
unchanged; only two new icon resources and icon bindings were added. Native
icon display still needs an in-game check.

## Heartbreaker tooltip description

Installed `love-actually-67f29359f709`. The inherited EquipmentGLP.BlindProgram
OnAttach entry supplied the Reboot Optics inventory bullet, independently of
Item.localizedDescription. Local native FillSpecialAbilities confirms this
lookup. Only that ability is replaced with a clone using quest-owned UIData;
OnEquip stats, actions and FX are retained. UIData uses LocKey expressions as
documented for native GameplayLogicPackageUIData string localization. Scanner
interaction description points to the same new effect entry.

29 quest regressions passed. Scoped onscreen CR2W readback, package extraction,
ZIP and all seven installed hashes passed. All previous payload hashes except
the edited onscreen localization remain unchanged. In-game tooltip verification
is pending.

## Dialogue pass 02 and deferred conversation

Installed `love-actually-5a4101e63d45`. The user explicitly listening-approved
ten new full-reference Velvet takes. Source WAVs, subtitles and twenty revised
facial variants match those selections; the combined set retains 86 quest
clips. Cooked re-export verified all facial key values (maximum error below
0.000000103) and clip durations (maximum error below 0.001 ms); key-time
quantization is bounded by the native uint16 normalized-time step.

Deferred conversation now immediately checks departure from the 2.5 m engage
radius, removing the old delayed subscription that missed quick returns.
Remote scenes spawn Velvet at vanilla's hidden studio marker, with studio
prefab streaming held by their parent phase and spawn-position validation
disabled. The old Kabuki marker depended on navigation 1.3 km away. The final
voice tag was already correct. Remote playback still needs an in-game check.

The briefing describes three Claws and two access points and explains the key
without requiring optional questions. Upload instructions finish before its
socket is enabled. The naming exchange belongs to the connected transfer
attempt and is cancelled on an interrupted link. Recovery post-transfer and
retry VO wait for arrival explanation; upload success waits for its naming
exchange. Retry and success wording now distinguish recovery/upload and
victims/guards. The approved replacement closing take removes the long pause.

30 quest, 26 package and 8 FX tests passed. All 44 native resources passed
WolvenKit authored-field readback. Archive extraction, ZIP verification and
all seven installed file hashes passed. Existing captured coordinates and
working native quickhack FX are retained. No runtime script was added.

## Upload opening line, exact socket mounts and native icon sizes

Installed `love-actually-01f50d352c01`. The user confirmed the missing speech is only
Velvet's opening success line: V's reply and Velvet's exit line already play.
That opening event was at time zero on a newly spawned remote performer. The
success scene now waits on its actual dynamic actor's spawned condition before
entering the dialogue section, using executable In rather than CutDestination.
No additional fixed-seconds delay or re-recording was added. Runtime confirmation
of that first-line repair remains required.

Socket surfaces were calculated from the screenshot-identified vanilla wall
collision actors: node 2409/actor 28 in exterior_-5_6_0_1, and node 2634/actor 45
in exterior_-10_12_0_0. The socket rear collider face sits 2 mm outside the wall;
root X offset accounts for its -0.01 m rear collider coordinate. Both yaw values
match the wall normals. `world/socket-mount-evidence.json` records decoded actor
and shape transforms plus collision hashes. Markers follow the mounted sockets.
Original capture reimports remain idempotent; different captures invalidate the
location-specific wall anchors rather than projecting onto an obsolete wall.

The original custom 256-pixel full-texture part was reused in every context.
Vanilla's 1080p scanner icon is 32x32. The atlas now has separate 100x128 coloured
inventory-chip and 32x32 monochrome HUD parts, with a 2x high-resolution texture.
Inventory uses standard ItemIcon metadata and custom iconPath; scanner and
active-target caption bindings use the small glyph. Both cooked texture mip-0
RGBA buffers exactly match their authored PNG pixels after the normal row flip.

32 quest, 26 packaging and 8 FX tests passed; all 44 native authored-field
readbacks passed. Archive extraction, ZIP and all seven installed hashes passed.
All 60 WEM payloads and native Velvet Crash effect resources match the preceding
package byte for byte. Other Ghostline packages remain disabled.

## Native audio-call HUD, deferred intro and inventory footprint

Installed `love-actually-736fbdd18ed4`. The user confirmed the success opening now plays and
that the first mount and both scanner/active-target glyphs are good.

The root now directly starts a native Audio-mode questCallContact after reach
and before recovery, and ends it after leave and before the in-person debrief.
Caller/addressee are contacts/velvet and contacts/player. There is no video,
avatar or answer prompt. Installed vanilla PhoneSystem.OnTriggerCall accepts
StartCall directly, and newHudPhoneGameController.UpdateHoloAudioCall switches
to EHudPhoneFunction.Audiocall for this mode. Existing scene-owned remote
performers and the successful readiness gate are retained. No new scripts.

Deferring sets gq004_meet_deferred. The next meeting dispatch enters resume on
the same scene, acquires the community actor and waits for engage/not-in-combat,
then shows choices directly without replaying the greeting or job setup. Both
original and resumed scenes retain acceptance and repeat-deferral exits.

The remaining chip overflow was caused by treating the high-resolution
inventory footprint as the 1080p footprint. The actual item_icons21_1080p
texture is 1012x1020; its vanilla quickhack region is approximately 50x65.
The custom inventory part now matches 50x65 rather than 100x128. The working
32x32 HUD glyph region was compared pixel-for-pixel with the preceding package
and is unchanged. The confirmed first mount is retained. The second mount has
a 3 cm visual inset beyond its collision-based placement, based on the supplied
side-view playtest feedback; its marker follows that corrected position.

34 quest, 26 package and 8 FX tests passed. All 44 native resources passed
WolvenKit authored-field readback; extraction, ZIP and all seven installed
hashes passed. All 60 voice WEMs and native FX resources match the previous
package. Runtime checks remain for audio-call UI/hangup, intro resume, the
second visual mount and the resized received/inventory/equipped chip. Use a
pre-meeting save to test the whole change, or pre-arrival for the call alone.
