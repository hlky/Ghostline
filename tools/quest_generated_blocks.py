"""Generated replacements for the retained quest-block regression fixtures.

Builders consume typed bindings directly. No runtime path reads a template or
substitutes placeholder strings. Legacy configurations preserve their graph;
additional structure is opt-in, with cancellation available through owned_scope.
"""

from pathlib import Path

from phase_graph import (
    PhaseGraphBuilder,
    cname,
    device_manager_node as device_manager,
    device_condition_node as device_condition,
    fact_condition_node,
    fact_node,
    input_node,
    output_node,
    objective_node,
    logical_xor_node,
    mappin_node,
    journal_entry_node,
    phase_document,
    inventory_condition_node,
)
from generate_advanced_quest_block_templates import (
    remove_item_node,
    character_spawned,
    mount_condition,
    trigger_condition,
    assign_character_to_vehicle,
    teleport_player,
    set_player_world_visibility,
    scene_node,
    objective_counter_node,
    puppet_ai_tier,
    assign_follower_role,
    clear_ai_role,
    character_killed,
)
from generate_ai_vehicle_block_templates import (
    vehicle_stopped_condition,
    trigger_condition_node,
    finish_linear,
    character_mount_condition,
    carried_inside_condition,
)
from phase_graph import entity_reference, community_action_node, realtime_delay_node
from quest_orchestration import order_handles
from quest_flow import walk


def entry_node(builder, stage):
    builder.stage = stage
    actual = input_node(builder)
    actual.data["socketName"] = cname(
        stage.data.get("inputs", {"start": "In1"})["start"]
    )
    previous = actual
    if stage.type != "meet_contact" and stage.data.get("description_entry"):
        description = journal_entry_node(
            builder,
            60000,
            stage.data["description_entry"],
            "gameJournalQuestDescription",
            2,
        )
        builder.connect(previous, description, destination_socket="Active")
        previous = description
    if stage.type in {"carry_npc", "deliver_vehicle"} and stage.data.get("mappin"):
        pin = mappin_node(builder, 60001, stage.data["mappin"])
        builder.connect(previous, pin, destination_socket="Active")
        previous = pin
    return previous


def exit_node(builder, stage):
    end = output_node(builder)
    end.data["socketName"] = cname(
        stage.data.get("outcomes", {"success": "Out1"})["success"]
    )
    return end


def finish(builder, previous, end, *, source_socket="Out"):
    stage = builder.stage
    if stage.type in {"carry_npc", "deliver_vehicle"} and stage.data.get("mappin"):
        pin = mappin_node(builder, 60002, stage.data["mappin"])
        builder.connect(
            previous, pin, source_socket=source_socket, destination_socket="Inactive"
        )
        previous, source_socket = pin, "Out"
    fact = stage.data.get("completion_fact")
    if (
        stage.type in {"carry_npc", "deliver_vehicle"}
        and fact
        and not any(
            node.get("$type") == "questSetVar_NodeType" and node.get("factName") == fact
            for node in walk(builder.graph)
        )
    ):
        completed = fact_node(builder, 60003, fact)
        builder.connect(previous, completed, source_socket=source_socket)
        previous, source_socket = completed, "Out"
    builder.connect_to_earlier_output(previous, end, source_socket=source_socket)


def finish_document(builder, archive, stage):
    document = phase_document(
        builder,
        archive,
        include_inplace_phases=stage.type
        in {"optional_condition", "choice_gate", "meet_contact"},
        exported_datetime="2026-07-24T00:00:00Z",
    )
    # Meeting and braindance retain their existing compiler lifecycle adapter.
    if stage.type not in {"meet_contact", "braindance_analysis"}:
        for field, state in (
            ("on_enter", "Active"),
            ("on_success", "Succeeded"),
            ("on_failure", "Failed"),
        ):
            if stage.data.get("objective_lifecycle", {}).get(field) == "retain":
                document = retain_generated_transition(
                    document, stage.data["objective"], state
                )
    return order_handles(document)


