# Black Lantern Assets

## Inventory And Readable Assets

The records below are authored in
`source/resources/r6/tweaks/ghostline/gq003_black_lantern.yaml`.

| Record | Purpose | Lifecycle |
| --- | --- | --- |
| `Items.GhostlineBlackLanternRouteBeacon` | Quest-owned routing beacon installed at the freight yard. | Planned placeholder record consumed during stage 10; replace only if the final plant interaction supplies an equivalent device-owned item. |
| `Items.GhostlineBlackLanternRouteAuth` | Route-authentication token recovered from the yard restraint case. | Granted during stage 8; may remain as a readable quest clue or be consumed by the beacon/dispatch sequence. |
| `Items.GhostlineExpeditedHandoff` | Readable Sato/Morita conversation. | Granted during stage 8 and opened in stage 9. |
| `Items.GhostlineBlackLanternCipher` | Pair 07-B reconstruction key and courier index. | Granted during stage 30; delivered if preserved, removed at the core if burned. |
| `Items.GhostlineBlackLanternReceipt` | Signed proof of index destruction. | Granted only by the burned operation; delivered in stage 35. |

The clinic intake, Mara ticket, reconstruction report, and courier ledger are
authored as Journal onscreen entries rather than inventory items. The generated
journal also contains Iris's reconstruction report and all quest phone threads.

## Mara

`characters/mara.character.json` is Mara's validated female-average character
manifest. The visual target is recorded in
`quests/story/ghostline/gq003/images/gq003-mara-character-concept.png`: a tired,
capable apartment-systems technician with dark asymmetrical hair, restrained
temple cyberware, and practical charcoal workwear rather than combat armor.
Treat the image as the tonal/silhouette reference rather than a literal hair
sheet.

The revised game-asset pass uses the tutorial's complete merlot asymmetrical
hair bundle, a dirt-worn gray syn-cotton T-shirt beneath the `leather`
appearance of the Blurry Road collar jacket, `military_dirty` rubber-lined
cargo pants, and gray STAR TRAIL work boots. The shirt and jacket occupy
separate inner- and outer-torso components. The
indexed clothing was checked against the local item database instead of being
chosen from mesh names alone. The Character Forge validates and generates this
combination, but its inherited cuff/shadow companions remain provisional and
need an in-game clipping/material review before the resources are promoted.

## Vehicles

`Vehicle.GhostlineBlackLanternPatchVan` is a quest-owned provisional Columbus
panel-van record. The stable ID lets the cleanup stage target only Patch's
temporary vehicle. Pair 07-B remains a world-community vehicle entry because
its exact refrigerated truck entity and appearance should be chosen with the
interchange and relay routes.
