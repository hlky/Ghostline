"""Construct race resources directly from typed RED fields and race inputs."""
from pathlib import Path

from generate_scene import (
    HandleAllocator, build_choice_option, build_loc_store, build_resource_refs,
    build_start_node, build_use_workspot_node, build_stop_workspot_node,
    cname, deterministic_event_id, empty_entity_ref, fnv1a64, node_ref,
    output_socket, resource_path, scene_node_id, scene_time, tweakdbid,
)


def typed(kind, **fields):
    return {'$type': kind, **fields}


def document(root, archive):
    return {'Header': {'WolvenKitVersion': '8.17.4', 'WKitJsonVersion': '0.0.9',
        'GameVersion': 2310, 'ExportedDateTime': '1970-01-01T00:00:00Z',
        'DataType': 'CR2W', 'ArchiveFileName': str(Path(archive).resolve())},
        'Data': {'Version': 195, 'BuildVersion': 0, 'RootChunk': root, 'EmbeddedFiles': []}}


def transform(z=0, backwards=False):
    return typed('WorldTransform',
        Orientation=typed('Quaternion', i=0, j=0, k=int(backwards), r=int(not backwards)),
        Position=typed('WorldPosition', **{
            axis: typed('FixedPoint', Bits=round((z if axis == 'z' else 0)*131072))
            for axis in 'xyz'}))


def choice(node_id, target, option_id, caption, mode, alloc, *, object_ref=None, display_name=''):
    world_attached = mode in ('attachToWorld', 'attachToGameObject')
    node = typed('scnChoiceNode', nodeId=scene_node_id(node_id), ffStrategy='automatic',
        mode=mode, interruptCapability='Interruptable',
        displayNameOverride=display_name if world_attached else '',
        localizedDisplayNameOverride={'unk1':'0','value':''},
        shapeParams=alloc.wrap(typed('scnInteractionShapeParams', preset='small',
            offset=typed('Vector3', X=0, Y=0, Z=0),
            rotation=typed('Quaternion', i=0, j=0, k=0, r=1),
            customIndicationRange=0, customActivationRange=0, activationYawLimit=360,
            activationBaseLength=1, activationHeight=3)) if world_attached else None,
        lookAtParams=alloc.wrap(typed('scnChoiceNodeNsBasicLookAtParams', slotName=cname('(Root)'),
            offset=typed('Vector3', X=0, Y=0, Z=0)))
            if world_attached else None,
        mappinParams=alloc.wrap(typed('scnChoiceNodeNsMappinParams',
            locationType='Interaction' if world_attached else 'None',
            mappinSettings=tweakdbid('183169082076', 'uint64') if world_attached else tweakdbid(0, 'uint64'))),
        ataParams=typed('scnChoiceNodeNsAttachToActorParams',
            actorId=typed('scnActorId', id=4294967295), visualizerStyle='onScreen'),
        atpParams=typed('scnChoiceNodeNsAttachToPropParams',
            propId=typed('scnPropId', id=4294967295), visualizerStyle='inWorld'),
        atgoParams=typed('scnChoiceNodeNsAttachToGameObjectParams',
            nodeRef=node_ref(object_ref) if object_ref else node_ref(0, 'uint64'), visualizerStyle='onScreen'),
        atsParams=typed('scnChoiceNodeNsAttachToScreenParams'),
        atwParams=typed('scnChoiceNodeNsAttachToWorldParams', customEntityRadius=0,
            entityPosition=typed('Vector3', X=0, Y=0, Z=0.82 if world_attached else 0),
            entityOrientation=typed('Quaternion', i=0, j=0, k=0, r=1),
            visualizerStyle='onScreen'),
        customPersistentLine=typed('scnscreenplayItemId', id=4294967040),
        interruptionSpeakerOverride=typed('scnActorId', id=4294967295),
        persistentLineEvents=[], options=[build_choice_option(
            {'caption': caption, 'choice_type': 257 if world_attached else 1}, option_id)],
        outputSockets=[output_socket(0, 0, [(target, 0, 0)]),
                       *[output_socket(i, 0, []) for i in range(1, 7)]])
    if world_attached:
        node['options'][0]['bluelineCondition'] = alloc.wrap(typed('questPaymentCondition',
            type=alloc.wrap(typed('questPaymentFixedAmount_ConditionType',
                scriptCondition=alloc.wrap(typed('PaymentFixedAmount_ScriptConditionType',
                    payAmount=2000))))))
        node['options'][0]['iconTagIds'] = [tweakdbid('119896558755','uint64')]
        node['options'][0]['questCondition'] = alloc.wrap(typed('questLogicalCondition', operation='AND', conditions=[
            alloc.wrap(typed('questCharacterCondition', type=alloc.wrap(typed('questCharacterMount_ConditionType',
                anyParent=1, childIsPlayer=1, childRef=empty_entity_ref('#player', 'string'),
                parentRef=empty_entity_ref(), condition='OnUnmount')))),
            alloc.wrap(typed('questCharacterCondition', type=alloc.wrap(typed('questCharacterCombat_ConditionType',
                inverted=1, isPlayer=1, objectRef=empty_entity_ref('#player', 'string')))))
        ]))
    return alloc.wrap(node)


