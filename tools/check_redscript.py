"""Compile candidate scripts with the installed scc C API in an isolated cache, without popups.

API contract: https://github.com/jac3km4/redscript/blob/v0.5.28/scc/lib/include/scc.h
"""
from __future__ import annotations

import argparse
import ctypes
import json
import shutil
import uuid
from pathlib import Path


def check_scripts(game: Path, sources: Path, output: Path, *, replace_folder: str) -> dict:
    run = output / uuid.uuid4().hex
    r6 = run / "r6"
    cache = r6 / "cache/final.redscripts"
    cache.parent.mkdir(parents=True)
    shutil.copyfile(game / "r6/cache/final.redscripts", cache)
    shutil.copytree(game / "r6/scripts", r6 / "scripts",
                    ignore=lambda path, names: [name for name in names if name.casefold() == replace_folder.casefold()])
    library = ctypes.CDLL(str(game / "engine/tools/scc_lib.dll"))
    signature = {
        "scc_settings_new": ([ctypes.c_char_p], ctypes.c_void_p),
        "scc_settings_set_custom_cache_file": ([ctypes.c_void_p, ctypes.c_char_p], None),
        "scc_settings_set_output_cache_file": ([ctypes.c_void_p, ctypes.c_char_p], None),
        "scc_settings_add_script_path": ([ctypes.c_void_p, ctypes.c_char_p], None),
        "scc_settings_disable_error_popup": ([ctypes.c_void_p], None),
        "scc_compile": ([ctypes.c_void_p], ctypes.c_void_p),
        "scc_get_success": ([ctypes.c_void_p], ctypes.c_void_p),
        "scc_copy_error": ([ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t], ctypes.c_size_t),
        "scc_free_result": ([ctypes.c_void_p], None),
    }
    for name, (arguments, result) in signature.items():
        function = getattr(library, name)  # Refuse old APIs before invoking the compiler.
        function.argtypes, function.restype = arguments, result
    encode = lambda path: str(path.resolve()).encode("utf-8")
    settings = library.scc_settings_new(encode(r6))
    library.scc_settings_disable_error_popup(settings)
    library.scc_settings_set_custom_cache_file(settings, encode(cache))
    compiled = cache.with_name("candidate.redscripts")
    library.scc_settings_set_output_cache_file(settings, encode(compiled))
    directories = [sources, *[p / "Scripts" for p in (game / "red4ext/plugins").iterdir() if (p / "Scripts").is_dir()]]
    for path in directories:
        library.scc_settings_add_script_path(settings, encode(path))
    result = library.scc_compile(settings)  # Consumes settings; result owns the output.
    try:
        success = bool(library.scc_get_success(result))
        buffer = ctypes.create_string_buffer(16384)
        library.scc_copy_error(result, buffer, len(buffer))
        receipt = {"passed": success, "error": buffer.value.decode("utf-8"),
                   "cache": str(compiled), "sources": [str(p) for p in directories],
                   "game_cache_modified": False, "error_popups_disabled": True}
        (run / "verification.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
        return receipt
    finally:
        library.scc_free_result(result)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--game", type=Path, required=True)
    parser.add_argument("--sources", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--replace-folder", required=True)
    args = parser.parse_args()
    result = check_scripts(args.game, args.sources, args.output, replace_folder=args.replace_folder)
    print(json.dumps(result, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
