"""Quest-owned native lifecycle hooks, shared compiler remains unchanged."""
from phase_graph import (
    PhaseGraphBuilder, input_node, output_node, objective_node, journal_entry_node,
    mappin_node, community_action_node, character_spawned_node, trigger_condition_node,
    fact_node, phase_document, realtime_delay_node, fact_condition_node,
    device_condition_node, device_manager_node, add_item_node, cname, entity_reference, tweakdbid,
    inventory_condition_node, journal_entry_visited_node, quest_completion_node, logical_and_node,
    journal_path, node_ref,
)
from quest_encounter import scene_flow_node, character_attitude_group_node, character_mortality_node


def audio_call(b, number, phase):
    """Native audio-call HUD; direct StartCall is supported by PhoneSystem."""
    kind = b.handles.wrap({'$type': 'questCallContact_NodeType',
        'caller': journal_path(b, 'contacts/velvet', 'gameJournalContact', 1),
        'addressee': journal_path(b, 'contacts/player', 'gameJournalContact', 1),
        'phase': phase, 'mode': 'Audio', 'prefabNodeRef': node_ref('#holocalls_studio'),
        'applyPhoneRestriction': 0, 'isRejectable': 0, 'showAvatar': 0, 'visuals': 'Default'})
    return b.node(number, 'questPhoneManagerNodeDefinition', input_names=('In',), properties={'type': kind})


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
    b = PhaseGraphBuilder()
    start, end = input_node(b), output_node(b)
    objective = objective_node(b, 10, stage.data['objective'])
    description = journal_entry_node(b, 11, stage.data['description_entry'], 'gameJournalQuestDescription', 2)
    pin = mappin_node(b, 12, stage.data['mappin'], disable_previous_mappins=True)
    spawn = community_action_node(b, 13, stage.data['community'], 'Activate')
    action = spawn.data['actions'][0]['type']['Data']
    action['communityEntryName']['$value'] = stage.data['contact']
    action['communityEntryPhaseName']['$value'] = 'default'
    ready = character_spawned_node(b, 14, stage.data['community'])
    friendly = character_attitude_group_node(b, 24, stage.data['community'], stage.data['contact'], group_name='friendly')
    protect = character_mortality_node(b, 25, stage.data['community'], stage.data['contact'],
        state='Invulnerable', source='gq004_velvet_protection')
    setup = trigger_condition_node(b, 15, '#gq004_tr_setup', 'IsInside')
    scene = scene_flow_node(b, 16, dict(scene=stage.data['scene'], origin='#gq004_sm_velvet',
                                      entry='start', exit='job_accept', completion_exits=['end']))
    # Subscribe immediately: a delay before this condition misses a quick
    # step away and return. Reuse the actual choice radius, not the greeting.
    outside = trigger_condition_node(b, 26, '#gq004_tr_engage', 'IsOutside')
    done = objective_node(b, 18, stage.data['objective'])
    hide = mappin_node(b, 19, stage.data['mappin'])
    fact = fact_node(b, 20, 'gq004_job_accepted' if stage.id == 'meet' else 'gq004_debrief_done')
    b.connect(start, objective, destination_socket='Active')
    b.connect(objective, description, destination_socket='Active')
    b.connect(description, pin, destination_socket='Active')
    for left, right in ((pin, spawn), (spawn, ready), (ready, friendly), (friendly, protect), (protect, setup)):
        b.connect(left, right)
    if stage.id == 'meet':
        returning = fact_branch(b, 28, 'gq004_meet_deferred')
        resume = scene_flow_node(b, 29, dict(scene=stage.data['scene'], origin='#gq004_sm_velvet',
            entry='resume', exit='job_accept', completion_exits=['end']))
        deferred = fact_node(b, 27, 'gq004_meet_deferred')
        b.connect(setup, returning)
        b.connect_to_earlier_input(returning, scene, source_socket='False', destination_socket='start')
        b.connect(returning, resume, source_socket='True', destination_socket='resume')
        b.connect(scene, deferred, source_socket='end')
        b.connect_to_earlier_input(resume, deferred, source_socket='end')
        b.connect_to_earlier_input(deferred, outside)
        b.connect_to_earlier_input(resume, done, source_socket='job_accept', destination_socket='Succeeded')
    else:
        b.connect(setup, scene, destination_socket='start')
        b.connect(scene, outside, source_socket='end')
    b.connect_to_earlier_input(outside, setup)
    b.connect(scene, done, source_socket='job_accept', destination_socket='Succeeded')
    b.connect(done, hide, destination_socket='Inactive')
    b.connect(hide, fact)
    if stage.id == 'return':
        reward = add_item_node(b, 21, 'Items.GhostlineLoveHeartbreaker', 1)
        b.connect(fact, reward)
        # The finish root verifies delivery after the transaction has settled.
        b.connect_to_earlier_output(reward, end)
    else:
        b.connect_to_earlier_output(fact, end)
    return phase_document(b, archive, phase_prefabs=('#gq004_pr_love_actually',))