def section(namespace, node_id, target, duration, output_name, alloc, *, restoring=False,
            extra_events=(), extra_routes=None, emit_exit=True):
    events = list(extra_events)
    if restoring:
        events.append(typed('scneventsCameraParamsEvent', startTime=1501, duration=1000,
            cameraOverrideSettings=typed('scneventsCameraOverrideSettings',
                overrideDof=0, overrideFov=0, resetDof=1, resetFov=1),
            isPlayerCamera=1, targetActor=typed('scnPerformerId', id=4294967040),
            targetSlot=cname('Chest'), fovValue=51, fovWeigh=1))
        events.append(typed('scnGameplayTransitionEvent', startTime=2632, duration=0,
            performer=typed('scnPerformerId', id=1), vehState='IdleStand'))
    if emit_exit:
        events.append(typed('scneventsSocket', startTime=duration-1, duration=0,
            osockStamp=typed('scnOutputSocketStamp', name=output_name, ordinal=0)))
    routes = {output_name:(target,1), **(extra_routes or {})}
    for index, event in enumerate(events):
        event.update(id=typed('scnSceneEventId', id=deterministic_event_id(namespace, node_id, index)),
            executionTagFlags=0,
            scalingData=alloc.wrap(typed('scnScalingData_KeepRelationWithOtherEvents',
                groupRfrncNdspaceEndtime=scene_time(duration), groupRfrncNdspaceStarttime=scene_time(0))))
    return alloc.wrap(typed('scnSectionNode', nodeId=scene_node_id(node_id), ffStrategy='automatic',
        actorBehaviors=[typed('scnSectionInternalsActorBehavior',
            actorId=typed('scnActorId', id=0), behaviorMode='OnlyIfAlive')],
        events=[alloc.wrap(event) for event in events], sectionDuration=scene_time(duration),
        outputSockets=[output_socket(i, 0, [(routes[i][0],0,routes[i][1])] if i in routes else [])
                       for i in range(max(routes)+1)]))


