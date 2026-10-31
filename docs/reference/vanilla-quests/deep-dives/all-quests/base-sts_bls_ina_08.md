# Gig: Trevor's Last Ride

Journal: `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08` · `StreetStory` · hash `3071127012`.

Journal premise: Gig type: SOS: Merc Needed\nObjective: Find Trevor's remains and deliver them to his family\nLocation: Highway 101\nDetails:\n\nThere's a popular saying among the Aldecaldos: "she who lives in the hearts of her loved ones can never truly die." Trevor Brass might indeed live on in memory, but if he had just keep his butt planted instead of dealing with Wraiths he'd still be just plain alive.\nI digress. Yesterday, man of mine spotted Trevor's car at a Wraiths' nest. The car had more holes than it started with and the Wraiths aren't known for taking prisoners.\nTrevor's relatives, as I mentioned, belong to the Aldecaldos. They aren't out for revenge. They just want to bury their son.\n\nFind Trevor's remains and help his family find peace.

**Coverage: journal-linked.** 59 exact journal-linked nodes in 5 resources; 7 resources in the inspected dependency context.

Resource roles in that context: 5 content candidate, 2 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: `base\open_world\district_definitions\open_world_kabuki.quest`; `base\open_world\open_world_test.quest`; `base\open_world\police_system\police_system_test.quest`. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Retrieve Trevor's body. (Primary) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/01_get_trevors_body_back` |
| Go to the Wraiths' territory. (Primary) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/02_get_to_the_camp` |
| Find Trevor's body. (Primary) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/03_find_body` |
| Scan the bodies to find Trevor. (Primary) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/04_scan_bodies_to_find_trevor` |
| Wait for the pickup. (Primary) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/05a_wait_for_pickup` |
| Place Trevor's body in the trunk. (Primary) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/06_put_body_in_trunk` |
| Retrieve the body from the Wraith outpost. (Primary) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/take_the_body_from_the_location` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `sts_bls_ina_08_bugfixing.questphase / h295 / 12` (Condition) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/04_scan_bodies_to_find_trevor` | 3:Out → 12:In; 12:True → 4:In; 12:False → 13:In |
| `sts_bls_ina_08_bugfixing.questphase / h295 / 13` (Condition) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/03_find_body` | 13:True → 4:In; 12:False → 13:In; 13:False → 14:In |
| `sts_bls_ina_08_bugfixing.questphase / h295 / 14` (Condition) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/02_get_to_the_camp` | 14:True → 4:In; 13:False → 14:In; 14:False → 15:In |
| `sts_bls_ina_08_bugfixing.questphase / h295 / 15` (Condition) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/02_get_to_the_camp` | 15:True → 4:In; 14:False → 15:In |
| `sts_bls_ina_08_openworld.questphase / h7 / 250` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/02_get_to_the_camp` | 250:Out → 124:In; 242:True → 250:Active |
| `sts_bls_ina_08_openworld.questphase / h7 / 251` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/02_get_to_the_camp` | 251:Out → 124:In; 242:False → 251:Active |
| `sts_bls_ina_08_openworld.questphase / h7 / 252` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/02_get_to_the_camp` | 124:Out → 252:Succeeded; 252:Out → 253:Active |
| `sts_bls_ina_08_openworld.questphase / h7 / 253` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/03_find_body` | 252:Out → 253:Active; 253:Out → 254:In |
| `sts_bls_ina_08_openworld.questphase / h7 / 255` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/03_find_body` | 254:Out → 255:Succeeded; 255:Out → 256:Active |
| `sts_bls_ina_08_openworld.questphase / h7 / 256` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/04_scan_bodies_to_find_trevor` | 255:Out → 256:Active; 256:Out → 259:In; 256:Out → 325:In |
| `sts_bls_ina_08_openworld.questphase / h7 / 258` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/04_scan_bodies_to_find_trevor` | 259:Out → 258:Succeeded; 258:Out → 292:Active |
| `sts_bls_ina_08_openworld.questphase / h7 / 264` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08` | 289:Out → 264:Succeeded; 264:Out → 322:In |
| `sts_bls_ina_08_openworld.questphase / h7 / 287` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/06_put_body_in_trunk` | 318:Out → 287:Active; 287:Out → 288:In |
| `sts_bls_ina_08_openworld.questphase / h7 / 289` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/06_put_body_in_trunk` | 289:Out → 264:Succeeded; 288:Out → 289:Succeeded; 289:Out → 313:In |
| `sts_bls_ina_08_openworld.questphase / h7 / 292` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/take_the_body_from_the_location` | 258:Out → 292:Active; 327:Out → 292:Active; 292:Out → 295:In; 292:Out → 323:In2; 292:Out → 347:In; 292:Out → 349:In; 292:Out → 351:In |
| `sts_bls_ina_08_openworld.questphase / h7 / 293` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/take_the_body_from_the_location` | 349:Out → 293:Succeeded; 293:Out → 318:In |
| `sts_bls_ina_08_openworld.questphase / h7 / 320` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/ina_08_briefing` | 247:Out → 320:Active |
| `sts_bls_ina_08_openworld.questphase / h7 / 327` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/04_scan_bodies_to_find_trevor` | 327:Out → 292:Active; 325:Out → 327:Inactive |
| `sts_bls_ina_08_openworld.questphase / h7 / 356` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08` | 353:Out → 356:Failed; 356:Out → 358:Active |
| `sts_bls_ina_08_openworld.questphase / h317 / 14` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/01_get_trevors_body_back` | 18:Out → 14:Active; 14:Out → 45:In |
| `sts_bls_ina_08_openworld.questphase / h317 / 16` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/01_get_trevors_body_back` | 45:Out → 16:Succeeded; 16:Out → 36:Active |
| `sts_bls_ina_08_openworld.questphase / h317 / 18` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/06_put_body_in_trunk` | 18:Out → 14:Active; 19:True → 18:Inactive |
| `sts_bls_ina_08_openworld.questphase / h317 / 19` (Condition) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/06_put_body_in_trunk` | 19:True → 18:Inactive; 41:Out → 19:In; 19:False → 49:Inactive |
| `sts_bls_ina_08_openworld.questphase / h317 / 36` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/06_put_body_in_trunk` | 36:Out → 12:In; 16:Out → 36:Active |
| `sts_bls_ina_08_openworld.questphase / h317 / 43` (PauseCondition) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/06_put_body_in_trunk` | 11:Out → 43:In; 43:Out → 44:In |
| `sts_bls_ina_08_openworld.questphase / h317 / 49` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/take_the_body_from_the_location` | 19:False → 49:Inactive; 49:Out → 50:Active |
| `sts_bls_ina_08_openworld.questphase / h317 / 50` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/01_get_trevors_body_back` | 49:Out → 50:Active; 50:Out → 51:In |
| `sts_bls_ina_08_openworld.questphase / h317 / 52` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/01_get_trevors_body_back` | 51:Out → 52:Succeeded; 52:Out → 53:Active |
| `sts_bls_ina_08_openworld.questphase / h317 / 53` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/take_the_body_from_the_location` | 53:Out → 12:In; 52:Out → 53:Active |
| `sts_bls_ina_08_openworld.questphase / h572 / 263` (PauseCondition) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/take_the_body_from_the_location` | 0:Out → 263:In; 263:Out → 212:In |
| `sts_bls_inland_avenue.questphase / h413 / 250` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/02_get_to_the_camp` | 250:Out → 124:In; 242:True → 250:Active |
| `sts_bls_inland_avenue.questphase / h413 / 251` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/02_get_to_the_camp` | 251:Out → 124:In; 242:False → 251:Active |
| `sts_bls_inland_avenue.questphase / h413 / 252` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/02_get_to_the_camp` | 124:Out → 252:Succeeded; 252:Out → 253:Active |
| `sts_bls_inland_avenue.questphase / h413 / 253` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/03_find_body` | 252:Out → 253:Active; 253:Out → 254:In |
| `sts_bls_inland_avenue.questphase / h413 / 255` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/03_find_body` | 254:Out → 255:Succeeded; 255:Out → 256:Active |
| `sts_bls_inland_avenue.questphase / h413 / 256` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/04_scan_bodies_to_find_trevor` | 255:Out → 256:Active; 256:Out → 259:In; 256:Out → 325:In |
| `sts_bls_inland_avenue.questphase / h413 / 258` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/04_scan_bodies_to_find_trevor` | 259:Out → 258:Succeeded; 258:Out → 292:Active |
| `sts_bls_inland_avenue.questphase / h413 / 264` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08` | 289:Out → 264:Succeeded; 264:Out → 322:In |
| `sts_bls_inland_avenue.questphase / h413 / 287` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/06_put_body_in_trunk` | 318:Out → 287:Active; 287:Out → 288:In |
| `sts_bls_inland_avenue.questphase / h413 / 289` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/06_put_body_in_trunk` | 289:Out → 264:Succeeded; 288:Out → 289:Succeeded; 289:Out → 313:In |
| `sts_bls_inland_avenue.questphase / h413 / 292` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/take_the_body_from_the_location` | 258:Out → 292:Active; 327:Out → 292:Active; 292:Out → 295:In; 292:Out → 323:In2; 292:Out → 347:In; 292:Out → 349:In; 292:Out → 351:In |
| `sts_bls_inland_avenue.questphase / h413 / 293` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/take_the_body_from_the_location` | 349:Out → 293:Succeeded; 293:Out → 318:In |
| `sts_bls_inland_avenue.questphase / h413 / 320` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/ina_08_briefing` | 247:Out → 320:Active |
| `sts_bls_inland_avenue.questphase / h413 / 327` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/04_scan_bodies_to_find_trevor` | 327:Out → 292:Active; 325:Out → 327:Inactive |
| `sts_bls_inland_avenue.questphase / h413 / 356` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08` | 353:Out → 356:Failed; 356:Out → 358:Active |
| `sts_bls_inland_avenue.questphase / h723 / 14` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/01_get_trevors_body_back` | 18:Out → 14:Active; 14:Out → 45:In |
| `sts_bls_inland_avenue.questphase / h723 / 16` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/01_get_trevors_body_back` | 45:Out → 16:Succeeded; 16:Out → 36:Active |
| `sts_bls_inland_avenue.questphase / h723 / 18` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/06_put_body_in_trunk` | 18:Out → 14:Active; 19:True → 18:Inactive |
| `sts_bls_inland_avenue.questphase / h723 / 19` (Condition) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/06_put_body_in_trunk` | 19:True → 18:Inactive; 41:Out → 19:In; 19:False → 49:Inactive |
| `sts_bls_inland_avenue.questphase / h723 / 36` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/06_put_body_in_trunk` | 36:Out → 12:In; 16:Out → 36:Active |
| `sts_bls_inland_avenue.questphase / h723 / 43` (PauseCondition) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/06_put_body_in_trunk` | 11:Out → 43:In; 43:Out → 44:In |
| `sts_bls_inland_avenue.questphase / h723 / 49` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/take_the_body_from_the_location` | 19:False → 49:Inactive; 49:Out → 50:Active |
| `sts_bls_inland_avenue.questphase / h723 / 50` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/01_get_trevors_body_back` | 49:Out → 50:Active; 50:Out → 51:In |
| `sts_bls_inland_avenue.questphase / h723 / 52` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/01_get_trevors_body_back` | 51:Out → 52:Succeeded; 52:Out → 53:Active |
| `sts_bls_inland_avenue.questphase / h723 / 53` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/take_the_body_from_the_location` | 53:Out → 12:In; 52:Out → 53:Active |
| `sts_bls_inland_avenue.questphase / h978 / 263` (PauseCondition) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/take_the_body_from_the_location` | 0:Out → 263:In; 263:Out → 212:In |
| `sts_badlands.questphase / h11 / 7` (PauseCondition) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08` | 0:Out → 7:In; 7:Out → 12:In7 |
| `open_world_bugfixing.questphase / h1543 / 12` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08` | 11:True → 12:Succeeded; 13:True → 12:Failed |
| `open_world_bugfixing.questphase / h2679 / 12` (Journal) | `quests/street_stories/badlands/inland_avenue/sts_bls_ina_08` | 11:True → 12:Succeeded; 13:True → 12:Failed |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `sts_bls_ina_08_openworld.questphase / h7 / 321` | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\scenes\sts_bls_ina_08_holocall_prebrief.scene`; `#sts_sm_bls_ina_08_holocall_prebrief` | 321:End1 → 302:Active; 321:rejected_out → 302:Active; 344:True → 321:Start1; 321:Holocall INT → 346:In; 321:Holocall RET → 345:In |
| `sts_bls_ina_08_openworld.questphase / h717 / 23` | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\scenes\sts_bls_ina_08_holocall_debriefs.scene`; `#sts_sm_bls_ina_08_holocall_debriefs` | 23:End1 → 8:In; 40:False → 23:Start1; 23:rejected_out → 39:Active; 23:Holocall INT → 27:In; 23:Holocall RET → 26:In |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\open_world\bugfixing\sts\sts_ina_south_bugfixing.questphase` / h0 / 10 | `sts_bls_ina_08_bugfixing.questphase` | 16: DeletionMarker; 16:Out → 10:In1 |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\phases\sts_bls_ina_08_phase.questphase` / h0 / 3 | `sts_bls_ina_08_openworld.questphase` | 4: Input; 4:Out → 3:In1; 3:Out1 → 5:In |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_inland_avenue.questphase` / h4925 / 3 | `sts_bls_ina_08_openworld.questphase` | 4: Input; 4:Out → 3:In1; 3:Out1 → 5:In |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\phases\sts_bls_ina_08_openworld.questphase` / h717 / 23 | `sts_bls_ina_08_holocall_debriefs.scene` | 40: Condition; 23:End1 → 8:In; 40:False → 23:Start1; 23:rejected_out → 39:Active; 23:Holocall INT → 27:In; 23:Holocall RET → 26:In |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_inland_avenue.questphase` / h1123 / 23 | `sts_bls_ina_08_holocall_debriefs.scene` | 40: Condition; 23:End1 → 8:In; 40:False → 23:Start1; 23:rejected_out → 39:Active; 23:Holocall INT → 27:In; 23:Holocall RET → 26:In |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\phases\sts_bls_ina_08_openworld.questphase` / h7 / 321 | `sts_bls_ina_08_holocall_prebrief.scene` | 344: Condition; 321:End1 → 302:Active; 321:rejected_out → 302:Active; 344:True → 321:Start1; 321:Holocall INT → 346:In; 321:Holocall RET → 345:In |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_inland_avenue.questphase` / h413 / 321 | `sts_bls_ina_08_holocall_prebrief.scene` | 344: Condition; 321:End1 → 302:Active; 321:rejected_out → 302:Active; 344:True → 321:Start1; 321:Holocall INT → 346:In; 321:Holocall RET → 345:In |
| `base\open_world\street_stories\badlands\sts_badlands.questphase` / h0 / 2 | `sts_bls_inland_avenue.questphase` | 0: Input; 0:Out → 2:In1 |
| `base\open_world\street_stories\street_stories.questphase` / h0 / 2 | `sts_badlands.questphase` | 0: Input; 0:Out → 2:In1 |
| `base\quest\bugfixing.questphase` / h0 / 11 | `open_world_bugfixing.questphase` | 16: DeletionMarker; 16:Out → 11:In1 |
| `base\quest\bugfixing\open_world_bugfixing.questphase` / h11 / 49 | `sts_ina_south_bugfixing.questphase` | 9: DeletionMarker; 9:Out → 49:In1 |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\sts_bls_ina_08.quest` / h0 / 23 | `sts_bls_ina_08_phase.questphase` | 28: FactsDBManager: ina_08_test_def; 23:Out1 → 1:In; 28:Out → 23:In1 |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_inland_avenue.questphase` / h0 / 12 | `sts_bls_ina_08_phase.questphase` | 42: Journal; 42:Out → 12:In1 |
| `base\open_world\community\heywood\wellsprings\hey_spr_quest.quest` / h0 / 4 | `street_stories.questphase` | 1: Start; 1:Out → 4:In1 |
| `base\open_world\community\westbrook\charter_hill\wbr_hil_com_test.quest` / h0 / 21 | `street_stories.questphase` | 0: Start; 0:Out → 21:In1 |
| `base\open_world\phases\open_world_content.questphase` / h0 / 2 | `street_stories.questphase` | 33: PauseCondition: sts_loop_start; 122: Input; 33:Out → 2:In1; 122:Out → 2:In1 |
| `base\quest\cyberpunk2077.questphase` / h520 / 4 | `bugfixing.questphase` | 9: LogicalHub; 21: FactsDBManager: ep1_standalone_bugfix_start; 4:Out_res_act1 → 14:In; 4:to_mq025 → 6:to_mq025; 4:sq026_02_signal → 5:sq026_02_signal; 9:Out1 → 4:In1; 21:Out → 4:In1; 4:CYB-656199 → 15:In; 4:ep1_active_out → 23:In |
| `base\quest\main_quests\epilogue\q201\q201_heir.quest` / h0 / 44 | `bugfixing.questphase` | 11: Start; 11:Out → 44:In1 |
| `base\quest\main_quests\part1\q101\q101.quest` / h0 / 47 | `bugfixing.questphase` | 0: Start; 0:Out → 47:In1 |
| `base\quest\main_quests\part1\q110\q110.quest` / h0 / 76 | `bugfixing.questphase` | 0: Start; 0:Out → 76:In1 |
| `base\quest\main_quests\part1\q112\q112_abduction.quest` / h0 / 23 | `bugfixing.questphase` | 0: Start; 0:Out → 23:In1 |
| `base\quest\main_quests\part1\q115\q115_afterlife.quest` / h0 / 140 | `bugfixing.questphase` | 0: Start; 0:Out → 140:In1 |
| `base\quest\minor_quests\mq026\mq026.quest` / h0 / 5 | `bugfixing.questphase` | 1: Phase: mq026_00_chickentest.questphase; 1: Phase: mq026_00_chickentest.questphase; 1: Phase: mq026_00_chickentest.questphase; 1: Phase: mq026_00_chickentest.questphase; 1:Out1 → 5:In1; 1:conspiracy_out → 5:In1; 1:combat_out → 5:In1; 1:death_out → 5:In1 |
| `base\quest\side_quests\sq021\sq021.quest` / h0 / 61 | `bugfixing.questphase` | 0: Start; 0:Out → 61:In1 |
| `base\quest\side_quests\sq023\sq023.quest` / h0 / 20 | `bugfixing.questphase` | 0: Start; 0:Out → 20:In1 |
| `base\quest\side_quests\sq025\sq025.quest` / h0 / 68 | `bugfixing.questphase` | 49: Phase; 49:additional_content_out → 68:In1 |
| `base\quest\side_quests\sq027\sq0027_queen_of_the_highway.quest` / h0 / 64 | `bugfixing.questphase` | 0: Start; 0:Out → 64:In1 |
| `ep1\quest\main_quests\q307\q307.quest` / h128 / 13 | `bugfixing.questphase` | 11: LogicalHub; 11:Out1 → 13:In1 |
| `base\open_world\district_definitions\open_world_kabuki.quest` / h0 / 2 | `open_world_content.questphase` | 4: PauseCondition: {"seconds": 1}; 4:Out → 2:In1 |
| `base\open_world\metro\ue_metro\ue_metro.quest` / h0 / 21 | `open_world_content.questphase` | 0: Start; 0:Out → 21:EP1_Standalone |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07.quest` / h0 / 7 | `open_world_content.questphase` | 8: Scene: ma_bls_ina_07_chicken.scene; 8:start → 7:In1 |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06.quest` / h0 / 3 | `open_world_content.questphase` | 2: FactsDBManager: sts_std_arr_tier_1; 2:Out → 3:In1 |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_quest.quest` / h0 / 4 | `open_world_content.questphase` | 3: FactsDBManager: sts_wat_kab_tier_1; 3:Out → 4:In1 |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_22\ma_wat_nid_22.quest` / h0 / 3 | `open_world_content.questphase` | 2: FactsDBManager: sts_wat_nid_tier_1; 2:Out → 3:In1 |
| `base\open_world\open_world_test.quest` / h0 / 2 | `open_world_content.questphase` | 4: PauseCondition: {"seconds": 1}; 4:Out → 2:In1 |
| `base\open_world\police_system\police_system_test.quest` / h0 / 2 | `open_world_content.questphase` | 4: PauseCondition: {"seconds": 1}; 4:Out → 2:In1 |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.quest` / h0 / 4 | `open_world_content.questphase` | 0: Start; 0:Out → 4:In1 |
| `base\quest\additional_game_elements.questphase` / h0 / 19 | `open_world_content.questphase` | 0: Input; 36: Input; 0:Out → 19:In1; 36:Out → 19:EP1_Standalone |
| `base\quest\cyberpunk2077.quest` / h0 / 2 | `cyberpunk2077.questphase` | 0: Start; 0:Out → 2:Start |
| `base\quest\demos\handson_2020\handson_2020.quest` / h0 / 33 | `cyberpunk2077.questphase` | 34: FactsDBManager: e3_2020; 34:Out → 33:Start |
| `base\quest\demos\handson_2020\handson_2020_testing.quest` / h0 / 5 | `cyberpunk2077.questphase` | 6: FactsDBManager: e3_2020; 6:Out → 5:Testing |
| `ep1\quest\cyberpunk2077_ep1_standalone.quest` / h0 / 1 | `cyberpunk2077.questphase` | 2: Start; 2:Out → 1:EP1_Standalone |
| `base\open_world\mini_world_stories\watson\mws_wat_08\mws_wat_08.quest` / h0 / 10 | `additional_game_elements.questphase` | 1: Start; 1:Out → 10:Input |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08.quest` / h0 / 4 | `additional_game_elements.questphase` | 5: FactsDBManager: sts_bls_ina_tier_1; 5:Out → 4:Input |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22.quest` / h0 / 6 | `additional_game_elements.questphase` | 4: FactsDBManager: sts_bls_ina_tier_1; 4:Out → 6:Input |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03.quest` / h0 / 5 | `additional_game_elements.questphase` | 4: FactsDBManager: sts_cct_dtn_tier_1; 4:Out → 5:Input |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07.quest` / h0 / 2 | `additional_game_elements.questphase` | 3: FactsDBManager: sts_cct_dtn_tier_1; 3:Out → 2:Input |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04.quest` / h0 / 6 | `additional_game_elements.questphase` | 4: Scene: ma_hey_spr_04_00_chickentest.scene; 4:End 0 → 6:Input |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06.quest` / h0 / 4 | `additional_game_elements.questphase` | 5: FactsDBManager: sts_hey_spr_tier_1; 5:Out → 4:Input |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\ma_pac_cvi_08.quest` / h0 / 4 | `additional_game_elements.questphase` | 3: Scene: ma_pac_cvi_08_00_chickentest.scene; 3:End 0 → 4:Input |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15.quest` / h0 / 2 | `additional_game_elements.questphase` | 3: FactsDBManager: sts_pac_cvi_tier_1; 3:Out → 2:Input |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\ma_std_rcr_11.quest` / h0 / 3 | `additional_game_elements.questphase` | 2: Scene: mq_std_rcr_11_00_chickentest.scene; 2:End 0 → 3:Input |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_quest.quest` / h0 / 6 | `additional_game_elements.questphase` | 1: Start; 1:Out → 6:Input |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_quest.quest` / h0 / 7 | `additional_game_elements.questphase` | 3: FactsDBManager: sts_wat_kab_tier_1; 3:Out → 7:Input |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\ma_wat_lch_06.quest` / h0 / 2 | `additional_game_elements.questphase` | 3: Scene: ma_wat_lch_06_chicken_test.scene; 3:End 0 → 2:Input |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_03\ma_wat_nid_03.quest` / h0 / 8 | `additional_game_elements.questphase` | 9: FactsDBManager: ow_psychos_intro_done; 9:Out → 8:Input |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\ma_wat_nid_15.quest` / h0 / 6 | `additional_game_elements.questphase` | 8: LogicalHub; 8:Out1 → 6:Input |
| `base\quest\cyberpunk2077.questphase` / h520 / 3 | `additional_game_elements.questphase` | 9: LogicalHub; 21: FactsDBManager: ep1_standalone_bugfix_start; 9:Out1 → 3:Input; 21:Out → 3:EP1_Standalone |
| `base\quest\demos\handson_2020\handson_2020_scavengers.quest` / h0 / 20 | `additional_game_elements.questphase` | 25: LogicalHub; 25:Out1 → 20:Input |
| `base\quest\main_quests\epilogue\q201\q201_heir.quest` / h0 / 29 | `additional_game_elements.questphase` | 11: Start; 11:Out → 29:Input |
| `base\quest\main_quests\epilogue\q202\q202.quest` / h0 / 22 | `additional_game_elements.questphase` | 0: Start; 0:Out → 22:Input |
| `base\quest\main_quests\epilogue\q203\q203_legend.quest` / h0 / 30 | `additional_game_elements.questphase` | 27: FactsDBManager: q204_var_test_def; 27:Out → 30:Input |
| `base\quest\main_quests\epilogue\q204\q204_reborn.quest` / h0 / 6 | `additional_game_elements.questphase` | 0: Start; 0:Out → 6:Input |
| `base\quest\main_quests\part1\q101\q101.quest` / h0 / 30 | `additional_game_elements.questphase` | 0: Start; 0:Out → 30:Input |
| `base\quest\main_quests\part1\q103\q103.quest` / h0 / 45 | `additional_game_elements.questphase` | 0: Start; 0:Out → 45:Input |
| `base\quest\main_quests\part1\q105\q105_main.quest` / h0 / 40 | `additional_game_elements.questphase` | 58: LogicalHub; 58:Out1 → 40:Input |
| `base\quest\main_quests\part1\q110\q110.quest` / h0 / 17 | `additional_game_elements.questphase` | 0: Start; 0:Out → 17:Input |
| `base\quest\main_quests\part1\q112\q112_abduction.quest` / h0 / 9 | `additional_game_elements.questphase` | 0: Start; 0:Out → 9:Input |
| `base\quest\main_quests\part1\q113\q113.quest` / h0 / 40 | `additional_game_elements.questphase` | 36: FactsDBManager: q113_active; 36:Out → 40:Input |
| `base\quest\main_quests\part1\q114\q114_nomads.quest` / h0 / 16 | `additional_game_elements.questphase` | 0: Start; 0:Out → 16:Input |
| `base\quest\main_quests\part1\q115\q115_afterlife.quest` / h0 / 57 | `additional_game_elements.questphase` | 0: Start; 0:Out → 57:Input |
| `base\quest\main_quests\prologue\q000\q000.quest` / h0 / 10 | `additional_game_elements.questphase` | 2: Start; 2:Out → 10:Input |
| `base\quest\main_quests\prologue\q001\q001.quest` / h0 / 30 | `additional_game_elements.questphase` | 120: LogicalHub; 120:Out1 → 30:Input |
| `base\quest\main_quests\prologue\q003\q003.quest` / h0 / 26 | `additional_game_elements.questphase` | 0: Start; 0:Out → 26:Input |
| `base\quest\main_quests\prologue\q004\q004.quest` / h0 / 1087 | `additional_game_elements.questphase` | 24: Start; 24:Out → 1087:Input |
| `base\quest\main_quests\prologue\q005\q005_heist.quest` / h0 / 14 | `additional_game_elements.questphase` | 17: FactsDBManager: jackie_default_on write/default comparison 0; 17:Out → 14:Input |
| `base\quest\minor_quests\mq000\mq000.quest` / h0 / 12 | `additional_game_elements.questphase` | 3: Scene: mq000_00_chickentest.scene; 3:out → 12:Input |
| `base\quest\minor_quests\mq001\mq001.quest` / h0 / 10 | `additional_game_elements.questphase` | 21: Start; 21:Out → 10:Input |
| `base\quest\minor_quests\mq003\mq003_orbitals.quest` / h0 / 7 | `additional_game_elements.questphase` | 2: Start; 2:Out → 7:Input |
| `base\quest\minor_quests\mq006\mq006.quest` / h0 / 7 | `additional_game_elements.questphase` | 6: Scene: mq006_chicken_test.scene; 6:End 0 → 7:Input |
| `base\quest\minor_quests\mq007\mq007.quest` / h0 / 10 | `additional_game_elements.questphase` | 0: Start; 0:Out → 10:Input |
| `base\quest\minor_quests\mq008\mq008.quest` / h0 / 14 | `additional_game_elements.questphase` | 0: Start; 0:Out → 14:Input |
| `base\quest\minor_quests\mq011\mq011.quest` / h0 / 8 | `additional_game_elements.questphase` | 1: Start; 1:Out → 8:Input |
| `base\quest\minor_quests\mq012\mq012.quest` / h0 / 9 | `additional_game_elements.questphase` | 1: Start; 1:Out → 9:Input |
| `base\quest\minor_quests\mq013\mq013.quest` / h0 / 4 | `additional_game_elements.questphase` | 1: Start; 1:Out → 4:Input |
| `base\quest\minor_quests\mq014\mq014.quest` / h0 / 5 | `additional_game_elements.questphase` | 0: Start; 0:Out → 5:Input |
| `base\quest\minor_quests\mq015\mq015_wizardbook.quest` / h0 / 7 | `additional_game_elements.questphase` | 0: Start; 0:Out → 7:Input |
| `base\quest\minor_quests\mq016\mq016_bartmoss.quest` / h0 / 9 | `additional_game_elements.questphase` | 0: Start; 0:Out → 9:Input |
| `base\quest\minor_quests\mq017\mq017_streetkid.quest` / h0 / 8 | `additional_game_elements.questphase` | 1: Start; 1:Out → 8:Input |
| `base\quest\minor_quests\mq018\mq018.quest` / h0 / 5 | `additional_game_elements.questphase` | 1: Phase: mq018_00_chickentest.questphase; 1:additional_content_out → 5:Input |
| `base\quest\minor_quests\mq019\mq019_paparazzi.quest` / h0 / 7 | `additional_game_elements.questphase` | 0: Start; 0:Out → 7:Input |
| `base\quest\minor_quests\mq021\mq021.quest` / h0 / 5 | `additional_game_elements.questphase` | 2: Start; 2:Out → 5:Input |
| `base\quest\minor_quests\mq022\mq022.quest` / h0 / 5 | `additional_game_elements.questphase` | 2: Start; 2:Out → 5:Input |
| `base\quest\minor_quests\mq023\mq023_bootleg.quest` / h0 / 11 | `additional_game_elements.questphase` | 1: Start; 1:Out → 11:Input |
| `base\quest\minor_quests\mq024\mq024.quest` / h0 / 15 | `additional_game_elements.questphase` | 0: Start; 0:Out → 15:Input |
| `base\quest\minor_quests\mq025\mq025_psycho_brawl.quest` / h0 / 4 | `additional_game_elements.questphase` | 10: FactsDBManager: disable_tutorials; 10:Out → 4:Input |
| `base\quest\minor_quests\mq026\mq026.quest` / h0 / 4 | `additional_game_elements.questphase` | 1: Phase: mq026_00_chickentest.questphase; 1:additional_content_out → 4:Input |
| `base\quest\minor_quests\mq028\mq028.quest` / h0 / 4 | `additional_game_elements.questphase` | 1: Phase: mq028_00_chickentest.questphase; 1:additional_content_out → 4:Input |
| `base\quest\minor_quests\mq030\mq030.quest` / h0 / 9 | `additional_game_elements.questphase` | 0: Start; 0:Out → 9:Input |
| `base\quest\minor_quests\mq032\mq032_sacrum.quest` / h0 / 12 | `additional_game_elements.questphase` | 0: Start; 0:Out → 12:Input |
| `base\quest\minor_quests\mq033\mq033_tarot.quest` / h0 / 2 | `additional_game_elements.questphase` | 0: Start; 0:Out → 2:Input |
| `base\quest\minor_quests\mq035\mq035_ozob.quest` / h0 / 5 | `additional_game_elements.questphase` | 4: Scene: mq035_chicken_test.scene; 4:start → 5:Input |
| `base\quest\minor_quests\mq037\mq037_brendan.quest` / h0 / 4 | `additional_game_elements.questphase` | 0: Start; 0:Out → 4:Input |
| `base\quest\minor_quests\mq038\mq038.quest` / h0 / 5 | `additional_game_elements.questphase` | 2: Start; 2:Out → 5:Input |
| `base\quest\minor_quests\mq040\mq040_biosculpt.quest` / h0 / 10 | `additional_game_elements.questphase` | 22: Condition: mq040_add_ele_on Equal 1; 22:True → 10:Input |
| `base\quest\minor_quests\mq041\mq041_corpo.quest` / h0 / 8 | `additional_game_elements.questphase` | 1: Start; 1:Out → 8:Input |
| `base\quest\minor_quests\mq048\mq048.quest` / h0 / 12 | `additional_game_elements.questphase` | 1: Start; 1:Out → 12:Input |
| `base\quest\minor_quests\mq055\mq055.quest` / h0 / 4 | `additional_game_elements.questphase` | 3: Scene: mq055_chicken.scene; 3:End 0 → 4:EP1_Standalone |
| `base\quest\side_quests\sq004\sq004_riders_quest.quest` / h0 / 9 | `additional_game_elements.questphase` | 0: Start; 0:Out → 9:Input |
| `base\quest\side_quests\sq006\sq006.quest` / h0 / 9 | `additional_game_elements.questphase` | 0: Start; 0:Out → 9:Input |
| `base\quest\side_quests\sq011\sq011.quest` / h0 / 9 | `additional_game_elements.questphase` | 0: Start; 0:Out → 9:Input |
| `base\quest\side_quests\sq012\sq012_the_law.quest` / h0 / 6 | `additional_game_elements.questphase` | 2: Start; 2:Out → 6:Input |
| `base\quest\side_quests\sq017\sq017.quest` / h0 / 5 | `additional_game_elements.questphase` | 0: Start; 0:Out → 5:Input |
| `base\quest\side_quests\sq018\sq018.quest` / h0 / 24 | `additional_game_elements.questphase` | 16: Start; 16:Out → 24:Input |
| `base\quest\side_quests\sq021\sq021.quest` / h0 / 17 | `additional_game_elements.questphase` | 0: Start; 0:Out → 17:Input |
| `base\quest\side_quests\sq023\sq023.quest` / h0 / 15 | `additional_game_elements.questphase` | 0: Start; 0:Out → 15:Input |
| `base\quest\side_quests\sq024\sq024.quest` / h0 / 29 | `additional_game_elements.questphase` | 0: Start; 0:Out → 29:Input |
| `base\quest\side_quests\sq025\sq025.quest` / h0 / 66 | `additional_game_elements.questphase` | 49: Phase; 49:additional_content_out → 66:Input |
| `base\quest\side_quests\sq026\sq026.quest` / h0 / 9 | `additional_game_elements.questphase` | 0: Start; 0:Out → 9:Input |
| `base\quest\side_quests\sq027\sq0027_queen_of_the_highway.quest` / h0 / 8 | `additional_game_elements.questphase` | 0: Start; 0:Out → 8:Input |
| `base\quest\side_quests\sq028\sq028.quest` / h0 / 4 | `additional_game_elements.questphase` | 0: Start; 0:Out → 4:Input |
| `base\quest\side_quests\sq029\sq029.quest` / h0 / 20 | `additional_game_elements.questphase` | 1: Start; 1:Out → 20:Input |
| `base\quest\side_quests\sq030\sq030.quest` / h0 / 11 | `additional_game_elements.questphase` | 4: SceneManager; 4:Out → 11:Input |
| `base\quest\side_quests\sq031\sq031.quest` / h0 / 6 | `additional_game_elements.questphase` | 0: Start; 0:Out → 6:Input |
| `base\quest\side_quests\sq032\sq032.quest` / h0 / 12 | `additional_game_elements.questphase` | 0: Start; 0:Out → 12:Input |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_03\mws_cz_03.quest` / h0 / 11 | `additional_game_elements.questphase` | 6: FactsDBManager: ep1_side_content; 6:Out → 11:Input |
| `ep1\quest\main_quests\q304\q304.quest` / h0 / 20 | `additional_game_elements.questphase` | 12: Checkpoint; 12:Out → 20:EP1_Standalone |
| `ep1\quest\main_quests\q305\q305.quest` / h0 / 5 | `additional_game_elements.questphase` | 1: Start; 1:Out → 5:Input |
| `ep1\quest\main_quests\q306\q306.quest` / h0 / 8 | `additional_game_elements.questphase` | 9: PauseCondition: q306_DEBUG_useBaseGameAdditionalGameElements; 9:Out → 8:Input |
| `ep1\quest\main_quests\q307\q307.quest` / h128 / 3 | `additional_game_elements.questphase` | 4: LogicalHub; 10: CutControl; 4:Out1 → 3:Input; 10:CutSource → 3:CutDestination |
| `ep1\quest\minor_quests\mq301\mq301.quest` / h0 / 7 | `additional_game_elements.questphase` | 1: Start; 1:Out → 7:Input |
| `ep1\quest\minor_quests\mq303\mq303.quest` / h95 / 2 | `additional_game_elements.questphase` | 0: Input; 0:Out → 2:Input |
| `ep1\quest\minor_quests\mq304\mq304.quest` / h130 / 3 | `additional_game_elements.questphase` | 4: LogicalHub; 4:Out1 → 3:Input |
| `ep1\quest\minor_quests\mq305\mq305.quest` / h0 / 4 | `additional_game_elements.questphase` | 1: Start; 1:Out → 4:Input |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `sts_bls_ina_08_holocall_debriefs.scene` | Start1 → End1, rejected_out | fixer; v; 23 nodes / 30 edges |
| `sts_bls_ina_08_holocall_prebrief.scene` | Start1 → End1, rejected_out | fixer; v; 22 nodes / 25 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| No choice option in resolved scene context | — | — | — |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `#ina_08_ready` | sts_bls_ina_08_openworld.questphase / h926 / 10 | No reader in selected context |
| `CYB-611159` | sts_bls_ina_08_bugfixing.questphase / h10 / 4 | sts_bls_ina_08_bugfixing.questphase / h10 / 3 |
| `CYB-632528` | sts_bls_ina_08_bugfixing.questphase / h71 / 3 | sts_bls_ina_08_bugfixing.questphase / h71 / 2 |
| `CYB-632528_additional_fix` | Producer outside selected context | sts_bls_ina_08_bugfixing.questphase / h71 / 19 |
| `CYB-640985` | sts_bls_ina_08_bugfixing.questphase / h173 / 3 | sts_bls_ina_08_bugfixing.questphase / h173 / 2 |
| `CYB-657732` | sts_bls_ina_08_bugfixing.questphase / h229 / 5 | sts_bls_ina_08_bugfixing.questphase / h229 / 4 |
| `CYB-672815` | sts_bls_ina_08_bugfixing.questphase / h295 / 3 | sts_bls_ina_08_bugfixing.questphase / h295 / 2 |
| `bls_achievement` | sts_bls_ina_08_openworld.questphase / h717 / 7 | No reader in selected context |
| `holo_active_call_interrupted` | Producer outside selected context | sts_bls_ina_08_holocall_prebrief.scene / scene / 283 |
| `holo_dakota_calls_v_end_activate` | sts_bls_ina_08_holocall_debriefs.scene / scene / 103; sts_bls_ina_08_holocall_prebrief.scene / scene / 103; sts_bls_ina_08_openworld.questphase / h7 / 346; sts_bls_ina_08_openworld.questphase / h717 / 27 | No reader in selected context |
| `holo_dakota_calls_v_end_done` | sts_bls_ina_08_holocall_debriefs.scene / scene / 99; sts_bls_ina_08_holocall_prebrief.scene / scene / 99 | sts_bls_ina_08_holocall_debriefs.scene / scene / 98; sts_bls_ina_08_holocall_prebrief.scene / scene / 98 |
| `holo_dakota_calls_v_rejectable` | sts_bls_ina_08_holocall_debriefs.scene / scene / 280; sts_bls_ina_08_holocall_prebrief.scene / scene / 254; sts_bls_ina_08_holocall_prebrief.scene / scene / 281 | No reader in selected context |
| `holo_dakota_calls_v_rejected` | sts_bls_ina_08_holocall_debriefs.scene / scene / 284; sts_bls_ina_08_holocall_prebrief.scene / scene / 258 | sts_bls_ina_08_holocall_debriefs.scene / scene / 282; sts_bls_ina_08_holocall_prebrief.scene / scene / 256 |
| `holo_dakota_calls_v_start_activate` | sts_bls_ina_08_bugfixing.questphase / h71 / 8; sts_bls_ina_08_holocall_debriefs.scene / scene / 102; sts_bls_ina_08_holocall_debriefs.scene / scene / 259; sts_bls_ina_08_holocall_prebrief.scene / scene / 102; sts_bls_ina_08_holocall_prebrief.scene / scene / 279; sts_bls_ina_08_openworld.questphase / h7 / 345; sts_bls_ina_08_openworld.questphase / h717 / 26 | sts_bls_ina_08_bugfixing.questphase / h71 / 6; sts_bls_ina_08_bugfixing.questphase / h71 / 9; sts_bls_ina_08_holocall_debriefs.scene / scene / 251 |
| `holo_dakota_calls_v_start_done` | sts_bls_ina_08_holocall_debriefs.scene / scene / 97; sts_bls_ina_08_holocall_prebrief.scene / scene / 97 | sts_bls_ina_08_holocall_debriefs.scene / scene / 270; sts_bls_ina_08_holocall_prebrief.scene / scene / 267 |
| `holo_delamain_deep_vehicle_talk` | sts_bls_ina_08_bugfixing.questphase / h71 / 16 | No reader in selected context |
| `holo_interrupt_call` | Producer outside selected context | sts_bls_ina_08_bugfixing.questphase / h71 / 6; sts_bls_ina_08_bugfixing.questphase / h71 / 9 |
| `holo_setup_active` | Producer outside selected context | sts_bls_ina_08_holocall_debriefs.scene / scene / 251; sts_bls_ina_08_holocall_prebrief.scene / scene / 283 |
| `holo_setup_started` | Producer outside selected context | sts_bls_ina_08_holocall_debriefs.scene / scene / 251; sts_bls_ina_08_holocall_prebrief.scene / scene / 283 |
| `ina_08_failed` | sts_bls_ina_08_openworld.questphase / h7 / 360 | open_world_bugfixing.questphase / h1543 / 13; open_world_bugfixing.questphase / h2679 / 13; sts_bls_ina_08_openworld.questphase / h717 / 28 |
| `ina_08_finished` | sts_bls_ina_08_openworld.questphase / h717 / 24 | open_world_bugfixing.questphase / h1543 / 11; open_world_bugfixing.questphase / h2679 / 11 |
| `ina_08_pickup_arrived` | sts_bls_ina_08_openworld.questphase / h572 / 209 | No reader in selected context |
| `ina_08_start` | sts_bls_ina_08_openworld.questphase / h7 / 300 | No reader in selected context |
| `ina_08_test_def` | Producer outside selected context | sts_bls_ina_08_openworld.questphase / h7 / 242; sts_bls_inland_avenue.questphase / h413 / 242 |
| `ina_08_trevor_in_pickup_area` | sts_bls_ina_08_openworld.questphase / h572 / 212; sts_bls_inland_avenue.questphase / h978 / 212 | No reader in selected context |
| `travelling_merchant_lives` | Producer outside selected context | sts_bls_ina_08_bugfixing.questphase / h0 / 19 |

