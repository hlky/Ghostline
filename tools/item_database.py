"""Equipment authoring CLI; public helpers are re-exported for existing callers."""

from __future__ import annotations
import argparse
import json
import os
import sys
from pathlib import Path

from item_common import (
    ATTRIBUTE_BLOCK as ATTRIBUTE_BLOCK,
    BLENDER_SCRIPT as BLENDER_SCRIPT,
    DEFAULT_BLENDER as DEFAULT_BLENDER,
    DEFAULT_GAME as DEFAULT_GAME,
    DEFAULT_GHOSTLINE_RED as DEFAULT_GHOSTLINE_RED,
    DEFAULT_INDEX as DEFAULT_INDEX,
    DEFAULT_KRAKEN as DEFAULT_KRAKEN,
    DEFAULT_OUTPUT as DEFAULT_OUTPUT,
    DEFAULT_RED_SCHEMA as DEFAULT_RED_SCHEMA,
    DEFAULT_TWEAK_ROOT as DEFAULT_TWEAK_ROOT,
    DEFAULT_WOLVENKIT as DEFAULT_WOLVENKIT,
    EQUIPMENT_SLOTS as EQUIPMENT_SLOTS,
    FRAME_LABELS as FRAME_LABELS,
    FRAME_SUFFIX as FRAME_SUFFIX,
    FRAME_TOKEN as FRAME_TOKEN,
    GALLERY_ROOT as GALLERY_ROOT,
    ItemDatabaseError as ItemDatabaseError,
    LOC_KEY as LOC_KEY,
    PACKAGE_LINE as PACKAGE_LINE,
    PRIMARY_COMPONENT_TYPES as PRIMARY_COMPONENT_TYPES,
    QUOTED_STRING as QUOTED_STRING,
    RECORD_HEADER as RECORD_HEADER,
    ROOT as ROOT,
    SCHEMA_VERSION as SCHEMA_VERSION,
    STRING_PROPERTY as STRING_PROPERTY,
    TAGS_PROPERTY as TAGS_PROPERTY,
    file_identity as file_identity,
    read_json as read_json,
    sha1_text as sha1_text,
    write_json as write_json,
)
from item_catalog import (
    TweakRecord as TweakRecord,
    app_appearance_rows as app_appearance_rows,
    app_assets as app_assets,
    asset_sources as asset_sources,
    balanced_block as balanced_block,
    build_database as build_database,
    caption_jobs as caption_jobs,
    connect as connect,
    count_variants as count_variants,
    create_schema as create_schema,
    database_summary as database_summary,
    extract_app_metadata as extract_app_metadata,
    extract_localization as extract_localization,
    fallback_title as fallback_title,
    infer_app_path as infer_app_path,
    is_shadow_component as is_shadow_component,
    load_app_index as load_app_index,
    load_localizations as load_localizations,
    load_tweak_records as load_tweak_records,
    localization_entries as localization_entries,
    localized_value as localized_value,
    mesh_frame as mesh_frame,
    parse_tweak_file as parse_tweak_file,
    query_variants as query_variants,
    record_attributes as record_attributes,
    resolve_record as resolve_record,
    resource_path as resource_path,
    typed_value as typed_value,
    variant_filter as variant_filter,
)
from item_assets import (
    material_export_fingerprint as material_export_fingerprint,
    prepare_material_export as prepare_material_export,
    prepare_material_exports_bulk as prepare_material_exports_bulk,
    source_archive_for_mesh as source_archive_for_mesh,
)
from item_render import (
    compatible_render_reports as compatible_render_reports,
    render_fingerprint as render_fingerprint,
    render_variants as render_variants,
)
from item_gallery_server import (
    GalleryHandler as GalleryHandler,
    serve as serve,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build and render the Ghostline equipment database")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--gamepath", type=Path, default=DEFAULT_GAME)
    parser.add_argument("--wolvenkit", type=Path, default=DEFAULT_WOLVENKIT)
    parser.add_argument("--kraken", type=Path, default=None)
    parser.add_argument("--ghostline-red", type=Path, default=DEFAULT_GHOSTLINE_RED)
    parser.add_argument("--red-schema", type=Path, default=DEFAULT_RED_SCHEMA)
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX)
    subparsers = parser.add_subparsers(dest="command", required=True)

    build = subparsers.add_parser("build", help="Build SQLite and JSON equipment catalogs")
    build.add_argument("--tweaks", type=Path, help="Defaults to the selected game's REDmod item database")
    build.add_argument("--apps", type=Path)
    build.add_argument("--localization", type=Path, action="append", default=[])
    build.add_argument("--extract-apps", action="store_true")
    build.add_argument("--extract-localization", action="store_true")

    render = subparsers.add_parser("render", help="Render material-aware item previews")
    render.add_argument("--database", type=Path)
    render.add_argument("--blender", type=Path, default=DEFAULT_BLENDER)
    render.add_argument("--item", default="")
    render.add_argument("--frame", choices=["", "pma", "pwa", "unknown"], default="")
    render.add_argument("--slot", default="")
    render.add_argument("--limit", type=int, default=1)
    render.add_argument("--resolution", type=int, default=1024)
    render.add_argument("--samples", type=int, default=128)
    render.add_argument("--engine", choices=["BLENDER_EEVEE", "CYCLES"], default="CYCLES")
    render.add_argument("--views", default="hero,back")
    render.add_argument(
        "--batch-size",
        type=int,
        default=25,
        help="Variants rendered per persistent Blender process",
    )
    render.add_argument(
        "--workers",
        type=int,
        default=2,
        help="Persistent Blender processes run concurrently",
    )
    render.add_argument(
        "--export-workers",
        type=int,
        default=min(12, os.cpu_count() or 1),
        help="Concurrent ghostline-red mesh/material preparation jobs",
    )
    render.add_argument(
        "--reuse-compatible",
        action="store_true",
        help="Reuse matching reports after renderer performance-only changes",
    )

    captions = subparsers.add_parser("caption-export", help="Write caption-model JSONL jobs")
    captions.add_argument("--database", type=Path)
    captions.add_argument("--file", type=Path)
    captions.add_argument("--include-unrendered", action="store_true")
    captions.add_argument("--limit", type=int, default=100000)

    gallery = subparsers.add_parser("serve", help="Serve the local searchable item gallery")
    gallery.add_argument("--database", type=Path)
    gallery.add_argument("--host", default="127.0.0.1")
    gallery.add_argument("--port", type=int, default=8766)
    gallery.add_argument("--open", action="store_true")
    return parser

