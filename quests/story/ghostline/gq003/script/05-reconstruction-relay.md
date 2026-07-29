# Act V Script

## Act V Text

### Relay clue responses

#### Carrier rack

**Scan title:** PAIR 07-B CIPHER RACK

**V:** Cipher housing is still cold. Index is live.

**Iris:** Pull the physical key. Do not slot it into anything until we control
the core.

Grants `Items.GhostlineBlackLanternCipher`.

#### Reconstruction core

**Scan title:** MNEMONIC RECONSTRUCTION CORE

**V:** Core has two execution paths. Verify and forward, or revoke and wipe.

**Iris:** Preserve or burn. Morita built the moral argument into the interface
so operators could call themselves technicians.

#### Courier ledger

**Scan title:** BLACK LANTERN COURIER LEDGER

**V:** Twenty-six subject aliases. Seven completed pairs. Four marked
unrecoverable.

**Morrow:** And one live dispatch signature. Morita touched this ledger less
than an hour ago.

### Courier ledger

```text
BLACK LANTERN / MNEMONIC TRANSPORT LEDGER
AUTHORIZED VIEW: ROUTE OPERATOR

PAIR 01  VERIFIED      SUBJECT INDEX SEALED
PAIR 02  VERIFIED      SUBJECT INDEX SEALED
PAIR 03  PARTIAL       MNEMONIC SUBJECT UNRECOVERABLE
PAIR 04  VERIFIED      SUBJECT INDEX SEALED
PAIR 05  REVOKED       CIPHER LOST / SUBJECTS WIPED
PAIR 06  PARTIAL       DESTINATION IDENTITY UNSTABLE
PAIR 07  EXPEDITED     MARA VENN / CIPHER INBOUND

ACTIVE ROUTE AUTHORITY: K. MORITA
UPSTREAM AUTHORITY: [EXTERNAL ATTESTATION]

OPERATOR NOTE:
Courier names are retained until destination reconstruction is confirmed.
Deletion before confirmation invalidates route payment and upstream audit.

PENDING SIGNAL:
PAIR 08 selection suspended -- KABUKI CLASSIFIER OFFLINE
```

### Morrow and Iris argument

This is one conceptual stage but requires a custom phase or compiler support
for sequential messages from two contacts. The ordering is fixed so the player
hears both positions before the choice.

**Morrow:** The ledger carries Morita's live attestation. Preserve the route
and I can follow the next handshake upstream.

**Iris:** The same route carries names for every stolen identity. Leave it open
and anyone with the cipher can reconstruct them again.

**Morrow:** Burn it and Morita disappears behind the organization that paid
him. We save today's couriers and guarantee replacements tomorrow.

**Iris:** Preserve it and the people already inside remain inventory. A future
rescue does not cancel a present weapon.

**Morrow:** V, keep the line open. We trace Morita, copy what we need, then
close it from the top.

**Iris:** There is no harmless copy. Erase the index and issue the wipe. Mara
keeps her life. The route loses everyone else's.

### Final choice

#### Preserve the route

**Choice text:** Keep the line open. Find Morita.

**V:** Preserve the index. We use it to find Morita.

**Morrow:** Confirmed. Authenticate the cipher and leave the uplink intact.

Sets `gq003_choice_preserve = 1`.

#### Burn the identities

**Choice text:** Erase the route. Nobody gets the names.

**V:** Burn the index. Nobody carries these people again.

**Iris:** Confirmed. Revoke every package, then destroy the local key.

Sets `gq003_choice_burn = 1`.

### Core-operation feedback

#### Preserved route

**System:** ROUTE ATTESTED / PAIR 07 VERIFIED / NEXT HANDOFF PENDING

**Morrow:** Black Lantern accepted the cipher. I have Morita's next handshake.

**Iris:** Mara's fragments are scrubbed. The wider index is still live. That
part is yours now.

Sets `gq003_route_preserved = 1`. The intact cipher remains in inventory.

#### Burned identities

**System:** ROUTE REVOKED / SUBJECT INDEX PURGED / PACKAGE WIPE ISSUED

**Iris:** Index is gone. Wipe acknowledgements are returning now.

**Morrow:** Morita's signature just vanished. Save the signed destruction
receipt. It is the only physical proof Black Lantern existed.

Sets `gq003_route_burned = 1`. The cipher is removed and
`Items.GhostlineBlackLanternReceipt` is granted.
