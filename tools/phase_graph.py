"""Quest graph primitives shared by typed stages and proven template generators.

Handle construction deliberately embeds destinations before referring back to them.
Keep this importer ordering independent of any particular quest's content.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

JsonObject = dict[str, Any]


def cname(value: str) -> JsonObject:
    return {"$type": "CName", "$storage": "string", "$value": value}


def node_ref(value: str, *, storage: str = "string") -> JsonObject:
    return {"$type": "NodeRef", "$storage": storage, "$value": value}


def tweakdbid(value: str) -> JsonObject:
    return {"$type": "TweakDBID", "$storage": "string", "$value": value}


def entity_reference(
    reference: str | None = None, *, names: Iterable[str] = ()
) -> JsonObject:
    """Return a vanilla entity reference, optionally scoped to named entries."""

    return {
        "$type": "gameEntityReference",
        "dynamicEntityUniqueName": cname("None"),
        "names": [cname(name) for name in names],
        "reference": (
            node_ref(reference)
            if reference is not None
            else node_ref("0", storage="uint64")
        ),
        "sceneActorContextName": cname("None"),
        "slotName": cname("None"),
        "type": "EntityRef",
    }


def local_player_reference(builder: "PhaseGraphBuilder") -> JsonObject:
    """Return the vanilla questUniversalRef form for the local player."""

    return builder.handles.wrap(
        {
            "$type": "questUniversalRef",
            "entityReference": entity_reference(),
            "mainPlayerObject": 0,
            "refLocalPlayer": 1,
        }
    )


class Handles:
    """Allocate deterministic CR2W handle IDs."""

    def __init__(self) -> None:
        self._next = 0

    def reserve(self) -> str:
        handle_id = str(self._next)
        self._next += 1
        return handle_id

    @staticmethod
    def define(handle_id: str, data: JsonObject) -> JsonObject:
        return {"HandleId": handle_id, "Data": data}

    def wrap(self, data: JsonObject) -> JsonObject:
        return self.define(self.reserve(), data)

    @staticmethod
    def ref(handle: JsonObject | str) -> JsonObject:
        handle_id = handle if isinstance(handle, str) else handle["HandleId"]
        return {"HandleRefId": handle_id}


@dataclass
class GraphNode:
    wrapper: JsonObject
    inputs: dict[str, JsonObject]
    outputs: dict[str, JsonObject]

    @property
    def data(self) -> JsonObject:
        return self.wrapper["Data"]


class PhaseGraphBuilder:
    def __init__(self) -> None:
        self.handles = Handles()
        graph_handle = self.handles.reserve()
        self.graph = self.handles.define(
            graph_handle,
            {"$type": "questGraphDefinition", "nodes": []},
        )

    def socket(self, name: str, socket_type: str) -> JsonObject:
        return self.handles.wrap(
            {
                "$type": "questSocketDefinition",
                "connections": [],
                "name": cname(name),
                "type": socket_type,
            }
        )

    def node(
        self,
        quest_id: int,
        node_type: str,
        *,
        input_names: Iterable[str],
        output_names: Iterable[str] = ("Out",),
        properties: JsonObject | None = None,
    ) -> GraphNode:
        handle_id = self.handles.reserve()
        cut = self.socket("CutDestination", "CutDestination")
        inputs = {name: self.socket(name, "Input") for name in input_names}
        outputs = {name: self.socket(name, "Output") for name in output_names}
        data: JsonObject = {
            "$type": node_type,
            "id": quest_id,
            "sockets": [cut, *inputs.values(), *outputs.values()],
        }
        if properties:
            data.update(properties)
        wrapper = self.handles.define(handle_id, data)
        result = GraphNode(wrapper, inputs, outputs)
        self.graph["Data"]["nodes"].append(wrapper)
        return result

    @staticmethod
    def _replace_socket(
        node: GraphNode, socket: JsonObject, replacement: JsonObject
    ) -> None:
        sockets = node.data["sockets"]
        index = next(
            index for index, candidate in enumerate(sockets) if candidate is socket
        )
        sockets[index] = replacement

    def connect(
        self,
        source: GraphNode,
        destination: GraphNode,
        *,
        source_socket: str = "Out",
        destination_socket: str = "In",
    ) -> None:
        """Connect a node to a later node using WolvenKit's forward embedding."""

        source_handle = source.outputs[source_socket]
        destination_handle = destination.inputs[destination_socket]
        destination_is_inline = any(
            candidate is destination_handle for candidate in destination.data["sockets"]
        )
        connection_id = self.handles.reserve()
        destination_handle["Data"]["connections"].append(
            self.handles.ref(connection_id)
        )
        connection = self.handles.define(
            connection_id,
            {
                "$type": "graphGraphConnectionDefinition",
                "destination": (
                    destination_handle
                    if destination_is_inline
                    else self.handles.ref(destination_handle)
                ),
                "source": self.handles.ref(source_handle),
            },
        )
        source_handle["Data"]["connections"].append(connection)
        if destination_is_inline:
            self._replace_socket(
                destination,
                destination_handle,
                self.handles.ref(destination_handle),
            )

    def connect_to_earlier_output(
        self,
        source: GraphNode,
        output_node: GraphNode,
        *,
        source_socket: str = "Out",
    ) -> None:
        """Connect the final node to the conventionally second Output node."""

        source_handle = source.outputs[source_socket]
        destination_handle = output_node.inputs["In"]
        connection_id = self.handles.reserve()
        source_handle["Data"]["connections"].append(self.handles.ref(connection_id))
        connection = self.handles.define(
            connection_id,
            {
                "$type": "graphGraphConnectionDefinition",
                "destination": self.handles.ref(destination_handle),
                "source": source_handle,
            },
        )
        destination_handle["Data"]["connections"].append(connection)
        self._replace_socket(source, source_handle, self.handles.ref(source_handle))

    def connect_to_earlier_input(
        self,
        source: GraphNode,
        destination: GraphNode,
        *,
        source_socket: str = "Out",
        destination_socket: str = "In",
    ) -> None:
        """Connect a later node to an input socket owned by an earlier node."""

        source_handle = source.outputs[source_socket]
        destination_handle = destination.inputs[destination_socket]
        connection_id = self.handles.reserve()
        source_handle["Data"]["connections"].append(self.handles.ref(connection_id))
        connection = self.handles.define(
            connection_id,
            {
                "$type": "graphGraphConnectionDefinition",
                "destination": self.handles.ref(destination_handle),
                "source": source_handle,
            },
        )
        destination_handle["Data"]["connections"].append(connection)
        self._replace_socket(source, source_handle, self.handles.ref(source_handle))


