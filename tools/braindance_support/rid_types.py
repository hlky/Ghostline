"""RID metadata wrappers and validation result types."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any


RID_KIND = "ghostline_braindance_animation_handoff"


RID_REPORT_KIND = "ghostline_braindance_rid_report"


CR2W_MAGIC = b"CR2W"


ANIMATION_SAMPLE_SPACE = "blender_local_z_up_right_handed"


CONST_TRANSLATION_AUX = 0x9C3F


CONST_TRACK_AUX = 0x3454


class RidCompileError(RuntimeError):
    """Raised for an invalid handoff, template, or compiler result."""


@dataclass(frozen=True)
class RidValidationReport:
    errors: tuple[str, ...]
    warnings: tuple[str, ...]
    details: dict[str, Any]

    @property
    def ok(self) -> bool:
        return not self.errors


def _root(document: dict[str, Any]) -> dict[str, Any]:
    try:
        root = document["Data"]["RootChunk"]
    except (KeyError, TypeError) as exc:
        raise RidCompileError("Template is missing Data.RootChunk") from exc
    if not isinstance(root, dict) or root.get("$type") != "scnRidResource":
        raise RidCompileError("Template RootChunk must be a scnRidResource")
    return root


def _cname(value: Any) -> str | None:
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        inner = value.get("$value")
        return inner if isinstance(inner, str) else None
    return None


def _serial(value: Any) -> int | None:
    if isinstance(value, int) and not isinstance(value, bool):
        return value
    if isinstance(value, dict):
        inner = value.get("serialNumber")
        return inner if isinstance(inner, int) and not isinstance(inner, bool) else None
    return None


def _set_cname(container: dict[str, Any], key: str, text: str) -> None:
    current = container.get(key)
    if isinstance(current, dict):
        current["$value"] = text
        current.setdefault("$type", "CName")
        current.setdefault("$storage", "string")
    else:
        container[key] = {
            "$type": "CName",
            "$storage": "string",
            "$value": text,
        }


def _set_serial(tag: dict[str, Any], value: int) -> None:
    current = tag.get("serialNumber")
    if isinstance(current, dict):
        current["serialNumber"] = value
        current.setdefault("$type", "scnRidSerialNumber")
    else:
        tag["serialNumber"] = {
            "$type": "scnRidSerialNumber",
            "serialNumber": value,
        }


def _tag_signature(record: dict[str, Any]) -> str | None:
    tag = record.get("tag")
    return _cname(tag.get("signature")) if isinstance(tag, dict) else None


def _set_tag(record: dict[str, Any], signature: str, serial: int) -> None:
    tag = record.get("tag")
    if not isinstance(tag, dict):
        tag = {"$type": "scnRidTag"}
        record["tag"] = tag
    _set_cname(tag, "signature", signature)
    _set_serial(tag, serial)


def _set_next_serial(root: dict[str, Any], value: int) -> None:
    current = root.get("nextSerialNumber")
    if isinstance(current, dict):
        current["serialNumber"] = value
        current.setdefault("$type", "scnRidSerialNumber")
    else:
        root["nextSerialNumber"] = {
            "$type": "scnRidSerialNumber",
            "serialNumber": value,
        }


def _set_animation_name(animation_rid: dict[str, Any], value: str) -> None:
    animation = animation_rid.get("animation")
    if not isinstance(animation, dict):
        raise RidCompileError("Actor animation template has no animation handle")
    data = animation.get("Data")
    if not isinstance(data, dict) or data.get("$type") != "animAnimation":
        raise RidCompileError("Actor animation handle must contain animAnimation")
    _set_cname(data, "name", value)


def _patch_durations(value: Any, duration: float) -> None:
    """Retimes duration-bearing template objects without touching key bytes."""
    if isinstance(value, dict):
        for key, child in value.items():
            if key == "duration" and isinstance(child, (int, float)) and not isinstance(child, bool):
                value[key] = duration
            else:
                _patch_durations(child, duration)
    elif isinstance(value, list):
        for child in value:
            _patch_durations(child, duration)


def _actor_sample(
    samples: dict[str, Any],
    actor_id: str,
) -> dict[str, Any]:
    actors = samples.get("actors")
    if not isinstance(actors, list):
        raise RidCompileError("animation_samples.actors must be an array")
    matches = [
        actor for actor in actors
        if isinstance(actor, dict) and actor.get("id") == actor_id
    ]
    if len(matches) != 1:
        raise RidCompileError(
            f"animation_samples must contain exactly one actor {actor_id!r}"
        )
    return matches[0]

