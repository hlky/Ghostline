"""Small independent emitted-graph model, not a REDengine/save simulation.

Cuts fence queued signals; AND/XOR latch once; scenes/children and timers wait
for explicit test events. Native scheduling and persistence remain playtests.
"""

from collections import defaultdict, deque

from quest_flow import walk


class ScopeRun:
    def __init__(
        self, document, *, facts=None, items=None, random_choice=1, targets=None
    ):
        self.defs = {
            str(x["HandleId"]): x["Data"] for x in walk(document) if "HandleId" in x
        }
        self.nodes = {
            key: value for key, value in self.defs.items() if "sockets" in value
        }
        self.owners = {}
        self.outputs = defaultdict(list)
        for key, node in self.nodes.items():
            for wrapper in node["sockets"]:
                socket = self.resolve(wrapper)
                self.owners[self.handle(wrapper)] = (key, socket["name"]["$value"])
                if socket["type"] == "Output":
                    self.outputs[key].append(socket["name"]["$value"])
        self.edges = defaultdict(list)
        for node in self.defs.values():
            if node.get("$type") == "graphGraphConnectionDefinition":
                self.edges[self.owners[self.handle(node["source"])]].append(
                    self.owners[self.handle(node["destination"])]
                )
        self.facts, self.items = dict(facts or {}), dict(items or {})
        self.targets = dict(targets or {})
        self.random_choice = random_choice
        self.active, self.cut, self.fired = set(), set(), set()
        self.seen = defaultdict(set)
        self.pending = deque()
        self.trace, self.outcomes = [], []
        self.terminated = False
        start = next(
            key
            for key, node in self.nodes.items()
            if node["$type"] == "questInputNodeDefinition"
        )
        self.emit(start, "Out")
        self.drain()

    @staticmethod
    def handle(wrapper):
        return str(wrapper.get("HandleId", wrapper.get("HandleRefId")))

    def resolve(self, wrapper):
        return self.defs[self.handle(wrapper)]

    def emit(self, key, socket):
        self.pending.extend(self.edges[key, socket])

    def condition(self, node):
        condition = self.resolve(node["condition"])
        nested = condition.get("type")
        return self.resolve(nested) if isinstance(nested, dict) else condition

    def truth(self, condition):
        kind = condition["$type"]
        if kind == "questVarComparison_ConditionType":
            value, expected = (
                self.facts.get(condition["factName"], 0),
                condition["value"],
            )
            return {
                "Greater": value > expected,
                "Equal": value == expected,
                "GreaterOrEqual": value >= expected,
            }[condition["comparisonType"]]
        if kind == "questInventory_ConditionType":
            return (
                self.items.get(condition["itemID"]["$value"], 0)
                >= condition["quantity"]
            )
        if kind == "questCharacterKilled_ConditionType":
            state = self.targets.get(condition["objectRef"]["names"][0]["$value"])
            return bool(state and condition.get(state))
        return False

    def drain(self):
        while self.pending and not self.terminated:
            key, socket = self.pending.popleft()
            if socket == "CutDestination":
                self.cut.add(key)
                self.active.discard(key)
                continue
            if key in self.cut:
                continue
            node = self.nodes[key]
            kind = node["$type"]
            self.trace.append((node, socket))
            if kind == "questCutControlNodeDefinition":
                # This explicit model assumption is checked structurally here;
                # engine signal/cut ordering needs the installed race cases.
                for destination, _ in self.edges[key, "CutSource"]:
                    self.cut.add(destination)
                    self.active.discard(destination)
                self.emit(key, "Out")
                continue
            if kind == "questOutputNodeDefinition":
                self.outcomes.append(node["socketName"]["$value"])
                self.terminated = node["type"] == "Terminating"
                continue
            if kind in {"questPhaseNodeDefinition", "questSceneNodeDefinition"}:
                self.active.add(key)
                continue
            if kind == "questPauseConditionNodeDefinition":
                self.active.add(key)
                if self.truth(self.condition(node)):
                    self.active.remove(key)
                    self.emit(key, "Out")
                continue
            if kind == "questConditionNodeDefinition":
                self.emit(key, "True" if self.truth(self.condition(node)) else "False")
                continue
            if kind in {
                "questLogicalXorNodeDefinition",
                "questLogicalAndNodeDefinition",
            }:
                if key in self.fired:
                    continue
                self.seen[key].add(socket)
                if (
                    kind == "questLogicalAndNodeDefinition"
                    and len(self.seen[key]) < node["inputSocketCount"]
                ):
                    continue
                self.fired.add(key)
            if kind == "questRandomizerNodeDefinition":
                choice = min(self.random_choice, len(node["outputWeights"]))
                self.emit(key, f"Out{choice}")
                continue
            if kind == "questFactsDBManagerNodeDefinition":
                operation = self.resolve(node["type"])
                self.facts[operation["factName"]] = operation["value"]
            if kind == "questItemManagerNodeDefinition":
                operation = self.resolve(self.resolve(node["type"])["params"][0])
                item = operation["itemID"]["$value"]
                self.items[item] = self.items.get(item, 0) + operation["quantity"]
            outputs = self.outputs[key]
            assert len(outputs) == 1, (kind, outputs)
            self.emit(key, outputs[0])

    def events(self, *, facts=None, items=None, scan=None, timer=False, targets=None):
        self.facts.update(facts or {})
        self.items.update(items or {})
        self.targets.update(targets or {})
        for key in sorted(self.active, key=int):
            node = self.nodes[key]
            if node["$type"] != "questPauseConditionNodeDefinition":
                continue
            condition = self.condition(node)
            matched = self.truth(condition)
            if condition["$type"] == "questScan_ConditionType":
                matched = (
                    condition["eventType"] == "Finished"
                    and condition["objectRef"]["reference"]["$value"] == scan
                )
            if condition["$type"] in {
                "questRealtimeDelay_ConditionType",
                "questGameTimeDelay_ConditionType",
            }:
                matched = timer
            if matched:
                self.active.remove(key)
                self.emit(key, "Out")
        self.drain()

    def resource(self, depot, output="Out1", *, notification=False):
        matches = [
            key
            for key in self.active
            if any(
                value.get("$value") == depot
                for value in walk(
                    self.nodes[key].get(
                        "phaseResource", self.nodes[key].get("sceneFile", {})
                    )
                )
            )
        ]
        assert len(matches) == 1, (depot, matches)
        key = matches[0]
        if not notification:
            self.active.remove(key)
        self.emit(key, output)
        self.drain()

    def writes(self, fact):
        return sum(
            1
            for node, _ in self.trace
            if node["$type"] == "questFactsDBManagerNodeDefinition"
            and self.resolve(node["type"])["factName"] == fact
        )

    def has_resource(self, depot):
        return any(
            any(value.get("$value") == depot for value in walk(self.nodes[key]))
            for key in self.active
        )