def input_node(builder: PhaseGraphBuilder) -> GraphNode:
    return builder.node(
        0,
        "questInputNodeDefinition",
        input_names=(),
        properties={"socketName": cname("In1")},
    )


def output_node(builder: PhaseGraphBuilder) -> GraphNode:
    return builder.node(
        1,
        "questOutputNodeDefinition",
        input_names=("In",),
        output_names=(),
        properties={"socketName": cname("Out1"), "type": "Terminating"},
    )


def journal_path(
    builder: PhaseGraphBuilder, real_path: str, class_name: str, index: int
) -> JsonObject:
    return builder.handles.wrap(
        {
            "$type": "gameJournalPath",
            "className": cname(class_name),
            "editorPath": "",
            "fileEntryIndex": index,
            "realPath": real_path,
        }
    )


def objective_node(builder: PhaseGraphBuilder, quest_id: int, path: str) -> GraphNode:
    node_type = builder.handles.wrap(
        {
            "$type": "questJournalQuestEntry_NodeType",
            "optional": 0,
            "path": journal_path(builder, path, "gameJournalQuestObjective", 2),
            "sendNotification": 1,
            "trackQuest": 1,
            "version": "Initial",
        }
    )
    return builder.node(
        quest_id,
        "questJournalNodeDefinition",
        input_names=("Active", "Inactive", "Succeeded", "Failed"),
        properties={"type": node_type},
    )


