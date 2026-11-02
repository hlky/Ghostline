"""Targeted vehicle catalog, preview provenance and HTTP contract tests."""
from contextlib import closing
import http.server
import json
from pathlib import Path
import sys
import tempfile
import threading
import unittest
import urllib.error
import urllib.request
from unittest import mock

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import vehicle_catalog as catalog
from vehicle_database import GalleryHandler, attach_preview
from vehicle_previews import crop_part, extract_previews
from vehicle_performance import HUD_RESOURCE
from vehicle_studio import appearance_binding, appearance_proxy


FIXTURE = r'''
package Vehicle
Base {
 entityTemplatePath = "base\vehicles\car.ent";
 displayName = "LocKey#123";
 type = "Vehicle.Car";
 manufacturer = "Vehicle.Maker";
 tags = ["Fast"];
 icon = "UIIcon.car";
 vehicleUIData = "Vehicle.Specs";
 vehEngineData = "Vehicle.Engine";
}
child : Base {
 appearanceName = "paint_red";
 tags += ["Quest"];
}
replacement : child { tags = ["Police"]; }
Maker { enumName = "Test Motors"; }
Specs { horsepower = 500.f; mass = 1200.f; driveLayout = "LocKey#124"; productionYear="2070"; }
Engine {
 engineMaxTorque = 600.f;
 maxRPM = 7000.f;
 fk< VehicleGear >[] gears = [{maxSpeed = 10.f;}, {maxSpeed = 42.f;}];
}
Inline : Base {
 vehEngineData = {engineMaxTorque = 650.f;} : Engine;
}
'''


class VehicleTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.game = self.root / 'game'
        self.output = self.root / 'catalog'
        source = self.game / 'tools/redmod/tweaks/base/gameplay/static_data/database/vehicles/test.tweak'
        source.parent.mkdir(parents=True)
        source.write_text(FIXTURE)
        icons = source.parent.parent / 'ui/icons/test.tweak'
        icons.parent.mkdir(parents=True)
        icons.write_text('package UIIcon\ncar {atlasResourcePath="base\\preview.inkatlas"; atlasPartName="red";}')
        self.source = source
        catalog.build(self.game, self.output, [])

    def test_inheritance_inline_engines_and_gear_speed_provenance(self):
        records, _ = catalog.load_records(self.game)
        rows = {r['record_id']: r for r in catalog.vehicle_rows(records, {'123': 'Super Car', '124': 'AWD', '2070': 'Unrelated localization'})}
        child = rows['Vehicle.child']
        self.assertEqual(child['title'], 'Super Car')
        self.assertEqual(child['tags'], ['Fast', 'Quest'])
        self.assertEqual(rows['Vehicle.replacement']['tags'], ['Police'])
        self.assertEqual(child['template'], r'base\vehicles\car.ent')
        self.assertEqual(child['drivetrain'], 'AWD')
        self.assertEqual(child['year'], '2070')
        self.assertEqual(child['stats']['gear_speed_limit_raw'], 42)
        self.assertNotIn('top_speed_mph', child['stats'])
        self.assertEqual(rows['Vehicle.Inline']['stats']['engine_torque'], 650)
        self.assertEqual(rows['Vehicle.Inline']['stats']['max_rpm'], 7000)
        self.assertIn('not measured', child['stats_note'])

    def test_cycle_is_rejected_and_missing_values_stay_unknown(self):
        self.source.write_text('package Vehicle\na : b {}\nb : a {}')
        records, _ = catalog.load_records(self.game)
        with self.assertRaisesRegex(catalog.VehicleError, 'cycle'):
            records.resolve('Vehicle.a')
        self.source.write_text('package Vehicle\na {entityTemplatePath="base\\car.ent";}')
        records, _ = catalog.load_records(self.game)
        row = catalog.vehicle_rows(records, {})[0]
        self.assertIsNone(row['stats']['horsepower'])
        self.assertIsNone(row['stats']['gear_speed_limit_raw'])

    def test_queries_and_rebuild_preserve_attached_studio_render(self):
        image = self.root / 'studio.png'
        Image.new('RGBA', (30, 20), (255, 0, 0, 255)).save(image)
        attach_preview(self.output, 'Vehicle.child', image)
        catalog.build(self.game, self.output, [])
        with closing(catalog.connect(self.output / 'vehicles.sqlite3')) as db:
            self.assertEqual(catalog.query(db, q='Vehicle.child', rendered=True)['total'], 1)
            self.assertEqual(catalog.query(db, q="' OR 1=1 --")['total'], 0)
            self.assertEqual(catalog.query(db, manufacturer='Test Motors')['total'], 4)
            self.assertEqual(catalog.query(db, offset=1, limit=1)['offset'], 1)
            self.assertEqual(catalog.summary(db)['previews'], 1)
            self.assertEqual(catalog.summary(db)['studio_renders'], 1)
            self.assertEqual(catalog.query(db, preview_kind='studio')['total'], 1)
            self.assertEqual(catalog.query(db, preview_kind='game')['total'], 0)
        with self.assertRaisesRegex(catalog.VehicleError, 'Unknown vehicle'):
            attach_preview(self.output, 'Vehicle.missing', image)

    def test_build_publishes_calculated_speed_and_curve_provenance(self):
        data = {'sources': [{'resource': HUD_RESOURCE, 'data_sha256': 'fixture'}],
                'curves': {HUD_RESOURCE: {'speed_to_multiplier': {
                    'InterpolationType': 'Linear',
                    'Elements': [{'Point': 0, 'Value': 4.6}, {'Point': 100, 'Value': 4.6}],
                }}}}
        with mock.patch('vehicle_catalog.extract_curve_data', return_value=data):
            catalog.build(self.game, self.output, [], speed_tools={'red': 'fixture', 'schema': 'fixture'})
        with closing(catalog.connect(self.output / 'vehicles.sqlite3')) as db:
            row = catalog.query(db, q='Vehicle.child', sort='speed')['vehicles'][0]
            self.assertAlmostEqual(row['stats']['hud_top_speed_mph'], 42 * 4.6)
            self.assertEqual(row['performance']['gear_index'], 1)
            self.assertEqual(catalog.summary(db)['source']['performance']['sources'], data['sources'])

    def test_atlas_crop_uses_top_left_uv_and_rejects_invalid_rectangles(self):
        image = Image.new('RGBA', (100, 60), (255, 0, 0, 255))
        image.paste((0, 255, 0, 255), (0, 0, 50, 30))
        part = {'clippingRectInUVCoords': {'Left': 0, 'Top': 0, 'Right': .5, 'Bottom': .5}}
        cropped = crop_part(image, part)
        self.assertEqual(cropped.size, (50, 30))
        self.assertEqual(cropped.getpixel((0, 0)), (0, 255, 0, 255))
        part['clippingRectInUVCoords']['Right'] = 2
        with self.assertRaises(catalog.VehicleError):
            crop_part(image, part)

    def test_preview_fallback_is_labelled_and_studio_render_is_preserved(self):
        image = self.root / 'atlas.png'
        Image.new('RGBA', (100, 60), 'red').save(image)
        attach_preview(self.output, 'Vehicle.child', image)
        with catalog.connect(self.output / 'vehicles.sqlite3') as db:
            row = json.loads(db.execute('SELECT data FROM vehicles WHERE record_id="Vehicle.Inline"').fetchone()[0])
            row['atlas'] = ''; row['atlas_part'] = ''
            db.execute('UPDATE vehicles SET data=? WHERE record_id=?', (json.dumps(row), row['record_id']))
        class Resources:
            fingerprint = 'fixture'
            def atlas(self, depot):
                return {'slots': {'Elements': [{'texture': {'DepotPath': {'$value': 'base\\preview.xbm'}},
                    'parts': [{'partName': {'$value': 'red'}, 'clippingRectInUVCoords': {'Left': 0, 'Top': 0, 'Right': 1, 'Bottom': 1}}]}]}}
            def texture(self, depot):
                return image
        result = extract_previews(self.output / 'vehicles.sqlite3', self.output, Resources())
        self.assertEqual(result['missing'], 0)
        with closing(catalog.connect(self.output / 'vehicles.sqlite3')) as db:
            self.assertEqual(catalog.query(db, q='Vehicle.child')['vehicles'][0]['preview_kind'], 'studio')
            row = catalog.query(db, q='Vehicle.Inline')['vehicles'][0]
            self.assertTrue(row['preview_metadata']['model_fallback'])

    def test_http_pagination_bad_queries_and_image_traversal(self):
        image = self.output / 'renders/test/hero.png'
        image.parent.mkdir(parents=True)
        Image.new('RGBA', (30, 20), 'blue').save(image)
        with catalog.connect(self.output / 'vehicles.sqlite3') as db:
            db.execute('INSERT INTO previews VALUES(?,?,?,?)', ('Vehicle.child', str(image), 'studio',
                json.dumps({'images': {'hero': str(image), 'outside': str(self.root / 'secret.png')}})))
        handler = type('TestGallery', (GalleryHandler,), {'database': self.output / 'vehicles.sqlite3', 'output': self.output})
        server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        base = f'http://127.0.0.1:{server.server_port}'
        with urllib.request.urlopen(base + '/api/vehicles?limit=1&offset=1') as response:
            result = json.load(response)
        self.assertEqual(len(result['vehicles']), 1)
        with urllib.request.urlopen(base + '/api/vehicles?studio=1') as response:
            rendered = json.load(response)['vehicles']
        self.assertEqual(len(rendered), 1)
        self.assertEqual(rendered[0]['image_views'], {'hero': '/images/renders/test/hero.png'})
        self.assertNotIn('preview_path', rendered[0])
        with urllib.request.urlopen(base + rendered[0]['image_views']['hero']) as response:
            self.assertEqual(response.headers['Content-Type'], 'image/png')
            self.assertEqual(response.read(), image.read_bytes())
        for path, code in [('/api/vehicles?sort=invalid', 400), ('/api/vehicles?limit=bad', 400),
                           ('/images/..%2F..%2Fsecret.png', 403), ('/unknown', 404)]:
            with self.subTest(path=path), self.assertRaises(urllib.error.HTTPError) as error:
                urllib.request.urlopen(base + path)
            self.assertEqual(error.exception.code, code)

    def test_render_binding_preserves_exact_appearance_and_rejects_random(self):
        entity = {'defaultAppearance': {'$value': 'random'}, 'appearances': [
            {'name': {'$value': 'paint_red'}, 'appearanceName': {'$value': 'red'},
             'appearanceResource': {'DepotPath': {'$value': r'base\car.app'}}}]}
        self.assertEqual(appearance_binding(entity, 'paint_red'), (r'base\car.app', 'red'))
        for requested in ('paint_blue', 'random', ''):
            with self.subTest(requested=requested), self.assertRaises(catalog.VehicleError):
                appearance_binding(entity, requested)
        entity['defaultAppearance'] = {'$value': 'paint_red'}
        self.assertEqual(appearance_binding(entity, ''), (r'base\car.app', 'red'))

    def test_render_proxy_requires_exact_definition_and_assembled_geometry(self):
        app = {'appearances': [{'Data': {'name': {'$value': 'red'},
               'proxyMesh': {'DepotPath': {'$value': r'base\red.mesh'}}}}]}
        self.assertEqual(appearance_proxy(app, 'red'), r'base\red.mesh')
        with self.assertRaises(catalog.VehicleError):
            appearance_proxy(app, 'blue')
        app['appearances'][0]['Data'].pop('proxyMesh')
        with self.assertRaises(catalog.VehicleError):
            appearance_proxy(app, 'red')


if __name__ == '__main__':
    unittest.main()
