# base-sts-wbr-hil-101

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_101\community\sts_wbr_hil_101.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_101\community\sts_wbr_hil_101_combat.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_101\scenes\sts_wbr_hil_101_chats.scene` | content candidate | 0 / 4 |  |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_101\sts_wbr_hil_101.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_101\sts_wbr_hil_101_test.gamedef` | content candidate | 0 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 1 |
| `scnEndNode[scnNodeId]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 1 |
| `scnStartNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `adb35b885aae85462082` | 1 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_101\scenes\sts_wbr_hil_101_chats.scene` / scene / 1 -> 7 -> 4 |
| `e3594d38b5cb466193f1` | 1 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_101\scenes\sts_wbr_hil_101_chats.scene` / scene / 7 -> 4 -> 2 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
