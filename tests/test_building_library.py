"""Catalogue measurements, original pivots, collision and native placement."""
import copy
import hashlib
import json
from pathlib import Path
import struct
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import building_library as library
from building_builder import BuildingError, compile_layout, native_documents, export_project
from building_navigation import route


def fixture_glb(path, *, transformed=False):
    data = {"nodes": [{"mesh": 0, **({"translation": [1, 0, 0]} if transformed else {})}],
            "meshes": [{"primitives": [{"attributes": {"POSITION": 0}, "indices": 1}]}],
            "accessors": [{"min": [-3, 0, -.2], "max": [0, 4, 0], "count": 8}, {"count": 36}]}
    raw = json.dumps(data).encode(); raw += b" " * (-len(raw) % 4)
    path.write_bytes(struct.pack("<4sIII4s", b"glTF", 2, len(raw) + 20, len(raw), b"JSON") + raw)


class LibraryMeasurementTests(unittest.TestCase):
    def test_glb_measures_red_axes_and_preserves_off_center_pivot(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.glb"; fixture_glb(path)
            result = library.glb_geometry(path)
            self.assertEqual(result["min"], [-3, 0, 0])
            self.assertEqual(result["max"], [0, .2, 4])
            self.assertEqual(result["triangles"], 12)

    def test_transformed_or_invalid_preview_is_not_certified(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.glb"; fixture_glb(path, transformed=True)
            with self.assertRaisesRegex(ValueError, "transforms"):
                library.glb_geometry(path)
            path.write_bytes(b"bad")
            with self.assertRaises(ValueError): library.glb_geometry(path)

    def test_measure_record_handles_omitted_default_appearance_and_real_names(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); raw = root / "source.json"; preview = root / "preview.glb"; fixture_glb(preview)
            raw.write_text(json.dumps({"Data": {"RootChunk": {"$type": "CMesh", "boundingBox": {
                "Min": dict(zip("XYZ", [-3, 0, 0])), "Max": dict(zip("XYZ", [0, .2, 4]))},
                "appearances": [{"Data": {}}, {"Data": {"name": {"$value": "blue"}}}]}}}), encoding="utf-8")
            record = library.measure_record(r"base\environment\architecture\common\int\test\wall.mesh", raw, preview)
            self.assertEqual(record["status"], "prepared")
            self.assertEqual(record["appearances"], ["default", "blue"])
            self.assertEqual(record["source_json_sha256"], hashlib.sha256(raw.read_bytes()).hexdigest())
            changed=json.loads(raw.read_bytes());changed["Header"]={"ArchiveFileName":"a-different-temporary-path"}
            raw.write_text(json.dumps(changed),encoding="utf-8")
            refreshed=library.measure_record(record["path"],raw,preview)
            self.assertEqual(record["source_content_sha256"],refreshed["source_content_sha256"])
            self.assertNotEqual(record["source_json_sha256"],refreshed["source_json_sha256"])

    def test_discovery_groups_do_not_include_filenames(self):
        self.assertEqual(library.family_path(r"base\environment\architecture\common\wall.mesh"), r"base\environment\architecture\common")
        self.assertEqual(library.role_hint(r"base\environment\architecture\common\int\int_kts_staircase_a\int_kts_staircase_a_handrail_l300_a.mesh"), "railing")
        self.assertEqual(library.role_hint(r"base\environment\architecture\common\int\int_kts_staircase_a\int_kts_staircase_a_wall_h400_l300_a.mesh"), "wall")
        with tempfile.TemporaryDirectory() as directory:
            checked=Path(directory)/"catalog.json"
            checked.write_text(json.dumps({"assets":[{"path":"base\\mesh.mesh"}],"non_mesh_references":["base\\material.mi"]}),encoding="utf-8")
            with patch.object(library,"EVIDENCE",Path(directory)/"missing.json"),patch.object(library,"CATALOG",checked):
                self.assertEqual(set(library.discover()),{"base\\mesh.mesh","base\\material.mi"})

    def test_search_filters_and_pages_without_conflating_role_with_readiness(self):
        rows = [{"id": str(i), "path": f"base\\apartments\\wall_{i}.mesh", "family": "apartment", "role": "wall", "status": "prepared"} for i in range(60)]
        with patch.object(library, "catalog", return_value={"assets": rows}):
            result = library.search(query="apartments wall", family="apartment", offset=48)
            self.assertEqual(result["total"], 60)
            self.assertEqual(len(result["assets"]), 12)
            self.assertEqual(library.search(role="stairs")["total"], 0)


class ModulePlacementTests(unittest.TestCase):
    def setUp(self):
        self.record = {"id": "abc123", "path": r"base\environment\architecture\common\wall.mesh", "name": "wall", "role": "wall",
            "status": "prepared", "source_json_sha256": "source", "preview_sha256": "geometry", "appearances": ["default", "blue"],
            "geometry": {"min": [-3, -.1, 0], "max": [3, .1, 4]}}
        self.patcher = patch.object(library, "catalog", return_value={"assets":[self.record], "by_id": {"abc123": self.record}})
        self.patcher.start(); self.addCleanup(self.patcher.stop)
        self.layout = {"schema_version": 1, "id": "module_test", "name": "Module test", "kit": "common-3m",
            "origin": {"x": 100, "y": -200, "z": 40, "yaw": 90}, "rooms": [
                {"id": "room", "name": "Room", "x": 0, "y": 0, "width": 6, "depth": 6, "level": 0}],
            "openings": {}, "modules": [{"id": "wall", "asset": "abc123", "position": [3, 3, 0], "yaw": 0, "level": 0}]}

    def test_actual_asset_appearance_and_identity_reach_native_export(self):
        self.layout["modules"][0]["appearance"] = "blue"
        scene = compile_layout(self.layout)
        module = next(i for i in scene["instances"] if i.get("kind") == "module")
        self.assertEqual(module["world_position"], [97, -197, 40])
        sector, block, _ = native_documents(scene, ROOT / ".tmp/module-native")
        node = next(n["Data"] for n in sector["Data"]["RootChunk"]["nodes"] if n["Data"].get("meshAppearance", {}).get("$value") == "blue")
        self.assertEqual(node["mesh"]["DepotPath"]["$value"], self.record["path"])

    def test_base_centre_and_original_pivot_are_distinct(self):
        self.record["geometry"] = {"min": [-6, -2, 1], "max": [0, 0, 5]}
        self.layout["modules"][0]["yaw"] = 90
        scene = compile_layout(self.layout); module = next(i for i in scene["instances"] if i.get("kind") == "module")
        self.assertEqual(module["position"], [2, 6, -1])
        self.layout["modules"][0]["anchor"] = "pivot"
        module = next(i for i in compile_layout(self.layout)["instances"] if i.get("kind") == "module")
        self.assertEqual(module["position"], [3, 3, 0])

    def test_existing_shell_reference_is_visible_but_not_exported_or_collidable(self):
        self.layout['modules'][0]['reference_only']=True
        scene=compile_layout(self.layout)
        self.assertTrue(next(v for v in scene['instances'] if v.get('kind')=='module')['reference_only'])
        sector,_,_=native_documents(scene,ROOT/'.tmp/reference-native')
        self.assertFalse(any(n['Data'].get('mesh',{}).get('DepotPath',{}).get('$value')==self.record['path']
                             for n in sector['Data']['RootChunk']['nodes']))
        with tempfile.TemporaryDirectory() as directory:
            export_project(scene,Path(directory))
            exported=json.loads((Path(directory)/'source/raw/mod/building_lab/module_test.streamingsector.json').read_bytes())
            self.assertFalse(any(n['Data'].get('mesh',{}).get('DepotPath',{}).get('$value')==self.record['path']
                                 for n in exported['Data']['RootChunk']['nodes']))
        self.layout['modules'][0]['collision']='box'
        with self.assertRaises(BuildingError):compile_layout(self.layout)
        self.layout['modules'][0]['collision']='none'
        self.layout['rooms']=[]
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(BuildingError,'references alone'):
                export_project(compile_layout(self.layout),Path(directory))

    def test_reviewed_shell_import_preserves_world_transform_and_rejects_stale_source(self):
        from building_shell_import import import_shell
        import math
        with tempfile.TemporaryDirectory(dir=ROOT/'.tmp') as directory:
            source=Path(directory)/'shell.json'
            document={'Data':{'RootChunk':{'nodes':[{'Data':{'$type':'worldStaticMeshNode',
                'mesh':{'DepotPath':{'$value':self.record['path']}}}}],
                'nodeData':{'Data':[{'NodeIndex':0,'Position':dict(X=100,Y=-197,Z=40),
                    'Orientation':dict(i=0,j=0,k=math.sqrt(.5),r=math.sqrt(.5)),
                    'Scale':dict(X=2,Y=1,Z=1)}]}}}}
            source.write_text(json.dumps(document))
            spec={'name':'Shell','layout':{**self.layout,'modules':[]},'sources':[{
                'source':source.relative_to(ROOT).as_posix(),'sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
                'path':'base\\shell.streamingsector','expectedNodes':1,'placements':[
                    {'id':'existing','index':0,'mesh':self.record['path']}]}]}
            layout=import_shell(spec)
            scene=compile_layout(layout)
            module=next(v for v in scene['instances'] if v.get('reference_only'))
            for actual,expected in zip(module['world_position'],[100,-197,40]):
                self.assertAlmostEqual(actual,expected)
            self.assertEqual(module['scale'],[2,1,1])
            self.assertAlmostEqual(module['world_orientation']['k'],math.sqrt(.5))
            self.assertEqual(scene['retrofit_patches'],[])
            spec['sources'][0]['placements'][0]['index']=-1
            with self.assertRaises(ValueError):import_shell(spec)
            source.write_text(source.read_text()+'\n')
            with self.assertRaisesRegex(ValueError,'changed'):import_shell(spec)

    def test_solid_box_blocks_route_while_visual_only_does_not(self):
        self.assertTrue(route(compile_layout(self.layout)["navigation"], [1.5, 1.5, 0], [1.5, 4.5, 0])["reachable"])
        self.layout["modules"][0]["collision"] = "box"
        self.assertFalse(route(compile_layout(self.layout)["navigation"], [1.5, 1.5, 0], [1.5, 4.5, 0])["reachable"])

    def test_source_change_invalid_appearance_duplicate_and_door_box_rejected(self):
        for changes in ({"source_sha256": "old"}, {"appearance": "invented"}, {"position": [0, float("nan"), 0]}):
            layout = copy.deepcopy(self.layout); layout["modules"][0].update(changes)
            with self.assertRaises(BuildingError): compile_layout(layout)
        layout = copy.deepcopy(self.layout); layout["modules"] *= 2
        with self.assertRaises(BuildingError): compile_layout(layout)
        self.record["role"] = "doorway"; self.layout["modules"][0]["collision"] = "box"
        with self.assertRaises(BuildingError): compile_layout(self.layout)

    def test_module_only_project_can_export_without_inventing_navigation(self):
        self.layout["rooms"] = []
        with tempfile.TemporaryDirectory() as directory:
            scene = compile_layout(self.layout)
            self.assertEqual(scene["navigation"]["triangles"], [])
            export_project(scene, Path(directory))
            self.assertTrue((Path(directory) / "source/raw/mod/building_lab/module_test.streamingsector.json").is_file())

    def test_named_building_archive_does_not_replace_default_package(self):
        self.layout['archive_name']='Ghostline_AKPPLogistics'
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            export_project(compile_layout(self.layout),root)
            self.assertTrue((root/'source/resources/Ghostline_AKPPLogistics.archive.xl').is_file())
            self.assertFalse((root/'source/resources/Ghostline_BuildingLab.archive.xl').exists())
            profile=json.loads((root/'packaging/profiles.json').read_bytes())
            self.assertEqual(profile['profiles']['building-lab']['archive_name'],'Ghostline_AKPPLogistics')
            self.layout['archive_name']='../invalid'
            with self.assertRaises(BuildingError):export_project(compile_layout(self.layout),root)


if __name__ == "__main__": unittest.main()
