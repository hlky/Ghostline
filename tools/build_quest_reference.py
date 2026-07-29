#!/usr/bin/env python3
"""Build an IGN-linked vanilla quest reference from the local journal export.

IGN pages provide the curated walkthrough group and source URL. The checked
local quest JSON provides titles, descriptions, phase/objective paths, hashes,
and map-pin data. Generated Markdown deliberately summarizes structure instead
of copying walkthrough prose.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path
from urllib.parse import urljoin, urlsplit, urlunsplit

import requests
from bs4 import BeautifulSoup


BASE_URL = "https://www.ign.com"
INDEXES = {
    "main-jobs": (
        "Main Jobs",
        "https://www.ign.com/wikis/cyberpunk-2077/Walkthrough_-_Main_Jobs",
        {"MainQuest"},
    ),
    "side-jobs": (
        "Side Jobs",
        "https://www.ign.com/wikis/cyberpunk-2077/Side_Jobs",
        {"SideQuest", "MinorQuest", "CourierSideQuest", "CourierQuest"},
    ),
    "gigs": (
        "Gigs",
        "https://www.ign.com/wikis/cyberpunk-2077/Gigs",
        {"StreetStory", "Contract", "CyberPsycho"},
    ),
}
HEADERS = {"User-Agent": "Mozilla/5.0 (Ghostline quest-reference builder)"}
TITLE_ALIASES = {
    "the street kid": "the streetkid",
    "the corpo": "the corpo rat",
    "m ap tann pelen": "m ap tann pèlen",
    "killing moon": "the killing moon",
    "i m in love with my car ken block car location": "i m in love with my car",
    "talking bout a revolution": "talkin bout a revolution",
    "going up or going down": "going up or down",
    "dancing on a mine field": "dancing on a minefield",
}


def normalize_title(value: str) -> str:
    value = html.unescape(value)
    value = unicodedata.normalize("NFKD", value)
    value = "".join(char for char in value if unicodedata.category(char) != "Mn")
    value = value.replace("’", "'").replace("‘", "'").replace("–", "-")
    value = re.sub(r"^(gig|side job):\s*", "", value, flags=re.I)
    value = re.sub(r"\s*\((side gig|side job|walkthrough)\)\s*$", "", value, flags=re.I)
    value = re.sub(r"\s+-\s+.*walkthrough.*$", "", value, flags=re.I)
    value = re.sub(r"[^a-z0-9]+", " ", value.lower())
    return " ".join(value.split())


def clean_url(href: str) -> str:
    url = urljoin(BASE_URL, href)
    parts = urlsplit(url)
    return urlunsplit((parts.scheme, parts.netloc, parts.path, "", ""))


def get_index_links(session: requests.Session, url: str) -> list[dict[str, str]]:
    response = session.get(url, headers=HEADERS, timeout=30)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    root = soup.select_one(".wiki-html")
    if root is None:
        raise RuntimeError(f"IGN article body not found: {url}")

    links: list[dict[str, str]] = []
    seen: set[str] = set()
    for anchor in root.select('a[href*="/wikis/cyberpunk-2077/"]'):
        title = " ".join(anchor.get_text(" ", strip=True).split())
        href = clean_url(anchor.get("href", ""))
        if not title or href in seen or href == clean_url(url):
            continue
        seen.add(href)
        links.append({"title": title, "url": href})
    return links


def quest_index(quests: list[dict]) -> dict[str, list[dict]]:
    result: dict[str, list[dict]] = defaultdict(list)
    for quest in quests:
        title = quest.get("title")
        if isinstance(title, str) and title.strip():
            result[normalize_title(title)].append(quest)
    return result


def choose_match(
    link: dict[str, str],
    candidates: dict[str, list[dict]],
    allowed_types: set[str],
) -> dict | None:
    normalized = normalize_title(link["title"])
    normalized = normalize_title(TITLE_ALIASES.get(normalized, normalized))
    matches = [row for row in candidates.get(normalized, []) if row.get("type") in allowed_types]
    if not matches:
        return None
    # Prefer base-game records when IGN's base-game lists collide with EP1.
    matches.sort(
        key=lambda row: (
            str(row.get("path", "")).startswith("ep1/"),
            str(row.get("path", "")).count("/"),
            str(row.get("path", "")),
        )
    )
    return matches[0]


def flatten_objectives(quest: dict) -> list[dict]:
    rows: list[dict] = []
    seen: set[tuple] = set()
    for phase in quest.get("phases", []):
        phase_path = phase.get("path", "")
        for objective in phase.get("objectives", []):
            key = (
                objective.get("path"),
                objective.get("description"),
                objective.get("type"),
            )
            if key in seen:
                continue
            seen.add(key)
            rows.append(
                {
                    "phase": phase_path,
                    "path": objective.get("path", ""),
                    "hash": objective.get("hash"),
                    "type": objective.get("type", ""),
                    "description": objective.get("description", ""),
                    "entries": objective.get("entries", []),
                }
            )
    return rows


def building_blocks(objectives: list[dict]) -> list[str]:
    text = " ".join(str(row.get("description", "")).lower() for row in objectives)
    rules = [
        ("phone/message contact", ("call ", "message ", "read the message", "text ")),
        ("meet/contact conversation", ("meet ", "talk to ", "speak with ", "ask ")),
        ("travel/reach location", ("go to ", "reach ", "get to ", "head to ", "enter ")),
        ("follow/escort", ("follow ", "escort ", "lead ")),
        ("wait/time gate", ("wait ", "sit ", "lean ")),
        ("search/investigate", ("search ", "look for ", "investigate", "scan ", "find ")),
        ("interact/use device", ("use ", "connect ", "interact", "activate ", "open ")),
        ("hack/breach/download", ("hack ", "breach", "download", "upload", "datamine")),
        ("retrieve/collect item", ("take ", "retrieve", "collect", "pick up", "grab ")),
        ("deliver/deposit item", ("deliver", "deposit", "leave the ", "place ")),
        ("combat/neutralize", ("defeat", "kill ", "neutralize", "eliminate", "fight ")),
        ("stealth/avoid detection", ("sneak", "remain undetected", "avoid ", "don't raise")),
        ("vehicle sequence", ("drive ", "get in", "ride ", "vehicle", "car ")),
        ("choice/decision", ("choose", "decide", "optional", "accept ", "refuse ")),
        ("leave/escape area", ("leave ", "escape", "get out")),
    ]
    return [label for label, needles in rules if any(needle in text for needle in needles)]


def markdown_escape(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def render_category(
    label: str,
    index_url: str,
    records: list[dict],
    quest_json_source: str,
) -> str:
    lines = [
        f"# Cyberpunk 2077 {label} Reference",
        "",
        f"Source index: [IGN — {label}]({index_url})",
        "",
        "This is a structural reference derived from IGN's walkthrough index and",
        f"the local `{quest_json_source}` journal export. It summarizes",
        "vanilla quest objectives and links to IGN; it does not reproduce IGN's",
        "walkthrough prose.",
        "",
        f"Matched quests: **{len(records)}**",
        "",
        "## Quick index",
        "",
        "| Quest | Vanilla type | Quest path | Building blocks |",
        "|---|---|---|---|",
    ]
    for record in records:
        quest = record["quest"]
        anchor = re.sub(r"[^a-z0-9 -]", "", quest["title"].lower()).replace(" ", "-")
        blocks = ", ".join(record["building_blocks"]) or "objective sequence"
        lines.append(
            f"| [{markdown_escape(quest['title'])}](#{anchor}) "
            f"([IGN]({record['ign_url']})) | {quest.get('type', '')} | "
            f"`{quest.get('path', '')}` | {markdown_escape(blocks)} |"
        )

    for record in records:
        quest = record["quest"]
        objectives = record["objectives"]
        lines.extend(
            [
                "",
                f"## {quest['title']}",
                "",
                f"- IGN walkthrough: [{record['ign_title']}]({record['ign_url']})",
                f"- Vanilla type: `{quest.get('type', '')}`",
                f"- Quest hash: `{quest.get('hash', '')}`",
                f"- Quest path: `{quest.get('path', '')}`",
            ]
        )
        if quest.get("district"):
            lines.append(f"- District: {quest['district']}")
        if quest.get("level") is not None:
            lines.append(f"- Level: {quest['level']}")
        lines.append(
            "- Candidate building blocks: "
            + (", ".join(f"`{x}`" for x in record["building_blocks"]) or "`objective sequence`")
        )
        if quest.get("description"):
            lines.extend(["", "### Journal premise", "", markdown_escape(quest["description"])])
        lines.extend(["", "### Objective sequence", ""])
        if not objectives:
            lines.append("_No objectives were present in the exported journal record._")
        for index, objective in enumerate(objectives, 1):
            description = markdown_escape(objective.get("description") or "(unnamed objective)")
            lines.append(
                f"{index}. **{description}**  \n"
                f"   `{objective.get('type', '')}` · `{objective.get('path', '')}`"
            )
            entries = objective.get("entries", [])
            map_pins = [entry for entry in entries if entry.get("type") == "MapPin"]
            for pin in map_pins:
                details = []
                if pin.get("ref"):
                    details.append(f"ref `{pin['ref']}`")
                if pin.get("pos"):
                    details.append("position `" + ", ".join(str(x) for x in pin["pos"]) + "`")
                if details:
                    lines.append("   - Map pin: " + "; ".join(details))
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--quest-json", type=Path, default=Path(r"H:\projects\quest.json"))
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("docs/reference/vanilla-quests"),
    )
    parser.add_argument(
        "--link-map",
        type=Path,
        default=Path("reference/quests/ign-link-map.json"),
    )
    args = parser.parse_args()

    quests = json.loads(args.quest_json.read_text(encoding="utf-8"))
    candidates = quest_index(quests)
    session = requests.Session()
    all_records: dict[str, list[dict]] = {}
    unmatched: dict[str, list[dict[str, str]]] = {}

    for slug, (label, index_url, allowed_types) in INDEXES.items():
        records: list[dict] = []
        misses: list[dict[str, str]] = []
        for link in get_index_links(session, index_url):
            quest = choose_match(link, candidates, allowed_types)
            if quest is None:
                misses.append(link)
                continue
            if any(row["quest"]["path"] == quest["path"] for row in records):
                continue
            objectives = flatten_objectives(quest)
            records.append(
                {
                    "ign_title": link["title"],
                    "ign_url": link["url"],
                    "quest": quest,
                    "objectives": objectives,
                    "building_blocks": building_blocks(objectives),
                }
            )
        records.sort(key=lambda row: row["quest"]["title"].casefold())
        all_records[slug] = records
        unmatched[slug] = misses

    args.output.mkdir(parents=True, exist_ok=True)
    quest_json_source = str(args.quest_json)
    for slug, (label, index_url, _) in INDEXES.items():
        (args.output / f"{slug}.md").write_text(
            render_category(label, index_url, all_records[slug], quest_json_source),
            encoding="utf-8",
            newline="\n",
        )

    mapping = {
        "source_quest_json": str(args.quest_json),
        "indexes": {
            slug: {
                "title": INDEXES[slug][0],
                "url": INDEXES[slug][1],
                "matches": [
                    {
                        "quest_hash": row["quest"].get("hash"),
                        "quest_path": row["quest"].get("path"),
                        "quest_title": row["quest"].get("title"),
                        "quest_type": row["quest"].get("type"),
                        "ign_title": row["ign_title"],
                        "ign_url": row["ign_url"],
                        "building_blocks": row["building_blocks"],
                    }
                    for row in records
                ],
                "unmatched_index_links": unmatched[slug],
            }
            for slug, records in all_records.items()
        },
    }
    args.link_map.parent.mkdir(parents=True, exist_ok=True)
    args.link_map.write_text(
        json.dumps(mapping, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )

    readme = [
        "# Vanilla Quest Reference",
        "",
        "These files are generated research material. Regenerate them from their",
        "source indexes; do not maintain individual quest entries by hand.",
        "",
        "IGN's walkthrough indexes provide the curated quest lists and source URLs.",
        "The local `H:\\projects\\quest.json` export provides the exact vanilla",
        "journal paths, hashes, descriptions, objectives, and map-pin references.",
        "",
        "Generated files:",
        "",
    ]
    for slug, (label, _, _) in INDEXES.items():
        readme.append(f"- [{label}]({slug}.md): {len(all_records[slug])} matched quests")
    readme.extend(
        [
            "",
            "Machine-readable linkage:",
            "[`reference/quests/ign-link-map.json`](../../../reference/quests/ign-link-map.json).",
            "",
            "Regenerate:",
            "",
            "```powershell",
            "py -B .\\tools\\build_quest_reference.py",
            "```",
            "",
            "The generated pages summarize local journal data and link to IGN. They",
            "do not mirror or reproduce IGN walkthrough articles.",
            "",
        ]
    )
    (args.output / "README.md").write_text(
        "\n".join(readme),
        encoding="utf-8",
        newline="\n",
    )

    for slug, records in all_records.items():
        print(f"{slug}: {len(records)} matched")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
