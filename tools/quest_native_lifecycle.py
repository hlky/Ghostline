"""Native lifecycle builders extracted from GQ004; story resources are explicit bindings."""
from __future__ import annotations

from phase_graph import (
    PhaseGraphBuilder, input_node, output_node, objective_node, journal_entry_node,
    mappin_node, community_action_node, character_spawned_node, trigger_condition_node,
    fact_node, phase_document, realtime_delay_node, fact_condition_node,
    device_condition_node, device_manager_node, add_item_node, cname, entity_reference,
    tweakdbid, inventory_condition_node, quest_completion_node, logical_and_node,
    journal_path, node_ref,
)
from quest_encounter import scene_flow_node, character_attitude_group_node, character_mortality_node

def audio_call(b, number, phase, *, caller, addressee='contacts/player', prefab='#holocalls_studio'):
    """Native audio-call HUD; direct StartCall is supported by PhoneSystem."""
    kind = b.handles.wrap({'$type': 'questCallContact_NodeType',
        'caller': journal_path(b, caller, 'gameJournalContact', 1),
        'addressee': journal_path(b, addressee, 'gameJournalContact', 1),
        'phase': phase, 'mode': 'Audio', 'prefabNodeRef': node_ref(prefab),
        'applyPhoneRestriction': 0, 'isRejectable': 0, 'showAvatar': 0, 'visuals': 'Default'})
    return b.node(number, 'questPhoneManagerNodeDefinition', input_names=('In',), properties={'type': kind})


def meeting(stage, archive, *, setup_trigger, rearm_trigger, scene_origin,
            success_fact, protection_source, phase_prefabs=(), deferred_fact=None,
            resume_entry='resume', reward_item=None, reward_quantity=1,
            entry='start', accept_exit='job_accept', defer_exit='end'):
    """Protected community meeting; deferred entry resumes without a polling delay."""
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
        state='Invulnerable', source=protection_source)
    setup = trigger_condition_node(b, 15, setup_trigger, 'IsInside')
    scene = scene_flow_node(b, 16, dict(scene=stage.data['scene'], origin=scene_origin,
                                      entry=entry, exit=accept_exit, completion_exits=[defer_exit]))
    # Subscribe immediately: a delay before this condition misses a quick
    # step away and return. Reuse the actual choice radius, not the greeting.
    outside = trigger_condition_node(b, 26, rearm_trigger, 'IsOutside')
    done = objective_node(b, 18, stage.data['objective'])
    hide = mappin_node(b, 19, stage.data['mappin'])
    fact = fact_node(b, 20, success_fact)
    b.connect(start, objective, destination_socket='Active')
    b.connect(objective, description, destination_socket='Active')
    b.connect(description, pin, destination_socket='Active')
    for left, right in ((pin, spawn), (spawn, ready), (ready, friendly), (friendly, protect), (protect, setup)):
        b.connect(left, right)
    if deferred_fact is not None:
        returning = fact_branch(b, 28, deferred_fact)
        resume = scene_flow_node(b, 29, dict(scene=stage.data['scene'], origin=scene_origin,
            entry=resume_entry, exit=accept_exit, completion_exits=[defer_exit]))
        deferred = fact_node(b, 27, deferred_fact)
        b.connect(setup, returning)
        b.connect_to_earlier_input(returning, scene, source_socket='False', destination_socket=entry)
        b.connect(returning, resume, source_socket='True', destination_socket=resume_entry)
        b.connect(scene, deferred, source_socket=defer_exit)
        b.connect_to_earlier_input(resume, deferred, source_socket=defer_exit)
        b.connect_to_earlier_input(deferred, outside)
        b.connect_to_earlier_input(resume, done, source_socket=accept_exit, destination_socket='Succeeded')
    else:
        b.connect(setup, scene, destination_socket=entry)
        b.connect(scene, outside, source_socket=defer_exit)
    b.connect_to_earlier_input(outside, setup)
    b.connect(scene, done, source_socket=accept_exit, destination_socket='Succeeded')
    b.connect(done, hide, destination_socket='Inactive')
    b.connect(hide, fact)
    if reward_item is not None:
        reward = add_item_node(b, 21, reward_item, reward_quantity)
        b.connect(fact, reward)
        # The finish root verifies delivery after the transaction has settled.
        b.connect_to_earlier_output(reward, end)
    else:
        b.connect_to_earlier_output(fact, end)
    return phase_document(b, archive, phase_prefabs=phase_prefabs)


