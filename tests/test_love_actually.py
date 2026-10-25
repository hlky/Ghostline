"""Placement import must not silently accept partial or invalid world captures."""
import copy
import importlib.util
import json
import math
import shutil
import subprocess
import tempfile
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / 'projects/ghostline/quests/gq004/implementation'
sys.path.insert(0, str(ROOT / 'tools'))
spec = importlib.util.spec_from_file_location('love_actually_scout', HERE / 'scout.py')
scout = importlib.util.module_from_spec(spec)
spec.loader.exec_module(scout)
world_spec = importlib.util.spec_from_file_location('love_actually_world', HERE / 'build_world.py')
world_builder = importlib.util.module_from_spec(world_spec)
world_spec.loader.exec_module(world_builder)
sys.path.insert(0, str(HERE))
import phases
from compile_native import device_values, stage_native_inputs
from explore_questphase import QuestphaseExplorer


class NativeRuntimeTests(unittest.TestCase):
    def test_heartbreaker_custom_icon_has_native_inventory_and_scanner_bindings(self):
        from build_icon import render
        from package_manifest import read_tweak_dependencies
        image=render()
        self.assertEqual(image.size,(256,256))
        self.assertEqual(image.getpixel((0,0))[3],0)
        self.assertGreater(image.getchannel('A').getbbox()[2],140)
        records=read_tweak_dependencies(ROOT/'projects/ghostline/source/resources/r6/tweaks/ghostline/z_gq004_heartbreaker_icon.yaml')
        self.assertEqual(records['Items.GhostlineLoveHeartbreaker']['icon'],'UIIcon.ItemIcon')
        self.assertEqual(records['ChoiceCaptionParts.GhostlineLoveHeartbreaker']['texturePartID'],'UIIcon.GhostlineVelvetCrashGlyph')
        self.assertEqual(records['UIIcon.GhostlineVelvetCrashGlyph']['atlasPartName'],'velvet_crash')
        self.assertEqual(records['GhostlineVelvetCrash.Interaction']['captionIcon'],'ChoiceCaptionParts.GhostlineLoveHeartbreaker')
        self.assertEqual(records['UIIcon.GhostlineLoveHeartbreaker']['atlasPartName'],'heartbreaker')
        self.assertIn('EquipmentGLP.BlindProgram',records['Items.GhostlineLoveHeartbreaker']['OnAttach'])
        self.assertEqual(records['GhostlineLove.HeartbreakerTooltip']['UIData'],'GhostlineLove.HeartbreakerTooltipUI')
        self.assertEqual(records['GhostlineLove.HeartbreakerTooltipUI']['localizedDescription'],'LocKey("gl_gq004_heartbreaker_effect")')
        self.assertEqual(records['GhostlineVelvetCrash.Interaction']['description'],'gl_gq004_heartbreaker_effect')

    def test_socket_mappins_follow_mounted_devices_without_new_capture_targets(self):
        world = json.loads(scout.WORLD.read_text())
        quest = json.loads((HERE/'quest.json').read_text(encoding='utf-8'))
        markers = {m['ref']:m for m in world['markers']}
        devices = {d['ref']:d for d in world['devices']}
        for name in ('recover','upload'):
            marker = markers['#gq004_mp_'+name]
            self.assertEqual(marker['position'], devices[marker['derived_from']]['position'])
            self.assertEqual(quest['composition']['objectives'][name]['mappins']['target']['ref'], marker['ref'])
        log = json.loads((HERE/'world/love-actually.locations.json').read_text())
        log['captures']['#gq004_ap_upload']['x'] += 2
        updated = scout.apply_captures(world, log)
        marker = next(m for m in updated['markers'] if m['ref']=='#gq004_mp_upload')
        device = next(d for d in updated['devices'] if d['ref']==marker['derived_from'])
        self.assertEqual(marker['position'],device['position'])
        self.assertEqual(len(scout.targets(updated)),16)

    def test_root_retains_velvet_until_player_leaves_after_debrief(self):
        from quest_compiler import load_spec,validate_handle_graph,validate_no_forward_handle_refs
        spec,_ = load_spec(HERE/'quest.json')
        document = phases.root(spec,Path('root.questphase'))
        validate_handle_graph(document,context='retained velvet')
        validate_no_forward_handle_refs(document,context='retained velvet')
        explorer=self.explorer(document)
        ids={h:int(n.quest_id) for h,n in explorer.nodes_by_handle.items()}
        edges={(ids[e.source_node],ids[e.destination_node]) for e in explorer.edges_by_handle.values()}
        self.assertTrue({(26,40),(40,41),(41,1)} <= edges)
        self.assertNotIn((26,1),edges)
        self.assertIn('IsOutside',json.dumps(document))

    def test_departure_during_upload_dialogue_or_before_load_is_not_missed(self):
        from quest_compiler import load_spec, validate_handle_graph, validate_no_forward_handle_refs
        spec, diagnostics = load_spec(HERE / 'quest.json')
        self.assertFalse([d for d in diagnostics if d.level == 'error'])
        stage = next(s for s in spec.stages if s.id == 'leave')
        document = phases.leave(stage, Path('leave.questphase'))
        validate_handle_graph(document, context='leave')
        validate_no_forward_handle_refs(document, context='leave')
        text = json.dumps(document)
        self.assertNotIn('"type": "Exited"', text)
        self.assertIn('"type": "IsOutside"', text)
        explorer = self.explorer(document)
        data = {int(n.quest_id): explorer.node_data_by_handle[h] for h,n in explorer.nodes_by_handle.items()}
        self.assertEqual(data[12]['condition']['Data']['triggerAreaRef']['$value'], '#gq004_tr_cleanup')
        ids = {h: int(n.quest_id) for h,n in explorer.nodes_by_handle.items()}
        edges = {(ids[e.source_node], ids[e.destination_node]) for e in explorer.edges_by_handle.values()}
        # The outside gate still precedes objective success, left fact and cleanup.
        self.assertTrue({(11,12), (12,13), (13,14), (14,15), (15,1)} <= edges)

    def test_compiler_localization_survives_authored_input_staging(self):
        with tempfile.TemporaryDirectory() as folder:
            source, target = Path(folder)/'source', Path(folder)/'target'
            relative = Path('localization/en-us/onscreens/gq004.json.json')
            for base, text in ((source,'stale'), (target,'fresh read objective strings')):
                (base/relative).parent.mkdir(parents=True)
                (base/relative).write_text(text, encoding='utf-8')
            device = source/'devices/recover.ent.json'
            device.parent.mkdir(); device.write_text('authored', encoding='utf-8')
            stage_native_inputs(source, target)
            self.assertEqual((target/relative).read_text(), 'fresh read objective strings')
            self.assertEqual((target/'devices/recover.ent.json').read_text(), 'authored')

    def test_finish_precedes_optional_phone_and_queries_current_inventory(self):
        from quest_compiler import validate_handle_graph, validate_no_forward_handle_refs
        document = phases.finish_and_epilogue(Path('finish.questphase'))
        validate_handle_graph(document, context='finish')
        validate_no_forward_handle_refs(document, context='finish')
        explorer = self.explorer(document)
        data = {int(n.quest_id): explorer.node_data_by_handle[h] for h,n in explorer.nodes_by_handle.items()}
        self.assertEqual(data[12]['$type'], 'questConditionNodeDefinition')
        self.assertEqual(data[16]['type']['Data']['$type'], 'questJournalQuestEntry_NodeType')
        self.assertEqual(data[18]['condition']['Data']['type']['Data']['seconds'], 45)
        self.assertEqual(data[11]['condition']['Data']['type']['Data']['$type'], 'questTickDelay_ConditionType')
        self.assertEqual(data[11]['condition']['Data']['type']['Data']['tickCount'],2)
        self.assertNotIn('questTriggerCondition', json.dumps(document))
        self.assertIn('gq004_completed', json.dumps(data[17]))
        tweak = (ROOT/'projects/ghostline/source/resources/r6/tweaks/ghostline/gq004_love_actually.yaml').read_text()
        self.assertIn('quality: Quality.Legendary', tweak)
        self.assertIn('statType: BaseStats.IsItemIconic', tweak)

    def test_reward_is_inventory_verified_and_completed_save_repair_is_once_only(self):
        from quest_compiler import validate_handle_graph, validate_no_forward_handle_refs
        document = phases.reward_repair(Path('repair.questphase'))
        validate_handle_graph(document, context='repair')
        validate_no_forward_handle_refs(document, context='repair')
        explorer = self.explorer(document)
        ids = {h: int(n.quest_id) for h, n in explorer.nodes_by_handle.items()}
        edges = {(ids[e.source_node], ids[e.destination_node]) for e in explorer.edges_by_handle.values()}
        self.assertTrue({(10,11), (11,12), (12,1), (12,13), (13,16), (13,14),
                         (14,15), (15,16), (16,17), (17,1)} <= edges)
        data = {ids[h]: row for h, row in explorer.node_data_by_handle.items()}
        self.assertEqual(data[12]['condition']['Data']['type']['Data']['factName'],
                         'gq004_reward_delivery_verified')
        self.assertIn('questInventory_ConditionType', json.dumps(data[15]))
        self.assertIn('Items.GhostlineLoveHeartbreaker', json.dumps(data[15]))
        tweak = (ROOT / 'projects/ghostline/source/resources/r6/tweaks/ghostline/gq004_love_actually.yaml').read_text()
        self.assertNotIn('$base: Items.GhostlineVelvetCrashProtocol', tweak)
        self.assertIn('$base: Items.BlindProgram', tweak)

    def test_shard_comments_wait_for_read_and_epilogue_waits_for_departure(self):
        from quest_compiler import compile_manifest_artifacts
        artifacts = compile_manifest_artifacts(HERE / 'quest.json', Path('raw'), Path('archive'),
            allow_planned=True, stage_overrides={'recover': phases.transfer, 'return': phases.meeting},
            root_override=phases.root)
        documents = {a.archive_path.name: a.document for a in artifacts}
        explorer = self.explorer(documents['gq004_recover.questphase'])
        ids = {h: int(n.quest_id) for h, n in explorer.nodes_by_handle.items()}
        edges = {(ids[e.source_node], ids[e.destination_node]) for e in explorer.edges_by_handle.values()}
        self.assertTrue({(52,60), (60,61), (61,62), (62,63), (63,82), (82,83), (83,65), (65,66),
                         (66,67), (67,68), (68,84), (84,85), (85,70), (70,71), (71,72), (72,1)} <= edges)
        data = {ids[h]: row for h, row in explorer.node_data_by_handle.items()}
        self.assertIn('Items.GhostlineLoveSales',json.dumps(data[31]))
        self.assertIn('Items.GhostlineLoveArchive',json.dumps(data[83]))
        self.assertIn('Items.GhostlineLoveRevocation',json.dumps(data[85]))
        for number, shard in ((61,'sales'), (66,'archive'), (71,'revocation')):
            kind = data[number]['condition']['Data']['type']['Data']
            self.assertEqual(kind['$type'], 'questJournalEntryVisited_ConditionType')
            self.assertEqual(kind['visited'], 1)
            self.assertTrue(kind['path']['Data']['realPath'].endswith('/'+shard))
        text = json.dumps(documents['archive'])
        self.assertNotIn('gq004_ending.questphase', text)
        self.assertIn('gq004_reward_delivery_verified', json.dumps(phases.finish_and_epilogue(Path('finish'))))

    def test_upload_label_and_success_bar_are_native_completion(self):
        document = phases.attempt('#upload', Path('attempt.questphase'), 'Velvet Crash')
        explorer = self.explorer(document)
        data = {int(n.quest_id): explorer.node_data_by_handle[h] for h,n in explorer.nodes_by_handle.items()}
        self.assertEqual(data[11]['type']['Data']['text']['value'], 'Velvet Crash')
        self.assertEqual(data[11]['type']['Data']['show'], 1)
        self.assertEqual(data[15]['type']['Data']['show'], 0)
        self.assertEqual(data[14]['condition']['Data']['type']['Data']['tickCount'], 2)

    def test_meetings_and_operation_accept_players_already_inside_after_fast_travel(self):
        from quest_compiler import compile_manifest_artifacts
        artifacts = compile_manifest_artifacts(HERE / 'quest.json', Path('raw'), Path('archive'),
            allow_planned=True, stage_overrides={'meet': phases.meeting, 'return': phases.meeting,
                                               'reach': phases.reach}, root_override=phases.root)
        for artifact in artifacts:
            if artifact.archive_path.name not in ('gq004_meet.questphase', 'gq004_return.questphase', 'gq004_reach.questphase'):
                continue
            text = json.dumps(artifact.document)
            self.assertNotIn('"type": "Entered"', text)
            self.assertIn('"type": "IsInside"', text)
            if artifact.archive_path.name == 'gq004_reach.questphase': continue
            self.assertIn('"state": "Invulnerable"', text)
            self.assertIn('"$value": "friendly"', text)
            explorer = self.explorer(artifact.document)
            ids = {h: int(n.quest_id) for h, n in explorer.nodes_by_handle.items()}
            edges = {(ids[e.source_node], ids[e.destination_node]) for e in explorer.edges_by_handle.values()}
            self.assertIn((14, 24), edges)  # Spawn readiness precedes protection.
            self.assertIn((24, 25), edges)
            self.assertIn((25, 15), edges)
            if artifact.archive_path.name == 'gq004_meet.questphase':
                self.assertTrue({(16,27),(29,27),(27,26)} <= edges)
            else:
                self.assertIn((16,26),edges)
            self.assertIn((26, 15), edges)
            self.assertNotIn(17, ids.values())
            self.assertIn('#gq004_tr_engage', json.dumps(explorer.node_data_by_handle[next(h for h in ids if ids[h] == 26)]))
        text = (ROOT / 'projects/ghostline/source/resources/r6/tweaks/ghostline/character_velvet.yaml').read_text()
        self.assertIn('baseAttitudeGroup: friendly', text)
        self.assertIn('!append Invulnerable', text)

    def test_transfer_devices_have_no_active_hacking_gate_or_old_saved_identity(self):
        world = json.loads(scout.WORLD.read_text())
        quest = json.loads((HERE / 'quest.json').read_text())
        devices = {world['prefab_root'] + '/' + d['ref']: d for d in world['devices']}
        project = ROOT / 'projects/ghostline'
        def typed(value, kind):
            if isinstance(value, dict):
                if value.get('$type') == kind: yield value
                for child in value.values(): yield from typed(child, kind)
            elif isinstance(value, list):
                for child in value: yield from typed(child, kind)
        for stage in quest['stages']:
            if stage['id'] not in ('recover', 'upload'): continue
            self.assertEqual(stage['completion_function'], 'IsPersonalLinkConnected')
            device = devices[stage['device']]
            self.assertNotEqual(device['ref'], device['capture_ref'])
            raw = project / 'source/raw' / (device['entity_template'].replace('\\', '/') + '.json')
            document = device_values(json.loads(raw.read_text()))
            checks = list(typed(document, 'HackingSkillCheck'))
            self.assertTrue(checks)
            for check in checks:
                self.assertEqual(check['difficulty'], 'NONE')
                self.assertEqual(check['isActive'], 0)
            for controller in typed(document, 'AccessPointControllerPS'):
                self.assertEqual(controller['shouldSkipNetrunnerMinigame'], 1)
                self.assertEqual(controller['personalLinkForced'], 1)

    def test_meeting_retains_velvet_and_device_actions_use_registered_controller(self):
        from quest_compiler import compile_manifest_artifacts
        artifacts = compile_manifest_artifacts(HERE / 'quest.json', Path('raw'), Path('archive'),
            allow_planned=True, stage_overrides={'meet': phases.meeting, 'return': phases.meeting,
                'reach': phases.reach, 'recover': phases.transfer, 'upload': phases.transfer},
            root_override=phases.root)
        documents = {a.archive_path.name: a.document for a in artifacts}
        self.assertNotIn('Deactivate', json.dumps(documents['gq004_meet.questphase']))
        self.assertIn('Deactivate', json.dumps(documents['gq004_reach.questphase']))
        for name in ('recover', 'upload'):
            document = documents[f'gq004_{name}.questphase']
            text = json.dumps(document)
            self.assertNotIn('ScriptableDeviceComponentPS', text)
            self.assertIn('AccessPointControllerPS', text)
            self.assertIn('ForceON', text)
            self.assertIn('ForceDisabled', text)

    def test_intro_waits_until_three_metres_and_skin_textures_exist(self):
        world = json.loads(scout.WORLD.read_text())
        awareness = next(t for t in world['triggers'] if t['ref'] == '#gq004_tr_awareness')
        self.assertEqual(awareness['outline']['radius'], 3)
        project = ROOT / 'projects/ghostline'
        body = project / 'source/raw/mod/ghostline/characters/velvet/body/t0_000_pwa_base__full.mesh.json'
        text = body.read_text()
        self.assertNotIn('tutorial', text)
        textures = project / 'source/archive/mod/ghostline/characters/velvet/body/textures'
        self.assertEqual(len(list(textures.glob('*.xbm'))), 3)


    def test_socket_plate_normal_matches_captured_player_facing(self):
        world = json.loads(scout.WORLD.read_text())
        log = json.loads((HERE / 'world/love-actually.locations.json').read_text())
        updated = scout.apply_captures(world, log)
        for device in updated['devices']:
            capture = log['captures'][device.get('capture_ref', device['ref'])]
            angle = math.radians(device['yaw'])
            mount = device.get('wall_mount')
            if mount:
                nx,ny=mount['normal'];px,py=mount['surface_point']
                self.assertAlmostEqual(math.cos(angle),nx,places=6)
                self.assertAlmostEqual(math.sin(angle),ny,places=6)
                distance=(device['position']['x']-px)*nx+(device['position']['y']-py)*ny
                self.assertAlmostEqual(distance-mount['rear_offset']+mount.get('render_surface_inset',0),mount['clearance'],places=6)
                self.assertGreater(math.cos(angle)*capture['forward_x']+math.sin(angle)*capture['forward_y'],.99)
            else:
                self.assertAlmostEqual(math.cos(angle), capture['forward_x'], places=5)
                self.assertAlmostEqual(math.sin(angle), capture['forward_y'], places=5)
        # Reimporting captures never applies the mounting offset twice.
        self.assertEqual(updated['devices'], scout.apply_captures(updated, log)['devices'])

    def explorer(self, document):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'test.json'
            path.write_text(json.dumps(document), encoding='utf-8')
            return QuestphaseExplorer(path)

    def test_transfer_retry_terminates_pending_timer_and_success_requires_delay(self):
        document = phases.attempt('#gq004_ap_relay', Path('attempt.questphase'))
        from quest_compiler import validate_handle_graph, validate_no_forward_handle_refs
        validate_handle_graph(document, context='attempt')
        validate_no_forward_handle_refs(document, context='attempt')
        explorer = self.explorer(document)
        ids = {h: int(node.quest_id) for h, node in explorer.nodes_by_handle.items()}
        edges = {(ids[e.source_node], ids[e.destination_node]) for e in explorer.edges_by_handle.values()}
        self.assertIn((11, 12), edges)  # Progress starts a fresh timer and disconnect listener.
        self.assertIn((11, 13), edges)
        self.assertIn((13, 15), edges)
        self.assertIn((15, 2), edges)
        self.assertIn((12, 14), edges)
        self.assertIn((14, 1), edges)
        for h, node in explorer.nodes_by_handle.items():
            if ids[h] in (1, 2):
                self.assertEqual(explorer.node_data_by_handle[h]['type'], 'Terminating')

    def test_device_shared_persistent_state_aliases_cannot_silently_split(self):
        shared = {'Data': {'RootChunk': {'$type': 'entEntityTemplate',
            'a': {'HandleId': '0', 'Data': {'$type': 'AccessPointControllerPS', 'hasPersonalLinkSlot': 1}},
            'b': {'HandleRefId': '0'}}}}
        split = copy.deepcopy(shared)
        split['Data']['RootChunk']['b'] = {'HandleId': '1', 'Data': copy.deepcopy(shared['Data']['RootChunk']['a']['Data'])}
        report = world_builder.verify_document(device_values(shared), device_values(split), {})
        self.assertFalse(report['ok'])

    def test_native_field_scenes_route_only_velvet_through_phone_audio(self):
        import generate_scene
        spec = json.loads((HERE / 'scenes/gq004_02_upload.scene-spec.json').read_text())
        scene = generate_scene.build_scene(spec)
        self.assertEqual(generate_scene.validate_scene(scene, spec), [])
        root = scene['Data']['RootChunk']
        lines = {row['itemId']['id']: row for row in root['screenplayStore']['lines']}
        events = [event['Data'] for node in root['sceneGraph']['Data']['graph']
                  for event in node['Data'].get('events', []) if event['Data'].get('$type') == 'scnDialogLineEvent']
        self.assertEqual(len(events), 1)  # Naming exchange belongs to its connection-triggered scene.
        self.assertEqual(root['actors'][0]['spawnDespawnParams']['spawnMarkerNodeRef']['$value'], '#holocall_marker')
        self.assertEqual(root['actors'][0]['spawnDespawnParams']['validateSpawnPostion'], 0)
        self.assertEqual(root['actors'][0]['voicetagId']['id'], '5506207259407814236')
        for event in events:
            line = lines[event['screenplayLineId']['id']]
            self.assertEqual(event['voParams']['isHolocallSpeaker'], int(line['speaker']['id'] == 0))

    def test_upload_naming_starts_on_connection_and_retires_with_attempt(self):
        from quest_compiler import validate_no_forward_handle_refs
        document = phases.attempt('#upload', Path('attempt.questphase'), 'Velvet Crash')
        validate_no_forward_handle_refs(document, context='upload attempt')
        explorer = self.explorer(document)
        ids = {h: int(n.quest_id) for h, n in explorer.nodes_by_handle.items()}
        edges = {(ids[e.source_node], ids[e.destination_node]) for e in explorer.edges_by_handle.values()}
        self.assertTrue({(10,11), (11,16), (11,12), (12,17), (16,17), (17,14), (14,1)} <= edges)
        data = {ids[h]: row for h,row in explorer.node_data_by_handle.items()}
        self.assertIn('gq004_02_brand.scene', json.dumps(data[16]))
        self.assertEqual(data[2]['type'], 'Terminating')
        spec = json.loads((HERE / 'scenes/gq004_02_brand.scene-spec.json').read_text())
        self.assertEqual(spec['spoken_line_order'], ['gq004_02_v_brand', 'gq004_02_velvet_brand'])

    def test_success_waits_for_remote_performer_before_time_zero_line(self):
        import generate_scene
        spec=json.loads((HERE/'scenes/gq004_02_success.scene-spec.json').read_text())
        scene=generate_scene.build_scene(spec)
        self.assertEqual(generate_scene.validate_scene(scene,spec),[])
        self.assertEqual(spec['start_node']['on_start'],[{'node_id':4,'input_name':0,'input_ordinal':1}])
        self.assertEqual(spec['quest_nodes'][0]['kind'],'wait_actor_spawned')
        self.assertEqual(spec['quest_nodes'][0]['dynamic_name'],spec['actors'][0]['dynamic_name'])
        self.assertEqual(spec['quest_nodes'][0]['on_out'],[{'node_id':2}])

    def test_scanner_glyph_uses_vanilla_32_pixel_extent_at_1080p(self):
        atlas=json.loads((ROOT/'projects/ghostline/source/raw/mod/gq004/ui/heartbreaker.inkatlas.json').read_text())
        slot=atlas['Data']['RootChunk']['slots']['Elements'][1]
        parts={p['partName']['$value']:p['clippingRectInUVCoords'] for p in slot['parts']}
        for name,expected in [('heartbreaker',(50,65)),('velvet_crash',(32,32))]:
            rect=parts[name]
            self.assertEqual(((rect['Right']-rect['Left'])*256,(rect['Bottom']-rect['Top'])*256),expected)

    def test_audio_call_spans_recovery_upload_and_leave_without_video(self):
        from quest_compiler import load_spec,validate_no_forward_handle_refs
        spec,_=load_spec(HERE/'quest.json')
        document=phases.root(spec,Path('root.questphase'))
        validate_no_forward_handle_refs(document,context='operation audio call')
        explorer=self.explorer(document)
        ids={h:int(n.quest_id) for h,n in explorer.nodes_by_handle.items()}
        edges={(ids[e.source_node],ids[e.destination_node]) for e in explorer.edges_by_handle.values()}
        self.assertTrue({(22,60),(60,23),(25,61),(61,26)} <= edges)
        data={ids[h]:v for h,v in explorer.node_data_by_handle.items()}
        for number,phase in ((60,'StartCall'),(61,'EndCall')):
            call=data[number]['type']['Data']
            self.assertEqual(call['mode'],'Audio')
            self.assertEqual(call['phase'],phase)
            self.assertEqual(call['showAvatar'],0)
            self.assertEqual(call['caller']['Data']['realPath'],'contacts/velvet')
            self.assertEqual(call['addressee']['Data']['realPath'],'contacts/player')

    def test_deferred_meeting_resumes_choices_without_replaying_intro(self):
        import generate_scene
        spec=json.loads((HERE/'scenes/gq004_01.scene-spec.json').read_text())
        scene=generate_scene.build_scene(spec)
        self.assertEqual(generate_scene.validate_scene(scene,spec),[])
        self.assertIn({'name':'resume','node_id':23},spec['entry_points'])
        resume=next(n for n in spec['start_nodes'] if n['node_id']==23)
        self.assertEqual([n['node_id'] for n in resume['on_start']],[10,24])
        gate=next(n for n in spec['quest_nodes'] if n['node_id']==24)
        self.assertEqual(gate['trigger_ref'],'#gq004_tr_engage')
        self.assertEqual(gate['on_out'],[{'node_id':8}])


