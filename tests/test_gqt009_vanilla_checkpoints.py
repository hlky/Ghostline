"""GQT009 console candidate: stock entities, gate geometry and replay rearming."""
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import race_builder


class GQT009VanillaCheckpointTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.project = ROOT / 'projects/test-quests/gqt009'
        spec = cls.project / 'implementation/builder.spec.json'
        cls.config = json.loads(spec.read_text())
        survey = json.loads((spec.parent / cls.config['survey']).read_text())
        cls.survey_route = survey['world_spec']['race_splines'][0]
        _, cls.bindings, cls.docs, _ = race_builder.documents(
            cls.config, survey, cls.project, cls.project / 'generated/vanilla-test')
        cls.world, _ = race_builder.survey_bindings(survey, race_builder.normalize(cls.config))

    def test_no_custom_entity_or_diagnostic_dependency(self):
        self.assertEqual(self.config['checkpoint_mode'], 'vanilla')
        self.assertFalse(self.config['vehicle_diagnostics'])
        self.assertFalse(any(path.endswith('.ent') for path in self.docs))
        self.assertNotIn('ghostline_race_vehicle_trace', json.dumps(self.docs))
        profiles = json.loads((self.project / 'packaging/profiles.json').read_text())
        for profile in profiles['profiles'].values():
            self.assertFalse(any('vehicletrace' in path.lower()
                                 for path in profile.get('include_loose', [])))

    def test_checkpoint_count_is_independent_of_route_detail(self):
        self.assertEqual(len(self.bindings['checkpoints']), 9)
        self.assertEqual(self.world['race_splines'][0]['points'], self.survey_route['points'])
        self.assertEqual(len(self.survey_route['points']), 57)
        for doc in self.docs.values():
            for item in race_builder.walk(doc):
                if item.get('$type') == 'VehicleRaceQuestEvent':
                    self.assertEqual(item['maxCheckpoints'], 10)
        def gates(points):
            world = {'race_splines':[{'points':points,'position':{'x':0,'y':0,'z':0}}],
                     'markers':[], 'triggers':[]}
            groups = {'checkpoint':[]}
            race_builder.route_checkpoints(world,groups,'test',125)
            return world['markers']
        self.assertEqual(gates([[0,0,0],[1000,0,0]]),
                         gates([[x,0,0] for x in range(0,1001,10)]))

    def test_race_splines_and_entrant_home_nodes_remain_streamed_for_full_course(self):
        checked = set()
        entrant_refs = {self.bindings['community']}
        for community in self.world['communities']:
            if community['ref'] == self.bindings['community']:
                entrant_refs.update(spot['ref'] for entry in community['entries'] for spot in entry['spots'])
        for doc in self.docs.values():
            root = doc['Data']['RootChunk']
            if root['$type'] != 'worldStreamingSector':
                continue
            placements = {p['NodeIndex']:p for p in root['nodeData']['Data']}
            for index, (wrapper, reference) in enumerate(zip(root['nodes'],root['nodeRefs'])):
                alias = reference['$value'].rsplit('/',1)[-1]
                if 'SplineNode' in wrapper['Data']['$type'] or alias in entrant_refs:
                    self.assertGreater(placements[index]['MaxStreamingDistance'], 1201)
                    self.assertGreater(placements[index]['UkFloat1'], 1201)
                    checked.add(alias)
        self.assertTrue(entrant_refs <= checked)

    def test_normal_finish_preserves_vehicle_workspot_and_restores_entry(self):
        doc = next(doc for path,doc in self.docs.items() if path.endswith('_lifecycle.questphase'))
        handles = {item['HandleId']:item['Data'] for item in race_builder.walk(doc)
                   if 'HandleId' in item and 'Data' in item}
        nodes = {n['Data']['id']:n['Data'] for n in doc['Data']['RootChunk']['graph']['Data']['nodes']}
        def resolve(wrapper):
            return handles[wrapper.get('HandleId',wrapper.get('HandleRefId'))]
        owners = {s.get('HandleId',s.get('HandleRefId')):node_id
                  for node_id,node in nodes.items() for s in node['sockets']}
        def targets(socket):
            return [owners[resolve(c)['destination'].get('HandleId',resolve(c)['destination'].get('HandleRefId'))]
                    for c in socket['connections']]
        call = next(n for n in nodes.values() if n.get('phaseResource',{}).get('DepotPath',{}).get('$value','').endswith('_attempt.questphase'))
        for outcome in ('Success','Failure'):
            socket = next(resolve(s) for s in call['sockets'] if resolve(s)['name']['$value']==outcome)
            pending, seen = targets(socket), set()
            while pending:
                node_id = pending.pop()
                if node_id in seen:
                    continue
                seen.add(node_id)
                for socket in nodes[node_id]['sockets']:
                    socket = resolve(socket)
                    if socket['type']=='Output' and socket['name']['$value']!='CutSource':
                        pending.extend(targets(socket))
            items = [item for node_id in seen for item in race_builder.walk(nodes[node_id])]
            self.assertFalse(any(i.get('function')=='StopWorkspot' for i in items))
            doors = [i for i in items if i.get('$type')=='questToggleDoor_NodeType'
                     and i.get('vehicleRef',{}).get('reference',{}).get('$value')=='#owned_vehicle']
            self.assertTrue(any(i['doorAction']=='ResetInteractions' for i in doors))
            for door in ('seat_front_left','seat_front_right'):
                self.assertTrue(any(i['doorAction']=='ForceUnlock' and i.get('door')==door for i in doors))
                self.assertTrue(any(i['doorAction']=='EnableInteraction' and i.get('door')==door for i in doors))

    def test_stock_instances_keep_directions_and_authored_gate_dimensions(self):
        expected = {item['ref']: item for item in self.world['entities']
                    if 'checkpoint_direction' in item}
        triggers = {item['ref']: item for item in self.world['triggers']}
        seen = set()
        for doc in self.docs.values():
            root = doc['Data']['RootChunk']
            if root['$type'] != 'worldStreamingSector':
                continue
            for node, ref in zip(root['nodes'], root['nodeRefs']):
                alias = ref['$value'].rsplit('/', 1)[-1]
                if alias not in expected:
                    continue
                seen.add(alias)
                node = node['Data']
                self.assertEqual(node['entityTemplate']['DepotPath']['$value'],
                                 race_builder.VANILLA_CHECKPOINT)
                package = node['instanceData']['Data']['buffer']['Data']
                self.assertEqual(package['CruidDict'], {
                    '0': '2451685433260048384', '1': '2451685433209716736',
                    '2': '1734314053524791296'})
                direction = expected[alias]['checkpoint_direction']
                record = ('LCDScreens.RaceFinish' if direction == 'Finish'
                          else 'LCDScreens.RaceCheckpoint' + direction)
                for widget in package['Chunks'][:2]:
                    self.assertEqual(widget['signSelector']['Data']['recordID']['$value'], record)
                trigger = package['Chunks'][2]
                self.assertFalse(trigger['isEnabled'])  # Only the current gate may count.
                outline = trigger['outline']['Data']
                authored = triggers[expected[alias]['checkpoint_trigger']]['outline']
                xs = [point['X'] for point in outline['points']]
                ys = [point['Y'] for point in outline['points']]
                self.assertEqual(max(xs) - min(xs), authored['width'])
                self.assertEqual(max(ys) - min(ys), authored['depth'])
                self.assertEqual(outline['height'], authored['height'])
        self.assertEqual(seen, set(expected))

    def test_reusable_attempt_resets_counter_and_uses_one_quest_writer_per_gate(self):
        attempt = next(doc for path, doc in self.docs.items() if path.endswith('_attempt.questphase'))
        items = list(race_builder.walk(attempt))
        enabled = {item['objectRef']['$value'] for item in items
                   if item.get('$type') == 'questDeviceManager_NodeTypeParams'
                   and item['deviceAction']['$value'] == 'QuestForceEnabled'}
        visuals = {*self.bindings['checkpoint_visuals'], self.bindings['finish_visual']}
        self.assertEqual(enabled, set())
        toggles = {}
        for item in items:
            if item.get('$type') == 'questEntityManagerToggleComponent_NodeTypeParams':
                ref = item['objectRef']['reference']['$value']
                toggles.setdefault(ref, {})[item['componentName']['$value']] = item['enable']
        for visual in visuals:
            self.assertEqual(toggles[visual], {
                'ui_front': 1, 'ui_back': 1, 'trigger': 0})
        # Rearming lives inside the reusable attempt, not a one-time root setup.
        counter_resets = [item for item in items
                          if item.get('$type') == 'questSetVar_NodeType'
                          and item.get('factName') == 'sq024_current_race_checkpoint_fact_add']
        self.assertEqual([(item['setExactValue'], item['value']) for item in counter_resets],
                         [(1, value) for value in range(11)])
        # Inspect executable edges: every ordered road crossing leads directly
        # to its counter commit, with no dependency on a device-fact callback.
        handles = {item['HandleId']:item['Data'] for item in items
                   if 'HandleId' in item and 'Data' in item}
        nodes = {n['Data']['id']:n['Data'] for n in attempt['Data']['RootChunk']['graph']['Data']['nodes']}
        owners = {s.get('HandleId',s.get('HandleRefId')):node_id
                  for node_id,node in nodes.items() for s in node['sockets']}
        def resolve(wrapper):
            return handles[wrapper.get('HandleId',wrapper.get('HandleRefId'))]
        def outgoing(node):
            return [owners[resolve(c)['destination'].get('HandleId',resolve(c)['destination'].get('HandleRefId'))]
                    for s in node['sockets'] if resolve(s)['type']=='Output'
                    and resolve(s)['name']['$value']!='CutSource' for c in resolve(s)['connections']]
        for count,ref in enumerate([*self.bindings['checkpoints'],self.bindings['finish']],1):
            guards = {node['condition']['Data']['type']:node for node in nodes.values()
                      if node.get('condition',{}).get('Data',{}).get('$type')=='questTriggerCondition'
                      and node['condition']['Data']['triggerAreaRef']['$value']==ref
                      and node['condition']['Data']['isPlayerActivator']}
            self.assertEqual(outgoing(guards['IsOutside']), [guards['IsInside']['id']])
            commit = next(n for n in nodes.values()
                          if isinstance(n.get('type'),dict)
                          and n['type'].get('Data',{}).get('$type')=='questSetVar_NodeType'
                          and n['type']['Data'].get('factName')=='sq024_current_race_checkpoint_fact_add'
                          and n['type']['Data']['value']==count)
            self.assertEqual(outgoing(guards['IsInside']), [commit['id']])


if __name__ == '__main__':
    unittest.main()
