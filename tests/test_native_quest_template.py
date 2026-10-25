"""Native transition contracts and GQ004 extraction parity; no engine simulation claim."""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import native_quest_template as template
from quest_compiler import load_spec, validate_handle_graph, validate_no_forward_handle_refs
from explore_questphase import QuestphaseExplorer


class NativeTemplateTests(unittest.TestCase):
    def setUp(self):
        self.config = json.loads((ROOT / 'quests/templates/native-personal-link/template.json').read_text())
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        self.output = Path(self.folder.name) / 'preview'
        self.ports = set()

    def build(self, config=None):
        artifacts, contract = template.compile_template(config or self.config, self.output)
        return {a.archive_path.name: a.document for a in artifacts}, contract

    def graph(self, document):
        path = Path(self.folder.name) / 'graph.json'
        path.write_text(json.dumps(document))
        validate_handle_graph(document, context='template')
        validate_no_forward_handle_refs(document, context='template')
        explorer = QuestphaseExplorer(path)
        ids = {h: int(n.quest_id) for h, n in explorer.nodes_by_handle.items()}
        nodes = {ids[h]: d for h, d in explorer.node_data_by_handle.items()}
        edges = {(ids[e.source_node], ids[e.destination_node]) for e in explorer.edges_by_handle.values()}
        self.ports = {(ids[e.source_node], e.source_socket_name, ids[e.destination_node], e.destination_socket_name)
                      for e in explorer.edges_by_handle.values()}
        return nodes, edges

    def test_isolated_complete_artifact_set_and_input_immutability(self):
        original = copy.deepcopy(self.config)
        docs, contract = self.build()
        self.assertEqual(len(docs), 12)
        self.assertEqual(self.config, original)
        for name, doc in docs.items():
            self.assertTrue(Path(doc['Header']['ArchiveFileName']).is_relative_to(self.output))
            if name.endswith('.questphase'):
                self.graph(doc)
        self.assertEqual(len(contract['registration_fragment']['quest']['phases']), 2)
        self.assertEqual(contract['profile_additional_root_phases'], [r'mod\relay_demo\phases\relay_demo_finish.questphase'])
        self.assertIn('not game-tested', contract['evidence'])

    def test_meeting_has_spawn_protection_and_immediate_resume_loop(self):
        docs, contract = self.build()
        nodes, edges = self.graph(docs['relay_demo_meet.questphase'])
        self.assertTrue({(13, 14), (14, 24), (24, 25), (25, 15), (15, 28),
                         (27, 26), (26, 15), (29, 18), (18, 19), (19, 20)} <= edges)
        self.assertEqual(nodes[15]['condition']['Data']['type'], 'IsInside')
        self.assertEqual(nodes[26]['condition']['Data']['type'], 'IsOutside')
        self.assertNotIn('questRealtimeDelay_ConditionType', json.dumps(nodes))
        self.assertEqual(nodes[29]['sceneFile']['DepotPath']['$value'], self.config['giver']['meeting_scene'])
        self.assertIn('Invulnerable', json.dumps(nodes[25]))
        self.assertEqual(contract['meeting_scene']['entries'], ['start', 'resume'])
        self.assertTrue({(28, 'False', 16, 'start'), (28, 'True', 29, 'resume'),
                         (29, 'end', 27, 'In'), (29, 'job_accept', 18, 'Succeeded')} <= self.ports)

    def test_attempt_retry_terminates_and_does_not_hide_success(self):
        self.config['transfers'][0]['duration_seconds'] = 9
        docs, _ = self.build()
        nodes, edges = self.graph(docs['relay_demo_recover_attempt.questphase'])
        self.assertTrue({(11, 12), (11, 13), (13, 15), (15, 2), (12, 14), (14, 1)} <= edges)
        self.assertNotIn((14, 15), edges)
        self.assertEqual(nodes[1]['type'], 'Terminating')
        self.assertEqual(nodes[2]['type'], 'Terminating')
        self.assertEqual(nodes[11]['type']['Data']['duration'], 9.0)
        self.assertEqual(nodes[12]['condition']['Data']['type']['Data']['seconds'], 9)

    def test_transfer_retirement_precedes_unplug_and_retry_reenters_attempt(self):
        docs, _ = self.build()
        nodes, edges = self.graph(docs['relay_demo_upload.questphase'])
        self.assertTrue({(15, 15), (15, 18), (18, 19), (19, 22), (22, 20),
                         (20, 21), (21, 50), (50, 51), (51, 1)} <= edges)
        self.assertNotIn((19, 20), edges)
        self.assertIn((15, 'Retry', 15, 'In1'), self.ports)
        self.assertIn((15, 'Out1', 18, 'In'), self.ports)
        self.assertEqual(nodes[22]['condition']['Data']['type']['Data']['tickCount'], 2)
        self.assertIn('QuestForceDisconnectPersonalLink', json.dumps(nodes[20]))
        self.assertNotIn('questAddRemoveItemNodeDefinition', json.dumps(nodes))

    def test_inventory_confirmation_completes_without_epilogue_or_cleanup(self):
        self.config['reward']['quantity'] = 2
        docs, _ = self.build()
        nodes, edges = self.graph(docs['relay_demo_finish.questphase'])
        self.assertTrue({(0, 20), (20, 1), (20, 10), (10, 11), (11, 12), (12, 13),
                         (12, 14), (13, 14), (14, 15), (15, 16), (16, 17), (17, 1)} <= edges)
        self.assertEqual(nodes[12]['condition']['Data']['type']['Data']['quantity'], 2)
        self.assertEqual(nodes[13]['condition']['Data']['type']['Data']['quantity'], 2)
        self.assertTrue({(20, 'True', 1, 'In'), (20, 'False', 10, 'In'),
                         (12, 'True', 14, 'In'), (12, 'False', 13, 'In')} <= self.ports)
        self.assertNotIn('questTriggerCondition', json.dumps(nodes))
        root, root_edges = self.graph(docs['relay_demo_root.questphase'])
        self.assertTrue({(23, 40), (40, 41), (41, 1)} <= root_edges)
        self.assertTrue({(10, 'True', 1, 'In'), (10, 'False', 20, 'In1')} <= self.ports)
        self.assertEqual(root[40]['condition']['Data']['type'], 'IsOutside')
        self.assertNotIn('questJournalQuestEntry_NodeType', json.dumps(root))

    def test_optional_epilogue_follows_completion_and_repair_is_once_only(self):
        self.config['epilogue'] = {'phase': r'mod\relay_demo\phases\later_messages.questphase', 'delay_seconds': 30}
        self.config['reward']['repair_completed_saves'] = True
        docs, contract = self.build()
        nodes, edges = self.graph(docs['relay_demo_finish.questphase'])
        self.assertTrue({(16, 17), (17, 18), (18, 19), (19, 1)} <= edges)
        self.assertEqual(nodes[18]['condition']['Data']['type']['Data']['seconds'], 30)
        nodes, edges = self.graph(docs['relay_demo_reward_repair.questphase'])
        self.assertTrue({(12, 1), (12, 13), (13, 16), (13, 14), (14, 15), (15, 16), (16, 17)} <= edges)
        self.assertEqual(len(contract['profile_additional_root_phases']), 2)
        self.assertTrue({(12, 'True', 1, 'In'), (12, 'False', 13, 'In'),
                         (13, 'False', 14, 'In'), (13, 'True', 16, 'In')} <= self.ports)

    def test_connected_speech_and_intro_are_ordered_with_actual_connection(self):
        scene = dict(scene=r'mod\relay_demo\scenes\field.scene', origin='#holocall_marker', entry='begin', exit='finished')
        transfer = self.config['transfers'][1]
        for key in ('intro_scene', 'retry_scene', 'success_scene', 'connected_scene'):
            transfer[key] = scene
        self.config['phase_prefabs'].append('#holocalls_studio')
        self.config['audio_call'] = dict(caller='contacts/relay_giver', addressee='contacts/player',
            prefab='#holocalls_studio', start_before='recover', end_before='return')
        docs, _ = self.build()
        _, edges = self.graph(docs['relay_demo_upload_attempt.questphase'])
        self.assertTrue({(11, 16), (12, 17), (16, 17), (17, 14)} <= edges)
        _, edges = self.graph(docs['relay_demo_upload.questphase'])
        self.assertTrue({(12, 13), (13, 14), (14, 15), (15, 17), (17, 15), (51, 52)} <= edges)
        root, _ = self.graph(docs['relay_demo_root.questphase'])
        self.assertIn('StartCall', json.dumps(root[60]))
        self.assertIn('EndCall', json.dumps(root[61]))

    def test_second_namespace_has_no_gq004_content_or_source_dependency(self):
        config = json.loads(json.dumps(self.config).replace('relay_demo', 'other_relay'))
        original = Path.read_text
        def guarded(path, *args, **kwargs):
            if 'gq004' in path.as_posix():
                raise AssertionError('Template depends on quest-owned GQ004 inputs')
            return original(path, *args, **kwargs)
        with patch.object(Path, 'read_text', guarded):
            docs, contract = self.build(config)
        text = json.dumps([docs, contract])
        self.assertNotIn('relay_demo', text)
        self.assertNotIn('gq004', text)
        self.assertNotIn('Velvet', text)
        self.assertIn('other_relay_reward_delivery_verified', text)

    def test_devices_use_pinned_neutral_clones_without_hacking_gate(self):
        docs, contract = self.build()
        for name in ('recover', 'upload'):
            device = docs[name + '.ent']
            state = device['Data']['RootChunk']['compiledData']['Data']['Chunks'][4]['persistentState']['Data']
            check = state['accessPointSkillChecks']['Data']['hackingCheck']['Data']
            self.assertEqual((check['difficulty'], check['isActive']), ('NONE', 0))
            self.assertEqual(state['shouldSkipNetrunnerMinigame'], 1)
            self.assertEqual(state['hasPersonalLinkSlot'], 1)
            self.assertEqual(state['personalLinkCustomInteraction']['$value'], 'Interactions.ConnectPersonalLink')
        self.assertEqual(len(contract['required_world']['devices']), 2)

    def test_entity_readback_adapter_preserves_values_and_default_alias_policy(self):
        from cr2w_validation import compare_documents
        value = {'$type': 'AccessPointControllerPS', 'shouldSkipNetrunnerMinigame': 1}
        inline = {'Data': {'RootChunk': {'$type': 'entEntityTemplate',
            'first': copy.deepcopy(value), 'second': copy.deepcopy(value)}}}
        shared = {'Data': {'RootChunk': {'$type': 'entEntityTemplate',
            'first': {'HandleId': '0', 'Data': copy.deepcopy(value)}, 'second': {'HandleRefId': '0'}}}}
        self.assertEqual(template.access_point_values(shared), inline)
        with self.assertRaisesRegex(ValueError, 'Unsupported shared'):
            compare_documents(inline, shared, schema={})
        shared['Data']['RootChunk']['first']['Data']['shouldSkipNetrunnerMinigame'] = 0
        self.assertFalse(compare_documents(inline, template.access_point_values(shared), schema={}).ok)

    def test_entity_readback_adapter_rejects_unknown_duplicate_and_cyclic_handles(self):
        base = {'Data': {'RootChunk': {'$type': 'entEntityTemplate',
            'value': {'HandleId': '0', 'Data': {'$type': 'AccessPointControllerPS'}}}}}
        cases = []
        d = copy.deepcopy(base); d['Data']['RootChunk']['other'] = {'HandleRefId': '99'}; cases.append(d)
        d = copy.deepcopy(base); d['Data']['RootChunk']['other'] = copy.deepcopy(d['Data']['RootChunk']['value']); cases.append(d)
        d = copy.deepcopy(base); d['Data']['RootChunk']['value']['Data']['cycle'] = {'HandleRefId': '0'}; cases.append(d)
        for document in cases:
            with self.subTest(document=document), self.assertRaises(ValueError):
                template.access_point_values(document)
        with self.assertRaises(ValueError):
            template.access_point_values({'Data': {'RootChunk': {'$type': 'questQuestPhaseResource'}}})

    def test_custom_interaction_and_quantity_remain_explicit_bindings(self):
        self.config['reward']['quantity'] = 3
        self.config['transfers'][0]['interaction_record'] = 'Interactions.MyRecovery'
        docs, _ = self.build()
        state = docs['recover.ent']['Data']['RootChunk']['compiledData']['Data']['Chunks'][4]['persistentState']['Data']
        self.assertEqual(state['personalLinkCustomInteraction']['$value'], 'Interactions.MyRecovery')
        returned, _ = self.graph(docs['relay_demo_return.questphase'])
        self.assertIn('Items.RelayDemoPrototype', json.dumps(returned[21]))
        # The same authored quantity reaches the transaction and both inventory checks.
        self.assertIn('"quantity": 3', json.dumps(returned[21]))

    def test_invalid_bindings_fail_before_publication(self):
        invalid = []
        d = copy.deepcopy(self.config); d['namespace'] = '../foreign'; invalid.append(d)
        d = copy.deepcopy(self.config); d['transfers'][0]['duration_seconds'] = True; invalid.append(d)
        d = copy.deepcopy(self.config); d['transfers'][0]['duration_seconds'] = 0; invalid.append(d)
        d = copy.deepcopy(self.config); d['transfers'][0]['typo'] = 'bad'; invalid.append(d)
        d = copy.deepcopy(self.config); d['transfers'][1]['device'] = d['transfers'][0]['device']; invalid.append(d)
        d = copy.deepcopy(self.config); d['transfers'][1]['id'] = 'recover_attempt'; invalid.append(d)
        d = copy.deepcopy(self.config); d['giver']['meeting_scene'] = 'mod/../bad.scene'; invalid.append(d)
        d = copy.deepcopy(self.config); d['epilogue'] = dict(phase=r'mod\relay_demo\phases\relay_demo_finish.questphase', delay_seconds=1); invalid.append(d)
        for config in invalid:
            with self.subTest(config=config), self.assertRaises(ValueError):
                self.build(config)
        self.assertFalse(self.output.exists())

    def test_output_cannot_overwrite_project_or_template_source(self):
        for destination in [ROOT, ROOT / 'projects/ghostline', ROOT / 'quests/templates/source/raw/new-template']:
            with self.subTest(destination=destination), self.assertRaises(ValueError):
                template.compile_template(self.config, destination)

    def test_cli_publishes_scratch_artifacts_and_contract(self):
        subprocess.run([sys.executable, str(ROOT / 'tools/native_quest_template.py'), '--spec',
            str(ROOT / 'quests/templates/native-personal-link/template.json'), '--out-root', str(self.output)],
            cwd=ROOT, check=True, capture_output=True)
        self.assertEqual(len(list((self.output / 'source/raw').rglob('*.json'))), 12)
        self.assertEqual(json.loads((self.output / 'native-contract.json').read_text())['namespace'], 'relay_demo')


