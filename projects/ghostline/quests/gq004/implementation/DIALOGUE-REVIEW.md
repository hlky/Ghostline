# Dialogue flow review

The first playable flow treated downloading files as reading them. V discussed
the ledger and private research before the player had seen either. It also
played the copy confirmation after those discussions. The revised order is:

1. Recover the prototype and signing key; receive the sales ledger.
2. V confirms that the copy is clean.
3. Read **HEARTBREAKER / wholesale terms**; V and Velvet discuss the sales ledger.
4. After the ledger exchange, receive and read **VK / conditioning-interrupt research**;
   V asks about the original purpose.
5. Velvet asks V to read the revoke instructions.
6. After that exchange, receive and read **Deployment / preserve before patch**;
   the upload objective becomes available.
7. Velvet explains the corrected build; the naming exchange plays during the actual upload.
8. Upload, leave, and return to Velvet for the personal explanation and reward.
9. Confirm reward ownership and finish the quest. Send the optional closing text
   45 seconds later, through a separate native root so streaming-area conditions
   and unanswered phone replies cannot keep the journal open.

Each read gate uses `questJournalEntryVisited_ConditionType` with the shard's
`gameJournalOnscreen` path, matching the vanilla Bloody Ritual investigation
scene. Already visited shards satisfy the gate. Menu/pickup-preview visited
behavior remains an in-game check. New explicit read objectives prevent an
unexplained pause before the second access point becomes available.

Approved dialogue, audio and lipsync remain aligned. Spoken revisions use the
new user-selected takes and regenerated facial clips; no subtitle-only rewrites
are applied.

## Dialogue pass 02

Ten replacement Velvet takes were generated using the approved full-reference
voice direction and explicitly listening-approved by the user. Their hashes
and selection are recorded in `../voice/dialogue-review-02.json`.

The briefing now describes three guards and two access points, explains the
original protective purpose, and makes clear why the signing key is needed.
The field exchanges use simpler instructions and distinguish the guards'
short optics interruption from stopping conditioning of the victims. The
retry line fits both transfers. The replacement closing line removes the old
long pause. See DIALOGUE-FLOW.md for all current spoken text and choices.

Recovery remains armed while arrival VO plays, but the next spoken reply
waits for that explanation. Upload instructions finish before its socket is
enabled. V's naming remark and Velvet's short reply start with the actual
connection, inside the terminating attempt, so an interrupted attempt cancels
both the timer and that exchange. Success waits for both timer and exchange.

The remote actor previously spawned at the distant Kabuki meeting marker with
navigation validation enabled. Field scenes now use vanilla mq007's hidden
studio marker and the transfer phase holds the studio prefab. This repair
still requires in-game listening confirmation; the compiled voice tag was
already correct. No video call or runtime scripting dependency was introduced.

Deferring the meeting now starts its departure check immediately, using the
2.5 m engage radius. The old two-second delay could miss a quick departure
and return before the check subscribed.

## Transfer presentation

Recovery displays **Heartbreaker Protocol**; upload displays **Velvet Crash**.
The success path lets the native five-second progress bar finish its own outro
and lets the terminating attempt retire before a two-tick parent delay and disconnect. It no longer explicitly
hides the successful bar, which could race the HUD's delayed progress callback
and produce its failed animation. Genuine disconnection still cancels the bar.
The native unplug animation can still take time; no extra seconds-long pause
is added after a successful transfer.

The approach objective retains the central area marker. Recovery and upload
use separate always-loaded markers derived from each mounted access point;
they follow imported socket coordinates without adding capture stops.

After debrief, the main root retains the community until V leaves the 60 m
meeting area. That cleanup is independent of journal completion. The finish
root settles for two ticks rather than a full second before checking reward
ownership and completing the quest. The item and completion notifications are
therefore part of the same ending beat.
