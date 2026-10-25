"""GQ004 content bindings and callbacks over the reusable native lifecycle."""
import quest_native_lifecycle as native
from quest_native_lifecycle import tick_delay, fact_branch
from phase_graph import (
    PhaseGraphBuilder, input_node, output_node, objective_node, journal_entry_node,
    mappin_node, community_action_node, character_spawned_node, trigger_condition_node,
    fact_node, phase_document, fact_condition_node,
    device_condition_node, device_manager_node, add_item_node, entity_reference, tweakdbid,
    journal_entry_visited_node, logical_and_node,
)
from quest_encounter import scene_flow_node, character_attitude_group_node


def leave(stage, archive):
    """Accept departure during the preceding upload VO or before save/load."""
    from quest_compiler import build_leave_area_phase
    document = build_leave_area_phase(stage, archive)
    def patch(value):
        if isinstance(value, dict):
            if value.get('$type') == 'questTriggerCondition':
                value['type'] = 'IsOutside'
            for child in value.values():
                patch(child)
        elif isinstance(value, list):
            for child in value:
                patch(child)
    patch(document)
    return document


def reach(stage, archive):
    b = PhaseGraphBuilder()
    start, end = input_node(b), output_node(b)
    chain = [
        (objective_node(b, 10, stage.data['objective']), 'Active'),
        (journal_entry_node(b, 11, stage.data['description_entry'], 'gameJournalQuestDescription', 2), 'Active'),
        (mappin_node(b, 12, stage.data['mappin'], disable_previous_mappins=True), 'Active'),
        (community_action_node(b, 13, '#gq004_com_claws', 'Activate'), 'In'),
        (character_spawned_node(b, 14, '#gq004_com_claws'), 'In'),
    ]
    for index, entry in enumerate(('guard_ranged_m', 'guard_ranged_f', 'guard_melee')):
        chain.append((character_attitude_group_node(b, 15 + index, '#gq004_com_claws', entry,
                                                    group_name='hostile'), 'In'))
    chain.extend([
        (trigger_condition_node(b, 20, stage.data['trigger'], 'IsInside'), 'In'),
        (fact_node(b, 21, 'gq004_operation_reached'), 'In'),
        (objective_node(b, 22, stage.data['objective']), 'Succeeded'),
        (mappin_node(b, 23, stage.data['mappin']), 'Inactive'),
        (community_action_node(b, 24, '#gq004_com_velvet', 'Deactivate'), 'In'),
    ])
    previous = start
    for node, socket in chain:
        b.connect(previous, node, destination_socket=socket)
        previous = node
    b.connect_to_earlier_output(previous, end)
    return phase_document(b, archive)


def meeting(stage, archive):
    return native.meeting(stage, archive, setup_trigger='#gq004_tr_setup',
        rearm_trigger='#gq004_tr_engage', scene_origin='#gq004_sm_velvet',
        success_fact='gq004_job_accepted' if stage.id == 'meet' else 'gq004_debrief_done',
        protection_source='gq004_velvet_protection', phase_prefabs=('#gq004_pr_love_actually',),
        deferred_fact='gq004_meet_deferred' if stage.id == 'meet' else None,
        reward_item='Items.GhostlineLoveHeartbreaker' if stage.id == 'return' else None)


def attempt(device, archive, label='Heartbreaker Protocol'):
    connected_scene = dict(scene=r'mod\gq004\scenes\gq004_02_brand.scene',
        origin='#holocall_marker', entry='start', exit='end') if label == 'Velvet Crash' else None
    return native.attempt(device, archive, label, connected_scene=connected_scene)


def field_scene(b, number, beat):
    return scene_flow_node(b, number, dict(scene=rf'mod\gq004\scenes\gq004_02_{beat}.scene',
        origin='#holocall_marker', entry='start', exit='end'))


def status(b, number, entry, record):
    subtype = b.handles.wrap({'$type': 'questCharacterManagerParameters_SetStatusEffect',
        'isPlayer': 0, 'isPlayerStatusEffectSource': 1, 'set': 1,
        'puppetRef': entity_reference('#gq004_com_claws', names=[entry]),
        'statusEffectID': tweakdbid(record), 'statusEffectSourceObject': entity_reference('#player'),
        'recordSelector': None})
    kind = b.handles.wrap({'$type': 'questCharacterManagerParameters_NodeType', 'subtype': subtype})
    return b.node(number, 'questCharacterManagerNodeDefinition', input_names=('In',), properties={'type': kind})


