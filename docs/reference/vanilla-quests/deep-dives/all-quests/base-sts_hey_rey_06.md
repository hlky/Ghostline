# Gig: Jeopardy

Journal: `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06` · `StreetStory` · hash `1377965103`.

Journal premise: Gig type: Search and Recover\nObjective: Shard with daemon program\nLocation: La Catrina Crematorium, intersection of Phalarope and Plover St.\nDetails:\n\nI'd like you to commit a minor transgression against God and His people – disturbing the dead from their eternal rest.\n\nDeceased's name is Jim Greyer. He smuggled unstable shards by slotting them inside his head. Sadly, during his last transit things went sideways. The Daemon got out of its cage and barbecued his brain. Jim Greyer ended up in the La Catrina funeral home along with my client's shard.\n\nGo to La Catrina, find Greyer's body and get that shard before it's burnt to cinders. FYI – the crematorium's cozy with the Valentinos. That's where they get rid of their bodies. One wrong move and you'll end up there too.

**Coverage: journal-linked.** 72 exact journal-linked nodes in 5 resources; 9 resources in the inspected dependency context.

Resource roles in that context: 6 content candidate, 3 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: `base\open_world\district_definitions\open_world_kabuki.quest`; `base\open_world\open_world_test.quest`; `base\open_world\police_system\police_system_test.quest`. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Deposit the shard in the Drop Point. (Primary) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/drop` |
| Leave the crematorium. (Primary) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/escape` |
| Get inside the morgue. (Primary) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/find_body` |
| Find Jim Greyer's body. (Primary) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/find_body1` |
| Look for Jim Greyer's body in the morgue. (Primary) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/find_greyers_in_the_morgue` |
| Contract type Thievery\nGoal Retrieve the shard from Grayer’s head. \nLocation La Cartina Funeral House in Vista Del Rey . \n\nDetails My client worked with a Nomad mule, Jim Greyer. Contractor gave him a shard, which Greyer used to smuggle danger cybervirus. Unfortunately, during his last smuggling op, the security system malfunctioned, freezing Jim’s head before he even got to the Spaceport. Greyer’s body now lies in the morgue at the La Cartina Funeral Home (controlled by Valentinos) awaiting cremation. You have to retrieve shard form smuggler’s head.  (Primary) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/go_to_the_funeral_home` |
| Retrieve the infected shard. (Primary) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/main` |
| Find Jim Greyer using your scanner. (Primary) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/scan_the_bodies` |
| Pull the shard from Jim Greyer's body. (Primary) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/take_drugs` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `sts_vista_bugfixing.questphase / h208 / 13` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/find_body` | 11:True → 13:Inactive |
| `sts_hey_rey_06_openworld.questphase / h581 / 124` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/find_body` | 318:Out → 124:Active; 124:Out → 172:Inactive; 124:Out → 283:In |
| `sts_hey_rey_06_openworld.questphase / h581 / 125` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/go_to_the_funeral_home` | 128:Out → 125:Succeeded; 125:Out → 151:Active; 125:Out → 320:In |
| `sts_hey_rey_06_openworld.questphase / h581 / 129` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/take_drugs` | 190:Out → 129:Active; 129:Out → 159:In |
| `sts_hey_rey_06_openworld.questphase / h581 / 135` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/go_to_the_funeral_home` | 162:True → 135:Active; 135:Out → 161:In1 |
| `sts_hey_rey_06_openworld.questphase / h581 / 138` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/find_body` | 139:Out → 138:Succeeded; 138:Out → 194:Active |
| `sts_hey_rey_06_openworld.questphase / h581 / 141` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/escape` | 141:Out → 140:In; 226:Out → 141:Active; 227:False → 141:Active |
| `sts_hey_rey_06_openworld.questphase / h581 / 142` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/escape` | 140:Out → 142:Succeeded; 142:Out → 254:In |
| `sts_hey_rey_06_openworld.questphase / h581 / 145` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06` | 148:Out → 145:Succeeded; 145:Out → 267:In |
| `sts_hey_rey_06_openworld.questphase / h581 / 147` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/drop` | 313:Out → 147:Active; 147:Out → 202:In |
| `sts_hey_rey_06_openworld.questphase / h581 / 148` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/drop` | 148:Out → 145:Succeeded; 202:Out → 148:Succeeded |
| `sts_hey_rey_06_openworld.questphase / h581 / 151` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/find_body1` | 125:Out → 151:Active; 151:Out → 187:In; 151:Out → 283:In |
| `sts_hey_rey_06_openworld.questphase / h581 / 165` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/go_to_the_funeral_home` | 165:Out → 161:In2; 162:False → 165:Active |
| `sts_hey_rey_06_openworld.questphase / h581 / 170` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/brief` | 161:Out1 → 170:Active |
| `sts_hey_rey_06_openworld.questphase / h581 / 172` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/find_body1` | 124:Out → 172:Inactive; 172:Out → 139:In |
| `sts_hey_rey_06_openworld.questphase / h581 / 188` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/scan_the_bodies` | 188:Out → 159:In; 188:Out → 186:In; 306:Out → 188:Active; 188:Out → 212:In; 188:Out → 213:In; 188:Out → 214:In |
| `sts_hey_rey_06_openworld.questphase / h581 / 194` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/find_greyers_in_the_morgue` | 138:Out → 194:Active; 194:Out → 197:In |
| `sts_hey_rey_06_openworld.questphase / h581 / 196` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/find_greyers_in_the_morgue` | 197:Out → 196:Succeeded; 196:Out → 280:Succeeded |
| `sts_hey_rey_06_openworld.questphase / h581 / 215` (MappinManager) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/scan_the_bodies/mp_body_2` | 212:Out → 215:Inactive |
| `sts_hey_rey_06_openworld.questphase / h581 / 216` (MappinManager) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/scan_the_bodies/mp_body_3` | 213:Out → 216:Inactive |
| `sts_hey_rey_06_openworld.questphase / h581 / 217` (MappinManager) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/scan_the_bodies/mp_body_4` | 214:Out → 217:Inactive |
| `sts_hey_rey_06_openworld.questphase / h581 / 222` (MappinManager) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/scan_the_bodies/mp_body_1` | 186:Out → 222:Inactive; 222:Out → 305:In |
| `sts_hey_rey_06_openworld.questphase / h581 / 190` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/scan_the_bodies` | 190:Out → 129:Active; 262:Out → 190:Succeeded |
| `sts_hey_rey_06_openworld.questphase / h581 / 224` (Condition) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/take_drugs` | 159:Out → 224:In; 224:True → 225:Succeeded; 224:False → 227:In |
| `sts_hey_rey_06_openworld.questphase / h581 / 225` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/take_drugs` | 224:True → 225:Succeeded; 225:Out → 227:In |
| `sts_hey_rey_06_openworld.questphase / h581 / 226` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/scan_the_bodies` | 226:Out → 141:Active; 227:True → 226:Succeeded |
| `sts_hey_rey_06_openworld.questphase / h581 / 227` (Condition) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/scan_the_bodies` | 227:False → 141:Active; 224:False → 227:In; 225:Out → 227:In; 227:True → 226:Succeeded |
| `sts_hey_rey_06_openworld.questphase / h581 / 264` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/find_body1` | 263:Out → 264:Succeeded; 264:Out → 270:Active |
| `sts_hey_rey_06_openworld.questphase / h581 / 269` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/take_drugs` | 269:Out → 159:In; 274:Out → 269:Active |
| `sts_hey_rey_06_openworld.questphase / h581 / 270` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/find_body` | 264:Out → 270:Active; 270:Out → 271:In |
| `sts_hey_rey_06_openworld.questphase / h581 / 272` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/find_greyers_in_the_morgue` | 276:Out → 272:Active; 272:Out → 273:In |
| `sts_hey_rey_06_openworld.questphase / h581 / 274` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/find_greyers_in_the_morgue` | 274:Out → 269:Active; 273:Out → 274:Succeeded |
| `sts_hey_rey_06_openworld.questphase / h581 / 276` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/find_body` | 271:Out → 276:Succeeded; 276:Out → 272:Active |
| `sts_hey_rey_06_openworld.questphase / h581 / 280` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/find_body1` | 187:Out → 280:Succeeded; 196:Out → 280:Succeeded; 280:Out → 321:In |
| `sts_hey_rey_06_openworld.questphase / h581 / 322` (PauseCondition) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/find_body1` | 320:Out → 322:In; 322:Out → 323:In |
| `sts_hey_vista_del_rey.questphase / h863 / 124` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/find_body` | 318:Out → 124:Active; 124:Out → 172:Inactive; 124:Out → 283:In |
| `sts_hey_vista_del_rey.questphase / h863 / 125` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/go_to_the_funeral_home` | 128:Out → 125:Succeeded; 125:Out → 151:Active; 125:Out → 320:In |
| `sts_hey_vista_del_rey.questphase / h863 / 129` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/take_drugs` | 190:Out → 129:Active; 129:Out → 159:In |
| `sts_hey_vista_del_rey.questphase / h863 / 135` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/go_to_the_funeral_home` | 162:True → 135:Active; 135:Out → 161:In1 |
| `sts_hey_vista_del_rey.questphase / h863 / 138` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/find_body` | 139:Out → 138:Succeeded; 138:Out → 194:Active |
| `sts_hey_vista_del_rey.questphase / h863 / 141` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/escape` | 141:Out → 140:In; 226:Out → 141:Active; 227:False → 141:Active |
| `sts_hey_vista_del_rey.questphase / h863 / 142` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/escape` | 140:Out → 142:Succeeded; 142:Out → 254:In |
| `sts_hey_vista_del_rey.questphase / h863 / 145` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06` | 148:Out → 145:Succeeded; 145:Out → 267:In |
| `sts_hey_vista_del_rey.questphase / h863 / 147` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/drop` | 313:Out → 147:Active; 147:Out → 202:In |
| `sts_hey_vista_del_rey.questphase / h863 / 148` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/drop` | 148:Out → 145:Succeeded; 202:Out → 148:Succeeded |
| `sts_hey_vista_del_rey.questphase / h863 / 151` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/find_body1` | 125:Out → 151:Active; 151:Out → 187:In; 151:Out → 283:In |
| `sts_hey_vista_del_rey.questphase / h863 / 165` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/go_to_the_funeral_home` | 165:Out → 161:In2; 162:False → 165:Active |
| `sts_hey_vista_del_rey.questphase / h863 / 170` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/brief` | 161:Out1 → 170:Active |
| `sts_hey_vista_del_rey.questphase / h863 / 172` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/find_body1` | 124:Out → 172:Inactive; 172:Out → 139:In |
| `sts_hey_vista_del_rey.questphase / h863 / 188` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/scan_the_bodies` | 188:Out → 159:In; 188:Out → 186:In; 306:Out → 188:Active; 188:Out → 212:In; 188:Out → 213:In; 188:Out → 214:In |
| `sts_hey_vista_del_rey.questphase / h863 / 194` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/find_greyers_in_the_morgue` | 138:Out → 194:Active; 194:Out → 197:In |
| `sts_hey_vista_del_rey.questphase / h863 / 196` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/find_greyers_in_the_morgue` | 197:Out → 196:Succeeded; 196:Out → 280:Succeeded |
| `sts_hey_vista_del_rey.questphase / h863 / 215` (MappinManager) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/scan_the_bodies/mp_body_2` | 212:Out → 215:Inactive |
| `sts_hey_vista_del_rey.questphase / h863 / 216` (MappinManager) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/scan_the_bodies/mp_body_3` | 213:Out → 216:Inactive |
| `sts_hey_vista_del_rey.questphase / h863 / 217` (MappinManager) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/scan_the_bodies/mp_body_4` | 214:Out → 217:Inactive |
| `sts_hey_vista_del_rey.questphase / h863 / 222` (MappinManager) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/scan_the_bodies/mp_body_1` | 186:Out → 222:Inactive; 222:Out → 305:In |
| `sts_hey_vista_del_rey.questphase / h863 / 190` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/scan_the_bodies` | 190:Out → 129:Active; 262:Out → 190:Succeeded |
| `sts_hey_vista_del_rey.questphase / h863 / 224` (Condition) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/take_drugs` | 159:Out → 224:In; 224:True → 225:Succeeded; 224:False → 227:In |
| `sts_hey_vista_del_rey.questphase / h863 / 225` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/take_drugs` | 224:True → 225:Succeeded; 225:Out → 227:In |
| `sts_hey_vista_del_rey.questphase / h863 / 226` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/scan_the_bodies` | 226:Out → 141:Active; 227:True → 226:Succeeded |
| `sts_hey_vista_del_rey.questphase / h863 / 227` (Condition) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/scan_the_bodies` | 227:False → 141:Active; 224:False → 227:In; 225:Out → 227:In; 227:True → 226:Succeeded |
| `sts_hey_vista_del_rey.questphase / h863 / 264` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/find_body1` | 263:Out → 264:Succeeded; 264:Out → 270:Active |
| `sts_hey_vista_del_rey.questphase / h863 / 269` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/take_drugs` | 269:Out → 159:In; 274:Out → 269:Active |
| `sts_hey_vista_del_rey.questphase / h863 / 270` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/find_body` | 264:Out → 270:Active; 270:Out → 271:In |
| `sts_hey_vista_del_rey.questphase / h863 / 272` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/find_greyers_in_the_morgue` | 276:Out → 272:Active; 272:Out → 273:In |
| `sts_hey_vista_del_rey.questphase / h863 / 274` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/find_greyers_in_the_morgue` | 274:Out → 269:Active; 273:Out → 274:Succeeded |
| `sts_hey_vista_del_rey.questphase / h863 / 276` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/find_body` | 271:Out → 276:Succeeded; 276:Out → 272:Active |
| `sts_hey_vista_del_rey.questphase / h863 / 280` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/find_body1` | 187:Out → 280:Succeeded; 196:Out → 280:Succeeded; 280:Out → 321:In |
| `sts_hey_vista_del_rey.questphase / h863 / 322` (PauseCondition) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/find_body1` | 320:Out → 322:In; 322:Out → 323:In |
| `mq036_quest_bugfixes.questphase / h870 / 240` (Condition) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/drop` | 235:False → 240:In; 239:Out → 240:In; 240:True → 241:In; 240:False → 253:In |
| `open_world_bugfixing.questphase / h1127 / 16` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06` | 15:True → 16:Succeeded |
| `open_world_bugfixing.questphase / h2262 / 16` (Journal) | `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06` | 15:True → 16:Succeeded |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `sts_hey_rey_06_openworld.questphase / h168 / 23` | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\sts_hey_rey_06_civilians.scene`; `#sts_sm_hey_rey_06_civilians` | 43:Out → 23:rey_06_priest_chat_start |
| `sts_hey_rey_06_openworld.questphase / h168 / 24` | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\sts_hey_rey_06_receptionist.scene`; `#sts_sm_hey_rey_06_receptionist` | 50:CutSource → 24:CutDestination; 34:Out → 24:rey_06_receptionist_talk_start |
| `sts_hey_rey_06_openworld.questphase / h168 / 46` | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\sts_hey_rey_06_civilians.scene`; `#sts_sm_hey_rey_06_civilians` | 45:Out → 46:rey_06_hologram_start |
| `sts_hey_rey_06_openworld.questphase / h168 / 47` | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\sts_hey_rey_06_civilians.scene`; `#sts_sm_hey_rey_06_civilians` | 48:Out → 47:rey_06_civilian_002_chat_start |
| `sts_hey_rey_06_openworld.questphase / h307 / 55` | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\sts_hey_rey_06_holocall_debriefs.scene`; `#sts_sm_hey_rey_06_holocall_debriefs` | 55:End1 → 14:In; 76:False → 55:Start1; 55:rejected_out → 75:Active; 55:Holocall INT → 60:In; 55:Holocall RET → 59:In |
| `sts_hey_rey_06_openworld.questphase / h581 / 265` | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\sts_hey_rey_06_holocall_prebrief.scene`; `#sts_sm_hey_rey_06_holocall_prebrief` | 279:True → 265:Start1; 265:End1 → 266:Active; 265:rejected_out → 266:Active; 265:Holocall INT → 285:In; 265:Holocall RET → 284:In |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\quest\bugfixing\open_world_bugfixing.questphase` / h11 / 40 | `sts_vista_bugfixing.questphase` | 9: DeletionMarker; 9:Out → 40:In1 |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\sts_hey_rey_06.questphase` / h0 / 198 | `sts_hey_rey_06_openworld.questphase` | 0: Input; 0:Out → 198:In1; 198:Out1 → 1:In |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase` / h9034 / 198 | `sts_hey_rey_06_openworld.questphase` | 0: Input; 0:Out → 198:In1; 198:Out1 → 1:In |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\phases\sts_hey_rey_06_openworld.questphase` / h168 / 23 | `sts_hey_rey_06_civilians.scene` | 43: PauseCondition: #rey_06_tr_priest; 43:Out → 23:rey_06_priest_chat_start |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\phases\sts_hey_rey_06_openworld.questphase` / h168 / 46 | `sts_hey_rey_06_civilians.scene` | 45: PauseCondition: rey_06_holo_hack; 45:Out → 46:rey_06_hologram_start |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\phases\sts_hey_rey_06_openworld.questphase` / h168 / 47 | `sts_hey_rey_06_civilians.scene` | 48: PauseCondition: #rey_06_tr_dead_body; 48:Out → 47:rey_06_civilian_002_chat_start |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase` / h450 / 23 | `sts_hey_rey_06_civilians.scene` | 43: PauseCondition: #rey_06_tr_priest; 43:Out → 23:rey_06_priest_chat_start |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase` / h450 / 46 | `sts_hey_rey_06_civilians.scene` | 45: PauseCondition: rey_06_holo_hack; 45:Out → 46:rey_06_hologram_start |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase` / h450 / 47 | `sts_hey_rey_06_civilians.scene` | 48: PauseCondition: #rey_06_tr_dead_body; 48:Out → 47:rey_06_civilian_002_chat_start |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\phases\sts_hey_rey_06_openworld.questphase` / h307 / 55 | `sts_hey_rey_06_holocall_debriefs.scene` | 76: Condition; 55:End1 → 14:In; 76:False → 55:Start1; 55:rejected_out → 75:Active; 55:Holocall INT → 60:In; 55:Holocall RET → 59:In |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase` / h589 / 55 | `sts_hey_rey_06_holocall_debriefs.scene` | 76: Condition; 55:End1 → 14:In; 76:False → 55:Start1; 55:rejected_out → 75:Active; 55:Holocall INT → 60:In; 55:Holocall RET → 59:In |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\phases\sts_hey_rey_06_openworld.questphase` / h581 / 265 | `sts_hey_rey_06_holocall_prebrief.scene` | 279: Condition; 279:True → 265:Start1; 265:End1 → 266:Active; 265:rejected_out → 266:Active; 265:Holocall INT → 285:In; 265:Holocall RET → 284:In |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase` / h863 / 265 | `sts_hey_rey_06_holocall_prebrief.scene` | 279: Condition; 279:True → 265:Start1; 265:End1 → 266:Active; 265:rejected_out → 266:Active; 265:Holocall INT → 285:In; 265:Holocall RET → 284:In |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\phases\sts_hey_rey_06_openworld.questphase` / h168 / 24 | `sts_hey_rey_06_receptionist.scene` | 50: CutControl; 34: PauseCondition: {"seconds": 2}; 50:CutSource → 24:CutDestination; 34:Out → 24:rey_06_receptionist_talk_start |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase` / h450 / 24 | `sts_hey_rey_06_receptionist.scene` | 50: CutControl; 34: PauseCondition: {"seconds": 2}; 50:CutSource → 24:CutDestination; 34:Out → 24:rey_06_receptionist_talk_start |
| `base\open_world\street_stories\heywood\sts_heywood.questphase` / h0 / 3 | `sts_hey_vista_del_rey.questphase` | 0: Input; 5: Input; 0:Out → 3:In1; 5:Out → 3:sts_hey_rey_02_bugfixing |
| `base\quest\bugfixing\quest_bugfixing.questphase` / h233 / 54 | `mq036_quest_bugfixes.questphase` | 20: LogicalHub; 20:Out1 → 54:In1 |
| `base\quest\bugfixing.questphase` / h0 / 11 | `open_world_bugfixing.questphase` | 16: DeletionMarker; 16:Out → 11:In1 |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\sts_hey_rey_06_quest.quest` / h0 / 62 | `sts_hey_rey_06.questphase` | 63: FactsDBManager: rey_06_journal_test; 62:Out1 → 2:In; 63:Out → 62:In1 |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase` / h0 / 7 | `sts_hey_rey_06.questphase` | 61: Journal; 61:Out → 7:In1 |
| `base\open_world\street_stories\street_stories.questphase` / h0 / 4 | `sts_heywood.questphase` | 0: Input; 21: Input; 0:Out → 4:In1; 21:Out → 4:sts_hey_rey_02_bugfixing |
| `base\quest\bugfixing.questphase` / h0 / 9 | `quest_bugfixing.questphase` | 16: DeletionMarker; 9:Out_res_act1 → 20:In; 16:Out → 9:In1; 9:to_mq025 → 55:In |
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
| `base\open_world\community\heywood\wellsprings\hey_spr_quest.quest` / h0 / 4 | `street_stories.questphase` | 1: Start; 1:Out → 4:In1 |
| `base\open_world\community\westbrook\charter_hill\wbr_hil_com_test.quest` / h0 / 21 | `street_stories.questphase` | 0: Start; 0:Out → 21:In1 |
| `base\open_world\phases\open_world_content.questphase` / h0 / 2 | `street_stories.questphase` | 33: PauseCondition: sts_loop_start; 122: Input; 33:Out → 2:In1; 122:Out → 2:In1 |
| `base\quest\cyberpunk2077.quest` / h0 / 2 | `cyberpunk2077.questphase` | 0: Start; 0:Out → 2:Start |
| `base\quest\demos\handson_2020\handson_2020.quest` / h0 / 33 | `cyberpunk2077.questphase` | 34: FactsDBManager: e3_2020; 34:Out → 33:Start |
| `base\quest\demos\handson_2020\handson_2020_testing.quest` / h0 / 5 | `cyberpunk2077.questphase` | 6: FactsDBManager: e3_2020; 6:Out → 5:Testing |
| `ep1\quest\cyberpunk2077_ep1_standalone.quest` / h0 / 1 | `cyberpunk2077.questphase` | 2: Start; 2:Out → 1:EP1_Standalone |
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
| `sts_hey_rey_06_civilians.scene` | rey_06_hologram_start, rey_06_priest_chat_start, rey_06_civilian_002_chat_start → rey_06_priest_chat_end, rey_06_hologram_end, rey_06_civilian_002_chat_end | prayer_001; priest; prayer_002; V; 15 nodes / 15 edges |
| `sts_hey_rey_06_holocall_debriefs.scene` | Start1 → rejected_out, End1 | fixer; v; 23 nodes / 30 edges |
| `sts_hey_rey_06_holocall_prebrief.scene` | Start1 → End1, rejected_out | fixer; v; 22 nodes / 25 edges |
| `sts_hey_rey_06_receptionist.scene` | rey_06_receptionist_talk_start →  | receptionist; V; 14 nodes / 15 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `sts_hey_rey_06_receptionist.scene / n203 / 0` | Got any special offers? (``) | No option-level predicate stored | 0:0 → 204:0:0 |
| `sts_hey_rey_06_receptionist.scene / n203 / 1` | I'm from the Greyer family. (``) | No option-level predicate stored | 0:1 → 79:0:0 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `glossary_valentinos` | sts_hey_rey_06_openworld.questphase / h12 / 69 | No reader in selected context |
| `hey_achievement` | sts_hey_rey_06_openworld.questphase / h307 / 28 | sts_hey_rey_06_openworld.questphase / h307 / 65 |
| `holo_active_call_interrupted` | Producer outside selected context | sts_hey_rey_06_holocall_prebrief.scene / scene / 280 |
| `holo_padre_calls_v_end_activate` | sts_hey_rey_06_holocall_debriefs.scene / scene / 105; sts_hey_rey_06_holocall_prebrief.scene / scene / 103; sts_hey_rey_06_openworld.questphase / h307 / 60; sts_hey_rey_06_openworld.questphase / h581 / 285 | No reader in selected context |
| `holo_padre_calls_v_end_done` | sts_hey_rey_06_holocall_debriefs.scene / scene / 101; sts_hey_rey_06_holocall_prebrief.scene / scene / 99 | sts_hey_rey_06_holocall_debriefs.scene / scene / 100; sts_hey_rey_06_holocall_prebrief.scene / scene / 98 |
| `holo_padre_calls_v_rejectable` | sts_hey_rey_06_holocall_debriefs.scene / scene / 283; sts_hey_rey_06_holocall_prebrief.scene / scene / 256; sts_hey_rey_06_holocall_prebrief.scene / scene / 286 | No reader in selected context |
| `holo_padre_calls_v_rejected` | sts_hey_rey_06_holocall_debriefs.scene / scene / 287; sts_hey_rey_06_holocall_prebrief.scene / scene / 260 | sts_hey_rey_06_holocall_debriefs.scene / scene / 285; sts_hey_rey_06_holocall_prebrief.scene / scene / 258 |
| `holo_padre_calls_v_start_activate` | sts_hey_rey_06_holocall_debriefs.scene / scene / 104; sts_hey_rey_06_holocall_debriefs.scene / scene / 261; sts_hey_rey_06_holocall_prebrief.scene / scene / 102; sts_hey_rey_06_holocall_prebrief.scene / scene / 284; sts_hey_rey_06_openworld.questphase / h307 / 59; sts_hey_rey_06_openworld.questphase / h581 / 284 | sts_hey_rey_06_holocall_debriefs.scene / scene / 253 |
| `holo_padre_calls_v_start_done` | sts_hey_rey_06_holocall_debriefs.scene / scene / 99; sts_hey_rey_06_holocall_prebrief.scene / scene / 97 | sts_hey_rey_06_holocall_debriefs.scene / scene / 272; sts_hey_rey_06_holocall_prebrief.scene / scene / 267 |
| `holo_setup_active` | Producer outside selected context | sts_hey_rey_06_holocall_debriefs.scene / scene / 253; sts_hey_rey_06_holocall_prebrief.scene / scene / 280 |
| `holo_setup_started` | Producer outside selected context | sts_hey_rey_06_holocall_debriefs.scene / scene / 253; sts_hey_rey_06_holocall_prebrief.scene / scene / 280 |
| `rey_06_com_ready` | sts_hey_rey_06_openworld.questphase / h307 / 62 | No reader in selected context |
| `rey_06_finished` | sts_hey_rey_06_openworld.questphase / h307 / 57 | open_world_bugfixing.questphase / h1127 / 15; open_world_bugfixing.questphase / h2262 / 15 |
| `rey_06_go_to_the_morgue` | sts_hey_rey_06_receptionist.scene / scene / 216 | sts_hey_rey_06_openworld.questphase / h581 / 318; sts_hey_vista_del_rey.questphase / h863 / 318; sts_vista_bugfixing.questphase / h208 / 11 |
| `rey_06_holo_hack` | Producer outside selected context | sts_hey_rey_06_openworld.questphase / h168 / 45 |
| `rey_06_journal_test` | Producer outside selected context | sts_hey_rey_06_openworld.questphase / h581 / 162; sts_hey_vista_del_rey.questphase / h863 / 162 |
| `rey_06_start` | sts_hey_rey_06_openworld.questphase / h12 / 68 | No reader in selected context |
| `sts_hey_rey_06_shard` | Producer outside selected context | sts_hey_rey_06_openworld.questphase / h581 / 202; sts_hey_vista_del_rey.questphase / h863 / 202 |