## Exact gates, joins and cancellation

<details><summary>97 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `sts_bls_ina_08_bugfixing.questphase / h0 / 19` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant_lives","value":9999,"comparisonType":"GreaterOrEqual"}}}` | 20:Out → 19:In |
| `sts_bls_ina_08_bugfixing.questphase / h10 / 3` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-611159"}}}` | 0:Out → 3:In; 3:False → 4:In |
| `sts_bls_ina_08_bugfixing.questphase / h10 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ina_08_com_guide","names":["guide"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 7:Out → 5:In; 5:Out → 6:In |
| `sts_bls_ina_08_bugfixing.questphase / h10 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ina_08_tr_in_freezer"}}` | 4:Out → 7:In; 7:Out → 5:In |
| `sts_bls_ina_08_bugfixing.questphase / h71 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-632528"}}}` | 0:Out → 2:In; 2:False → 3:In |
| `sts_bls_ina_08_bugfixing.questphase / h71 / 6` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questSceneCondition","type":{"$type":"questSceneNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\badlands\\inland_avenue\\sts_bls_ina_08\\scenes\\sts_bls_ina_08_holocall_prebrief.scene","Flags":"Soft"}}},{"$type":"questSystemCondition","type":{"$type":"questPhone_ConditionType","caller":{"$type":"gameJournalPath","realPath":"contacts/dakota_smith","fileEntryIndex":1,"className":"gameJournalContact"},"addressee":{"$type":"gameJournalPath","realPath":"contacts/player","fileEntryIndex":1,"className":"gameJournalContact"},"callPhase":"EndCall"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_interrupt_call","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_dakota_calls_v_start_activate","value":1,"comparisonType":"Less"}}]}}` | 3:Out → 6:In; 6:True → 9:In; 6:True → 11:In |
| `sts_bls_ina_08_bugfixing.questphase / h71 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questSceneCondition","type":{"$type":"questSceneNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\badlands\\inland_avenue\\sts_bls_ina_08\\scenes\\sts_bls_ina_08_holocall_prebrief.scene","Flags":"Soft"},"type":"IsOutside"}},{"$type":"questSystemCondition","type":{"$type":"questPhone_ConditionType","caller":{"$type":"gameJournalPath","realPath":"contacts/dakota_smith","fileEntryIndex":1,"className":"gameJournalContact"},"addressee":{"$type":"gameJournalPath","realPath":"contacts/player","fileEntryIndex":1,"className":"gameJournalContact"}}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_interrupt_call"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_dakota_calls_v_start_activate"}}]}}` | 6:True → 9:In; 9:Out → 13:In |
| `sts_bls_ina_08_bugfixing.questphase / h71 / 11` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 6:True → 11:In; 11:Out → 8:In; 13:CutSource → 11:CutDestination |
| `sts_bls_ina_08_bugfixing.questphase / h71 / 13` | `questCutControlNodeDefinition` `{}` | 9:Out → 13:In; 13:CutSource → 11:CutDestination |
| `sts_bls_ina_08_bugfixing.questphase / h71 / 15` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#sq025_com_delamain_deep","names":["delamain_deep"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":80.0},"comparisonType":"Less"}}]}}` | 3:Out → 15:In; 15:False → 16:In |
| `sts_bls_ina_08_bugfixing.questphase / h71 / 19` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-632528_additional_fix"}}}` | 3:Out → 19:In |
| `sts_bls_ina_08_bugfixing.questphase / h173 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-640985"}}}` | 0:Out → 2:In; 2:False → 3:In |
| `sts_bls_ina_08_bugfixing.questphase / h173 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ina_08_tr"}}` | 3:Out → 7:In; 7:Out → 4:In |
| `sts_bls_ina_08_bugfixing.questphase / h229 / 4` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-657732"}}}` | 2:Out → 4:In; 4:False → 5:In |
| `sts_bls_ina_08_bugfixing.questphase / h229 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ina_08_com_guide","names":["guide"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 8:Out → 6:In; 6:Out → 7:In |
| `sts_bls_ina_08_bugfixing.questphase / h229 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ina_08_tr_in_freezer"}}` | 5:Out → 8:In; 8:Out → 6:In |
| `sts_bls_ina_08_bugfixing.questphase / h295 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-672815"}}}` | 0:Out → 2:In; 2:False → 3:In |
| `sts_bls_ina_08_bugfixing.questphase / h295 / 12` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/04_scan_bodies_to_find_trevor","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 3:Out → 12:In; 12:True → 4:In; 12:False → 13:In |
| `sts_bls_ina_08_bugfixing.questphase / h295 / 13` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/03_find_body","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 13:True → 4:In; 12:False → 13:In; 13:False → 14:In |
| `sts_bls_ina_08_bugfixing.questphase / h295 / 14` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/02_get_to_the_camp","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 14:True → 4:In; 13:False → 14:In; 14:False → 15:In |
| `sts_bls_ina_08_bugfixing.questphase / h295 / 15` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/02_get_to_the_camp","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 15:True → 4:In; 14:False → 15:In |
| `sts_bls_ina_08_openworld.questphase / h7 / 124` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ina_08_tr_outpost"}}` | 250:Out → 124:In; 251:Out → 124:In; 124:Out → 252:Succeeded |
| `sts_bls_ina_08_openworld.questphase / h7 / 242` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ina_08_test_def"}}}` | 300:Out → 242:In; 242:True → 250:Active; 242:False → 251:Active |
| `sts_bls_ina_08_openworld.questphase / h7 / 254` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ina_08_tr_in_freezer"}}` | 253:Out → 254:In; 254:Out → 255:Succeeded; 254:Out → 363:In |
| `sts_bls_ina_08_openworld.questphase / h7 / 259` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ina_08_com_guide","names":["guide"]},"eventType":"Finished"}}}` | 256:Out → 259:In; 259:Out → 258:Succeeded |
| `sts_bls_ina_08_openworld.questphase / h7 / 288` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questVehicleCondition","type":{"$type":"questVehicleTrunk_ConditionType","playerVehicle":false,"vehicleRef":{"$type":"gameEntityReference","reference":"#ina_08_com_nomads","names":["car_01"]},"objectRef":{"$type":"gameEntityReference","reference":"#ina_08_com_guide","names":["guide"]}}}}` | 287:Out → 288:In; 288:Out → 289:Succeeded |
| `sts_bls_ina_08_openworld.questphase / h7 / 295` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":8}}}` | 292:Out → 295:In; 295:Out → 303:Active |
| `sts_bls_ina_08_openworld.questphase / h7 / 308` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ina_08_tr"}}` | 302:Out → 308:In; 308:Out → 307:In; 310:Out → 308:In |
| `sts_bls_ina_08_openworld.questphase / h7 / 309` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ina_08_tr"}}` | 307:Out → 309:In; 309:Out → 310:In |
| `sts_bls_ina_08_openworld.questphase / h7 / 322` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 264:Out → 322:In; 322:Out → 311:In |
| `sts_bls_ina_08_openworld.questphase / h7 / 325` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentIsPlayer":true,"childRef":{"$type":"gameEntityReference","reference":"#ina_08_com_guide","names":["guide"]}}}}` | 256:Out → 325:In; 325:Out → 327:Inactive |
| `sts_bls_ina_08_openworld.questphase / h7 / 344` | `questConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 344:False → 302:Active; 344:True → 321:Start1; 365:False → 344:In |
| `sts_bls_ina_08_openworld.questphase / h7 / 349` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ina_08_tr_outpost"},{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentIsPlayer":true,"childRef":{"$type":"gameEntityReference","reference":"#ina_08_com_guide","names":["guide"]}}}]}}` | 292:Out → 349:In; 349:Out → 293:Succeeded |
| `sts_bls_ina_08_openworld.questphase / h7 / 351` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#ina_08_com_guide","names":["guide"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":100.0}}}}` | 292:Out → 351:In; 351:Out → 352:Active |
| `sts_bls_ina_08_openworld.questphase / h7 / 353` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#ina_08_com_guide","names":["guide"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":200.0}}}}` | 352:Out → 353:In; 353:Out → 356:Failed |
| `sts_bls_ina_08_openworld.questphase / h7 / 364` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\badlands\\inland_avenue\\sts_bls_ina_08\\scenes\\sts_bls_ina_08_holocall_prebrief.scene","Flags":"Soft"},"type":"IsOutside"}}}` | 364:Out → 265:In; 311:Out → 364:In |
| `sts_bls_ina_08_openworld.questphase / h7 / 365` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}}}` | 0:Out → 365:In; 365:True → 302:Active; 365:False → 344:In |
| `sts_bls_ina_08_openworld.questphase / h317 / 19` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/06_put_body_in_trunk","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 19:True → 18:Inactive; 41:Out → 19:In; 19:False → 49:Inactive |
| `sts_bls_ina_08_openworld.questphase / h317 / 41` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentIsPlayer":true,"childRef":{"$type":"gameEntityReference","reference":"#ina_08_com_guide","names":["guide"]},"condition":"OnUnmount"}}}` | 11:Out → 41:In; 41:Out → 19:In |
| `sts_bls_ina_08_openworld.questphase / h317 / 43` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/06_put_body_in_trunk","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 11:Out → 43:In; 43:Out → 44:In |
| `sts_bls_ina_08_openworld.questphase / h317 / 45` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentIsPlayer":true,"childRef":{"$type":"gameEntityReference","reference":"#ina_08_com_guide","names":["guide"]}}}}` | 14:Out → 45:In; 45:Out → 16:Succeeded |
| `sts_bls_ina_08_openworld.questphase / h317 / 51` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentIsPlayer":true,"childRef":{"$type":"gameEntityReference","reference":"#ina_08_com_guide","names":["guide"]}}}}` | 50:Out → 51:In; 51:Out → 52:Succeeded |
| `sts_bls_ina_08_openworld.questphase / h572 / 200` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ina_08_com_nomads"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 199:Out → 200:In; 200:Out → 201:In |
| `sts_bls_ina_08_openworld.questphase / h572 / 202` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#ina_08_com_nomads","names":["car_01"]},"childRef":{"$type":"gameEntityReference","reference":"#ina_08_com_nomads","names":["nomad_01"]},"role":"Driver"}}}` | 201:Out → 202:In; 202:Out → 251:In; 202:Out → 209:In |
| `sts_bls_ina_08_openworld.questphase / h572 / 222` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 209:Out → 222:In; 222:Out → 258:In |
| `sts_bls_ina_08_openworld.questphase / h572 / 224` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questVehicleCondition","type":{"$type":"questVehicleTrunk_ConditionType","playerVehicle":false,"vehicleRef":{"$type":"gameEntityReference","reference":"#ina_08_com_nomads","names":["car_01"]},"objectRef":{"$type":"gameEntityReference","reference":"#ina_08_com_guide","names":["guide"]}}}}` | 209:Out → 224:In; 224:Out → 225:In; 224:Out → 227:In |
| `sts_bls_ina_08_openworld.questphase / h572 / 225` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questVehicleCondition","type":{"$type":"questVehicleDoor_ConditionType","vehicleRef":{"$type":"gameEntityReference","reference":"#ina_08_com_nomads","names":["car_01"]},"door":"trunk","state":"Closed"}}}` | 224:Out → 225:In; 225:Out → 229:In |
| `sts_bls_ina_08_openworld.questphase / h572 / 227` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 224:Out → 227:In; 227:Out → 228:In |
| `sts_bls_ina_08_openworld.questphase / h572 / 229` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 225:Out → 229:In; 229:Out → 226:In |
| `sts_bls_ina_08_openworld.questphase / h572 / 263` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/take_the_body_from_the_location","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 0:Out → 263:In; 263:Out → 212:In |
| `sts_bls_ina_08_openworld.questphase / h717 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#ina_08_com_nomads","names":["nomad_01"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":100.0}}}}` | 7:Out → 2:In; 2:Out → 3:In |
| `sts_bls_ina_08_openworld.questphase / h717 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":200}}}` | 3:Out → 5:In; 5:Out → 4:In |
| `sts_bls_ina_08_openworld.questphase / h717 / 21` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","days":2}}}` | 31:Out → 21:In; 21:Out → 30:In |
| `sts_bls_ina_08_openworld.questphase / h717 / 28` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ina_08_failed"}}}` | 38:Out → 28:In; 28:True → 29:In; 28:False → 40:In |
| `sts_bls_ina_08_openworld.questphase / h717 / 30` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ina_08_tr"}}` | 30:Out → 15:In; 21:Out → 30:In |
| `sts_bls_ina_08_openworld.questphase / h717 / 36` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\badlands\\inland_avenue\\sts_bls_ina_08\\scenes\\sts_bls_ina_08_holocall_debriefs.scene","Flags":"Soft"},"type":"IsOutside"}}}` | 36:Out → 1:In; 18:Out → 36:In; 19:Out → 36:In; 20:Out → 36:In; 25:Out → 36:In |
| `sts_bls_ina_08_openworld.questphase / h717 / 38` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 38:Out → 28:In; 37:Out → 38:In |
| `sts_bls_ina_08_openworld.questphase / h717 / 40` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}}}` | 40:False → 23:Start1; 28:False → 40:In; 40:True → 39:Active |
| `sts_bls_ina_08_openworld.questphase / h926 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ina_08_com_cars"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":2,"comparisonType":"GreaterOrEqual"}}}}` | 24:Out → 7:In; 7:Out → 42:In |
| `sts_bls_ina_08_openworld.questphase / h926 / 11` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 13:Out → 11:In; 11:Out → 38:In |
| `sts_bls_ina_08_openworld.questphase / h926 / 44` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#ina_08_tr"},{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PlayerSubType","vehicleComparisonType":"NotEqual","vehicleState":"Driving"}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PlayerSubType","vehicleComparisonType":"NotEqual","vehicleState":"Passenger"}}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleScene","inverted":true}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleSceneFpp","inverted":true}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleSceneFppOnlyForward","inverted":true}}]}}` | 44:Out → 43:In; 45:Out → 44:In |
| `sts_bls_ina_08_holocall_debriefs.scene / scene / 98` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_dakota_calls_v_end_done"}}}` | 98:0:0 → 99:0:1; 103:0:0 → 98:0:1 |
| `sts_bls_ina_08_holocall_debriefs.scene / scene / 249` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2,"miliseconds":600}}}` | 96:666:0 → 249:0:1; 249:0:0 → 251:0:1; 257:0:0 → 249:0:1; 261:1:0 → 249:0:0; 261:1:0 → 249:1026:0 |
| `sts_bls_ina_08_holocall_debriefs.scene / scene / 251` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_dakota_calls_v_start_activate","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 249:0:0 → 251:0:1; 251:0:0 → 253:0:1; 261:1:0 → 251:0:0; 261:1:0 → 251:1026:0 |
| `sts_bls_ina_08_holocall_debriefs.scene / scene / 253` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2,"miliseconds":600}}}` | 251:0:0 → 253:0:1; 253:0:0 → 255:0:1; 261:1:0 → 253:0:0; 261:1:0 → 253:1026:0 |
| `sts_bls_ina_08_holocall_debriefs.scene / scene / 255` | `questConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 253:0:0 → 255:0:1; 255:0:0 → 259:0:1; 255:0:1 → 257:0:0 |
| `sts_bls_ina_08_holocall_debriefs.scene / scene / 270` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_dakota_calls_v_start_done"}}}` | 96:666:0 → 270:0:1; 270:0:0 → 261:0:0 |
| `sts_bls_ina_08_holocall_debriefs.scene / scene / 282` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_dakota_calls_v_rejected"}}}` | 102:0:0 → 282:0:1; 282:0:0 → 284:0:1 |
| `sts_bls_ina_08_holocall_prebrief.scene / scene / 98` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_dakota_calls_v_end_done"}}}` | 98:0:0 → 99:0:1; 103:0:0 → 98:0:1 |
| `sts_bls_ina_08_holocall_prebrief.scene / scene / 256` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_dakota_calls_v_rejected"}}}` | 102:0:0 → 256:0:1; 256:0:0 → 258:0:1 |
| `sts_bls_ina_08_holocall_prebrief.scene / scene / 267` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_dakota_calls_v_start_done"}}}` | 96:666:0 → 267:0:1; 267:0:0 → 270:0:0 |
| `sts_bls_ina_08_holocall_prebrief.scene / scene / 273` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":30}}}` | 96:666:0 → 273:0:1; 270:1:0 → 273:0:0; 273:0:0 → 283:0:1 |
| `sts_bls_ina_08_holocall_prebrief.scene / scene / 283` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_active_call_interrupted","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 273:0:0 → 283:0:1; 283:0:0 → 281:0:1; 283:0:1 → 285:0:1; 285:0:0 → 283:0:1 |
| `sts_bls_ina_08_holocall_prebrief.scene / scene / 285` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 270:1:0 → 285:0:0; 283:0:1 → 285:0:1; 285:0:0 → 283:0:1 |
| `sts_bls_inland_avenue.questphase / h413 / 124` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ina_08_tr_outpost"}}` | 250:Out → 124:In; 251:Out → 124:In; 124:Out → 252:Succeeded |
| `sts_bls_inland_avenue.questphase / h413 / 242` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ina_08_test_def"}}}` | 300:Out → 242:In; 242:True → 250:Active; 242:False → 251:Active |
| `sts_bls_inland_avenue.questphase / h413 / 254` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ina_08_tr_in_freezer"}}` | 253:Out → 254:In; 254:Out → 255:Succeeded; 254:Out → 363:In |
| `sts_bls_inland_avenue.questphase / h413 / 259` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ina_08_com_guide","names":["guide"]},"eventType":"Finished"}}}` | 256:Out → 259:In; 259:Out → 258:Succeeded |
| `sts_bls_inland_avenue.questphase / h413 / 288` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questVehicleCondition","type":{"$type":"questVehicleTrunk_ConditionType","playerVehicle":false,"vehicleRef":{"$type":"gameEntityReference","reference":"#ina_08_com_nomads","names":["car_01"]},"objectRef":{"$type":"gameEntityReference","reference":"#ina_08_com_guide","names":["guide"]}}}}` | 287:Out → 288:In; 288:Out → 289:Succeeded |
| `sts_bls_inland_avenue.questphase / h413 / 295` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":8}}}` | 292:Out → 295:In; 295:Out → 303:Active |
| `sts_bls_inland_avenue.questphase / h413 / 322` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 264:Out → 322:In; 322:Out → 311:In |
| `sts_bls_inland_avenue.questphase / h413 / 325` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentIsPlayer":true,"childRef":{"$type":"gameEntityReference","reference":"#ina_08_com_guide","names":["guide"]}}}}` | 256:Out → 325:In; 325:Out → 327:Inactive |
| `sts_bls_inland_avenue.questphase / h413 / 349` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ina_08_tr_outpost"},{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentIsPlayer":true,"childRef":{"$type":"gameEntityReference","reference":"#ina_08_com_guide","names":["guide"]}}}]}}` | 292:Out → 349:In; 349:Out → 293:Succeeded |
| `sts_bls_inland_avenue.questphase / h413 / 351` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#ina_08_com_guide","names":["guide"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":100.0}}}}` | 292:Out → 351:In; 351:Out → 352:Active |
| `sts_bls_inland_avenue.questphase / h413 / 353` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#ina_08_com_guide","names":["guide"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":200.0}}}}` | 352:Out → 353:In; 353:Out → 356:Failed |
| `sts_bls_inland_avenue.questphase / h723 / 19` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/06_put_body_in_trunk","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 19:True → 18:Inactive; 41:Out → 19:In; 19:False → 49:Inactive |
| `sts_bls_inland_avenue.questphase / h723 / 41` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentIsPlayer":true,"childRef":{"$type":"gameEntityReference","reference":"#ina_08_com_guide","names":["guide"]},"condition":"OnUnmount"}}}` | 11:Out → 41:In; 41:Out → 19:In |
| `sts_bls_inland_avenue.questphase / h723 / 43` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/06_put_body_in_trunk","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 11:Out → 43:In; 43:Out → 44:In |
| `sts_bls_inland_avenue.questphase / h723 / 45` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentIsPlayer":true,"childRef":{"$type":"gameEntityReference","reference":"#ina_08_com_guide","names":["guide"]}}}}` | 14:Out → 45:In; 45:Out → 16:Succeeded |
| `sts_bls_inland_avenue.questphase / h723 / 51` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentIsPlayer":true,"childRef":{"$type":"gameEntityReference","reference":"#ina_08_com_guide","names":["guide"]}}}}` | 50:Out → 51:In; 51:Out → 52:Succeeded |
| `sts_bls_inland_avenue.questphase / h978 / 263` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/badlands/inland_avenue/sts_bls_ina_08/sts_bls_ina_08/take_the_body_from_the_location","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 0:Out → 263:In; 263:Out → 212:In |
| `sts_badlands.questphase / h11 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/badlands/inland_avenue/sts_bls_ina_08","fileEntryIndex":4,"className":"gameJournalQuest"},"state":"Active"}}}` | 0:Out → 7:In; 7:Out → 12:In7 |
| `sts_badlands.questphase / h11 / 12` | `questLogicalXorNodeDefinition` `{"inputSocketCount":9}` | 2:Out → 12:In1; 3:Out → 12:In2; 4:Out → 12:In3; 5:Out → 12:In4; 6:Out → 12:In5; 7:Out → 12:In7; 8:Out → 12:In6; 9:Out → 12:In8; 10:Out → 12:In9; 12:Out1 → 13:In |
| `open_world_bugfixing.questphase / h1543 / 11` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ina_08_finished"}}}` | 0:Out → 11:In; 11:True → 12:Succeeded |
| `open_world_bugfixing.questphase / h1543 / 13` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ina_08_failed"}}}` | 0:Out → 13:In; 13:True → 12:Failed |
| `open_world_bugfixing.questphase / h2679 / 11` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ina_08_finished"}}}` | 0:Out → 11:In; 11:True → 12:Succeeded |
| `open_world_bugfixing.questphase / h2679 / 13` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ina_08_failed"}}}` | 0:Out → 13:In; 13:True → 12:Failed |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | sts_bls_ina_08_bugfixing.questphase / h10 / 5; sts_bls_ina_08_bugfixing.questphase / h229 / 6; sts_bls_ina_08_openworld.questphase / h572 / 200; sts_bls_ina_08_openworld.questphase / h926 / 7 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `checkpoint` | sts_bls_ina_08_openworld.questphase / h0 / 8; sts_bls_ina_08_openworld.questphase / h926 / 33 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `community_lifecycle` | sts_bls_ina_08_bugfixing.questphase / h173 / 4; sts_bls_ina_08_bugfixing.questphase / h295 / 4; sts_bls_ina_08_openworld.questphase / h572 / 199; sts_bls_ina_08_openworld.questphase / h717 / 15; +4 locations in catalogue.json | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | open_world_bugfixing.questphase / h1543 / 11; open_world_bugfixing.questphase / h1543 / 13; open_world_bugfixing.questphase / h2679 / 11; open_world_bugfixing.questphase / h2679 / 13; +20 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | sts_bls_ina_08_openworld.questphase / h7 / 307; sts_bls_ina_08_openworld.questphase / h7 / 310; sts_bls_ina_08_openworld.questphase / h7 / 311; sts_bls_ina_08_openworld.questphase / h717 / 29; +2 locations in catalogue.json | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `controller_event` | sts_bls_ina_08_openworld.questphase / h7 / 313; sts_bls_ina_08_openworld.questphase / h717 / 18; sts_bls_ina_08_openworld.questphase / h717 / 19; sts_bls_ina_08_openworld.questphase / h717 / 20; +1 locations in catalogue.json | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `elapsed_time` | sts_bls_ina_08_openworld.questphase / h717 / 21 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `journal_transition` | open_world_bugfixing.questphase / h1543 / 12; open_world_bugfixing.questphase / h2679 / 12; sts_bls_ina_08_openworld.questphase / h317 / 14; sts_bls_ina_08_openworld.questphase / h317 / 16; +55 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `mount_state` | sts_bls_ina_08_openworld.questphase / h317 / 41; sts_bls_ina_08_openworld.questphase / h317 / 45; sts_bls_ina_08_openworld.questphase / h317 / 51; sts_bls_ina_08_openworld.questphase / h572 / 202; +7 locations in catalogue.json | parent vehicle/puppet + child + role/event → mount/unmount condition. Match seat/role and OnMount/OnUnmount semantics; do not confuse assignment with readiness. |
| `persistent_decision` | sts_bls_ina_08_bugfixing.questphase / h10 / 4; sts_bls_ina_08_bugfixing.questphase / h173 / 3; sts_bls_ina_08_bugfixing.questphase / h229 / 5; sts_bls_ina_08_bugfixing.questphase / h295 / 3; +30 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | sts_badlands.questphase / h11 / 12 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | sts_bls_ina_08_bugfixing.questphase / h71 / 11; sts_bls_ina_08_holocall_debriefs.scene / scene / 249; sts_bls_ina_08_holocall_debriefs.scene / scene / 253; sts_bls_ina_08_holocall_prebrief.scene / scene / 273; +11 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | sts_bls_ina_08_bugfixing.questphase / h71 / 13 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `reward_commit` | sts_bls_ina_08_openworld.questphase / h717 / 8 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scan_evidence` | sts_bls_ina_08_openworld.questphase / h7 / 259; sts_bls_inland_avenue.questphase / h413 / 259 | clue reference + exact scan event + required-set policy → clue observed. Preserve Started versus Finished, ordering, bypass and reaction joins. |
| `scene_interface` | sts_bls_ina_08_openworld.questphase / h7 / 321; sts_bls_ina_08_openworld.questphase / h717 / 23 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | sts_bls_ina_08_bugfixing.questphase / h10 / 7; sts_bls_ina_08_bugfixing.questphase / h173 / 7; sts_bls_ina_08_bugfixing.questphase / h229 / 8; sts_bls_ina_08_openworld.questphase / h7 / 124; +9 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `vehicle_control` | sts_bls_ina_08_bugfixing.questphase / h173 / 5; sts_bls_ina_08_bugfixing.questphase / h173 / 6; sts_bls_ina_08_openworld.questphase / h572 / 201; sts_bls_ina_08_openworld.questphase / h572 / 219; +9 locations in catalogue.json | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |
| `world_variant` | sts_bls_ina_08_openworld.questphase / h717 / 25 | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\phases\sts_bls_ina_08_bugfixing.questphase` | repair; journal anchor | `base-sts-bls-ina-08` |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\phases\sts_bls_ina_08_openworld.questphase` | content candidate; journal anchor | `base-sts-bls-ina-08` |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\scenes\sts_bls_ina_08_holocall_debriefs.scene` | content candidate; forward dependency | `base-sts-bls-ina-08` |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\scenes\sts_bls_ina_08_holocall_prebrief.scene` | content candidate; forward dependency | `base-sts-bls-ina-08` |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_inland_avenue.questphase` | content candidate; journal anchor | `base-shared` |
| `base\open_world\street_stories\badlands\sts_badlands.questphase` | content candidate; journal anchor | `base-shared` |
| `base\quest\bugfixing\open_world_bugfixing.questphase` | repair; journal anchor | `base-shared` |