def transfer(stage, archive):
    from quest_compiler import phase_node
    b = PhaseGraphBuilder()
    start, end = input_node(b), output_node(b)
    chain = [
        (objective_node(b, 10, stage.data['objective']), 'Active'),
        (journal_entry_node(b, 11, stage.data['description_entry'], 'gameJournalQuestDescription', 2), 'Active'),
        (mappin_node(b, 12, stage.data['mappin'], disable_previous_mappins=True), 'Active'),
        (device_manager_node(b, 14, stage.data['device'], 'AccessPointControllerPS', 'ForceON'), 'In'),
    ]
    previous, output = start, 'Out'
    for node, port in chain:
        if stage.id == 'upload' and node is chain[-1][0]:
            continue
        b.connect(previous, node, source_socket=output, destination_socket=port)
        previous, output = node, 'Out'
    # Recovery remains armed while its approach explanation plays. Upload's
    # explanation finishes before enabling that socket, so its naming exchange
    # can start with the actual connection rather than over the instructions.
    intro = field_scene(b, 13, 'arrive' if stage.id == 'recover' else 'upload')
    b.connect(chain[2][0], intro, destination_socket='start')
    wait = phase_node(b, 15, rf'mod\gq004\phases\gq004_{stage.id}_attempt.questphase', outputs=('Out1', 'Retry'))
    if stage.id == 'upload':
        b.connect_to_earlier_input(intro, chain[-1][0], source_socket='end')
        previous, output = chain[-1][0], 'Out'
    b.connect(previous, wait, source_socket=output, destination_socket='In1')
    interrupted = fact_node(b, 16, 'gq004_link_interrupted')
    retry_vo = field_scene(b, 17, 'retry')
    b.connect(wait, interrupted, source_socket='Retry')
    if stage.id == 'recover':
        briefed = fact_node(b, 23, 'gq004_recovery_briefing_done')
        wait_briefing = fact_condition_node(b, 24, 'gq004_recovery_briefing_done', comparison='Equal', value=1)
        b.connect(intro, briefed, source_socket='end')
        b.connect(interrupted, wait_briefing)
        b.connect_to_earlier_input(wait_briefing, retry_vo, destination_socket='start')
    else:
        b.connect(interrupted, retry_vo, destination_socket='start')
    b.connect_to_earlier_input(retry_vo, wait, source_socket='end', destination_socket='In1')
    still_connected = device_condition_node(b, 18, stage.data['device'], stage.data['controller_class'], stage.data['completion_function'])
    copied = fact_node(b, 19, stage.data['success_fact'])
    b.connect(wait, still_connected, source_socket='Out1')
    b.connect(still_connected, copied)
    disconnect = device_manager_node(b, 20, stage.data['device'], 'AccessPointControllerPS', 'QuestForceDisconnectPersonalLink')
    # Give the terminating child time to remove its disconnect listener BEFORE
    # forcing an unplug; delaying inside the child does not protect this edge.
    retired = tick_delay(b, 22)
    b.connect(copied, retired)
    b.connect_to_earlier_input(retired, disconnect)
    disable = device_manager_node(b, 21, stage.data['device'], 'AccessPointControllerPS', 'ForceDisabled')
    b.connect(disconnect, disable)
    previous = disable
    number = 30
    if stage.id == 'recover':
        for alias in ('Sales',):
            journal = journal_entry_node(b, number, f'onscreens/emails/quests/minor_quest/gq004/files/{alias.lower()}', 'gameJournalOnscreen', 0)
            grant = add_item_node(b, number + 1, 'Items.GhostlineLove' + alias, 1)
            b.connect(previous, journal, destination_socket='Active')
            b.connect(journal, grant)
            previous, number = grant, number + 2
    else:
        for entry in ('guard_ranged_m', 'guard_ranged_f', 'guard_melee'):
            for record in ('BaseStatusEffect.GhostlineVelvetCrashVision', 'BaseStatusEffect.GhostlineVelvetCrashShortBlind'):
                fx = status(b, number, entry, record)
                b.connect(copied, fx)  # Fire-and-forget: dead/missing guards cannot block progression.
                number += 1
    done = objective_node(b, 50, stage.data['objective'])
    pin = mappin_node(b, 51, stage.data['mappin'])
    vo = field_scene(b, 52, 'recovered' if stage.id == 'recover' else 'success')
    b.connect(previous, done, destination_socket='Succeeded')
    b.connect(done, pin, destination_socket='Inactive')
    heard = logical_and_node(b, 53, 2)
    b.connect(pin, heard, destination_socket='In1')
    b.connect(intro, heard, source_socket='end', destination_socket='In2')
    b.connect_to_earlier_input(heard, vo, source_socket='Out1', destination_socket='start')
    if stage.id == 'recover':
        previous, socket = vo, 'end'
        for index, (shard, beat) in enumerate((('sales', 'evidence'), ('archive', 'archive'), ('revocation', None))):
            number = 60 + index * 5
            if index:
                # Reveal the next document only after the preceding read and
                # its comment scene have finished. Existing saves keep items.
                journal = journal_entry_node(b, 80 + index * 2,
                    f'onscreens/emails/quests/minor_quest/gq004/files/{shard}', 'gameJournalOnscreen', 0)
                grant = add_item_node(b, 81 + index * 2, 'Items.GhostlineLove' + shard.title(), 1)
                b.connect(previous, journal, source_socket=socket, destination_socket='Active')
                b.connect(journal, grant)
                previous, socket = grant, 'Out'
            path = f'quests/minor_quest/gq004/gq004_01/gq004_obj_read_{shard}'
            active = objective_node(b, number, path)
            read = journal_entry_visited_node(b, number + 1,
                f'onscreens/emails/quests/minor_quest/gq004/files/{shard}', 'gameJournalOnscreen', file_index=0)
            done_read = objective_node(b, number + 2, path)
            b.connect(previous, active, source_socket=socket, destination_socket='Active')
            b.connect(active, read)
            b.connect(read, done_read, destination_socket='Succeeded')
            previous, socket = done_read, 'Out'
            if beat:
                comment = field_scene(b, number + 3, beat)
                b.connect(previous, comment, destination_socket='start')
                previous, socket = comment, 'end'
        b.connect_to_earlier_output(previous, end, source_socket=socket)
    else:
        b.connect_to_earlier_output(vo, end, source_socket='end')
    return phase_document(b, archive, phase_prefabs=('#gq004_pr_love_actually', '#holocalls_studio'))


