#!/usr/bin/env python3
"""Refresh editor-only schema definitions from the canonical quest contracts.

The checked-in schema works in ordinary JSON editors without Python. Canonical
stage branches remain the single hand-maintained registry; generated definitions
reference their literal constraints and add whole-value aliases at value sites.
"""

from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path

from artifact_io import atomic_write_json
from quest_authoring import RECIPES

SCHEMA_PATH = Path(__file__).with_name("quest-schema-v1.json")
AUTHORING = "#/$defs/authoring/$defs/"
IDENTITY_FIELDS = {"schema_version", "id", "title", "description", "composition"}
ALIAS = {
    "type": "string",
    "pattern": r"^@(quest|resources|objectives|contacts|locations|clues|facts|points_of_interest|readables)(\.[a-z][a-z0-9_]*)*$",
    "description": "Whole-value composition alias; resolved values must satisfy the canonical field contract.",
}


def _pointer(value: str) -> str:
    return value.replace("~", "~0").replace("/", "~1")


def generated_definitions(schema: dict) -> dict:
    """Build alias-aware forms without maintaining a second stage registry."""
    canonical = {
        name: value for name, value in schema["$defs"].items() if name != "authoring"
    }

    def value_schema(
        value: dict | bool, path: str, *, literal: bool = False
    ) -> dict | bool:
        if isinstance(value, bool):
            return value
        if literal:
            return {"$ref": path}
        return {"anyOf": [{"$ref": AUTHORING + "alias"}, body(value, path)]}

    def body(value: dict | bool, path: str) -> dict | bool:
        if isinstance(value, bool):
            return value
        structural = {
            "$ref",
            "properties",
            "items",
            "allOf",
            "anyOf",
            "oneOf",
            "then",
            "else",
        }
        if not structural.intersection(value) and not isinstance(
            value.get("additionalProperties"), dict
        ):
            return {"$ref": path}
        result = copy.deepcopy(value)
        if "$ref" in result:
            ref = result["$ref"]
            if not ref.startswith("#/$defs/"):
                raise ValueError(f"Unsupported canonical schema reference: {ref}")
            result["$ref"] = AUTHORING + ref[len("#/$defs/") :]
        for key in ("properties", "patternProperties"):
            if key in value:
                result[key] = {
                    name: value_schema(
                        child,
                        f"{path}/{key}/{_pointer(name)}",
                        literal=name == "type"
                        or (name == "id" and path == "#/$defs/baseStage"),
                    )
                    for name, child in value[key].items()
                }
        for key in ("items", "additionalProperties"):
            if isinstance(value.get(key), dict):
                result[key] = value_schema(value[key], f"{path}/{key}")
        for key in ("allOf", "anyOf", "oneOf"):
            if key in value:
                result[key] = [
                    body(child, f"{path}/{key}/{index}")
                    for index, child in enumerate(value[key])
                ]
        for key in ("then", "else"):
            if key in value:
                result[key] = body(value[key], f"{path}/{key}")
        # Conditions and negation test literal values/presence; alias resolution
        # is followed by canonical validation, which checks the resolved branch.
        for key in ("if", "not", "propertyNames"):
            if key in value:
                result[key] = {"$ref": f"{path}/{key}"}
        return result

    definitions = {
        name: body(value, f"#/$defs/{name}") for name, value in canonical.items()
    }
    definitions["alias"] = copy.deepcopy(ALIAS)
    definitions["baseStage"]["required"] = ["id", "type"]
    definitions["manifestFields"]["required"] = []
    definitions["manifestFields"]["properties"]["stages"] = {
        "type": "array",
        "items": {"$ref": AUTHORING + "stage"},
    }
    definitions["recipeBaseStage"] = {
        "type": "object",
        "properties": definitions["baseStage"]["properties"],
    }
    stage_indices = {
        branch["allOf"][1]["properties"]["type"]["const"]: index
        for index, branch in enumerate(canonical["stage"]["oneOf"])
    }
    recipe_stages = []
    for stage_type, index in stage_indices.items():
        definition = {
            "allOf": [
                {"$ref": AUTHORING + "recipeBaseStage"},
                {"$ref": f"{AUTHORING}stage/oneOf/{index}/allOf/1"},
            ],
            "unevaluatedProperties": False,
        }
        definitions[f"recipe_{stage_type}"] = definition
        recipe_stages.append(
            {
                "allOf": [
                    {"$ref": AUTHORING + f"recipe_{stage_type}"},
                    {"required": ["type"]},
                ]
            }
        )
    definitions["recipeStage"] = {"oneOf": recipe_stages}
    recipes = []
    for recipe_name, steps in RECIPES.items():
        properties = {
            "name": {"const": recipe_name},
            "prefix": {"type": "string", "pattern": "^([a-z][a-z0-9_]*)?$"},
            "steps": {
                "type": "object",
                "additionalProperties": False,
                "required": [name for name, _ in steps],
                "properties": {
                    name: {
                        "if": {"required": ["type"]},
                        "then": {"$ref": AUTHORING + "recipeStage"},
                        "else": {"$ref": AUTHORING + f"recipe_{stage_type}"},
                    }
                    for name, stage_type in steps
                },
            },
        }
        required = ["name", "steps"]
        if recipe_name == "encounter_evidence_report_reward":
            properties["reward"] = value_schema(
                canonical["tweakDbId"], "#/$defs/tweakDbId"
            )
            required.append("reward")
        recipes.append(
            {
                "type": "object",
                "additionalProperties": False,
                "required": required,
                "properties": properties,
            }
        )
    definitions["recipe"] = {"oneOf": recipes}
    return {
        "$comment": "Generated by tools/quest_authoring_schema.py; edit canonical definitions and refresh, never edit this block directly.",
        "$defs": definitions,
    }