## Exact gates, joins and cancellation

<details><summary>103 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `sts_vista_bugfixing.questphase / h208 / 11` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"rey_06_go_to_the_morgue"}}}` | 4:Out → 11:In; 11:True → 13:Inactive |
| `sts_hey_rey_06_openworld.questphase / h12 / 45` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#rey_06_spwn_fluff_hearse"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 43:Out → 45:In; 45:Out → 64:In |
| `sts_hey_rey_06_openworld.questphase / h12 / 60` | `questLogicalAndNodeDefinition` `{"inputSocketCount":5}` | 60:Out1 → 43:In; 54:Out → 60:In1; 55:Out → 60:In2; 56:Out → 60:In3; 57:Out → 60:In4; 58:Out → 60:In5 |
| `sts_hey_rey_06_openworld.questphase / h12 / 79` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#rey_06_tr_sts_start"},{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PlayerSubType","vehicleComparisonType":"NotEqual","vehicleState":"Driving"}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PlayerSubType","vehicleComparisonType":"NotEqual","vehicleState":"Passenger"}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleScene","inverted":true}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleSceneFpp","inverted":true}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleSceneFppOnlyForward","inverted":true}}]}}` | 79:Out → 66:In; 80:Out → 79:In |
| `sts_hey_rey_06_openworld.questphase / h154 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#rey_06_dvc_security_system","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsSystemInCombat"}}}` | 0:Out → 12:In; 12:Out → 1:In |
| `sts_hey_rey_06_openworld.questphase / h168 / 34` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 34:Out → 24:rey_06_receptionist_talk_start; 37:Out → 34:In |
| `sts_hey_rey_06_openworld.questphase / h168 / 37` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rey_06_tr_receptionist_talking"}}` | 0:Out → 37:In; 37:Out → 34:In |
| `sts_hey_rey_06_openworld.questphase / h168 / 38` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rey_06_tr_funeral_disturb_voiceseset"}}` | 0:Out → 38:In; 38:Out → 41:In |
| `sts_hey_rey_06_openworld.questphase / h168 / 41` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 38:Out → 41:In; 41:Out → 39:In |
| `sts_hey_rey_06_openworld.questphase / h168 / 42` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 39:Out → 42:In; 42:Out → 40:In |
| `sts_hey_rey_06_openworld.questphase / h168 / 43` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rey_06_tr_priest"}}` | 0:Out → 43:In; 43:Out → 23:rey_06_priest_chat_start |
| `sts_hey_rey_06_openworld.questphase / h168 / 45` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"rey_06_holo_hack"}}}` | 0:Out → 45:In; 45:Out → 46:rey_06_hologram_start |
| `sts_hey_rey_06_openworld.questphase / h168 / 48` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rey_06_tr_dead_body"}}` | 0:Out → 48:In; 48:Out → 47:rey_06_civilian_002_chat_start |
| `sts_hey_rey_06_openworld.questphase / h168 / 49` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#rey_06_com","names":["receptionist"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 0:Out → 49:In; 49:Out → 50:In |
| `sts_hey_rey_06_openworld.questphase / h168 / 50` | `questCutControlNodeDefinition` `{}` | 50:CutSource → 24:CutDestination; 49:Out → 50:In |
| `sts_hey_rey_06_openworld.questphase / h307 / 32` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#rey_06_tr_sms_trigger"}}` | 36:Out → 32:In; 32:Out → 54:In; 32:Out → 53:In; 32:Out → 52:In; 32:Out → 51:In; 32:Out → 50:In |
| `sts_hey_rey_06_openworld.questphase / h307 / 36` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","days":1}}}` | 36:Out → 32:In; 56:Out → 36:In |
| `sts_hey_rey_06_openworld.questphase / h307 / 58` | `questLogicalAndNodeDefinition` `{"inputSocketCount":5}` | 15:Out → 58:In1; 16:Out → 58:In2; 17:Out → 58:In3; 18:Out → 58:In4; 19:Out → 58:In5; 58:Out1 → 29:In; 58:Out1 → 30:In; 58:Out1 → 31:In; 58:Out1 → 34:In; 58:Out1 → 35:In |
| `sts_hey_rey_06_openworld.questphase / h307 / 70` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\heywood\\vista_del_rey\\sts_hey_rey_06\\scenes\\sts_hey_rey_06_holocall_debriefs.scene","Flags":"Soft"},"type":"IsOutside"}}}` | 70:Out → 1:In; 64:Out → 70:In |
| `sts_hey_rey_06_openworld.questphase / h307 / 74` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 73:Out → 74:In; 74:Out → 76:In |
| `sts_hey_rey_06_openworld.questphase / h307 / 76` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}}}` | 76:False → 55:Start1; 74:Out → 76:In; 76:True → 75:Active |
| `sts_hey_rey_06_openworld.questphase / h581 / 128` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rey_06_tr_funeral_001"}}` | 128:Out → 125:Succeeded; 161:Out1 → 128:In; 128:Out → 286:In; 128:Out → 295:In; 128:Out → 287:In |
| `sts_hey_rey_06_openworld.questphase / h581 / 139` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rey_06_tr_morgue"}}` | 139:Out → 138:Succeeded; 172:Out → 139:In |
| `sts_hey_rey_06_openworld.questphase / h581 / 140` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#rey_06_tr_funeral_001"}}` | 141:Out → 140:In; 140:Out → 142:Succeeded |
| `sts_hey_rey_06_openworld.questphase / h581 / 159` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"115548629546","comparisonType":"Greater"}}}` | 129:Out → 159:In; 269:Out → 159:In; 188:Out → 159:In; 159:Out → 231:In; 159:Out → 224:In; 159:Out → 228:In |
| `sts_hey_rey_06_openworld.questphase / h581 / 161` | `questLogicalXorNodeDefinition` `{}` | 161:Out1 → 128:In; 135:Out → 161:In1; 165:Out → 161:In2; 161:Out1 → 170:Active |
| `sts_hey_rey_06_openworld.questphase / h581 / 162` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"rey_06_journal_test"}}}` | 0:Out → 162:In; 162:True → 135:Active; 162:False → 165:Active |
| `sts_hey_rey_06_openworld.questphase / h581 / 186` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#rey_06_ws_body"},"eventType":"Finished"}}}` | 263:CutSource → 186:CutDestination; 188:Out → 186:In; 186:Out → 222:Inactive |
| `sts_hey_rey_06_openworld.questphase / h581 / 187` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rey_06_tr_bodies_room"}}` | 151:Out → 187:In; 187:Out → 280:Succeeded |
| `sts_hey_rey_06_openworld.questphase / h581 / 197` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rey_06_tr_bodies_room"}}` | 194:Out → 197:In; 197:Out → 196:Succeeded |
| `sts_hey_rey_06_openworld.questphase / h581 / 202` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_hey_rey_06_shard"}}}` | 147:Out → 202:In; 202:Out → 148:Succeeded |
| `sts_hey_rey_06_openworld.questphase / h581 / 212` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#rey_06_ws_body_01"},"eventType":"Finished"}}}` | 188:Out → 212:In; 212:Out → 215:Inactive |
| `sts_hey_rey_06_openworld.questphase / h581 / 213` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#rey_06_ws_body_02"},"eventType":"Finished"}}}` | 188:Out → 213:In; 213:Out → 216:Inactive |
| `sts_hey_rey_06_openworld.questphase / h581 / 214` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#rey_06_ws_body_03"},"eventType":"Finished"}}}` | 188:Out → 214:In; 214:Out → 217:Inactive |
| `sts_hey_rey_06_openworld.questphase / h581 / 224` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/take_drugs","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 159:Out → 224:In; 224:True → 225:Succeeded; 224:False → 227:In |
| `sts_hey_rey_06_openworld.questphase / h581 / 227` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/scan_the_bodies","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 227:False → 141:Active; 224:False → 227:In; 225:Out → 227:In; 227:True → 226:Succeeded |
| `sts_hey_rey_06_openworld.questphase / h581 / 256` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rey_06_tr_sts_start"}}` | 266:Out → 256:In; 310:Out → 256:In; 256:Out → 311:In |
| `sts_hey_rey_06_openworld.questphase / h581 / 257` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#rey_06_tr_sts_start"}}` | 309:Out → 257:In; 257:Out → 312:In |
| `sts_hey_rey_06_openworld.questphase / h581 / 262` | `questCutControlNodeDefinition` `{}` | 262:Out → 190:Succeeded; 305:Out → 262:In; 262:CutSource → 283:CutDestination |
| `sts_hey_rey_06_openworld.questphase / h581 / 263` | `questCutControlNodeDefinition` `{}` | 263:CutSource → 186:CutDestination; 283:Out → 263:In; 263:Out → 264:Succeeded |
| `sts_hey_rey_06_openworld.questphase / h581 / 267` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 145:Out → 267:In; 267:Out → 315:In |
| `sts_hey_rey_06_openworld.questphase / h581 / 271` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rey_06_tr_morgue"}}` | 270:Out → 271:In; 271:Out → 276:Succeeded |
| `sts_hey_rey_06_openworld.questphase / h581 / 273` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rey_06_tr_bodies_room"}}` | 272:Out → 273:In; 273:Out → 274:Succeeded |
| `sts_hey_rey_06_openworld.questphase / h581 / 279` | `questConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 279:True → 265:Start1; 279:False → 266:Active; 324:False → 279:In |
| `sts_hey_rey_06_openworld.questphase / h581 / 283` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#rey_06_ws_body"},"eventType":"Finished"}},{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#rey_06_tr_morgue"}]}}` | 124:Out → 283:In; 151:Out → 283:In; 262:CutSource → 283:CutDestination; 283:Out → 263:In |
| `sts_hey_rey_06_openworld.questphase / h581 / 287` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rey_06_tr_guards_passed"}}` | 128:Out → 287:In; 287:Out → 288:In |
| `sts_hey_rey_06_openworld.questphase / h581 / 289` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#arr_05_dvc_security_system","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsSystemInCombat"}}}` | 0:Out → 289:In; 298:Out → 289:In; 289:Out → 291:In |
| `sts_hey_rey_06_openworld.questphase / h581 / 295` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#rey_06_tr_funeral_001"}}` | 128:Out → 295:In; 295:Out → 296:In |
| `sts_hey_rey_06_openworld.questphase / h581 / 297` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#arr_05_dvc_security_system","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsSystemSafe"}}}` | 291:Out → 297:In; 297:Out → 298:In |
| `sts_hey_rey_06_openworld.questphase / h581 / 315` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\heywood\\vista_del_rey\\sts_hey_rey_06\\scenes\\sts_hey_rey_06_holocall_prebrief.scene","Flags":"Soft"},"type":"IsOutside"}}}` | 315:Out → 1:In; 267:Out → 315:In |
| `sts_hey_rey_06_openworld.questphase / h581 / 318` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"rey_06_go_to_the_morgue"}}}` | 318:Out → 124:Active; 321:CutSource → 318:CutDestination; 323:CutSource → 318:CutDestination; 320:Out → 318:In |
| `sts_hey_rey_06_openworld.questphase / h581 / 321` | `questCutControlNodeDefinition` `{}` | 280:Out → 321:In; 321:Out → 306:In; 321:CutSource → 318:CutDestination |
| `sts_hey_rey_06_openworld.questphase / h581 / 322` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/find_body1","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 320:Out → 322:In; 322:Out → 323:In |
| `sts_hey_rey_06_openworld.questphase / h581 / 323` | `questCutControlNodeDefinition` `{}` | 323:CutSource → 318:CutDestination; 322:Out → 323:In |
| `sts_hey_rey_06_openworld.questphase / h581 / 324` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}}}` | 0:Out → 324:In; 324:True → 266:Active; 324:False → 279:In |
| `sts_hey_rey_06_civilians.scene / scene / 208` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":25}}}` | 207:0:0 → 208:0:1; 208:0:0 → 241:0:1 |
| `sts_hey_rey_06_civilians.scene / scene / 216` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneInterrupt_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\heywood\\vista_del_rey\\sts_hey_rey_06\\scenes\\sts_hey_rey_06_civilians.scene","Flags":"Soft"},"interruptConditions":[{"$type":"scnCheckSpeakerDistractedInterruptCondition"}]}}}` | 186:0:0 → 216:0:1; 216:0:0 → 244:0:0 |
| `sts_hey_rey_06_civilians.scene / scene / 217` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneInterrupt_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\heywood\\vista_del_rey\\sts_hey_rey_06\\scenes\\sts_hey_rey_06_civilians.scene","Flags":"Soft"},"interruptConditions":[{"$type":"scnCheckSpeakerDistractedInterruptCondition"}]}}}` | 193:0:0 → 217:0:1; 217:0:0 → 194:0:0 |
| `sts_hey_rey_06_civilians.scene / scene / 257` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneInterrupt_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\heywood\\vista_del_rey\\sts_hey_rey_06\\scenes\\sts_hey_rey_06_civilians.scene","Flags":"Soft"},"interruptConditions":[{"$type":"scnCheckSpeakerDistractedInterruptCondition"}]}}}` | 243:0:0 → 257:0:1; 257:0:0 → 205:0:0 |
| `sts_hey_rey_06_holocall_debriefs.scene / scene / 100` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_padre_calls_v_end_done"}}}` | 100:0:0 → 101:0:1; 105:0:0 → 100:0:1 |
| `sts_hey_rey_06_holocall_debriefs.scene / scene / 251` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2,"miliseconds":500}}}` | 98:666:0 → 251:0:1; 251:0:0 → 253:0:1; 259:0:0 → 251:0:1; 263:1:0 → 251:0:0; 263:1:0 → 251:1026:0 |
| `sts_hey_rey_06_holocall_debriefs.scene / scene / 253` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_padre_calls_v_start_activate","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 251:0:0 → 253:0:1; 253:0:0 → 255:0:1; 263:1:0 → 253:0:0; 263:1:0 → 253:1026:0 |
| `sts_hey_rey_06_holocall_debriefs.scene / scene / 255` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2,"miliseconds":500}}}` | 253:0:0 → 255:0:1; 255:0:0 → 257:0:1; 263:1:0 → 255:0:0; 263:1:0 → 255:1026:0 |
| `sts_hey_rey_06_holocall_debriefs.scene / scene / 257` | `questConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 255:0:0 → 257:0:1; 257:0:0 → 261:0:1; 257:0:1 → 259:0:0 |
| `sts_hey_rey_06_holocall_debriefs.scene / scene / 272` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_padre_calls_v_start_done"}}}` | 98:666:0 → 272:0:1; 272:0:0 → 263:0:0 |
| `sts_hey_rey_06_holocall_debriefs.scene / scene / 285` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_padre_calls_v_rejected"}}}` | 104:0:0 → 285:0:1; 285:0:0 → 287:0:1 |
| `sts_hey_rey_06_holocall_prebrief.scene / scene / 98` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_padre_calls_v_end_done"}}}` | 98:0:0 → 99:0:1; 103:0:0 → 98:0:1 |
| `sts_hey_rey_06_holocall_prebrief.scene / scene / 258` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_padre_calls_v_rejected"}}}` | 102:0:0 → 258:0:1; 258:0:0 → 260:0:1 |
| `sts_hey_rey_06_holocall_prebrief.scene / scene / 267` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_padre_calls_v_start_done"}}}` | 96:666:0 → 267:0:1; 267:0:0 → 270:0:0 |
| `sts_hey_rey_06_holocall_prebrief.scene / scene / 273` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":30}}}` | 96:666:0 → 273:0:1; 270:1:0 → 273:0:0; 273:0:0 → 280:0:1 |
| `sts_hey_rey_06_holocall_prebrief.scene / scene / 280` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_active_call_interrupted","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 273:0:0 → 280:0:1; 280:0:0 → 286:0:1; 280:0:1 → 282:0:1; 282:0:0 → 280:0:1 |
| `sts_hey_rey_06_holocall_prebrief.scene / scene / 282` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 270:1:0 → 282:0:0; 280:0:1 → 282:0:1; 282:0:0 → 280:0:1 |
| `sts_hey_vista_del_rey.questphase / h863 / 128` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rey_06_tr_funeral_001"}}` | 128:Out → 125:Succeeded; 161:Out1 → 128:In; 128:Out → 286:In; 128:Out → 295:In; 128:Out → 287:In |
| `sts_hey_vista_del_rey.questphase / h863 / 139` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rey_06_tr_morgue"}}` | 139:Out → 138:Succeeded; 172:Out → 139:In |
| `sts_hey_vista_del_rey.questphase / h863 / 140` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#rey_06_tr_funeral_001"}}` | 141:Out → 140:In; 140:Out → 142:Succeeded |
| `sts_hey_vista_del_rey.questphase / h863 / 159` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"115548629546","comparisonType":"Greater"}}}` | 129:Out → 159:In; 269:Out → 159:In; 188:Out → 159:In; 159:Out → 231:In; 159:Out → 224:In; 159:Out → 228:In |
| `sts_hey_vista_del_rey.questphase / h863 / 161` | `questLogicalXorNodeDefinition` `{}` | 161:Out1 → 128:In; 135:Out → 161:In1; 165:Out → 161:In2; 161:Out1 → 170:Active |
| `sts_hey_vista_del_rey.questphase / h863 / 162` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"rey_06_journal_test"}}}` | 0:Out → 162:In; 162:True → 135:Active; 162:False → 165:Active |
| `sts_hey_vista_del_rey.questphase / h863 / 186` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#rey_06_ws_body"},"eventType":"Finished"}}}` | 263:CutSource → 186:CutDestination; 188:Out → 186:In; 186:Out → 222:Inactive |
| `sts_hey_vista_del_rey.questphase / h863 / 187` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rey_06_tr_bodies_room"}}` | 151:Out → 187:In; 187:Out → 280:Succeeded |
| `sts_hey_vista_del_rey.questphase / h863 / 197` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rey_06_tr_bodies_room"}}` | 194:Out → 197:In; 197:Out → 196:Succeeded |
| `sts_hey_vista_del_rey.questphase / h863 / 202` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_hey_rey_06_shard"}}}` | 147:Out → 202:In; 202:Out → 148:Succeeded |
| `sts_hey_vista_del_rey.questphase / h863 / 212` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#rey_06_ws_body_01"},"eventType":"Finished"}}}` | 188:Out → 212:In; 212:Out → 215:Inactive |
| `sts_hey_vista_del_rey.questphase / h863 / 213` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#rey_06_ws_body_02"},"eventType":"Finished"}}}` | 188:Out → 213:In; 213:Out → 216:Inactive |
| `sts_hey_vista_del_rey.questphase / h863 / 214` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#rey_06_ws_body_03"},"eventType":"Finished"}}}` | 188:Out → 214:In; 214:Out → 217:Inactive |
| `sts_hey_vista_del_rey.questphase / h863 / 224` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/take_drugs","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 159:Out → 224:In; 224:True → 225:Succeeded; 224:False → 227:In |
| `sts_hey_vista_del_rey.questphase / h863 / 227` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/scan_the_bodies","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 227:False → 141:Active; 224:False → 227:In; 225:Out → 227:In; 227:True → 226:Succeeded |
| `sts_hey_vista_del_rey.questphase / h863 / 262` | `questCutControlNodeDefinition` `{}` | 262:Out → 190:Succeeded; 305:Out → 262:In; 262:CutSource → 283:CutDestination |
| `sts_hey_vista_del_rey.questphase / h863 / 263` | `questCutControlNodeDefinition` `{}` | 263:CutSource → 186:CutDestination; 283:Out → 263:In; 263:Out → 264:Succeeded |
| `sts_hey_vista_del_rey.questphase / h863 / 267` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 145:Out → 267:In; 267:Out → 315:In |
| `sts_hey_vista_del_rey.questphase / h863 / 271` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rey_06_tr_morgue"}}` | 270:Out → 271:In; 271:Out → 276:Succeeded |
| `sts_hey_vista_del_rey.questphase / h863 / 273` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#rey_06_tr_bodies_room"}}` | 272:Out → 273:In; 273:Out → 274:Succeeded |
| `sts_hey_vista_del_rey.questphase / h863 / 283` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#rey_06_ws_body"},"eventType":"Finished"}},{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#rey_06_tr_morgue"}]}}` | 124:Out → 283:In; 151:Out → 283:In; 262:CutSource → 283:CutDestination; 283:Out → 263:In |
| `sts_hey_vista_del_rey.questphase / h863 / 318` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"rey_06_go_to_the_morgue"}}}` | 318:Out → 124:Active; 321:CutSource → 318:CutDestination; 323:CutSource → 318:CutDestination; 320:Out → 318:In |
| `sts_hey_vista_del_rey.questphase / h863 / 321` | `questCutControlNodeDefinition` `{}` | 280:Out → 321:In; 321:Out → 306:In; 321:CutSource → 318:CutDestination |
| `sts_hey_vista_del_rey.questphase / h863 / 322` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/find_body1","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 320:Out → 322:In; 322:Out → 323:In |
| `sts_hey_vista_del_rey.questphase / h863 / 323` | `questCutControlNodeDefinition` `{}` | 323:CutSource → 318:CutDestination; 322:Out → 323:In |
| `mq036_quest_bugfixes.questphase / h870 / 235` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/leave_device_in_droppoint","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 228:False → 235:In; 234:Out → 235:In; 235:True → 236:In; 235:False → 240:In |
| `mq036_quest_bugfixes.questphase / h870 / 240` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/drop","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 235:False → 240:In; 239:Out → 240:In; 240:True → 241:In; 240:False → 253:In |
| `mq036_quest_bugfixes.questphase / h870 / 241` | `questConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"115548629546","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 240:True → 241:In; 241:True → 244:In; 241:False → 242:In |
| `mq036_quest_bugfixes.questphase / h870 / 253` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/watson/northside_industrial_district/sts_wat_nid_04/sts_wat_nid_04/get_to_droppoint","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 240:False → 253:In; 245:Out → 253:In; 253:True → 254:In; 253:False → 259:In |
| `open_world_bugfixing.questphase / h1127 / 15` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"rey_06_finished"}}}` | 0:Out → 15:In; 15:True → 16:Succeeded |
| `open_world_bugfixing.questphase / h2262 / 15` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"rey_06_finished"}}}` | 0:Out → 15:In; 15:True → 16:Succeeded |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | sts_hey_rey_06_openworld.questphase / h12 / 45 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `checkpoint` | sts_hey_rey_06_openworld.questphase / h12 / 66; sts_hey_rey_06_openworld.questphase / h307 / 56 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `choice_gate` | sts_hey_rey_06_receptionist.scene / scene / 203 | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `community_lifecycle` | sts_hey_rey_06_civilians.scene / scene / 207; sts_hey_rey_06_civilians.scene / scene / 241; sts_hey_rey_06_openworld.questphase / h12 / 64; sts_hey_rey_06_openworld.questphase / h12 / 74; +2 locations in catalogue.json | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | open_world_bugfixing.questphase / h1127 / 15; open_world_bugfixing.questphase / h2262 / 15; sts_hey_rey_06_holocall_debriefs.scene / scene / 100; sts_hey_rey_06_holocall_debriefs.scene / scene / 253; +14 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | sts_hey_rey_06_openworld.questphase / h307 / 27; sts_hey_rey_06_openworld.questphase / h307 / 67; sts_hey_rey_06_openworld.questphase / h581 / 309; sts_hey_rey_06_openworld.questphase / h581 / 310; +2 locations in catalogue.json | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `controller_event` | mq036_quest_bugfixes.questphase / h870 / 239; sts_hey_rey_06_openworld.questphase / h307 / 29; sts_hey_rey_06_openworld.questphase / h307 / 30; sts_hey_rey_06_openworld.questphase / h307 / 31; +9 locations in catalogue.json | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `device_action` | sts_hey_rey_06_openworld.questphase / h12 / 54; sts_hey_rey_06_openworld.questphase / h12 / 55; sts_hey_rey_06_openworld.questphase / h12 / 56; sts_hey_rey_06_openworld.questphase / h12 / 57; +11 locations in catalogue.json | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `device_state` | sts_hey_rey_06_openworld.questphase / h154 / 12; sts_hey_rey_06_openworld.questphase / h581 / 289; sts_hey_rey_06_openworld.questphase / h581 / 297 | controller class + object + condition function → device predicate. Check already-satisfied state and controller persistence across save/load. |
| `elapsed_time` | sts_hey_rey_06_openworld.questphase / h307 / 36 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `item_state` | mq036_quest_bugfixes.questphase / h870 / 241; sts_hey_rey_06_openworld.questphase / h581 / 159; sts_hey_vista_del_rey.questphase / h863 / 159 | item ID + entity + quantity/comparison → ownership predicate. Ownership alone does not prove reading, device interaction or reward delivery. |
| `journal_transition` | open_world_bugfixing.questphase / h1127 / 16; open_world_bugfixing.questphase / h2262 / 16; sts_hey_rey_06_openworld.questphase / h12 / 81; sts_hey_rey_06_openworld.questphase / h307 / 75; +58 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `parallel_join` | sts_hey_rey_06_openworld.questphase / h12 / 60; sts_hey_rey_06_openworld.questphase / h307 / 58 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | sts_hey_rey_06_holocall_debriefs.scene / scene / 101; sts_hey_rey_06_holocall_debriefs.scene / scene / 104; sts_hey_rey_06_holocall_debriefs.scene / scene / 105; sts_hey_rey_06_holocall_debriefs.scene / scene / 261; +21 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | sts_hey_rey_06_openworld.questphase / h581 / 161; sts_hey_vista_del_rey.questphase / h863 / 161 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | sts_hey_rey_06_civilians.scene / scene / 208; sts_hey_rey_06_holocall_debriefs.scene / scene / 251; sts_hey_rey_06_holocall_debriefs.scene / scene / 255; sts_hey_rey_06_holocall_prebrief.scene / scene / 273; +7 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | sts_hey_rey_06_openworld.questphase / h168 / 50; sts_hey_rey_06_openworld.questphase / h581 / 262; sts_hey_rey_06_openworld.questphase / h581 / 263; sts_hey_rey_06_openworld.questphase / h581 / 321; +5 locations in catalogue.json | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `reward_commit` | sts_hey_rey_06_openworld.questphase / h307 / 14 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scan_evidence` | sts_hey_rey_06_openworld.questphase / h581 / 186; sts_hey_rey_06_openworld.questphase / h581 / 212; sts_hey_rey_06_openworld.questphase / h581 / 213; sts_hey_rey_06_openworld.questphase / h581 / 214; +6 locations in catalogue.json | clue reference + exact scan event + required-set policy → clue observed. Preserve Started versus Finished, ordering, bypass and reaction joins. |
| `scene_interface` | sts_hey_rey_06_openworld.questphase / h168 / 23; sts_hey_rey_06_openworld.questphase / h168 / 24; sts_hey_rey_06_openworld.questphase / h168 / 46; sts_hey_rey_06_openworld.questphase / h168 / 47; +2 locations in catalogue.json | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | sts_hey_rey_06_openworld.questphase / h12 / 79; sts_hey_rey_06_openworld.questphase / h168 / 37; sts_hey_rey_06_openworld.questphase / h168 / 38; sts_hey_rey_06_openworld.questphase / h168 / 43; +22 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `target_resolution` | sts_hey_rey_06_openworld.questphase / h168 / 49 | target set + lethal/unconscious/defeated policy → target resolved. Review RED defaults, early defeat and per-target deduplication before counter joins. |
| `workspot_performance` | sts_hey_rey_06_receptionist.scene / scene / 219; sts_hey_rey_06_receptionist.scene / scene / 225; sts_hey_rey_06_receptionist.scene / scene / 226; sts_hey_rey_06_receptionist.scene / scene / 227; +4 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\open_world\bugfixing\sts\sts_vista_bugfixing.questphase` | repair; journal anchor | `base-shared` |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\phases\sts_hey_rey_06_openworld.questphase` | content candidate; journal anchor | `base-sts-hey-rey-06` |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\sts_hey_rey_06_civilians.scene` | content candidate; forward dependency | `base-sts-hey-rey-06` |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\sts_hey_rey_06_holocall_debriefs.scene` | content candidate; forward dependency | `base-sts-hey-rey-06` |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\sts_hey_rey_06_holocall_prebrief.scene` | content candidate; forward dependency | `base-sts-hey-rey-06` |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\sts_hey_rey_06_receptionist.scene` | content candidate; forward dependency | `base-sts-hey-rey-06` |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase` | content candidate; journal anchor | `base-shared` |
| `base\quest\bugfixing\minor_quests\mq036\mq036_quest_bugfixes.questphase` | repair; journal anchor | `base-mq036` |
| `base\quest\bugfixing\open_world_bugfixing.questphase` | repair; journal anchor | `base-shared` |