Evidence shards for this dossier (including parent context): [base-ma-bls-ina-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-07.json.gz), [base-ma-bls-ina-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-08.json.gz), [base-ma-bls-ina-se1-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-se1-22.json.gz), [base-ma-cct-dtn-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-03.json.gz), [base-ma-cct-dtn-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-07.json.gz), [base-ma-hey-spr-04](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-04.json.gz), [base-ma-hey-spr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-06.json.gz), [base-ma-pac-cvi-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-08.json.gz), [base-ma-pac-cvi-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-15.json.gz), [base-ma-std-arr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-arr-06.json.gz), [base-ma-std-rcr-11](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-rcr-11.json.gz), [base-ma-wat-kab-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-02.json.gz), [base-ma-wat-kab-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-08.json.gz), [base-ma-wat-lch-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-lch-06.json.gz), [base-ma-wat-nid-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-03.json.gz), [base-ma-wat-nid-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-15.json.gz), [base-ma-wat-nid-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-22.json.gz), [base-mq000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq000.json.gz), [base-mq001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq001.json.gz), [base-mq003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq003.json.gz), [base-mq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq006.json.gz), [base-mq007](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq007.json.gz), [base-mq008](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq008.json.gz), [base-mq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq011.json.gz), [base-mq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq012.json.gz), [base-mq013](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq013.json.gz), [base-mq014](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq014.json.gz), [base-mq015](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq015.json.gz), [base-mq016](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq016.json.gz), [base-mq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq017.json.gz), [base-mq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq018.json.gz), [base-mq019](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq019.json.gz), [base-mq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq021.json.gz), [base-mq022](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq022.json.gz), [base-mq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq023.json.gz), [base-mq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq024.json.gz), [base-mq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq025.json.gz), [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-mq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq028.json.gz), [base-mq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq030.json.gz), [base-mq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq032.json.gz), [base-mq033](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq033.json.gz), [base-mq035](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq035.json.gz), [base-mq037](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq037.json.gz), [base-mq038](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq038.json.gz), [base-mq040](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq040.json.gz), [base-mq041](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq041.json.gz), [base-mq048](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq048.json.gz), [base-mq055](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq055.json.gz), [base-mws-wat-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mws-wat-08.json.gz), [base-q000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q000.json.gz), [base-q001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q001.json.gz), [base-q003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q003.json.gz), [base-q004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q004.json.gz), [base-q005](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q005.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q103](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q103.json.gz), [base-q105](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q105.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q113](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q113.json.gz), [base-q114](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q114.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-q202](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q202.json.gz), [base-q203](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q203.json.gz), [base-q204](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q204.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq004.json.gz), [base-sq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq006.json.gz), [base-sq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq011.json.gz), [base-sq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq012.json.gz), [base-sq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq017.json.gz), [base-sq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq018.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq024.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq026.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [base-sq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq028.json.gz), [base-sq029](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq029.json.gz), [base-sq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq030.json.gz), [base-sq031](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq031.json.gz), [base-sq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq032.json.gz), [base-sts-bls-ina-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-bls-ina-08.json.gz), [base-sts-hey-rey-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-hey-rey-02.json.gz), [base-ue-metro](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ue-metro.json.gz), [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

189 repeated typed/socket path signatures in this selected graph context; 34 distinct direct resource identities; 11 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `e5742f9794e6583c67cb` | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\scenes\sts_bls_ina_08_holocall_debriefs.scene` / scene / 102 -> 282 -> 284 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `fee3756653cd083fb28e` | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\phases\sts_bls_ina_08_openworld.questphase` / h717 / 31 -> 21 -> 30 | questDeletionMarkerNodeDefinition -> questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition] -> questPauseConditionNodeDefinition[questTriggerCondition]; Out -> In; Out -> In |
| `1d933adb5a617880c93e` | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\scenes\sts_bls_ina_08_holocall_debriefs.scene` / scene / 101 -> 103 -> 98 | scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `2e1ee5a1324dbeeb9071` | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\phases\sts_bls_ina_08_openworld.questphase` / h926 / 26 -> 24 -> 7 | questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]; Out -> In; Out -> In |
| `d6b7c21f5d2d0ab76fc6` | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\scenes\sts_bls_ina_08_holocall_debriefs.scene` / scene / 282 -> 284 -> 286 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnEndNode[scnNodeId]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `26762f051e7728f090ca` | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\scenes\sts_bls_ina_08_holocall_debriefs.scene` / scene / 97 -> 100 -> 26 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `101b60945ddf6f25f378` | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\scenes\sts_bls_ina_08_holocall_debriefs.scene` / scene / 26 -> 101 -> 103 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:0; 0:0 -> 0:1 |
| `9e5e28ecb38ea2a53a15` | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\scenes\sts_bls_ina_08_holocall_debriefs.scene` / scene / 280 -> 102 -> 282 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `2beeeaa3b4da5300c035` | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\scenes\sts_bls_ina_08_holocall_debriefs.scene` / scene / 94 -> 280 -> 102 | scnStartNode[scnNodeId] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `eaf5aab427d50e5598b6` | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\phases\sts_bls_ina_08_bugfixing.questphase` / h10 / 0 -> 3 -> 4 | questInputNodeDefinition -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; False -> In |
| `4e9253a72e6b0134b8dd` | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\phases\sts_bls_ina_08_openworld.questphase` / h7 / 124 -> 252 -> 253 | questPauseConditionNodeDefinition[questTriggerCondition] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Succeeded; Out -> Active |
| `bbf9efd740881cf31a37` | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\scenes\sts_bls_ina_08_holocall_debriefs.scene` / scene / 270 -> 261 -> 249 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> scnCutControlNode[scnNodeId] -> questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]; 0:0 -> 0:0; 1:0 -> 0:0 |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_inland_avenue.questphase` / h413 / 323 | `h723` | [{"$type":"questInputNodeDefinition","id":11,"socketName":"In2"},{"$type":"questOutputNodeDefinition","id":12,"socketName":"Out2"},{"$type":"questOutputNodeDefinition","id":44,"socketName":"Out1"}] |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\phases\sts_bls_ina_08_bugfixing.questphase` / h0 / 3 | `h10` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\phases\sts_bls_ina_08_bugfixing.questphase` / h0 / 9 | `h71` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\phases\sts_bls_ina_08_bugfixing.questphase` / h0 / 12 | `h173` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\phases\sts_bls_ina_08_bugfixing.questphase` / h0 / 16 | `h229` | [{"$type":"questInputNodeDefinition","id":2,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":3,"socketName":"Out1"}] |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\phases\sts_bls_ina_08_bugfixing.questphase` / h0 / 21 | `h295` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\phases\sts_bls_ina_08_openworld.questphase` / h0 / 1 | `h7` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":265,"socketName":"Out1"}] |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\phases\sts_bls_ina_08_openworld.questphase` / h7 / 323 | `h317` | [{"$type":"questInputNodeDefinition","id":11,"socketName":"In2"},{"$type":"questOutputNodeDefinition","id":12,"socketName":"Out2"},{"$type":"questOutputNodeDefinition","id":44,"socketName":"Out1"}] |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\phases\sts_bls_ina_08_openworld.questphase` / h0 / 2 | `h572` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\phases\sts_bls_ina_08_openworld.questphase` / h0 / 3 | `h717` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\phases\sts_bls_ina_08_openworld.questphase` / h0 / 5 | `h926` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

### Launch definition context

These definitions reference this quest context or a resolved ancestor. They can include test/debug launch configurations; their presence does not establish that the installed game selects them.

| Definition | Path role | Referenced context |
| --- | --- | --- |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07.gamedef` | content candidate | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07.quest |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08.gamedef` | content candidate | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08.quest |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22.gamedef` | content candidate | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22.quest |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03.gamedef` | content candidate | base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03.quest |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07.gamedef` | content candidate | base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07.quest |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04.gamedef` | content candidate | base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04.quest |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06.gamedef` | content candidate | base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06.quest |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\ma_pac_cvi_08.gamedef` | content candidate | base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\ma_pac_cvi_08.quest |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15.gamedef` | content candidate | base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15.quest |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06.gamedef` | content candidate | base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06.quest |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\ma_std_rcr_11.gamedef` | content candidate | base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\ma_std_rcr_11.quest |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02.gamedef` | content candidate | base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_quest.quest |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_def.gamedef` | content candidate | base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_quest.quest |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\ma_wat_lch_06.gamedef` | content candidate | base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\ma_wat_lch_06.quest |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_03\ma_wat_nid_03.gamedef` | content candidate | base\open_world\minor_activities\watson\northside\ma_wat_nid_03\ma_wat_nid_03.quest |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\ma_wat_nid_15.gamedef` | content candidate | base\open_world\minor_activities\watson\northside\ma_wat_nid_15\ma_wat_nid_15.quest |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_22\ma_wat_nid_22.gamedef` | content candidate | base\open_world\minor_activities\watson\northside\ma_wat_nid_22\ma_wat_nid_22.quest |
| `base\quest\minor_quests\mq000\mq000.gamedef` | content candidate | base\quest\minor_quests\mq000\mq000.quest |
| `base\quest\minor_quests\mq000\mq000_thank_you.gamedef` | content candidate | base\quest\minor_quests\mq000\mq000.quest |
| `base\quest\minor_quests\mq001\mq001.gamedef` | content candidate | base\quest\minor_quests\mq001\mq001.quest |
| `base\quest\minor_quests\mq003\mq003_orbitals.gamedef` | content candidate | base\quest\minor_quests\mq003\mq003_orbitals.quest |
| `base\quest\minor_quests\mq006\mq006.gamedef` | content candidate | base\quest\minor_quests\mq006\mq006.quest |
| `base\quest\minor_quests\mq007\mq007.gamedef` | content candidate | base\quest\minor_quests\mq007\mq007.quest |
| `base\quest\minor_quests\mq008\mq008.gamedef` | content candidate | base\quest\minor_quests\mq008\mq008.quest |
| `base\quest\minor_quests\mq011\mq011.gamedef` | content candidate | base\quest\minor_quests\mq011\mq011.quest |
| `base\quest\minor_quests\mq012\mq012.gamedef` | content candidate | base\quest\minor_quests\mq012\mq012.quest |
| `base\quest\minor_quests\mq013\mq013.gamedef` | content candidate | base\quest\minor_quests\mq013\mq013.quest |
| `base\quest\minor_quests\mq014\mq014.gamedef` | content candidate | base\quest\minor_quests\mq014\mq014.quest |
| `base\quest\minor_quests\mq015\mq015_wizardbook.gamedef` | content candidate | base\quest\minor_quests\mq015\mq015_wizardbook.quest |
| `base\quest\minor_quests\mq016\mq016_bartmoss.gamedef` | content candidate | base\quest\minor_quests\mq016\mq016_bartmoss.quest |
| `base\quest\minor_quests\mq017\mq017_streetkid.gamedef` | content candidate | base\quest\minor_quests\mq017\mq017_streetkid.quest |
| `base\quest\minor_quests\mq018\mq018.gamedef` | content candidate | base\quest\minor_quests\mq018\mq018.quest |
| `base\quest\minor_quests\mq019\mq019_paparazzi.gamedef` | content candidate | base\quest\minor_quests\mq019\mq019_paparazzi.quest |
| `base\quest\minor_quests\mq021\mq021.gamedef` | content candidate | base\quest\minor_quests\mq021\mq021.quest |
| `base\quest\minor_quests\mq022\mq022.gamedef` | content candidate | base\quest\minor_quests\mq022\mq022.quest |
| `base\quest\minor_quests\mq023\mq023_bootleg.gamedef` | content candidate | base\quest\minor_quests\mq023\mq023_bootleg.quest |
| `base\quest\minor_quests\mq024\mq024.gamedef` | content candidate | base\quest\minor_quests\mq024\mq024.quest |
| `base\quest\minor_quests\mq025\mq025_psycho_brawl.gamedef` | content candidate | base\quest\minor_quests\mq025\mq025_psycho_brawl.quest |
| `base\quest\minor_quests\mq026\mq026.gamedef` | content candidate | base\quest\minor_quests\mq026\mq026.quest |
| `base\quest\minor_quests\mq028\mq028.gamedef` | content candidate | base\quest\minor_quests\mq028\mq028.quest |
| `base\quest\minor_quests\mq030\mq030.gamedef` | content candidate | base\quest\minor_quests\mq030\mq030.quest |
| `base\quest\minor_quests\mq032\mq032_sacrum.gamedef` | content candidate | base\quest\minor_quests\mq032\mq032_sacrum.quest |
| `base\quest\minor_quests\mq033\mq033_tarot.gamedef` | content candidate | base\quest\minor_quests\mq033\mq033_tarot.quest |
| `base\quest\minor_quests\mq035\mq035_ozob.gamedef` | content candidate | base\quest\minor_quests\mq035\mq035_ozob.quest |
| `base\quest\minor_quests\mq037\mq037_brendan.gamedef` | content candidate | base\quest\minor_quests\mq037\mq037_brendan.quest |
| `base\quest\minor_quests\mq038\mq038.gamedef` | content candidate | base\quest\minor_quests\mq038\mq038.quest |
| `base\quest\minor_quests\mq040\mq040_biosculpt.gamedef` | content candidate | base\quest\minor_quests\mq040\mq040_biosculpt.quest |
| `base\quest\minor_quests\mq041\mq041_corpo.gamedef` | content candidate | base\quest\minor_quests\mq041\mq041_corpo.quest |
| `base\quest\minor_quests\mq048\mq048.gamedef` | content candidate | base\quest\minor_quests\mq048\mq048.quest |
| `base\quest\minor_quests\mq055\mq055.gamedef` | content candidate | base\quest\minor_quests\mq055\mq055.quest |
| `base\open_world\mini_world_stories\watson\mws_wat_08\mws_wat_08.gamedef` | content candidate | base\open_world\mini_world_stories\watson\mws_wat_08\mws_wat_08.quest |
| `base\quest\main_quests\prologue\q000\q000.gamedef` | content candidate | base\quest\main_quests\prologue\q000\q000.quest |
| `base\quest\main_quests\prologue\q001\q001.gamedef` | content candidate | base\quest\main_quests\prologue\q001\q001.quest |
| `base\quest\main_quests\prologue\q001\test\q001_miss0_mark_world.gamedef` | test/debug | base\quest\main_quests\prologue\q001\q001.quest |
| `base\quest\main_quests\prologue\q003\q003.gamedef` | content candidate | base\quest\main_quests\prologue\q003\q003.quest |
| `base\quest\main_quests\prologue\q005\q005_heist.gamedef` | content candidate | base\quest\main_quests\prologue\q005\q005_heist.quest |
| `base\quest\main_quests\part1\q101\q101.gamedef` | content candidate | base\quest\main_quests\part1\q101\q101.quest |
| `base\quest\main_quests\part1\q103\q103.gamedef` | content candidate | base\quest\main_quests\part1\q103\q103.quest |
| `base\quest\main_quests\part1\q105\q105_main.gamedef` | content candidate | base\quest\main_quests\part1\q105\q105_main.quest |
| `base\quest\main_quests\part1\q110\q110.gamedef` | content candidate | base\quest\main_quests\part1\q110\q110.quest |
| `base\quest\main_quests\part1\q112\q112_abduction.gamedef` | content candidate | base\quest\main_quests\part1\q112\q112_abduction.quest |
| `base\quest\main_quests\part1\q113\q113.gamedef` | content candidate | base\quest\main_quests\part1\q113\q113.quest |
| `base\quest\main_quests\part1\q114\q114_nomads.gamedef` | content candidate | base\quest\main_quests\part1\q114\q114_nomads.quest |
| `base\quest\main_quests\part1\q115\q115_afterlife.gamedef` | content candidate | base\quest\main_quests\part1\q115\q115_afterlife.quest |
| `base\quest\main_quests\epilogue\q201\q201_heir.gamedef` | content candidate | base\quest\main_quests\epilogue\q201\q201_heir.quest |
| `base\quest\main_quests\epilogue\q202\q202.gamedef` | content candidate | base\quest\main_quests\epilogue\q202\q202.quest |
| `base\quest\main_quests\epilogue\q203\q203_legend.gamedef` | content candidate | base\quest\main_quests\epilogue\q203\q203_legend.quest |
| `base\quest\main_quests\epilogue\q204\q204_reborn.gamedef` | content candidate | base\quest\main_quests\epilogue\q204\q204_reborn.quest |
| `base\open_world\community\heywood\glen\hey_gle_def.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\heywood\wellsprings\hey_spr_def.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\heywood\wellsprings\hey_spr_testdef.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\pacifica\west_wind_estate\pac_wwd_def.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\santo_domingo\arroyo\std_arr_def.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\santo_domingo\rancho_coronado\std_rcr_def.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\watson\kabuki\wat_kab_def.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\watson\kabuki\wat_kab_testdef.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\watson\little_china\wat_lch_prolog_ow_test.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\watson\northside\wat_nid_def.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\westbrook\charter_hill\wbr_hil_com_test.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\westbrook\charter_hill\wbr_hil_com_test_03_02.gamedef` | content candidate | base\open_world\community\westbrook\charter_hill\wbr_hil_com_test.quest |
| `base\open_world\district_definitions\open_world_kabuki.gamedef` | content candidate | base\open_world\district_definitions\open_world_kabuki.quest |
| `base\open_world\open_world_test.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\police_system\police_system_test.gamedef` | content candidate | base\open_world\police_system\police_system_test.quest |
| `base\quest\cyberpunk2077.gamedef` | content candidate | base\quest\cyberpunk2077.quest |
| `base\quest\demos\handson_2020\handson_2020.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020.quest |
| `base\quest\demos\handson_2020\handson_2020_scavengers.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_scavengers.quest |
| `base\quest\demos\handson_2020\handson_2020_testing.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_testing.quest |
| `base\quest\side_quests\sq004\sq004_riders_on_the_storm.gamedef` | content candidate | base\quest\side_quests\sq004\sq004_riders_quest.quest |
| `base\quest\side_quests\sq006\sq006.gamedef` | content candidate | base\quest\side_quests\sq006\sq006.quest |
| `base\quest\side_quests\sq011\sq011.gamedef` | content candidate | base\quest\side_quests\sq011\sq011.quest |
| `base\quest\side_quests\sq012\sq012_the_law.gamedef` | content candidate | base\quest\side_quests\sq012\sq012_the_law.quest |
| `base\quest\side_quests\sq017\sq017.gamedef` | content candidate | base\quest\side_quests\sq017\sq017.quest |
| `base\quest\side_quests\sq018\sq018.gamedef` | content candidate | base\quest\side_quests\sq018\sq018.quest |
| `base\quest\side_quests\sq021\sq021.gamedef` | content candidate | base\quest\side_quests\sq021\sq021.quest |
| `base\quest\side_quests\sq023\sq023.gamedef` | content candidate | base\quest\side_quests\sq023\sq023.quest |
| `base\quest\side_quests\sq024\sq024.gamedef` | content candidate | base\quest\side_quests\sq024\sq024.quest |
| `base\quest\side_quests\sq025\sq025.gamedef` | content candidate | base\quest\side_quests\sq025\sq025.quest |
| `base\quest\side_quests\sq026\sq026.gamedef` | content candidate | base\quest\side_quests\sq026\sq026.quest |
| `base\quest\side_quests\sq027\sq027_queen_of_the_highway.gamedef` | content candidate | base\quest\side_quests\sq027\sq0027_queen_of_the_highway.quest |
| `base\quest\side_quests\sq028\sq028.gamedef` | content candidate | base\quest\side_quests\sq028\sq028.quest |
| `base\quest\side_quests\sq029\sq029.gamedef` | content candidate | base\quest\side_quests\sq029\sq029.quest |
| `base\quest\side_quests\sq030\sq030.gamedef` | content candidate | base\quest\side_quests\sq030\sq030.quest |
| `base\quest\side_quests\sq031\sq031.gamedef` | content candidate | base\quest\side_quests\sq031\sq031.quest |
| `base\quest\side_quests\sq032\sq032.gamedef` | content candidate | base\quest\side_quests\sq032\sq032.quest |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\sts_bls_ina_08.gamedef` | content candidate | base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\sts_bls_ina_08.quest |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\sts_bls_ina_08_test.gamedef` | content candidate | base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\sts_bls_ina_08.quest |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.gamedef` | content candidate | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.quest |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02_test.gamedef` | content candidate | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.quest |
| `base\open_world\metro\ue_metro\ue_metro.gamedef` | content candidate | base\open_world\metro\ue_metro\ue_metro.quest |
| `ep1\quest\minor_quests\mq301\mq301.gamedef` | content candidate | ep1\quest\minor_quests\mq301\mq301.quest |
| `ep1\quest\minor_quests\mq303\mq303.gamedef` | content candidate | ep1\quest\minor_quests\mq303\mq303.quest |
| `ep1\quest\minor_quests\mq304\mq304.gamedef` | content candidate | ep1\quest\minor_quests\mq304\mq304.quest |
| `ep1\quest\minor_quests\mq305\mq305.gamedef` | content candidate | ep1\quest\minor_quests\mq305\mq305.quest |
| `ep1\quest\minor_quests\mq306\mq306.gamedef` | content candidate | ep1\quest\cyberpunk2077_ep1_standalone.quest |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_03\mws_cz_03.gamedef` | content candidate | ep1\openworld\mini_world_stories\combat_zone\mws_cz_03\mws_cz_03.quest |
| `ep1\quest\main_quests\q304\q304.gamedef` | content candidate | ep1\quest\main_quests\q304\q304.quest |
| `ep1\quest\main_quests\q304\q304_car_retrieval_test.gamedef` | content candidate | ep1\quest\main_quests\q304\q304.quest |
| `ep1\quest\main_quests\q304\test\q304_from_escape.gamedef` | test/debug | ep1\quest\main_quests\q304\q304.quest |
| `ep1\quest\main_quests\q304\test\q304_from_lab.gamedef` | test/debug | ep1\quest\main_quests\q304\q304.quest |
| `ep1\quest\main_quests\q304\test\q304_from_songbird_finale.gamedef` | test/debug | ep1\quest\main_quests\q304\q304.quest |
| `ep1\quest\main_quests\q304\test\q304_from_stadium.gamedef` | test/debug | ep1\quest\main_quests\q304\q304.quest |
| `ep1\quest\main_quests\q305\q305.gamedef` | content candidate | ep1\quest\main_quests\q305\q305.quest |
| `ep1\quest\main_quests\q306\q306.gamedef` | content candidate | ep1\quest\main_quests\q306\q306.quest |
| `ep1\quest\main_quests\q307\q307.gamedef` | content candidate | ep1\quest\main_quests\q307\q307.quest |
| `ep1\quest\ep1.gamedef` | content candidate | base\quest\cyberpunk2077.quest |
| `ep1\quest\ep1_standalone.gamedef` | content candidate | ep1\quest\cyberpunk2077_ep1_standalone.quest |
| `ep1\quest\ep1_standalone_debug.gamedef` | content candidate | ep1\quest\cyberpunk2077_ep1_standalone.quest |

