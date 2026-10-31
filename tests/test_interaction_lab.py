"""GQT008 cancellation, re-entry and resource contracts; no engine simulation."""
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from explore_questphase import QuestphaseExplorer
from quest_compiler import validate_handle_graph, validate_no_forward_handle_refs
import generate_scene
from build_scene_performance_library import walk

spec = importlib.util.spec_from_file_location('interaction_fixture', ROOT / 'projects/test-quests/gqt008/implementation/build.py')
fixture = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fixture)


class InteractionLabTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.artifacts = fixture.build_artifacts()
        cls.documents = {a.archive_path.name: a.document for a in cls.artifacts}

    def graph(self, name):
        document = self.documents[name]
        validate_handle_graph(document, context=name)
        validate_no_forward_handle_refs(document, context=name)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'phase.json'
            path.write_text(json.dumps(document))
            explorer = QuestphaseExplorer(path)
            ids = {h: int(n.quest_id) for h, n in explorer.nodes_by_handle.items()}
            nodes = {ids[h]: d for h, d in explorer.node_data_by_handle.items()}
            ports = {(ids[e.source_node], e.source_socket_name, ids[e.destination_node], e.destination_socket_name)
                     for e in explorer.edges_by_handle.values()}
        return nodes, ports

    def test_attempt_terminates_all_three_outcomes_and_owns_departure_listener(self):
        for entry in ('start', 'resume'):
            nodes, ports = self.graph(f'attempt_{entry}.questphase')
            self.assertEqual({nodes[i]['socketName']['$value'] for i in (1, 2, 3)}, {'Complete', 'Deferred', 'Away'})
            self.assertTrue(all(nodes[i]['type'] == 'Terminating' for i in (1, 2, 3)))
            self.assertTrue({(0, 'Out', 10, entry), (0, 'Out', 11, 'In'),
                (10, 'job_accept', 1, 'In'), (10, 'end', 2, 'In'), (11, 'Out', 3, 'In')} <= ports)
            self.assertEqual(nodes[11]['condition']['Data']['type'], 'IsOutside')

    def test_quick_return_is_latched_before_restoration_and_away_needs_no_second_departure(self):
        nodes, ports = self.graph('gqt008_interaction.questphase')
        edges = {(a, c) for a, _, c, _ in ports}
        self.assertTrue({(30, 32), (30, 38), (32, 35), (35, 39), (38, 39),
            (39, 20), (31, 33), (33, 36), (36, 20)} <= edges)
        self.assertNotIn((36, 38), edges)
        self.assertEqual(nodes[38]['condition']['Data']['type'], 'IsOutside')
        self.assertEqual(nodes[38]['condition']['Data']['triggerAreaRef']['$value'], '#gqt008_tr_engage')
        self.assertIn((21, 'False', 22, 'In1'), ports)
        self.assertIn((21, 'True', 23, 'In1'), ports)

    def test_spawn_and_activity_readiness_precede_presentation_and_completion_precedes_cleanup(self):
        _, ports = self.graph('gqt008_interaction.questphase')
        edges = {(a, c) for a, _, c, _ in ports}
        self.assertTrue({(12, 13), (13, 14), (14, 15), (17, 18), (18, 20),
            (34, 37), (37, 40), (40, 41), (41, 42), (42, 43), (43, 44),
            (44, 45), (45, 46), (46, 47)} <= edges)
        self.assertIn((41, 'Out', 42, 'Inactive'), ports)
        self.assertIn((42, 'Out', 43, 'Succeeded'), ports)

    def test_scene_bindings_and_world_targets_are_isolated(self):
        for a in self.artifacts:
            self.assertTrue(a.archive_path.is_relative_to(fixture.PROJECT / 'source/archive/mod/gqt008'))
            self.assertNotIn('mod\\building_lab\\', json.dumps(a.document).replace('\\\\', '\\'))
        world = fixture.read(fixture.PROJECT / 'implementation/world/interaction.world.json')
        self.assertEqual(world['community']['character'], 'Character.mq010_barry')
        self.assertEqual(world['community']['active_on_start'], 0)
        self.assertEqual(world['origin']['z'], 700)
        self.assertEqual(world['ai_spots'][0]['ref'], '#gqt008_spot_wait')

    def test_performance_and_restore_commands_use_acknowledged_distinct_routes(self):
        for key, filename in [('interaction', 'gqt008_interaction.scene'), ('restore', 'gqt008_restore.scene')]:
            authored = fixture.read(fixture.PROJECT / f'implementation/scenes/{key}.scene-spec.json')
            self.assertEqual(generate_scene.validate_scene(self.documents[filename], authored), [])
        main = self.documents['gqt008_interaction.scene']['Data']['RootChunk']
        restore = self.documents['gqt008_restore.scene']['Data']['RootChunk']
        body = [v for v in walk(main) if v.get('$type') == 'scnPlaySkAnimEvent']
        self.assertEqual(len(body), 4)
        work = [v for v in walk(main) if v.get('$type') == 'questUseWorkspotParamsV1']
        move = next(v for v in work if v['function'] == 'UseWorkspot')
        self.assertEqual((move['teleport'], move['instant'], move['repeatCommandOnInterrupt']), (0, 0, 0))
        exit_work = next(v for v in work if v['function'] == 'StopWorkspot')
        self.assertEqual(exit_work['exitEntryId']['id'], 19)
        modes = [v for v in walk(restore) if v.get('$type') == 'questUseWorkspotParamsV1']
        seat = next(v for v in modes if v['function'] == 'UseWorkspot')
        self.assertEqual(seat['entryId']['id'], 2)
        release = next(v for v in modes if v['function'] == 'IdleOnlyMode')
        self.assertEqual(release['enableIdleMode'], 0)
        self.assertEqual(release['workspotNode']['$value'], '0')
        self.assertEqual(release['repeatCommandOnInterrupt'], 0)


if __name__ == '__main__':
    unittest.main()
