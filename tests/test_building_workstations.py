"""Native office fixture bindings and placement ownership."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'tools'))
from building_builder import compile_layout
from building_encounters import content_documents, quest_fragment
from quest_compiler import build_read_terminal_document_phase
from quest_types import CompiledStage


class WorkstationTests(unittest.TestCase):
    def layout(self):
        return json.loads((ROOT/'projects/experiments/building-lab/buildings/akpp-logistics-open-shell.building.json').read_bytes())

    def test_chair_and_desk_own_child_transforms(self):
        layout = self.layout()
        scene = compile_layout(layout)
        worker = scene['workstations'][0]
        self.assertEqual(worker['actor']['position'], [2.1,1.05,.05])
        self.assertEqual(worker['actor']['yaw'], 0)
        self.assertEqual(next(m for m in layout['modules'] if m['id']=='office-chair')['yaw'],0)
        self.assertEqual(worker['computer']['yaw'],90)
        self.assertAlmostEqual(worker['computer']['position'][2],1.061)
        self.assertGreater(worker['computer']['position'][2]-.21109,.8493)
        moved = copy.deepcopy(layout)
        desk = next(m for m in moved['modules'] if m['id']=='office-desk')
        desk['position'][0] += .5
        chair = next(m for m in moved['modules'] if m['id']=='office-chair')
        chair['position'][1] -= .3
        chair['yaw'] = 90
        actual = compile_layout(moved)['workstations'][0]
        self.assertAlmostEqual(actual['computer']['position'][0], worker['computer']['position'][0]+.5)
        self.assertAlmostEqual(actual['actor']['position'][1],worker['actor']['position'][1]-.3)
        self.assertEqual(actual['actor']['yaw'],90)
        # Furniture edits never change stable quest references or completion facts.
        for key in ('community','seat','computer_ref','read_fact'):
            self.assertEqual(actual[key], worker[key])

    def test_native_community_computer_and_quest_block_contract(self):
        scene = compile_layout(self.layout())
        with tempfile.TemporaryDirectory(dir=ROOT/'.tmp') as directory:
            docs, block, contract = content_documents(scene,Path(directory))
            self.assertEqual(len(docs),4)
            self.assertTrue(block.endswith('_content.streamingblock'))
            registry = next(d['Data']['RootChunk'] for n,d in docs.items() if n.endswith('_always.streamingsector'))
            worker = registry['nodes'][0]['Data']['communitiesData'][0]
            self.assertEqual(worker['entriesInitialState'][0]['entryActiveOnStart'],1)
            entry = worker['template']['Data']['entries'][0]['Data']
            self.assertEqual(entry['characterRecordId']['$value'],'Character.WorkerSpecialistMale')
            sector = next(d['Data']['RootChunk'] for n,d in docs.items() if n.endswith('_content.streamingsector'))
            spot = next(n['Data'] for n in sector['nodes'] if n['Data']['$type']=='worldAISpotNode')
            self.assertEqual(spot['isWorkspotInfinite'],1)
            self.assertEqual(spot['isWorkspotStatic'],1)
            pc = next(n['Data'] for n in sector['nodes'] if n['Data']['$type']=='worldDeviceNode')
            ps = pc['instanceData']['Data']['buffer']['Data']['Chunks'][1]['persistentState']['Data']
            setup = ps['computerSetup']
            self.assertEqual(setup['mailsStructure'],[])
            document = setup['filesStructure'][0]['content'][0]
            self.assertEqual(document['wasRead'],0)
            binding = contract['workstations'][0]
            fragment = quest_fragment(contract)
            self.assertEqual(fragment['terminal_stages'][0]['completion_fact'],binding['read_fact'])
            self.assertTrue(fragment['actors'][0]['requires_character_spawned_gate'])
            self.assertEqual(document['questInfo']['factName']['$value'],binding['read_fact'])
            self.assertNotIn('kab_07',json.dumps(pc))
            stage = CompiledStage(0,'read_office_file','read_terminal_document','ready',
                r'mod\building_lab\office_read.questphase',dict(computer=binding['computer'],
                completion_fact=binding['read_fact'],objective='quests/minor_quest/office_fixture/read'))
            phase = build_read_terminal_document_phase(stage,Path(directory)/'read.questphase')
            self.assertIn(binding['read_fact'],json.dumps(phase))

    def test_quest_activation_and_replaceable_character(self):
        layout = self.layout()
        layout['workstations'][0]['actor']['active_on_start'] = False
        layout['workstations'][0]['actor']['record'] = 'Character.FutureOfficeManager'
        scene = compile_layout(layout)
        with tempfile.TemporaryDirectory(dir=ROOT/'.tmp') as directory:
            docs,_,contract = content_documents(scene,Path(directory))
            registry = next(d['Data']['RootChunk'] for n,d in docs.items() if n.endswith('_always.streamingsector'))
            self.assertEqual(registry['nodes'][0]['Data']['communitiesData'][0]['entriesInitialState'][0]['entryActiveOnStart'],0)
            self.assertEqual(contract['workstations'][0]['character'],'Character.FutureOfficeManager')

    def test_fixtures_stream_without_quest_prefab_activation(self):
        scene = compile_layout(self.layout())
        with tempfile.TemporaryDirectory(dir=ROOT/'.tmp') as directory:
            docs,_,_ = content_documents(scene,Path(directory))
            sector = docs['akpp-logistics-open-shell_content.streamingsector']['Data']['RootChunk']
            block = docs['akpp-logistics-open-shell_content.streamingblock']['Data']['RootChunk']
            descriptor = block['descriptors'][0]
            self.assertEqual((sector['category'],sector['level']),('Exterior',0))
            self.assertEqual((descriptor['category'],descriptor['level']),('Exterior',0))
            self.assertEqual(descriptor['questPrefabNodeRef']['$value'],'0')
            self.assertEqual(block['descriptors'][1]['category'],'AlwaysLoaded')
            for placement in sector['nodeData']['Data']:
                for axis in ('X','Y','Z'):
                    self.assertLess(descriptor['streamingBox']['Min'][axis],placement['Position'][axis])
                    self.assertGreater(descriptor['streamingBox']['Max'][axis],placement['Position'][axis])

    def test_reject_invalid_actor_and_missing_prop(self):
        for key,value in [('record','not-a-record'),('active_on_start','yes'),('workspot','../bad.workspot')]:
            layout=self.layout()
            layout['workstations'][0]['actor'][key]=value
            with self.assertRaises(ValueError):
                compile_layout(layout)
        layout=self.layout()
        layout['workstations'][0]['chair']='office-desk'
        with self.assertRaises(ValueError):
            compile_layout(layout)
        layout=self.layout()
        layout['workstations'][0]['chair']='missing'
        with self.assertRaises(ValueError):
            compile_layout(layout)


if __name__ == '__main__':
    unittest.main()