def retain_generated_transition(document, objective, transition):
    """Bypass a journal transition with arbitrary fan-in/out and handle layout.

    Flatten handle identity before rewiring, then embed definitions at first
    use. This avoids the older meeting adapter's single-edge layout constraint.
    Unconnected journal definitions remain harmless editor/reference evidence.
    """
    import copy

    definitions = {
        str(item["HandleId"]): copy.deepcopy(item["Data"])
        for item in walk(document)
        if "HandleId" in item
    }

    def reference(value):
        if isinstance(value, list):
            return [reference(child) for child in value]
        if not isinstance(value, dict):
            return value
        if "HandleId" in value or "HandleRefId" in value:
            return {"HandleRefId": str(value.get("HandleId", value.get("HandleRefId")))}
        return {key: reference(child) for key, child in value.items()}

    flat = {key: reference(value) for key, value in definitions.items()}
    identifier = lambda wrapper: str(wrapper["HandleRefId"])
    graph = flat[identifier(reference(document)["Data"]["RootChunk"]["graph"])]
    next_handle = max(map(int, flat)) + 1
    for wrapper in graph["nodes"]:
        node = flat[identifier(wrapper)]
        if node["$type"] != "questJournalNodeDefinition":
            continue
        operation = flat[identifier(node["type"])]
        path = operation.get("path")
        if not path or flat[identifier(path)].get("realPath") != objective:
            continue
        sockets = {
            flat[identifier(s)]["name"]["$value"]: identifier(s)
            for s in node["sockets"]
        }
        if transition not in sockets or "Out" not in sockets:
            continue
        incoming = list(flat[sockets[transition]]["connections"])
        outgoing = list(flat[sockets["Out"]]["connections"])
        if not incoming:
            continue
        for incoming_ref in incoming:
            incoming_id = identifier(incoming_ref)
            connection = flat[incoming_id]
            source = flat[identifier(connection["source"])]
            if not outgoing:
                source["connections"] = [
                    edge
                    for edge in source["connections"]
                    if identifier(edge) != incoming_id
                ]
            for index, outgoing_ref in enumerate(outgoing):
                destination = flat[
                    identifier(flat[identifier(outgoing_ref)]["destination"])
                ]
                if index == 0:
                    edge_id = incoming_id
                else:
                    edge_id = str(next_handle)
                    next_handle += 1
                    flat[edge_id] = copy.deepcopy(connection)
                    source["connections"].append({"HandleRefId": edge_id})
                flat[edge_id]["destination"] = copy.deepcopy(
                    flat[identifier(outgoing_ref)]["destination"]
                )
                destination["connections"].append({"HandleRefId": edge_id})
        for outgoing_ref in outgoing:
            destination = flat[
                identifier(flat[identifier(outgoing_ref)]["destination"])
            ]
            destination["connections"] = [
                edge
                for edge in destination["connections"]
                if identifier(edge) != identifier(outgoing_ref)
            ]
        flat[sockets[transition]]["connections"] = []
        flat[sockets["Out"]]["connections"] = []
    seen = set()

    def embed(value):
        if isinstance(value, list):
            return [embed(child) for child in value]
        if not isinstance(value, dict):
            return value
        if "HandleRefId" in value:
            handle = identifier(value)
            if handle in seen:
                return value
            seen.add(handle)
            return {"HandleId": handle, "Data": embed(flat[handle])}
        return {key: embed(child) for key, child in value.items()}

    return embed(reference(document))


def build_generated_optional_condition_phase(stage, archive: Path):
    """Evaluate a boolean fact immediately and converge both outcomes."""
    data = stage.data
    builder = PhaseGraphBuilder()
    start, end = (entry_node(builder, stage), exit_node(builder, stage))
    objective = objective_node(builder, 10, data["objective"])
    passed = fact_condition_node(
        builder, 11, data["condition"]["value"], comparison="Greater", value=0
    )
    failed = (
        fact_condition_node(
            builder, 12, data["condition"]["value"], comparison="Equal", value=0
        )
        if data.get("evaluation") != "on_entry"
        else None
    )
    if failed is None:
        snapshot_node(builder, passed)
    success = fact_node(builder, 13, data["success_fact"])
    failure = fact_node(builder, 14, data["failure_fact"])
    join = logical_xor_node(builder, 15, input_count=2)
    objective_done = objective_node(builder, 16, data["objective"])
    builder.connect(start, objective, destination_socket="Active")
    builder.connect(objective, passed)
    if failed is None:
        builder.connect(passed, success, source_socket="True")
        builder.connect(passed, failure, source_socket="False")
    else:
        builder.connect(objective, failed)
        builder.connect(passed, success)
        builder.connect(failed, failure)
    builder.connect(success, join, destination_socket="In1")
    builder.connect(failure, join, destination_socket="In2")
    builder.connect(
        join, objective_done, source_socket="Out1", destination_socket="Succeeded"
    )
    builder.connect_to_earlier_output(objective_done, end)
    return finish_document(builder, archive, stage)