def refresh_schema(schema: dict) -> dict:
    """Install unified editor selection while retaining canonical source schemas."""
    result = copy.deepcopy(schema)
    definitions = result["$defs"]
    if "manifestFields" not in definitions:
        definitions["manifestFields"] = {
            "type": "object",
            "required": ["stages"],
            "properties": {
                name: value
                for name, value in result["properties"].items()
                if name not in IDENTITY_FIELDS
            },
        }
    for name, value in result["properties"].items():
        if name not in IDENTITY_FIELDS and (
            value or name not in definitions["manifestFields"]["properties"]
        ):
            definitions["manifestFields"]["properties"][name] = value
    for name in definitions["manifestFields"]["properties"]:
        result["properties"][name] = {}
    result["required"] = ["schema_version", "id", "title"]
    result["allOf"] = [
        {
            "if": {"required": ["composition"]},
            "then": {
                "allOf": [
                    {"$ref": AUTHORING + "manifestFields"},
                    {
                        "anyOf": [
                            {
                                "required": ["stages"],
                                "properties": {"stages": {"minItems": 1}},
                            },
                            {
                                "properties": {
                                    "composition": {
                                        "required": ["recipes"],
                                        "properties": {"recipes": {"minItems": 1}},
                                    }
                                }
                            },
                        ]
                    },
                ],
            },
            "else": {"$ref": "#/$defs/manifestFields"},
        }
    ]
    result["properties"]["composition"]["properties"]["recipes"]["items"] = {
        "$ref": AUTHORING + "recipe"
    }
    definitions["authoring"] = generated_definitions(result)
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail when the checked-in editor definitions need refresh",
    )
    args = parser.parse_args(argv)
    original = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    refreshed = refresh_schema(original)
    if args.check:
        if refreshed != original:
            print(
                "Quest editor schema is stale; run python tools/quest_authoring_schema.py"
            )
            return 1
    else:
        atomic_write_json(SCHEMA_PATH, refreshed)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
