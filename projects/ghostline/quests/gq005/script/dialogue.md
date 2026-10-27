# Five-Star Service — spoken dialogue draft 1

Unapproved performance draft. Stable authoring IDs; no synthesized VO yet.
Bracketed text is direction. **Choice text is unvoiced UI**; the V line below
it is spoken. Responses rejoin unless a destination is named. V dialogue is
gender-neutral and supports separate voice performances.

## 01 — AKPP offer

Trigger: V initiates conversation with Leena, ready at her desk. No prior quest
knowledge required. First hello plays once; returning before acceptance uses
`FSS_01_RETURN`.

| ID | Speaker | Line |
| --- | --- | --- |
| FSS_01_HELLO | Leena | If you're here about a parcel, I haven't got it. If you're here for work, I've got three. |
| FSS_01_V_WORK | V | Depends what they pay. |
| FSS_01_OFFER | Leena | Eighteen hundred for the route. Twelve hundred bonus if your service score hits four point six. |
| FSS_01_V_ROUTE | V | Three stops. First and last are in the same building. |
| FSS_01_ROUTE | Leena | Yeah. |
| FSS_01_V_ORDER | V | So I'll do those together. |
| FSS_01_ORDER | Leena | App only opens one recipient window at a time. Change the order and it calls the others failed attempts. |

Choices, all available:

**“Who am I working for?”**

| ID | Speaker | Line |
| --- | --- | --- |
| FSS_01_V_COMPANY | V | Sign says AKPP. Contract says Deliverance. |
| FSS_01_COMPANY | Leena | We sort their parcels. They send the routes. When somebody complains, we're AKPP again. |

**“Ninety seconds?”**

| ID | Speaker | Line |
| --- | --- | --- |
| FSS_01_V_TIME | V | Says the whole route takes ninety seconds. |
| FSS_01_TIME | Leena | That's travelling. Doesn't include doors. |
| FSS_01_V_DOORS | V | Delivering to a lot of open fields? |
| FSS_01_DOORS | Leena | Waiting counts against you, though. |

**“What's in the big one?”**

| ID | Speaker | Line |
| --- | --- | --- |
| FSS_01_V_WEIGHT | V | That one's a crate. |
| FSS_01_WEIGHT | Leena | Bottled water. Thirty-six kilos. Listed as a small packet. |
| FSS_01_V_SMALL | V | Compared to what? |
| FSS_01_SMALL | Leena | Doesn't say. |

**“I'll take the route.”** → commit acceptance, grant parcels once.

| ID | Speaker | Line |
| --- | --- | --- |
| FSS_01_V_ACCEPT | V | Fine. Load me up. |
| FSS_01_ACCEPT | Leena | First one's got no access code. Call the customer when you get there. Keep the receipts. |

**“Maybe later.”** → defer, no items or timer.

| ID | Speaker | Line |
| --- | --- | --- |
| FSS_01_V_DEFER | V | Got something else first. |
| FSS_01_DEFER | Leena | Fine. I'll be here. |
| FSS_01_RETURN | Leena | Still got those three, if you want them. |

## 02 — first building, security desk

Trigger: current stop A, V uses desk interaction. Guard is available. The same
guard recognises V at stop C. Security is not the target of the joke.

| ID | Speaker | Line |
| --- | --- | --- |
| FSS_02_GUARD | Guard | Delivery code? |
| FSS_02_V_CODE | V | Says “concierge will know.” |
| FSS_02_GUARD_CODE | Guard | Concierge would love to. |

**“I'll call them.”** → recipient intercom/call.

| ID | Speaker | Line |
| --- | --- | --- |
| FSS_02_V_CALL | V | I'll get the code. |
| FSS_02_CUSTOMER | Adrian | You're late. |
| FSS_02_V_ACCESS | V | At security. Need your access code. |
| FSS_02_INSTRUCTIONS | Adrian | I put it in the instructions. |
| FSS_02_V_READ | V | “Concierge will know.” That's all you've put. |
| FSS_02_CODE | Adrian | Well, ask him. It's seven-three-one-nine. Don't tell anyone else. |

**“Can you call upstairs?”** → same code fact through guard.

| ID | Speaker | Line |
| --- | --- | --- |
| FSS_02_V_GUARDCALL | V | Can you call the apartment? |
| FSS_02_GUARDCALL | Guard | Tried when you came in. He told me to ask the courier. Hang on. |
| FSS_02_GUARDRESULT | Guard | Seven-three-one-nine. Apparently we should both have known. |

Rejoin: access granted once; objective changes to apartment A.