def build_generated_stealth_monitor_phase(stage, archive: Path):
    data = stage.data
    builder = PhaseGraphBuilder()
    start, end = (entry_node(builder, stage), exit_node(builder, stage))
    active = objective_node(builder, 10, data["objective"])
    failed = fact_condition_node(
        builder, 11, data["failure_fact"], comparison="Greater", value=0
    )
    stopped = fact_condition_node(
        builder, 12, data["stop_fact"], comparison="Greater", value=0
    )
    failed_objective = objective_node(builder, 13, data["objective"])
    succeeded_objective = objective_node(builder, 14, data["objective"])
    success_fact = fact_node(builder, 15, data["success_fact"])
    join = logical_xor_node(builder, 16, input_count=2)
    builder.connect(start, active, destination_socket="Active")
    builder.connect(active, failed)
    builder.connect(active, stopped)
    for index, name in enumerate(data.get("additional_failure_facts", [])):
        detected = fact_condition_node(builder, 100 + index, name)
        builder.connect(active, detected)
        builder.connect(detected, failed_objective, destination_socket="Failed")
    builder.connect(failed, failed_objective, destination_socket="Failed")
    builder.connect(stopped, succeeded_objective, destination_socket="Succeeded")
    builder.connect(failed_objective, join, destination_socket="In1")
    builder.connect(succeeded_objective, success_fact)
    builder.connect(success_fact, join, destination_socket="In2")
    finish(builder, join, end, source_socket="Out1")
    return finish_document(builder, archive, stage)


def build_generated_plant_item_phase(stage, archive: Path):
    data = stage.data
    builder = PhaseGraphBuilder()
    start, end = (entry_node(builder, stage), exit_node(builder, stage))
    active = objective_node(builder, 10, data["objective"])
    action = device_manager(
        builder, 11, data["device"], data["controller_class"], data["action"]
    )
    completed = device_condition(
        builder,
        12,
        data["device"],
        data["controller_class"],
        data["completion_function"],
    )
    remove = (
        remove_item_node(builder, 13, data["item"])
        if data.get("consume_item", True)
        else None
    )
    done = objective_node(builder, 14, data["objective"])
    fact = fact_node(builder, 15, data["completion_fact"])
    builder.connect(start, active, destination_socket="Active")
    builder.connect(active, action)
    builder.connect(action, completed)
    if remove is not None:
        builder.connect(completed, remove)
        builder.connect(remove, done, destination_socket="Succeeded")
    else:
        retained = inventory_condition_node(builder, 13, data["item"])
        builder.connect(completed, retained)
        builder.connect(retained, done, destination_socket="Succeeded")
    builder.connect(done, fact)
    finish(builder, fact, end)
    return finish_document(builder, archive, stage)


def build_generated_release_or_rescue_npc_phase(stage, archive: Path):
    data = stage.data
    builder = PhaseGraphBuilder()
    start, end = (entry_node(builder, stage), exit_node(builder, stage))
    active = objective_node(builder, 10, data["objective"])
    action = device_manager(
        builder, 11, data["device"], data["controller_class"], data["action"]
    )
    released = device_condition(
        builder,
        12,
        data["device"],
        data["controller_class"],
        data["completion_function"],
    )
    ready = character_spawned(builder, 13, data["community"], data["entry"])
    done = objective_node(builder, 14, data["objective"])
    fact = fact_node(builder, 15, data["completion_fact"])
    builder.connect(start, active, destination_socket="Active")
    builder.connect(active, action)
    builder.connect(action, released)
    builder.connect(released, ready)
    previous = ready
    for index, entry in enumerate(data.get("additional_entries", [])):
        actor = character_spawned(builder, 100 + index, data["community"], entry)
        builder.connect(previous, actor)
        previous = actor
    builder.connect(previous, done, destination_socket="Succeeded")
    builder.connect(done, fact)
    finish(builder, fact, end)
    return finish_document(builder, archive, stage)


def build_generated_enter_vehicle_phase(stage, archive: Path):
    data = stage.data
    builder = PhaseGraphBuilder()
    start, end = (entry_node(builder, stage), exit_node(builder, stage))
    active = objective_node(builder, 10, data["objective"])
    pin_on = mappin_node(builder, 11, data["mappin"])
    mounted = mount_condition(
        builder,
        12,
        vehicle=data["vehicle_community"],
        vehicle_community=data["vehicle_community"],
        vehicle_entry=data["vehicle_entry"],
    )
    mounted.data["condition"]["Data"]["type"]["Data"]["role"] = data.get(
        "player_role", "Invalid"
    )
    done = objective_node(builder, 13, data["objective"])
    pin_off = mappin_node(builder, 14, data["mappin"])
    builder.connect(start, active, destination_socket="Active")
    builder.connect(active, pin_on, destination_socket="Active")
    builder.connect(pin_on, mounted)
    builder.connect(mounted, done, destination_socket="Succeeded")
    builder.connect(done, pin_off, destination_socket="Inactive")
    finish(builder, pin_off, end)
    return finish_document(builder, archive, stage)