class WorldReadbackTests(unittest.TestCase):
    def setUp(self):
        self.document = {'Data': {'RootChunk': {
            '$type': 'worldStreamingSector',
            'nodes': [{'nodeRef': '#gq004_guard_1', 'position': {'X': -614.9, 'Y': 805.7, 'Z': 20.2}}],
        }}}

    def test_corrupted_placement_reference_and_missing_fields_fail(self):
        for change in ('position', 'reference', 'missing', 'extra_node'):
            actual = copy.deepcopy(self.document)
            nodes = actual['Data']['RootChunk']['nodes']
            if change == 'position':
                nodes[0]['position']['X'] += 1
            elif change == 'reference':
                nodes[0]['nodeRef'] = '#gq004_guard_2'
            elif change == 'missing':
                del nodes[0]['position']['Z']
            else:
                nodes.append(copy.deepcopy(nodes[0]))
            with self.subTest(change=change):
                self.assertFalse(world_builder.verify_document(self.document, actual, {})['ok'])

    def test_added_reader_fields_are_disclosed(self):
        actual = copy.deepcopy(self.document)
        actual['Data']['RootChunk']['readerDefault'] = 0
        report = world_builder.verify_document(self.document, actual, {})
        self.assertTrue(report['ok'])
        self.assertEqual(len(report['reader_added_fields']), 1)

    def test_device_buffer_envelope_does_not_hide_device_changes(self):
        data = {'$type': 'gameDeviceResourceData', 'devices': [{'nodeRef': '#gq004_ap_relay'}]}
        expected = {'Data': {'RootChunk': {'$type': 'gameDeviceResource', 'data': {'Data': data}}}}
        actual = {'Data': {'RootChunk': {'$type': 'gameDeviceResource', 'data': copy.deepcopy(data)}}}
        self.assertTrue(world_builder.verify_document(expected, actual, {})['ok'])
        actual['Data']['RootChunk']['data']['devices'][0]['nodeRef'] = '#gq004_ap_upload'
        self.assertFalse(world_builder.verify_document(expected, actual, {})['ok'])