| ID | Speaker | Line |
| --- | --- | --- |
| FSS_02_ACCESS | Guard | You're cleared. Door on the left. |
| FSS_02_ADRIAN_DOOR | Adrian | You weren't supposed to bring it through the lobby. |
| FSS_02_V_LOBBY | V | Only entrance security would let me use. |
| FSS_02_ADRIAN_LIFT | Adrian | There are people in there. They don't want to look at parcels. |

**“Here's your parcel.”**

| ID | Speaker | Line |
| --- | --- | --- |
| FSS_02_V_HANDOVER | V | Here. Sign. |
| FSS_02_ADRIAN_SIGN | Adrian | Next time, read the instructions. |

**“Then collect it yourself.”**

| ID | Speaker | Line |
| --- | --- | --- |
| FSS_02_V_RETORT | V | Could've saved them the sight. Picked it up yourself. |
| FSS_02_ADRIAN_RETORT | Adrian | I pay for delivery so I don't have to do that. Give it here. |

Either branch transfers parcel A and acknowledges delivery. App assigns B.

## 03 — drinks delivery

Trigger: B is current, V examines broken lift. Notice already visible; lift
interaction plays these lines once. Stairs remain usable without examining it.

| ID | Speaker | Line |
| --- | --- | --- |
| FSS_03_V_LIFT | V | Lift's dead. |
| FSS_03_DARIA_CALL | Daria | You're downstairs? Bring it up. |
| FSS_03_V_WATER | V | Thirty-six kilos of water. Want to meet me? |
| FSS_03_DARIA_MEET | Daria | I've got guests. I can't leave them. |
| FSS_03_V_GUESTS | V | One of them help carry it? |
| FSS_03_DARIA_HELP | Daria | They're guests. |

At penthouse door: complete stair approach, Daria ready.

| ID | Speaker | Line |
| --- | --- | --- |
| FSS_03_DARIA_DOOR | Daria | In the kitchen. Don't put it on the floor. |

**“Delivery ends here.”**

| ID | Speaker | Line |
| --- | --- | --- |
| FSS_03_V_LIMIT | V | Delivery's to your door. Here it is. |
| FSS_03_DARIA_LIMIT | Daria | Unbelievable. Fine. I'll have somebody move it. |

**“Where do you want it?”** → short service-corridor drop, no extra reward gate.

| ID | Speaker | Line |
| --- | --- | --- |
| FSS_03_V_KITCHEN | V | Where's the kitchen? |
| FSS_03_DARIA_KITCHEN | Daria | Through there. Not that counter. The other one. |
| FSS_03_V_DONE | V | There. |
| FSS_03_DARIA_WARM | Daria | It's warm. |

Both branches consume B and acknowledge receipt; no branch can deny delivery.
App assigns C at building A. Play once after the receipt menu closes:

| ID | Speaker | Line |
| --- | --- | --- |
| FSS_03_V_BACK | V | Back there? Could've done this one half an hour ago. |

Performance note: replace “half an hour” with “before coming here” if observed
route length makes that exaggeration distracting.

## 04 — return to the first building

Trigger: C current, guard proximity after speech cooldown.

| ID | Speaker | Line |
| --- | --- | --- |
| FSS_04_GUARD | Guard | Forget something? |
| FSS_04_V_RETURN | V | App did. |
| FSS_04_GUARD_RETURN | Guard | Same floor. Other side. |

At C buzzer: instruction text says ring once; first ring starts the brief wait.

| ID | Speaker | Line |
| --- | --- | --- |
| FSS_04_NIKO_RING | Niko | Don't ring. Dog goes mad. |
| FSS_04_V_RING | V | You wrote “ring once.” |
| FSS_04_NIKO_LEAVE | Niko | Just leave it outside. |

After the wait or second interaction, Niko opens the door before parcel transfer.

| ID | Speaker | Line |
| --- | --- | --- |
| FSS_04_NIKO_DOOR | Niko | Were you about to leave that unattended? |

**“You told me to.”**

| ID | Speaker | Line |
| --- | --- | --- |
| FSS_04_V_TOLD | V | You just told me to leave it. |
| FSS_04_NIKO_TOLD | Niko | Not if there's nobody watching it. |

**“Take the parcel.”**

| ID | Speaker | Line |
| --- | --- | --- |
| FSS_04_V_TAKE | V | Take it. |
| FSS_04_NIKO_TAKE | Niko | No need to be rude. |

Both acknowledge C. Show score after V leaves the conversation, not over speech.

## 05 — settlement at AKPP

Trigger: all three receipts, V speaks to Leena. Score already visible.

| ID | Speaker | Line |
| --- | --- | --- |
| FSS_05_LEENA | Leena | All three? |
| FSS_05_V_SCORE | V | Delivered. Four point five nine. |
| FSS_05_LEENA_SCORE | Leena | Yeah. |
| FSS_05_V_KNEW | V | You knew. |
| FSS_05_LEENA_KNEW | Leena | I knew you wouldn't get the bonus. Didn't know what they'd call it this time. |

