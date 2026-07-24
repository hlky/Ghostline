# The Machine Stops (`gq002`)

## Premise

Patch introduces V to **Cinder**, the field organizer for **Common Ground**:
a mutual-aid collective that removes predatory smart infrastructure from
tenements and replaces it with repairable, locally controlled hardware.
Common Ground is anti-dependency rather than blindly anti-technology. Cinder
uses implants when lives depend on them, but distrusts systems whose owners can
withdraw access remotely.

Cinder wants a Kabuki telecom relay taken offline. She believes a
property consortium uses it to profile tenants before clearing a block for
redevelopment. At the site, V discovers that the relay also carries a
neighborhood clinic's emergency telemetry. The consortium deliberately mixed
the two services so that resistance to its surveillance would appear to endanger
patients.

The player can destroy the relay as contracted or preserve the medical route
and falsify evidence of a shutdown. Neither outcome is perfectly clean.

## Characters

### Cinder

Former Trauma Team subcontractor and current Common Ground organizer. Woman,
late thirties, practical clothes assembled from durable workwear, minimal
visible chrome, old medical gloves kept on her belt. Calm under pressure and
unimpressed by ideological purity. Her voice is low, dry, and controlled; anger
appears as precision rather than volume.

### Patch

Introduces the job by phone. He knows Common Ground through courier work and
frames Cinder as reliable but difficult to impress.

## Runtime Flow

1. `phone_job_offer`: Patch asks V to meet Cinder.
2. `meet_contact`: Cinder explains the suspected tenant-surveillance relay.
3. `reach_area`: V reaches the Kabuki relay.
4. `investigate_clues`: V scans all three local clues in authored order.
5. `read_shard`: V reads the recovered service-routing exchange.
6. `combat_encounter`: the consortium's hired security team intervenes.
7. `phone_conversation`: Cinder reviews the evidence and asks V to choose.
8. `choice_gate`: the phone outcome sets `destroy` or `spoof`.
9. `interact_device`: V performs the selected relay action.
10. `leave_area`: surviving security is cleaned up after V leaves.
11. `phone_conversation`: Cinder responds to the outcome and closes the job.

## Investigation Clues

1. **Tenant classifier** — a routing module tagged with apartment access,
   missed rent, and visitor-frequency fields.
2. **Trauma telemetry bridge** — an undocumented clinic uplink carrying
   pacemaker alerts and emergency dispatch packets.
3. **Failover invoice** — a maintenance record proving the consortium merged
   both services after Common Ground began targeting surveillance hardware.

All three scans are required. This is the first playable use of the generated
variable-length `investigate_clues` block.

## Selected Relay Site

The target anchor is the native small antenna access point at
`(-1111.06006, 1456.39990, 16.359997)` in Kabuki. It already uses
`AccessPointControllerPS` and exposes the normal jack-in interaction. The
surrounding rooftop contains both small and large satellite assemblies.

The exact source evidence and nearby collision actors are recorded in
`reference/world/gq002-locations.json`. Ghostline will place its own quest
device/ref, clues, guards, and triggers here rather than depending on the
vanilla street-story state.

## Archived Conversation

**Archived conversation: Sato and Keene**

> **SATO:** Tenant classifier is live. Missed payments, unauthorized occupants,
> behavioral flags. All routed through the Kabuki relay.
>
> **KEENE:** And the clinic telemetry?
>
> **SATO:** Same failover bus. If anyone cuts surveillance, the clinic loses
> remote diagnostics.
>
> **KEENE:** Good. Make removal expensive enough that activists have to choose
> who gets hurt.
>
> **SATO:** Tyger Claws are billing for on-site security.
>
> **KEENE:** Approve it. Fear is cheaper than rebuilding.

## Scene 1: Meet Cinder

### Opening

**Cinder:** Patch says you can remove a machine without turning the whole block
into a fireworks display.

### Optional choice: “Who are Common Ground?”

**V:** Common Ground. Activists, gang, support group?

**Cinder:** Neighbors with tools. We pull subscription locks off water pumps,
print parts corps stopped selling, keep old implants alive. If that sounds like
a gang, blame the city.

### Optional choice: “You hate tech?”

**V:** So what, you want everyone back to candles and hand-cranks?

**Cinder:** I want a hand-crank when the vendor kills the cloud. Technology
isn't the problem. Obedience disguised as convenience is.

### Main choice: “What needs removing?”

**V:** Show me the machine.

**Cinder:** Kabuki relay. Officially dead. Actually profiles tenants for
a redevelopment shell. Scan it first. I want proof before you cut power.

### Optional follow-up: “Why me?”

**V:** Your people fix machines. Why hire me to break one?

**Cinder:** Because the owners hired people who break bones. My crew are
technicians, not martyrs.

### Main follow-up: “I’ll check it.”

**V:** I'll inspect the relay. If it's what you say, it's gone.

**Cinder:** If it's what I say. Evidence first, conviction second.

## Relay Choice Phone Thread

### Opening

**Cinder:** Saw the scan. Tenant classifier and clinic telemetry share one
relay. Deliberate hostage circuit.

**Cinder:** Two options: destroy it after I warn the clinic, or blind the
classifier and spoof a failure.

### Main choice A: “Destroy the relay.”

**V choice text:** Destroy the relay.

**Cinder:** Hard stop. I'll warn the clinic and reroute what I can before you
pull it.

Sets `gq002_choice_destroy = 1`.

### Main choice B: “Spoof the shutdown.”

**V choice text:** Spoof the shutdown.

**Cinder:** Quiet cut. I'll feed the owners a clean failure report while you
blind the classifier.

Sets `gq002_choice_spoof = 1`.

**Cinder:** Make the call real. Jack in.

## Phone Debrief

### Destroy outcome

**Cinder:** Relay is dark. Clinic had six minutes' warning and Common Ground
has runners covering every monitored patient.

**V choice — “Cost of doing business.”**

**V:** Surveillance ended. Nobody said it would be clean.

**Cinder:** Clean is marketing copy. We kept the cost off the patients. That's
what matters.

**V choice — “They made patients shields.”**

**V:** Consortium wired sick people into its armor. That's on them.

**Cinder:** It started with them. Where it ended was our decision. Remember the
difference.

### Spoof outcome

**Cinder:** Their dashboard reports a catastrophic relay failure. Clinic
telemetry is still moving. Nicely dishonest.

**V choice — “Machines believe anything.”**

**V:** Machines believe whatever their owners pay them to measure.

**Cinder:** And owners believe green lights. For tonight, that works for us.

**V choice — “Move the clinic fast.”**

**V:** Lie has a shelf life. Get the clinic off that route.

**Cinder:** Already moving. You bought us twelve hours. We only needed three.

### Final message

**Cinder:** Payment sent. Patch was right about you. Common Ground may have
another machine that needs a more careful kind of stopping.

## Voice Production

- Generate three numbered takes for every spoken line.
- V must use the existing `v.pt` embedding from
  `C:\Users\user\Downloads\workspace\orkspace`.
- Cinder receives a reviewed design prompt and a reusable speaker embedding.
- Do not convert or install WEM files until one take per line has been selected.