def activation(config, archive, bindings):
    """Own the entire interaction graph; derive registries from created nodes."""
    ns = config['id']
    alloc = HandleAllocator(1)
    # Actor IDs index the combined NPC/player table. This scene has no NPCs,
    # so V occupies slot zero and performer 1 (actor ID * 256 + 1).
    player = typed('scnPlayerActorDef', actorId=typed('scnActorId', id=0),
        playerName='Player', acquisitionPlan='findInContext', specAppearance=cname('default'),
        specCharacterRecordId=tweakdbid('Character.Player_Puppet_Base'), specTemplate=cname('(None)'),
        voicetagId=typed('scnVoicetagId', id='1103967280742240864'),
        lipsyncAnimSet=typed('scnLipsyncAnimSetSRRefId', id=0),
        findActorInContextParams=typed('scnFindEntityInContextParams', contextualName='Player',
            contextActorName=cname('None'), forceMaxVisibility=0,
            specRecordId=tweakdbid('Character.Player_Puppet_Base'), voiceVagId=typed('scnVoicetagId', id='0')),
        **{name: [] for name in ('animSets', 'bodyCinematicAnimSets', 'cyberwareAnimSets',
            'cyberwareCinematicAnimSets', 'deformationAnimSets', 'dynamicAnimSets',
            'facialAnimSets', 'facialCinematicAnimSets')})
    graph = [build_start_node(55, [{'node_id': 119}], alloc),
        choice(119, 121, 2, 'wait', 'attachToWorld', alloc, display_name=config['title']),
        section(ns, 121, 125, 2600, 3, alloc,
            extra_events=[typed('scneventsSocket',startTime=2001,duration=0,
                osockStamp=typed('scnOutputSocketStamp',name=2,ordinal=0))],
            extra_routes={2:(164,1)})]
    # MQ056: glitch -> 600 ms -> fade_out notification; the phase prepares
    # the grid, then the scene's readiness fact -> 2 seconds -> fade-in.
    # Standing waiting uses a scene tier instead of the vanilla chair.
    from generate_scene import (build_render_fade_node, build_realtime_delay_node,
                                build_quest_node_base, add_quest_sockets)
    # MQ056 starts its Money progress bar in parallel with the wait section.
    graph[1]['Data']['outputSockets'][0]['destinations'].extend(
        output_socket(0,0,[(199,0,1)])['destinations'])
    data, quest = build_quest_node_base(199,'questUIManagerNodeDefinition',
        ['CutDestination','In'],['Out'],[],alloc)
    quest['type'] = alloc.wrap(typed('questProgressBar_NodeType',duration=2.0,
        text={'unk1':'0','value':'LocKey#83354'},type='Money'))
    add_quest_sockets(quest,['CutDestination','In'],['Out'],alloc)
    graph.append(alloc.wrap(data))
    from generate_scene import build_scene_tier_node
    # Standing waiting has no seated animation/workspot handoff. Hold V in
    # the scene tier directly, and release it at the Start choice below.
    graph.append(build_scene_tier_node({'node_id':125,
        'tier':'Tier2_StagedGameplay','force_empty_hands':True}, alloc))
    def glitch(node_id, target, ordinal):
        data, quest = build_quest_node_base(node_id,'questFXManagerNodeDefinition',
            ['CutDestination','In'],['Out'],[{'node_id':target,'input_ordinal':ordinal}],alloc)
        quest['type'] = alloc.wrap(typed('questPlayFX_NodeType',params=[
            typed('questPlayFX_NodeTypeParams',objectRef=empty_entity_ref('#player','string'),
                  isPlayer=1,effectName=cname('fast_travel_glitch'))]))
        add_quest_sockets(quest,['CutDestination','In'],['Out'],alloc)
        return alloc.wrap(data)
    graph.append(glitch(164,129,1))
    graph.append(build_realtime_delay_node({'node_id':129,'milliseconds':600,
        'on_out':[{'node_id':127,'input_ordinal':1}]},alloc))
    graph.append(build_render_fade_node({'node_id':127, 'fade_in':False,
        'duration_seconds':0, 'on_out':[{'node_id':97}, {'node_id':101}]},alloc))
    graph.append(alloc.wrap(typed('scnEndNode',nodeId=scene_node_id(97),
        ffStrategy='automatic',outputSockets=[],type='NonTerminating')))
    graph.append(section(ns,101,99,1750,0,alloc,emit_exit=False,
        extra_events=[
            typed('scneventsSocket',startTime=510,duration=0,
                osockStamp=typed('scnOutputSocketStamp',name=2,ordinal=0)),
            typed('scneventsCameraParamsEvent',startTime=750,duration=1000,
                fovValue=40,dofIntensity=1,dofFarBlur=2,dofFarFocus=1,isPlayerCamera=1,
                cameraOverrideSettings=typed('scneventsCameraOverrideSettings',overrideDof=0),
                targetSlot=cname('Chest'))],extra_routes={2:(111,1)}))
    graph.append(build_scene_tier_node({'node_id':111,
        'tier':'Tier2_StagedGameplay','force_empty_hands':True}, alloc))
    data, quest = build_quest_node_base(99,'questPauseConditionNodeDefinition',
        ['CutDestination','In'],['Out'],[{'node_id':140,'input_ordinal':1}],alloc)
    quest['condition'] = alloc.wrap(typed('questFactsDBCondition',type=alloc.wrap(
        typed('questVarComparison_ConditionType',factName=ns+'_crowd_spawned',
              comparisonType='Greater',value=0))))
    add_quest_sockets(quest,['CutDestination','In'],['Out'],alloc)
    graph.append(alloc.wrap(data))
    graph.append(build_realtime_delay_node({'node_id':140,'seconds':2,
        'on_out':[{'node_id':146,'input_ordinal':1}]},alloc))
    # Restore the surveyed standing pose while black, before revealing the grid.
    from generate_scene import build_teleport_player_node
    graph.append(build_teleport_player_node({'node_id':146,
        'destination_ref':bindings['activation'],
        'on_out':[{'node_id':138,'input_ordinal':1},
                  {'node_id':142,'input_ordinal':1}]},alloc))
    graph.append(build_realtime_delay_node({'node_id':142,'seconds':2,
        'on_out':[{'node_id':144,'input_ordinal':1}]},alloc))
    data, quest = build_quest_node_base(144,'questUIManagerNodeDefinition',
        ['CutDestination','In'],['Out'],[],alloc)
    quest['type'] = alloc.wrap(typed('questShowOnscreen_NodeType',
        localizedMessage={'unk1':'0','value':'LocKey#77682'}))
    add_quest_sockets(quest,['CutDestination','In'],['Out'],alloc)
    graph.append(alloc.wrap(data))
    graph.append(build_render_fade_node({'node_id':138,'fade_in':True,
        'duration_seconds':0,'on_out':[{'node_id':168,'input_ordinal':1}]},alloc))
    graph.append(glitch(168,151,0))
    graph.extend([choice(151, 154, 258, 'start', 'attachToScreen', alloc),
        section(ns,154,172,3133,3,alloc,restoring=True,
            extra_events=[typed('scneventsSocket',startTime=3132,duration=0,
                osockStamp=typed('scnOutputSocketStamp',name=4,ordinal=0))],
            extra_routes={4:(158,1)})])
    graph.append(build_scene_tier_node({'node_id':158,
        'tier':'Tier1_FullGameplay'}, alloc))
    data, quest = build_quest_node_base(172,'questFactsDBManagerNodeDefinition',
        ['CutDestination','In'],['Out'],[{'node_id':161}],alloc)
    quest['type'] = alloc.wrap(typed('questSetVar_NodeType',factName=ns+'_standup',
        value=1,setExactValue=1))
    add_quest_sockets(quest,['CutDestination','In'],['Out'],alloc)
    graph.extend([alloc.wrap(data), alloc.wrap(typed('scnEndNode', nodeId=scene_node_id(161),
        ffStrategy='automatic', outputSockets=[], type='Terminating'))])
    options = {'wait': {'string_id': str(fnv1a64(ns+':wait')), 'text': '[Wait for the race]'},
               'start': {'string_id': str(fnv1a64(ns+':start')), 'text': '[Start the race]'}}
    root = typed('scnSceneResource', version=5, cookingPlatform='PLATFORM_PC', sceneCategoryTag='minorQuests',
        actors=[], playerActors=[player],
        entryPoints=[typed('scnEntryPoint', name=cname(ns+'_waiting_in'), nodeId=scene_node_id(55))],
        exitPoints=[typed('scnExitPoint', name=cname('fade_out'), nodeId=scene_node_id(97)),
                    typed('scnExitPoint', name=cname(ns+'_waiting_out'), nodeId=scene_node_id(161))],
        sceneGraph=alloc.wrap(typed('scnSceneGraph', graph=graph,
            **{key: [node['Data']['nodeId'] for node in graph if node['Data']['$type'] == kind]
               for key, kind in [('startNodes', 'scnStartNode'), ('endNodes', 'scnEndNode')]})),
        screenplayStore=typed('scnscreenplayStore', lines=[], options=[
            typed('scnscreenplayChoiceOption', itemId=typed('scnscreenplayItemId', id=item_id),
                locstringId=typed('scnlocLocstringId', ruid=options[key]['string_id']),
                usage=typed('scnscreenplayOptionUsage', playerGenderMask=typed('scnGenderMask', mask=3)))
            for key, item_id in [('wait', 2), ('start', 258)]]),
        locStore=build_loc_store({'name': ns, 'choice_line_order': list(options)}, options),
        resouresReferences=build_resource_refs({'actors': [{'kind': 'player', 'id': 0, 'lipsync': 0}]}),
        debugSymbols=typed('scnDebugSymbols', performersDebugSymbols=[typed('scnPerformerSymbol',
            editorPerformerId='0', entityRef=empty_entity_ref('#player', 'string'),
            performerId=typed('scnPerformerId', id=1))], sceneEventsDebugSymbols=[],
            sceneNodesDebugSymbols=[], workspotsDebugSymbols=[]),
        workspots=[], workspotInstances=[],
        sceneSolutionHash=typed('scnSceneSolutionHash', sceneSolutionHash=typed('scnSceneSolutionHashHash',
            sceneSolutionHashDate=str(fnv1a64(ns)))),
        **{name: [] for name in ('effectDefinitions', 'effectInstances', 'executionTagEntries',
            'executionTags', 'interruptionScenarios', 'localMarkers', 'notablePoints', 'props',
            'referencePoints', 'ridResources', 'voInfo')})
    return document(root, archive)


