#!/usr/bin/env python3
"""Generate the placed GQT006 Goth Baddie Cyberpsycho quest package."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT = next(
    parent
    for parent in Path(__file__).resolve().parents
    if (parent / "AGENTS.md").is_file()
)
PROJECT = next(parent for parent in Path(__file__).resolve().parents if (parent / "project.json").is_file())
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))


import generate_world as world_builder
import quest_authoring
import quest_build
from quest_content import load
import quest_compiler


NAME = "gqt006_goth_baddie_cyberpsycho"
WORLD_SPEC = (
    PROJECT / "implementation/world/goth-baddie-cyberpsycho.world.json"
)
MANIFEST = PROJECT / "gqt006_goth_baddie_cyberpsycho.quest.json"
JOURNAL_RAW = PROJECT / "source/raw/mod/gqt006/journal/gqt006.journal.json"
JOURNAL_ARCHIVE = PROJECT / "source/archive/mod/gqt006/journal/gqt006.journal"
ONSCREEN_RAW = (
    PROJECT / "source/raw/mod/gqt006/localization/en-us/onscreens/gqt006.json.json"
)
ONSCREEN_ARCHIVE = (
    PROJECT / "source/archive/mod/gqt006/localization/en-us/onscreens/gqt006.json"
)
ROOT_PHASE_RAW = PROJECT / f"source/raw/mod/gqt006/phases/{NAME}.questphase.json"
ROOT_PHASE_ARCHIVE = PROJECT / f"source/archive/mod/gqt006/phases/{NAME}.questphase"


def disconnect_scene_exit(
    document: dict[str, Any],
    *,
    scene_path: str,
    exit_name: str,
) -> None:
    """Leave a scene exit unhandled so it returns to the active quest stage."""

    handles: dict[str, dict[str, Any]] = {}

    def collect(value: Any) -> None:
        if isinstance(value, dict):
            handle_id = value.get("HandleId")
            if isinstance(handle_id, str) and isinstance(value.get("Data"), dict):
                handles[handle_id] = value
            for child in value.values():
                collect(child)
        elif isinstance(value, list):
            for child in value:
                collect(child)

    collect(document)
    graph = document["Data"]["RootChunk"]["graph"]["Data"]
    scene_node: dict[str, Any] | None = None
    for wrapper in graph["nodes"]:
        data = wrapper["Data"]
        if data.get("$type") != "questSceneNodeDefinition":
            continue
        depot_path = data.get("sceneFile", {}).get("DepotPath", {}).get("$value")
        if depot_path == scene_path:
            scene_node = data
            break
    if scene_node is None:
        raise ValueError(f"Scene node not found for {scene_path}")

    removed_socket_ids: set[str] = set()
    connection_ids: set[str] = set()
    kept_sockets: list[dict[str, Any]] = []
    for socket in scene_node["sockets"]:
        resolved = socket
        if "HandleRefId" in socket:
            resolved = handles.get(socket["HandleRefId"], socket)
        socket_data = resolved.get("Data", {})
        name = socket_data.get("name", {})
        name_value = name.get("$value") if isinstance(name, dict) else name
        if name_value != exit_name or socket_data.get("type") != "Output":
            kept_sockets.append(socket)
            continue
        socket_id = resolved.get("HandleId") or socket.get("HandleRefId")
        if isinstance(socket_id, str):
            removed_socket_ids.add(socket_id)
        for connection in socket_data.get("connections", []):
            connection_id = connection.get("HandleId") or connection.get("HandleRefId")
            if isinstance(connection_id, str):
                connection_ids.add(connection_id)
        detached_socket = json.loads(json.dumps(resolved))
        detached_socket["Data"]["connections"] = []
        kept_sockets.append(detached_socket)
    if not removed_socket_ids:
        raise ValueError(f"Scene exit {exit_name!r} not found for {scene_path}")
    scene_node["sockets"] = kept_sockets

    def remove_connections(value: Any) -> None:
        if isinstance(value, dict):
            connections = value.get("connections")
            if isinstance(connections, list):
                value["connections"] = [
                    connection
                    for connection in connections
                    if (connection.get("HandleId") or connection.get("HandleRefId"))
                    not in connection_ids
                ]
            for child in value.values():
                remove_connections(child)
        elif isinstance(value, list):
            for child in value:
                remove_connections(child)

    remove_connections(document)
    quest_compiler.validate_handle_graph(
        document,
        context=f"Scene exit {exit_name}",
    )


def equip_goth_katana_node(
    builder: quest_compiler.PhaseGraphBuilder,
    quest_id: int,
    *,
    community: str,
    entry: str,
) -> quest_compiler.GraphNode:
    """Equip Goth's authored primary weapon as soon as her spawn resolves."""

    observable_ref = builder.handles.wrap(
        {
            "$type": "questObservableUniversalRef",
            "entityReference": quest_compiler.entity_reference(
                community,
                names=[entry],
            ),
            "mainPlayerObject": 0,
            "refLocalPlayer": 0,
        }
    )
    params = builder.handles.wrap(
        {
            "$type": "questEquipItemParams",
            "byItem": 1,
            "equipDurationOverride": -1,
            "equipLastWeapon": 0,
            "equipTypes": "LastWeaponEquipped",
            "failIfItemNotFound": 0,
            "forceFirstEquip": 0,
            "ignoreStateMachine": 0,
            "instant": 1,
            "isPlayer": 0,
            "itemId": quest_compiler.tweakdbid("Items.Preset_Katana_E3"),
            "slotId": quest_compiler.tweakdbid("AttachmentSlots.WeaponRight"),
            "type": "Equip",
            "unequipDurationOverride": -1,
            "unequipTypes": "AllWeapons",
        }
    )
    return builder.node(
        quest_id,
        "questEquipItemNodeDefinition",
        input_names=("In",),
        properties={
            "entityReference": observable_ref,
            "params": params,
        },
    )


