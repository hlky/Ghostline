"""Check bound entries and terminal/notification ports against typed resources."""

from quest_flow import walk


def scene_interface(document, *, entries=(), exits=()):
    root = document["Data"]["RootChunk"]
    problems = []
    for table, kind, required in (
        ("entryPoints", "scnStartNode", entries),
        ("exitPoints", "scnEndNode", exits),
    ):
        points = {
            point.get("name", {}).get("$value"): point.get("nodeId", {}).get("id")
            for point in root.get(table, [])
        }
        nodes = {
            node.get("nodeId", {}).get("id")
            for node in walk(root.get("sceneGraph", {}))
            if node.get("$type") == kind
        }
        for name in required:
            if name not in points or points[name] not in nodes:
                problems.append(f"{table}: {name} does not resolve to {kind}")
    return problems


def phase_interface(document, *, entry, exits, notifications=()):
    nodes = list(walk(document))
    entries = {
        node.get("socketName", {}).get("$value")
        for node in nodes
        if node.get("$type") == "questInputNodeDefinition"
    }
    outputs = {
        node.get("socketName", {}).get("$value"): node.get("type")
        for node in nodes
        if node.get("$type") == "questOutputNodeDefinition"
    }
    problems = []
    if entry not in entries:
        problems.append(f"missing phase entry {entry}")
    for alias, socket in exits.items():
        expected = "NonTerminating" if alias in notifications else "Terminating"
        if outputs.get(socket) != expected:
            problems.append(
                f"phase output {socket} requires {expected}, found {outputs.get(socket)!r}"
            )
    return problems


def bound_interfaces(stage):
    """Typed bindings and explicit ports; legacy scene exit supersets stay optional."""
    stage_type = stage.data.get("type", getattr(stage, "type", None))
    if stage_type == "meet_contact" and not stage.data.get("phase_template"):
        yield (
            stage.data["scene"],
            "scene",
            {
                "entries": (stage.data.get("scene_entry", "start"),),
                "exits": tuple(
                    stage.data[key]
                    for key in ("accept_exit", "defer_exit")
                    if key in stage.data
                ),
            },
        )
    if stage_type == "braindance_analysis" and not stage.data.get("phase_template"):
        # Legacy graphs listen to a superset of scene exits (for example GQT005
        # exports complete but not end). Only explicitly requested exits are a
        # required scene contract; engine interruption/return sockets are global.
        exits = stage.data.get("scene_exit_sockets", ())
        yield (
            stage.data["scene"],
            "scene",
            {
                "entries": (stage.data.get("scene_entry", "start"),),
                "exits": tuple(
                    name for name in exits if name not in {"Default INT", "Default RET"}
                ),
            },
        )
    for item in walk(stage.data):
        if "entry" in item and "exits" in item:
            if "phase" in item:
                notifications = (
                    stage.data.get("notifications", {})
                    if item is stage.data.get("child")
                    else ()
                )
                yield (
                    item["phase"],
                    "phase",
                    {
                        "entry": item["entry"],
                        "exits": item["exits"],
                        "notifications": notifications,
                    },
                )
            elif "scene" in item:
                yield (
                    item["scene"],
                    "scene",
                    {
                        "entries": (item["entry"],),
                        "exits": tuple(item["exits"].values()),
                    },
                )
        elif item.get("kind") == "phase":
            yield (
                item["phase"],
                "phase",
                {"entry": item["entry"], "exits": {"done": item["exit"]}},
            )


def audit_bound_interfaces(stage, resolver):
    from quest_types import Diagnostic

    result = []
    for resource, kind, binding in bound_interfaces(stage):
        try:
            document = resolver(resource)
            problems = (phase_interface if kind == "phase" else scene_interface)(
                document, **binding
            )
        except (OSError, ValueError, KeyError, TypeError) as exc:
            problems = [f"missing typed interface evidence: {exc}"]
        for problem in problems:
            result.append(
                Diagnostic(
                    "warning" if stage.status == "planned" else "error",
                    "invalid_bound_interface",
                    f"{resource}: {problem}",
                    stage.id,
                )
            )
    return result
