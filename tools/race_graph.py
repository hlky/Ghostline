"""Native race orchestration built from shared quest graph/lifetime primitives."""
from math import ceil
from phase_graph import (
    cname, entity_reference, fact_condition_node, fact_node,
    realtime_delay_node, trigger_condition_node, objective_node,
    quest_completion_node, add_item_node, local_player_reference,
)
from quest_block_builders import Signal, _instant
from quest_scope import OwnedScope, child_node, cut_node
from quest_types import CompiledStage
from quest_encounter import scene_flow_node
from race_lifecycle import checkpoint, restrictions, mortality, content_ready, stop_workspot
from race_lifecycle import health_drop, speeding, sandstorm, destroyed
from phase_graph import mappin_node, journal_path, logical_and_node


def race_poi(b, n, path):
    """Use MQ056's explicit racing POI journal-state operation."""
    return b.node(n,'questJournalNodeDefinition',input_names=('Active','Inactive'),properties={
        'type':b.handles.wrap({'$type':'questJournalQuestEntry_NodeType',
            'path':journal_path(b,path,'gameJournalPointOfInterestMappin',1),
            'sendNotification':0,'trackQuest':0,'version':'OptionalProperty','optional':0})})


def manager(b, n, kind, operation):
    return b.node(n,kind,input_names=('In',),properties={'type':b.handles.wrap(operation)})


def vehicle(b, n, operation):
    return manager(b,n,'questVehicleNodeDefinition',operation)


def show(b, n, ref, visible):
    return manager(b,n,'questWorldDataManagerNodeDefinition',{
        '$type':'questShowWorldNode_NodeType','objectRef':{'$type':'NodeRef','$storage':'string','$value':ref},
        'show':int(visible),'componentName':cname('None'),'isPlayer':0})


def enable_checkpoint(b, source, bindings, ref, *, finish=False):
    """Restore vanilla signs on every activation; quest areas own crossing."""
    source = b.chain(source,show,ref,True)
    if bindings.get('checkpoint_mode') != 'vanilla':
        return source
    # Do not route progress through a template device's persistent-state action.
    # World trigger areas own the counter, so the template trigger stays off.
    return b.chain(source,manager,'questEntityManagerNodeDefinition',{
        '$type':'questEntityManagerToggleComponent_NodeType','params':[
            {'$type':'questEntityManagerToggleComponent_NodeTypeParams',
             'objectRef':entity_reference(ref),'isPlayer':0,'componentName':cname(name),
             'enable':int(name != 'trigger')}
            for name in ('ui_front','ui_back','trigger')]})


def ui(b, n, mode, checkpoints, entrants):
    return b.node(n,'questEventManagerNodeDefinition',input_names=('In',),properties={
        'objectRef':entity_reference('#mounted_vehicle'),'managerName':'VehicleManager',
        'isObjectPlayer':0,'isUiEvent':0,
        'PSClassName':cname('VehicleComponentPS'),'componentName':cname('controller'),
        'event':b.handles.wrap({'$type':'VehicleRaceQuestEvent','mode':mode,
                              'maxCheckpoints':checkpoints,'maxPosition':entrants})})


def mounting(b, n, *, condition='OnMount', parent='#mounted_vehicle', child=None, player=True):
    params = {'$type':'questCharacterMount_ConditionType',
        'parentRef':parent if isinstance(parent,dict) else entity_reference(parent),
        'childRef':child or entity_reference('#player'),
        'childIsPlayer':bool(player),'condition':condition}
    if player:
        params['role'] = 'Driver'
    kind = b.handles.wrap(params)
    return b.node(n,'questPauseConditionNodeDefinition',input_names=('In',),properties={
        'condition':b.handles.wrap({'$type':'questCharacterCondition','type':kind})})


def spawned(b, n, community, entry=None, *, is_vehicle=False):
    ref = entity_reference(community,names=(entry,) if entry is not None else ())
    if is_vehicle and community == '#owned_vehicle' and entry is None:
        ref = {'$type':'gameEntityReference',
               'reference':{'$type':'NodeRef','$storage':'string','$value':'#owned_vehicle'}}
    kind = {'$type':'questVehicleSpawned_ConditionType','vehicleRef':ref} if is_vehicle else {
        '$type':'questCharacterSpawned_ConditionType','objectRef':ref,
        'comparisonParams':b.handles.wrap({'$type':'questComparisonParam','comparisonType':'Greater',
                                         'count':0,'entireCommunity':0})}
    condition = b.handles.wrap({'$type':'questVehicleCondition' if is_vehicle else 'questCharacterCondition',
                               'type':b.handles.wrap(kind)})
    return b.node(n,'questPauseConditionNodeDefinition',input_names=('In',),properties={'condition':condition})


def community(b, n, ref, action):
    return b.node(n,'questSpawnManagerNodeDefinition',input_names=('In',),properties={'actions':[{
        '$type':'questSpawnManagerNodeActionEntry','type':b.handles.wrap({
            '$type':'questCommunityTemplate_NodeType','action':action,'spawnerReference':{'$type':'NodeRef','$storage':'string','$value':ref},
            'communityEntryName':cname('None'),'communityEntryPhaseName':cname('default')})}]})


def area(b, n, ref, activator=None, outside=False):
    node = trigger_condition_node(b,n,ref,'IsOutside' if outside else 'IsInside')
    if activator:
        node.data['condition']['Data'].update(activatorRef=activator,isPlayerActivator=0)
    return node


def increment(b, n, name):
    node = fact_node(b,n,name)
    node.data['type']['Data']['setExactValue'] = 0
    return node


def fact_value(b, n, name, value):
    node = fact_node(b,n,name)
    node.data['type']['Data']['value'] = value
    return node


def fact_compare(b, n, name, comparison, value):
    return fact_condition_node(b,n,name,comparison=comparison,value=value)


