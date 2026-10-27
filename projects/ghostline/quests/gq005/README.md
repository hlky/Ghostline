# Five-Star Service

*The Customer Is Always Wrong*

Satirical courier side quest. Target: 15 minutes. First authoring draft;
locations, dialogue and character design remain editable.

V collects three Deliverance Logistics packages from its AKPP subcontractor.
The app sends V to a residential building, across the neighbourhood, then back
to the first building. Each customer has a different way to make delivery
impossible while insisting that the problem is V. Completed deliveries earn
4.59/5; the advertised bonus requires 4.60.

The humour comes from recognisable courier work: missing access codes,
contradictory instructions, oversized parcels, unanswered buzzers, and a route
that treats couriers' time as free. Customers are unreasonable in distinct,
specific ways. Avoid turning every exchange into a corporate slogan.

## Review packet

- [Walkthrough and state flow](flow.md)
- [Complete spoken dialogue draft](script/dialogue.md)
- [App, terminal, messages and journal text](script/readables.md)
- [Location requirements and survey checklist](implementation/locations.md)
- [Quest blocks, lifecycle and first playable milestone](implementation/plan.md)
- [Office manager: Leena Shah](../../characters/leena.md)
- [Character builder manifest](../../characters/leena.character.json)

## Proposed boundaries

AKPP is the pickup and debrief hub. Keep its exterior branding and Ru Lai intact.
Deliverance supplies the contracts and app; AKPP is a local subcontractor. No
connection to the Quiet Spine storyline is required to understand this job.

Three packages, three customers, one security guard, Leena and V. Delivery one
and three share a residential building. Delivery two is a short journey away,
with a broken passenger lift and an accessible stair route. A luxury retrofit
is preferred to a new tower. The distant site supplies the penthouse encounter;
we do not need a fully enterable high-rise.

The app's 90-second estimate is an unfair performance target, not a quest-fail
timer. Its overrun persists as a joke without penalising exploration or dialogue.
The 4.59 result is fixed by company policy, not by the player's real speed,
dialogue responses or accessibility settings. Completion is always possible.

Proposed reward: €$1,800 guaranteed, €$1,200 advertised bonus. All endings pay the
base once. Exposing the scheme preserves evidence but brings no immediate
bonus; accepting settles the base only; correcting the system releases V's
bonus plus the local depot's held courier bonuses. These amounts are tuning
values. No reward should be silently lost after interrupted dialogue.

## Current production state

Quest plan, full dialogue and readables authored. Delivery sites not selected.
Leena's manifest validates; isolated character source generation passes. The
candidate is not a rendered, packed or installed character. Head geometry,
appearance review, VO, scenes and native quest route are pending. The installed
AKPP office still uses the generic seated worker.

The next runtime milestone is one complete pickup → provisional delivery →
return → reward route, before bulk VO or appearance polish. See the plan for
the exact acceptance gate.