def journal_entry_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    path: str,
    class_name: str,
    file_index: int,
) -> GraphNode:
    node_type = builder.handles.wrap(
        {
            "$type": "questJournalEntry_NodeType",
            "path": journal_path(builder, path, class_name, file_index),
            "sendNotification": 1,
        }
    )
    return builder.node(
        quest_id,
        "questJournalNodeDefinition",
        input_names=("Active", "Inactive"),
        properties={"type": node_type},
    )


def mappin_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    path: str,
    *,
    disable_previous_mappins: bool = False,
) -> GraphNode:
    return builder.node(
        quest_id,
        "questMappinManagerNodeDefinition",
        input_names=("Active", "Inactive"),
        properties={
            "disablePreviousMappins": int(disable_previous_mappins),
            "path": journal_path(builder, path, "gameJournalQuestMapPin", 2),
        },
    )


def fact_node(builder: PhaseGraphBuilder, quest_id: int, fact_name: str) -> GraphNode:
    fact_type = builder.handles.wrap(
        {
            "$type": "questSetVar_NodeType",
            "factName": fact_name,
            "setExactValue": 1,
            "value": 1,
        }
    )
    return builder.node(
        quest_id,
        "questFactsDBManagerNodeDefinition",
        input_names=("In",),
        properties={"type": fact_type},
    )


def logical_and_node(
    builder: PhaseGraphBuilder, quest_id: int, input_count: int
) -> GraphNode:
    input_names = tuple(f"In{index}" for index in range(1, input_count + 1))
    return builder.node(
        quest_id,
        "questLogicalAndNodeDefinition",
        input_names=input_names,
        output_names=("Out1",),
        properties={
            "inputSocketCount": input_count,
            "outputSocketCount": 1,
        },
    )


def trigger_condition_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    trigger_ref: str,
    condition_type: str,
) -> GraphNode:
    condition = builder.handles.wrap(
        {
            "$type": "questTriggerCondition",
            "activatorRef": entity_reference(),
            "isPlayerActivator": 1,
            "triggerAreaRef": node_ref(trigger_ref),
            "type": condition_type,
        }
    )
    return builder.node(
        quest_id,
        "questPauseConditionNodeDefinition",
        input_names=("In",),
        properties={"condition": condition},
    )


def realtime_delay_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    *,
    seconds: int = 1,
    milliseconds: int = 0,
) -> GraphNode:
    condition_type = builder.handles.wrap(
        {
            "$type": "questRealtimeDelay_ConditionType",
            "hours": 0,
            "miliseconds": milliseconds,
            "minutes": 0,
            "seconds": seconds,
        }
    )
    condition = builder.handles.wrap(
        {"$type": "questTimeCondition", "type": condition_type}
    )
    return builder.node(
        quest_id,
        "questPauseConditionNodeDefinition",
        input_names=("In",),
        properties={"condition": condition},
    )


def inventory_condition_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    item_id: str,
    *,
    quantity: int = 1,
) -> GraphNode:
    """Wait until the local player owns at least ``quantity`` of an item."""

    condition_type = builder.handles.wrap(
        {
            "$type": "questInventory_ConditionType",
            "comparisonType": "GreaterOrEqual",
            "isPlayer": 1,
            "itemID": tweakdbid(item_id),
            "itemTag": cname("None"),
            "objectRef": entity_reference(),
            "quantity": quantity,
        }
    )
    condition = builder.handles.wrap(
        {"$type": "questObjectCondition", "type": condition_type}
    )
    return builder.node(
        quest_id,
        "questPauseConditionNodeDefinition",
        input_names=("In",),
        properties={"condition": condition},
    )