def progress(b, number, show, label, *, duration_seconds=5, bottom_text='Verifying transfer'):
    subtype = b.handles.wrap({'$type': 'questProgressBar_NodeType', 'duration': float(duration_seconds),
        'show': int(show), 'text': {'unk1': '0', 'value': label},
        'bottomText': {'unk1': '0', 'value': bottom_text}, 'type': 'Connection'})
    return b.node(number, 'questUIManagerNodeDefinition', input_names=('In',), properties={'type': subtype})


def tick_delay(b, number):
    ticks = b.handles.wrap({'$type': 'questTickDelay_ConditionType', 'tickCount': 2})
    condition = b.handles.wrap({'$type': 'questTimeCondition', 'type': ticks})
    return b.node(number, 'questPauseConditionNodeDefinition', input_names=('In',),
                  properties={'condition': condition})


def attempt(device, archive, label, *, duration_seconds=5, connected_scene=None, bottom_text='Verifying transfer'):
    """Terminating success/retry exits cancel the losing timer/listener branch."""
    if type(duration_seconds) is not int or duration_seconds <= 0:
        raise ValueError('Transfer duration_seconds must be a positive integer')
    b = PhaseGraphBuilder()
    start, success = input_node(b), output_node(b)
    retry = b.node(2, 'questOutputNodeDefinition', input_names=('In',), output_names=(),
                   properties={'socketName': cname('Retry'), 'type': 'Terminating'})
    arm = device_manager_node(b, 3, device, 'AccessPointControllerPS', 'QuestForcePersonalLinkUnderStrictQuestControl')
    connected = device_condition_node(b, 10, device, 'AccessPointControllerPS', 'IsPersonalLinkConnected')
    bar = progress(b, 11, True, label, duration_seconds=duration_seconds, bottom_text=bottom_text)
    timer = realtime_delay_node(b, 12, seconds=duration_seconds)
    broken = device_condition_node(b, 13, device, 'AccessPointControllerPS', 'IsPersonalLinkDisconnected')
    # Native HUD owns the successful outro. Hiding at the timer boundary races
    # its delayed progress callback and incorrectly plays the failed animation.
    settled = tick_delay(b, 14)
    hide_retry = progress(b, 15, False, label, duration_seconds=duration_seconds, bottom_text=bottom_text)
    b.connect(start, arm)
    b.connect(arm, connected)
    b.connect(connected, bar)
    b.connect(bar, timer)
    b.connect(bar, broken)
    if connected_scene is not None:
        # This scene belongs to the attempt: it starts with the actual plug-in
        # and a terminating retry cancels it along with the progress timer.
        brand = scene_flow_node(b, 16, connected_scene)
        heard = logical_and_node(b, 17, 2)
        b.connect(bar, brand, destination_socket=connected_scene['entry'])
        b.connect(timer, heard, destination_socket='In1')
        b.connect(brand, heard, source_socket=connected_scene['exit'], destination_socket='In2')
        b.connect_to_earlier_input(heard, settled, source_socket='Out1')
    else:
        b.connect(timer, settled)
    b.connect(broken, hide_retry)
    b.connect_to_earlier_output(settled, success)
    b.connect_to_earlier_output(hide_retry, retry)
    return phase_document(b, archive)


