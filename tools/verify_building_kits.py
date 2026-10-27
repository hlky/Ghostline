"""Batch-write and independently verify native resources for every room preset."""
import argparse
import copy
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

from artifact_io import atomic_write_json
from building_builder import CACHE, ROOT, compile_layout, export_project, kits, verify_native_project
from toolchain import resolve_tool


def verify(output):
    output=Path(output).resolve();projects=[];paths=[]
    source=json.loads((ROOT/"projects/experiments/building-lab/buildings/navigation-lab.building.json").read_bytes())
    for catalog in kits():
        layout=copy.deepcopy(source);layout.update(id="verify_"+catalog["id"],kit=catalog["id"],name="Verify "+catalog["name"],wall_appearance=catalog["wall_appearances"][0])
        scene=compile_layout(layout);project=output/catalog["id"]
        export_project(scene,project)
        raw=sorted((project/"source/raw/mod/building_lab").glob("*.json"))
        projects.append((scene,project,raw));paths.extend(raw)
    with tempfile.TemporaryDirectory(prefix="building-kits-native-") as temporary:
        subprocess.run([str(resolve_tool("wolvenkit")),"convert","deserialize",*[str(p) for p in paths],"-o",temporary],
                       check=True,capture_output=True,text=True,timeout=600)
        for scene,project,raw in projects:
            for path in raw:
                name=path.name.removesuffix(".json");destination=project/"source/archive/mod/building_lab"/name
                destination.parent.mkdir(parents=True,exist_ok=True)
                shutil.copy2(Path(temporary)/name,destination)
            verify_native_project(scene,project,raw)
    report={"schema_version":1,"method":"WolvenKit batch serialization and independent ghostline-red readback",
        "runtime_verified":False,"presets":len(projects),"resources":len(paths),"projects":[
            {"id":scene["kit"]["id"],"name":scene["kit"]["name"],"stats":scene["stats"],
             "binaries":json.loads((project/"building-report.json").read_bytes())["binaries"]} for scene,project,raw in projects]}
    atomic_write_json(output/"verification.json",report)
    return report


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument("--out",type=Path,default=CACHE/"kit-verification")
    result=verify(parser.parse_args().out);print(json.dumps({k:result[k] for k in ("presets","resources","runtime_verified")}))