def main() -> int:
    args = build_parser().parse_args()
    output = args.output.resolve()
    database = (getattr(args, "database", None) or output / "items.sqlite3").resolve()
    try:
        if args.command == "build":
            app_root = args.apps
            localization_paths = list(args.localization)
            if args.extract_apps:
                app_root = extract_app_metadata(
                    args.index.resolve(), output / "cache", args.wolvenkit.resolve(), args.gamepath.resolve()
                )
            if args.extract_localization:
                localization_paths.extend(
                    extract_localization(output / "cache", args.wolvenkit.resolve(), args.gamepath.resolve())
                )
            summary = build_database(
                database,
                (args.tweaks or args.gamepath / "tools/redmod/tweaks/base/gameplay/static_data/database/items").resolve(),
                app_root.resolve() if app_root else None,
                [path.resolve() for path in localization_paths],
                output / "catalog.json",
            )
            print(json.dumps(summary, indent=2))
        elif args.command == "render":
            result = render_variants(
                database,
                args.index.resolve(),
                output,
                args.ghostline_red.resolve(),
                args.red_schema.resolve(),
                args.blender.resolve(),
                args.gamepath.resolve(),
                args.item,
                args.frame,
                args.slot,
                args.limit,
                args.resolution,
                args.samples,
                args.engine,
                [value for value in args.views.split(",") if value],
                args.batch_size,
                args.workers,
                args.export_workers,
                args.reuse_compatible,
                kraken=args.kraken,
            )
            print(json.dumps(result, indent=2))
            return 1 if result["failures"] else 0
        elif args.command == "caption-export":
            result = caption_jobs(
                database,
                (args.file or output / "caption-jobs.jsonl").resolve(),
                not args.include_unrendered,
                args.limit,
            )
            print(json.dumps(result, indent=2))
        elif args.command == "serve":
            serve(database, output, args.host, args.port, args.open)
        return 0
    except ItemDatabaseError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
