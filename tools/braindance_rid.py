"""Braindance compatibility CLI and public entry points."""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
from braindance_support.rid_io import DEFAULT_HANDOFF as DEFAULT_HANDOFF, DEFAULT_OUTPUT as DEFAULT_OUTPUT, compile_binary as compile_binary, load_json as load_json
from braindance_support.rid_types import RID_KIND as RID_KIND, RidCompileError as RidCompileError, RidValidationReport as RidValidationReport
from braindance_support.rid_validation import validate_compiled_document as validate_compiled_document, validate_handoff as validate_handoff
from braindance_support.rid_codec import _animation_buffer_from_actor as _animation_buffer_from_actor, _animation_buffer_from_camera as _animation_buffer_from_camera, _camera_trajectory as _camera_trajectory, _const_transform_key_sort_key as _const_transform_key_sort_key, _continuous_quaternions as _continuous_quaternions, _encode_spline_motion_extraction as _encode_spline_motion_extraction, _interpolate_pose_values as _interpolate_pose_values, _is_near_vector as _is_near_vector, _longest_locomotion_segment as _longest_locomotion_segment, _merge_template_pose_channels as _merge_template_pose_channels, _motion_extraction_positions as _motion_extraction_positions, _multiply_quaternions as _multiply_quaternions, _pack_const_transform_key as _pack_const_transform_key, _pack_raw_transform_key as _pack_raw_transform_key, _pack_time as _pack_time, _pack_track_key as _pack_track_key, _proxy_pose_motion_sync as _proxy_pose_motion_sync, _raw_transform_key_sort_key as _raw_transform_key_sort_key, _red_transform as _red_transform, _replace_compressed_buffer as _replace_compressed_buffer, _rotate_vector as _rotate_vector, _sample_time as _sample_time, _unpack_raw_transform_key as _unpack_raw_transform_key, _world_actor_transform as _world_actor_transform, encode_compressed_animation as encode_compressed_animation, euler_degrees_to_quaternion as euler_degrees_to_quaternion, inspect_compressed_buffer as inspect_compressed_buffer, inspect_motion_extraction as inspect_motion_extraction, look_at_quaternion as look_at_quaternion
from braindance_support.rid_compile import _actor_sample as _actor_sample, _camera_joints as _camera_joints, _camera_red_quaternion as _camera_red_quaternion, _camera_tracks as _camera_tracks, _channel_track_samples as _channel_track_samples, _collect_buffer_ids as _collect_buffer_ids, _compile_actor_aux_channel as _compile_actor_aux_channel, _freshen_buffer_ids as _freshen_buffer_ids, _freshen_handle_ids as _freshen_handle_ids, _sampled_camera_lod_tracks as _sampled_camera_lod_tracks, _sampled_camera_trajectory as _sampled_camera_trajectory, _select_actor_slots as _select_actor_slots, _template_actor_slots as _template_actor_slots, compile_rid_document as compile_rid_document
from braindance_support.rid_io import ROOT as ROOT, WOLVENKIT_CLI as WOLVENKIT_CLI, _run as _run, _validation_buffer_hashes as _validation_buffer_hashes, deserialize_rid as deserialize_rid, file_sha256 as file_sha256, find_wolvenkit as find_wolvenkit, serialize_template as serialize_template, verify_binary as verify_binary, write_json as write_json
from braindance_support.rid_types import ANIMATION_SAMPLE_SPACE as ANIMATION_SAMPLE_SPACE, CONST_TRACK_AUX as CONST_TRACK_AUX, CONST_TRANSLATION_AUX as CONST_TRANSLATION_AUX, CR2W_MAGIC as CR2W_MAGIC, RID_REPORT_KIND as RID_REPORT_KIND, _cname as _cname, _patch_durations as _patch_durations, _root as _root, _serial as _serial, _set_animation_name as _set_animation_name, _set_cname as _set_cname, _set_next_serial as _set_next_serial, _set_serial as _set_serial, _set_tag as _set_tag, _tag_signature as _tag_signature
from braindance_support.rid_validation import _collect_handle_ids as _collect_handle_ids


def _print_validation(report: RidValidationReport) -> None:
    print(
        json.dumps(
            {
                "ok": report.ok,
                "errors": list(report.errors),
                "warnings": list(report.warnings),
                "details": report.details,
            },
            indent=2,
        )
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    validate = commands.add_parser("validate", help="Validate a handoff or compiled RID JSON")
    validate.add_argument("path", type=Path)
    compile_command = commands.add_parser(
        "compile",
        help="Compile a handoff with a vanilla .scenerid template",
    )
    compile_command.add_argument("--handoff", type=Path, default=DEFAULT_HANDOFF)
    compile_command.add_argument("--template", type=Path, required=True)
    compile_command.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    compile_command.add_argument("--json-output", type=Path)
    compile_command.add_argument("--report", type=Path)
    compile_command.add_argument("--wolvenkit", type=Path)
    compile_command.add_argument(
        "--actor-template",
        action="append",
        dest="actor_templates",
        help="Template actor signature, in handoff actor order; repeat for each actor",
    )
    compile_command.add_argument(
        "--no-verify",
        action="store_true",
        help="Skip the generated binary's WolvenKit JSON verification pass",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "validate":
            document = load_json(args.path)
            if document.get("kind") == RID_KIND:
                report = validate_handoff(document)
            else:
                report = validate_compiled_document(document)
            _print_validation(report)
            return 0 if report.ok else 1
        build_report = compile_binary(
            args.handoff,
            args.template,
            args.output,
            wolvenkit_path=args.wolvenkit,
            actor_template_signatures=args.actor_templates,
            json_output_path=args.json_output,
            report_path=args.report,
            verify=not args.no_verify,
        )
        print(json.dumps(build_report, indent=2))
        return 0
    except RidCompileError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
