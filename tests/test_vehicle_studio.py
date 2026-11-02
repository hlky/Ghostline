"""Targeted full-detail vehicle selection and existing-renderer integration checks."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from vehicle_full_studio import mesh_components


class VehicleStudioTests(unittest.TestCase):
    def test_full_assembly_keeps_parts_and_omits_proxies_and_effect_shells(self):
        def component(name, **extra):
            return {'name': {'$value': name}, 'mesh': {'DepotPath': {'$value': 'base\\car.mesh'}}, **extra}
        rows = [component('body'), component('wheel_front_left'), component('door'),
                component('body_shadow'), component('fx_cutout'), component('engine_overheating'),
                component('proxy', **{'$type': 'entAppearanceProxyMeshComponent'}),
                component('disabled', isEnabled=0)]
        self.assertEqual([c['name']['$value'] for c in mesh_components(rows)], ['body', 'wheel_front_left', 'door'])

    def test_selection_preserves_chunk_mask_and_requested_material(self):
        original = {'name': {'$value': 'wheel'}, 'mesh': {'DepotPath': {'$value': 'base\\wheel.mesh'}},
                    'chunkMask': '13', 'meshAppearance': {'$value': 'chrome'}}
        selected = mesh_components([original])[0]
        self.assertEqual(selected['chunkMask'], '13')
        self.assertEqual(selected['meshAppearance']['$value'], 'chrome')
        selected['resolved_glb'] = 'generated.glb'
        self.assertNotIn('resolved_glb', original)


if __name__ == '__main__':
    unittest.main()