def fact_condition_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    fact_name: str,
    *,
    comparison: str = "Greater",
    value: int = 0,
) -> GraphNode:
    condition_type = builder.handles.wrap(
        {
            "$type": "questVarComparison_ConditionType",
            "comparisonType": comparison,
            "factName": fact_name,
            "value": value,
        }
    )
    condition = builder.handles.wrap(
        {"$type": "questFactsDBCondition", "type": condition_type}
    )
    return builder.node(
        quest_id,
        "questPauseConditionNodeDefinition",
        input_names=("In",),
        properties={"condition": condition},
    )


def _empty_action_widget_package() -> JsonObject:
    """Return the inherited action defaults serialized by vanilla drop points."""

    return {
        "$type": "SActionWidgetPackage",
        "action": None,
        "bckgroundTextureID": {
            "$type": "TweakDBID",
            "$storage": "uint64",
            "$value": "0",
        },
        "customData": None,
        "dependendActions": [],
        "displayName": "",
        "iconID": cname("None"),
        "iconTextureID": {
            "$type": "TweakDBID",
            "$storage": "uint64",
            "$value": "0",
        },
        "isValid": 1,
        "isWidgetInactive": 0,
        "libraryID": cname("None"),
        "libraryPath": {
            "$type": "redResourceReferenceScriptToken",
            "resource": {
                "DepotPath": {
                    "$type": "ResourcePath",
                    "$storage": "uint64",
                    "$value": "0",
                },
                "Flags": "Soft",
            },
        },
        "orientation": "Horizontal",
        "ownerID": {
            "$type": "gamePersistentID",
            "componentName": cname("None"),
            "entityHash": "0",
        },
        "ownerIDClassName": cname("None"),
        "placement": "DOCKED",
        "textData": None,
        "wasInitalized": 0,
        "widget": None,
        "widgetName": "",
        "widgetState": "DEFAULT",
        "widgetTweakDBID": {
            "$type": "TweakDBID",
            "$storage": "uint64",
            "$value": "0",
        },
    }


def _empty_interaction_choice() -> JsonObject:
    return {
        "$type": "gameinteractionsChoice",
        "caption": "",
        "captionParts": {
            "$type": "gameinteractionsChoiceCaption",
            "parts": [],
        },
        "choiceMetaData": {
            "$type": "gameinteractionsChoiceMetaData",
            "tweakDBID": {
                "$type": "TweakDBID",
                "$storage": "uint64",
                "$value": "0",
            },
            "tweakDBName": "",
            "type": {
                "$type": "gameinteractionsChoiceTypeWrapper",
                "properties": 0,
            },
        },
        "data": [],
        "doNotTurnOffPreventionSystem": 0,
        "lookAtDescriptor": {
            "$type": "gameinteractionsChoiceLookAtDescriptor",
            "offset": {"$type": "Vector3", "X": 0, "Y": 0, "Z": 0},
            "orbId": {"$type": "gameinteractionsOrbID", "id": 0},
            "slotName": cname("None"),
            "type": "Root",
        },
    }