class PlacementImportTests(unittest.TestCase):
    def setUp(self):
        self.world = json.loads(scout.WORLD.read_text(encoding='utf-8'))
        self.log = dict(schema_version=1, quest='gq004', captures={
            row['id']: dict(x=120, y=230, z=16, yaw=45)
            for row in scout.targets(self.world)
        })
        self.log['captures']['#gq004_ap_upload']['x'] = 123

    def test_complete_capture_preserves_geometry_and_does_not_mutate_source(self):
        before = copy.deepcopy(self.world)
        updated = scout.apply_captures(self.world, self.log)
        self.assertEqual(self.world, before)
        self.assertEqual(updated['triggers'][0]['position'], dict(x=120, y=230, z=10))
        self.assertEqual(updated['devices'][0]['yaw'], 135)
        self.assertEqual(updated['triggers'][0]['outline'], before['triggers'][0]['outline'])
        from generate_world import build_world_documents
        generated, _ = build_world_documents(updated, ROOT / '.tmp/test-gq004/raw', ROOT / '.tmp/test-gq004/archive')
        self.assertEqual(len(generated), 4)

    def test_missing_target_is_rejected(self):
        self.log['captures'].pop('#gq004_ap_upload')
        with self.assertRaisesRegex(ValueError, 'Missing captures'):
            scout.apply_captures(self.world, self.log)

    def test_capture_guidance_and_shortcuts_cover_every_target(self):
        rows = scout.targets(self.world)
        self.assertEqual(len({row['id'] for row in rows}), 16)
        self.assertEqual(sum(row['group'] == 'meeting' for row in rows), 8)
        self.assertEqual(sum(row['group'] == 'operation' for row in rows), 3)
        self.assertTrue(all(row['hint'] and row['label'] for row in rows))
        self.assertEqual(sum(row['height'] == 1.2 for row in rows), 2)

    def test_install_check_detects_outdated_capture_contract(self):
        with tempfile.TemporaryDirectory() as directory:
            game = Path(directory)
            executable = game / 'bin/x64/Cyberpunk2077.exe'
            executable.parent.mkdir(parents=True)
            executable.write_bytes(b'fixture')
            mod = game / 'bin/x64/plugins/cyber_engine_tweaks/mods' / scout.MOD
            mod.mkdir(parents=True)
            (game / 'bin/x64/plugins/cyber_engine_tweaks.asi').write_bytes(b'fixture')
            (mod / 'init.lua').write_bytes((HERE / 'cet/init.lua').read_bytes())
            rows = scout.targets(self.world)
            (mod / 'targets.json').write_text(json.dumps(rows), encoding='utf-8')
            self.assertTrue(scout.check_install(game, self.world)['ready_for_capture'])
            rows[0]['id'] = 'obsolete_origin'
            (mod / 'targets.json').write_text(json.dumps(rows), encoding='utf-8')
            report = scout.check_install(game, self.world)
            self.assertFalse(report['ready_for_capture'])
            self.assertIn('Installed target list is outdated', report['errors'])

    @unittest.skipUnless(shutil.which('lua'), 'Lua is needed for the CET contract harness')
    def test_cet_capture_persistence_and_resume_contract(self):
        rows = scout.targets(self.world)
        fixture = 'return {' + ','.join(
            '{id=' + json.dumps(row['id']) + ',label=' + json.dumps(row['label'])
            + ',group=' + json.dumps(row['group']) + ',height=' + str(row['height']) + '}'
            for row in rows) + '}'
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'targets.lua'
            path.write_text(fixture, encoding='utf-8')
            result = subprocess.run([shutil.which('lua'), 'tests/love_actually_scout_harness.lua', str(path)],
                                    cwd=ROOT, capture_output=True, text=True, timeout=20)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_nonfinite_and_boolean_positions_are_rejected(self):
        for value in (float('nan'), float('inf'), True, '16'):
            with self.subTest(value=value):
                self.log['captures']['origin']['z'] = value
                with self.assertRaisesRegex(ValueError, 'finite XYZ'):
                    scout.apply_captures(self.world, self.log)

    def test_other_quest_log_is_rejected(self):
        self.log['quest'] = 'gq003'
        with self.assertRaisesRegex(ValueError, 'GQ004'):
            scout.apply_captures(self.world, self.log)

    def test_coincident_socket_mounts_are_rejected(self):
        self.log['captures']['#gq004_ap_upload'] = dict(self.log['captures']['#gq004_ap_relay'])
        with self.assertRaisesRegex(ValueError, 'Socket captures coincide'):
            scout.apply_captures(self.world, self.log)

    def test_recovery_and_upload_use_distinct_devices(self):
        quest = json.loads((HERE / 'quest.json').read_text(encoding='utf-8'))
        stages = {s['id']: s for s in quest['stages']}
        self.assertNotEqual(stages['recover']['device'], stages['upload']['device'])
        self.assertNotEqual(stages['recover']['success_fact'], stages['upload']['success_fact'])
        self.assertNotIn('combat_encounter', {s['type'] for s in quest['stages']})


if __name__ == '__main__':
    unittest.main()
