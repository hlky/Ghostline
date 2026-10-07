"""Cyberpsycho graph construction, preserving vanilla node and connection order.

Each behavior function returns its signal endpoint. Node IDs are consumed from
one iterator so optional paths retain their established serialized order.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import count
from pathlib import Path
from typing import Any, Iterator

from phase_graph import (
    GraphNode,
    JsonObject,
    PhaseGraphBuilder,
    cname,
    entity_reference,
    node_ref,
    resource_ref,
    input_node,
    output_node,
    trigger_condition_node,
    objective_node,
    journal_entry_node,
    mappin_node,
    community_action_node,
    logical_xor_node,
    realtime_delay_node,
    combat_threat_node,
    fact_node,
    fact_condition_node,
    phase_document,
)
from quest_types import CompiledStage, QuestSpecError


@dataclass(frozen=True)
class _Signal:
    node: GraphNode
    socket: str = "Out"


def gameplay_ai_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    community: str,
    entry: str,
    *,
    ai_tier: str | None = None,
) -> GraphNode:
    """Set a named puppet's AI tier, or restore gameplay AI when omitted."""

    entry_data: JsonObject = {
        "$type": "questPuppetAIManagerNodeDefinitionEntry",
        "entityReference": entity_reference(community, names=[entry]),
    }
    if ai_tier is not None:
        entry_data["aiTier"] = ai_tier

    return builder.node(
        quest_id,
        "questPuppetAIManagerNodeDefinition",
        input_names=("In",),
        output_names=("Out",),
        properties={"entries": [entry_data]},
    )


def character_not_in_combat_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    community: str,
    entry: str,
    *,
    is_player: bool = False,
) -> GraphNode:
    """Wait until a named puppet, or V, is no longer in combat."""

    object_ref = (
        entity_reference() if is_player else entity_reference(community, names=[entry])
    )

    condition_type = builder.handles.wrap(
        {
            "$type": "questCharacterCombat_ConditionType",
            "objectRef": object_ref,
            "isPlayer": int(is_player),
            "inverted": 1,
        }
    )
    condition = builder.handles.wrap(
        {
            "$type": "questCharacterCondition",
            "type": condition_type,
        }
    )
    return builder.node(
        quest_id,
        "questPauseConditionNodeDefinition",
        input_names=("In",),
        properties={"condition": condition},
    )


def clear_ai_role_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    community: str,
    entry: str,
) -> GraphNode:
    """Clear a named puppet's assigned AI role before a scene takes control."""

    params = builder.handles.wrap({"$type": "AIClearRoleCommandParams"})
    return builder.node(
        quest_id,
        "questMiscAICommandNode",
        input_names=("In",),
        output_names=("Success",),
        properties={
            "entityReference": entity_reference(community, names=[entry]),
            "function": cname("AIClearRoleCommandParams"),
            "params": params,
        },
    )


def alerted_patrol_role_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    community: str,
    entry: str,
    alerted_path: str,
    alerted_spots: list[str],
) -> GraphNode:
    """Assign Lt. Mower's forced-alerted patrol role to the named boss."""

    path_params = builder.handles.wrap(
        {
            "$type": "AIPatrolPathParameters",
            "movementType": "Sprint",
            "patrolWithWeapon": 1,
        }
    )
    alerted_path_params = builder.handles.wrap(
        {
            "$type": "AIPatrolPathParameters",
            "path": node_ref(alerted_path),
            "movementType": "Sprint",
            "patrolWithWeapon": 1,
        }
    )
    workspots = builder.handles.wrap(
        {
            "$type": "AIbehaviorWorkspotList",
            "spots": [node_ref(value) for value in alerted_spots],
        }
    )
    role = builder.handles.wrap(
        {
            "$type": "AIPatrolRole",
            "pathParams": path_params,
            "alertedPathParams": alerted_path_params,
            "alertedSpots": workspots,
            "forceAlerted": 1,
        }
    )
    params = builder.handles.wrap(
        {
            "$type": "AIAssignRoleCommandParams",
            "role": role,
        }
    )
    return builder.node(
        quest_id,
        "questMiscAICommandNode",
        input_names=("In",),
        output_names=("Success",),
        properties={
            "entityReference": entity_reference(community, names=[entry]),
            "params": params,
        },
    )


