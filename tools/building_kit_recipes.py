"""Promote compatible measured 3 m wall/frame pairs into room presets.

Topology sampling rejects filled, offset or small door apertures. This is an
offline geometric check; it does not certify live collision or device fitting.
Every other prepared module remains available in the free-placement library.
"""
import json
from pathlib import Path
import re
import shutil
import struct

from artifact_io import atomic_write_json
from building_library import CACHE, catalog

ROOT = Path(__file__).resolve().parents[1]


def projected_triangles(path):
    raw = Path(path).read_bytes()
    size = struct.unpack_from("<I", raw, 12)[0]
    document = json.loads(raw[20:20+size])
    binary_offset = 20 + size + 8

    def accessor(index):
        item = document["accessors"][index]; view = document["bufferViews"][item["bufferView"]]
        code = {5121: "B", 5123: "H", 5125: "I", 5126: "f"}[item["componentType"]]
        count = {"SCALAR": 1, "VEC3": 3}[item["type"]]
        pattern = "<" + code*count; stride = view.get("byteStride", struct.calcsize(pattern))
        offset = binary_offset + view.get("byteOffset", 0) + item.get("byteOffset", 0)
        return [struct.unpack_from(pattern, raw, offset+i*stride) for i in range(item["count"])]

    triangles = []
    for mesh in document["meshes"]:
        for primitive in mesh["primitives"]:
            if primitive.get("mode", 4) != 4:
                continue
            vertices = accessor(primitive["attributes"]["POSITION"])
            indices = [v[0] for v in accessor(primitive["indices"])] if "indices" in primitive else list(range(len(vertices)))
            for offset in range(0, len(indices)-2, 3):
                # glTF X/Y is RED X/Z. The ray spans the complete thickness.
                triangle = [vertices[i][:2] for i in indices[offset:offset+3]]
                triangles.append(triangle)
    return triangles


def covered(triangles, x, z):
    for (ax,az),(bx,bz),(cx,cz) in triangles:
        determinant = (bz-cz)*(ax-cx)+(cx-bx)*(az-cz)
        if abs(determinant)<1e-9:
            continue
        u=((bz-cz)*(x-cx)+(cx-bx)*(z-cz))/determinant
        v=((cz-az)*(x-cx)+(ax-cx)*(z-cz))/determinant
        if u>=-1e-6 and v>=-1e-6 and u+v<=1+1e-6:
            return True
    return False


def offset(record):
    low,high=record["geometry"]["min"],record["geometry"]["max"]
    return [-1.5-(low[0]+high[0])/2,-low[1],-low[2]]


def aperture_clear(triangles, dx=0, dz=0):
    from shapely.geometry import Polygon, box
    aperture=box(-2.25-dx,-dz,-.75-dx,2.4-dz)
    for triangle in triangles:
        polygon=Polygon(triangle)
        if polygon.area>1e-9 and polygon.intersection(aperture).area>1e-5:
            return False
    return True


def fits(record, doorway):
    geometry=record["geometry"];width,thickness,height=geometry["dimensions"]
    if abs(width-3)>.11 or not .04<thickness<.55 or not 2.8<height<5:
        return False
    if re.search(r"corner|cornice|conv|conc|arc|curv|slope|pit|window|elevator|double|garage",record["name"]):
        return False
    triangles=projected_triangles(CACHE/"assets"/(record["id"]+".glb"));dx,dy,dz=offset(record)
    def sample(x,z):return covered(triangles,x-dx,z-dz)
    if doorway:
        if not aperture_clear(triangles,dx,dz):return False
        if any(sample(x,z) for x in (-2.22,-2,-1.75,-1.5,-1.25,-1,-.78) for z in (.05,.5,1,1.5,2,2.35)):
            return False
        return all(sample(x,z) for x,z in ((-2.65,1.2),(-.35,1.2),(-1.5,(height+2.4)/2)))
    return all(sample(x,z) for x in (-2.8,-2.4,-1.8,-1.5,-1.2,-.6,-.2) for z in (.1,1.2,2.3,height-.1))


