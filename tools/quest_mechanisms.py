"""Research-derived recipes sharing an owned lifecycle and explicit bindings.

These builders emit ordinary questphase graphs. They do not install resources,
simulate scene execution, or promote source evidence to runtime acceptance.
"""

from pathlib import Path

from phase_graph import (
    fact_condition_node,
    inventory_condition_node,
    realtime_delay_node,
)
from quest_block_builders import Signal
from quest_encounter import named_character_outcome_node
from quest_scope import OwnedScope


def build_investigate_reactions_phase(stage, archive: Path):
    """Independent Finished scans; each reaction joins before clue completion."""
    from dataclasses import replace
    from phase_graph import logical_xor_node, mappin_node, scan_started_node
    from quest_block_builders import distinct_threshold

    scope = OwnedScope(stage)
    data = stage.data
    running = scope.begin()
    completed = []
    pins = list(
        dict.fromkeys(clue["mappin"] for clue in data["clues"] if clue.get("mappin"))
    )
    for clue in data["clues"]:
        done, remaining = scope.snapshot(
            running, fact_condition_node, clue["completion_fact"]
        )
        if clue.get("mappin"):
            remaining = scope.append(
                remaining, scope.node(mappin_node, clue["mappin"]), "Active"
            )
        scanned, waiting = scope.snapshot(
            remaining, fact_condition_node, clue["scan_fact"]
        )
        scan = scope.watch(scan_started_node, clue["object_ref"])
        scope.connect(waiting, scan)
        scan = scope.fact(scope.once(scan), clue["scan_fact"])
        available = scope.node(logical_xor_node, 2, socket="Out1")
        scope.connect(scanned, available, "In1")
        scope.connect(scan, available, "In2")
        reacted = (
            scope.scene(available, clue["reaction"])["success"]
            if clue.get("reaction")
            else available
        )
        reacted = scope.fact(reacted, clue["completion_fact"])
        clue_done = scope.node(logical_xor_node, 2, socket="Out1")
        scope.connect(done, clue_done, "In1")
        scope.connect(reacted, clue_done, "In2")
        completed.append(clue_done)
    investigated = distinct_threshold(
        scope, completed, data.get("required_count", len(completed))
    )
    routes = {"success": investigated}
    if data.get("discovery_fact"):
        discovered = scope.watch(fact_condition_node, data["discovery_fact"])
        scope.connect(running, discovered)
        joined = scope.node(logical_xor_node, 2, socket="Out1")
        scope.connect(investigated, joined, "In1")
        scope.connect(discovered, joined, "In2")
        routes["success"] = joined
    # Pins are owned by this block and retire on bypass and cancellation too.
    scope.stage = replace(
        stage,
        data={
            **data,
            "restore": [
                *[{"kind": "mappin", "path": pin, "state": "Inactive"} for pin in pins],
                *data.get("restore", []),
            ],
        },
    )
    scope.finish_routes(running, routes)
    return scope.document(archive)


def build_owned_scope_phase(stage, archive: Path):
    scope = OwnedScope(stage)
    running = scope.begin()
    routes = scope.child(running, stage.data["child"])
    # Nonterminating child notifications update milestone facts without
    # entering terminal cleanup. Their native output kind is audited separately.
    for name, fact in stage.data.get("notifications", {}).items():
        scope.fact(routes.pop(name), fact)
    scope.finish_routes(running, routes)
    return scope.document(archive)


def build_acquire_or_use_phase(stage, archive: Path):
    scope = OwnedScope(stage)
    data = stage.data
    running = scope.begin()
    existing, missing = scope.snapshot(
        running,
        inventory_condition_node,
        data["item"],
        quantity=data.get("quantity", 1),
    )
    existing = scope.fact(existing, data.get("existing_fact"))
    acquired = scope.watch(
        inventory_condition_node, data["item"], quantity=data.get("quantity", 1)
    )
    scope.connect(missing, acquired)
    acquired = scope.fact(acquired, data.get("acquired_fact"))
    # Alternative ownership routes converge once; neither proves application.
    from phase_graph import logical_xor_node

    available = scope.node(logical_xor_node, 2, socket="Out1")
    scope.connect(existing, available, "In1")
    scope.connect(acquired, available, "In2")
    routes = scope.child(available, data["application"])
    scope.finish_routes(running, routes)
    return scope.document(archive)


def build_access_routes_phase(stage, archive: Path):
    scope = OwnedScope(stage)
    running = scope.begin()
    candidates = {
        route["id"]: scope.child(running, route)["success"]
        for route in stage.data["routes"]
    }
    # Cut losing access attempts before the shared use/application boundary.
    winners = scope.race(candidates, owned=list(scope.owned))
    from phase_graph import logical_xor_node

    converged = scope.node(logical_xor_node, len(winners), socket="Out1")
    for index, (name, signal) in enumerate(winners.items(), 1):
        signal = scope.fact(signal, stage.data.get("route_facts", {}).get(name))
        scope.connect(signal, converged, f"In{index}")
    routes = scope.child(converged, stage.data["application"])
    scope.finish_routes(running, routes)
    return scope.document(archive)