def combat_target_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    community: str,
    entry: str,
) -> GraphNode:
    """Assign V as the named boss's immediate combat target."""

    params = builder.handles.wrap(
        {
            "$type": "questCombatNodeParams_CombatTarget",
            "duration": 0.01,
            "immediately": 1,
            "targetNode": node_ref("0", storage="uint64"),
            "targetPuppet": entity_reference("#player"),
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


def named_character_spawned_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    community: str,
    entry: str,
) -> GraphNode:
    comparison = builder.handles.wrap(
        {
            "$type": "questComparisonParam",
            "comparisonType": "GreaterOrEqual",
            "count": 1,
            "entireCommunity": 0,
        }
    )
    condition_type = builder.handles.wrap(
        {
            "$type": "questCharacterSpawned_ConditionType",
            "comparisonParams": comparison,
            "objectRef": entity_reference(community, names=[entry]),
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


def named_character_outcome_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    community: str,
    entry: str,
    *,
    killed: bool,
    unconscious: bool,
    defeated: bool,
) -> GraphNode:
    comparison = builder.handles.wrap(
        {
            "$type": "questComparisonParam",
            "comparisonType": "GreaterOrEqual",
            "count": 1,
            "entireCommunity": 0,
        }
    )
    condition_type = builder.handles.wrap(
        {
            "$type": "questCharacterKilled_ConditionType",
            "comparisonParams": comparison,
            "defeated": int(defeated),
            "killed": int(killed),
            "objectRef": entity_reference(community, names=[entry]),
            "source": None,
            "unconscious": int(unconscious),
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


def cyberpsycho_reveal_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    kind: str,
    community: str,
    entry: str,
) -> GraphNode:
    boss = entity_reference(community, names=[entry])
    if kind == "scan":
        wrapper_type = "questObjectCondition"
        condition_type = {
            "$type": "questScan_ConditionType",
            "objectRef": boss,
        }
    elif kind == "attacked_by_boss":
        wrapper_type = "questCharacterCondition"
        condition_type = {
            "$type": "questCharacterAttack_ConditionType",
            "attackerRef": boss,
            "isTargetPlayer": 1,
        }
    elif kind == "boss_hit_by_player":
        wrapper_type = "questCharacterCondition"
        condition_type = {
            "$type": "questCharacterHit_ConditionType",
            "isAttackerPlayer": 1,
            "targetRef": boss,
        }
    elif kind == "boss_sees_player":
        wrapper_type = "questSensesCondition"
        condition_type = {
            "$type": "questVision_ConditionType",
            "observerPuppetRef": boss,
        }
    else:
        raise QuestSpecError(f"Unsupported cyberpsycho reveal route: {kind}")
    wrapped_type = builder.handles.wrap(condition_type)
    condition = builder.handles.wrap({"$type": wrapper_type, "type": wrapped_type})
    return builder.node(
        quest_id,
        "questPauseConditionNodeDefinition",
        input_names=("In",),
        properties={"condition": condition},
    )


def character_mortality_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    community: str,
    entry: str,
    *,
    state: str,
    source: str,
    is_player: bool = False,
    reset_to_default: bool = False,
) -> GraphNode:
    puppet_ref = (
        entity_reference() if is_player else entity_reference(community, names=[entry])
    )
    subtype = builder.handles.wrap(
        {
            "$type": "questCharacterManagerParameters_SetMortality",
            "isPlayer": int(is_player),
            "puppetRef": puppet_ref,
            "resetToDefault": int(reset_to_default),
            "source": cname(source),
            "state": state,
        }
    )
    node_type = builder.handles.wrap(
        {
            "$type": "questCharacterManagerParameters_NodeType",
            "subtype": subtype,
        }
    )
    return builder.node(
        quest_id,
        "questCharacterManagerNodeDefinition",
        input_names=("In",),
        properties={"type": node_type},
    )


def character_attitude_group_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    community: str,
    entry: str,
    *,
    group_name: str,
) -> GraphNode:
    """Force a named community puppet into a vanilla attitude group."""

    subtype = builder.handles.wrap(
        {
            "$type": "questCharacterManagerParameters_SetAttitudeGroupForPuppet",
            "groupName": cname(group_name),
            "isPlayer": 0,
            "puppetRef": entity_reference(community, names=[entry]),
        }
    )
    node_type = builder.handles.wrap(
        {
            "$type": "questCharacterManagerParameters_NodeType",
            "subtype": subtype,
        }
    )
    return builder.node(
        quest_id,
        "questCharacterManagerNodeDefinition",
        input_names=("In",),
        properties={"type": node_type},
    )


def player_health_condition_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    *,
    percent: float,
) -> GraphNode:
    condition_type = builder.handles.wrap(
        {
            "$type": "questCharacterHealth_ConditionType",
            "comparisonType": "LessOrEqual",
            "isPlayer": 1,
            "objectRef": entity_reference(),
            "percent": percent,
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


def player_modify_health_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    *,
    percent: float,
) -> GraphNode:
    subtype = builder.handles.wrap(
        {
            "$type": "questCharacterManagerCombat_ModifyHealth",
            "damageSourceRef": entity_reference(),
            "isPlayer": 1,
            "noDamageIndicator": 1,
            "percent": percent,
            "puppetRef": entity_reference(),
            "setExactValue": 1,
        }
    )
    node_type = builder.handles.wrap(
        {
            "$type": "questCharacterManagerCombat_NodeType",
            "subtype": subtype,
        }
    )
    return builder.node(
        quest_id,
        "questCharacterManagerNodeDefinition",
        input_names=("In",),
        properties={"type": node_type},
    )


def scene_flow_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    scene_flow: dict[str, Any],
) -> GraphNode:
    """Build a scene node with one explicit entry and completion exit."""

    output_names = [scene_flow["exit"]]
    output_names.extend(scene_flow.get("completion_exits", []))
    output_names.extend(
        branch["exit"] for branch in scene_flow.get("completion_branches", [])
    )
    return builder.node(
        quest_id,
        "questSceneNodeDefinition",
        input_names=(scene_flow["entry"],),
        output_names=tuple(output_names),
        properties={
            "interruptionOperations": [],
            "notAllowedToBeFrozen": 0,
            "reapplyInterruptionOperationsAfterGameLoad": 0,
            "sceneFile": resource_ref(scene_flow["scene"]),
            "sceneLocation": {
                "$type": "scnWorldMarker",
                "nodeRef": node_ref(scene_flow["origin"]),
                "tag": cname("None"),
                "type": "NodeRef",
            },
            "syncToMusic": 0,
        },
    )