def delay(b, n, seconds):
    milliseconds = round(seconds * 1000)
    return realtime_delay_node(b,n,seconds=milliseconds//1000,milliseconds=milliseconds%1000)


def flow_relay(b, number):
    return b.node(number,'questLogicalHubNodeDefinition',input_names=('In1',),
        output_names=('Out1',),properties={'inputSocketCount':1})


def warning(b, n, show_warning):
    return manager(b,n,'questUIManagerNodeDefinition',{
        '$type':'questWarningMessage_NodeType','message':'RETURN TO THE RACE',
        'localizedMessage':{'unk1':'0','value':'LocKey#78795' if show_warning else 'LocKey#78783'},
        'show':int(show_warning)})


def recovery_tooltip(b, number, enabled):
    return manager(b,number,'questUIManagerNodeDefinition',{
        '$type':'questShowCustomTooltip_NodeType','setTooltip':enabled,
        'text':{'unk1':'0','value':'LocKey#50189'},'inputAction':'Exit',
        'holdIndicationType':'Hold'})


def recovery_input(b, number, held=False):
    kind = 'questConditionNodeDefinition' if held else 'questPauseConditionNodeDefinition'
    return b.node(number,kind,input_names=('In',),
        output_names=('True','False') if held else ('Out',),properties={
            'condition':b.handles.wrap({'$type':'questSystemCondition','type':b.handles.wrap({
                '$type':'questInputAction_ConditionType','inputAction':cname('Exit'),
                'checkIfButtonAlreadyPressed':held})})})


def fade(b, n, fade_in):
    return manager(b,n,'questRenderFxManagerNodeDefinition',{
        '$type':'questSetFadeInOut_NodeType','fadeIn':int(fade_in),'duration':0})


def course_condition(b, n, bindings, outside):
    conditions = []
    for name,comparison,value in [('RacePlayerDistanceFromSpline','GreaterOrEqual' if outside else 'Less',
                                    50 if outside else 40)]:
        conditions.append(b.handles.wrap({'$type':'questFactsDBCondition','type':b.handles.wrap({
            '$type':'questVarComparison_ConditionType','factName':name,
            'comparisonType':comparison,'value':value})}))
    for ref in bindings['water_areas']:
        conditions.append(b.handles.wrap({'$type':'questTriggerCondition',
            'triggerAreaRef':{'$type':'NodeRef','$storage':'string','$value':ref},
            'activatorRef':entity_reference('#owned_vehicle'),'isPlayerActivator':0,
            'type':'IsInside' if outside else 'IsOutside'}))
    return b.node(n,'questPauseConditionNodeDefinition',input_names=('In',),properties={
        'condition':b.handles.wrap({'$type':'questLogicalCondition',
            'operation':'OR' if outside else 'AND','conditions':conditions})})


def race_environment(b, source, bindings, enable):
    for ref in bindings['crowd_null_areas']:
        source = b.chain(source,manager,'questCrowdManagerNodeDefinition',{
            '$type':'questCrowdManagerNodeType_EnableNullArea','areaReference':{
                '$type':'NodeRef','$storage':'string','$value':ref},'enable':int(enable)})
    source = b.chain(source,fact_value,'disable_combat_events',int(enable))
    return b.chain(source,fact_value,bindings['id']+'_environment_active',int(enable))


def variant(b, n, bindings, name, enabled):
    return manager(b,n,'questWorldDataManagerNodeDefinition',{
        '$type':'questTogglePrefabVariant_NodeType','params':[{
            '$type':'questTogglePrefabVariant_NodeTypeParams','prefabNodeRef':{
                '$type':'NodeRef','$storage':'string','$value':bindings['prefab']},
            'variantStates':[{'$type':'questVariantState','name':cname(name),'show':int(enabled)}]}]})


def quip(b, source, bindings, name, owned=None):
    available = b.watch(fact_compare,'mq056_johnny_talking','Equal',0)
    if owned is not None:
        owned.append(available.node)
    source = b.append(source,available)
    source = b.chain(source,fact_value,'mq056_johnny_talking',1)
    scene = b.watch(scene_flow_node,{'scene':bindings['result_scene'],
        'origin':bindings['activation'],'entry':name+'_in','exit':name+'_out'},socket=name+'_out')
    if owned is not None:
        owned.append(scene.node)
    source = b.append(source,scene,name+'_in')
    return b.chain(source,fact_value,'mq056_johnny_talking',0)


def drive(b, n, ref, spline, *, rubberband, driving_spline):
    racing = {'$type':'questvehicleRacingParams','splineRef':{'$type':'NodeRef','$storage':'string','$value':spline},
              'pushOtherVehiclesAside':False,'rubberBanding':True}
    racing['rubberBandingParam'] = b.handles.wrap({'$type':'questParamRubberbanding',
            'targetRef':local_player_reference(b),
            'minDistance':rubberband['min_distance'],'maxDistance':rubberband['max_distance'],
            'stayInFront':int(rubberband['stay_in_front']),'teleportToCatchUp':0,
            'targetForwardOffset':rubberband.get('target_forward_offset',0.0),'stopAndWait':0})
    return b.node(n,'questVehicleNodeCommandDefinition',input_names=('In',),output_names=('Success','Failure'),properties={
        'vehicle':ref,'commandParams':b.handles.wrap({'$type':'questVehicleCommandParams',
        'type':'Racing','additionalParamsRacing':b.handles.wrap(racing),
        'additionalParamsOnSpline':b.handles.wrap({'$type':'questvehicleOnSplineParams',
            'splineRef':{'$type':'NodeRef','$storage':'string','$value':driving_spline},
            'keepDistanceParam':b.handles.wrap({'$type':'questParamKeepDistance',
                'companionTargetRef':local_player_reference(b),'distance':10.0}),
            'rubberBanding':True,
            'rubberBandingParam':b.handles.wrap({'$type':'questParamRubberbanding',
                'targetRef':local_player_reference(b),'minDistance':20.0,
                'maxDistance':70.0,'teleportToCatchUp':True})}),
        'additionalParamsToNode':b.handles.wrap({'$type':'questvehicleToNodeParams',
            'portals':b.handles.wrap({'$type':'vehiclePortalsList'})}),
        **{key:b.handles.wrap({'$type':kind}) for key,kind in (
            ('additionalParamsChase','questvehicleChaseParams'),
            ('additionalParamsJoinTraffic','questvehicleJoinTrafficParams'),
            ('additionalParamsPanic','questvehiclePanicParams'),
            ('additionalParamsFollow','questvehicleFollowParams'))}})})


class RaceGraph(OwnedScope):
    @property
    def handles(self):
        return self.graph.handles

    def __init__(self, namespace, outputs=('success','failure','aborted')):
        super().__init__(CompiledStage(0,namespace,'race','ready','',{
            'inputs':{'start':'In1'},'outcomes':{key:key.title() for key in outputs}}))

    def branch(self, source, factory, *args):
        yes,no = _instant(self.node(factory,*args),self)
        self.connect(source,yes)
        return yes,no

    def chain(self, source, factory, *args, socket='Out'):
        return self.append(source,self.node(factory,*args,socket=socket))


def audio_mix(b, number, signpost):
    return b.node(number,'questAudioNodeDefinition',input_names=('In',),properties={
        'type':b.handles.wrap({'$type':'questAudioMixNodeType','mixSignpost':cname(signpost)})})


def crew_engine_audio(b, number, bindings, event):
    entrant = bindings['entrants'][min(2,len(bindings['entrants'])-1)]
    return manager(b,number,'questAudioNodeDefinition',{
        '$type':'questAudioEventNodeType','event':{'$type':'audioAudEventStruct','event':cname(event)},
        'objectRef':entity_reference(bindings['community'],names=(entrant['vehicle_entry'],))})


def remote_control(b, source, bindings, enabled):
    refs = [entity_reference(bindings['community'],names=(entrant['vehicle_entry'],))
            for entrant in bindings['entrants']]
    refs.append(entity_reference('#owned_vehicle'))
    ready = b.node(logical_and_node,len(refs),socket='Out1')
    for index,ref in enumerate(refs,1):
        changed = b.chain(source,vehicle,{'$type':'questSetCanVehicleBeRemoteControlled_NodeType',
            'vehicleRef':ref,'val':bool(enabled)})
        b.connect(changed,ready,'In'+str(index))
    return b.append(ready,b.watch(delay,0.2))


def health_below(b, number, percent):
    return b.node(number,'questConditionNodeDefinition',input_names=('In',),output_names=('True','False'),properties={
        'condition':b.handles.wrap({'$type':'questCharacterCondition','type':b.handles.wrap({
            '$type':'questCharacterHealth_ConditionType','objectRef':entity_reference('#mounted_vehicle'),
            'isPlayer':False,'comparisonType':'Less','percent':percent})})})


def nearby(b, number, ref, distance, pause=False, comparison='Less'):
    return b.node(number,'questPauseConditionNodeDefinition' if pause else 'questConditionNodeDefinition',
        input_names=('In',),output_names=('Out',) if pause else ('True','False'),properties={
        'condition':b.handles.wrap({'$type':'questDistanceCondition','type':b.handles.wrap({
            '$type':'questDistanceComparison_ConditionType','comparisonType':comparison,
            'distanceDefinition1':b.handles.wrap({'$type':'questObjectDistance',
                'entityRef':local_player_reference(b),'nodeRef2':ref}),
            'distanceDefinition2':b.handles.wrap({'$type':'questValueDistance','distanceValue':distance})})})})


def commentary_chance(b, number):
    return b.node(number,'questRandomizerNodeDefinition',input_names=('In',),output_names=('Out1','Out2'))


def community_entry(b, number, ref, entry, action, phase='default'):
    return b.node(number,'questSpawnManagerNodeDefinition',input_names=('In',),properties={
        'actions':[{'$type':'questSpawnManagerNodeActionEntry','type':b.handles.wrap({
            '$type':'questCommunityTemplate_NodeType','action':action,
            'spawnerReference':{'$type':'NodeRef','$storage':'string','$value':ref},
            'communityEntryName':cname(entry),'communityEntryPhaseName':cname(phase)})}]})


def camera_away(b, number, ref):
    return b.node(number,'questPauseConditionNodeDefinition',input_names=('In',),properties={
        'condition':b.handles.wrap({'$type':'questSystemCondition','type':b.handles.wrap({
            '$type':'questCameraFocus_ConditionType','objectRef':ref,
            'angleTolerance':180.0,'inverted':True})})})


def johnny_fx(b, number, bindings, effect):
    return b.node(number,'questFXManagerNodeDefinition',input_names=('In',),properties={
        'type':b.handles.wrap({'$type':'questPlayFX_NodeType','params':[
            {'$type':'questPlayFX_NodeTypeParams',
             'objectRef':entity_reference(bindings['crowd'],names=('johnny',)),
             'effectName':cname(effect)}]})})


def johnny_appearance(b, source, bindings):
    owned = []
    def wait(source, factory, *args, **kwargs):
        signal = b.watch(factory,*args,**kwargs)
        owned.append(signal.node)
        return b.append(source,signal)
    source = b.chain(source,community_entry,bindings['crowd'],'johnny','Activate')
    source = wait(source,spawned,bindings['crowd'],'johnny')
    johnny_spawned = source
    proximity = b.watch(nearby,entity_reference(bindings['crowd'],names=('johnny',)),4.0,True)
    owned.append(proximity.node)
    source = b.append(source,proximity)
    first,already = b.branch(source,fact_compare,'mq056_johnny_you_ready','Equal',0)
    first = b.chain(first,fact_value,'mq056_johnny_you_ready',1)
    first = quip(b,first,bindings,'you_ready',owned=owned)
    look = b.watch(camera_away,entity_reference(bindings['crowd'],names=('johnny',)))
    owned.append(look.node)
    b.connect(first,look)
    b.connect(already,look)
    # MQ056's everyone_mount input bypasses the camera-away wait when V sits.
    forced = b.watch(fact_compare,bindings['id']+'_everyone_mount','Greater',0)
    owned.append(forced.node)
    b.connect(johnny_spawned,forced)
    mount_request = b.node(fact_value,bindings['id']+'_johnny_mount_requested',1)
    b.connect(look,mount_request)
    b.connect(forced,mount_request)
    source = b.chain(b.once(mount_request),johnny_fx,bindings,'johnny_teleport_start')
    source = wait(source,spawned,'#owned_vehicle',is_vehicle=True)
    source = b.chain(source,vehicle,{'$type':'questAssignCharacter_NodeType',
        'characterRef':entity_reference(bindings['crowd'],names=('johnny',)),
        'vehicleRef':entity_reference('#owned_vehicle'),'slotName':cname('seat_front_right'),
        'isInstant':True})
    seated = b.watch(mounting,parent='#owned_vehicle',
        child=entity_reference(bindings['crowd'],names=('johnny',)),player=False)
    owned.append(seated.node)
    source = b.append(source,seated)
    b.chain(source,fact_value,bindings['id']+'_johnny_passenger',1)
    return owned


def winnings_bar(b, number):
    return b.node(number,'questUIManagerNodeDefinition',input_names=('In',),properties={
        'type':b.handles.wrap({'$type':'questProgressBar_NodeType','duration':2.5,
            'text':{'unk1':'0','value':'LocKey#95684'},'type':'Money'})})


def content_tokens(b, number, source, block):
    operation = {'$type':'questBlockTokenActivation_NodeSubType','source':cname(source)}
    if not block:
        operation['action'] = 'UnblockAll'
    return b.node(number,'questGameManagerNodeDefinition',input_names=('In',),properties={
        'type':b.handles.wrap({'$type':'questContentTokenManager_NodeType',
            'subtype':b.handles.wrap(operation)})})


def release_restrictions(b, number):
    return b.node(number,'questGameManagerNodeDefinition',input_names=('In',),properties={
        'type':b.handles.wrap({'$type':'questGameplayRestrictions_NodeType',
            'action':'RemoveAllRestrictions'})})


def resume_content(b, number):
    return b.node(number,'questGameManagerNodeDefinition',input_names=('In',),properties={
        'type':b.handles.wrap({'$type':'questContentTokenManager_NodeType',
            'subtype':b.handles.wrap({'$type':'questSpawnToken_NodeSubType'})})})


def population(b, number, ref, action):
    return b.node(number,'questSpawnManagerNodeDefinition',input_names=('In',),properties={
        'actions':[{'$type':'questSpawnManagerNodeActionEntry','type':b.handles.wrap({
            '$type':'questSpawner_NodeType','action':action,
            'spawnerReference':{'$type':'NodeRef','$storage':'string','$value':ref}})}]})


def forbidden(b, number, ref, active):
    return vehicle(b,number,{'$type':'questForbiddenTrigger_NodeType',
        'triggerNodeRef':{'$type':'NodeRef','$storage':'string','$value':ref},'activate':bool(active)})


def crate_loot(b, number, ref, table):
    return b.node(number,'questItemManagerNodeDefinition',input_names=('In',),properties={
        'type':b.handles.wrap({'$type':'questReInitContainers_NodeType','params':[
            {'$type':'questReInitContainers_NodeTypeParams',
             'containerNodeRef':{'$type':'NodeRef','$storage':'string','$value':ref},
             'lootTables':[{'$type':'TweakDBID','$storage':'uint64','$value':table}]}]})})


def population_spawned(b, number, ref):
    return b.node(number,'questPauseConditionNodeDefinition',input_names=('In',),properties={
        'condition':b.handles.wrap({'$type':'questCharacterCondition','type':b.handles.wrap({
            '$type':'questCharacterSpawned_ConditionType','objectRef':entity_reference(ref),
            'comparisonParams':b.handles.wrap({'$type':'questComparisonParam',
                'comparisonType':'Greater','entireCommunity':False})})})})


def courier_waiting(b, number, bindings):
    return b.node(number,'questUseWorkspotNodeDefinition',input_names=('In',),properties={
        'entityReference':entity_reference(bindings['courier']),
        'paramsV1':b.handles.wrap({'$type':'questUseWorkspotParamsV1',
            'workspotNode':{'$type':'NodeRef','$storage':'string',
                            '$value':bindings['courier_workspot']}})})


def crate_opened(b, number, ref):
    return b.node(number,'questPauseConditionNodeDefinition',input_names=('In',),properties={
        'condition':b.handles.wrap({'$type':'questObjectCondition','type':b.handles.wrap({
            '$type':'questInteraction_ConditionType','objectRef':{
                '$type':'NodeRef','$storage':'string','$value':ref},'eventType':'Executed'})})})


def join_traffic(b, number, ref):
    return b.node(number,'questVehicleNodeCommandDefinition',input_names=('In',),
        output_names=('Success','Failure'),properties={'vehicle':ref,
            'commandParams':b.handles.wrap({'$type':'questVehicleCommandParams','type':'Join Traffic',
                'additionalParamsJoinTraffic':b.handles.wrap({'$type':'questvehicleJoinTrafficParams'})})})


def reward_courier(b, source, bindings):
    ns,owned = bindings['id'],[]
    def wait(source, factory, *args, **kwargs):
        signal = b.watch(factory,*args,**kwargs)
        owned.append(signal.node)
        return b.append(source,signal)
    source = b.chain(source,fact_value,ns+'_cour_active',1)
    source = b.chain(source,variant,bindings,'crate',True)
    source = b.chain(source,variant,bindings,'vehicle_forbidden_courier',True)
    source = b.chain(source,forbidden,bindings['forbidden_courier'],True)
    source = b.append(source,b.node(mappin_node,bindings['reward_mappin']),'Active')
    # The player, not the motorcycle, enters the delivery area to prepare loot.
    delivered = wait(source,area,bindings['courier_trigger'])
    delivered = b.chain(delivered,crate_loot,bindings['reward_crate'],'68807470672')
    delivered = wait(delivered,delay,0.2)
    delivered = b.chain(delivered,crate_loot,bindings['reward_crate'],'127118606071')
    claimed = wait(delivered,crate_opened,bindings['reward_crate'])
    claimed = b.chain(claimed,increment,'vehicle_metaquest_discount')
    claimed = b.chain(claimed,fact_value,ns+'_reward_taken',1)
    claimed = b.append(claimed,b.node(mappin_node,bindings['reward_mappin']),'Inactive')
    claimed = b.append(claimed,b.node(objective_node,bindings['reward_objective']),'Succeeded')
    journal_done = wait(claimed,delay,1)
    b.append(journal_done,b.node(replay_journal,bindings['journal']),'Inactive')
    for ref in (bindings['courier'],bindings['courier_bike']):
        source = b.chain(source,population,ref,'Activate')
    source = wait(source,population_spawned,bindings['courier'])
    waiting = b.watch(courier_waiting,bindings)
    owned.append(waiting.node)
    b.connect(source,waiting)
    source = wait(source,spawned,bindings['courier_bike'],is_vehicle=True)
    ready = wait(source,delay,1)
    b.append(ready,b.node(objective_node,bindings['reward_objective']),'Active')
    # Pickup releases the courier's waiting performance, then remounts the bike.
    depart = wait(claimed,delay,2)
    cut = b.node(cut_node)
    depart = b.append(depart,cut)
    b.cut_targets(depart,[waiting.node])
    depart = b.chain(depart,vehicle,{'$type':'questAssignCharacter_NodeType',
        'characterRef':entity_reference(bindings['courier']),
        'vehicleRef':entity_reference(bindings['courier_bike'])})
    mounted = wait(depart,mounting,parent=bindings['courier_bike'],
        child=entity_reference(bindings['courier']),player=False)
    distant_mount = wait(depart,nearby,entity_reference(bindings['courier_bike']),100.0,True,'Greater')
    forced = b.chain(distant_mount,vehicle,{'$type':'questAssignCharacter_NodeType',
        'characterRef':entity_reference(bindings['courier']),
        'vehicleRef':entity_reference(bindings['courier_bike']),'isInstant':True})
    mounting_done = b.node(fact_value,ns+'_courier_mounted',1)
    b.connect(mounted,mounting_done)
    b.connect(forced,mounting_done)
    mounting_done = b.once(mounting_done)
    source = wait(mounting_done,delay,1)
    source = b.chain(source,forbidden,bindings['forbidden_courier'],False)
    command = b.watch(finish_drive,entity_reference(bindings['courier_bike']),bindings['courier_spline'],False)
    command.node.data['commandParams']['Data']['additionalParamsOnSpline']['Data']['needDriver'] = True
    owned.append(command.node)
    b.connect(source,command)
    leaving = b.watch(join_traffic,entity_reference(bindings['courier_bike']))
    owned.append(leaving.node)
    b.connect(Signal(command.node,'Success'),leaving)
    distant = wait(mounting_done,nearby,entity_reference(bindings['courier_bike']),150.0,True,'Greater')
    for ref in (bindings['courier'],bindings['courier_bike']):
        distant = b.chain(distant,population,ref,'Deactivate')
    distant = b.chain(distant,fact_value,ns+'_cour_active',0)
    distant = wait(distant,delay,0.2)
    b.chain(distant,fact_value,ns+'_courier_finished',1)
    return owned,ready


def attitude(b, number, ref, group):
    return b.node(number,'questCharacterManagerNodeDefinition',input_names=('In',),properties={
        'type':b.handles.wrap({'$type':'questCharacterManagerParameters_NodeType',
            'subtype':b.handles.wrap({'$type':'questCharacterManagerParameters_SetAttitudeGroupForPuppet',
                'puppetRef':ref,'groupName':cname(group)})})})


def passenger_reaction(b, number, ref):
    return b.node(number,'questCharacterManagerNodeDefinition',input_names=('In',),properties={
        'type':b.handles.wrap({'$type':'questCharacterManagerParameters_NodeType',
            'subtype':b.handles.wrap({'$type':'questCharacterManagerParameters_SetReactionPreset',
                'puppetRef':ref,'recordSelector':b.handles.wrap({
                    '$type':'questReactionPresetRecordSelector','gangerRecordID':{
                        '$type':'TweakDBID','$storage':'uint64','$value':'144575748405'}})})})})


def inject_threat(b, number, ref, target):
    return b.node(number,'questCombatNodeDefinition',input_names=('In',),properties={
        'entityReference':ref,'params':b.handles.wrap({'$type':'AIInjectCombatThreatCommandParams',
            'targetPuppetRef':target,'isPersistent':True})})


def finish_drive(b, number, ref, spline, stop, *, racing_spline=None):
    return b.node(number,'questVehicleNodeCommandDefinition',input_names=('In',),
        output_names=('Success','Failure'),properties={
            'vehicle':ref,'commandParams':b.handles.wrap({'$type':'questVehicleCommandParams',
                'type':'OnSpline','additionalParamsOnSpline':b.handles.wrap({
                    '$type':'questvehicleOnSplineParams','splineRef':{
                        '$type':'NodeRef','$storage':'string','$value':spline},
                    'pushOtherVehiclesAside':False,'stopAtEnd':bool(stop),
                    'keepDistanceParam':b.handles.wrap({'$type':'questParamKeepDistance',
                        'companionTargetRef':local_player_reference(b),'distance':10.0}),
                    'rubberBandingParam':b.handles.wrap({'$type':'questParamRubberbanding',
                        'targetRef':b.handles.wrap({'$type':'questUniversalRef','refLocalPlayer':False}),
                        'minDistance':20.0,'maxDistance':70.0})}),
                'additionalParamsRacing':b.handles.wrap({
                    '$type':'questvehicleRacingParams',
                    **({'pushOtherVehiclesAside':False,'splineRef':{
                        '$type':'NodeRef','$storage':'string','$value':racing_spline},
                        'rubberBanding':True,'rubberBandingParam':b.handles.wrap({
                            '$type':'questParamRubberbanding','targetRef':local_player_reference(b),
                            'minDistance':20.0,'maxDistance':80.0})} if racing_spline else {})}),
                'additionalParamsToNode':b.handles.wrap({'$type':'questvehicleToNodeParams',
                    'portals':b.handles.wrap({'$type':'vehiclePortalsList'})}),
                **{key:b.handles.wrap({'$type':kind}) for key,kind in (
                    ('additionalParamsChase','questvehicleChaseParams'),
                    ('additionalParamsJoinTraffic','questvehicleJoinTrafficParams'),
                    ('additionalParamsPanic','questvehiclePanicParams'),
                    ('additionalParamsFollow','questvehicleFollowParams'))}})})


def vehicle_out_of_view(b, number, ref, seconds=0.0):
    return b.node(number,'questPauseConditionNodeDefinition',input_names=('In',),properties={
        'condition':b.handles.wrap({'$type':'questSystemCondition','type':b.handles.wrap({
            '$type':'questCameraFocus_ConditionType','objectRef':ref,
            'onScreenTest':True,'useFrustrumCheck':True,'inverted':True,
            'timeInterval':seconds})})})


def finish_opponents(b, source, bindings):
    ns,community_ref = bindings['id'],bindings['community']
    owned = []
    source = b.chain(source,attitude,entity_reference(community_ref),'friendly')
    for entrant in bindings['entrants']:
        ref = entity_reference(community_ref,names=(entrant['vehicle_entry'],))
        finished,unfinished = b.branch(source,fact_compare,ns+'_'+entrant['id']+'_finished','Greater',0)
        continuing = b.watch(finish_drive,ref,bindings['spline'],False,
            racing_spline=bindings['driving_spline'])
        b.connect(unfinished,continuing)
        parking = b.watch(finish_drive,ref,bindings['finish_splines'][entrant['id']],True,
            racing_spline=bindings['driving_spline'])
        owned.extend((continuing.node,parking.node))
        b.connect(finished,parking)
        b.connect(Signal(continuing.node,'Success'),parking)
        wreck = b.watch(destroyed,ref)
        owned.append(wreck.node)
        b.connect(source,wreck)
        cut = b.node(cut_node)
        cut = b.append(wreck,cut)
        b.cut_targets(cut,[continuing.node,parking.node])
        respawn = b.chain(cut,vehicle,{'$type':'questAssignCharacter_NodeType',
            'characterRef':entity_reference(community_ref,names=(entrant['passenger_entry'],)),
            'vehicleRef':ref,'assign':False,'slotName':cname('seat_front_right'),'isInstant':True})
        pause = b.watch(delay,0.1)
        owned.append(pause.node)
        respawn = b.append(respawn,pause)
        for entry in (entrant['driver_entry'],entrant['passenger_entry'],entrant['vehicle_entry']):
            respawn = b.chain(respawn,community_entry,community_ref,entry,'Reactivate','finish')
        exists = b.watch(spawned,community_ref,entrant['vehicle_entry'],is_vehicle=True)
        owned.append(exists.node)
        respawn = b.append(respawn,exists)
        ticks = b.watch(tick_delay,5)
        owned.append(ticks.node)
        respawn = b.append(respawn,ticks)
        respawn = b.chain(respawn,vehicle,{'$type':'questSetImmovable_NodeType',
            'vehicleRef':ref})
        b.chain(respawn,vehicle,{'$type':'questToggleDoor_NodeType',
            'vehicleRef':ref,'doorAction':'DisableAllInteractions'})
    return owned


def tick_delay(b, number, ticks):
    return b.node(number,'questPauseConditionNodeDefinition',input_names=('In',),properties={
        'condition':b.handles.wrap({'$type':'questTimeCondition',
            'type':b.handles.wrap({'$type':'questTickDelay_ConditionType','tickCount':ticks})})})


def replay_journal(b, number, path):
    node = quest_completion_node(b,number,path)
    node.data['type']['Data']['version'] = 'OptionalProperty'
    return node


def finish_vehicle_health(b, source, namespace):
    damaged,healthy = b.branch(source,health_below,40.0)
    damaged = b.chain(damaged,manager,'questCharacterManagerNodeDefinition',{
        '$type':'questCharacterManagerCombat_NodeType',
        'subtype':b.handles.wrap({'$type':'questCharacterManagerCombat_ModifyHealth',
            'puppetRef':entity_reference('#mounted_vehicle'),'percent':40.0,
            'setExactValue':True,'noDamageIndicator':True})})
    merge = b.node(fact_value,namespace+'_vehicle_restored',1)
    b.connect(damaged,merge)
    b.connect(healthy,merge)
    return merge


def opponent_boarding(b, source, bindings):
    """Visible MQ056 boarding, with everyone_mount's instant fallback."""
    ns,ref = bindings['id'],bindings['community']
    owned,timed = [],[]
    def wait(signal, factory, *args):
        target = b.watch(factory,*args)
        owned.append(target.node)
        timed.append(target.node)
        return b.append(signal,target)
    def assign(signal, entrant, role, instant=False):
        return b.chain(signal,vehicle,{'$type':'questAssignCharacter_NodeType',
            'characterRef':entity_reference(ref,names=(entrant[role+'_entry'],)),
            'vehicleRef':entity_reference(ref,names=(entrant['vehicle_entry'],)),
            'slotName':cname('seat_front_left' if role=='driver' else 'seat_front_right'),
            'isInstant':instant})
    for index,entrant in enumerate(bindings['entrants']):
        if index==0:
            assign(source,entrant,'passenger')
            assign(wait(source,delay,5),entrant,'driver')
        elif index==1:
            fallback = wait(source,delay,50)
            fallback = assign(fallback,entrant,'passenger')
            assign(fallback,entrant,'driver')
        elif index==3:
            camera_gate = wait(source,delay,20)
            # Preserve MQ056's actual cross-team camera references.
            passenger = wait(camera_gate,vehicle_out_of_view,
                entity_reference(ref,names=(bindings['entrants'][1]['driver_entry'],)),3.0)
            assign(passenger,entrant,'passenger')
            driver = wait(camera_gate,vehicle_out_of_view,
                entity_reference(ref,names=(entrant['passenger_entry'],)),3.0)
            assign(driver,entrant,'driver')
        else:
            boarding = wait(source,delay,15 if index==4 else 7)
            boarding = assign(boarding,entrant,'driver')
            assign(boarding,entrant,'passenger')
    force = b.watch(fact_compare,ns+'_everyone_mount','Greater',0)
    owned.append(force.node)
    b.connect(source,force)
    cut = b.node(cut_node)
    instant = b.append(force,cut)
    b.cut_targets(instant,timed)
    for entrant in bindings['entrants']:
        instant = assign(instant,entrant,'driver',True)
        instant = assign(instant,entrant,'passenger',True)
    pause = b.watch(delay,2)
    owned.append(pause.node)
    instant = b.append(instant,pause)
    instant = b.chain(instant,crew_engine_audio,bindings,'sq024_race_01_engine_revs')
    b.chain(instant,fact_value,ns+'_opponents_mounted',1)
    return owned


def vehicle_trace(b, source, config, bindings, stage):
    """Side-channel probes; the race never waits for diagnostic delivery."""
    if not config.get('vehicle_diagnostics',False):
        return source
    for target in ('#player','#owned_vehicle'):
        probe = b.node(lambda graph,number: graph.node(number,'questEventManagerNodeDefinition',
            input_names=('In',),properties={
                'isObjectPlayer':target=='#player',
                'objectRef':entity_reference(target),
                'managerName':'None',
                'event':graph.handles.wrap({'$type':'AITaggedAIEvent',
                    'name':cname('ghostline_race_vehicle_trace'),
                    'tags':[cname(config['id']),cname(stage),cname(target)]})}))
        b.connect(source,probe)
    return source


def vehicle_destination_probe(b, source, config, bindings):
    if not config.get('vehicle_diagnostics',False):
        return
    condition = b.handles.wrap({'$type':'questDistanceCondition','type':b.handles.wrap({
        '$type':'questDistanceComparison_ConditionType','comparisonType':'Less',
        'distanceDefinition1':b.handles.wrap({'$type':'questObjectDistance',
            'entityRef':b.handles.wrap({'$type':'questUniversalRef','refLocalPlayer':False,
                'entityReference':entity_reference('#owned_vehicle')}),
            'nodeRef2':entity_reference(bindings['player_vehicle_spawn'])}),
        'distanceDefinition2':b.handles.wrap({'$type':'questValueDistance','distanceValue':3.0})})})
    probe = b.node(lambda graph,number: graph.node(number,'questConditionNodeDefinition',
        input_names=('In',),output_names=('True','False'),properties={'condition':condition}))
    b.connect(source,probe)
    vehicle_trace(b,Signal(probe.node,'True'),config,bindings,'destination_within_3m')
    vehicle_trace(b,Signal(probe.node,'False'),config,bindings,'destination_not_within_3m_or_unresolved')


def prepare_grid(b, source, config, bindings):
    """MQ056's phase-owned setup, called by the scene's fade_out exit."""
    ns, community_ref = config['id'], bindings['community']
    vehicle_trace(b,source,config,bindings,'before_despawn')
    source = b.chain(source,vehicle,{'$type':'questSpawnPlayerVehicle_NodeType',
        'despawn':True,'despawnAllEnabledVehicles':True,
        'positionRef':b.handles.wrap({'$type':'questUniversalRef','refLocalPlayer':False}),
        'vehicle':'Currently Active Car'})
    vehicle_trace(b,source,config,bindings,'despawn_output')
    source = b.chain(source,manager,'questTimeManagerNodeDefinition',
        {'$type':'questSetTime_NodeType','hours':3,'minutes':0,'seconds':0,'source':cname(ns)})
    source = b.chain(source,manager,'questTimeManagerNodeDefinition',
        {'$type':'questPauseTime_NodeType','pause':1,'source':cname(ns)})
    source = b.chain(source,manager,'questEnvironmentManagerNodeDefinition',
        {'$type':'questPlayEnv_SetWeather','weatherID':{
            '$type':'TweakDBID','$storage':'uint64','$value':'89407126858'},
            'blendTime':0.0,'source':cname(ns)})
    source = race_environment(b,source,bindings,True)
    source = b.append(source,b.watch(delay,0.5))
    vehicle_trace(b,source,config,bindings,'spawn_requested')
    # MQ056 forks here. Crowd actors and boarding are not fade-in gates.
    ready = b.node(logical_and_node,2,socket='Out1')
    # Match the native player-vehicle payloads, including their sparse entity
    # references. Only the authored destination differs from MQ056.
    spawn_ref = {'$type':'gameEntityReference',
        'reference':{'$type':'NodeRef','$storage':'string','$value':bindings['player_vehicle_spawn']}}
    owned_ref = {'$type':'gameEntityReference',
        'reference':{'$type':'NodeRef','$storage':'string','$value':'#owned_vehicle'}}
    player = b.chain(source,vehicle,{'$type':'questSpawnPlayerVehicle_NodeType',
        'positionRef':b.handles.wrap({'$type':'questUniversalRef','refLocalPlayer':False,
            'entityReference':spawn_ref}),
        'vehicle':'Currently Active Car'})
    vehicle_trace(b,player,config,bindings,'spawn_command_output')
    player = b.append(player,b.watch(spawned,'#owned_vehicle',is_vehicle=True))
    vehicle_trace(b,player,config,bindings,'spawn_condition_passed')
    player = b.chain(player,vehicle,{'$type':'questTeleport_NodeType',
        'entityReference':owned_ref,
        'params':{'$type':'questTeleportPuppetParams',
            'destinationRef':b.handles.wrap({'$type':'questUniversalRef',
                'refLocalPlayer':False,'entityReference':spawn_ref})}})
    vehicle_trace(b,player,config,bindings,'teleport_command_output')
    vehicle_destination_probe(b,player,config,bindings)
    player = b.chain(player,vehicle,{'$type':'questToggleDoor_NodeType',
        'vehicleRef':owned_ref,'doorAction':'DisableAllInteractions'})
    b.connect(player,ready,'In2')
    opponents = b.chain(source,variant,bindings,'barriers',True)
    opponents = b.chain(opponents,community,community_ref,'Activate')
    opponents = b.chain(opponents,community,bindings['crowd'],'Activate')
    vehicles_ready = b.node(logical_and_node,len(bindings['entrants']),socket='Out1')
    for index,entrant in enumerate(bindings['entrants'],1):
        exists = b.append(opponents,b.watch(spawned,community_ref,
            entrant['vehicle_entry'],is_vehicle=True))
        b.connect(exists,vehicles_ready,'In'+str(index))
    opponents = b.chain(vehicles_ready,community,community_ref,'ResetKillCount')
    for entrant in bindings['entrants']:
        opponents = b.chain(opponents,vehicle,{'$type':'questToggleDoor_NodeType',
            'vehicleRef':entity_reference(community_ref,names=(entrant['vehicle_entry'],)),
            'doorAction':'DisableAllInteractions'})
    b.connect(opponents,ready,'In1')
    audio = b.chain(source,variant,bindings,'race_crowd_finish',False)
    b.chain(audio,variant,bindings,'race_crowd_start',True)
    # Native setup joins the two vehicle branches, waits 200 ms, removes its
    # story-only Sampson entries, then waits one second before readiness.
    source = b.append(ready,b.watch(delay,0.2))
    source = b.append(source,b.watch(delay,1))
    source = b.chain(source,mortality,community_ref,ns,True)
    source = b.chain(source,attitude,entity_reference(bindings['crowd']),'friendly')
    source = b.chain(source,fact_value,ns+'_crowd_spawned',1)
    vehicle_trace(b,source,config,bindings,'preparation_ready')
    source = b.chain(source,fact_value,'radio_on',0)
    source = b.chain(source,variant,bindings,'vehicle_forbidden_start',True)
    vehicle_trace(b,source,config,bindings,'waiting_exclusion_streamed')
    source = b.chain(source,forbidden,bindings['forbidden_start'],False)
    vehicle_trace(b,source,config,bindings,'waiting_exclusion_disabled')
    for door in ('seat_front_left','seat_front_right'):
        source = b.chain(source,vehicle,{'$type':'questToggleDoor_NodeType',
            'vehicleRef':entity_reference('#owned_vehicle'),'doorAction':'EnableInteraction','door':door})
    source = remote_control(b,source,bindings,False)
    return source


def preparation(config, bindings, archive):
    ns = config['id']
    b = RaceGraph(ns+'_prepare',('success','aborted'))
    # Vanilla keeps the preparation phase alive after announcing grid readiness.
    # The parent lifecycle cuts this phase when the race attempt ends.
    b.outputs['success'].data['type'] = 'NonTerminating'
    source = b.chain(b.start,restrictions,ns,True)
    ready = prepare_grid(b,source,config,bindings)
    ready = b.chain(ready,restrictions,ns,True,'preparation')
    ready = b.chain(ready,content_tokens,ns,True)
    cancel = b.watch(fact_condition_node,ns+'_abort')
    b.connect(b.start,cancel)
    for outcome,signal in b.race({'success':ready,'aborted':cancel}).items():
        b.finish(signal,outcome)
    doc = b.document(archive)
    doc['Data']['RootChunk']['phasePrefabs'] = [{'$type':'questQuestPrefabEntry',
        'prefabNodeRef':{'$type':'NodeRef','$storage':'string','$value':bindings['prefab']}}]
    return doc


def attempt(config, bindings, archive):
    """One terminating activation owns countdown, checkpoints and finish waits."""
    ns, community_ref = config['id'], bindings['community']
    b = RaceGraph(ns,('success','failure','aborted','prevention'))
    source = b.start
    for name in ('progress','enemy_finish'):
        source = b.chain(source,fact_value,ns+'_'+name,0)
    for entrant in bindings['entrants']:
        source = b.chain(source,fact_value,ns+'_'+entrant['id']+'_finished',0)
    source = b.chain(source,fact_value,ns+'_inside_car',0)
    source = b.chain(source,fact_value,ns+'_countdown_end',0)
    source = b.chain(source,fact_value,'sq024_current_race_checkpoint_fact_add',0)
    source = b.chain(source,fact_value,'RacePlayerDistanceFromSpline',0)
    for visual in [*bindings['checkpoint_visuals'],bindings['finish_visual']]:
        source = b.chain(source,show,visual,False)
    # The parent phase already prepared the entire grid during fade_out.
    source = b.append(source,b.watch(mounting,parent='#owned_vehicle'))
    unmount = b.watch(mounting,parent='#owned_vehicle',condition='OnUnmount')
    b.connect(source,unmount)
    source = b.chain(source,fact_value,ns+'_everyone_mount',1)
    inside = b.append(source,b.watch(delay,2))
    inside = b.chain(inside,fact_value,ns+'_inside_car',1)
    b.chain(inside,fact_value,ns+'_countdown_requested',1)
    source = b.chain(source,checkpoint,ns,True)
    source = b.chain(source,mortality,'#player',ns,True,True)
    source = b.chain(source,mortality,'#mounted_vehicle',ns,True)
    source = b.append(source,b.node(objective_node,bindings['mount_objective']),'Succeeded')
    source = b.append(source,b.node(objective_node,bindings['countdown_objective']),'Active')
    source = b.chain(source,vehicle,{'$type':'questToggleForceBrake_NodeType',
        'vehicleRef':entity_reference('#mounted_vehicle'),'playerVehicle':1,'val':1})
    # MQ056 starts race initialization from the scene's countdown-start exit,
    # not from mounting and not from the later GO exit.
    source = b.append(source,b.watch(fact_compare,ns+'_countdown_started','Greater',0))
    source = b.chain(source,variant,bindings,'checkpoints',True)
    source = b.chain(source,variant,bindings,'checkpoints2',True)
    source = b.chain(source,variant,bindings,'gps_path',True)
    vehicle_trace(b,source,config,bindings,'course_enabled_before_race_init')
    source = b.chain(source,vehicle,{'$type':'questStartRace_NodeType'})
    vehicle_trace(b,source,config,bindings,'race_init_command_output')
    source = b.chain(source,manager,'questSceneManagerNodeDefinition',{'$type':'questSetTier_NodeType'})
    source = b.chain(source,audio_mix,'sq024_city_race_begin')
    source = b.chain(source,vehicle,{'$type':'questToggleDoor_NodeType',
        'vehicleRef':entity_reference('#mounted_vehicle'),'doorAction':'DisableAllInteractions'})
    source = b.chain(source,restrictions,ns,True,'mounted')
    source = b.append(source,b.watch(fact_compare,ns+'_opponents_mounted','Greater',0))
    source = b.append(source,b.watch(fact_compare,ns+'_countdown_end','Greater',0))
    source = b.chain(source,restrictions,ns,True,'countdown')
    source = b.chain(source,restrictions,ns,False,'preparation')
    # The scene's 4130 ms socket owns the journal and RaceStart handoff.
    go = b.chain(source,vehicle,{'$type':'questToggleForceBrake_NodeType',
        'vehicleRef':entity_reference('#mounted_vehicle'),'val':False})
    go = b.chain(go,crew_engine_audio,bindings,'sq024_race_04_engine_revs_stop_all')
    mortal = b.append(go,b.watch(delay,10))
    b.chain(mortal,mortality,community_ref,ns,False)
    veteran,hackable = b.branch(go,fact_compare,ns+'_won','Greater',2)
    remote_control(b,hackable,bindings,True)
    combat = b.append(go,b.watch(delay,3))
    for i,entrant in enumerate(bindings['entrants']):
        team = b.chain(combat,attitude,entity_reference(community_ref,
            names=(entrant['driver_entry'],entrant['passenger_entry'])),f'sq024_race_team_{i%5+1}')
        shooter = entity_reference(community_ref,names=(entrant['passenger_entry'],))
        team = b.chain(team,passenger_reaction,shooter)
        targets = [entity_reference('#player'),*[entity_reference(community_ref,
            names=(other['passenger_entry'],)) for other in bindings['entrants'] if other is not entrant]]
        for target in targets:
            b.connect(team,b.watch(inject_threat,shooter,target))
    commentary = b.append(go,b.watch(fact_compare,ns+'_johnny_passenger','Greater',0))
    commentary = b.append(commentary,b.watch(fact_compare,ns+'_countdown_end','Greater',0))
    health_ready = b.node(fact_value,ns+'_health_commentary_requested',1)
    for percent in (90.0,60.0,40.0):
        health = b.append(commentary,b.watch(health_drop,percent))
        b.connect(health,health_ready)
    quip(b,health_ready,bindings,'car_hp_drop')
    storm = b.append(commentary,b.watch(sandstorm))
    quip(b,storm,bindings,'sandstorm')
    speed = b.append(commentary,b.watch(delay,30))
    speed = b.append(speed,b.watch(speeding))
    heard,first = b.branch(speed,fact_compare,'mq056_johnny_speed_vo','Greater',0)
    chance = b.node(commentary_chance)
    b.connect(heard,chance)
    repeat = Signal(chance.node,'Out2')
    first = quip(b,first,bindings,'speeding')
    first = b.chain(first,fact_value,'mq056_johnny_speed_vo',1)
    quip(b,repeat,bindings,'speeding')
    wreck_ready = b.node(fact_value,ns+'_wrecked_nearby',1)
    quip(b,b.once(wreck_ready),bindings,'destroying_enemy')
    for entrant in bindings['entrants']:
        zero,prior = b.branch(go,fact_compare,ns+'_won','Equal',0)
        one,prior = b.branch(prior,fact_compare,ns+'_won','Equal',1)
        two,three = b.branch(prior,fact_compare,ns+'_won','Equal',2)
        for gate,maximum,offset in ((zero,150.0,0.0),(one,200.0,20.0),
                                    (two,300.0,50.0),(three,1000.0,80.0)):
            command = b.watch(drive,entity_reference(community_ref,names=(entrant['vehicle_entry'],)),
                bindings['spline'],driving_spline=bindings['driving_spline'],
                rubberband={'min_distance':20.0,'max_distance':maximum,
                    'stay_in_front':True,'target_forward_offset':offset})
            b.connect(gate,command)
        # MQ056 records each opponent's finish and commits a shared enemy flag.
        opponent = go
        ref = entity_reference(community_ref,names=(entrant['vehicle_entry'],))
        wrecked = b.watch(destroyed,ref)
        b.connect(commentary,wrecked)
        visible,_ = b.branch(wrecked,nearby,ref,50.0)
        chance = b.node(commentary_chance)
        b.connect(visible,chance)
        b.connect(Signal(chance.node,'Out1'),wreck_ready)
        opponent = b.append(opponent,b.watch(area,bindings['finish'],ref,outside=True))
        opponent = b.append(opponent,b.watch(area,bindings['finish'],ref))
        opponent = b.once(opponent)
        opponent = b.chain(opponent,fact_value,ns+'_'+entrant['id']+'_finished',1)
        b.chain(opponent,fact_value,ns+'_enemy_finish',1)
    progress = go
    for i,checkpoint_ref in enumerate(bindings['checkpoints'],1):
        progress = enable_checkpoint(b,progress,bindings,bindings['checkpoint_visuals'][i-1])
        if bindings.get('checkpoint_mode') == 'vanilla':
            # One ordered outside->inside crossing commits one absolute count.
            # The stock entity trigger is disabled, preventing a second writer.
            progress = b.append(progress,b.watch(area,checkpoint_ref,outside=True))
            progress = b.append(progress,b.watch(area,checkpoint_ref))
            progress = b.chain(progress,fact_value,'sq024_current_race_checkpoint_fact_add',i)
            b.chain(progress,manager,'questAudioNodeDefinition',{
                '$type':'questAudioEventNodeType','event':{'$type':'audioAudEventStruct',
                    'event':cname('sq024_race_countdown')},'objectRef':entity_reference('#player')})
        else:
            progress = b.append(progress,b.watch(fact_compare,
                'sq024_current_race_checkpoint_fact_add','GreaterOrEqual',i))
        progress = b.chain(progress,show,bindings['checkpoint_visuals'][i-1],False)
        progress = b.chain(progress,fact_value,ns+'_progress',i)
    progress = enable_checkpoint(b,progress,bindings,bindings['finish_visual'],finish=True)
    progress = b.append(progress,b.watch(area,bindings['finish'],outside=True))
    progress = b.append(progress,b.watch(area,bindings['finish']))
    if bindings.get('checkpoint_mode') == 'vanilla':
        progress = b.chain(progress,fact_value,'sq024_current_race_checkpoint_fact_add',
                           len(bindings['checkpoints'])+1)
    win,lose = b.branch(progress,fact_compare,ns+'_enemy_finish','Equal',0)
    routes = {'success':win,'failure':lose}
    cancel = b.watch(fact_condition_node,ns+'_abort')
    b.connect(b.start,cancel)
    # Separate terminal names retain the reason while first arrival retires all waits.
    police = b.watch(fact_compare,'wanted_level','GreaterOrEqual',3)
    b.connect(go,police)
    routes.update(aborted=cancel,unmounted=unmount,prevention=police)
    b.outputs['unmounted'] = b.outputs['aborted']
    off = b.watch(course_condition,bindings,True)
    b.connect(go,off)
    warned = b.chain(off,warning,True)
    grace = b.watch(delay,2)
    b.connect(warned,grace)
    returned = b.watch(course_condition,bindings,False)
    b.connect(warned,returned)
    reset = b.node(cut_node)
    reset.node.data['permanent'] = 0
    reset = b.append(returned,reset)
    b.cut_targets(reset,[grace.node])
    cleared = b.chain(reset,warning,False)
    b.graph.connect_to_earlier_input(cleared.node,off.node,source_socket=cleared.socket)
    recover = b.node(cut_node)
    recover.node.data['permanent'] = 0
    recover = b.append(grace,recover)
    # Native Exit is manual return-to-race recovery, with a 350 ms hold.
    manual = b.append(go,b.watch(delay,5))
    manual = b.chain(manual,recovery_tooltip,True)
    pressed = b.watch(recovery_input)
    b.connect(manual,pressed)
    held = b.append(pressed,b.watch(delay,0.35))
    confirmed,released = b.branch(held,recovery_input,True)
    b.connect(confirmed,recover)
    b.graph.connect_to_earlier_input(released.node,pressed.node,source_socket=released.socket)
    b.cut_targets(recover,[returned.node,grace.node,off.node])
    recover = b.chain(recover,fade,False)
    recover = b.append(recover,b.watch(delay,0.1))
    recover = b.chain(recover,vehicle,{'$type':'questGoBackToRace_NodeType'})
    recover = b.append(recover,b.watch(delay,1))
    recover = b.chain(recover,vehicle,{'$type':'questRepair_NodeType',
        'vehicleRef':entity_reference('#mounted_vehicle')})
    recover = b.chain(recover,fade,True)
    recover = b.chain(recover,warning,False)
    course_rearm = b.append(recover,b.node(flow_relay,socket='Out1'),'In1')
    input_rearm = b.append(recover,b.node(flow_relay,socket='Out1'),'In1')
    b.graph.connect_to_earlier_input(course_rearm.node,off.node,source_socket=course_rearm.socket)
    b.graph.connect_to_earlier_input(input_rearm.node,pressed.node,source_socket=input_rearm.socket)
    for outcome,selected in b.race(routes).items():
        b.finish(selected,outcome)
    doc = b.document(archive)
    doc['Data']['RootChunk']['phasePrefabs'] = [{'$type':'questQuestPrefabEntry','prefabNodeRef':{'$type':'NodeRef','$storage':'string','$value':bindings['prefab']}}]
    return doc


def staging_lifecycle(b, source, bindings):
    """MQ056's post-standup area watch; race start retires this branch."""
    owned = []
    def wait(signal, factory, *args, **kwargs):
        target = b.watch(factory,*args,**kwargs)
        owned.append(target.node)
        return b.append(signal,target)
    source = wait(source,area,bindings['staging_exit'])
    source = b.chain(source,manager,'questSceneManagerNodeDefinition',{
        '$type':'questSetTier_NodeType','tier':'Tier2_StagedGameplay'})
    source = wait(source,area,bindings['staging_exit'],outside=True)
    source = b.chain(source,manager,'questSceneManagerNodeDefinition',{'$type':'questSetTier_NodeType'})
    source = b.append(source,b.node(journal_state,bindings['journal']+'/race','gameJournalQuestPhase'),'Inactive')
    source = b.chain(source,community_entry,bindings['crowd'],'johnny','Deactivate')
    source = wait(source,delay,0.2)
    source = b.append(source,b.node(replay_journal,bindings['journal']),'Inactive')
    return source,owned


def journal_state(b, number, path, class_name):
    node = replay_journal(b,number,path)
    node.data['type']['Data']['path']['Data']['className'] = cname(class_name)
    return node


def prevention_failure(b, source, bindings):
    """Native police failure's warning, mortality and 200 ms handoff."""
    source = b.chain(source,variant,bindings,'checkpoints',False)
    source = b.chain(source,variant,bindings,'checkpoints2',False)
    source = b.chain(source,manager,'questUIManagerNodeDefinition',{
        '$type':'questWarningMessage_NodeType','localizedMessage':{'unk1':'0','value':'LocKey#95051'},
        'duration':5.0,'show':True,'instant':True})
    source = b.chain(source,mortality,'#player',bindings['id'],False,True)
    source = b.chain(source,mortality,'#mounted_vehicle',bindings['id'],False)
    source = b.chain(source,fact_value,bindings['id']+'_prevention_fail',1)
    source = b.chain(source,audio_mix,'sq024_city_race_finish')
    source = b.append(source,b.node(journal_state,bindings['journal']+'/race','gameJournalQuestPhase'),'Inactive')
    return b.append(source,b.watch(delay,0.2))


def prevention_unseen(b, number, ref):
    return b.node(number,'questPauseConditionNodeDefinition',input_names=('In',),properties={
        'condition':b.handles.wrap({'$type':'questSystemCondition','type':b.handles.wrap({
            '$type':'questCameraFocus_ConditionType','objectRef':ref,'inverted':True})})})


def prevention_global_restore(b, source, bindings):
    """MQ056's global restoration precedes the city cleanup by two seconds."""
    ns = bindings['id']
    source = b.chain(source,release_restrictions)
    source = b.chain(source,content_tokens,ns,False)
    source = b.chain(source,mortality,'#player',ns,False,True)
    for group in ('grid','preparation','mounted','countdown'):
        source = b.chain(source,restrictions,ns,False,group)
    source = b.chain(source,manager,'questTimeManagerNodeDefinition',
        {'$type':'questPauseTime_NodeType','pause':0,'source':cname(ns)})
    source = b.chain(source,manager,'questEnvironmentManagerNodeDefinition',
        {'$type':'questPlayEnv_SetWeather','reset':True,'blendTime':30.0,'source':cname(ns)})
    source = b.chain(source,fact_value,'radio_on',1)
    source = b.append(source,b.watch(delay,2))
    return b.append(source,b.node(replay_journal,bindings['journal']),'Inactive')


def prevention_opponents(b, source, bindings):
    """Let the crews leave in traffic before the native cleanup/timeout."""
    ns,community_ref = bindings['id'],bindings['community']
    owned = []
    def wait(signal, factory, *args, **kwargs):
        target = b.watch(factory,*args,**kwargs)
        owned.append(target.node)
        return b.append(signal,target)
    traffic = wait(source,delay,1)
    camera = wait(source,delay,30)
    timeout = wait(source,delay,300)
    all_gone = b.node(logical_and_node,len(bindings['entrants']),socket='Out1')
    for index,entrant in enumerate(bindings['entrants'],1):
        ref = entity_reference(community_ref,names=(entrant['vehicle_entry'],))
        command = b.watch(join_traffic,ref)
        owned.append(command.node)
        b.connect(traffic,command)
        distant = wait(source,nearby,ref,200.0,True,'Greater')
        unseen = wait(camera,prevention_unseen,ref)
        retire = b.node(fact_value,ns+'_'+entrant['id']+'_retired',1)
        b.connect(distant,retire)
        b.connect(unseen,retire)
        retired = b.once(retire)
        for role in ('vehicle_entry','driver_entry','passenger_entry'):
            retired = b.chain(retired,community_entry,community_ref,entrant[role],'Deactivate')
        b.connect(retired,all_gone,'In'+str(index))
    departed = wait(all_gone,delay,1)
    complete = b.node(community,community_ref,'Deactivate')
    for selected in b.race({'departed':departed,'timeout':timeout},owned=owned).values():
        b.connect(selected,complete)
    complete = b.chain(complete,community,bindings['crowd'],'Deactivate')
    b.chain(complete,fact_value,ns+'_police_cleanup_done',1)


def lifecycle(config, bindings, archive, attempt_depot):
    ns = config['id']
    b = RaceGraph(ns,('done',))
    done = b.start
    already,fresh = b.branch(done,fact_compare,ns+'_settled','Greater',0)
    poi = b.node(race_poi,bindings['activation_poi'])
    already = b.append(already,poi,'Inactive')
    b.finish(already,'done')
    poi = b.node(race_poi,bindings['activation_poi'])
    source = b.append(fresh,poi,'Active')
    source = b.chain(source,fact_value,ns+'_result',0)
    source = b.chain(source,fact_value,ns+'_abort',0)
    source = b.chain(source,fact_value,ns+'_standup',0)
    source = b.chain(source,fact_value,ns+'_inside_car',0)
    source = b.chain(source,fact_value,ns+'_countdown_requested',0)
    source = b.chain(source,fact_value,ns+'_countdown_started',0)
    source = b.chain(source,fact_value,ns+'_countdown_end',0)
    source = b.chain(source,fact_value,ns+'_johnny_passenger',0)
    source = b.chain(source,fact_value,ns+'_everyone_mount',0)
    source = b.chain(source,fact_value,ns+'_opponents_mounted',0)
    source = b.chain(source,fact_value,ns+'_prevention_fail',0)
    source = b.chain(source,fact_value,ns+'_police_cleanup_done',0)
    for entrant in bindings['entrants']:
        source = b.chain(source,fact_value,ns+'_'+entrant['id']+'_retired',0)
    source = b.chain(source,fact_value,ns+'_reward_delivered',0)
    source = b.chain(source,fact_value,ns+'_reward_taken',0)
    source = b.chain(source,fact_value,ns+'_courier_finished',0)
    source = b.chain(source,fact_value,ns+'_courier_mounted',0)
    source = b.chain(source,fact_value,ns+'_save_unlocked',0)
    approach = b.watch(area,bindings['staging'])
    source = b.append(source,b.node(replay_journal,bindings['journal']),'Active')
    source = b.append(source,b.node(objective_node,bindings['activation_objective']),'Active')
    source = b.append(source,b.node(mappin_node,bindings['activation_mappin']),'Active')
    source = b.append(source,approach)
    source = b.chain(source,fact_value,ns+'_crowd_spawned',0)
    approach_outside = b.watch(area,bindings['staging'],outside=True)
    b.connect(source,approach_outside)
    activation = b.watch(scene_flow_node,{'scene':bindings['activation_scene'],
        'origin':bindings['activation'],'entry':ns+'_waiting_in','exit':ns+'_waiting_out',
        'completion_exits':['fade_out']})
    source = b.append(source,activation,ns+'_waiting_in')
    # Leaving before Wait only retires this interaction. Re-entry creates a
    # fresh scene activation without settling the race or starting cooldown.
    approach_cut = b.node(cut_node)
    approach_cut.node.data['permanent'] = 0
    leaving = b.append(approach_outside,approach_cut)
    b.cut_targets(leaving,[activation.node])
    approach_pause = b.watch(delay,0.2)
    leaving = b.append(leaving,approach_pause)
    b.graph.connect_to_earlier_input(leaving.node,approach.node,source_socket=leaving.socket)
    accepted_cut = b.node(cut_node)
    accepted_cut.node.data['permanent'] = 0
    accepted = b.append(Signal(activation.node,'fade_out'),accepted_cut)
    b.cut_targets(accepted,[approach_outside.node,approach_pause.node])
    preparing = b.watch(child_node,bindings['preparation_phase'],'In1',('Success','Aborted'))
    preparing.node.data['phaseInstancePrefabs'] = [{
        '$type':'questQuestPrefabEntry',
        'prefabNodeRef':{'$type':'NodeRef','$storage':'string','$value':bindings['prefab']}}]
    b.connect(accepted,preparing,'In1')
    appearance = johnny_appearance(b,accepted,bindings)
    source = Signal(activation.node,ns+'_waiting_out')
    boarding = opponent_boarding(b,source,bindings)
    staging_left,staging_targets = staging_lifecycle(b,source,bindings)
    source = b.append(source,b.node(mappin_node,bindings['activation_mappin']),'Inactive')
    source = b.append(source,b.node(objective_node,bindings['activation_objective']),'Succeeded')
    poi = b.node(race_poi,bindings['activation_poi'])
    source = b.append(source,poi,'Inactive')
    source = b.append(source,b.node(objective_node,bindings['mount_objective']),'Active')
    source = b.chain(source,manager,'questJournalNodeDefinition',{
        '$type':'questJournalTrackQuest_NodeType',
        'path':b.handles.wrap({'$type':'gameJournalPath',
            'realPath':bindings['mount_objective'],'fileEntryIndex':2,
            'className':cname('gameJournalQuestObjective')})})
    countdown = b.watch(scene_flow_node,{'scene':bindings['countdown_scene'],
        'origin':bindings['activation'],'entry':'announcer_in','exit':'countdown_go',
        'additional_entries':['countdown_in'],'completion_exits':['announcer_out','countdown_started']})
    announcer_wait = b.watch(delay,1)
    b.connect(source,announcer_wait)
    b.connect(announcer_wait,countdown,'announcer_in')
    countdown_request = b.watch(fact_compare,ns+'_countdown_requested','Greater',0)
    b.connect(source,countdown_request)
    b.connect(countdown_request,countdown,'countdown_in')
    staging_cut = b.append(Signal(countdown.node,'countdown_started'),b.node(cut_node))
    b.cut_targets(staging_cut,staging_targets)
    b.chain(staging_cut,fact_value,ns+'_countdown_started',1)
    call = b.watch(child_node,attempt_depot,'In1',('Success','Failure','Aborted','Prevention'))
    call.node.data['phaseInstancePrefabs'] = [{
        '$type':'questQuestPrefabEntry',
        'prefabNodeRef':{'$type':'NodeRef','$storage':'string','$value':bindings['prefab']}}]
    b.connect(source,call,'In1')
    outcomes = [('success',Signal(call.node,'Success'),1),('failure',Signal(call.node,'Failure'),2),
                ('aborted',Signal(call.node,'Aborted'),3),
                ('prevention',Signal(call.node,'Prevention'),2),
                ('preparation_aborted',Signal(preparing.node,'Aborted'),3),
                ('staging_left',staging_left,3)]
    for name,source,value in outcomes:
        retire = b.node(cut_node)
        source = b.append(source,retire)
        b.cut_targets(source,[activation.node,preparing.node,call.node,countdown.node,
                              countdown_request.node,announcer_wait.node,approach.node,
                              approach_outside.node,approach_pause.node])
        b.cut_targets(source,appearance)
        b.cut_targets(source,boarding)
        b.cut_targets(source,staging_targets)
        police_failure = name=='prevention'
        if police_failure:
            source = prevention_failure(b,source,bindings)
            source = prevention_global_restore(b,source,bindings)
            prevention_opponents(b,source,bindings)
        source = b.append(source,b.node(mappin_node,bindings['activation_mappin']),'Inactive')
        source = b.append(source,b.node(race_poi,bindings['activation_poi']),'Inactive')
        for objective in ('activation_objective','mount_objective','countdown_objective'):
            source = b.append(source,b.node(objective_node,bindings[objective]),'Inactive')
        # A mounted vehicle uses a workspot too. Stopping V's workspot here
        # breaks the seated animation without unmounting the vehicle.
        if name in ('preparation_aborted','staging_left'):
            stop = b.node(stop_workspot)
            b.connect(source,stop)
        for visual in [*bindings['checkpoint_visuals'],bindings['finish_visual']]:
            source = b.chain(source,show,visual,False)
        source = b.chain(source,vehicle,{'$type':'questToggleForceBrake_NodeType',
            'vehicleRef':entity_reference('#owned_vehicle'),'val':False})
        source = b.chain(source,ui,'RaceEnd',len(bindings['checkpoints'])+1,len(bindings['entrants'])+1)
        source = b.chain(source,vehicle,{'$type':'questStopRace_NodeType'})
        source = b.chain(source,audio_mix,'sq024_city_race_finish')
        source = b.chain(source,crew_engine_audio,bindings,'sq024_race_04_engine_revs_stop_all')
        source = b.chain(source,ui,'Disable',len(bindings['checkpoints'])+1,len(bindings['entrants'])+1)
        # Normal finishes release restrictions after three seconds in parallel
        # with the result scenes. Aborted attempts still release immediately.
        normal_finish = name in ('success','failure')
        restrictions_done = b.append(source,b.watch(delay,3)) if normal_finish else source
        if not police_failure:
            for restriction_group in ('grid','preparation','mounted','countdown'):
                restrictions_done = b.chain(restrictions_done,restrictions,ns,False,restriction_group)
            restrictions_done = b.chain(restrictions_done,release_restrictions)
        if normal_finish:
            save_ready = b.node(logical_and_node,3,socket='Out1')
            b.connect(restrictions_done,save_ready,'In1')
            unlocked = b.append(save_ready,b.watch(delay,1))
            unlocked = b.chain(unlocked,checkpoint,ns,False)
            b.chain(unlocked,fact_value,ns+'_save_unlocked',1)
        elif not police_failure:
            source = b.chain(restrictions_done,checkpoint,ns,False)
        if not police_failure:
            source = b.chain(source,mortality,'#player',ns,False,True)
        source = b.chain(source,mortality,'#mounted_vehicle',ns,False)
        source = b.chain(source,mortality,bindings['community'],ns,False)
        if name in ('success','failure'):
            source = finish_vehicle_health(b,source,ns)
        source = remote_control(b,source,bindings,True)
        source = b.chain(source,warning,False)
        source = b.chain(source,recovery_tooltip,False)
        source = b.chain(source,fact_value,'mq056_johnny_talking',0)
        source = b.chain(source,fact_value,'sq024_current_race_checkpoint_fact_add',0)
        source = b.chain(source,fact_value,'RacePlayerDistanceFromSpline',0)
        source = b.chain(source,manager,'questSceneManagerNodeDefinition',{'$type':'questSetTier_NodeType'})
        source = b.chain(source,fade,True)
        source = b.chain(source,vehicle,{'$type':'questToggleDoor_NodeType',
            'vehicleRef':entity_reference('#owned_vehicle'),'doorAction':'ResetInteractions'})
        for door in ('seat_front_left','seat_front_right'):
            source = b.chain(source,vehicle,{'$type':'questToggleDoor_NodeType',
                'vehicleRef':entity_reference('#owned_vehicle'),'doorAction':'ForceUnlock','door':door})
            source = b.chain(source,vehicle,{'$type':'questToggleDoor_NodeType',
                'vehicleRef':entity_reference('#owned_vehicle'),'doorAction':'EnableInteraction','door':door})
        if not police_failure:
            source = b.chain(source,manager,'questTimeManagerNodeDefinition',
                {'$type':'questPauseTime_NodeType','pause':0,'source':cname(ns)})
            source = b.chain(source,manager,'questEnvironmentManagerNodeDefinition',
                {'$type':'questPlayEnv_SetWeather','reset':True,'blendTime':30.0,'source':cname(ns)})
        if name in ('success','failure'):
            # This branch is independent of pickup, courier departure and VO.
            left_finish = b.append(source,b.watch(area,bindings['end_area'],outside=True))
            left_finish = b.chain(left_finish,fact_value,'disable_combat_events',0)
            finish_handoff = b.node(logical_and_node,2,socket='Out1')
            b.connect(left_finish,finish_handoff,'In1')
        finish_targets = []
        if name in ('success','failure'):
            if 'forbidden_finish' in bindings:
                source = b.chain(source,variant,bindings,'vehicle_forbidden_finish',True)
            finish_targets = finish_opponents(b,source,bindings)
            # Reward collection/departure can remain pending indefinitely.
            # Retire race crews as soon as the player leaves the finish area.
            retire = b.append(left_finish,b.watch(delay,0.5))
            retire = b.append(retire,b.node(cut_node))
            b.cut_targets(retire,finish_targets)
            b.chain(retire,community,bindings['community'],'Deactivate')
            source = b.chain(source,variant,bindings,'race_crowd_start',False)
            source = b.chain(source,variant,bindings,'race_crowd_finish',True)
        elif not police_failure:
            source = b.chain(source,community,bindings['community'],'Deactivate')
        for variant_name in bindings['variants']:
            if variant_name not in ('barriers','crate','race_crowd_start','race_crowd_finish') and not variant_name.startswith('vehicle_forbidden_'):
                source = b.chain(source,variant,bindings,variant_name,False)
        source = b.append(source,b.node(objective_node,bindings['objective']),
                          'Succeeded' if name=='success' else 'Failed')
        if name=='failure':
            journal_closed = b.append(source,b.watch(delay,1))
            b.append(journal_closed,b.node(replay_journal,bindings['journal']),'Inactive')
            b.connect(source,save_ready,'In3')
        if name=='success':
            courier_targets,courier_ready = reward_courier(b,source,bindings)
            b.connect(courier_ready,save_ready,'In3')
            payment = b.append(source,b.watch(delay,2))
            payment = b.chain(payment,winnings_bar)
            payment = b.append(payment,b.watch(delay,2.5))
            payment = b.chain(payment,add_item_node,config['reward']['item'],config['reward']['quantity'])
            payment = b.chain(payment,increment,ns+'_won')
            b.chain(payment,fact_value,ns+'_reward_delivered',1)
        if name in ('success','failure'):
            entry = 'win' if name=='success' else 'lose'
            source = quip(b,source,bindings,entry)
            source = b.append(source,b.watch(delay,1))
            source = quip(b,source,bindings,'johnny_'+entry)
        if name in ('success','failure'):
            source = b.append(source,b.watch(delay,2))
            source = b.chain(source,johnny_fx,bindings,'johnny_spawn_normal')
            source = b.append(source,b.watch(delay,1))
        source = b.chain(source,community_entry,bindings['crowd'],'johnny','Deactivate')
        if normal_finish:
            b.connect(source,save_ready,'In2')
        if name=='success':
            source = b.append(source,b.watch(fact_compare,ns+'_reward_delivered','Greater',0))
            source = b.append(source,b.watch(fact_compare,ns+'_reward_taken','Greater',0))
            source = b.append(source,b.watch(fact_compare,ns+'_courier_finished','Greater',0))
        if name in ('success','failure'):
            # MQ056 latches the first exit independently, then joins it with
            # Johnny/courier completion after the half-second phase handoff.
            handoff = b.append(source,b.watch(delay,0.5))
            b.connect(handoff,finish_handoff,'In2')
            source = finish_handoff
            cleanup_cut = b.node(cut_node)
            source = b.append(source,cleanup_cut)
            b.cut_targets(source,finish_targets+ (courier_targets if name=='success' else []))
            source = b.chain(source,community,bindings['community'],'Deactivate')
        if not police_failure:
            source = b.chain(source,community,bindings['crowd'],'Deactivate')
        for ref in (bindings['courier'],bindings['courier_bike']):
            source = b.chain(source,population,ref,'Deactivate')
        source = b.chain(source,variant,bindings,'crate',False)
        for role in ('start','finish','courier'):
            if 'forbidden_'+role not in bindings:
                continue
            source = b.chain(source,forbidden,bindings['forbidden_'+role],False)
            source = b.chain(source,variant,bindings,'vehicle_forbidden_'+role,False)
        source = b.chain(source,variant,bindings,'barriers',False)
        source = b.chain(source,variant,bindings,'race_crowd_start',False)
        source = b.chain(source,variant,bindings,'race_crowd_finish',False)
        source = race_environment(b,source,bindings,False)
        if not police_failure:
            source = b.chain(source,content_tokens,ns,False)
        source = b.chain(source,resume_content)
        source = b.chain(source,fact_value,'radio_on',1)
        source = b.chain(source,fact_value,ns+'_result',value)
        source = b.chain(source,fact_value,ns+'_abort',0)
        complete = b.node(replay_journal,bindings['journal'])
        source = b.append(source,complete,'Inactive')
        source = b.chain(source,fact_value,ns+'_settled',1)
        if normal_finish:
            source = b.append(source,b.watch(area,bindings['cleanup_area'],outside=True))
            # The checkpoint remains independent of the cleanup-area exit.
            source = b.append(source,b.watch(fact_compare,ns+'_save_unlocked','Greater',0))
        if police_failure:
            source = b.append(source,b.watch(delay,0.5))
            source = b.append(source,b.watch(fact_compare,ns+'_police_cleanup_done','Greater',0))
            source = b.chain(source,checkpoint,ns,False)
        b.finish(source,'done')
    doc = b.document(archive)
    doc['Data']['RootChunk']['phasePrefabs'] = [{'$type':'questQuestPrefabEntry','prefabNodeRef':{'$type':'NodeRef','$storage':'string','$value':bindings['prefab']}}]
    return doc


def root(config, bindings, archive, lifecycle_depot):
    """Initial and replay availability have no timed delay."""
    ns = config['id']
    b = RaceGraph(ns+'_availability',())
    ready = b.watch(content_ready)
    b.connect(b.start,ready)
    fresh = b.chain(ready,fact_value,ns+'_settled',0)
    run = b.watch(child_node,lifecycle_depot,'In1',('Done',))
    run.node.data['phaseInstancePrefabs'] = [{
        '$type':'questQuestPrefabEntry',
        'prefabNodeRef':{'$type':'NodeRef','$storage':'string','$value':bindings['prefab']}}]
    b.connect(fresh,run,'In1')
    b.graph.connect_to_earlier_input(run.node,ready.node,source_socket='Done')
    return b.document(archive)