def build_resolve_and_report_phase(stage, archive: Path):
    scope = OwnedScope(stage)
    data = stage.data
    running = scope.begin()
    resolutions = []
    for target in data["targets"]:
        policy = target["resolution"]
        resolved = scope.watch(
            named_character_outcome_node, target["community"], target["entry"], **policy
        )
        scope.connect(running, resolved)
        resolutions.append(scope.once(resolved))
    resolved = scope.fact(scope.join(resolutions), data["resolved_fact"])
    routes = scope.child(resolved, data["report"])
    # The report fact belongs to the selected successful terminal path, not a
    # scene signal which may lose a cancellation race.
    data = {
        **data,
        "effects": {
            **data.get("effects", {}),
            "success": [
                {"kind": "fact", "fact": data["reported_fact"]},
                *data.get("effects", {}).get("success", []),
            ],
        },
    }
    from dataclasses import replace

    scope.stage = replace(stage, data=data)
    scope.finish_routes(running, routes)
    return scope.document(archive)


def build_observe_lethal_phase(stage, archive: Path):
    """An independent observer whose declared stop fact owns its lifetime."""
    scope = OwnedScope(stage)
    data = stage.data
    running = scope.begin()
    closed, observing = scope.snapshot(running, fact_condition_node, data["stop_fact"])
    for target in data["targets"]:
        killed = scope.watch(
            named_character_outcome_node,
            target["community"],
            target["entry"],
            killed=True,
            unconscious=False,
            defeated=False,
        )
        scope.connect(observing, killed)
        scope.fact(scope.once(killed), target["killed_fact"])
    stop = scope.watch(fact_condition_node, data["stop_fact"])
    scope.connect(observing, stop)
    from phase_graph import logical_xor_node

    finished = scope.node(logical_xor_node, 2, socket="Out1")
    scope.connect(closed, finished, "In1")
    scope.connect(stop, finished, "In2")
    scope.finish_routes(running, {"success": finished})
    return scope.document(archive)


def build_reward_commit_phase(stage, archive: Path):
    scope = OwnedScope(stage)
    data = stage.data
    running = scope.begin()
    ready = scope.watch(fact_condition_node, data["reported_fact"])
    scope.connect(running, ready)
    existing, missing = scope.snapshot(
        ready, inventory_condition_node, data["item"], quantity=data.get("quantity", 1)
    )
    granted = scope.actions(
        missing,
        [{"kind": "item", "item": data["item"], "quantity": data.get("quantity", 1)}],
    )
    verified = scope.watch(
        inventory_condition_node, data["item"], quantity=data.get("quantity", 1)
    )
    scope.connect(granted, verified)
    from phase_graph import logical_xor_node

    delivered = scope.node(logical_xor_node, 2, socket="Out1")
    scope.connect(existing, delivered, "In1")
    scope.connect(verified, delivered, "In2")
    # commit_fact is mandatory and prevents a regrant after consumption/sale.
    scope.finish_routes(running, {"success": delivered})
    return scope.document(archive)


def build_contact_fallback_phase(stage, archive: Path):
    scope = OwnedScope(stage)
    data = stage.data
    running = scope.begin()
    calling = running
    fallbacks = []
    for fact in data.get("unavailable_facts", []):
        unavailable, calling = scope.snapshot(calling, fact_condition_node, fact)
        fallbacks.append(unavailable)
    results = scope.scene(calling, data["call"])
    connected = results.pop("connected")
    fallbacks.extend(results.values())
    from phase_graph import logical_xor_node

    fallback = scope.node(logical_xor_node, len(fallbacks), socket="Out1")
    for index, signal in enumerate(fallbacks, 1):
        scope.connect(signal, fallback, f"In{index}")
    # Arbitrate BEFORE delivering either effect: rejection/mute share one post.
    candidates = {"connected": connected, "fallback": fallback}
    if data.get("cancellation_fact"):
        cancel = scope.watch(fact_condition_node, data["cancellation_fact"])
        scope.connect(running, cancel)
        if scope.initial_cancel is not None:
            from phase_graph import logical_xor_node

            gate = scope.node(logical_xor_node, 2, socket="Out1")
            scope.connect(scope.initial_cancel, gate, "In1")
            scope.connect(cancel, gate, "In2")
            cancel = gate
        candidates["cancelled"] = cancel
    selected = scope.race(candidates)
    for outcome, signal in selected.items():
        if outcome == "fallback":
            signal = scope.actions(
                signal, [{"kind": "message", "path": data["message"]}]
            )
            signal = scope.fact(signal, data["message_fact"])
        elif outcome == "connected":
            signal = scope.fact(signal, data["connected_fact"])
        signal = scope.actions(signal, data.get("restore", []))
        signal = scope.actions(signal, data.get("effects", {}).get(outcome, []))
        scope.finish(signal, outcome)
    return scope.document(archive)


