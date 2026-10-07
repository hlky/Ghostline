# The Machine Stops Runtime Flow

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