def progress(b, number, show, label='Heartbreaker Protocol'):
    subtype = b.handles.wrap({'$type': 'questProgressBar_NodeType', 'duration': 5.0,
        'show': int(show), 'text': {'unk1': '0', 'value': label},
        'bottomText': {'unk1': '0', 'value': 'Verifying transfer'}, 'type': 'Connection'})
    return b.node(number, 'questUIManagerNodeDefinition', input_names=('In',), properties={'type': subtype})


def tick_delay(b, number):
    ticks = b.handles.wrap({'$type': 'questTickDelay_ConditionType', 'tickCount': 2})
    condition = b.handles.wrap({'$type': 'questTimeCondition', 'type': ticks})
    return b.node(number, 'questPauseConditionNodeDefinition', input_names=('In',),
                  properties={'condition': condition})


def attempt(device, archive, label='Heartbreaker Protocol'):
    """Terminating success/retry exits cancel the losing timer/listener branch."""
    b = PhaseGraphBuilder()
    start, success = input_node(b), output_node(b)
    retry = b.node(2, 'questOutputNodeDefinition', input_names=('In',), output_names=(),
                   properties={'socketName': cname('Retry'), 'type': 'Terminating'})
    arm = device_manager_node(b, 3, device, 'AccessPointControllerPS', 'QuestForcePersonalLinkUnderStrictQuestControl')
    connected = device_condition_node(b, 10, device, 'AccessPointControllerPS', 'IsPersonalLinkConnected')
    bar = progress(b, 11, True, label)
    timer = realtime_delay_node(b, 12, seconds=5)
    broken = device_condition_node(b, 13, device, 'AccessPointControllerPS', 'IsPersonalLinkDisconnected')
    # Native HUD owns the successful outro. Hiding at the timer boundary races
    # its delayed progress callback and incorrectly plays the failed animation.
    settled = tick_delay(b, 14)
    hide_retry = progress(b, 15, False, label)
    b.connect(start, arm)
    b.connect(arm, connected)
    b.connect(connected, bar)
    b.connect(bar, timer)
    b.connect(bar, broken)
    if label == 'Velvet Crash':
        # This scene belongs to the attempt: it starts with the actual plug-in
        # and a terminating retry cancels it along with the progress timer.
        brand = field_scene(b, 16, 'brand')
        heard = logical_and_node(b, 17, 2)
        b.connect(bar, brand, destination_socket='start')
        b.connect(timer, heard, destination_socket='In1')
        b.connect(brand, heard, source_socket='end', destination_socket='In2')
        b.connect_to_earlier_input(heard, settled, source_socket='Out1')
    else:
        b.connect(timer, settled)
    b.connect(broken, hide_retry)
    b.connect_to_earlier_output(settled, success)
    b.connect_to_earlier_output(hide_retry, retry)
    return phase_document(b, archive)


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
    from quest_compiler import phase_node
    b = PhaseGraphBuilder()
    start, end = input_node(b), output_node(b)
    fresh = fact_condition_node(b, 10, 'gq004_completed', comparison='Equal', value=0)
    b.connect(start, fresh)
    previous = fresh
    socket = 'Out'
    for index, stage in enumerate(spec.stages):
        if stage.id == 'ending':
            continue  # Optional texts cannot hold the quest open.
        if stage.id == 'recover':
            connect_call = audio_call(b, 60, 'StartCall')
            b.connect(previous, connect_call, source_socket=socket)
            previous, socket = connect_call, 'Out'
        if stage.id == 'return':
            hang_up = audio_call(b, 61, 'EndCall')
            b.connect(previous, hang_up, source_socket=socket)
            previous, socket = hang_up, 'Out'
        child = phase_node(b, 20 + index, stage.phase_resource)
        b.connect(previous, child, source_socket=socket, destination_socket='In1')
        previous, socket = child, 'Out1'
    # Retain the community/prefab after debrief. Completion is owned by the
    # independent finish root, so cleanup must not hold the journal open.
    away = trigger_condition_node(b, 40, '#gq004_tr_mood', 'IsOutside')
    release = community_action_node(b, 41, '#gq004_com_velvet', 'Deactivate')
    b.connect(previous, away, source_socket=socket)
    b.connect(away, release)
    b.connect_to_earlier_output(release, end)
    return phase_document(b, archive, phase_prefabs=spec.phase_prefabs)