def _activate_and_wait(
    builder: PhaseGraphBuilder,
    stage: CompiledStage,
    node_ids: Iterator[int],
    start: GraphNode,
) -> GraphNode:
    previous = start
    activation = trigger_condition_node(
        builder,
        next(node_ids),
        stage.data["activation_trigger"],
        stage.data.get("activation_mode", "Entered"),
    )
    builder.connect(previous, activation)
    previous = activation

    if stage.data.get("objective"):
        objective = objective_node(builder, next(node_ids), stage.data["objective"])
        builder.connect(previous, objective, destination_socket="Active")
        previous = objective
    if stage.data.get("description_entry"):
        description = journal_entry_node(
            builder,
            next(node_ids),
            stage.data["description_entry"],
            "gameJournalQuestDescription",
            2,
        )
        builder.connect(previous, description, destination_socket="Active")
        previous = description
    if stage.data.get("mappin"):
        active_mappin = mappin_node(builder, next(node_ids), stage.data["mappin"])
        builder.connect(previous, active_mappin, destination_socket="Active")
        previous = active_mappin

    if stage.data.get("activate", True):
        activate = community_action_node(
            builder, next(node_ids), stage.data["community"], "Activate"
        )
        builder.connect(previous, activate)
        previous = activate

    spawned = named_character_spawned_node(
        builder,
        next(node_ids),
        stage.data["community"],
        stage.data["boss_entry"],
    )
    builder.connect(previous, spawned)
    previous = spawned

    protected = character_mortality_node(
        builder,
        next(node_ids),
        stage.data["community"],
        stage.data["boss_entry"],
        state="Invulnerable",
        source=stage.id,
    )
    builder.connect(previous, protected)
    previous = protected

    return previous