### Supporting resource ownership

Providers below are archive-index matches for exact depot hashes. Index presence establishes availability, not payload inspection or runtime load order. Phase/scene/community contents are structurally indexed when marked; other bindings require their own controller, world, performance or localization validation.

| Resource | Binding role | Providers / inspection |
| --- | --- | --- |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_gpl.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_ow.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\phases\sts_bls_ina_03.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\phases\sts_bls_ina_03_gpl.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\phases\sts_bls_ina_03_ow.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_04\phases\sts_bls_ina_04.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_04\phases\sts_bls_ina_04_gameplay.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_04\phases\sts_bls_ina_04_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_05\phases\sts_bls_ina_05_gameplay_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_05\phases\sts_bls_ina_05_openworld_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_05\sts_bls_ina_05.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_06\phases\sts_bls_ina_06.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_06\phases\sts_bls_ina_06_gpl.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_06\phases\sts_bls_ina_06_ow.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\phases\sts_bls_ina_07.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\phases\sts_bls_ina_07_gpl.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\phases\sts_bls_ina_07_ow.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\phases\sts_bls_ina_08_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\phases\sts_bls_ina_08_gameplay.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\phases\sts_bls_ina_08_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\phases\sts_bls_ina_08_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\scenes\lipsync\en\sts_bls_ina_08_holocall_debriefs\dakota_smith.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\scenes\lipsync\en\sts_bls_ina_08_holocall_debriefs\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\scenes\lipsync\en\sts_bls_ina_08_holocall_prebrief\dakota_smith.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\scenes\lipsync\en\sts_bls_ina_08_holocall_prebrief\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\scenes\sts_bls_ina_08_holocall_debriefs.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\scenes\sts_bls_ina_08_holocall_prebrief.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_09\phases\sts_bls_ina_09.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_09\phases\sts_bls_ina_09_gameplay.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_09\phases\sts_bls_ina_09_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\phases\sts_bls_ina_11.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\phases\sts_bls_ina_11_gpl.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\phases\sts_bls_ina_11_ow.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `#ina_08_ready` | base\open_world\street_stories\badlands\inland_avenue\sts_bls_inland_avenue.questphase / h1332 / 10; 1 total source locations in compressed evidence |
| `bls_achievement` | base\open_world\bugfixing\fixers\dakota_bugfixing.questphase / h22 / 61; base\open_world\bugfixing\ma\ma_ina_south_bugfixing.questphase / h589 / 3; base\open_world\bugfixing\ma\ma_ina_south_bugfixing.questphase / h589 / 5; base\open_world\bugfixing\ma\ma_ina_south_bugfixing.questphase / h589 / 7; 32 total source locations in compressed evidence |
| `holo_active_call_interrupted` | base\quest\holocalls\holocall_interrupts.questphase / h0 / 100; base\quest\holocalls\holocall_interrupts.questphase / h0 / 104; base\quest\holocalls\holocall_interrupts.questphase / h0 / 115; base\quest\holocalls\holocall_interrupts.questphase / h0 / 118; 4 total source locations in compressed evidence |
| `holo_dakota_calls_v_end_activate` | base\open_world\fixers\dakota\phases\dakota.questphase / h0 / 63; base\open_world\fixers\dakota\scenes\dakota_smith_defaut.scene / scene / 295; base\open_world\street_stories\badlands\inland_avenue\sts_bls_inland_avenue.questphase / h413 / 346; base\open_world\street_stories\badlands\inland_avenue\sts_bls_inland_avenue.questphase / h1123 / 27; 57 total source locations in compressed evidence |
| `holo_dakota_calls_v_end_done` | base\open_world\fixers\dakota\scenes\dakota_smith_defaut.scene / scene / 291; base\quest\bugfixing\additional_content\holocall_bugfixing.questphase / h121 / 83; base\quest\holocalls\dakota\dakota_holocall.scene / scene / 42; base\quest\holocalls\dakota\dakota_holocall.scene / scene / 555; 21 total source locations in compressed evidence |
| `holo_dakota_calls_v_rejectable` | base\quest\holocalls\dakota\dakota_holocall.scene / scene / 634; base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_holocall_debriefs.scene / scene / 280; base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_holocall_prebrief.scene / scene / 254; base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_holocall_prebrief.scene / scene / 292; 25 total source locations in compressed evidence |
| `holo_dakota_calls_v_rejected` | base\quest\holocalls\dakota\dakota_holocall.scene / scene / 642; base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_holocall_debriefs.scene / scene / 284; base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_holocall_prebrief.scene / scene / 266; base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\scenes\sts_bls_ina_03_holocall_debriefs.scene / scene / 286; 17 total source locations in compressed evidence |
| `holo_dakota_calls_v_start_activate` | base\open_world\fixers\dakota\phases\dakota.questphase / h0 / 62; base\open_world\fixers\dakota\scenes\dakota_smith_defaut.scene / scene / 294; base\open_world\street_stories\badlands\inland_avenue\sts_bls_inland_avenue.questphase / h413 / 345; base\open_world\street_stories\badlands\inland_avenue\sts_bls_inland_avenue.questphase / h1123 / 26; 73 total source locations in compressed evidence |
| `holo_dakota_calls_v_start_done` | base\open_world\fixers\dakota\scenes\dakota_smith_defaut.scene / scene / 289; base\quest\bugfixing\additional_content\holocall_bugfixing.questphase / h121 / 82; base\quest\holocalls\dakota\dakota_holocall.scene / scene / 41; base\quest\holocalls\dakota\dakota_holocall.scene / scene / 580; 21 total source locations in compressed evidence |
| `holo_delamain_deep_vehicle_talk` | base\quest\side_quests\sq025\scenes\sq025_05_scan.scene / scene / 7532; base\quest\side_quests\sq025\scenes\sq025_05_scan.scene / scene / 7534; base\quest\side_quests\sq025\scenes\sq025_05_scan.scene / scene / 8471; base\quest\side_quests\sq025\scenes\sq025_05_scan.scene / scene / 8477; 6 total source locations in compressed evidence |
| `holo_interrupt_call` | base\quest\holocalls\holocall_initializers.questphase / h0 / 114; base\quest\holocalls\holocall_interrupts.questphase / h0 / 1; base\quest\holocalls\holocall_interrupts.questphase / h0 / 4; base\quest\holocalls\holocall_interrupts.questphase / h0 / 33; 8 total source locations in compressed evidence |
| `holo_setup_active` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 135; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 138; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 45; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 46; 972 total source locations in compressed evidence |
| `holo_setup_started` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 136; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 139; base\quest\bugfixing\part1\q112\q112_quest_bugfixes.questphase / h566 / 8; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 56; 469 total source locations in compressed evidence |
| `ina_08_failed` | base\open_world\street_stories\badlands\inland_avenue\sts_bls_inland_avenue.questphase / h413 / 360; 1 total source locations in compressed evidence |
| `ina_08_finished` | base\open_world\street_stories\badlands\inland_avenue\sts_bls_inland_avenue.questphase / h1123 / 24; 1 total source locations in compressed evidence |
| `ina_08_pickup_arrived` | base\open_world\street_stories\badlands\inland_avenue\sts_bls_inland_avenue.questphase / h978 / 209; 1 total source locations in compressed evidence |
| `ina_08_start` | base\open_world\street_stories\badlands\inland_avenue\sts_bls_inland_avenue.questphase / h413 / 300; 1 total source locations in compressed evidence |
| `ina_08_test_def` | base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\sts_bls_ina_08.quest / h0 / 28; 1 total source locations in compressed evidence |

NodeRef uses: 100; TweakDB binding uses: 11. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\scenes\sts_bls_ina_08_holocall_debriefs.scene` | 1 / 1 | scnDialogLineEvent: 1 |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_08\scenes\sts_bls_ina_08_holocall_prebrief.scene` | 1 / 3 | scnDialogLineEvent: 3 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
