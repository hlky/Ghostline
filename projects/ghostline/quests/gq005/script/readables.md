# App, terminal and journal text — draft 1

All text is unvoiced unless separately assigned a spoken line. Location and
apartment labels are placeholders pending surveys. Keep company names fixed:
AKPP Logistics is the subcontractor; Deliverance Logistics owns the app.

## Contract screen

**Deliverance Logistics / Available route**

3 consignments · Estimated route: 00:01:30

Guaranteed route fee: €$1,800

Service bonus: €$1,200 · Required service score: 4.60 / 5

Follow the assigned delivery order. Recipient access windows are activated per
stop. An out-of-window visit does not count as a delivery attempt.

**Accept route** / **Not now**

The briefing exposes the bad route before acceptance. Do not hide the order
behind a surprise objective change; the return trip is the payoff.

## Consignments

| Item / label | Recipient | Handling text | Proposed inventory identity |
| --- | --- | --- | --- |
| A — Personal goods | Adrian Voss, building A, apartment A | Concierge will know. Deliver to door. | `Items.gq005_parcel_a` |
| B — Small packet | Daria Bell, building B, penthouse | Bottled water. 36 kg. Keep upright. | `Items.gq005_parcel_b` |
| C — Home accessories | Niko Hales, building A, apartment C | Ring once. Do not leave unattended. | `Items.gq005_parcel_c` |

Quest items have no resale value, cannot be dismantled and do not use weight
penalties. The drinks prop communicates bulk at transfer. These are proposed
records, not existing item assets.

## App notifications

Only one notification at a time. Queue until conversation ends; never obscure a
choice. Persist once-only flags. The elapsed route clock is cosmetic.

| ID | Trigger | Text |
| --- | --- | --- |
| FSS_APP_START | Accepted and parcels granted | Route started. Estimated completion: 90 seconds. |
| FSS_APP_LATE | Target exceeded outside dialogue | You're behind schedule. Please continue safely. |
| FSS_APP_ACCESS | Waiting for first access code | Time at destination is included in your performance score. |
| FSS_APP_A | Receipt A | Delivery 1 of 3 complete. Next recipient window active. |
| FSS_APP_BULK | Inspect drinks/lift | This consignment qualifies for Small Packet handling. |
| FSS_APP_B | Receipt B | Delivery 2 of 3 complete. Return to building A. |
| FSS_APP_C | Receipt C | Route complete. Calculating customer satisfaction… |
| FSS_APP_SCORE | After completion notification | Customer satisfaction: 4.59 / 5. Bonus threshold: 4.60. Bonus not awarded. |

## Broken lift notice

**Passenger lift unavailable**

Residents: use the service stairs. Deliveries remain door-to-door.

Repair appointment: awaiting access to lift control room.

## Office terminal: dispatch policy

File title: **Service score — depot guidance**

Customer star ratings are inputs to the Service Performance Index. The index
also includes route adherence and time at destination. The courier app labels
the combined result “Customer satisfaction.” Do not give recipients the index
formula.

Access delays, concierge verification and unanswered doorbells remain courier
time. Consignment size is taken from the booking category; depot staff cannot
correct it after route assignment.

Current automatic settlement configuration:

    Standard route payout:       ENABLED
    Automatic bonus release:     HELD
    Maximum displayed index:     4.59
    Bonus eligibility threshold: 4.60
    Recipient rating inputs:     RECEIVED

Do not describe held bonuses as unpaid wages in courier correspondence.
Use “performance reconciliation.”

**Read-state contract:** set `gq005_policy_read` when this file is actually
selected/read, not when the terminal UI is opened. This is sufficient evidence
for the final branches; no separate hidden readable is mandatory.

## Office terminal: held payments

File title: **AKPP depot / current reconciliation batch**

Approved route fees have cleared. Earned service bonuses are retained pending
eligibility validation. Individual courier records and private addresses are
restricted to settlement staff.

Proposed readable rows: V — €$1,200; L. Shah — six weeks outstanding; additional
local courier entries. Names/amounts beyond V are authored fiction, not a query
against actual game NPC accounts. Avoid assigning a claimed citywide total.

## Settlement actions

Available after reading policy and returning to Leena's debrief.

**Close dispute and accept €$1,800**

You receive the guaranteed route fee. No service bonus will be paid.

**Publish redacted evidence**

Share the score policy and held-payment evidence. Remove courier identities and
recipient addresses. The depot can still be identified. You receive €$1,800.

**Release depot bonus batch**

Mark the local depot's held bonuses eligible and submit payment. The action is
logged against Leena's terminal. You receive €$1,800 plus your €$1,200 bonus.

Each has **Confirm** / **Back**. Back changes no facts or money. The confirmation
is a fictional in-game interaction; no real external service is contacted.

## Closing messages

**Accept — Deliverance Logistics**

Your route fee of €$1,800 has been transferred. Your dispute is closed.
Thank you for choosing flexible work.

**Expose — local courier group**

Got the files. Policy, cap, payment holds. Kept the redacted copy mirrored.
They've been telling everyone it was just their score.

**Correct — local courier group**

Bonus just cleared. Six weeks. Someone else got theirs too.
If this was you, thanks. If it wasn't, don't tell them.

**Correct — Deliverance Logistics**

Your service reconciliation is complete. Payment received: €$3,000.
Your account has been selected for a routine compliance review.

Only the chosen ending's messages are sent. Courier acknowledgement happens
after the committed action, not merely after viewing its menu option.

## Journal

**Offer:** Three packages, one route, and a bonus that almost doubles the pay.
Leena at AKPP handles pickup. Deliverance handles the directions. Apparently
neither of them handles common sense.

| Objective ID | Player-facing objective |
| --- | --- |
| pickup | Collect the Deliverance parcels from Leena. |
| drop_a_access | Get access to the first recipient's building. |
| drop_a | Deliver Adrian's parcel. |
| drop_b | Deliver Daria's shipment. |
| drop_c | Return to the first building and deliver Niko's parcel. |
| return | Return to Leena for payment. |
| policy | Read the service-score policy on Leena's terminal. [Optional until choosing exposure/correction.] |
| resolve | Settle the route payment. |

**Accept completed:** All delivered. Bonus denied by a hundredth of a point.
V took the route fee. Deliverance called that satisfaction.

**Expose completed:** The score was capped below the bonus threshold. V
published the evidence, with courier names stripped out. The files are out
there. What happens to Deliverance next is another question.

**Correct completed:** V released the depot's withheld bonuses. Leena's
terminal took the blame. At least this time the money went where it belonged.
