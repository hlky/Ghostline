# Act VI Script

## Act VI Text

### Drop-point package copy

#### Preserved route

**Item name:** Black Lantern Reconstruction Cipher

**Description:** Pair 07-B's physical reconstruction key and intact courier
index. The route remains live under Ghostline observation.

#### Burned route

**Item name:** Black Lantern Destruction Receipt

**Description:** A signed hardware attestation confirming that the courier
index was purged and its remaining packages received wipe commands.

### Final debrief

The preferred presentation uses Morrow as the required reply thread, followed
by non-blocking Iris and Patch messages. It opens on the final outcome, then
adds one shorter yard-stealth line. This avoids multiplying the player's final
reply choices into four separate branch combinations.

#### Preserved route opening

**Morrow:** Black Lantern is still carrying traffic. Now it carries our shadow
with it.

**Iris companion message:** You gave Morrow a map made of people. Make sure he
remembers what the symbols mean.

#### Burned route opening

**Morrow:** You protected the couriers and destroyed the only clean path
upward. Iris calls that mercy. I call it an expensive preference.

**Iris companion message:** Mara remembers one apartment now. Her own. That
will have to count as a victory.

#### Stealth succeeded addition

**Morrow:** The freight yard still treats Pair Seven as an internal failure.
No public description, no bounty. Clean work.

#### Stealth failed addition

**Morrow:** Freight security circulated your description. Black Lantern knows
the route was attacked, even if it does not know what survived.

#### Player reply group

**V choice: “People aren't route infrastructure.”**

**V:** Whatever lead we kept or lost, the couriers were never infrastructure.

**Morrow:** No. They were leverage. Our disagreement is whether destroying the
leverage removes the hand holding it.

**V choice: “Morita is still out there.”**

**V:** Morita is still out there. This only changes how we find him.

**Morrow:** Correct. You changed the route, not the destination. We adapt.

#### Common close

**Morrow:** Payment transferred. Keep the channel open. Black Lantern was a
route, not the destination.

**Patch companion message:** Should've told you what I knew. Next time I sell
confidence, ask what I'm using as collateral.

Grant `QuestRewards.gq003_completion`, set `gq003_completed = 1`, and succeed
`quests/minor_quest/gq003` after the final required message is visited.