def condition_branch(b, number, condition):
    return b.node(number, 'questConditionNodeDefinition', input_names=('In',),
                  output_names=('True', 'False'), properties={'condition': condition})


def fact_branch(b, number, name):
    kind = b.handles.wrap({'$type': 'questVarComparison_ConditionType', 'comparisonType': 'Equal',
                          'factName': name, 'value': 1})
    return condition_branch(b, number, b.handles.wrap({'$type': 'questFactsDBCondition', 'type': kind}))


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
    """Verify actual ownership, finish the quest, then send optional texts."""
    from quest_compiler import phase_node
    b = PhaseGraphBuilder()
    start, end = input_node(b), output_node(b)
    debrief = fact_condition_node(b, 10, 'gq004_debrief_done', comparison='Equal', value=1)
    settled = tick_delay(b, 11)
    # A condition branch queries current inventory, including items granted
    # before this root attached or before a pause listener subscribed.
    kind = b.handles.wrap({'$type': 'questInventory_ConditionType', 'comparisonType': 'GreaterOrEqual',
        'isPlayer': 1, 'itemID': tweakdbid('Items.GhostlineLoveHeartbreaker'),
        'itemTag': cname('None'), 'objectRef': entity_reference(), 'quantity': 1})
    owns = condition_branch(b, 12, b.handles.wrap({'$type': 'questObjectCondition', 'type': kind}))
    wait = inventory_condition_node(b, 13, 'Items.GhostlineLoveHeartbreaker')
    verified = fact_node(b, 14, 'gq004_reward_delivery_verified')
    granted = fact_node(b, 15, 'gq004_reward_granted')
    succeeded = quest_completion_node(b, 16, 'quests/minor_quest/gq004')
    completed = fact_node(b, 17, 'gq004_completed')
    delay = realtime_delay_node(b, 18, seconds=45)
    phone = phase_node(b, 19, r'mod\gq004\phases\gq004_ending.questphase')
    b.connect(start, debrief)
    b.connect(debrief, settled)
    b.connect(settled, owns)
    b.connect(owns, verified, source_socket='True')
    b.connect(owns, wait, source_socket='False')
    b.connect_to_earlier_input(wait, verified)
    b.connect(verified, granted)
    b.connect(granted, succeeded, destination_socket='Succeeded')
    b.connect(succeeded, completed)
    b.connect(completed, delay)
    b.connect(delay, phone, destination_socket='In1')
    b.connect_to_earlier_output(phone, end, source_socket='Out1')
    return phase_document(b, archive)


def reward_repair(archive):
    """Once-only inventory-verified migration for already completed saves."""
    b = PhaseGraphBuilder()
    start, end = input_node(b), output_node(b)
    completed = fact_condition_node(b, 10, 'gq004_completed', comparison='Equal', value=1)
    debrief = fact_condition_node(b, 11, 'gq004_debrief_done', comparison='Equal', value=1)
    def branch(number, condition):
        return b.node(number, 'questConditionNodeDefinition', input_names=('In',),
                      output_names=('True', 'False'), properties={'condition': condition})
    kind = b.handles.wrap({'$type': 'questVarComparison_ConditionType', 'comparisonType': 'Equal',
                          'factName': 'gq004_reward_delivery_verified', 'value': 1})
    verified = branch(12, b.handles.wrap({'$type': 'questFactsDBCondition', 'type': kind}))
    kind = b.handles.wrap({'$type': 'questInventory_ConditionType', 'comparisonType': 'GreaterOrEqual',
        'isPlayer': 1, 'itemID': tweakdbid('Items.GhostlineLoveHeartbreaker'),
        'itemTag': cname('None'), 'objectRef': entity_reference(), 'quantity': 1})
    owns = branch(13, b.handles.wrap({'$type': 'questObjectCondition', 'type': kind}))
    grant = add_item_node(b, 14, 'Items.GhostlineLoveHeartbreaker', 1)
    confirm = inventory_condition_node(b, 15, 'Items.GhostlineLoveHeartbreaker')
    mark = fact_node(b, 16, 'gq004_reward_delivery_verified')
    legacy = fact_node(b, 17, 'gq004_reward_granted')
    b.connect(start, completed)
    b.connect(completed, debrief)
    b.connect(debrief, verified)
    b.connect_to_earlier_output(verified, end, source_socket='True')
    b.connect(verified, owns, source_socket='False')
    b.connect(owns, mark, source_socket='True')
    b.connect(owns, grant, source_socket='False')
    b.connect(grant, confirm)
    b.connect_to_earlier_input(confirm, mark)
    b.connect(mark, legacy)
    b.connect_to_earlier_output(legacy, end)
    return phase_document(b, archive)