def promote():
    data=catalog();groups={}
    for record in data["assets"]:
        if record["status"]=="prepared" and record["role"] in ("wall","doorway"):
            groups.setdefault(record["family"],{"wall":[],"doorway":[]})[record["role"]].append(record)
    common=json.loads((ROOT/"tools/building_ui/common-kit.json").read_bytes())
    floor_records={r["path"]:r for r in data["assets"]}
    promoted=[]
    excluded=("\\int_common_a","\\int_ent_industrial_a","\\rancho_coronado")
    for family,roles in sorted(groups.items()):
        if family.endswith(excluded):continue
        walls=[r for r in roles["wall"] if fits(r,False)]
        doors=[r for r in roles["doorway"] if fits(r,True)]
        pairs=[]
        for wall in walls:
            for door in doors:
                wall_stem=re.split(r"_(?:wall|door|entrance)",wall["name"],maxsplit=1)[0]
                door_stem=re.split(r"_(?:wall|door|entrance)",door["name"],maxsplit=1)[0]
                if wall_stem!=door_stem:continue
                appearances=[a for a in wall["appearances"] if a in door["appearances"]]
                if abs(wall["geometry"]["dimensions"][2]-door["geometry"]["dimensions"][2])<.02 and appearances:
                    pairs.append((wall,door,appearances))
        if not pairs:continue
        wall,door,appearances=min(pairs,key=lambda p:(len(p[0]["name"])+len(p[1]["name"]),p[0]["path"],p[1]["path"]))
        identity="kit-"+wall["id"][:12]
        name=family.removeprefix("base\\environment\\architecture\\common\\int\\").removeprefix("base\\environment\\architecture\\").replace("\\"," / ").replace("_"," ")
        height=round(wall["geometry"]["dimensions"][2],3)
        recipe={"id":identity,"name":name.title(),"grid":3,"wall_height":height,"storey_height":round(height+.4,3),
            "wall_thickness":round(max(wall["geometry"]["dimensions"][1],door["geometry"]["dimensions"][1]),4),
            "door_clearance":[1.5,2.4],"wall_appearances":appearances,"floor_appearances":common["floor_appearances"],
            "pieces":{role:dict(piece) for role,piece in common["pieces"].items()},"family":family,"status":"geometry-checked",
            "provenance":"Measured vanilla geometry. Closed-wall coverage sampled; centred 1.5 x 2.4 m aperture checked against projected triangle intersections. Shared common floors/ceilings. Live gameplay remains unverified."}
        for role,record in (("wall",wall),("doorway",door)):
            recipe["pieces"][role]={"mesh":record["path"],"preview_appearance":appearances[0],"catalog_asset":record["id"],
                "offset":offset(record),"source_json_sha256":record["source_json_sha256"],"preview_sha256":record["preview_sha256"]}
        for role in ("floor","ceiling"):
            recipe["pieces"][role]["catalog_asset"]=floor_records[recipe["pieces"][role]["mesh"]]["id"]
        atomic_write_json(ROOT/"tools/building_ui/kits"/(identity+".json"),recipe)
        for role,piece in recipe["pieces"].items():
            target=ROOT/"generated/building-editor/assets"/identity/(role+".glb");target.parent.mkdir(parents=True,exist_ok=True)
            shutil.copy2(CACHE/"assets"/(piece["catalog_asset"]+".glb"),target)
        promoted.append({"id":identity,"name":recipe["name"],"family":family,"wall":wall["path"],"doorway":door["path"]})
    coverage=ROOT/"reference/world/building-room-kit-coverage.json"
    if coverage.is_file():
        retained={r["id"] for r in promoted}
        for previous in json.loads(coverage.read_bytes())["promoted"]:
            identity=previous["id"]
            if identity not in retained and re.fullmatch(r"kit-[0-9a-f]{12}",identity):
                path=ROOT/"tools/building_ui/kits"/(identity+".json")
                if path.is_file():path.unlink()
    atomic_write_json(coverage,{"promoted":promoted,"original_presets":3,
        "notes":["Families without a compatible centred 3 m pair remain available in the module library.",
                 "Sampled geometric suitability does not certify source collision, materials or live doors."]})
    return promoted


if __name__=="__main__": print(json.dumps(promote(),indent=2))