def build_generated_drive_to_phase(stage, archive: Path):
    data = stage.data
    builder = PhaseGraphBuilder()
    start, end = (entry_node(builder, stage), exit_node(builder, stage))
    active = objective_node(builder, 10, data["objective"])
    pin_on = mappin_node(builder, 11, data["mappin"])
    arrived = trigger_condition(
        builder,
        12,
        data["destination"],
        entity_reference(data["vehicle_community"], names=(data["vehicle_entry"],)),
    )
    done = objective_node(builder, 13, data["objective"])
    pin_off = mappin_node(builder, 14, data["mappin"])
    fact = fact_node(builder, 15, data["completion_fact"])
    builder.connect(start, active, destination_socket="Active")
    builder.connect(active, pin_on, destination_socket="Active")
    previous = pin_on
    for index, waypoint in enumerate(data.get("waypoints", [])):
        gate = trigger_condition(
            builder,
            100 + index,
            waypoint,
            entity_reference(data["vehicle_community"], names=(data["vehicle_entry"],)),
        )
        builder.connect(previous, gate)
        previous = gate
    builder.connect(previous, arrived)
    builder.connect(arrived, done, destination_socket="Succeeded")
    builder.connect(done, pin_off, destination_socket="Inactive")
    builder.connect(pin_off, fact)
    finish(builder, fact, end)
    return finish_document(builder, archive, stage)


def build_generated_steal_vehicle_phase(stage, archive: Path):
    data = stage.data
    builder = PhaseGraphBuilder()
    start, end = (entry_node(builder, stage), exit_node(builder, stage))
    active = objective_node(builder, 10, data["objective"])
    pin_on = mappin_node(builder, 11, data["mappin"])
    mounted = mount_condition(
        builder,
        12,
        vehicle=data["vehicle_community"],
        vehicle_community=data["vehicle_community"],
        vehicle_entry=data["vehicle_entry"],
    )
    mounted.data["condition"]["Data"]["type"]["Data"]["role"] = data.get(
        "player_role", "Invalid"
    )
    done = objective_node(builder, 13, data["objective"])
    pin_off = mappin_node(builder, 14, data["mappin"])
    completed = fact_node(builder, 15, data["completion_fact"])
    builder.connect(start, active, destination_socket="Active")
    builder.connect(active, pin_on, destination_socket="Active")
    builder.connect(pin_on, mounted)
    builder.connect(mounted, done, destination_socket="Succeeded")
    builder.connect(done, pin_off, destination_socket="Inactive")
    builder.connect(pin_off, completed)
    finish(builder, completed, end)
    return finish_document(builder, archive, stage)


def build_generated_vehicle_cleanup_phase(stage, archive: Path):
    data = stage.data
    builder = PhaseGraphBuilder()
    start, end = (entry_node(builder, stage), exit_node(builder, stage))
    fact = fact_node(builder, 10, data["completion_fact"])
    previous = start
    for index, community in enumerate(data.get("cleanup_communities", [])):
        deactivate = community_action_node(
            builder, 100 + index, community, "Deactivate"
        )
        builder.connect(previous, deactivate)
        previous = deactivate
    builder.connect(previous, fact)
    finish(builder, fact, end)
    return finish_document(builder, archive, stage)


def build_generated_deliver_vehicle_phase(stage, archive: Path):
    data = stage.data
    builder = PhaseGraphBuilder()
    start = entry_node(builder, stage)
    end = exit_node(builder, stage)
    objective_active = objective_node(builder, 10, data["objective"])
    arrived = trigger_condition_node(
        builder, 11, data["destination"], activator=entity_reference(data["vehicle"])
    )
    stopped = (
        vehicle_stopped_condition(builder, 12, data["vehicle"])
        if data.get("require_stop", True)
        else None
    )
    objective_success = objective_node(builder, 13, data["objective"])
    nodes = [
        (start, "Out", "In"),
        (objective_active, "Out", "Active"),
        (arrived, "Out", "In"),
    ]
    if stopped is not None:
        nodes.append((stopped, "Out", "In"))
    if data.get("require_player_exit", False):
        mounted = mount_condition(builder, 100, vehicle=data["vehicle"])
        mounted.data["condition"]["Data"]["type"]["Data"]["role"] = "Invalid"
        snapshot_node(builder, mounted)
        unmounted = mount_condition(builder, 101, vehicle=data["vehicle"])
        operation = unmounted.data["condition"]["Data"]["type"]["Data"]
        operation["condition"], operation["role"] = "OnUnmount", "Invalid"
        previous, socket, _ = nodes[-1]
        finish_linear(builder, nodes)
        builder.connect(previous, mounted, source_socket=socket)
        builder.connect(mounted, unmounted, source_socket="True")
        builder.connect(
            mounted,
            objective_success,
            source_socket="False",
            destination_socket="Succeeded",
        )
        builder.connect(unmounted, objective_success, destination_socket="Succeeded")
    else:
        nodes.append((objective_success, "Out", "Succeeded"))
        finish_linear(builder, nodes)
    finish(builder, objective_success, end)
    return finish_document(builder, archive, stage)


