# Player walkthrough and flow

All IDs below use the `gq005_` prefix at runtime. Dialogue line IDs and choice
labels are in `script/dialogue.md`; readables are in `script/readables.md`.
This is an authoring contract, not a compiled quest manifest.

| Stage | Player experience | Completion evidence | Target |
| --- | --- | --- | --- |
| offer | Speak to Leena at AKPP; ask questions, accept or defer. | Acceptance committed; three parcels issued once. | 2 min |
| drop_a | Reach building A. Security requires a code the customer omitted. Call them, receive the code, deliver to their door. | Correct parcel handed over; receipt A acknowledged. | 3 min |
| drop_b | App sends V away to building B. Carry a drinks shipment upstairs to an unpleasant penthouse customer. | Correct shipment handed over; receipt B acknowledged. | 4 min |
| drop_c | App sends V back to building A, next to the first drop. Customer ignores the buzzer, then complains about the handover. | Correct parcel handed over; receipt C acknowledged. | 2 min |
| reconcile | Receive 4.59/5, return to Leena and inspect the performance policy on her terminal. | Policy file actually read. | 2 min |
| resolve | Take the base pay, publish evidence, or release held bonuses. | One ending committed; base/relevant bonus granted once. | 2 min |

## Route and access

On acceptance show the three destinations and the fixed order A → B → A.
The app reserves a recipient access window only for the current stop. A future
door/buzzer explains this if V approaches early; it never discards a parcel.
The player can see the bad route and object to it during briefing. Navigation
to the next stop activates only after the current receipt is acknowledged.

At A, security is procedural rather than hostile. V can wait for the customer
to supply the code or ask the guard to call upstairs. Both converge on valid
entry. No mandatory hacking skill, bribery, combat or trespass. A late code is
the customer's responsibility in dialogue, despite the app's contrary metric.

At B the manifest calls the drinks a small packet. The bulk appears as a parcel
prop at pickup/handover, while inventory carries the delivery item. No forced
encumbrance, physics hauling or loss of movement controls in the first version.
The broken lift has a visible service notice and the stair entrance has clear
signage. At most two short playable flights connect to the penthouse retrofit;
do not make the player climb an empty tower for the joke.

At C the customer gives conflicting instructions: ring, do not ring, leave it,
do not leave it. A short authored wait advances to the confrontation even if V
does nothing. Waiting is skippable through a second buzzer interaction. The
parcel is accepted in either response branch; the complaint cannot softlock V.

## Debrief and ending knowledge

Leena first explains that she cannot manually raise the rating. V can immediately
take base pay. To expose or alter the system, V must read the policy file and
learn that access delays are scored as courier delays and the internal service
score is deliberately capped at 4.59. The public-facing score is presented as
customer satisfaction. This accounts for the exact result without pretending
three five-star customer ratings average to 4.59.

Reading the policy unlocks the settlement console and the evidence export. The
local depot batch contains already-earned courier bonuses awaiting release;
V does not invent credits or compromise every courier system in Night City.

| Final choice | Immediate result | Leena's stake | Closing evidence |
| --- | --- | --- | --- |
| Accept | Base pay only; dispute closed. | Keeps her head down; no approval speech. | Settlement message: €$1,800. |
| Expose | Export policy and batch evidence, publish with courier identities redacted; base pay. | Her depot may be audited. She helps redact worker details. | Courier response confirms receipt, not instant corporate collapse. |
| Correct | Set held bonuses eligible and submit the existing local batch; base plus €$1,200 bonus. | Audit log names her terminal. She knowingly grants access. | Batch confirmation and courier thanks. |

These are mutually exclusive resolutions. Preview actions do not commit a
choice. The final console prompt spells out the consequence before execution.

## Interruptions, persistence and cleanup

- Walk away from the offer: Leena returns to idle; the offer remains available.
- Leave mid-briefing: acceptance only commits at the final acceptance response.
- After acceptance: resume current stop; never reissue parcels or restart a wait.
- Stop dialogue: parcel transfer and receipt are one logical transaction. On
  return, replay a short pickup line, not the entire customer argument.
- Save/load during a delivery: retain possession or its acknowledged receipt,
  never neither. Repair a missing quest item only when its receipt is false.
- Leave during terminal reading: opening the menu is not reading the policy.
- Leave during resolution: resume until ending, payment and journal settle once.
- No customer death or combat is required. Select sites without ambient combat
  pressure. If a required actor becomes unavailable, retain a recovery route
  through their delivery intercom/secure drop, with receipt ownership intact.
- Leena's seated idle yields to scene control and resumes after exit. Replace
  the generic office worker; do not layer a second manager on top of it.
- After completion remove quest pins, outstanding parcel prompts, access-window
  locks and notification callbacks. Keep ordinary office furniture and Leena.

No exposed/corrected ending is gated by player build or a hidden skill check.
Optional technical dialogue can vary the explanation without removing choices.