def reserve_drop_point_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    item_id: str,
    drop_point_ref: str,
) -> GraphNode:
    """Reserve one quest item to a live vanilla drop-point controller."""

    event = builder.handles.wrap(
        {
            "$type": "ReserveItemToThisDropPoint",
            "actionName": cname("None"),
            "actionWidgetPackage": _empty_action_widget_package(),
            "activationTimeReduction": 0,
            "activeStatusEffect": {
                "$type": "TweakDBID",
                "$storage": "uint64",
                "$value": "0",
            },
            "attachedProgram": {
                "$type": "TweakDBID",
                "$storage": "uint64",
                "$value": "0",
            },
            "calculatedBaseCost": 0,
            "canSkipPayCost": 0,
            "canTriggerStim": 1,
            "clearanceLevel": 0,
            "costComponents": [],
            "deviceActionQueue": None,
            "disableSpread": 0,
            "duration": 0,
            "executor": None,
            "hasInteraction": 0,
            "inactiveReason": "",
            "inkWidgetID": {
                "$type": "TweakDBID",
                "$storage": "uint64",
                "$value": "0",
            },
            "interactionChoice": _empty_interaction_choice(),
            "interactionIconType": {
                "$type": "TweakDBID",
                "$storage": "uint64",
                "$value": "0",
            },
            "interactionLayer": cname("None"),
            "isActionQueueingUsed": 0,
            "isActionRPGCheckDissabled": 0,
            "IsAppliedByMonowire": 0,
            "isInactive": 0,
            "isQueuedAction": 0,
            "isQuickHack": 0,
            "isSpiderbotAction": 0,
            "isTargetDead": 0,
            "item": tweakdbid(item_id),
            "localizedObjectName": "",
            "objectActionID": {
                "$type": "TweakDBID",
                "$storage": "uint64",
                "$value": "0",
            },
            "objectActionRecord": None,
            "paymentQuantity": 0,
            "prop": None,
            "proxyExecutor": None,
            "requesterID": {"$type": "entEntityID", "hash": "0"},
            "shouldActivateDevice": 0,
            "spiderbotActionLocationOverride": node_ref("0", storage="uint64"),
            "wasPerformedOnOwner": 0,
            "widgetStyle": "DarkBlue",
        }
    )
    return builder.node(
        quest_id,
        "questEventManagerNodeDefinition",
        input_names=("In",),
        properties={
            "componentName": cname("controller"),
            "event": event,
            "isObjectPlayer": 0,
            "isUiEvent": 0,
            "managerName": "DropPointManager",
            "objectRef": entity_reference(drop_point_ref),
            "PSClassName": cname("DropPointControllerPS"),
        },
    )


def journal_entry_visited_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    path: str,
    class_name: str,
    *,
    file_index: int = 1,
) -> GraphNode:
    condition_type = builder.handles.wrap(
        {
            "$type": "questJournalEntryVisited_ConditionType",
            "path": journal_path(
                builder,
                path,
                class_name,
                file_index,
            ),
            "visited": 1,
        }
    )
    condition = builder.handles.wrap(
        {"$type": "questJournalCondition", "type": condition_type}
    )
    return builder.node(
        quest_id,
        "questPauseConditionNodeDefinition",
        input_names=("In",),
        properties={"condition": condition},
    )


def journal_choice_succeeded_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    path: str,
) -> GraphNode:
    condition_type = builder.handles.wrap(
        {
            "$type": "questJournalEntryState_ConditionType",
            "inverted": 0,
            "path": journal_path(
                builder,
                path,
                "gameJournalPhoneChoiceEntry",
                1,
            ),
            "state": "Succeeded",
        }
    )
    condition = builder.handles.wrap(
        {"$type": "questJournalCondition", "type": condition_type}
    )
    return builder.node(
        quest_id,
        "questPauseConditionNodeDefinition",
        input_names=("In",),
        properties={"condition": condition},
    )


def logical_xor_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    input_count: int,
) -> GraphNode:
    return builder.node(
        quest_id,
        "questLogicalXorNodeDefinition",
        input_names=tuple(f"In{index}" for index in range(1, input_count + 1)),
        output_names=("Out1",),
        properties={
            "inputSocketCount": input_count,
            "outputSocketCount": 1,
        },
    )


def quest_completion_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    path: str,
) -> GraphNode:
    node_type = builder.handles.wrap(
        {
            "$type": "questJournalQuestEntry_NodeType",
            "optional": 0,
            "path": journal_path(builder, path, "gameJournalQuest", 2),
            "sendNotification": 1,
            "trackQuest": 1,
            "version": "Initial",
        }
    )
    return builder.node(
        quest_id,
        "questJournalNodeDefinition",
        input_names=("Active", "Inactive", "Succeeded", "Failed"),
        properties={"type": node_type},
    )