class GQ004ExtractionParityTests(unittest.TestCase):
    def test_playtested_graphs_remain_structurally_identical(self):
        here = ROOT / 'projects/ghostline/quests/gq004/implementation'
        spec = importlib.util.spec_from_file_location('gq004_extraction_adapter', here / 'phases.py')
        phases = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(phases)
        quest, diagnostics = load_spec(here / 'quest.json')
        self.assertFalse([d for d in diagnostics if d.level == 'error'])
        stages = {s.id: s for s in quest.stages}
        docs = {key: phases.meeting(stages[key], Path(key + '.questphase')) for key in ('meet', 'return')}
        for key, label in [('recover', 'Heartbreaker Protocol'), ('upload', 'Velvet Crash')]:
            docs[key + '_attempt'] = phases.attempt(stages[key].data['device'], Path(key + '_attempt.questphase'), label)
        docs.update(root=phases.root(quest, Path('root.questphase')),
            finish=phases.finish_and_epilogue(Path('finish.questphase')), repair=phases.reward_repair(Path('repair.questphase')))
        expected = json.loads((ROOT / 'quests/templates/native-personal-link/gq004-graph-baseline.json').read_text())
        for name, document in docs.items():
            digest = hashlib.sha256(json.dumps(document, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
            self.assertEqual(digest, expected['graphs'][name], name)


if __name__ == '__main__':
    unittest.main()