def snapshot_node(builder, node):
    """Turn an unwired native predicate into an immediate True/False branch."""
    node.data["$type"] = "questConditionNodeDefinition"
    node.data["sockets"] = [
        socket for socket in node.data["sockets"] if socket not in node.outputs.values()
    ]
    node.outputs.clear()
    for name in ("True", "False"):
        socket = builder.socket(name, "Output")
        node.outputs[name] = socket
        node.data["sockets"].append(socket)


def build_generated_carry_npc_phase(stage, archive: Path):
    data = stage.data
    builder = PhaseGraphBuilder()
    start = entry_node(builder, stage)
    end = exit_node(builder, stage)
    objective_active = objective_node(builder, 10, data["objective"])
    mounted = character_mount_condition(
        builder, 11, community=data["community"], entry=data["entry"]
    )
    delivered = carried_inside_condition(
        builder,
        12,
        community=data["community"],
        entry=data["entry"],
        destination=data["destination"],
    )
    objective_success = objective_node(builder, 13, data["objective"])
    nodes = [
        (start, "Out", "In"),
        (objective_active, "Out", "Active"),
        (mounted, "Out", "In"),
    ]
    for index, waypoint in enumerate(data.get("waypoints", [])):
        gate = carried_inside_condition(
            builder,
            100 + index,
            community=data["community"],
            entry=data["entry"],
            destination=waypoint,
        )
        nodes.append((gate, "Out", "In"))
    nodes.extend([(delivered, "Out", "In"), (objective_success, "Out", "Succeeded")])
    finish_linear(builder, nodes)
    finish(builder, objective_success, end)
    return finish_document(builder, archive, stage)


def build_generated_ride_with_contact_phase(stage, archive: Path):
    data = stage.data
    builder = PhaseGraphBuilder()
    start, end = (entry_node(builder, stage), exit_node(builder, stage))
    active = objective_node(builder, 10, data["objective"])
    assign = assign_character_to_vehicle(
        builder,
        11,
        community=data["contact_community"],
        entry=data["contact_entry"],
        vehicle=data["vehicle_community"],
        vehicle_entry=data["vehicle_entry"],
    )
    assign.data["type"]["Data"]["slotName"] = cname(
        data.get("contact_slot", "seat_front_right")
    )
    player = mount_condition(
        builder,
        12,
        vehicle=data["vehicle_community"],
        vehicle_community=data["vehicle_community"],
        vehicle_entry=data["vehicle_entry"],
    )
    contact = mount_condition(
        builder,
        13,
        vehicle=data["vehicle_community"],
        vehicle_community=data["vehicle_community"],
        vehicle_entry=data["vehicle_entry"],
        community=data["contact_community"],
        entry=data["contact_entry"],
    )
    player.data["condition"]["Data"]["type"]["Data"]["role"] = data.get(
        "player_role", "Driver"
    )
    contact.data["condition"]["Data"]["type"]["Data"]["role"] = data.get(
        "contact_role", "Passenger"
    )
    passengers = data.get("additional_passengers", [])
    count = len(passengers) + 2
    join = builder.node(
        14,
        "questLogicalAndNodeDefinition",
        input_names=tuple(f"In{i}" for i in range(1, count + 1)),
        output_names=("Out1",),
        properties={"inputSocketCount": count, "outputSocketCount": 1},
    )
    done = objective_node(builder, 15, data["objective"])
    builder.connect(start, active, destination_socket="Active")
    previous = active
    if data.get("wait_for_contacts", False):
        for index, actor in enumerate(
            [
                {
                    "community": data["contact_community"],
                    "entry": data["contact_entry"],
                },
                *passengers,
            ]
        ):
            ready = character_spawned(
                builder, 100 + index, actor["community"], actor["entry"]
            )
            builder.connect(previous, ready)
            previous = ready
    builder.connect(previous, assign)
    previous = assign
    mounted_passengers = []
    for index, actor in enumerate(passengers):
        assigned = assign_character_to_vehicle(
            builder,
            1000 + index * 2,
            community=actor["community"],
            entry=actor["entry"],
            vehicle=data["vehicle_community"],
            vehicle_entry=data["vehicle_entry"],
            slot=actor["slot"],
        )
        builder.connect(previous, assigned)
        previous = assigned
        mounted = mount_condition(
            builder,
            1001 + index * 2,
            vehicle=data["vehicle_community"],
            vehicle_community=data["vehicle_community"],
            vehicle_entry=data["vehicle_entry"],
            community=actor["community"],
            entry=actor["entry"],
        )
        mounted.data["condition"]["Data"]["type"]["Data"]["role"] = "Passenger"
        mounted_passengers.append(mounted)
    builder.connect(previous, player)
    builder.connect(previous, contact)
    for index, mounted in enumerate(mounted_passengers, 3):
        builder.connect(previous, mounted)
        builder.connect(mounted, join, destination_socket=f"In{index}")
    builder.connect(player, join, destination_socket="In1")
    builder.connect(contact, join, destination_socket="In2")
    builder.connect(join, done, source_socket="Out1", destination_socket="Succeeded")
    finish(builder, done, end)
    return finish_document(builder, archive, stage)