Evidence shards for this dossier (including parent context): [base-ma-bls-ina-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-07.json.gz), [base-ma-bls-ina-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-08.json.gz), [base-ma-bls-ina-se1-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-se1-22.json.gz), [base-ma-cct-dtn-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-03.json.gz), [base-ma-cct-dtn-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-07.json.gz), [base-ma-hey-spr-04](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-04.json.gz), [base-ma-hey-spr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-06.json.gz), [base-ma-pac-cvi-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-08.json.gz), [base-ma-pac-cvi-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-15.json.gz), [base-ma-std-arr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-arr-06.json.gz), [base-ma-std-rcr-11](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-rcr-11.json.gz), [base-ma-wat-kab-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-02.json.gz), [base-ma-wat-kab-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-08.json.gz), [base-ma-wat-lch-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-lch-06.json.gz), [base-ma-wat-nid-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-03.json.gz), [base-ma-wat-nid-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-15.json.gz), [base-ma-wat-nid-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-22.json.gz), [base-mq000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq000.json.gz), [base-mq001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq001.json.gz), [base-mq003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq003.json.gz), [base-mq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq006.json.gz), [base-mq007](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq007.json.gz), [base-mq008](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq008.json.gz), [base-mq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq011.json.gz), [base-mq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq012.json.gz), [base-mq013](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq013.json.gz), [base-mq014](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq014.json.gz), [base-mq015](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq015.json.gz), [base-mq016](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq016.json.gz), [base-mq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq017.json.gz), [base-mq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq018.json.gz), [base-mq019](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq019.json.gz), [base-mq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq021.json.gz), [base-mq022](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq022.json.gz), [base-mq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq023.json.gz), [base-mq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq024.json.gz), [base-mq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq025.json.gz), [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-mq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq028.json.gz), [base-mq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq030.json.gz), [base-mq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq032.json.gz), [base-mq033](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq033.json.gz), [base-mq035](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq035.json.gz), [base-mq036](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq036.json.gz), [base-mq037](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq037.json.gz), [base-mq038](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq038.json.gz), [base-mq040](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq040.json.gz), [base-mq041](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq041.json.gz), [base-mq048](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq048.json.gz), [base-mq055](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq055.json.gz), [base-mws-wat-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mws-wat-08.json.gz), [base-q000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q000.json.gz), [base-q001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q001.json.gz), [base-q003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q003.json.gz), [base-q004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q004.json.gz), [base-q005](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q005.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q103](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q103.json.gz), [base-q105](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q105.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q113](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q113.json.gz), [base-q114](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q114.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-q202](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q202.json.gz), [base-q203](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q203.json.gz), [base-q204](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q204.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq004.json.gz), [base-sq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq006.json.gz), [base-sq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq011.json.gz), [base-sq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq012.json.gz), [base-sq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq017.json.gz), [base-sq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq018.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq024.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq026.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [base-sq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq028.json.gz), [base-sq029](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq029.json.gz), [base-sq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq030.json.gz), [base-sq031](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq031.json.gz), [base-sq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq032.json.gz), [base-sts-hey-rey-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-hey-rey-02.json.gz), [base-sts-hey-rey-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-hey-rey-06.json.gz), [base-ue-metro](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ue-metro.json.gz), [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

218 repeated typed/socket path signatures in this selected graph context; 34 distinct direct resource identities; 5 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `598920ee48558917ab4e` | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\phases\sts_hey_rey_06_openworld.questphase` / h12 / 66 -> 69 -> 68 | questCheckpointNodeDefinition -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; Out -> In |
| `e5742f9794e6583c67cb` | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\sts_hey_rey_06_holocall_debriefs.scene` / scene / 105 -> 100 -> 101 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `1d933adb5a617880c93e` | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\sts_hey_rey_06_holocall_debriefs.scene` / scene / 103 -> 105 -> 100 | scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `d6b7c21f5d2d0ab76fc6` | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\sts_hey_rey_06_holocall_debriefs.scene` / scene / 100 -> 101 -> 97 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnEndNode[scnNodeId]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `26762f051e7728f090ca` | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\sts_hey_rey_06_holocall_debriefs.scene` / scene / 99 -> 102 -> 26 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `101b60945ddf6f25f378` | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\sts_hey_rey_06_holocall_debriefs.scene` / scene / 26 -> 103 -> 105 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:0; 0:0 -> 0:1 |
| `8cd3b647ae3f592ad947` | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\sts_hey_rey_06_civilians.scene` / scene / 186 -> 149 -> 244 | scnStartNode[scnNodeId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnEndNode[scnNodeId]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `9e5e28ecb38ea2a53a15` | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\sts_hey_rey_06_holocall_debriefs.scene` / scene / 283 -> 104 -> 285 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `2beeeaa3b4da5300c035` | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\sts_hey_rey_06_holocall_debriefs.scene` / scene / 96 -> 283 -> 104 | scnStartNode[scnNodeId] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `4e9253a72e6b0134b8dd` | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\phases\sts_hey_rey_06_openworld.questphase` / h581 / 128 -> 125 -> 151 | questPauseConditionNodeDefinition[questTriggerCondition] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Succeeded; Out -> Active |
| `bbf9efd740881cf31a37` | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\sts_hey_rey_06_holocall_debriefs.scene` / scene / 272 -> 263 -> 251 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> scnCutControlNode[scnNodeId] -> questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]; 0:0 -> 0:0; 1:0 -> 0:0 |
| `d5cbf4acf851cb8612b3` | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\sts_hey_rey_06_holocall_prebrief.scene` / scene / 286 -> 284 -> 254 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnEndNode[scnNodeId]; 0:0 -> 0:1; 0:0 -> 0:0 |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\phases\sts_hey_rey_06_openworld.questphase` / h0 / 2 | `h12` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\phases\sts_hey_rey_06_openworld.questphase` / h0 / 3 | `h154` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\phases\sts_hey_rey_06_openworld.questphase` / h154 / 11 | `h168` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\phases\sts_hey_rey_06_openworld.questphase` / h0 / 4 | `h307` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\phases\sts_hey_rey_06_openworld.questphase` / h0 / 5 | `h581` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

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
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.gamedef` | content candidate | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.quest |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02_test.gamedef` | content candidate | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.quest |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\sts_hey_rey_06.gamedef` | content candidate | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\sts_hey_rey_06_quest.quest |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\sts_hey_rey_06_test.gamedef` | content candidate | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\sts_hey_rey_06_quest.quest |
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
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_average_female_transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_female_average__sit_chair_lean180__2h_on_lap__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_female_average__stand__2h_back__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_01\phases\sts_hey_rey_01.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_01\phases\sts_hey_rey_01_gameplay.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_01\phases\sts_hey_rey_01_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_gameplay.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_open_world.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\phases\sts_hey_rey_06_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\phases\sts_hey_rey_06_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\lipsync\en\sts_hey_rey_06_civilians\civ_high_m_13_mex_40.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\lipsync\en\sts_hey_rey_06_civilians\civ_low_f_68_mex_20.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\lipsync\en\sts_hey_rey_06_civilians\civ_low_f_75_mex_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\lipsync\en\sts_hey_rey_06_civilians\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\lipsync\en\sts_hey_rey_06_holocall_debriefs\sebastian_padre_perez.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\lipsync\en\sts_hey_rey_06_holocall_debriefs\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\lipsync\en\sts_hey_rey_06_holocall_prebrief\sebastian_padre_perez.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\lipsync\en\sts_hey_rey_06_holocall_prebrief\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\lipsync\en\sts_hey_rey_06_receptionist\civ_low_f_69_mex_25.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\lipsync\en\sts_hey_rey_06_receptionist\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\sts_hey_rey_06_civilians.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\sts_hey_rey_06_holocall_debriefs.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\sts_hey_rey_06_holocall_prebrief.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\sts_hey_rey_06_receptionist.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\sts_hey_rey_06.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_08\sts_hey_rey_08.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_08\sts_hey_rey_08_gameplay.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_08\sts_hey_rey_08_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_09\phases\sts_hey_rey_09.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_09\phases\sts_hey_rey_09_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_09\phases\sts_hey_rey_09_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\workspots\common\chair\generic__sit_chair__sit_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__stand_around__05.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `glossary_valentinos` | base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase / h479 / 45; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase / h294 / 69; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase / h6436 / 74; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase / h6919 / 161; 13 total source locations in compressed evidence |
| `hey_achievement` | base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_02\ma_hey_spr_02_phase.questphase / h0 / 42; base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_03\ma_hey_spr_03_phase.questphase / h0 / 34; base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06_bugfixing.questphase / h89 / 8; base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_10\ma_hey_spr_10_phase.questphase / h0 / 40; 32 total source locations in compressed evidence |
| `holo_active_call_interrupted` | base\quest\holocalls\holocall_interrupts.questphase / h0 / 100; base\quest\holocalls\holocall_interrupts.questphase / h0 / 104; base\quest\holocalls\holocall_interrupts.questphase / h0 / 115; base\quest\holocalls\holocall_interrupts.questphase / h0 / 118; 4 total source locations in compressed evidence |
| `holo_padre_calls_v_end_activate` | base\open_world\fixers\padre\phases\padre.questphase / h0 / 54; base\open_world\fixers\padre\scenes\padre_default.scene / scene / 148; base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase / h479 / 145; base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase / h479 / 146; 77 total source locations in compressed evidence |
| `holo_padre_calls_v_end_done` | base\open_world\fixers\padre\scenes\padre_default.scene / scene / 144; base\quest\bugfixing\additional_content\holocall_bugfixing.questphase / h121 / 213; base\quest\holocalls\padre\padre_holocall.scene / scene / 42; base\quest\holocalls\padre\padre_holocall.scene / scene / 541; 24 total source locations in compressed evidence |
| `holo_padre_calls_v_rejectable` | base\quest\holocalls\padre\padre_holocall.scene / scene / 664; base\open_world\street_stories\heywood\glenn\sts_hey_gle_01\scenes\sts_hey_gle_01_holocall_debriefs.scene / scene / 283; base\open_world\street_stories\heywood\glenn\sts_hey_gle_01\scenes\sts_hey_gle_01_holocall_prebrief.scene / scene / 269; base\open_world\street_stories\heywood\glenn\sts_hey_gle_01\scenes\sts_hey_gle_01_holocall_prebrief.scene / scene / 308; 30 total source locations in compressed evidence |
| `holo_padre_calls_v_rejected` | base\quest\holocalls\padre\padre_holocall.scene / scene / 672; base\open_world\street_stories\heywood\glenn\sts_hey_gle_01\scenes\sts_hey_gle_01_holocall_debriefs.scene / scene / 287; base\open_world\street_stories\heywood\glenn\sts_hey_gle_01\scenes\sts_hey_gle_01_holocall_prebrief.scene / scene / 273; base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\scenes\sts_hey_gle_03_holocall_debriefs.scene / scene / 289; 20 total source locations in compressed evidence |
| `holo_padre_calls_v_start_activate` | base\open_world\fixers\padre\phases\padre.questphase / h0 / 53; base\open_world\fixers\padre\scenes\padre_default.scene / scene / 147; base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase / h479 / 141; base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase / h479 / 143; 93 total source locations in compressed evidence |
| `holo_padre_calls_v_start_done` | base\open_world\fixers\padre\scenes\padre_default.scene / scene / 142; base\quest\bugfixing\additional_content\holocall_bugfixing.questphase / h121 / 212; base\quest\holocalls\padre\padre_holocall.scene / scene / 41; base\quest\holocalls\padre\padre_holocall.scene / scene / 527; 24 total source locations in compressed evidence |
| `holo_setup_active` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 135; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 138; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 45; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 46; 972 total source locations in compressed evidence |
| `holo_setup_started` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 136; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 139; base\quest\bugfixing\part1\q112\q112_quest_bugfixes.questphase / h566 / 8; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 56; 469 total source locations in compressed evidence |
| `rey_06_com_ready` | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase / h589 / 62; 1 total source locations in compressed evidence |
| `rey_06_finished` | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase / h589 / 57; 1 total source locations in compressed evidence |
| `rey_06_holo_hack` | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase / h10156 / 49; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\phases\sts_hey_rey_06_combat.questphase / h236 / 49; 2 total source locations in compressed evidence |
| `rey_06_journal_test` | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\sts_hey_rey_06_quest.quest / h0 / 63; 1 total source locations in compressed evidence |
| `rey_06_start` | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase / h294 / 68; 1 total source locations in compressed evidence |

NodeRef uses: 124; TweakDB binding uses: 18. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\sts_hey_rey_06_civilians.scene` | 3 / 6 | scnDialogLineEvent: 6 |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\sts_hey_rey_06_holocall_debriefs.scene` | 1 / 2 | scnDialogLineEvent: 2 |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\sts_hey_rey_06_holocall_prebrief.scene` | 1 / 2 | scnDialogLineEvent: 2 |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\sts_hey_rey_06_receptionist.scene` | 3 / 36 | scnChangeIdleAnimEvent: 7; scnDialogLineEvent: 9; scnLookAtEvent: 6; scnPlaySkAnimEvent: 6; scneventsSocket: 8 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
