"""Local audio volume anchoring, routing integrity and unsafe-input rejection."""
import copy
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
from building_audio import compile_audio_areas,audio_area_node,verify_audio_area
from building_builder import world_point
from generate_world import HandleAllocator


class InteriorAudioTests(unittest.TestCase):
    def scene(self):
        return {'layout':{'origin':dict(x=20,y=40,z=3,yaw=90),
            'audio_areas':[dict(id='lobby',preset='residential-ground',position=[2,5,0],size=[10,6,3.7])]}}

    def test_volume_matches_world_and_survives_routing_audit(self):
        scene=self.scene();compile_audio_areas(scene,world_point)
        area=scene['audio_areas'][0]
        for a,b in zip(area['world_position'],[15,42,3]):self.assertAlmostEqual(a,b)
        node=audio_area_node(area,HandleAllocator())['Data'];verify_audio_area(node,node)
        self.assertIs(type(node['notifiers'][0]['Data']['occlusionEnabled']),int)
        for mutation in ('event','parameter','outline'):
            other=copy.deepcopy(node)
            settings=other['notifiers'][0]['Data']['Settings']['Data']
            if mutation=='event':settings['EventsOnActive'][0]['event']['$value']='wrong_event'
            elif mutation=='parameter':settings['Parameters'][0]['value']=0
            else:other['outline']['Data']['buffer']='wrong'
            with self.assertRaises(ValueError):verify_audio_area(node,other)

    def test_rejects_invalid_volume_and_unknown_presets(self):
        for change in [dict(preset='unknown'),dict(position=[0,0,float('nan')]),dict(size=[1,1,-1]),dict(id='bad id')]:
            s=self.scene();s['layout']['audio_areas'][0].update(change)
            with self.assertRaises(ValueError):compile_audio_areas(s,world_point)
        s=self.scene();s['layout']['audio_areas']*=2
        with self.assertRaises(ValueError):compile_audio_areas(s,world_point)
