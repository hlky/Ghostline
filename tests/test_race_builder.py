"""Targeted race compilation and lifecycle contracts; no live game required."""
import copy
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
import race_builder
from game_scout.core import Library
from game_scout.races import RacePlans
from explore_questphase import QuestphaseExplorer


class RaceBuilderTests(unittest.TestCase):
    @unittest.skipUnless(os.environ.get('GHOSTLINE_RED_TEST_CLI'),'Set GHOSTLINE_RED_TEST_CLI for native conversion integration')
    def test_native_conversion_from_empty_output_preserves_speed_and_width_sections(self):
        self.races.mark(self.race,'start_grid',{'x':0,'y':10,'z':0},270)
        exported=self.races.export(self.race)
        self.survey=json.loads(Path(exported['manifest_path']).read_text())
        self.config['entrants'].append({'id':'two','grid':1,'vehicle':'Vehicle.v_standard2_archer_quartz',
                                       'driver':'Character.sq024_city_race_corpo_racer'})
        spline=self.survey['world_spec']['race_splines'][0]
        spline['speed_sections']=[{'start':0,'end':1,'speed_mps':17.25}]
        spline['width_sections']=[{'from':0,'to':1,'left':3.25,'right':4.5}]
        output=self.root/'native-output'
        self.assertFalse(output.exists())
        cli=Path(os.environ['GHOSTLINE_RED_TEST_CLI']).resolve()
        schema=self.root/'schema.json'
        receipt=race_builder.build(self.spec(),output_root=output,deserialize=True,red_cli=cli,schema=schema)
        self.assertEqual(receipt['serializer'],'ghostline-red')
        self.assertEqual(len(list((output/'source/archive').rglob('*.*'))),9)
        binary=next((output/'source/archive').rglob('course.streamingsector'))
        decoded=self.root/'course.readback.json'
        race_builder.red_serialize(binary,decoded,red_cli=cli,schema=schema)
        course=json.loads(decoded.read_text())['Data']['RootChunk']
        node=next(n['Data'] for n in course['nodes'] if n['Data']['$type']=='worldRaceSplineNode')
        self.assertEqual(node['speedChangeSections'][0]['targetSpeed_M_P_S'],17.25)
        self.assertEqual(node['offsets'][0]['left'],3.25)
        self.assertEqual(node['offsets'][0]['right'],4.5)

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        races = RacePlans(Library(self.root/'library'))
        race = races.create('Course','gqt009')['id']
        self.races,self.race = races,race
        for role,x,y in [('spline_point',0,0),('spline_point',50,0),('spline_point',100,25),
                         ('checkpoint',50,0),('checkpoint',80,10),('start_grid',0,5),
                         ('player_start',0,0),('staging',-10,0),('activation',-10,0),('finish',100,25)]:
            races.mark(race,role,{'x':x,'y':y,'z':0},270)
        exported = races.export(race)
        self.survey = json.loads(Path(exported['manifest_path']).read_text())
        self.config = {'schema_version':1,'id':'race_test','title':'Race test','survey':'survey.json',
                       'entrants':[{'id':'one','grid':0,'vehicle':'Vehicle.v_standard2_archer_quartz',
                                    'driver':'Character.sq024_city_race_corpo_racer'}]}
        self.project = ROOT/'projects/test-quests/gqt009'

    def compile(self):
        return race_builder.documents(self.config,self.survey,self.project,self.root/'build')

    def spec(self):
        (self.root/'survey.json').write_text(json.dumps(self.survey),encoding='utf8')
        path = self.root/'race.json'
        path.write_text(json.dumps(self.config),encoding='utf8')
        return path

    def phase(self, docs, kind):
        depot = next(d for d in docs if d.endswith('_'+kind+'.questphase'))
        path = self.root/(kind+'.json')
        path.write_text(json.dumps(docs[depot]),encoding='utf8')
        return QuestphaseExplorer(path)

    def test_survey_builds_world_registry_journal_and_distinct_entrant_entries(self):
        config,binding,docs,registration = self.compile()
        self.assertEqual(len(docs),9)
        self.assertEqual(len(registration['quest']['phases']),1)
        self.assertTrue(registration['quest']['phases'][0]['path'].endswith('_root.questphase'))
        registry = next(d for d in docs.values() if d['Data']['RootChunk'].get('category')=='AlwaysLoaded')
        entries = [x for x in race_builder.walk(registry) if x.get('$type')=='communitySpawnEntry']
        self.assertEqual({e['entryName']['$value'] for e in entries},{'one_vehicle','one_driver'})
        self.assertEqual({e['characterRecordId']['$value'] for e in entries},
                         {'Vehicle.v_standard2_archer_quartz','Character.sq024_city_race_corpo_racer'})
        states = [x for x in race_builder.walk(registry) if x.get('$type')=='worldCommunityEntryInitialState']
        self.assertTrue(all(x['entryActiveOnStart']==0 for x in states))
        self.assertEqual(len(binding['checkpoint_visuals']),2)

    def test_activation_boundaries_only_reference_retained_nodes(self):
        _, binding, docs, _ = self.compile()
        scene = docs[binding['activation_scene']]
        graph = scene['Data']['RootChunk']['sceneGraph']['Data']
        self.assertEqual([node['id'] for node in graph['startNodes']], [55])
        self.assertEqual([node['id'] for node in graph['endNodes']], [161])
        race_builder.validate_activation_graph(scene)

    def test_activation_restores_player_pose_before_reveal(self):
        _, binding, docs, _ = self.compile()
        scene = docs[binding['activation_scene']]
        nodes = {node['Data']['nodeId']['id']: node['Data']
                 for node in scene['Data']['RootChunk']['sceneGraph']['Data']['graph']}
        reset = nodes[146]['questNode']['Data']
        self.assertEqual(reset['$type'],'questTeleportPuppetNodeDefinition')
        self.assertEqual(reset['entityReference']['Data']['refLocalPlayer'],1)
        self.assertEqual(reset['params']['Data']['destinationRef']['Data']['entityReference']
                         ['reference']['$value'],binding['activation'])
        destinations = [d['nodeId']['id'] for s in nodes[146]['outputSockets']
                        for d in s['destinations']]
        self.assertCountEqual(destinations,[138,142])

    def test_all_resources_generate_without_reading_templates(self):
        original_open = Path.open
        def open_input(path, *args, **kwargs):
            if 'templates' in path.parts and path.name != 'project.json':
                raise AssertionError(f'Race build attempted to read a template: {path}')
            return original_open(path, *args, **kwargs)
        with patch.object(Path, 'open', open_input):
            _, binding, docs, _ = self.compile()
        scene = docs[binding['activation_scene']]['Data']['RootChunk']
        use = next(node['Data'] for node in scene['sceneGraph']['Data']['graph']
                   if node['Data']['nodeId']['id'] == 125)
        self.assertEqual(use['questNode']['Data']['paramsV1']['Data']['$type'], 'scnUseSceneWorkspotParamsV1')
        self.assertEqual(len(scene['resouresReferences']['lipsyncAnimSets']), 1)
        self.assertEqual(scene['resouresReferences']['cinematicAnimSets'], [])

    def test_world_choice_has_native_interaction_parameters(self):
        _, binding, docs, _ = self.compile()
        scene = docs[binding['activation_scene']]
        nodes = {node['Data']['nodeId']['id']: node['Data']
                 for node in scene['Data']['RootChunk']['sceneGraph']['Data']['graph']}
        choice = nodes[119]
        self.assertEqual(choice['shapeParams']['Data']['preset'], 'small')
        self.assertEqual(choice['shapeParams']['Data']['activationYawLimit'], 360)
        self.assertEqual(choice['lookAtParams']['Data']['slotName']['$value'], '(Root)')
        self.assertEqual(choice['mappinParams']['Data']['locationType'], 'Interaction')
        self.assertEqual(choice['options'][0]['type']['properties'], 257)
        for field in ('shapeParams', 'lookAtParams', 'mappinParams'):
            saved = choice[field]
            choice[field] = None
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, 'requires '+field):
                race_builder.validate_activation_graph(scene)
            choice[field] = saved

    def test_scene_events_omit_the_unnamed_event_type_enum(self):
        _, binding, docs, _ = self.compile()
        scene = docs[binding['activation_scene']]
        events = [event['Data'] for node in scene['Data']['RootChunk']['sceneGraph']['Data']['graph']
                  for event in node['Data'].get('events', [])]
        self.assertEqual(len(events), 4)
        self.assertTrue(all('type' not in event for event in events))
        events[0]['type'] = '0'
        with self.assertRaisesRegex(ValueError, 'unnamed scnEventType'):
            race_builder.validate_activation_graph(scene)

    def test_activation_player_occupies_slot_zero_and_all_references_match(self):
        _, binding, docs, _ = self.compile()
        scene = docs[binding['activation_scene']]
        root = scene['Data']['RootChunk']
        self.assertEqual(root['actors'], [])
        self.assertEqual([actor['actorId']['id'] for actor in root['playerActors']], [0])
        actor_refs = {item['id'] for item in race_builder.walk(root)
                      if item.get('$type') == 'scnActorId' and item['id'] != 4294967295}
        performer_refs = {item['id'] for item in race_builder.walk(root)
                          if item.get('$type') == 'scnPerformerId' and item['id'] != 4294967040}
        self.assertEqual(actor_refs, {0})
        self.assertEqual(performer_refs, {1})
        race_builder.validate_activation_graph(scene)

    def test_activation_rejects_sparse_actor_table_from_crash(self):
        _, binding, docs, _ = self.compile()
        scene = docs[binding['activation_scene']]
        scene['Data']['RootChunk']['playerActors'][0]['actorId']['id'] = 1
        with self.assertRaisesRegex(ValueError, 'contiguous table slots starting at zero'):
            race_builder.validate_activation_graph(scene)

    def test_activation_rejects_stale_performer_after_actor_renumbering(self):
        _, binding, docs, _ = self.compile()
        scene = docs[binding['activation_scene']]
        for item in race_builder.walk(scene):
            if item.get('$type') == 'scnGameplayTransitionEvent':
                item['performer']['id'] = 257
        with self.assertRaisesRegex(ValueError, 'missing performer 257'):
            race_builder.validate_activation_graph(scene)

    def test_activation_rejects_deleted_start_and_end_nodes(self):
        _, binding, docs, _ = self.compile()
        scene = docs[binding['activation_scene']]
        graph = scene['Data']['RootChunk']['sceneGraph']['Data']
        for collection, removed in [('startNodes', 1), ('endNodes', 10)]:
            with self.subTest(collection=collection):
                graph[collection].append({'$type': 'scnNodeId', 'id': removed})
                with self.assertRaisesRegex(ValueError, f'{collection} references missing node {removed}'):
                    race_builder.validate_activation_graph(scene)
                graph[collection].pop()

    def test_checkpoint_visual_devices_cannot_write_the_stock_hud_counter(self):
        _,binding,docs,_ = self.compile()
        device = docs[binding['checkpoint_entity']]
        facts = [d['factName']['$value'] for d in race_builder.walk(device) if d.get('$type')=='SFactOperationData']
        self.assertTrue(facts)
        self.assertEqual(set(facts),{'race_test_visual_crossed'})
        sector = next(d['Data']['RootChunk'] for d in docs.values() if d['Data']['RootChunk'].get('category')=='Quest')
        nodes = [n['Data'] for n in sector['nodes'] if n['Data'].get('entityTemplate',{}).get('DepotPath',{}).get('$value')==binding['checkpoint_entity']]
        self.assertEqual(len(nodes),2)
        self.assertTrue(all(n['isVisibleInGame']==0 for n in nodes))

    def test_checkpoint_readback_preserves_package_outline_geometry(self):
        from cr2w_validation import compare_documents
        _,binding,docs,_ = self.compile()
        original = docs[binding['checkpoint_entity']]
        normalized = race_builder.checkpoint_comparison(original)
        self.assertTrue(compare_documents(normalized,normalized,schema={}).ok)
        changed = copy.deepcopy(original)
        outline = next(v for v in race_builder.walk(changed) if v.get('$type')=='AreaShapeOutline')
        outline['height'] += 1
        self.assertFalse(compare_documents(normalized,race_builder.checkpoint_comparison(changed),schema={}).ok)

    def test_off_course_threshold_uses_integer_native_fact_values(self):
        self.config['off_course'] = {'action':'fail','distance_m':50.5,'grace_seconds':2}
        _,_,docs,_ = self.compile()
        thresholds = [v['value'] for d in docs.values() for v in race_builder.walk(d)
                      if v.get('$type')=='questVarComparison_ConditionType'
                      and v.get('factName')=='RacePlayerDistanceFromSpline']
        self.assertEqual(thresholds,[51,51])
        self.assertTrue(all(type(v) is int for v in thresholds))

    def test_each_driver_and_vehicle_has_a_named_readiness_gate_and_driver_assignment(self):
        _,_,docs,_ = self.compile()
        attempt = next(d for path,d in docs.items() if path.endswith('_attempt.questphase'))
        values = list(race_builder.walk(attempt))
        vehicles = [v for v in values if v.get('$type')=='questVehicleSpawned_ConditionType']
        self.assertEqual(vehicles[0]['vehicleRef']['names'][0]['$value'],'one_vehicle')
        drivers = [v for v in values if v.get('$type')=='questCharacterSpawned_ConditionType']
        self.assertEqual(drivers[0]['objectRef']['names'][0]['$value'],'one_driver')
        mounts = [v for v in values if v.get('$type')=='questAssignCharacter_NodeType']
        self.assertEqual(mounts[0]['slotName']['$value'],'seat_front_left')
        self.assertTrue(any(v.get('$type')=='questVehicleCommandParams' and v.get('type')=='Racing' for v in values))

    def test_checkpoint_waits_require_exit_then_entry_for_player_and_opponent(self):
        _,binding,docs,_ = self.compile()
        attempt = next(d for path,d in docs.items() if path.endswith('_attempt.questphase'))
        for ref in binding['checkpoints']:
            waits = [v for v in race_builder.walk(attempt) if v.get('$type')=='questTriggerCondition' and v['triggerAreaRef']['$value']==ref]
            self.assertEqual(len(waits),4)
            self.assertEqual(sorted(w['type'] for w in waits),['IsInside','IsInside','IsOutside','IsOutside'])
            self.assertEqual(sum(w['isPlayerActivator']==0 for w in waits),2)
        # Every terminal route owns permanent cuts, including timers and commands.
        cuts = [v for v in race_builder.walk(attempt) if v.get('$type')=='questCutControlNodeDefinition']
        self.assertGreaterEqual(len(cuts),6)
        self.assertGreaterEqual(sum(v['permanent']==1 for v in cuts),6)
        self.assertEqual(sum(v['permanent']==0 for v in cuts),1)

    def test_only_success_route_grants_reward(self):
        _,_,docs,_ = self.compile()
        graph = self.phase(docs,'root')
        nodes = graph.node_data_by_handle
        edges = list(graph.edges_by_handle.values())
        calls = [key for key,node in nodes.items() if node['$type']=='questPhaseNodeDefinition']
        self.assertEqual(len(calls),1)
        def reachable(socket):
            starts = [edge.destination_node for edge in edges if edge.source_node==calls[0] and edge.source_socket_name==socket]
            visited=set()
            while starts:
                key=starts.pop()
                if key in visited: continue
                visited.add(key)
                starts.extend(e.destination_node for e in edges if e.source_node==key and e.source_socket_name!='CutSource')
            return [nodes[key] for key in visited]
        def has_reward(nodes):
            return any(x.get('$type')=='questAddRemoveItem_NodeTypeParams' for n in nodes for x in race_builder.walk(n))
        self.assertTrue(has_reward(reachable('Success')))
        self.assertFalse(has_reward(reachable('Failure')))
        self.assertFalse(has_reward(reachable('Aborted')))

    def test_finish_departure_cleanup_and_courier_spawn(self):
        _,binding,docs,_ = self.compile()
        graph = self.phase(docs,'lifecycle')
        nodes = graph.node_data_by_handle
        edges = [e for e in graph.edges_by_handle.values()
                 if e.destination_socket_name!='CutDestination' and e.source_socket_name!='CutSource']
        values = [v for node in nodes.values() for v in race_builder.walk(node)]
        distances = [v for v in values if v.get('$type')=='questObjectDistance']
        self.assertTrue(distances)
        self.assertTrue(all(v['entityRef']['Data'].get('refLocalPlayer')==1 for v in distances))

        def contains(node, kind, **fields):
            return any(v.get('$type')==kind and all(v.get(k)==value for k,value in fields.items())
                       for v in race_builder.walk(node))

        def reachable(starts, skip_joins=False):
            visited=set()
            while starts:
                key=starts.pop()
                if key in visited: continue
                node=nodes[key]
                if skip_joins and 'And' in node['$type']: continue
                if skip_joins and any(v.get('$type')=='questVarComparison_ConditionType'
                        and v.get('factName','').endswith(('_reward_taken','_courier_finished'))
                        for v in race_builder.walk(node)): continue
                visited.add(key)
                starts.extend(e.destination_node for e in edges if e.source_node==key)
            return visited

        exits=[key for key,node in nodes.items() if any(v.get('$type')=='questTriggerCondition'
               and v['triggerAreaRef']['$value']==binding['end_area'] and v['type']=='IsOutside'
               for v in race_builder.walk(node))]
        self.assertTrue(exits)
        # Leaving must reach actual crew deactivation without a reward gate or AND join.
        for exit_node in exits:
            reached=reachable([exit_node],skip_joins=True)
            self.assertTrue(any(contains(nodes[key],'questCommunityTemplate_NodeType',action='Deactivate')
                and any(v.get('$value')==binding['community'] for v in race_builder.walk(nodes[key]))
                for key in reached))
            self.assertTrue(any(nodes[key]['$type']=='questCutControlNodeDefinition' for key in reached))

        self.assertNotIn('courier_arrival',binding)
        self.assertFalse(any('courier_arrival_clearance' in str(v) for v in values))
        spawned=[key for key in nodes if contains(nodes[key],'questSpawner_NodeType',action='Activate')]
        self.assertEqual(len(spawned),2)

    def test_invalid_inputs_fail_before_writing_resources(self):
        for mutate in [lambda c:c.update(winning_places=0),lambda c:c.update(laps=2),
                       lambda c:c['entrants'].append(copy.deepcopy(c['entrants'][0])),
                       lambda c:c['entrants'][0].update(grid=5),
                       lambda c:c.update(timeout_seconds=float('nan'))]:
            original=copy.deepcopy(self.config)
            mutate(self.config)
            with self.assertRaises((ValueError,RuntimeError)):
                self.compile()
            self.config=original
        self.survey['world_spec']['block_path']='mod\\unowned\\world\\all.streamingblock'
        with self.assertRaises((ValueError,SystemExit)):
            self.compile()

    def test_raw_build_and_conversion_failure_preserve_the_previous_preview(self):
        path=self.spec()
        output=self.root/'preview'
        receipt=race_builder.build(path,output_root=output)
        self.assertFalse(receipt['runtime_verified'])
        before={p.relative_to(output):p.read_bytes() for p in output.rglob('*') if p.is_file()}
        self.assertEqual(len(list((output/'source/raw').rglob('*.json'))),9)
        self.assertEqual(list((output/'source/resources').rglob('*.reds')),[])
        self.assertEqual(receipt['dependencies'],['ArchiveXL'])
        with patch('race_builder.convert_resources',side_effect=RuntimeError('conversion failed')):
            with self.assertRaisesRegex(RuntimeError,'conversion failed'):
                race_builder.build(path,output_root=output,deserialize=True)
        after={p.relative_to(output):p.read_bytes() for p in output.rglob('*') if p.is_file()}
        self.assertEqual(before,after)

    def test_preview_may_not_write_to_source_and_survey_binding_tampering_is_rejected(self):
        with self.assertRaisesRegex(ValueError,'outside.*source tree'):
            race_builder.build(self.spec(),output_root=self.project/'source/raw/race_preview')
        self.survey['bindings'][0]['ref']='#does_not_exist'
        # Spline bindings come from the world spline, but a missing grid is fatal.
        grid=next(x for x in self.survey['bindings'] if x['role']=='start_grid')
        grid['ref']='#not_in_world'
        with self.assertRaises((ValueError,KeyError)):
            self.compile()

    def test_conversion_calls_ghostline_red_without_template_or_wolvenkit(self):
        spec = self.spec()
        output = self.root/'preview'
        receipt = race_builder.build(spec,output_root=output)
        self.assertEqual(receipt['serializer'],'ghostline-red')
        def write(raw,binary,**kwargs):
            self.assertEqual(set(kwargs),{'red_cli','schema'})
            binary.parent.mkdir(parents=True,exist_ok=True)
            binary.write_bytes(b'CR2Wtest-routing-only')
        def read(binary,decoded,**kwargs):
            # The staged raw input and output share the same depot-relative path.
            staging=next(p for p in binary.parents if (p/'source/raw').is_dir())
            relative=binary.relative_to(staging/'source/archive')
            raw=staging/'source/raw'/Path(str(relative)+'.json')
            decoded.write_bytes(raw.read_bytes())
        schema=self.root/'schema.json'
        schema.write_text('{}')
        with patch('race_builder.ensure_schema',return_value=schema), \
             patch('race_builder.red_deserialize',side_effect=write) as writer, \
             patch('race_builder.red_serialize',side_effect=read) as reader:
            race_builder.build(spec,output_root=output,deserialize=True)
        self.assertEqual(writer.call_count,9)
        self.assertEqual(reader.call_count,9)
        self.assertEqual(len(list((output/'source/archive').rglob('*.*'))),9)

    def test_workspot_action_gates_attempt_and_proximity_cannot_start_racing(self):
        _,binding,docs,_ = self.compile()
        scene = docs[binding['activation_scene']]['Data']['RootChunk']
        from cr2w_validation import compare_documents
        normalized = race_builder.activation_comparison(docs[binding['activation_scene']])
        self.assertTrue(compare_documents(normalized,normalized,schema={}).ok)
        from scene_validation import validate_reference_tables
        self.assertEqual(validate_reference_tables(scene),[])
        nodes = {n['Data']['nodeId']['id']:n['Data'] for n in scene['sceneGraph']['Data']['graph']}
        self.assertEqual(nodes[119]['$type'],'scnChoiceNode')
        self.assertEqual(nodes[121]['$type'],'scnSectionNode')
        self.assertEqual(nodes[154]['$type'],'scnSectionNode')
        use = nodes[125]['questNode']['Data']
        self.assertEqual(use['$type'],'questUseWorkspotNodeDefinition')
        self.assertTrue(use['paramsV1']['Data']['isPlayer'])
        self.assertEqual(nodes[125]['osockMappings'][1]['$value'],'Work Started')
        self.assertEqual(nodes[125]['outputSockets'][1]['destinations'][0]['nodeId']['id'],151)
        self.assertEqual(nodes[151]['$type'],'scnChoiceNode')
        self.assertEqual(nodes[158]['questNode']['Data']['paramsV1']['Data']['function'],'StopWorkspot')
        self.assertEqual(use['paramsV1']['Data']['entryId']['id'], 2)
        self.assertEqual(scene['workspotInstances'][0]['originMarker']['isMounted'], 0)
        self.assertTrue(scene['workspots'][0]['Data']['workspotResource']['DepotPath']['$value'].endswith('player__stand_ground__idle__01.workspot'))
        self.assertFalse(any(event['Data']['$type'] == 'scnPlaySkAnimEvent' for node in (nodes[121], nodes[154]) for event in node['events']))
        graph = self.phase(docs,'root')
        activation = next(k for k,v in graph.node_data_by_handle.items() if v['$type']=='questSceneNodeDefinition')
        edges = list(graph.edges_by_handle.values())
        exits = [e for e in edges if e.source_node==activation]
        self.assertTrue(exits)
        self.assertTrue(all(e.source_socket_name=='race_accepted' for e in exits))
        self.assertFalse(any(v.get('$type')=='questStartRace_NodeType' for v in race_builder.walk(graph.data)))

    def test_scout_build_adapter_produces_the_same_native_preview_without_scripts(self):
        receipt = self.races.build(self.race,self.config['entrants'],output_root=self.root/'scout-preview')
        target=Path(receipt['output_root'])
        self.assertEqual(len(list((target/'source/raw').rglob('*.json'))),9)
        self.assertEqual(list(target.rglob('*.reds')),[])
        self.assertEqual(receipt['dependencies'],['ArchiveXL'])


if __name__=='__main__':
    unittest.main()
