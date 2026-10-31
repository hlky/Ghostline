# Ghostline's current cinematic coverage

The catalogue-resolved project source trees contain **20 authored raw scene
resources**. This inventory excludes generated previews, templates and vanilla
references. It inspects section events, not every cinematic action a phase,
world resource, workspot or script could perform.

Exact paths, event counts and raw hashes are retained in
[the project inventory](../../../../../reference/quests/deep-dives/cinematic-scenes/ghostline-scene-inventory.json).
Ownership comes from [projects/catalog.json](../../../../../projects/catalog.json);
the repository root is not treated as a WolvenKit project.

| Owning project | Raw scenes | Section events | Presentation represented |
| --- | ---: | ---: | --- |
| ghostline | 14 | 103 | Dialogue events only |
| ghostline-runtime | 1 | 19 | 13 dialogue and six gaze events |
| gqt005 | 2 | 21 | Dialogue/gaze launch plus braindance animation, camera, props, clues, visibility and audio |
| gqt006 | 2 | 77 | 27 dialogue, 27 actor RID, nine RID camera, ten camera and four gaze events |
| gqt007 | 1 | 2 | Dialogue events for the Barry lipsync probe |

No raw `.scene` resource was found in the registered source trees of GQT001–004
or the experiment projects. That is a statement about authored scene files,
not an assertion that those quests have no dialogue, external scene calls,
camera effects or other presentation.

## Story quests: dialogue is implemented more broadly than staging

The fourteen story-owned scenes are one Iris meeting for GQ001, one Cinder
meeting for GQ002, two Iris scenes for GQ003, and ten Velvet/field scenes for
GQ004. Every section event in those fourteen resources is a dialogue event.
Choice, actor acquisition and embedded quest graph operations still exist
outside the section-event count. The claim is therefore a gap in authored
performance events, not an absence of scene interaction or quest behavior.

The shared GQ000 prototype adds gaze events but is not a full staged-performance
template. Its scene lifecycle, actor/lipsync slot history and named acceptance
exit remain documented in the
[runtime flow](../../../../../projects/ghostline/quests/gq000/implementation/runtime-flow.md)
and [scene authoring rules](../../../../authoring/scenes.md).

GQ003 is the clearest production-status boundary. Its
[scene implementation notes](../../../../../projects/ghostline/quests/gq003/implementation/scenes.md)
describe eight dialogue manifests / 128 spoken lines, while only the opening
briefing and safe-site exchanges are formal scene sources. The other delivery
sets retain `runtime_pending`; localization coverage does not prove playback
wiring. Durations and WEM paths remain planning values until voice production.
The 31 dialogue events in its two formal scene resources must not be reported
as completion of all 128 authored lines or their cinematic production.

GQ004 provides stronger lifecycle evidence: its
[retrospective](../../../../../projects/ghostline/quests/gq004/RETROSPECTIVE.md)
records the user's successful full playthrough and the repaired readiness,
defer/return, transfer/retry, reward and cleanup behavior. That evidence is
valuable for staging extensions. It does not turn its dialogue-only section
event inventory into authored gestures, camera tracks or prop choreography,
and it does not establish exhaustive branch/save-state coverage.

## Existing specialized testbeds are useful donor boundaries

GQT005's launch scene has four dialogue and four look-at events. Its analysis
scene has thirteen events: two skeletal-animation, one RID camera, two
braindance visibility, three prop attachment, three clue and two duration-audio
events. Its [README](../../../../../projects/test-quests/gqt005/README.md)
explicitly keeps runtime braindance playback as an in-game test requirement.
Use this as a playback/analysis integration fixture, with seek/rewind/layer
and cleanup acceptance, rather than as proof of a finished cinematic.

GQT006 already demonstrates scene assembly with actor RID and camera playback.
The main scene has 45 events; the separate intimacy scene has 32, comprising
24 actor RID and eight RID camera events. Its
[authoring notes](../../../../../projects/test-quests/gqt006/README.md)
keep scene/animation/voice prerequisites distinct from the quest compiler and
state that structural migration checks do not establish new in-game evidence.
The [release text](../../../../../projects/test-quests/gqt006/RELEASE.md) is
explicitly a draft. Neither should be upgraded into runtime validation here.

GQT007 isolates spoken-line/lipsync work. Two dialogue events are a useful
audio/facial regression probe, but do not test staged body animation or camera
ownership.

## Recommended order for implementation

1. Extend a small, proven conversation lifecycle with a coordinated starting
   idle, one gesture and intentional gaze. Preserve exact screenplay and VO
   bindings and named exits. The common vanilla pattern is conventional
   animation plus attention, so it is the most broadly applicable first step.
2. Expose named section ports for physical actions and transitions. Use the
   Barry source case to retain timed signals, socket ordinals and workspot
   handoffs; ensure interruption before and after the action has a defined
   return state.
3. Add a camera-beat contract that states the controlled camera, marker,
   activation, blends and restoration. Distinguish phone cameras, player
   parameter changes and RID camera playback in both specs and review output.
4. Expand RID/prop choreography through the GQT006 boundary, binding table
   indices, resource handlers, serials, actor components and marker placement.
   A reused vanilla RID is not proof of compatibility with a different rig,
   height, placement or prop setup.
5. Validate GQT005's complete analysis lifecycle before promoting braindance
   production: seek, rewind, layer-specific clues, interrupted exit, restoration
   and replay. Do not treat animation or serialization success as that milestone.

These are follow-on proposals. This research changes documentation and
inspection tools only; it does not regenerate, package or install quest assets.