def _reveal_gate(
    builder: PhaseGraphBuilder,
    stage: CompiledStage,
    node_ids: Iterator[int],
    ready: GraphNode,
) -> _Signal:
    previous, previous_socket = ready, "Out"
    reveal = stage.data["reveal"]
    reveal_nodes: list[GraphNode] = []
    if isinstance(reveal.get("trigger"), str):
        reveal_nodes.append(
            trigger_condition_node(
                builder, next(node_ids), reveal["trigger"], "Entered"
            )
        )
    for kind in (
        "scan",
        "attacked_by_boss",
        "boss_hit_by_player",
        "boss_sees_player",
    ):
        if reveal.get(kind) is True:
            reveal_nodes.append(
                cyberpsycho_reveal_node(
                    builder,
                    next(node_ids),
                    kind,
                    stage.data["community"],
                    stage.data["boss_entry"],
                )
            )
    for reveal_node in reveal_nodes:
        builder.connect(previous, reveal_node)
    if len(reveal_nodes) == 1:
        previous = reveal_nodes[0]
        previous_socket = "Out"
    else:
        reveal_join = logical_xor_node(builder, next(node_ids), len(reveal_nodes))
        for index, reveal_node in enumerate(reveal_nodes, start=1):
            builder.connect(
                reveal_node,
                reveal_join,
                destination_socket=f"In{index}",
            )
        previous = reveal_join
        previous_socket = "Out1"

    if isinstance(stage.data.get("arena_trigger"), str):
        entered_arena = trigger_condition_node(
            builder,
            next(node_ids),
            stage.data["arena_trigger"],
            stage.data.get("arena_mode", "Entered"),
        )
        builder.connect(
            previous,
            entered_arena,
            source_socket=previous_socket,
        )
        previous = entered_arena
        previous_socket = "Out"

    return _Signal(previous, previous_socket)


def _start_combat(
    builder: PhaseGraphBuilder,
    stage: CompiledStage,
    node_ids: Iterator[int],
    reveal: _Signal,
) -> GraphNode:
    previous, previous_socket = reveal.node, reveal.socket
    gameplay_ai = gameplay_ai_node(
        builder,
        next(node_ids),
        stage.data["community"],
        stage.data["boss_entry"],
    )
    builder.connect(
        previous,
        gameplay_ai,
        source_socket=previous_socket,
    )

    mortal = character_mortality_node(
        builder,
        next(node_ids),
        stage.data["community"],
        stage.data["boss_entry"],
        state="Mortal",
        source=stage.id,
    )
    builder.connect(gameplay_ai, mortal)

    alerted_path = stage.data.get("alerted_path")
    alerted_spots = stage.data.get("alerted_spots", [])
    if isinstance(alerted_path, str) and alerted_spots:
        handoff_delay = realtime_delay_node(
            builder,
            next(node_ids),
            seconds=0,
            milliseconds=200,
        )
        builder.connect(gameplay_ai, handoff_delay)

        not_in_combat = character_not_in_combat_node(
            builder,
            next(node_ids),
            stage.data["community"],
            stage.data["boss_entry"],
        )
        builder.connect(handoff_delay, not_in_combat)

        alerted_role = alerted_patrol_role_node(
            builder,
            next(node_ids),
            stage.data["community"],
            stage.data["boss_entry"],
            alerted_path,
            alerted_spots,
        )
        builder.connect(not_in_combat, alerted_role)
        combat_handoff: GraphNode = handoff_delay
        combat_handoff_socket = "Out"
    else:
        combat_handoff = mortal
        combat_handoff_socket = "Out"

    target_player = combat_target_node(
        builder,
        next(node_ids),
        stage.data["community"],
        stage.data["boss_entry"],
    )
    builder.connect(
        combat_handoff,
        target_player,
        source_socket=combat_handoff_socket,
    )

    return target_player


def _start_hostility(
    builder: PhaseGraphBuilder,
    stage: CompiledStage,
    node_ids: Iterator[int],
    target_player: GraphNode,
) -> _Signal:
    player_defeat_scene = stage.data.get("player_defeat_scene")
    player_is_protected = isinstance(player_defeat_scene, dict)
    if player_is_protected:
        player_immortal = character_mortality_node(
            builder,
            next(node_ids),
            "",
            "",
            state="Immortal",
            source=f"{stage.id}_player_defeat",
            is_player=True,
        )
        builder.connect(
            target_player,
            player_immortal,
            source_socket="Success",
        )
        hostile_source = player_immortal
        hostile_source_socket = "Out"
    else:
        hostile_source = target_player
        hostile_source_socket = "Success"

    hostile = combat_threat_node(
        builder,
        next(node_ids),
        stage.data["community"],
        stage.data["boss_entry"],
    )
    builder.connect(
        hostile_source,
        hostile,
        source_socket=hostile_source_socket,
    )

    return _Signal(hostile_source, hostile_source_socket)


