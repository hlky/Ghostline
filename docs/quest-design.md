# Ghostline Quest Design

This document records the recovered narrative brief and the canonical writing
selected for `gq000`. Runtime graph and localization implementation details
remain in `docs/quest-scene-flow.md`.

## Faction

Ghostline is a loose netrunner cell operating from half-abandoned telecom
infrastructure in Watson and Japantown. It is a broker collective rather than
a conventional street gang: intrusion specialists, signal thieves, courier
coders, braindance editors, and blackmail archivists. Ghostline hires outside
muscle when a job crosses into meatspace.

### Morrow

Ghostline's operational lead. A former network-maintenance contractor who
learned how much supposedly dead city infrastructure still carries private
traffic. Calm, precise, and slightly condescending.

### Iris

A braindance editor and memory splicer. Iris turns recovered fragments into
usable leads. She is more empathetic than the rest of the cell, which makes
her dangerous in a different way.

### Patch

Field courier and local fixer-contact. Patch meets V in person, talks fast,
and projects more confidence than he consistently feels.

## Story Spine

Ghostline has learned that the Tyger Claws are facilitating a quiet
data-laundering route for an Arasaka-adjacent broker. `gq000` is deliberately
small: meet Patch, reach the relay, breach it, recover the datacache, and
deliver it to an ordinary drop point.

The bridge meeting and its dialogue are implemented and runtime-confirmed. The
first cache site is implemented around a native hackable data relay with three
Tyger Claw guards. The delivery uses the live, map-labelled vanilla
`drop_point_009` machine in Kabuki, roughly 252.7 metres from the relay and
outside its cleanup radius.

## Canonical Quest Flow

1. Patch messages V and requests a bridge meeting.
2. V can ask about Ghostline and why Patch chose them before asking for the
   job.
3. Patch identifies a Tyger Claw relay that appears dead from the street.
4. V can press Patch about the client before accepting.
5. V reaches the cache site. Combat and stealth remain valid; defeating every
   guard is not a prerequisite for using the relay.
6. V connects to the relay and must complete the access-point hacking
   minigame.
7. Success immediately sets `gq000_cache_acquired`, closes the cache objective,
   and automatically grants the datacache quest package plus two readable
   archived-conversation shards with pickup notifications and matching Journal
   entries.
8. `Leave the relay area.` becomes the tracked objective; V clears the
   75-unit cleanup boundary before the surviving Tyger Claws can regroup.
9. V takes the cache to Kabuki's `drop_point_009`; the machine's native deposit
   interaction consumes the reserved package.
10. Morrow confirms delivery, V chooses how to answer, and Morrow hints that
    the laundering route has another end. Ghostline's completion reward is
    issued after the final message is read.

## Data-Courier Network Names

Five names were requested in the recovered brief. **Quiet Spine** is canonical
for `gq000`; the others are retained for future routes or aliases.

- Quiet Spine (canonical)
- Dead Channel
- Black Lantern
- Kintsugi Line
- Paper Tiger Route

## Archived Conversation Shards

### Archived conversation: Seki and K. Morita

```text
SEKI: Node six is carrying double tonight.
K. MORITA: Then split it between two couriers.
SEKI: Flesh couriers? Thought Quiet Spine stayed on the wire.
K. MORITA: Nothing stays on the wire through inspection. First courier carries
the cipher. Second carries the memory. Neither knows the other.
SEKI: And if the Claws open them?
K. MORITA: Then your fee becomes an apology to my employer.
```

Alternate variant:

```text
SEKI: Your packet missed the handoff.
K. MORITA: The courier did not. Check the second manifest.
SEKI: Two names, same faceprint.
K. MORITA: Quiet Spine does not move data. It moves the pieces required to
reconstruct it.
SEKI: That's a lot of theater for payroll records.
K. MORITA: You are not being paid to identify the audience.
```

### Archived conversation: Hiromi and K. Morita

```text
HIROMI: Little China relay is burned. Someone pinged the old municipal line.
K. MORITA: Move the next packet to Japantown. Quiet Spine, route C.
HIROMI: Drop is a braindance editor?
K. MORITA: The editor thinks she is cleaning signal noise. The courier thinks
he is moving scop. Keep it that way.
HIROMI: And the source?
K. MORITA: Above your invoice.
```

Alternate variant:

```text
HIROMI: Courier woke up remembering somebody else's apartment.
K. MORITA: Expected residue. Send him to the editor.
HIROMI: He saw the tower logo.
K. MORITA: He saw a reflection selected for him.
HIROMI: Quiet Spine is getting loud.
K. MORITA: Then stop discussing it on a channel I can archive.
```

## Message After Delivery

Canonical thread:

```text
MORROW: Cache authenticated. Clean extraction.
MORROW: Iris found a courier route folded into the payload. You brought us
more than Patch promised.

V: Then pay me for it.
MORROW: Already adjusted. Ghostline rewards useful surprises.

V: What kind of route?
MORROW: Names without faces, handoffs without addresses. Enough to know the
route is still live.

MORROW: Keep this number. When we find the other end, I may need someone who
works outside the wire.
```

Alternate thread:

```text
MORROW: Delivery verified. The cache was intact.
MORROW: Iris found a second signal nested inside it. That was not in Patch's
brief.

V: Sounds like your problem got bigger.
MORROW: More precise. Bigger problems are expensive; precise ones are useful.

V: So what did I drag home?
MORROW: A route with no declared destination and several familiar shadows.

MORROW: Consider the line open. If the route moves again, you will hear from
us.
```

## Runtime Facts

- `gq000_job_accepted`: Patch's scene exited through `job_accept`.
- `gq000_02_started`: the cache stage has initialized.
- `gq000_cache_acquired`: the relay's hacking minigame succeeded.
- `gq000_cache_delivered`: the cache was deposited at the selected drop point.
- `gq000_completed`: Morrow's completion thread has finished.

All five facts are wired across the root, meeting, cache, and delivery phases.
The drop-point controller additionally raises `gq000_datacache` from the quest
package's `friendlyName`; that engine-facing fact is distinct from the authored
`gq000_cache_delivered` milestone.