def transfer(stage, archive, *, attempt_resource, intro_scene=None,
             retry_scene=None, success_scene=None, phase_prefabs=()):
    """Native transfer envelope; scene/content ownership stays with the caller.

    The optional introduction finishes before arming the socket. A successful
    terminating attempt retires before forced unplug can reach its retry listener.
    """
    from quest_compiler import phase_node
    b = PhaseGraphBuilder()
    start, end = input_node(b), output_node(b)
    objective = objective_node(b, 10, stage.data['objective'])
    description = journal_entry_node(b, 11, stage.data['description_entry'], 'gameJournalQuestDescription', 2)
    pin = mappin_node(b, 12, stage.data['mappin'], disable_previous_mappins=True)
    enable = device_manager_node(b, 14, stage.data['device'], 'AccessPointControllerPS', 'ForceON')
    child = phase_node(b, 15, attempt_resource, outputs=('Out1', 'Retry'))
    b.connect(start, objective, destination_socket='Active')
    b.connect(objective, description, destination_socket='Active')
    b.connect(description, pin, destination_socket='Active')
    if intro_scene is not None:
        intro = scene_flow_node(b, 13, intro_scene)
        b.connect(pin, intro, destination_socket=intro_scene['entry'])
        b.connect_to_earlier_input(intro, enable, source_socket=intro_scene['exit'])
    else:
        b.connect(pin, enable)
    b.connect(enable, child, destination_socket='In1')
    if retry_scene is not None:
        retry = scene_flow_node(b, 17, retry_scene)
        b.connect(child, retry, source_socket='Retry', destination_socket=retry_scene['entry'])
        b.connect_to_earlier_input(retry, child, source_socket=retry_scene['exit'], destination_socket='In1')
    else:
        b.connect_to_earlier_input(child, child, source_socket='Retry', destination_socket='In1')
    connected = device_condition_node(b, 18, stage.data['device'], 'AccessPointControllerPS', 'IsPersonalLinkConnected')
    copied = fact_node(b, 19, stage.data['success_fact'])
    disconnect = device_manager_node(b, 20, stage.data['device'], 'AccessPointControllerPS', 'QuestForceDisconnectPersonalLink')
    disable = device_manager_node(b, 21, stage.data['device'], 'AccessPointControllerPS', 'ForceDisabled')
    retired = tick_delay(b, 22)
    done = objective_node(b, 50, stage.data['objective'])
    hide = mappin_node(b, 51, stage.data['mappin'])
    b.connect(child, connected, source_socket='Out1')
    b.connect(connected, copied)
    b.connect(copied, retired)
    b.connect_to_earlier_input(retired, disconnect)
    b.connect(disconnect, disable)
    b.connect(disable, done, destination_socket='Succeeded')
    b.connect(done, hide, destination_socket='Inactive')
    if success_scene is not None:
        success = scene_flow_node(b, 52, success_scene)
        b.connect(hide, success, destination_socket=success_scene['entry'])
        b.connect_to_earlier_output(success, end, source_socket=success_scene['exit'])
    else:
        b.connect_to_earlier_output(hide, end)
    return phase_document(b, archive, phase_prefabs=phase_prefabs)


def root(spec, archive, *, completed_fact, cleanup_trigger, cleanup_community,
         skipped_stages=(), call=None, guard_completed=True):
    """Retain community/prefab until departure; completion has a separate root."""
    from quest_compiler import phase_node
    if len(spec.stages) > 20:
        raise ValueError('Root supports at most twenty stage slots')
    b = PhaseGraphBuilder()
    start, end = input_node(b), output_node(b)
    fresh = (fact_branch(b, 10, completed_fact) if guard_completed else
             fact_condition_node(b, 10, completed_fact, comparison='Equal', value=0))
    b.connect(start, fresh)
    if guard_completed:
        b.connect_to_earlier_output(fresh, end, source_socket='True')
    previous = fresh
    socket = 'False' if guard_completed else 'Out'
    for index, stage in enumerate(spec.stages):
        if stage.id in skipped_stages:
            continue  # Optional texts cannot hold the quest open.
        if call is not None and stage.id == call['start_before']:
            connect_call = audio_call(b, 60, 'StartCall', caller=call['caller'], addressee=call.get('addressee', 'contacts/player'), prefab=call.get('prefab', '#holocalls_studio'))
            b.connect(previous, connect_call, source_socket=socket)
            previous, socket = connect_call, 'Out'
        if call is not None and stage.id == call['end_before']:
            hang_up = audio_call(b, 61, 'EndCall', caller=call['caller'], addressee=call.get('addressee', 'contacts/player'), prefab=call.get('prefab', '#holocalls_studio'))
            b.connect(previous, hang_up, source_socket=socket)
            previous, socket = hang_up, 'Out'
        child = phase_node(b, 20 + index, stage.phase_resource)
        b.connect(previous, child, source_socket=socket, destination_socket='In1')
        previous, socket = child, 'Out1'
    # Retain the community/prefab after debrief. Completion is owned by the
    # independent finish root, so cleanup must not hold the journal open.
    away = trigger_condition_node(b, 40, cleanup_trigger, 'IsOutside')
    release = community_action_node(b, 41, cleanup_community, 'Deactivate')
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


