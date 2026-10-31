"""Owned quest lifetimes, built from the existing RED graph primitives.

An activation chooses one terminal route, retires competing listeners, restores
its owned state, then emits its outcome. Cuts use the Chapel permanent-cut
pattern; scheduling and checkpoint persistence still require installed testing.
"""

from __future__ import annotations

from typing import Any

from phase_graph import (
    GraphNode,
    add_item_node,
    cname,
    community_action_node,
    fact_condition_node,
    journal_entry_node,
    logical_and_node,
    logical_xor_node,
    mappin_node,
    node_ref,
    objective_node,
    resource_ref,
)
from quest_block_builders import BlockBuilder, Signal, _instant
from quest_encounter import scene_flow_node


def child_node(builder, number, phase, entry, exits):
    return builder.node(
        number,
        "questPhaseNodeDefinition",
        input_names=(entry,),
        output_names=tuple(exits),
        properties={
            "phaseGraph": None,
            "phaseInstancePrefabs": [],
            "phaseResource": resource_ref(phase),
            "saveLock": 0,
            "unfreezingTriggerNodeRef": node_ref("0", storage="uint64"),
        },
    )


def cut_node(builder, number):
    return builder.node(
        number,
        "questCutControlNodeDefinition",
        input_names=("In",),
        output_names=("Out", "CutSource"),
        properties={"permanent": 1},
    )


def environment_node(builder, number, action):
    if action["kind"] == "weather_reset":
        operation = {
            "$type": "questPlayEnv_SetWeather",
            "reset": 1,
            "source": cname(action["source"]),
            "blendTime": action.get("blend_seconds", 5),
            "priority": 0,
            "weatherID": {"$type": "TweakDBID", "$storage": "uint64", "$value": "0"},
        }
        kind = "questEnvironmentManagerNodeDefinition"
    else:
        operation = {
            "$type": "questTogglePrefabVariant_NodeType",
            "params": [
                {
                    "$type": "questTogglePrefabVariant_NodeTypeParams",
                    "prefabNodeRef": node_ref(action["prefab"]),
                    "variantStates": [
                        {
                            "$type": "questVariantState",
                            "name": cname(action["variant"]),
                            "show": int(action["show"]),
                        }
                    ],
                }
            ],
        }
        kind = "questWorldDataManagerNodeDefinition"
    return builder.node(
        number,
        kind,
        input_names=("In",),
        properties={"type": builder.handles.wrap(operation)},
    )


