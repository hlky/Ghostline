"""Shared helpers for read-only CR2W-JSON explorer scripts."""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from typing import Any, Iterable


def load_json(path: Path) -> dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8-sig") as file:
            data = json.load(file)
    except FileNotFoundError:
        raise SystemExit(f"JSON file not found: {path}") from None
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Failed to parse JSON in {path}: {exc}") from None
    if not isinstance(data, dict):
        raise SystemExit(f"Expected a JSON object at the root of {path}")
    return data


def walk(value: Any, path: tuple[Any, ...] = ("$",)) -> Iterable[tuple[tuple[Any, ...], Any]]:
    yield path, value
    if isinstance(value, dict):
        for key, child in value.items():
            yield from walk(child, path + (key,))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk(child, path + (index,))


def path_to_string(path: tuple[Any, ...]) -> str:
    result = ""
    for part in path:
        if part == "$":
            result = "$"
        elif isinstance(part, int):
            result += f"[{part}]"
        else:
            text = str(part)
            if re.match(r"^[A-Za-z_][A-Za-z0-9_]*$", text):
                result += f".{text}"
            else:
                result += f"[{json.dumps(text)}]"
    return result


def typed_value(value: Any, default: Any = None) -> Any:
    if isinstance(value, dict) and "$value" in value:
        return value["$value"]
    return default


def typed_id(value: Any, default: Any = None) -> Any:
    if isinstance(value, dict) and "id" in value:
        return value["id"]
    return default


def object_handle(value: Any) -> str | None:
    if not isinstance(value, dict):
        return None
    if "HandleId" in value:
        return str(value["HandleId"])
    if "HandleRefId" in value:
        return str(value["HandleRefId"])
    return None


def depot_path_value(value: Any) -> str:
    if not isinstance(value, dict):
        return ""
    depot = value.get("DepotPath")
    if isinstance(depot, dict):
        return str(depot.get("$value", ""))
    return ""


def nested_get(value: Any, keys: tuple[str, ...], default: Any = None) -> Any:
    current = value
    for key in keys:
        if not isinstance(current, dict):
            return default
        current = current.get(key)
    return default if current is None else current


def short_type(type_name: str) -> str:
    if not type_name:
        return ""
    result = type_name
    for prefix in ("localizationPersistence", "quest", "scn", "loc"):
        if result.startswith(prefix):
            result = result[len(prefix) :]
            break
    for suffix in ("NodeDefinition", "Definition", "Resource", "Entry", "Entries"):
        if result.endswith(suffix):
            result = result[: -len(suffix)]
    return result or type_name


def first_scalar_label(value: dict[str, Any]) -> str:
    for key in ("debugString", "actorName", "playerName", "caption", "name", "type"):
        raw = value.get(key)
        if isinstance(raw, str) and raw:
            return raw
        if isinstance(raw, dict):
            unwrapped = typed_value(raw, "")
            if unwrapped:
                return str(unwrapped)
    return ""


def collect_type_counts(data: Any) -> Counter[str]:
    counts: Counter[str] = Counter()
    for _, value in walk(data):
        if isinstance(value, dict) and isinstance(value.get("$type"), str):
            counts[value["$type"]] += 1
    return counts


def print_json(value: Any) -> None:
    print(json.dumps(value, indent=2, ensure_ascii=False))


def print_table(rows: list[dict[str, Any]], columns: list[tuple[str, str]]) -> None:
    if not rows:
        print("(no rows)")
        return
    widths: dict[str, int] = {}
    for key, heading in columns:
        widths[key] = max(len(heading), *(len(str(row.get(key, ""))) for row in rows))
    print("  ".join(heading.ljust(widths[key]) for key, heading in columns))
    print("  ".join("-" * widths[key] for key, _ in columns))
    for row in rows:
        print("  ".join(str(row.get(key, "")).ljust(widths[key]) for key, _ in columns))


def bounded(items: list[Any], limit: int, offset: int = 0) -> tuple[list[Any], str]:
    total = len(items)
    start = max(offset, 0)
    if limit <= 0:
        selected = items[start:]
    else:
        selected = items[start : start + limit]
    suffix = ""
    if len(selected) + start < total:
        suffix = f"Showing {len(selected)} of {total}. Use --offset {start + len(selected)} or --limit 0 for more."
    elif start:
        suffix = f"Showing {len(selected)} of {total} from offset {start}."
    return selected, suffix


def int_or_text(value: str) -> tuple[int, int | str]:
    try:
        return (0, int(value))
    except ValueError:
        return (1, value)