def root(spec, archive):
    return native.root(spec, archive, completed_fact='gq004_completed',
        cleanup_trigger='#gq004_tr_mood', cleanup_community='#gq004_com_velvet',
        skipped_stages=('ending',), call=dict(start_before='recover', end_before='return',
        caller='contacts/velvet'), guard_completed=False)


def ending(stage, archive):
    """One-shot wrapper also guards old saves still running the previous root."""
    from quest_compiler import phase_node
    b = PhaseGraphBuilder()
    start, end = input_node(b), output_node(b)
    started = fact_branch(b, 10, 'gq004_epilogue_started')
    mark = fact_node(b, 11, 'gq004_epilogue_started')
    phone = phase_node(b, 12, r'mod\gq004\phases\gq004_epilogue_messages.questphase')
    b.connect(start, started)
    b.connect_to_earlier_output(started, end, source_socket='True')
    b.connect(started, mark, source_socket='False')
    b.connect(mark, phone, destination_socket='In1')
    b.connect_to_earlier_output(phone, end, source_socket='Out1')
    return phase_document(b, archive)


def finish_and_epilogue(archive):
    return native.finish_and_epilogue(archive, debrief_fact='gq004_debrief_done',
        reward_item='Items.GhostlineLoveHeartbreaker', verified_fact='gq004_reward_delivery_verified',
        granted_fact='gq004_reward_granted', quest_path='quests/minor_quest/gq004',
        completed_fact='gq004_completed', epilogue_phase=r'mod\gq004\phases\gq004_ending.questphase',
        guard_completed=False)


def reward_repair(archive):
    return native.reward_repair(archive, completed_fact='gq004_completed',
        debrief_fact='gq004_debrief_done', verified_fact='gq004_reward_delivery_verified',
        granted_fact='gq004_reward_granted', reward_item='Items.GhostlineLoveHeartbreaker')