def build_generated_braindance_analysis_phase(stage, archive: Path):
    data = stage.data
    builder = PhaseGraphBuilder()
    start, end = (entry_node(builder, stage), exit_node(builder, stage))
    active_objective = objective_node(builder, 20, data["objective"])
    park_player = teleport_player(builder, 9, data["player_anchor"], heal=True)
    hide_player = set_player_world_visibility(builder, 11, show=False)
    teardown = seconds_delay(builder, 19, data.get("teardown_seconds", 1.5))
    restore_player = teleport_player(builder, 14, data["player_return"], heal=False)
    show_player = set_player_world_visibility(builder, 15, show=True)
    settle = seconds_delay(builder, 16, data.get("settle_seconds", 0.05))
    enable_exit_delay = seconds_delay(builder, 17, data.get("exit_enable_seconds", 0.5))
    enable_exit = builder.node(
        18,
        "questUIManagerNodeDefinition",
        input_names=("In",),
        properties={
            "type": builder.handles.wrap(
                {"$type": "questEnableBraindanceFinish_NodeType"}
            )
        },
    )
    scene = scene_node(
        builder,
        12,
        data["scene"],
        data["scene_origin"],
        output_names=tuple(
            data.get(
                "scene_exit_sockets", ["end", "complete", "Default INT", "Default RET"]
            )
        ),
    )
    scene.inputs["start"]["Data"]["name"] = cname(data.get("scene_entry", "start"))
    clues = [
        fact_condition_node(
            builder,
            21 + index if index < 3 else 100 + index,
            name,
            comparison="Greater",
            value=0,
        )
        for index, name in enumerate(data["clue_facts"])
    ]
    counters = [
        objective_counter_node(
            builder, 26 + index if index < 3 else 1000 + index, data["objective"]
        )
        for index in range(len(clues))
    ]
    count = len(clues)
    clues_complete = builder.node(
        24,
        "questLogicalAndNodeDefinition",
        input_names=tuple(f"In{i}" for i in range(1, count + 1)),
        output_names=("Out1",),
        properties={"inputSocketCount": count, "outputSocketCount": 1},
    )
    succeeded_objective = objective_node(builder, 25, data["objective"])
    completed = fact_node(builder, 13, data["completion_fact"])
    builder.connect(start, active_objective, destination_socket="Active")
    builder.connect(active_objective, park_player)
    builder.connect(park_player, hide_player)
    builder.connect(hide_player, scene, destination_socket="start")
    builder.connect(hide_player, enable_exit_delay)
    for clue in clues:
        builder.connect(hide_player, clue)
    builder.connect(enable_exit_delay, enable_exit)
    for index, (clue, counter) in enumerate(zip(clues, counters), 1):
        builder.connect(clue, counter, destination_socket="Increment")
    for index, counter in enumerate(counters, 1):
        builder.connect(counter, clues_complete, destination_socket=f"In{index}")
    builder.connect(
        clues_complete,
        succeeded_objective,
        source_socket="Out1",
        destination_socket="Succeeded",
    )
    builder.connect(succeeded_objective, completed)
    for source_socket in data.get(
        "scene_exit_sockets", ["complete", "end", "Default INT", "Default RET"]
    ):
        builder.connect_to_earlier_input(scene, teardown, source_socket=source_socket)
    builder.connect(teardown, restore_player)
    builder.connect(restore_player, show_player)
    builder.connect(show_player, settle)
    finish(builder, settle, end)
    return finish_document(builder, archive, stage)


def seconds_delay(builder, number, seconds):
    milliseconds = round(seconds * 1000)
    return realtime_delay_node(
        builder, number, seconds=milliseconds // 1000, milliseconds=milliseconds % 1000
    )


