"""Appearance identities must never fall back to a model's repeated UI icon."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import vehicle_catalog as catalog
from vehicle_studio import resolve_slot, selected_chunk_materials
from vehicle_variant_render import valid_images
from vehicle_variants import bindings_for_record, create_tables, query_variants, variant_id
from tests.test_vehicle_database import FIXTURE


class VehicleVariantTests(unittest.TestCase):
    def test_mesh_material_selection_uses_exact_index_and_visible_chunks(self):
        appearances = {f'paint{i}{i}': [f'body{i}', 'glass'] for i in range(12)}
        sidecar = {'Appearances': appearances,
                   'Materials': [{'Name': f'body{i}'} for i in range(12)] + [{'Name': 'glass'}]}
        geometry = {'meshes': [
            {'name': 'submesh_00_LOD_1', 'extras': {'materialNames': [f'body{i}' for i in range(12)]}},
            {'name': 'submesh_01_LOD_1', 'extras': {'materialNames': ['glass'] * 12}}]}
        materials, key = selected_chunk_materials(sidecar, geometry, 'paint10', 1)
        self.assertEqual(key, 'paint1010')
        self.assertEqual([m['Name'] for m in materials], ['body10'])
        with self.assertRaises(catalog.VehicleError):
            selected_chunk_materials(sidecar, geometry, 'unavailable')
        materials, _ = selected_chunk_materials(sidecar, geometry, None)
        self.assertEqual([m['Name'] for m in materials], ['body0', 'glass'])

    def test_ambiguous_chunk_materials_are_rejected(self):
        sidecar = {'Appearances': {'red0': ['red'], 'blue1': ['blue']},
                   'Materials': [{'Name': 'red'}, {'Name': 'blue'}]}
        geometry = {'meshes': [{'name': 'submesh_00_LOD_1', 'extras': {'materialNames': ['red']}}]}
        with self.assertRaises(catalog.VehicleError):
            selected_chunk_materials(sidecar, geometry, 'blue')

    def test_all_authored_appearances_are_exposed_when_record_has_no_exact_name(self):
        entity = {'defaultAppearance': {'$value': 'red'}, 'appearances': [
            {'name': {'$value': 'red'}}, {'name': {'$value': 'blue'}}]}
        row = {'appearance': '', 'template': 'base\\car.ent'}
        self.assertEqual([v['name']['$value'] for v in bindings_for_record(row, entity)], ['red', 'blue'])
        row['appearance'] = 'blue'
        self.assertEqual([v['name']['$value'] for v in bindings_for_record(row, entity)], ['blue'])
        row['appearance'] = 'missing'
        with self.assertRaises(catalog.VehicleError):
            bindings_for_record(row, entity)

    def test_variant_images_do_not_fall_back_to_record_icon_or_another_appearance(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / 'game/tools/redmod/tweaks/base/gameplay/static_data/database/vehicles/test.tweak'
            source.parent.mkdir(parents=True)
            source.write_text(FIXTURE)
            output = root / 'database'
            catalog.build(root / 'game', output, [])
            with catalog.connect(output / 'vehicles.sqlite3') as db:
                create_tables(db)
                for name in ('red', 'blue'):
                    key = variant_id('base\\car.ent', name)
                    data = {'variant_id': key, 'template': 'base\\car.ent', 'appearance': name,
                            'app_resource': 'base\\car.app', 'app_appearance': name,
                            'records': ['Vehicle.child'], 'visual_tags': []}
                    db.execute('INSERT INTO vehicle_variants VALUES(?,?,?,?)', (key, data['template'], name, json.dumps(data)))
                    db.execute('INSERT INTO vehicle_variant_records VALUES(?,?,?)', (key, 'Vehicle.child', 1))
                db.execute('INSERT INTO previews VALUES(?,?,?,?)', ('Vehicle.child', 'shared-icon.png', 'game', '{}'))
                self.assertEqual(query_variants(db, rendered=True)['total'], 0)
                db.execute('INSERT INTO variant_previews VALUES(?,?,?,?)',
                           (variant_id('base\\car.ent', 'red'), 'red-render.png', 'studio', '{}'))
                rows = {r['appearance']: r for r in query_variants(db)['vehicles']}
                self.assertEqual(rows['red']['preview_path'], 'red-render.png')
                self.assertIsNone(rows['blue']['preview_path'])
                self.assertNotEqual(rows['red']['variant_id'], rows['blue']['variant_id'])

    def test_an_existing_image_for_another_paint_cannot_satisfy_the_render(self):
        with tempfile.TemporaryDirectory() as temporary:
            image = Path(temporary) / 'red.png'; image.write_bytes(b'fixture')
            metadata = {'template': 'car.ent', 'appearance': 'red', 'geometry': 'game_full_detail',
                        'resolution': 1536, 'images': {'hero': str(image)}}
            self.assertFalse(valid_images(metadata, {'template': 'car.ent', 'appearance': 'blue'}, 1536, ['hero']))
            self.assertTrue(valid_images(metadata, {'template': 'car.ent', 'appearance': 'red'}, 1536, ['hero']))

    def test_identical_duplicate_engine_slots_are_valid_but_conflicts_are_not(self):
        slot = {'slotName': {'$value': 'door'}, 'boneName': {'$value': 'door_bone'}}
        self.assertEqual(resolve_slot({'slots': [slot, dict(slot)]}, 'door'), slot)
        other = {'slotName': {'$value': 'door'}, 'boneName': {'$value': 'other_bone'}}
        with self.assertRaises(catalog.VehicleError):
            resolve_slot({'slots': [slot, other]}, 'door')


if __name__ == '__main__':
    unittest.main()