def reward_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    reward_id: str,
) -> GraphNode:
    node_type = builder.handles.wrap(
        {
            "$type": "questGiveReward_NodeType",
            "rewards": [tweakdbid(reward_id)],
        }
    )
    return builder.node(
        quest_id,
        "questRewardManagerNodeDefinition",
        input_names=("In",),
        properties={"type": node_type},
    )


def phase_document(
    builder: PhaseGraphBuilder,
    archive_target: Path,
    *,
    exported_datetime: str = "1970-01-01T00:00:00Z",
    include_inplace_phases: bool = True,
    phase_prefabs: tuple[str, ...] = (),
) -> JsonObject:
    document = {
        "Header": {
            "WolvenKitVersion": "8.17.4",
            "WKitJsonVersion": "0.0.9",
            "GameVersion": 2310,
            "ExportedDateTime": exported_datetime,
            "DataType": "CR2W",
            "ArchiveFileName": str(archive_target.resolve()),
        },
        "Data": {
            "Version": 195,
            "BuildVersion": 0,
            "RootChunk": {
                "$type": "questQuestPhaseResource",
                "cookingPlatform": "PLATFORM_PC",
                "graph": builder.graph,
                "inplacePhases": [],
                "phasePrefabs": [
                    {"$type": "questQuestPrefabEntry", "prefabNodeRef": node_ref(ref)}
                    for ref in phase_prefabs
                ],
            },
            "EmbeddedFiles": [],
        },
    }
    if not include_inplace_phases:
        del document["Data"]["RootChunk"]["inplacePhases"]
    return document


def community_action_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    community_ref: str,
    action: str,
) -> GraphNode:
    action_type = builder.handles.wrap(
        {
            "$type": "questCommunityTemplate_NodeType",
            "action": action,
            "communityEntryName": cname("None"),
            "communityEntryPhaseName": cname("None"),
            "spawnerReference": node_ref(community_ref),
        }
    )
    return builder.node(
        quest_id,
        "questSpawnManagerNodeDefinition",
        input_names=("In",),
        properties={
            "actions": [
                {
                    "$type": "questSpawnManagerNodeActionEntry",
                    "type": action_type,
                }
            ]
        },
    )


def device_manager_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    device: str,
    controller: str,
    action: str,
) -> GraphNode:
    params = builder.handles.wrap(
        {
            "$type": "questDeviceManager_NodeTypeParams",
            "actionProperties": [],
            "deviceAction": cname(action),
            "deviceControllerClass": cname(controller),
            "entityRef": entity_reference(),
            "objectRef": node_ref(device),
            "slotName": cname("None"),
        }
    )
    node_type = builder.handles.wrap(
        {"$type": "questDeviceManager_NodeType", "params": [params]}
    )
    return builder.node(
        quest_id,
        "questInteractiveObjectManagerNodeDefinition",
        input_names=("In",),
        properties={"type": node_type},
    )


def device_condition_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    device: str,
    controller: str,
    function: str,
) -> GraphNode:
    condition_type = builder.handles.wrap(
        {
            "$type": "questDevice_ConditionType",
            "deviceConditionFunction": cname(function),
            "deviceControllerClass": cname(controller),
            "functionParameters": [],
            "objectRef": node_ref(device),
        }
    )
    condition = builder.handles.wrap(
        {"$type": "questObjectCondition", "type": condition_type}
    )
    return builder.node(
        quest_id,
        "questPauseConditionNodeDefinition",
        input_names=("In",),
        properties={"condition": condition},
    )