def build_generated_meet_contact_phase(stage, archive: Path):
    """GQ000's root-owned UI and broad setup gate, with explicit scene ports."""
    from phase_graph import (
        character_spawned_node,
        trigger_condition_node as player_trigger,
    )
    from quest_compiler import checkpoint_node

    data = stage.data
    builder = PhaseGraphBuilder()
    start, end = entry_node(builder, stage), exit_node(builder, stage)
    spawn = community_action_node(builder, 10, data["community"], "Activate")
    action = spawn.data["actions"][0]["type"]["Data"]
    action["communityEntryName"] = cname(data["contact"])
    action["communityEntryPhaseName"] = cname(data.get("community_phase", "default"))
    ready = character_spawned_node(builder, 256, data["community"])
    setup = player_trigger(builder, 100, data["setup_trigger"], "IsInside")
    checkpoint = checkpoint_node(builder, 44, data.get("meeting_checkpoint", stage.id))
    entry = data.get("scene_entry", "start")
    accept, defer = data.get("accept_exit", "job_accept"), data.get("defer_exit", "end")
    scene = scene_node(
        builder,
        11,
        data["scene"],
        data["scene_origin"],
        output_names=(defer, accept, "Default INT", "Default RET"),
    )
    scene.inputs["start"]["Data"]["name"] = cname(entry)
    done = objective_node(builder, 300, data["objective"])
    done.data["type"]["Data"]["trackQuest"] = 0
    hide = mappin_node(builder, 301, data["mappin"])
    accepted = fact_node(builder, 302, data["accepted_fact"])
    builder.connect(start, spawn)
    builder.connect(spawn, ready)
    builder.connect(ready, setup)
    builder.connect(setup, checkpoint)
    builder.connect(checkpoint, scene, destination_socket="start")
    builder.connect(scene, done, source_socket=accept, destination_socket="Succeeded")
    builder.connect(done, hide, destination_socket="Inactive")
    builder.connect(hide, accepted)
    if data.get("defer_policy", "terminate") == "rearm":
        outside = player_trigger(builder, 303, data["rearm_trigger"], "IsOutside")
        builder.connect(scene, outside, source_socket=defer)
        builder.connect_to_earlier_input(outside, setup)
    else:
        builder.connect_to_earlier_output(scene, end, source_socket=defer)
    finish(builder, accepted, end)
    return finish_document(builder, archive, stage)


def build_generated_choice_gate_phase(stage, archive: Path):
    """Two fact-backed alternatives which set a branch fact and reconverge."""
    data = stage.data
    builder = PhaseGraphBuilder()
    start, end = (entry_node(builder, stage), exit_node(builder, stage))
    branch_a = fact_condition_node(
        builder, 10, data["branches"][0]["condition"], comparison="Greater", value=0
    )
    branch_b = fact_condition_node(
        builder, 11, data["branches"][1]["condition"], comparison="Greater", value=0
    )
    choose_a = fact_node(builder, 12, data["branches"][0]["set_fact"])
    choose_b = fact_node(builder, 13, data["branches"][1]["set_fact"])
    join = logical_xor_node(builder, 14, input_count=2)
    builder.connect(start, branch_a)
    builder.connect(start, branch_b)
    builder.connect(branch_a, choose_a)
    builder.connect(branch_b, choose_b)
    builder.connect(choose_a, join, destination_socket="In1")
    builder.connect(choose_b, join, destination_socket="In2")
    builder.connect_to_earlier_output(join, end, source_socket="Out1")
    return finish_document(builder, archive, stage)


def build_generated_defend_target_phase(stage, archive: Path):
    if stage.data.get("block_on_failure", False):
        return build_generated_defend_target_retry_phase(stage, archive)
    data = stage.data
    builder = PhaseGraphBuilder()
    start, end = (entry_node(builder, stage), exit_node(builder, stage))
    active = objective_node(builder, 10, data["objective"])
    complete = fact_condition_node(
        builder, 11, data["completion_fact"], comparison="Greater", value=0
    )
    killed = character_killed(builder, 12, data["community"], data["entry"])
    success = objective_node(builder, 13, data["objective"])
    failure = objective_node(builder, 14, data["objective"])
    failed_fact = fact_node(builder, 15, data["failure_fact"])
    join = logical_xor_node(builder, 16, input_count=2)
    builder.connect(start, active, destination_socket="Active")
    builder.connect(active, complete)
    builder.connect(active, killed)
    builder.connect(complete, success, destination_socket="Succeeded")
    builder.connect(killed, failure, destination_socket="Failed")
    builder.connect(success, join, destination_socket="In1")
    builder.connect(failure, failed_fact)
    builder.connect(failed_fact, join, destination_socket="In2")
    finish(builder, join, end, source_socket="Out1")
    return finish_document(builder, archive, stage)


def build_generated_defend_target_retry_phase(stage, archive: Path):
    """Fail the objective without emitting Out1 so a retry checkpoint can reload."""
    data = stage.data
    builder = PhaseGraphBuilder()
    start, end = (entry_node(builder, stage), exit_node(builder, stage))
    active = objective_node(builder, 10, data["objective"])
    complete = fact_condition_node(
        builder, 11, data["completion_fact"], comparison="Greater", value=0
    )
    killed = character_killed(builder, 12, data["community"], data["entry"])
    success = objective_node(builder, 13, data["objective"])
    failure = objective_node(builder, 14, data["objective"])
    failed_fact = fact_node(builder, 15, data["failure_fact"])
    builder.connect(start, active, destination_socket="Active")
    builder.connect(active, complete)
    builder.connect(active, killed)
    builder.connect(complete, success, destination_socket="Succeeded")
    builder.connect(killed, failure, destination_socket="Failed")
    builder.connect(failure, failed_fact)
    finish(builder, success, end)
    return finish_document(builder, archive, stage)