def journal(config, archive, bindings):
    alloc = HandleAllocator(0)
    ns = config['id']
    def entry(kind, name, children=(), **fields):
        return alloc.wrap(typed(kind, id=name, entries=list(children), journalEntryOverrideDataList=[], **fields))
    description = entry('gameJournalQuestDescription', 'description',
        description={'unk1': '0', 'value': ns+'_description'})
    description['Data'].pop('entries')
    objective = entry('gameJournalQuestObjective', 'finish', [description],
        description={'unk1': '0', 'value': ns+'_finish'}, counter=0, optional=0,
        districtID='', itemID=tweakdbid(0, 'uint64'), locationPrefabRef=node_ref(0, 'uint64'))
    pin = entry('gameJournalQuestMapPin', 'waiting_spot', enableGPS=1,
        reference=empty_entity_ref(bindings['activation_map_ref'], 'string'),
        slotName=cname('UI_Interaction'), offset=typed('Vector3', X=0, Y=0, Z=0.5),
        mappinData=typed('gamemappinsMappinData', active=1, debugCaption='',
            localizedCaption={'unk1':'0','value':''},
            mappinType=tweakdbid('Mappins.QuestStaticMappinDefinition'),
            variant='DefaultQuestVariant', visibleThroughWalls=1))
    start = entry('gameJournalQuestObjective', '01a_wait_for_race', [pin],
        description={'unk1':'0','value':ns+'_go_to_start'}, counter=0, optional=0,
        locationPrefabRef=node_ref(0, 'uint64'))
    get_in = entry('gameJournalQuestObjective', '01_get_in',
        description={'unk1':'0','value':ns+'_get_in'}, optional=0)
    countdown = entry('gameJournalQuestObjective', '01a_wait_for_race1',
        description={'unk1':'0','value':ns+'_wait_countdown'}, optional=0)
    reward_pin = entry('gameJournalQuestMapPin','reward_crate',enableGPS=1,
        reference=empty_entity_ref(bindings['reward_crate'],'string'),slotName=cname('UI_Interaction'),
        offset=typed('Vector3',X=0,Y=0,Z=0.5),mappinData=typed('gamemappinsMappinData',
            active=1,mappinType=tweakdbid('Mappins.QuestStaticMappinDefinition'),
            variant='DefaultQuestVariant',visibleThroughWalls=1))
    reward = entry('gameJournalQuestObjective','04_get_reward',[reward_pin],
        description={'unk1':'0','value':ns+'_get_reward'},optional=0)
    phase = entry('gameJournalQuestPhase', 'race', [start,get_in,countdown,objective,reward], locationPrefabRef=node_ref(0, 'uint64'))
    quest = entry('gameJournalQuest', ns, [phase], title={'unk1': '0', 'value': ns+'_title'},
        type='MinorQuest', districtID='', recommendedLevelID=tweakdbid(0, 'uint64'))
    folder = entry('gameJournalFolderEntry', 'minor_quest', [quest])
    primary = entry('gameJournalPrimaryFolderEntry', 'quests', [folder])
    poi = alloc.wrap(typed('gameJournalPointOfInterestMappin', id=ns+'_start', journalEntryOverrideDataList=[],
        # ArchiveXL must cook this position before the course sector streams.
        # A zero static ref selects its supported absolute-offset path.
        staticNodeRef=node_ref(0,'uint64'),
        dynamicEntityRef=empty_entity_ref(bindings['activation_map_ref'], 'string'),
        offset=typed('Vector3', **{axis.upper():bindings['activation_map_position'][axis]
                                 for axis in ('x','y','z')}),
        questPath=None,
        mappinData=typed('gamemappinsPointOfInterestMappinData', active=1, dynamicMappinRadius=30,
            dynamicMappinDef=tweakdbid('Mappins.DynamicPointOfInterestMappinDefinition'),
            staticMappinDef=tweakdbid('Mappins.StaticPointOfInterestMappinDefinition'),
            slotName=cname('UI_Interaction'),slotOffset=typed('Vector3', X=0, Y=0, Z=0.5),
            typedVariant=alloc.wrap(typed('gamemappinsCommonVariant',variant='Zzz18_RacingVariant')))))
    poi_group = entry('gameJournalPointOfInterestGroup', 'street_race', [poi])
    poi_folder = entry('gameJournalPrimaryFolderEntry', 'points_of_interest', [poi_group])
    root = entry('gameJournalRootFolderEntry', '', [primary,poi_folder],
        descriptor=resource_path(r'base\journal\descriptor.journaldesc'))
    return document(typed('gameJournalResource', cookingPlatform='PLATFORM_PC', entry=root), archive)


