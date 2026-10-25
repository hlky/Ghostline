# Love, Actually.exe sprint retrospective

Date: 2026-10-25. Completed quest commit: `30eb17e`. Final playtested package:
`love-actually-736fbdd18ed4`.

The quest met its creative and length goals. The user reported a successful
complete playthrough of approximately ten minutes, including driving. The main
process improvement is to prove a small playable route from acceptance through
reward and completion before investing in full character and audio production.

## Evidence and scope

This retrospective follows the complete session export, reviewed in five
chronological stages with technical details revisited for the main failures.
The export does not establish development hours or time saved by any proposal.
The original export is a workstation attachment; the maintained evidence in
the repository is linked below rather than relying on that temporary path.

- [Repair history](implementation/PLAYTEST-REPAIRS.md)
- [Playtest route and final feedback](implementation/PLAYTEST.md)
- [Final state](implementation/state.json) and [install receipt](implementation/install-receipt.json)
- [Complete dialogue flow](implementation/DIALOGUE-FLOW.md)
- [Reviewed voice workflow](voice/README.md)
- [Socket inspection evidence](implementation/world/socket-mount-evidence.json)

The final confirmation is a successful user playthrough. It does not establish
exhaustive coverage of every save/load state, both player voices, or every
stealth and combat branch.

## What worked

- The premise stayed focused: meet Velvet, recover her code, correct the
  distribution, return for the personal explanation and reward. Hearts, bows,
  and Velvet Crash gave the quest a recognizable identity.
- Visual review separated Velvet from Goth Baddie through a new face and
  blonde twin buns. Auditions established the voice direction, and ten later
  revised takes clarified instructions without replacing the whole cast.
- Seven capture stops supplied sixteen validated world targets. Grouping,
  resume support, height adjustment, and local import made location selection
  practical without manually transcribing coordinates.
- Reviewed source WAVs, selection hashes, lipsync verification, native
  readback, package extraction, and installed hashes made builds traceable.
- Precise user reports and screenshots narrowed failures. Runtime link
  traces, NPC template audits, and wall collision data produced decisive fixes.
- Scoped fixes preserved working content: the final icon correction retained
  the working HUD glyph, and the second socket adjustment retained the first.

## Problems and lessons

| Area | Observed problem | Change for subsequent quests |
| --- | --- | --- |
| Voice environment | Existing artifacts, environment setup, native libraries, and the compatible checkout were found after repeated user redirection. A rebuilt runtime rejected older checkpoint storage. | Inventory and preserve a compatible tool/artifact set, then run one short synthesis before rebuilding or generating a full batch. |
| Character baseline | Goth Baddie's face and donor details carried into Velvet; preview defects hid intended hair color and chunk masks. Missing embedded body texture dependencies appeared in game. | Start from a reviewed neutral baseline; audit donor details, embedded dependencies, and preview/runtime parity. |
| Runtime architecture | REDscript and Audioware were initially introduced for behavior subsequently implemented with native resources. | Inspect working native precedents before introducing a runtime dependency. Record the specific unsupported requirement when a fallback is justified. |
| Playability milestone | Considerable appearance, audio, lipsync, and placement work preceded the first complete playable package. | Prove acceptance, interaction, return, reward, and completion with provisional presentation early. |
| Progression | Fast travel inside setup, leaving during speech, quick defer/return, and immediate actor cleanup exposed timing assumptions. | Design state checks, re-entry, interruption, readiness, and cleanup together. |
| Narrative | Dialogue reacted to unread files, technical wording obscured intent, and messages arrived at awkward moments. | Review a complete flow with player knowledge and delivery prerequisites before bulk VO; sequence shard grants and comments. |
| Reward and ending | The reward record failed to load, yet the grant fact advanced. Completion depended on a closing text. | Confirm inventory delivery before marking the reward granted; complete independently of optional epilogue messaging. |
| Presentation | Estimated socket offsets and icon sizes required repeated correction. The item description did not replace the inherited ability tooltip. | Measure the actual vanilla resource and inspect each display context. |
| Diagnostics and documentation | The optional link trace remained enabled until the user asked; the quest README retained superseded candidate status. | Include helper shutdown and current status/receipt reconciliation in final acceptance. |

The body defect had already occurred with Goth Baddie, and the socket axis
convention was documented. These were missed transfers of existing knowledge.
The agent should have applied them before asking for another playtest.

## Testing and diagnosis

Conversion, readback, and hash checks proved important integrity properties.
They did not prove that the interaction started, speech played, the HUD showed
success, the item arrived, or the quest ended. Test counts should be reported
with their scope, alongside separate in-game evidence.

Review complete transitions such as prompt -> personal link -> progress ->
success -> disconnect -> next objective. GQ004 exposed defects between those
steps even when the authored nodes passed checks.

Some early diagnoses needed correction. The compiled field scenes already
contained Velvet's voice tag; the missing opening line was resolved with actor
readiness. The leave gate was unchanged across the regressing builds while
the preceding upload handoff changed. Future reports should distinguish
observations, hypotheses, and confirmed causes, and compare the last working
build before attributing a regression.

## Workflow to retain

1. Resolve tools, game paths, artifacts, and environment; smoke-test the voice
   recipe before replacing a compatible tool or starting a full batch.
2. Review objectives, all dialogue branches, shards, reward, and ending as one
   player-facing flow, including what the player knows at each beat.
3. Build a small complete playable route with provisional presentation.
4. Exercise fast travel, deferral, interrupted transfer, early departure,
   guard deaths, and appropriate save/load checkpoints.
5. Finish character, voice, lipsync, FX, and UI production on that working route.
6. Run final acceptance against a named package and starting save, disable
   temporary diagnostics, and reconcile current documentation with the result.

## Follow-up ownership

The adopted production process lives in
[Quest production](../../../../docs/workflows/quest-production.md). Reusable
construction rules belong to the linked authoring guides and repo-local skills.
The dated history remains here.

| Follow-up | Owner and status |
| --- | --- |
| Earlier complete playable route, dialogue review, evidence levels | Adopted in the quest production workflow. |
| Trigger, actor, transfer, reward, and cleanup lessons | Adopted in the scene, item, world, runtime-test, and packaging guidance. |
| Preserve working voice artifacts locally | Six compiled model artifact bundles in a project-local ignored cache with a tracked hash inventory; existing checkpoints and native libraries remain in place. See the voice environment workflow. |
| Generic native meeting/transfer/completion template | Proposed tooling work; GQ004 is a playtested reference implementation, not a newly extracted generic template. |
| Automatically generated dialogue walkthrough | Proposed tooling work; the current GQ004 walkthrough is maintained manually. |
| Automated checks of final localization, embedded textures, and resolved item records | Proposed extensions to existing validators; documentation checks do not constitute implemented automation. |
