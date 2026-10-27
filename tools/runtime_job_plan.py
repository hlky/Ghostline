"""Validate a narrow live-execution adapter against existing Ghostline quest blocks."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from pathlib import Path

from quest_compiler import load_spec
from quest_types import QuestSpecError

ROOT = Path(__file__).resolve().parents[1]


def build_runtime_plan(manifest: Path, runtime: Path, *, root: Path = ROOT) -> dict:
    spec, diagnostics = load_spec(manifest)
    if spec is None:
        raise QuestSpecError("; ".join(d.message for d in diagnostics if d.level == "error"))
    metadata = json.loads(runtime.read_text(encoding="utf-8"))
    if not isinstance(metadata, dict) or set(metadata) != {"schema_version", "binding", "reach_radius", "transfer_duration", "reward_amount", "offer", "choice_labels"} or metadata["schema_version"] != 1:
        raise QuestSpecError("Unsupported runtime adapter metadata")
    if spec.id != "gq_runtime_theft" or spec.parallel_groups or spec.entry_stage or spec.completion or spec.external_events or spec.external_facts:
        raise QuestSpecError("The first runtime adapter supports only the fixed data-theft contract")
    if [s.type for s in spec.stages] != ["reach_area", "interact_device", "choice_gate"] or any(s.status != "ready" for s in spec.stages):
        raise QuestSpecError("Runtime job must be ready reach_area -> interact_device -> choice_gate")
    reach, hack, decision = spec.stages
    supported = {
        "reach_area": {"id", "type", "status", "phase_resource", "trigger", "objective", "description_entry", "mappin"},
        "interact_device": {"id", "type", "status", "phase_resource", "device", "success_fact", "controller_class", "action", "completion_function", "send_action"},
        "choice_gate": {"id", "type", "status", "phase_resource", "gate_kind", "join", "branches"},
    }
    for stage in spec.stages:
        if set(stage.data) - supported[stage.type]:
            raise QuestSpecError(f"Unsupported live block fields in {stage.id}: {sorted(set(stage.data) - supported[stage.type])}")
    binding = metadata["binding"]
    if not isinstance(binding, dict) or set(binding) != {"mode", "device", "trigger", "catalog", "debug_name"} or binding["mode"] != "catalog_access_point" or binding["device"] != hack.data["device"] or binding["trigger"] != reach.data["trigger"]:
        raise QuestSpecError("Runtime bindings do not match the quest block identifiers")
    catalog_path = (root / binding["catalog"]).resolve()
    if not catalog_path.is_relative_to(root.resolve() / "reference/world"):
        raise QuestSpecError("Runtime targets must come from the extracted world catalogue")
    catalogue = json.loads(catalog_path.read_text(encoding="utf-8"))
    matches = [x for x in catalogue["instances"] if x["debug_name"] == binding["debug_name"]]
    if len(matches) != 1:
        raise QuestSpecError("Catalogue selector must identify exactly one access point")
    target = matches[0]
    if not target.get("node_ref", "").startswith("$/") or not target["resource"].endswith("antenna_access_point_small.ent"):
        raise QuestSpecError("Catalogue entry must have an absolute access-point NodeRef")
    if set(target["position"]) != {"x", "y", "z"} or any(not isinstance(v, (float, int)) or not math.isfinite(v) for v in target["position"].values()):
        raise QuestSpecError("Catalogue entry has no finite world position")
    if hack.data.get("controller_class") != "ScriptableDeviceComponentPS" or hack.data.get("completion_function") != "GhostlineDataTheftTransferred" or hack.data.get("send_action") is not False:
        raise QuestSpecError("Runtime interaction must observe the scoped transfer completion")
    if hack.data.get("action") != "TogglePersonalLink":
        raise QuestSpecError("Unsupported personal-link interaction contract")
    branches = decision.data["branches"]
    if decision.data.get("gate_kind") != "fact" or decision.data.get("join") is not True or [b["id"] for b in branches] != ["deliver", "keep_copy"]:
        raise QuestSpecError("Runtime delivery requires the two fixed fact-backed outcomes")
    if any(set(b) != {"id", "condition", "set_fact"} for b in branches):
        raise QuestSpecError("Runtime delivery branches cannot perform additional operations")
    facts = [hack.data["success_fact"], *[b[k] for b in branches for k in ["condition", "set_fact"]]]
    if len(set(facts)) != len(facts):
        raise QuestSpecError("Runtime completion and outcome facts must be distinct")
    for fact in facts:
        if not isinstance(fact, str) or not re.fullmatch(spec.id + r"_[a-z0-9_]+", fact):
            raise QuestSpecError("Runtime job facts must stay inside their job namespace")
    radius = metadata["reach_radius"]
    duration = metadata["transfer_duration"]
    if isinstance(duration, bool) or not isinstance(duration, (float, int)) or not math.isfinite(duration) or not 1 <= duration <= 30:
        raise QuestSpecError("Transfer duration must be finite and between 1 and 30 seconds")
    reward = metadata["reward_amount"]
    if isinstance(radius, bool) or not isinstance(radius, (float, int)) or not math.isfinite(radius) or not 1 <= radius <= 30:
        raise QuestSpecError("Reach radius must be finite and between 1 and 30 metres")
    if isinstance(reward, bool) or not isinstance(reward, int) or not 0 <= reward <= 10000:
        raise QuestSpecError("Reward must be an integer between 0 and 10000")
    if not isinstance(metadata["offer"], str) or not 1 <= len(metadata["offer"]) <= 500:
        raise QuestSpecError("A short job offer is required")
    if not isinstance(metadata["choice_labels"], dict) or set(metadata["choice_labels"]) != {"deliver", "keep_copy"} or any(not isinstance(v, str) or not 1 <= len(v) <= 100 for v in metadata["choice_labels"].values()):
        raise QuestSpecError("Both delivery outcomes need short labels")
    contract = {"schema_version": 1, "job_id": spec.id, "title": spec.title,
                "stages": [{"id": s.id, "type": s.type, "contract": s.data} for s in spec.stages], **metadata,
                "target": {"node_ref": target["node_ref"], "position": target["position"],
                           "debug_name": target["debug_name"], "resource": target["resource"],
                           "sector": target["sector"], "catalog_sha256": hashlib.sha256(catalog_path.read_bytes()).hexdigest()}}
    digest = hashlib.sha256(json.dumps(contract, sort_keys=True).encode("utf-8")).hexdigest()
    return {**contract, "sha256": digest, "revision": int(digest[:8], 16) & 0x7FFFFFFF,
            "runtime_tested": False, "presentation": "native temporary mappin, notifications and choices; no journal resource"}


def config_source(plan: dict) -> str:
    quote = lambda value: json.dumps(value, ensure_ascii=False)
    hack = plan["stages"][1]["contract"]
    branches = plan["stages"][2]["contract"]["branches"]
    functions = {"Revision": ("Int32", str(plan["revision"])),
                 "Radius": ("Float", str(float(plan["reach_radius"]))),
                 "Reward": ("Int32", str(plan["reward_amount"])),
                 "TargetRef": ("NodeRef", "CreateNodeRef(" + quote(plan["target"]["node_ref"]) + ")"),
                 "Duration": ("Float", str(float(plan["transfer_duration"]))),
                 "TransferFact": ("String", quote(hack["success_fact"])),
                 "DeliveredFact": ("String", quote(branches[0]["set_fact"])),
                 "KeptCopyFact": ("String", quote(branches[1]["set_fact"])),
                 "DeliverCondition": ("String", quote(branches[0]["condition"])),
                 "KeepCondition": ("String", quote(branches[1]["condition"]))}
    lines = ["// Generated by tools/runtime_job_plan.py; edit the job contracts instead.",
             "public class GhostlineDataTheftConfig extends IScriptable {"]
    lines.extend(f"  public static func {name}() -> {kind} = {value};" for name, (kind, value) in functions.items())
    p = plan["target"]["position"]
    lines.append(f"  public static func Position() -> Vector4 = new Vector4({float(p['x'])}, {float(p['y'])}, {float(p['z'])}, 1.0);")
    return "\n".join([*lines, "}", ""])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("runtime", type=Path)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--config", type=Path, required=True)
    args = parser.parse_args()
    plan = build_runtime_plan(args.manifest, args.runtime)
    args.plan.parent.mkdir(parents=True, exist_ok=True)
    args.config.parent.mkdir(parents=True, exist_ok=True)
    args.plan.write_text(json.dumps(plan, indent=2) + "\n", encoding="utf-8")
    args.config.write_text(config_source(plan), encoding="utf-8")
    print(json.dumps({"job": plan["job_id"], "revision": plan["revision"], "blocks": [s["type"] for s in plan["stages"]]}))


if __name__ == "__main__":
    main()