def character_spawned_node(
    builder: PhaseGraphBuilder, quest_id: int, community: str
) -> GraphNode:
    comparison = builder.handles.wrap(
        {
            "$type": "questComparisonParam",
            "comparisonType": "Greater",
            "count": 0,
            "entireCommunity": 1,
        }
    )
    condition_type = builder.handles.wrap(
        {
            "$type": "questCharacterSpawned_ConditionType",
            "comparisonParams": comparison,
            "objectRef": entity_reference(community),
        }
    )
    condition = builder.handles.wrap(
        {"$type": "questCharacterCondition", "type": condition_type}
    )
    return builder.node(
        quest_id,
        "questPauseConditionNodeDefinition",
        input_names=("In",),
        properties={"condition": condition},
    )


def community_defeated_node(
    builder: PhaseGraphBuilder, quest_id: int, community: str
) -> GraphNode:
    comparison = builder.handles.wrap(
        {
            "$type": "questComparisonParam",
            "comparisonType": "GreaterOrEqual",
            "count": 0,
            "entireCommunity": 1,
        }
    )
    condition_type = builder.handles.wrap(
        {
            "$type": "questCharacterKilled_ConditionType",
            "comparisonParams": comparison,
            "defeated": 1,
            "killed": 1,
            "objectRef": entity_reference(community),
            "source": None,
            "unconscious": 1,
        }
    )
    condition = builder.handles.wrap(
        {"$type": "questCharacterCondition", "type": condition_type}
    )
    return builder.node(
        quest_id,
        "questPauseConditionNodeDefinition",
        input_names=("In",),
        properties={"condition": condition},
    )


def add_item_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    item_id: str,
    quantity: int,
) -> GraphNode:
    params = builder.handles.wrap(
        {
            "$type": "questAddRemoveItem_NodeTypeParams",
            "entityRef": local_player_reference(builder),
            "flagItemAddedCallbackAsSilent": 0,
            "isPlayer": 0,
            "itemID": tweakdbid(item_id),
            "itemIDsToIgnoreOnRemove": [],
            "nodeType": "AddItem",
            "objectRef": entity_reference(),
            "quantity": quantity,
            "removeAllQuantity": 0,
            "sendNotification": 1,
            "tagsToIgnoreOnRemove": [],
            "tagToRemove": cname("None"),
        }
    )
    node_type = builder.handles.wrap(
        {"$type": "questAddRemoveItem_NodeType", "params": [params]}
    )
    return builder.node(
        quest_id,
        "questItemManagerNodeDefinition",
        input_names=("In",),
        properties={"type": node_type},
    )


def scan_started_node(
    builder: PhaseGraphBuilder, quest_id: int, object_ref: str
) -> GraphNode:
    condition_type = builder.handles.wrap(
        {
            "$type": "questScan_ConditionType",
            "eventType": "Finished",
            "objectRef": entity_reference(object_ref),
        }
    )
    condition = builder.handles.wrap(
        {"$type": "questObjectCondition", "type": condition_type}
    )
    return builder.node(
        quest_id,
        "questPauseConditionNodeDefinition",
        input_names=("In",),
        properties={"condition": condition},
    )


def combat_threat_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    community: str,
    entry: str,
) -> GraphNode:
    params = builder.handles.wrap(
        {
            "$type": "AIInjectCombatThreatCommandParams",
            "dontForceHostileAttitude": 0,
            "duration": 0.5,
            "isPersistent": 0,
            "targetNodeRef": node_ref("0", storage="uint64"),
            "targetPuppetRef": entity_reference("#player"),
        }
    )
    return builder.node(
        quest_id,
        "questCombatNodeDefinition",
        input_names=("In",),
        output_names=("Success",),
        properties={
            "entityReference": entity_reference(community, names=[entry]),
            "params": params,
        },
    )


def resource_ref(path: str) -> JsonObject:
    return {
        "DepotPath": {
            "$type": "ResourcePath",
            "$storage": "string",
            "$value": path,
        },
        "Flags": "Soft",
    }