def finish_and_epilogue(archive, *, debrief_fact, reward_item, verified_fact,
                        granted_fact, quest_path, completed_fact, reward_quantity=1,
                        epilogue_phase=None, epilogue_delay_seconds=45, guard_completed=True):
    """Verify actual ownership, finish the quest, then send optional texts."""
    from quest_compiler import phase_node
    b = PhaseGraphBuilder()
    start, end = input_node(b), output_node(b)
    debrief = fact_condition_node(b, 10, debrief_fact, comparison='Equal', value=1)
    settled = tick_delay(b, 11)
    # A condition branch queries current inventory, including items granted
    # before this root attached or before a pause listener subscribed.
    kind = b.handles.wrap({'$type': 'questInventory_ConditionType', 'comparisonType': 'GreaterOrEqual',
        'isPlayer': 1, 'itemID': tweakdbid(reward_item),
        'itemTag': cname('None'), 'objectRef': entity_reference(), 'quantity': reward_quantity})
    owns = condition_branch(b, 12, b.handles.wrap({'$type': 'questObjectCondition', 'type': kind}))
    wait = inventory_condition_node(b, 13, reward_item, quantity=reward_quantity)
    verified = fact_node(b, 14, verified_fact)
    granted = fact_node(b, 15, granted_fact)
    succeeded = quest_completion_node(b, 16, quest_path)
    completed = fact_node(b, 17, completed_fact)
    if epilogue_phase is not None:
        delay = realtime_delay_node(b, 18, seconds=epilogue_delay_seconds)
        phone = phase_node(b, 19, epilogue_phase)
    if guard_completed:
        already_done = fact_branch(b, 20, completed_fact)
        b.connect(start, already_done)
        b.connect_to_earlier_output(already_done, end, source_socket='True')
        b.connect_to_earlier_input(already_done, debrief, source_socket='False')
    else:
        b.connect(start, debrief)
    b.connect(debrief, settled)
    b.connect(settled, owns)
    b.connect(owns, verified, source_socket='True')
    b.connect(owns, wait, source_socket='False')
    b.connect_to_earlier_input(wait, verified)
    b.connect(verified, granted)
    b.connect(granted, succeeded, destination_socket='Succeeded')
    b.connect(succeeded, completed)
    if epilogue_phase is not None:
        b.connect(completed, delay)
        b.connect(delay, phone, destination_socket='In1')
        b.connect_to_earlier_output(phone, end, source_socket='Out1')
    else:
        b.connect_to_earlier_output(completed, end)
    return phase_document(b, archive)


def reward_repair(archive, *, completed_fact, debrief_fact, verified_fact,
                  granted_fact, reward_item, reward_quantity=1):
    """Once-only inventory-verified migration for already completed saves."""
    b = PhaseGraphBuilder()
    start, end = input_node(b), output_node(b)
    completed = fact_condition_node(b, 10, completed_fact, comparison='Equal', value=1)
    debrief = fact_condition_node(b, 11, debrief_fact, comparison='Equal', value=1)
    def branch(number, condition):
        return b.node(number, 'questConditionNodeDefinition', input_names=('In',),
                      output_names=('True', 'False'), properties={'condition': condition})
    kind = b.handles.wrap({'$type': 'questVarComparison_ConditionType', 'comparisonType': 'Equal',
                          'factName': verified_fact, 'value': 1})
    verified = branch(12, b.handles.wrap({'$type': 'questFactsDBCondition', 'type': kind}))
    kind = b.handles.wrap({'$type': 'questInventory_ConditionType', 'comparisonType': 'GreaterOrEqual',
        'isPlayer': 1, 'itemID': tweakdbid(reward_item),
        'itemTag': cname('None'), 'objectRef': entity_reference(), 'quantity': reward_quantity})
    owns = branch(13, b.handles.wrap({'$type': 'questObjectCondition', 'type': kind}))
    grant = add_item_node(b, 14, reward_item, reward_quantity)
    confirm = inventory_condition_node(b, 15, reward_item, quantity=reward_quantity)
    mark = fact_node(b, 16, verified_fact)
    legacy = fact_node(b, 17, granted_fact)
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