def onscreens(config, archive):
    ns = config['id']
    texts = {ns+'_title': config['title'], ns+'_finish': 'Finish the race.',
        ns+'_go_to_start':'Wait for the race.',
        ns+'_get_in':'Get in your vehicle.',
        ns+'_wait_countdown':'Wait for the race to start.',
        ns+'_get_reward':'Collect your reward.',
        ns+'_description': config.get('description', 'Complete the checkpoints in order and beat the other racers.')}
    root = typed('JsonResource', cookingPlatform='PLATFORM_PC', root={'HandleId': '0',
        'Data': typed('localizationPersistenceOnScreenEntries', entries=[
            typed('localizationPersistenceOnScreenEntry', primaryKey='0', secondaryKey=key,
                  femaleVariant=value, maleVariant='') for key, value in texts.items()])})
    return document(root, archive)


def checkpoint(config, archive, *, activation_sign=False, direction='Forward'):
    """Create a private checkpoint device, operations and two sign surfaces."""
    ns = config['id']
    alloc = HandleAllocator(0)
    chunks = [typed('GenericDevice', controllerTypeName=cname('GenericDeviceController'),
        durabilityType='INVULNERABLE', deviceState='OFF', isUIdirty=1, visibilityCheckDistance=16000)]
    def component(kind, name, **fields):
        result = typed(kind, name=cname(name), id=str(fnv1a64(ns+':component:'+name)), isReplicable=0, **fields)
        chunks.append(result)
        return result
    # Native device scripts acquire these named components during initialization.
    component('entSlotComponent', 'main_slot', localTransform=transform(), slots=[], fallbackSlots=[])
    component('workWorkspotResourceComponent', 'personalLinkPlayerWorkspot', localTransform=transform())
    component('senseVisibleObjectComponent', 'senseVisibleObject', localTransform=transform(),
        visibleObject=alloc.wrap(typed('senseVisibleObject', visibilityDistance=100, visibleObjectType='Undefined')))
    component('gameStatsComponent', 'StatsComponent', persistentState=alloc.wrap(typed('gameStatsComponentPS')))
    component('gameaudioSoundComponent', 'audio', localTransform=transform(), maxPlayDistance=40,
        obstructionChangeTime=0.2, audioName=cname('None'), voEventOverride=cname('None'), subSystems=[])
    operations = []
    def operation(kind, name, **fields):
        operations.append(alloc.wrap(typed(kind, operationName=cname(name), disableDevice=0,
            executeOnce=0, isEnabled=1, toggleOperations=[], **fields)))
    operation('FactsDeviceOperation', 'addFact', facts=[typed('SFactOperationData',
        factName=cname('sq024_current_race_checkpoint_fact_add'), factValue=1, operationType='Add')])
    operation('ToggleComponentsDeviceOperation', 'disableComponents', components=[
        typed('SComponentOperationData', componentName=cname(name), operationType='Disable')
        for name in ('ui_back', 'ui_front', 'trigger')])
    operations[-1]['Data']['disableDevice'] = 1
    operation('PlaySoundDeviceOperation', 'playSound', SFXs=[typed('SSFXOperationData',
        operationType='START', sfxName=cname('sq024_race_countdown'))])
    executions = [alloc.wrap(typed('OperationExecutionData', delay=delay,
        delayID=typed('gameDelayID'), isDelayActive=0, operationName=cname(name), resetDelay=0))
        for name, delay in [('addFact', 0), ('disableComponents', 0.1), ('playSound', 0)]]
    trigger = alloc.wrap(typed('TriggerVolumeOperationsTrigger', triggerData=alloc.wrap(
        typed('TriggerVolumeOperationTriggerData', canNPCBeDead=1, componentName=cname('trigger'),
            isActivatorNPC=0, isActivatorPlayer=1, operationsToExecute=executions, operationType='ENTER'))))
    if activation_sign:
        operations = []
    component('GenericDeviceController', 'controller', persistentState=alloc.wrap(typed('GenericDeviceControllerPS',
        deviceState='ON', deviceUIStyle='LightBlue', isInteractive=1, hasAuthorizationModule=1,
        tweakDBRecord=tweakdbid('Devices.GenericDevice'),
        deviceOperationsSetup=alloc.wrap(typed('DeviceOperationsContainer', operations=operations,
            triggers=[] if activation_sign or direction=='Finish' else [trigger])))))
    component('DisassemblableComponent', 'disassemblableComponent')
    component('gameinteractionsComponent', 'interaction', localTransform=transform(), isEnabled=1,
        interactionRootOffset=typed('Vector3', X=0, Y=0, Z=0), layerOverrides=[], layerOverridesTemp=[])
    component('entLocalizationStringComponent', 'localization', Strings=[])
    component('gameTargetingComponent', 'targeting', localTransform=transform(), isEnabled=1, isPrimary=1, aimAssistData=[])
    component('gameVisionModeComponent', 'vision', persistentState=alloc.wrap(typed('gameVisionModeComponentPS')))
    component('WorkspotMapperComponent', 'workspotMapper', workspotsMap=[])
    component('FxResourceMapperComponent', 'FxResourceMapper', investigationSlotOffsetMultiplier=1,
        areaEffectData=[], areaEffectInFocusMode=[], optionalAreaEffectData=[])
    component('GameplayRoleComponent', 'GameplayRole', alwaysCreateMappinAsDynamic=1, autoDeterminGameplayRole=1,
        currentGameplayRole='UnAssigned', gameplayRole='UnAssigned', mappinsDisplayMode='MINIMALISTIC', offsetValue=0.04)
    component('entSlotComponent', 'IKslots', localTransform=transform(), slots=[], fallbackSlots=[])
    component('StimBroadcasterComponent', 'StimBroadcaster', fallbackInterval=1)
    component('gameStaticTriggerAreaComponent', 'trigger', isEnabled=int(not activation_sign and direction!='Finish'), includeMask=1,
        localTransform=transform(-582373/131072), outline=alloc.wrap(typed('AreaShapeOutline', buffer='', height=30,
            points=[typed('Vector3', X=x, Y=y, Z=0) for x, y in [(-25,-20), (25,-20), (25,60), (-25,60)]])))
    mesh = r'base\environment\decoration\advertising\holograms\common\common_holograms_transparent_a.mesh'
    for side in ('front', 'back'):
        component('entMeshComponent', 'screen_'+side, isEnabled=1,
            localTransform=transform(1.5 if activation_sign else 368312/131072, side == 'front'),
            mesh=resource_path(mesh, flags='Default'), meshAppearance=cname('screen_ui'),
            visualScale=typed('Vector3', X=2.5 if activation_sign else 10, Y=1,
                Z=1.4 if activation_sign else 5.63000011),
            LODMode='AlwaysVisible', chunkMask='9223372036854775807', forceLODLevel=-1,
            objectTypeID='ROT_Static', renderingPlane='RPl_Scene', renderSceneLayerMask='Default',
            motionBlurScale=1, castShadows='Always', castLocalShadows='Always',
            castRayTracedGlobalShadows='Always', overrideMeshNavigationImpact=1,
            navigationImpact=typed('NavGenNavigationSetting', navmeshImpact='Ignored'))
        component('StreetSignWidgetComponent', 'ui_'+side, isEnabled=1, localTransform=transform(),
            isAStreetName=1, screenAreaMultiplier=1,
            meshTargetBinding=alloc.wrap(typed('worlduiMeshTargetBinding', bindName=cname('screen_'+side), enabled=1,
                enableMask=typed('entTagMask', excludedTags=typed('redTagList', tags=[cname('NoBinding')]),
                    hardTags=typed('redTagList', tags=[]), softTags=typed('redTagList', tags=[])))),
            signSelector=alloc.wrap(typed('RaceCheckpointSelector', baseTweakID=tweakdbid(0, 'uint64'),
                recordID=tweakdbid('LCDScreens.RaceFinish' if direction=='Finish' else 'LCDScreens.RaceCheckpoint'+direction))),
            streetSignTDBID=tweakdbid('LCDScreens.RaceFinish' if direction=='Finish' else 'LCDScreens.RaceCheckpoint'+direction))
    package = {'Version': 4, 'Sections': 7, 'CruidIndex': 0,
        'CruidDict': {str(i): chunk.get('id', '0') for i, chunk in enumerate(chunks)}, 'Chunks': chunks}
    return document(typed('entEntityTemplate', cookingPlatform='PLATFORM_PC',
        defaultAppearance=cname('default'), compiledData={'BufferId': '0', 'Flags': 4063232,
            'Type': 'WolvenKit.RED4.Archive.Buffer.RedPackage, WolvenKit.RED4, Version=8.17.4.0, Culture=neutral, PublicKeyToken=null',
            'Data': package},
        appearances=[], backendDataOverrides=[], bindingOverrides=[], compiledEntityLODFlags=0,
        componentResolveSettings=[], includes=[], inplaceResources=[], resolvedDependencies=[resource_path(mesh)]), archive)
