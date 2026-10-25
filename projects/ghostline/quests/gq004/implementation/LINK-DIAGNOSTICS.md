# Inert recovery prompt: read-only trace

The player confirmed body rendering, intro distance and Velvet retention are
fixed. Selecting recovery still does nothing and leaves the prompt visible.
The required mechanic remains a personal-link transfer without a minigame.
GQ001 and the current GQ002 implementation use the ordinary breach flow; that
candidate was stopped before publication or installation when the player chose
to retain the transfer. The installed archive remains `a1053fd8721b`.

The existing location helper loads `link_diagnostics.lua` at startup. It adds
observers only, not overrides. It does not execute actions, alter event arguments,
change controller state, spawn actors, or write quest facts.

After restarting the game, load the save, look at recovery and select it once.
The log is written beside the installed helper:

`K:/Cyberpunk 2077/bin/x64/plugins/cyber_engine_tweaks/mods/ghostline_love_actually_scout/love-actually-link-trace.jsonl`

It records hook setup results, live interaction record fields, relevant quest
facts and device states, the interaction event, RPG action processing, the
personal-link controller before/after, and delivery to the device entity.
No further screenshots or manual log uploads are needed.

Interpret the first missing step before changing the runtime:

- No interaction event: inspect the live prompt's input/action payload.
- Interaction event but no action processing: inspect choice data and gating.
- Action processing but no controller event: inspect action persistent target.
- Controller event without a transition: inspect status and player restrictions.
- CONNECTING without entity delivery/animation: inspect the workspot path.
- CONNECTED without progress: inspect quest NodeRef resolution and attempt state.

The stock `TogglePersonalLink` default duration is 2.733 seconds in the local
reflected type; a missing duration has not been established as the cause.
Guard kills are not a recovery prerequisite and upload effects are dispatched
without waiting for live guards.

## Trace result and repair

The trace captured four recovery selections. Each carried one ActionHacking
action (duration 1 s). The controller was ON, NOT_CONNECTED, had a personal-link
slot and reported no disruptive player effect. No personal-link controller or
entity event followed. See `evidence/recovery-action-trace.json`.

Both device clones now set HackingSkillCheck difficulty NONE and isActive false.
This removes the active hacking-slot substitution while retaining forced personal
link, minigame skipping and the five-second quest transfer. Fresh `_link` NodeRefs
avoid saved skill-slot state. Capture IDs and coordinates are preserved.

The optional diagnostic updater was also corrected: CET does not expose
registerForEvent inside required modules. The module now returns its updater,
which the scout registers from init.lua. The original interaction/controller
observers did run and supplied the evidence above.
