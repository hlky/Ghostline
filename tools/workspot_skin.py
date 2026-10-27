"""Source-mesh linear blend skinning with explicit deformation-rig rest poses."""
from pathlib import Path

import numpy as np

from lipsync_glb import read_glb


def transform(translation, rotation, scale):
    x, y, z, w = np.asarray(rotation, dtype=float) / np.linalg.norm(rotation)
    matrix = np.eye(4)
    matrix[:3, :3] = np.array([
        [1 - 2 * (y*y + z*z), 2 * (x*y-z*w), 2 * (x*z+y*w)],
        [2 * (x*y+z*w), 1 - 2 * (x*x+z*z), 2 * (y*z-x*w)],
        [2 * (x*z-y*w), 2 * (y*z+x*w), 1 - 2 * (x*x+y*y)],
    ]) @ np.diag(scale)
    matrix[:3, 3] = translation
    return matrix


def rest_matrix(bone):
    rest = bone["model_rest"]
    return transform(rest["translation"], rest["rotation"], rest["scale"])


def model_matrices(actor, frame):
    matrices = []
    for index, parent in enumerate(actor["parents"]):
        local = transform(actor["local_translations"][frame][index], actor["local_rotations"][frame][index], actor["local_scales"][frame][index])
        matrices.append(local if parent < 0 else matrices[parent] @ local)
    return dict(zip(actor["bone_names"], matrices))


def deformation_deltas(core_models, deform_contract):
    rest = [rest_matrix(bone) for bone in deform_contract["bones"]]
    posed = []
    result = {}
    for index, bone in enumerate(deform_contract["bones"]):
        parent = bone["parent"]
        if bone["name"] in core_models:
            matrix = core_models[bone["name"]]
        elif parent < 0:
            matrix = rest[index]
        else:
            local = np.linalg.inv(rest[parent]) @ rest[index]
            matrix = posed[parent] @ local
        posed.append(matrix)
        result[bone["name"]] = matrix @ np.linalg.inv(rest[index])
    return result


def accessor(document, binary, index):
    item = document["accessors"][index]
    if "sparse" in item:
        raise ValueError("Sparse mesh accessors are not supported")
    view = document["bufferViews"][item["bufferView"]]
    components = {"SCALAR": 1, "VEC2": 2, "VEC3": 3, "VEC4": 4, "MAT4": 16}[item["type"]]
    dtype = np.dtype({5120: "i1", 5121: "u1", 5122: "<i2", 5123: "<u2", 5125: "<u4", 5126: "<f4"}[item["componentType"]])
    offset = view.get("byteOffset", 0) + item.get("byteOffset", 0)
    stride = view.get("byteStride", dtype.itemsize * components)
    end = offset + max(0, item["count"] - 1) * stride + components * dtype.itemsize
    if end > len(binary):
        raise ValueError("Mesh accessor exceeds its binary buffer")
    data = np.ndarray((item["count"], components), dtype=dtype, buffer=binary, offset=offset, strides=(stride, dtype.itemsize)).copy()
    if item.get("normalized") and dtype.kind in ("u", "i"):
        data = np.maximum(data.astype(float) / np.iinfo(dtype).max, -1)
    return data


def load_parts(path, *, rigid_head=False):
    document, chunks = read_glb(Path(path))
    binary = next(raw for kind, raw in chunks if kind == 0x004E4942)
    if len(document.get("skins", [])) != 1:
        raise ValueError("Expected exactly one source mesh skin")
    names = [document["nodes"][i]["name"] for i in document["skins"][0]["joints"]]
    result = []
    # MeshOnly exports are world-rest geometry with identity mesh nodes.
    # glTF Y-up -> RED/Blender Z-up is (x,-z,y).
    for node in document["nodes"]:
        if "mesh" not in node:
            continue
        if any(k in node for k in ("matrix", "translation", "rotation", "scale")):
            raise ValueError("Unexpected transformed mesh node; cannot assume world-rest vertices")
        mesh = document["meshes"][node["mesh"]]
        if "_LOD_" in mesh.get("name", "") and not mesh["name"].endswith("_LOD_1"):
            continue
        for primitive in mesh["primitives"]:
            if primitive.get("mode", 4) != 4:
                raise ValueError("Only triangular mesh primitives are supported")
            attrs = primitive["attributes"]
            p = accessor(document, binary, attrs["POSITION"]).astype(float)
            vertices = p[:, [0, 2, 1]] * [1, -1, 1]
            faces = accessor(document, binary, primitive["indices"]).reshape(-1, 3)
            joints = np.concatenate([accessor(document, binary, attrs[k]) for k in ("JOINTS_0", "JOINTS_1") if k in attrs], axis=1).astype(int)
            weights = np.concatenate([accessor(document, binary, attrs[k]) for k in ("WEIGHTS_0", "WEIGHTS_1") if k in attrs], axis=1).astype(float)
            if np.any(joints >= len(names)) or np.any(joints < 0) or joints.shape != weights.shape:
                raise ValueError("Invalid mesh skin indices/weights")
            total = weights.sum(axis=1)
            if np.any(total < 0.99) or np.any(total > 1.01) or np.any(weights < 0):
                raise ValueError("Source skin weights must sum to one")
            weights /= total[:, None]
            result.append({"name": mesh["name"], "vertices": vertices, "faces": faces, "joints": joints, "weights": weights, "joint_names": names, "rigid_head": rigid_head})
    return result


def skin_vertices(part, deltas, head_delta=None):
    vertices = np.column_stack((part["vertices"], np.ones(len(part["vertices"]))))
    if part.get("rigid_head"):
        if head_delta is None:
            raise ValueError("Neutral head requires its source Head transform")
        return (vertices @ head_delta.T)[:, :3]
    active = np.unique(part["joints"][part["weights"] > 0])
    missing = [part["joint_names"][i] for i in active if part["joint_names"][i] not in deltas]
    if missing:
        raise ValueError(f"Weighted mesh joints absent from deformation rig: {missing}")
    matrices = np.stack([deltas.get(name, np.eye(4)) for name in part["joint_names"]])
    output = np.zeros_like(vertices)
    for influence in range(part["weights"].shape[1]):
        output += np.einsum("nij,nj->ni", matrices[part["joints"][:, influence]], vertices) * part["weights"][:, influence, None]
    return output[:, :3]