def _arm_boss_outcomes(
    builder: PhaseGraphBuilder,
    stage: CompiledStage,
    node_ids: Iterator[int],
    source: _Signal,
) -> tuple[GraphNode, GraphNode]:
    hostile_source, hostile_source_socket = source.node, source.socket
    killed = named_character_outcome_node(
        builder,
        next(node_ids),
        stage.data["community"],
        stage.data["boss_entry"],
        killed=True,
        unconscious=False,
        defeated=False,
    )
    spared = named_character_outcome_node(
        builder,
        next(node_ids),
        stage.data["community"],
        stage.data["boss_entry"],
        killed=False,
        unconscious=True,
        defeated=True,
    )
    # Arm fight-resolution listeners at the same gate that starts hostility.
    # Vanilla cyberpsycho phases do not wait for the threat command's Success
    # socket before registering their killed/defeated conditions.
    builder.connect(
        hostile_source,
        killed,
        source_socket=hostile_source_socket,
    )
    builder.connect(
        hostile_source,
        spared,
        source_socket=hostile_source_socket,
    )

    resolution = stage.data["resolution"]
    killed_fact = fact_node(builder, next(node_ids), resolution["killed_fact"])
    spared_fact = fact_node(builder, next(node_ids), resolution["spared_fact"])
    builder.connect(killed, killed_fact)
    builder.connect(spared, spared_fact)

    return killed_fact, spared_fact


def _protect_and_release_player(
    builder: PhaseGraphBuilder,
    stage: CompiledStage,
    node_ids: Iterator[int],
    source: _Signal,
    player_defeat_scene: dict[str, Any],
) -> GraphNode:
    hostile_source, hostile_source_socket = source.node, source.socket
    resolution = stage.data["resolution"]
    health_defeat = player_health_condition_node(
        builder,
        next(node_ids),
        percent=player_defeat_scene.get("health_percent", 5),
    )
    debug_defeat = fact_condition_node(
        builder,
        next(node_ids),
        player_defeat_scene["debug_fact"],
    )
    builder.connect(
        hostile_source,
        health_defeat,
        source_socket=hostile_source_socket,
    )
    builder.connect(
        hostile_source,
        debug_defeat,
        source_socket=hostile_source_socket,
    )

    defeat_trigger = logical_xor_node(builder, next(node_ids), 2)
    builder.connect(health_defeat, defeat_trigger, destination_socket="In1")
    builder.connect(debug_defeat, defeat_trigger, destination_socket="In2")

    protect_boss = character_mortality_node(
        builder,
        next(node_ids),
        stage.data["community"],
        stage.data["boss_entry"],
        state="Invulnerable",
        source=f"{stage.id}_player_defeat",
    )
    builder.connect(defeat_trigger, protect_boss, source_socket="Out1")

    friendly_boss = character_attitude_group_node(
        builder,
        next(node_ids),
        stage.data["community"],
        stage.data["boss_entry"],
        group_name="friendly",
    )
    builder.connect(protect_boss, friendly_boss)

    clear_boss_role = clear_ai_role_node(
        builder,
        next(node_ids),
        stage.data["community"],
        stage.data["boss_entry"],
    )
    builder.connect(friendly_boss, clear_boss_role)

    cinematic_boss = gameplay_ai_node(
        builder,
        next(node_ids),
        stage.data["community"],
        stage.data["boss_entry"],
        ai_tier="Cinematic",
    )
    builder.connect(
        clear_boss_role,
        cinematic_boss,
        source_socket="Success",
    )

    defeated_fact = fact_node(
        builder,
        next(node_ids),
        player_defeat_scene["defeat_fact"],
    )
    builder.connect(cinematic_boss, defeated_fact)

    loss_spared_fact = fact_node(
        builder,
        next(node_ids),
        resolution["spared_fact"],
    )
    builder.connect(defeated_fact, loss_spared_fact)

    combat_release_delay = realtime_delay_node(
        builder,
        next(node_ids),
        seconds=0,
        milliseconds=200,
    )
    builder.connect(loss_spared_fact, combat_release_delay)

    # Restore V before handing control to the post-defeat dialogue.  The
    # player remains Immortal until the scene exits.  Do not wait for the
    # player's combat flag here: after a protected-health defeat the flag
    # can remain latched even after the boss is friendly and her AI role
    # has been cleared, which deadlocks the handoff.  Vanilla living-NPC
    # combat-to-scene flows proceed from AIClearRole success instead of
    # polling the player's combat state.
    heal_player = player_modify_health_node(
        builder,
        next(node_ids),
        percent=100,
    )
    builder.connect(combat_release_delay, heal_player)

    return heal_player


