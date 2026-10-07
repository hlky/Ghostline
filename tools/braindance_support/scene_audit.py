"""Independent actor, camera, and lifecycle audits of authored braindance scenes."""
from __future__ import annotations
import math
from typing import Any
from braindance_support.scene_graph import (
    SceneGraphIndex,
)
from braindance_support.scene_types import (
    _root,
    _walk,
)
from braindance_support.clues import (
    audit_clues,
)


def audit_scene_document(
    document: dict[str, Any],
    *,
    handoff: dict[str, Any] | None = None,
    require_functional_exit: bool = True,
    require_functional_clues: bool = True,
) -> dict[str, Any]:
    errors: list[str] = []
    root = _root(document, "scnSceneResource")
    all_values = list(_walk(root))
    type_counts: dict[str, int] = {}
    for value in all_values:
        type_name = value.get("$type")
        if isinstance(type_name, str):
            type_counts[type_name] = type_counts.get(type_name, 0) + 1
    if type_counts.get("scnRewindableSectionNode", 0) < 1:
        errors.append("Scene has no scnRewindableSectionNode")
    if type_counts.get("scneventsPlayRidCameraAnimEvent", 0) < 1:
        errors.append("Scene has no RID camera event")
    camera_events = [
        value
        for value in all_values
        if value.get("$type") == "scneventsPlayRidCameraAnimEvent"
    ]
    camera_refs = [
        event.get("cameraRef", {}).get("$value")
        for event in camera_events
        if isinstance(event.get("cameraRef"), dict)
    ]
    if camera_events and not any(
        isinstance(camera_ref, str) and camera_ref not in {"", "0"}
        for camera_ref in camera_refs
    ):
        errors.append("Scene RID camera events have no bound camera NodeRef")
    if type_counts.get("scneventsBraindanceVisibilityEvent", 0) < 1:
        errors.append("Scene has no braindance visibility event")
    actor_definitions = [
        *root.get("actors", []),
        *root.get("playerActors", []),
    ]
    actor_ids = sorted(
        actor.get("actorId", {}).get("id")
        for actor in actor_definitions
        if isinstance(actor.get("actorId", {}).get("id"), int)
    )
    if actor_ids != list(range(len(actor_ids))):
        errors.append(
            "Scene actor IDs must be dense from zero; found "
            + ", ".join(str(actor_id) for actor_id in actor_ids)
        )
    prop_ids = sorted(
        prop.get("propId", {}).get("id")
        for prop in root.get("props", [])
        if isinstance(prop.get("propId", {}).get("id"), int)
    )
    if prop_ids != list(range(len(prop_ids))):
        errors.append(
            "Scene prop IDs must be dense from zero; found "
            + ", ".join(str(prop_id) for prop_id in prop_ids)
        )
    prop_by_performer = {
        2 + (int(prop["propId"]["id"]) << 8): prop
        for prop in root.get("props", [])
        if isinstance(prop, dict)
        and isinstance(prop.get("propId", {}).get("id"), int)
    }
    visibility_targets: list[str] = []
    for event in all_values:
        if event.get("$type") != "scneventsBraindanceVisibilityEvent":
            continue
        performer_id = event.get("performerId", {}).get("id")
        prop = prop_by_performer.get(performer_id)
        if prop is None:
            errors.append(
                "Braindance visibility event targets non-prop performer "
                f"{performer_id}"
            )
            continue
        prop_name = str(prop.get("propName", ""))
        visibility_targets.append(prop_name)
    visibility_target_names = {
        "bdview"
        if "bdview" in name.casefold()
        else "bdfog"
        if "bdfog" in name.casefold()
        else name.casefold()
        for name in visibility_targets
    }
    missing_visibility_targets = {"bdview", "bdfog"} - visibility_target_names
    if missing_visibility_targets:
        errors.append(
            "Braindance visibility events do not target: "
            + ", ".join(sorted(missing_visibility_targets))
        )
    references = root.get("resouresReferences", {})
    if not isinstance(references, dict):
        references = {}
    actor_reference_fields = {
        "animSets": "ridAnimSets",
        "facialAnimSets": "ridFacialAnimSets",
        "cyberwareAnimSets": "ridCyberwareAnimSets",
    }
    body_performers = {
        value.get("performer", {}).get("id")
        for value in all_values
        if value.get("$type") == "scnPlaySkAnimEvent"
    }
    root_motion_samples: dict[int, int] = {}
    for event in all_values:
        if event.get("$type") != "scnPlaySkAnimEvent":
            continue
        performer_id = event.get("performer", {}).get("id")
        root_motion = event.get("rootMotionData")
        if not isinstance(root_motion, dict) or root_motion.get("enabled") != 1:
            errors.append(
                f"Body performer {performer_id} has no enabled root motion"
            )
            continue
        trajectory = root_motion.get("trajectoryLOD")
        if not isinstance(trajectory, list) or len(trajectory) < 2:
            errors.append(
                f"Body performer {performer_id} has no root-motion trajectory"
            )
            continue
        times = [float(sample.get("time", -1.0)) for sample in trajectory]
        event_duration = float(event.get("duration", 0)) / 1000.0
        if times != sorted(times):
            errors.append(
                f"Body performer {performer_id} root-motion times decrease"
            )
        if times[0] < 0.0 or not math.isclose(
            times[-1],
            event_duration,
            abs_tol=1e-4,
        ):
            errors.append(
                f"Body performer {performer_id} root motion ends at "
                f"{times[-1]:g}s, event ends at {event_duration:g}s"
            )
        root_motion_samples[int(performer_id)] = len(trajectory)
    auxiliary_performers: dict[str, set[int | None]] = {
        "facialAnimSets": set(),
        "cyberwareAnimSets": set(),
    }
    for value in all_values:
        if value.get("$type") != "scnPlayRidAnimEvent":
            continue
        actor_field = (
            "cyberwareAnimSets"
            if value.get("actorComponent", {}).get("$value") == "cyberware"
            else "facialAnimSets"
        )
        auxiliary_performers[actor_field].add(
            value.get("performer", {}).get("id")
        )
    for actor in actor_definitions:
        actor_name = actor.get("actorName", actor.get("playerName", "<actor>"))
        actor_id = actor.get("actorId", {}).get("id")
        performer_id = (
            1 + (int(actor_id) << 8)
            if isinstance(actor_id, int)
            else None
        )
        if performer_id in body_performers and not actor.get("animSets"):
            errors.append(f"Actor {actor_name} has no bound RID body set")
        for actor_field, label in (
            ("facialAnimSets", "facial"),
            ("cyberwareAnimSets", "cyberware"),
        ):
            if (
                performer_id in auxiliary_performers[actor_field]
                and not actor.get(actor_field)
            ):
                errors.append(
                    f"Actor {actor_name} has no bound RID {label} set"
                )
        for actor_field, reference_field in actor_reference_fields.items():
            reference_count = len(references.get(reference_field, []))
            for reference in actor.get(actor_field, []):
                reference_id = reference.get("id")
                if (
                    not isinstance(reference_id, int)
                    or reference_id < 0
                    or reference_id >= reference_count
                ):
                    errors.append(
                        f"Actor {actor_name} has invalid {actor_field} "
                        f"reference {reference_id}"
                    )
        lipsync = actor.get("lipsyncAnimSet")
        if isinstance(lipsync, dict):
            lipsync_id = lipsync.get("id")
            lipsync_count = len(references.get("lipsyncAnimSets", []))
            if (
                lipsync_id != 0xFFFFFFFF
                and (
                    not isinstance(lipsync_id, int)
                    or lipsync_id < 0
                    or lipsync_id >= lipsync_count
                )
            ):
                errors.append(
                    f"Actor {actor_name} has invalid lipsyncAnimSet "
                    f"reference {lipsync_id}"
                )
    rid_animation_count = len(references.get("ridAnimations", []))
    for index, animation_set in enumerate(references.get("ridAnimSets", [])):
        for animation in animation_set.get("animations", []):
            animation_id = animation.get("id")
            if (
                not isinstance(animation_id, int)
                or animation_id < 0
                or animation_id >= rid_animation_count
            ):
                errors.append(
                    f"RID animation set {index} has invalid animation "
                    f"reference {animation_id}"
                )
    graph = SceneGraphIndex(root)
    node_by_id = graph.nodes
    outgoing = graph.outgoing
    nested_type = graph.nested_type
    reachable = graph.reachable
    clue_report = audit_clues(root, all_values, graph, handoff, require_functional_clues, errors)
    exit_points = root.get("exitPoints", [])
    exit_node_ids = {
        point.get("nodeId", {}).get("id")
        for point in exit_points
        if isinstance(point, dict)
        and isinstance(point.get("nodeId", {}).get("id"), int)
    }
    has_declared_exit = isinstance(exit_points, list) and bool(exit_points)
    if not has_declared_exit:
        errors.append("Scene has no exit point")
    elif require_functional_exit and not exit_node_ids:
        errors.append("Scene exit point has no target node")
    elif require_functional_exit and any(
        node_by_id.get(node_id, {}).get("$type") != "scnEndNode"
        for node_id in exit_node_ids
    ):
        errors.append("Scene exit points do not target End nodes")

    finish_node_ids = {
        node_id
        for node_id in node_by_id
        if nested_type(node_id, "questEnableBraindanceFinish_NodeType")
    }
    if require_functional_exit and not finish_node_ids:
        errors.append("Scene never enables the braindance Finish action")

    exit_action_node_ids = {
        node_id
        for node_id in node_by_id
        if any(
            item.get("$type") == "questInputAction_ConditionType"
            and item.get("inputAction", {}).get("$value")
            == "ExitBraindance"
            for item in _walk(node_by_id[node_id])
        )
    }
    if require_functional_exit and not exit_action_node_ids:
        errors.append("Scene does not consume the ExitBraindance action")

    finish_reachable = reachable(finish_node_ids)
    if (
        require_functional_exit
        and finish_node_ids
        and exit_action_node_ids
        and not (finish_reachable & exit_action_node_ids)
    ):
        errors.append(
            "Braindance Finish UI cannot reach the ExitBraindance condition"
        )

    exit_reachable = reachable(exit_action_node_ids)
    correct_end_edge = any(
        target in exit_node_ids
        and ordinal == 0
        and source in exit_reachable
        for source in exit_reachable
        for target, ordinal in outgoing(source)
    )
    if (
        require_functional_exit
        and exit_action_node_ids
        and exit_node_ids
        and not correct_end_edge
    ):
        errors.append(
            "ExitBraindance cannot reach a registered End at input ordinal 0"
        )

    rewind_node_ids = {
        node_id
        for node_id, node in node_by_id.items()
        if node.get("$type") == "scnRewindableSectionNode"
    }
    delay_node_ids = {
        node_id
        for node_id in node_by_id
        if nested_type(node_id, "questRealtimeDelay_ConditionType")
    }
    rewind_loop = any(
        delay in delay_node_ids
        and delay_ordinal == 1
        and any(
            target == rewind and ordinal == 0
            for target, ordinal in outgoing(delay)
        )
        for rewind in rewind_node_ids
        for delay, delay_ordinal in outgoing(rewind)
    )
    if require_functional_exit and rewind_node_ids and not rewind_loop:
        errors.append(
            "Rewindable section has no delayed loop back to input ordinal 0"
        )

    exit_audio = any(
        item.get("$type") == "questAudioMixNodeType"
        and item.get("mixSignpost", {}).get("$value")
        == "exit_braindance"
        for node_id in exit_reachable
        for item in _walk(node_by_id.get(node_id, {}))
    )
    if (
        require_functional_exit
        and exit_action_node_ids
        and not exit_audio
    ):
        errors.append("ExitBraindance path has no exit_braindance audio mix")

    normal_exit_present = (
        bool(
            exit_node_ids
            and finish_node_ids
            and exit_action_node_ids
            and (finish_reachable & exit_action_node_ids)
            and correct_end_edge
        )
        if require_functional_exit
        else has_declared_exit
    )
    interruption_scenarios = root.get("interruptionScenarios", [])
    enabled_interruptions = [
        scenario
        for scenario in interruption_scenarios
        if isinstance(scenario, dict) and scenario.get("enabled") == 1
    ]
    rid_resources = root.get("ridResources")
    if not isinstance(rid_resources, list) or len(rid_resources) != 1:
        errors.append("Scene must link exactly one authored RID resource")
    return {
        "schema_version": 1,
        "kind": "ghostline_braindance_scene_audit",
        "ok": not errors,
        "errors": errors,
        **clue_report,
        "type_counts": type_counts,
        "camera_refs": camera_refs,
        "visibility_targets": visibility_targets,
        "root_motion_samples": root_motion_samples,
        "rewindable": type_counts.get("scnRewindableSectionNode", 0) > 0,
        "layer_switching": type_counts.get(
            "scneventsBraindanceVisibilityEvent", 0
        )
        > 0,
        "normal_exit_present": normal_exit_present,
        "finish_action_enabled": bool(finish_node_ids),
        "exit_action_consumed": bool(exit_action_node_ids),
        "rewind_loop_present": rewind_loop,
        "interruption_scenario_present": bool(interruption_scenarios),
        "enabled_interruption_scenarios": len(enabled_interruptions),
        "normal_exit_cleanup": normal_exit_present and exit_audio,
        "interrupted_cleanup": False,
    }
