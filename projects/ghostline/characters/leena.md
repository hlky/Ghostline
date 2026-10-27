# Leena Shah — office manager, first draft

Quest: [Five-Star Service](../quests/gq005/README.md).
Authoring identity: `leena`. Runtime record: `Character.GhostlineLeena`.

Leena dispatches Deliverance contracts from the AKPP shop. Early forties, former
courier, two years behind the desk after six on routes. She keeps spare delivery
slips, knows which buildings never answer and eats lunch without leaving her
chair. Her managerial authority amounts to assigning work and absorbing blame.

She knowingly sells V a bonus she expects Deliverance to withhold. She needs
the route covered and admits it when confronted. She is neither a secretly
blameless friend nor a corporate villain. Her strongest action is letting V use
her settlement account despite the audit trail. She also has six weeks of her
own courier bonuses held, giving solidarity a concrete personal motive.

## Voice and performance

Plain, dry, economical. Initially talks while finishing paperwork; gives V full
attention when confronted about the bonus. Let pauses carry her recognition of
the route's absurdity. She does not deliver a joke after every line or treat V's
anger as funny. No ethnic accent prescribed by her name. Audition a grounded,
adult voice with tired warmth; avoid breathy glamour, cartoon hostility or an
omniscient exposition voice. No performance has been selected or generated.

## Appearance direction and actual candidate

Short merlot sidecut, practical black high-collar shirt, black work trousers
and boots. No combat harness, braindance visor, elaborate hair, donor face tattoo
or corporate luxury suit. Worn cuffs, an AKPP lanyard and a cheap wrist terminal
are optional later custom details, not assets already present.

The [manifest](leena.character.json) uses the complete Judy variation 02 merlot
hair bundle, including its animation and shadow companions, with no outer garment,
no business accessories and no face-tattoo layer. Indexed shirt/trouser meshes
are explicit female-frame paths; retained boot is the provisional curated donor.
Initial head values: eyes 9, nose 13, mouth 8, jaw 11, ears 4. These are proposed
sculpt inputs, not an already rebuilt or visually approved face. Age, tired eyes
and wear must be judged visually, not inferred from shape indices.

Entity, appearance, localization and tweak source generation passes in isolation
with no opaque numeric resource references. The
candidate uses the neutral female root rather than the installed male worker.
Generated source is under `projects/ghostline/generated/gq005/leena-candidate`;
it is not applied to shipping source, serialized as a complete character, or
installed. The office still has the generic worker.

## Review before replacing the worker

- Build the selected head geometry; render front, profile and seated silhouette.
- Inspect inherited skin/makeup/eye/cyberware layers and remove unintended donor
  identity in both component copies. “No face tattoo” is not proof of no makeup.
- Validate indexed appearances against the installed asset index; inspect shirt
  cuffs, trouser/boot joins, shadows and template texture dependencies.
- Check sitting posture at the existing desk, then talking and returning to idle.
- Verify civilian attitude and the AKPP Logistics faction display in game.
  Her affiliation is `Factions.AKPPLogistics`, based on the neutral unaffiliated
  faction; she is not a member of the Ghostline collective.
- Confirm no duplicated NPC, valid scene acquisition and persistence after load.

Name, appearance and backstory are proposed creative choices and can be revised
without changing the stable authoring identity or quest logic.