def _defeat_scene_chain(
    builder: PhaseGraphBuilder,
    node_ids: Iterator[int],
    heal_player: GraphNode,
    player_defeat_scene: dict[str, Any],
) -> tuple[GraphNode, _Signal]:
    loss_scene_node = scene_flow_node(
        builder,
        next(node_ids),
        player_defeat_scene,
    )
    builder.connect(
        heal_player,
        loss_scene_node,
        destination_socket=player_defeat_scene["entry"],
    )

    loss_tail = loss_scene_node
    loss_tail_socket = player_defeat_scene["exit"]
    for name in ("continuation_scene", "aftermath_scene"):
        followup = player_defeat_scene.get(name)
        if not isinstance(followup, dict):
            continue
        following_node = scene_flow_node(builder, next(node_ids), followup)
        builder.connect(
            loss_tail,
            following_node,
            source_socket=loss_tail_socket,
            destination_socket=followup["entry"],
        )
        loss_tail = following_node
        loss_tail_socket = followup["exit"]

    return loss_scene_node, _Signal(loss_tail, loss_tail_socket)


def _defeat_completion_routes(
    builder: PhaseGraphBuilder,
    node_ids: Iterator[int],
    loss_scene_node: GraphNode,
    tail: _Signal,
    player_defeat_scene: dict[str, Any],
) -> _Signal:
    loss_tail, loss_tail_socket = tail.node, tail.socket
    completion_exits = player_defeat_scene.get("completion_exits", [])
    completion_branches = player_defeat_scene.get("completion_branches", [])
    completion_branch_tails: list[GraphNode] = []
    for completion_branch in completion_branches:
        branch_fact = fact_node(
            builder,
            next(node_ids),
            completion_branch["set_fact"],
        )
        builder.connect(
            loss_scene_node,
            branch_fact,
            source_socket=completion_branch["exit"],
        )
        completion_branch_tails.append(branch_fact)

    if completion_exits or completion_branch_tails:
        completion_merge = logical_xor_node(
            builder,
            next(node_ids),
            1 + len(completion_exits) + len(completion_branch_tails),
        )
        builder.connect(
            loss_tail,
            completion_merge,
            source_socket=loss_tail_socket,
            destination_socket="In1",
        )
        for index, completion_exit in enumerate(
            completion_exits,
            start=2,
        ):
            builder.connect(
                loss_scene_node,
                completion_merge,
                source_socket=completion_exit,
                destination_socket=f"In{index}",
            )
        for index, branch_tail in enumerate(
            completion_branch_tails,
            start=2 + len(completion_exits),
        ):
            builder.connect(
                branch_tail,
                completion_merge,
                destination_socket=f"In{index}",
            )
        restore_source = completion_merge
        restore_source_socket = "Out1"
    else:
        restore_source = loss_tail
        restore_source_socket = loss_tail_socket

    return _Signal(restore_source, restore_source_socket)


def _restore_player(
    builder: PhaseGraphBuilder,
    stage: CompiledStage,
    node_ids: Iterator[int],
    source: _Signal,
) -> GraphNode:
    restored = character_mortality_node(
        builder,
        next(node_ids),
        "",
        "",
        state="Mortal",
        source=f"{stage.id}_player_defeat",
        is_player=True,
        reset_to_default=True,
    )
    builder.connect(source.node, restored, source_socket=source.socket)
    return restored


def _player_defeat_route(
    builder: PhaseGraphBuilder,
    stage: CompiledStage,
    node_ids: Iterator[int],
    source: _Signal,
) -> GraphNode | None:
    configuration = stage.data.get("player_defeat_scene")
    if not isinstance(configuration, dict):
        return None
    healed = _protect_and_release_player(
        builder, stage, node_ids, source, configuration
    )
    scene, tail = _defeat_scene_chain(builder, node_ids, healed, configuration)
    completion = _defeat_completion_routes(
        builder, node_ids, scene, tail, configuration
    )
    return _restore_player(builder, stage, node_ids, completion)