def randomizer_node(builder, number, weights):
    return builder.node(
        number,
        "questRandomizerNodeDefinition",
        input_names=("In",),
        output_names=tuple(f"Out{i}" for i in range(1, len(weights) + 1)),
        properties={"mode": "Random", "outputWeights": weights},
    )


def build_adaptive_timer_phase(stage, archive: Path):
    scope = OwnedScope(stage)
    data = stage.data
    running = scope.begin()
    eligible = running
    if data.get("eligibility_fact"):
        eligible = scope.watch(fact_condition_node, data["eligibility_fact"])
        scope.connect(running, eligible)
    branches = []
    remaining = eligible
    for profile in data.get("profiles", []):
        selected, remaining = scope.snapshot(
            remaining, fact_condition_node, profile["when_fact"]
        )
        branches.append((selected, profile["choices"]))
    branches.append((remaining, data["choices"]))
    waits = []
    for selected, choices in branches:
        randomizer = scope.node(
            randomizer_node, [choice["weight"] for choice in choices]
        )
        scope.connect(selected, randomizer)
        for index, choice in enumerate(choices, 1):
            if data["clock"] == "realtime":
                timer = scope.watch(realtime_delay_node, seconds=choice["seconds"])
            else:
                from quest_compiler import game_time_delay_node

                timer = scope.watch(
                    game_time_delay_node,
                    days=0,
                    hours=0,
                    minutes=0,
                    seconds=choice["seconds"],
                )
            scope.connect(Signal(randomizer.node, f"Out{index}"), timer)
            waits.append(timer)
    from phase_graph import logical_xor_node

    elapsed = scope.node(logical_xor_node, len(waits), socket="Out1")
    for index, timer in enumerate(waits, 1):
        scope.connect(timer, elapsed, f"In{index}")
    ready = elapsed
    if data.get("busy_fact"):
        busy, free = scope.snapshot(elapsed, fact_condition_node, data["busy_fact"])
        released = scope.watch(
            fact_condition_node, data["busy_fact"], comparison="Equal", value=0
        )
        timeout = scope.watch(realtime_delay_node, seconds=data["max_deferral_seconds"])
        scope.connect(busy, released)
        scope.connect(busy, timeout)
        ready = scope.node(logical_xor_node, 3, socket="Out1")
        for index, signal in enumerate((free, released, timeout), 1):
            scope.connect(signal, ready, f"In{index}")
    scope.finish_routes(running, {"success": ready})
    return scope.document(archive)


def build_entitlement_reconcile_phase(stage, archive: Path):
    """Entitlement is an explicit upstream predicate; no payment or delivery."""
    scope = OwnedScope(stage)
    data = stage.data
    running = scope.begin()
    if data.get("vehicle_record"):
        owned, absent = scope.snapshot(
            running, vehicle_available_node, data["vehicle_record"]
        )
    else:
        owned, absent = scope.snapshot(
            running, fact_condition_node, data["entitled_fact"]
        )
    for outcome, signal in scope.race({"owned": owned, "unowned": absent}).items():
        if outcome == "owned":
            signal = scope.fact(signal, data["owned_fact"])
            signal = scope.actions(signal, data["retire"])
        signal = scope.actions(signal, data.get("restore", []))
        signal = scope.actions(signal, data.get("effects", {}).get(outcome, []))
        scope.finish(signal, outcome)
    return scope.document(archive)


def vehicle_available_node(builder, number, record):
    condition = builder.handles.wrap(
        {
            "$type": "questVehicleCondition",
            "type": builder.handles.wrap(
                {
                    "$type": "questVehicleAvailable_ConditionType",
                    "vehicleName": record,
                "vehicleType": "SpecificVehicle",
                }
            ),
        }
    )
    return builder.node(
        number,
        "questPauseConditionNodeDefinition",
        input_names=("In",),
        properties={"condition": condition},
    )


BUILDERS = {
    name: globals()[f"build_{name}_phase"]
    for name in (
        "investigate_reactions",
        "owned_scope",
        "acquire_or_use",
        "access_routes",
        "resolve_and_report",
        "observe_lethal",
        "reward_commit",
        "contact_fallback",
        "adaptive_timer",
        "entitlement_reconcile",
    )
}