def challenge_scene_node(
    builder: quest_compiler.PhaseGraphBuilder,
    quest_id: int,
    *,
    scene: str,
    origin: str,
) -> quest_compiler.GraphNode:
    """Run the challenge scene while leaving its non-combat exit unhandled."""

    return builder.node(
        quest_id,
        "questSceneNodeDefinition",
        input_names=("start",),
        output_names=("start_combat", "end"),
        properties={
            "interruptionOperations": [],
            "notAllowedToBeFrozen": 0,
            "reapplyInterruptionOperationsAfterGameLoad": 0,
            "sceneFile": quest_compiler.resource_ref(scene),
            "sceneLocation": {
                "$type": "scnWorldMarker",
                "nodeRef": quest_compiler.node_ref(origin),
                "tag": quest_compiler.cname("None"),
                "type": "NodeRef",
            },
            "syncToMusic": 0,
        },
    )


def generate_challenge_phase(archive: Path) -> dict[str, Any]:
    """Generate Goth's pre-fight approach and challenge lifecycle."""

    manifest = load(MANIFEST)
    bindings = quest_authoring.resolve_bindings(manifest)
    normalized = quest_authoring.normalize_spec(manifest)
    stage = next(
        stage
        for stage in normalized["stages"]
        if stage["id"] == "challenge_goth_baddie"
    )
    community = stage["community"]
    builder = quest_compiler.PhaseGraphBuilder()
    start = quest_compiler.input_node(builder)
    end = quest_compiler.output_node(builder)
    activate = quest_compiler.community_action_node(builder, 10, community, "Activate")
    spawned = quest_compiler.character_spawned_node(builder, 11, community)
    friendly = quest_compiler.character_attitude_group_node(
        builder,
        12,
        community,
        stage["contact"],
        group_name="friendly",
    )
    equip = equip_goth_katana_node(
        builder, 13, community=community, entry=stage["contact"]
    )
    approach = quest_compiler.trigger_condition_node(
        builder, 14, bindings["locations"]["tr_dialogue"]["ref"], "IsInside"
    )
    checkpoint = quest_compiler.checkpoint_node(
        builder, 15, f"{bindings['quest']['id']}_{stage['id']}"
    )
    scene = challenge_scene_node(
        builder,
        16,
        scene=stage["scene"],
        origin=bindings["locations"]["sm_intimacy"]["ref"],
    )
    objective = quest_compiler.objective_node(
        builder,
        17,
        stage["objective"],
    )
    mappin = quest_compiler.mappin_node(
        builder,
        18,
        stage["mappin"],
    )
    accepted = quest_compiler.fact_node(
        builder, 19, bindings["facts"]["fight_accepted"]
    )

    builder.connect(start, activate)
    builder.connect(activate, spawned)
    builder.connect(spawned, friendly)
    builder.connect(friendly, equip)
    builder.connect(equip, approach)
    builder.connect(approach, checkpoint)
    builder.connect(checkpoint, scene, destination_socket="start")
    builder.connect(
        scene,
        objective,
        source_socket="start_combat",
        destination_socket="Succeeded",
    )
    builder.connect(objective, mappin, destination_socket="Inactive")
    builder.connect(mappin, accepted)
    builder.connect_to_earlier_output(accepted, end)

    document = quest_compiler.phase_document(builder, archive)
    document["Data"]["RootChunk"]["phasePrefabs"] = [
        {
            "$type": "questQuestPrefabEntry",
            "prefabNodeRef": quest_compiler.node_ref(normalized["phase_prefabs"][0]),
        }
    ]
    return document