class OwnedScope(BlockBuilder):
    """A single activation epoch; durable state is always an explicit fact.

    A committed re-entry bypasses setup and effects. Completion is written only
    after restoration. Cancellation during restoration cannot abandon it: the
    cancellation listener is retired when the terminal route is selected.
    """

    def __init__(self, stage):
        super().__init__(stage)
        self.owned: list[GraphNode] = []
        self.initial_cancel = None
        self.activation = self.start

    def watch(self, factory, *args, **kwargs) -> Signal:
        result = self.node(factory, *args, **kwargs)
        self.owned.append(result.node)
        return result

    def snapshot(self, source, factory, *args, **kwargs):
        yes, no = _instant(self.node(factory, *args, **kwargs), self)
        self.connect(source, yes)
        return yes, no

    def begin(self) -> Signal:
        source = self.start
        committed = self.stage.data.get("commit_fact")
        if committed:
            done, source = self.snapshot(source, fact_condition_node, committed)
            self.finish(done, "success")
        if self.stage.data.get("cancellation_fact"):
            self.initial_cancel, source = self.snapshot(
                source, fact_condition_node, self.stage.data["cancellation_fact"]
            )
        self.activation = source
        return self.actions(source, self.stage.data.get("setup", []))

    def child(self, source, spec) -> dict[str, Signal]:
        child = self.watch(
            child_node, spec["phase"], spec["entry"], tuple(spec["exits"].values())
        )
        self.connect(source, child, spec["entry"])
        return {
            outcome: Signal(child.node, socket)
            for outcome, socket in spec["exits"].items()
        }

    def scene(self, source, spec) -> dict[str, Signal]:
        exits = tuple(spec["exits"].values())
        flow = {
            "scene": spec["scene"],
            "origin": spec["origin"],
            "entry": spec["entry"],
            "exit": exits[0],
            "completion_exits": list(exits[1:]),
        }
        scene = self.watch(scene_flow_node, flow)
        self.connect(source, scene, spec["entry"])
        return {
            outcome: Signal(scene.node, socket)
            for outcome, socket in spec["exits"].items()
        }

    def join(self, signals: list[Signal]) -> Signal:
        if len(signals) == 1:
            return signals[0]
        joined = self.node(logical_and_node, len(signals), socket="Out1")
        for index, signal in enumerate(signals, 1):
            self.connect(signal, joined, f"In{index}")
        return joined

    def once(self, source: Signal) -> Signal:
        gate = self.node(logical_xor_node, 1, socket="Out1")
        return self.append(source, gate, "In1")

    def retire(self, source: Signal, targets: list[GraphNode]) -> Signal:
        cut = self.append(source, self.node(cut_node))
        self.cut_targets(cut, targets)
        return cut

    def cut_targets(self, cut: Signal, targets: list[GraphNode]) -> None:
        for target in dict((id(node), node) for node in targets).values():
            # Every graph node already owns this special socket, but it is not
            # part of PhaseGraphBuilder's ordinary Input map.
            if "CutDestination" not in target.inputs:
                target.inputs["CutDestination"] = next(
                    wrapper
                    for wrapper in target.data["sockets"]
                    if wrapper.get("Data", {}).get("type") == "CutDestination"
                )
            self.graph.connect(
                cut.node,
                target,
                source_socket="CutSource",
                destination_socket="CutDestination",
            )

    def race(self, routes: dict[str, Signal], *, owned=None) -> dict[str, Signal]:
        """First route cuts the other route gates before any side effects.

        Distinct gates preserve the selected outcome without a mutable result
        fact. The permanent cut also fences already queued competing signals.
        """
        gates = {name: self.once(signal) for name, signal in routes.items()}
        targets = self.owned if owned is None else owned
        cuts = {
            name: self.append(signal, self.node(cut_node))
            for name, signal in gates.items()
        }
        for name, cut in cuts.items():
            self.cut_targets(
                cut,
                [
                    *targets,
                    *[other.node for key, other in gates.items() if key != name],
                    *[other.node for key, other in cuts.items() if key != name],
                ],
            )
        return cuts

    def actions(self, source: Signal, actions: list[dict[str, Any]]) -> Signal:
        for action in actions:
            kind = action["kind"]
            if kind == "fact":
                source = self.fact(source, action["fact"], action.get("value", 1))
            elif kind == "item":
                source = self.append(
                    source,
                    self.node(add_item_node, action["item"], action.get("quantity", 1)),
                )
            elif kind == "objective":
                source = self.append(
                    source, self.node(objective_node, action["path"]), action["state"]
                )
            elif kind == "mappin":
                source = self.append(
                    source, self.node(mappin_node, action["path"]), action["state"]
                )
            elif kind == "message":
                source = self.append(
                    source,
                    self.node(
                        journal_entry_node, action["path"], "gameJournalPhoneMessage", 1
                    ),
                    action.get("state", "Active"),
                )
            elif kind == "community":
                target = self.node(
                    community_action_node, action["community"], action["action"]
                )
                operation = target.node.data["actions"][0]["type"]["Data"]
                operation["communityEntryName"] = cname(action["entry"])
                operation["communityEntryPhaseName"] = cname(
                    action.get("phase", "default")
                )
                source = self.append(source, target)
            elif kind in {"weather_reset", "prefab_variant"}:
                source = self.append(source, self.node(environment_node, action))
            elif kind == "phase":
                source = self.child(
                    source,
                    {
                        "phase": action["phase"],
                        "entry": action["entry"],
                        "exits": {"done": action["exit"]},
                    },
                )["done"]
            else:
                raise ValueError(f"Unsupported scope action: {kind}")
        return source

    def finish_routes(self, source, routes):
        cancellation = self.stage.data.get("cancellation_fact")
        if cancellation:
            cancelled = self.watch(fact_condition_node, cancellation)
            self.connect(self.activation, cancelled)
            if self.initial_cancel is not None:
                gate = self.node(logical_xor_node, 2, socket="Out1")
                self.connect(self.initial_cancel, gate, "In1")
                self.connect(cancelled, gate, "In2")
                cancelled = gate
            routes = {**routes, "cancelled": cancelled}
        for outcome, selected in self.race(routes).items():
            restored = self.actions(selected, self.stage.data.get("restore", []))
            committed = self.actions(
                restored, self.stage.data.get("effects", {}).get(outcome, [])
            )
            if outcome == "success":
                committed = self.fact(committed, self.stage.data.get("commit_fact"))
            self.finish(committed, outcome)