def build_generated_escort_npc_phase(stage, archive: Path):
    data = {
        **stage.data,
        "route_mappins": stage.data.get("route_mappins", [stage.data["mappin"]] * 3),
    }
    builder = PhaseGraphBuilder()
    start, end = (entry_node(builder, stage), exit_node(builder, stage))
    active = objective_node(builder, 10, data["objective"])
    pin_1_on = mappin_node(builder, 11, data["route_mappins"][0])
    ai = puppet_ai_tier(builder, 12, data["community"], data["entry"])
    follow = assign_follower_role(builder, 13, data["community"], data["entry"])
    actor = entity_reference(data["community"], names=(data["entry"],))
    gate_1 = trigger_condition(builder, 14, data["destinations"][0], actor)
    pin_1_off = mappin_node(builder, 15, data["route_mappins"][0])
    pin_2_on = mappin_node(builder, 16, data["route_mappins"][1])
    gate_2 = trigger_condition(builder, 17, data["destinations"][1], actor)
    pin_2_off = mappin_node(builder, 18, data["route_mappins"][1])
    pin_3_on = mappin_node(builder, 19, data["route_mappins"][2])
    gate_3 = trigger_condition(builder, 20, data["destinations"][2], actor)
    clear = clear_ai_role(builder, 21, data["community"], data["entry"])
    done = objective_node(builder, 22, data["objective"])
    pin_3_off = mappin_node(builder, 23, data["route_mappins"][2])
    fact = fact_node(builder, 24, data["completion_fact"])
    builder.connect(start, active, destination_socket="Active")
    builder.connect(active, pin_1_on, destination_socket="Active")
    builder.connect(pin_1_on, ai)
    builder.connect(ai, follow)
    builder.connect(follow, gate_1, source_socket="Success")
    builder.connect(gate_1, pin_1_off, destination_socket="Inactive")
    builder.connect(pin_1_off, pin_2_on, destination_socket="Active")
    builder.connect(pin_2_on, gate_2)
    builder.connect(gate_2, pin_2_off, destination_socket="Inactive")
    builder.connect(pin_2_off, pin_3_on, destination_socket="Active")
    builder.connect(pin_3_on, gate_3)
    builder.connect(gate_3, clear)
    builder.connect(
        clear, done, source_socket="Success", destination_socket="Succeeded"
    )
    builder.connect(done, pin_3_off, destination_socket="Inactive")
    builder.connect(pin_3_off, fact)
    finish(builder, fact, end)
    return finish_document(builder, archive, stage)


def build_generated_deliver_drop_point_phase(stage, archive: Path):
    """Single-item inventory/reservation/deposit; branch delivery stays shared."""
    from phase_graph import reserve_drop_point_node

    data = stage.data
    builder = PhaseGraphBuilder()
    start, end = entry_node(builder, stage), exit_node(builder, stage)
    previous = start
    if data.get("objective"):
        active = objective_node(builder, 10, data["objective"])
        builder.connect(previous, active, destination_socket="Active")
        previous = active
    if data.get("mappin"):
        pin = mappin_node(builder, 11, data["mappin"])
        builder.connect(previous, pin, destination_socket="Active")
        previous = pin
    inventory = inventory_condition_node(builder, 12, data["item"])
    reserve = reserve_drop_point_node(builder, 13, data["item"], data["drop_point"])
    deposited = fact_condition_node(builder, 14, data["deposit_fact"])
    builder.connect(previous, inventory)
    builder.connect(inventory, reserve)
    builder.connect(inventory, deposited)
    previous = deposited
    if data.get("objective"):
        done = objective_node(builder, 15, data["objective"])
        builder.connect(previous, done, destination_socket="Succeeded")
        previous = done
    if data.get("mappin"):
        hide = mappin_node(builder, 16, data["mappin"])
        builder.connect(previous, hide, destination_socket="Inactive")
        previous = hide
    finish(builder, previous, end)
    return finish_document(builder, archive, stage)


BUILDERS = {
    name: globals()[f"build_generated_{name}_phase"]
    for name in (
        "optional_condition",
        "stealth_monitor",
        "plant_item",
        "release_or_rescue_npc",
        "enter_vehicle",
        "drive_to",
        "steal_vehicle",
        "deliver_vehicle",
        "vehicle_cleanup",
        "carry_npc",
        "ride_with_contact",
        "braindance_analysis",
        "meet_contact",
        "choice_gate",
        "escort_npc",
        "defend_target",
        "deliver_drop_point",
    )
}