def generate_journal() -> dict[str, Any]:
    """Compatibility accessor for the manifest-owned composition resource."""
    return quest_authoring.compose(load(MANIFEST)).documents[
        "mod\\gqt006\\journal\\gqt006.journal"
    ]


def generate_onscreens() -> dict[str, Any]:
    """Compatibility accessor for the manifest-owned composition resource."""
    return quest_authoring.compose(load(MANIFEST)).documents[
        "mod\\gqt006\\localization\\en-us\\onscreens\\gqt006.json"
    ]


def quest_artifacts() -> list[quest_compiler.QuestArtifact]:
    return quest_compiler.compile_manifest_artifacts(
        MANIFEST,
        ROOT_PHASE_RAW,
        ROOT_PHASE_ARCHIVE,
        stage_overrides={
            "challenge_goth_baddie": lambda stage, archive: generate_challenge_phase(
                archive
            )
        },
    )


def build_artifacts(
    output_root: Path | None = None,
) -> list[quest_compiler.QuestArtifact]:
    """Build quest composition and its custom world before publishing anything."""
    world_outputs, world_documents = world_builder.build_world_documents(
        load(WORLD_SPEC),
        PROJECT / "source/raw",
        PROJECT / "source/archive",
    )
    artifacts = [
        *(
            quest_compiler.QuestArtifact(
                item.raw_path, item.archive_path, world_documents[item.raw_path]
            )
            for item in world_outputs
        ),
        *quest_artifacts(),
    ]
    return quest_build.relocate_artifacts(artifacts, output_root)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--deserialize", action="store_true")
    parser.add_argument(
        "--serializer",
        choices=("wolvenkit", "native"),
        default="wolvenkit",
    )
    parser.add_argument("--wolvenkit", type=Path)
    parser.add_argument(
        "--out-root", type=Path, help="Build all resources in an isolated output tree"
    )
    args = parser.parse_args()
    output_root = (args.out_root or PROJECT).resolve()

    artifacts = build_artifacts(args.out_root)
    outputs = quest_build.publish_build(
        artifacts,
        namespace="gqt006",
        output_root=args.out_root,
        deserialize=args.deserialize,
        serializer=args.serializer,
        wolvenkit=args.wolvenkit,
    )

    print(
        json.dumps(
            {
                "ok": True,
                "origin": load(WORLD_SPEC)["origin"],
                "registered": True,
                "quest": str(output_root / ROOT_PHASE_RAW.relative_to(PROJECT)),
                "children": [
                    str(
                        output_root
                        / quest_compiler.resource_paths(stage.phase_resource)[
                            0
                        ].relative_to(PROJECT)
                    )
                    for stage in quest_compiler.load_spec(MANIFEST)[0].stages
                ],
                "journal": str(output_root / JOURNAL_RAW.relative_to(PROJECT)),
                "world": [
                    str(raw)
                    for raw, _ in outputs
                    if raw.name.endswith(
                        (
                            ".streamingblock.json",
                            ".streamingsector.json",
                            ".community.json",
                        )
                    )
                ],
                "packed": bool(args.deserialize),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