**“You sold me that bonus.”**

| ID | Speaker | Line |
| --- | --- | --- |
| FSS_05_V_SOLD | V | You used it to get me out the door. |
| FSS_05_LEENA_SOLD | Leena | I did. Needed the route covered. That's not an excuse. |

**“Who controls the score?”**

| ID | Speaker | Line |
| --- | --- | --- |
| FSS_05_V_CONTROLS | V | Can you change it? |
| FSS_05_LEENA_CONTROLS | Leena | Not from the dispatch screen. There's a settlement account. They left me access to clear failed payments. |
| FSS_05_V_LOOK | V | Show me. |
| FSS_05_LEENA_LOOK | Leena | Policy's on my terminal. Read it yourself. |

**“Just pay the contract.”** → accept ending, base pay exactly once.

| ID | Speaker | Line |
| --- | --- | --- |
| FSS_05_V_ACCEPT | V | Eighteen hundred. Now. |
| FSS_05_LEENA_ACCEPT | Leena | Sent. Sorry, V. |

If V leaves before reading: Leena idle; policy remains available. Reading sets
`policy_read`. V returns to Leena; these lines play once:

| ID | Speaker | Line |
| --- | --- | --- |
| FSS_05_V_CAP | V | They cap the score below the bonus. Doesn't matter how the deliveries go. |
| FSS_05_LEENA_CAP | Leena | No. And the hold list's everyone from this depot. Not just you. |

**“How long have you worked here?”** optional, returns to final choices.

| ID | Speaker | Line |
| --- | --- | --- |
| FSS_05_V_YEARS | V | How long you been doing this? |
| FSS_05_LEENA_YEARS | Leena | Six years on routes. Two behind this desk. Thought sitting down would be the good bit. |

Final choices (accept still available):

**“Publish the evidence. Redact the couriers.”** → expose confirmation.

| ID | Speaker | Line |
| --- | --- | --- |
| FSS_05_V_EXPOSE | V | Send me the policy and the withheld payments. Keep the couriers' names out of it. |
| FSS_05_LEENA_EXPOSE | Leena | Depot number will still be on it. They'll come here first. |
| FSS_05_V_EXPOSE_CONFIRM | V | You want me to stop? |
| FSS_05_LEENA_EXPOSE_CONFIRM | Leena | No. Give me a minute to strip the addresses. |

Terminal action **“Publish redacted evidence”** commits expose. Then:

| ID | Speaker | Line |
| --- | --- | --- |
| FSS_05_LEENA_EXPOSE_DONE | Leena | Base pay's sent. Got a copy somewhere they can't delete it? |
| FSS_05_V_EXPOSE_DONE | V | More than one. |

**“Release the held bonuses.”** → correct confirmation.

| ID | Speaker | Line |
| --- | --- | --- |
| FSS_05_V_CORRECT | V | Payments are already there. Change eligibility, send the batch. |
| FSS_05_LEENA_CORRECT | Leena | It'll log my terminal. |
| FSS_05_V_CORRECT_CONFIRM | V | Your call. |
| FSS_05_LEENA_CORRECT_CONFIRM | Leena | I've still got six weeks on that list. Move over. |

Terminal action **“Release depot bonus batch”** commits correct. Then:

| ID | Speaker | Line |
| --- | --- | --- |
| FSS_05_LEENA_CORRECT_DONE | Leena | Yours went through. Rest are clearing. |
| FSS_05_V_CORRECT_DONE | V | There. Five-star service. |

Neither confirmation previews a successful action. Until the terminal commit,
V may leave, return, or select the other resolution. Final settlement messages
and courier responses live in `readables.md`.

## Return and retry lines

| ID | Trigger / speaker | Line |
| --- | --- | --- |
| FSS_R_LEENA_ACTIVE | Leena; route active | Trouble getting in, or trouble getting them to answer? |
| FSS_R_LEENA_POLICY | Leena; debrief, policy unread | Dispatch policy. On the terminal. |
| FSS_R_LEENA_PENDING | Leena; policy read, ending uncommitted | Haven't touched it. Your choice. |
| FSS_R_CUSTOMER_LATER | Future-stop intercom | Your delivery window hasn't started. |
| FSS_R_LEENA_ACCEPT | Leena; accept complete | No, I haven't found you another route. |
| FSS_R_LEENA_EXPOSE | Leena; expose complete | Been told not to discuss the new policy. Haven't seen a new policy. |
| FSS_R_LEENA_CORRECT | Leena; correct complete | Three people called to check if the payment was a mistake. Told them to spend it. |