def _merge_resolution(
    builder: PhaseGraphBuilder,
    stage: CompiledStage,
    node_ids: Iterator[int],
    killed_fact: GraphNode,
    spared_fact: GraphNode,
    player_defeat_tail: GraphNode | None,
) -> _Signal:
    player_is_protected = isinstance(stage.data.get("player_defeat_scene"), dict)
    postfight_scene = stage.data.get("postfight_scene")
    postfight_scene_node: GraphNode | None = None
    if isinstance(postfight_scene, dict):
        postfight_scene_node = scene_flow_node(
            builder,
            next(node_ids),
            postfight_scene,
        )

    killed_tail: GraphNode = killed_fact
    if player_is_protected:
        killed_tail = _restore_player(builder, stage, node_ids, _Signal(killed_tail))

    spared_tail: GraphNode = spared_fact
    if postfight_scene_node is not None and isinstance(postfight_scene, dict):
        builder.connect(
            spared_tail,
            postfight_scene_node,
            destination_socket=postfight_scene["entry"],
        )
        spared_tail = postfight_scene_node
        spared_tail_socket = postfight_scene["exit"]
    else:
        spared_tail_socket = "Out"
    if player_is_protected:
        spared_tail = _restore_player(
            builder, stage, node_ids, _Signal(spared_tail, spared_tail_socket)
        )
        spared_tail_socket = "Out"

    outcome_join = logical_xor_node(
        builder,
        next(node_ids),
        3 if player_defeat_tail is not None else 2,
    )
    builder.connect(killed_tail, outcome_join, destination_socket="In1")
    builder.connect(
        spared_tail,
        outcome_join,
        source_socket=spared_tail_socket,
        destination_socket="In2",
    )
    if player_defeat_tail is not None:
        builder.connect(
            player_defeat_tail,
            outcome_join,
            destination_socket="In3",
        )
    previous = outcome_join
    previous_socket = "Out1"

    return _Signal(previous, previous_socket)


def _finish_and_cleanup(
    builder: PhaseGraphBuilder,
    stage: CompiledStage,
    node_ids: Iterator[int],
    resolved: _Signal,
    end: GraphNode,
) -> None:
    previous, previous_socket = resolved.node, resolved.socket
    if stage.data.get("objective"):
        objective_done = objective_node(
            builder, next(node_ids), stage.data["objective"]
        )
        builder.connect(
            previous,
            objective_done,
            source_socket=previous_socket,
            destination_socket="Succeeded",
        )
        previous = objective_done
        previous_socket = "Out"
    if stage.data.get("mappin"):
        mappin_done = mappin_node(builder, next(node_ids), stage.data["mappin"])
        builder.connect(
            previous,
            mappin_done,
            source_socket=previous_socket,
            destination_socket="Inactive",
        )
        previous = mappin_done
        previous_socket = "Out"
    if stage.data.get("completion_fact"):
        completed = fact_node(builder, next(node_ids), stage.data["completion_fact"])
        builder.connect(previous, completed, source_socket=previous_socket)
        previous = completed
        previous_socket = "Out"

    cleanup = stage.data.get("cleanup")
    if isinstance(cleanup, dict):
        if isinstance(cleanup.get("trigger"), str):
            outside = trigger_condition_node(
                builder, next(node_ids), cleanup["trigger"], "IsOutside"
            )
            builder.connect(previous, outside, source_socket=previous_socket)
            previous = outside
            previous_socket = "Out"
        if cleanup.get("deactivate_community", True):
            deactivate = community_action_node(
                builder, next(node_ids), stage.data["community"], "Deactivate"
            )
            builder.connect(previous, deactivate, source_socket=previous_socket)
            previous = deactivate
            previous_socket = "Out"

    builder.connect_to_earlier_output(previous, end, source_socket=previous_socket)


def build_cyberpsycho_encounter_phase(
    stage: CompiledStage,
    archive_target: Path,
) -> JsonObject:
    """Assemble readiness, combat, defeat handoff, and cleanup in stable order."""
    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    node_ids = count(10)
    ready = _activate_and_wait(builder, stage, node_ids, start)
    reveal = _reveal_gate(builder, stage, node_ids, ready)
    target = _start_combat(builder, stage, node_ids, reveal)
    hostile = _start_hostility(builder, stage, node_ids, target)
    killed, spared = _arm_boss_outcomes(builder, stage, node_ids, hostile)
    defeated = _player_defeat_route(builder, stage, node_ids, hostile)
    resolution = _merge_resolution(builder, stage, node_ids, killed, spared, defeated)
    _finish_and_cleanup(builder, stage, node_ids, resolution, end)
    return phase_document(builder, archive_target)
