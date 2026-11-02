"""Directly authored MQ056 countdown and player result commentary."""
from generate_scene import (HandleAllocator, build_start_node, build_loc_store,
    build_resource_refs, cname, deterministic_event_id, empty_entity_ref, node_ref,
    output_socket, scene_node_id, scene_time, tweakdbid)
from race_resources import document, typed


def presentation(config, archive, bindings, *, result=False):
    from generate_scene import resource_path
    ns = config['id']
    alloc = HandleAllocator(1)
    graph, lines, entries, exits = [], [], [], []
    player_id = 1
    arrays = {name:[] for name in ('animSets','bodyCinematicAnimSets','cyberwareAnimSets',
        'cyberwareCinematicAnimSets','deformationAnimSets','dynamicAnimSets',
        'facialAnimSets','facialCinematicAnimSets')}
    player = typed('scnPlayerActorDef',actorId=typed('scnActorId',id=player_id),
        playerName='Player',acquisitionPlan='findInContext',
        specCharacterRecordId=tweakdbid('Character.Player_Puppet_Base'),
        voicetagId=typed('scnVoicetagId',id='1103967280742240864'),
        lipsyncAnimSet=typed('scnLipsyncAnimSetSRRefId',id=1),
        findActorInContextParams=typed('scnFindEntityInContextParams',
            specRecordId=tweakdbid('Character.Player_Puppet_Base')),**arrays)
    actors, symbols = [], [typed('scnPerformerSymbol',editorPerformerId='0',
        entityRef=empty_entity_ref('#player','string'),performerId=typed('scnPerformerId',id=player_id*256+1))]
    if not result:
        # Keep the native player acquisition fields; seated animation sets are
        # intentionally absent because this builder uses standing waiting.
        player.pop('specAppearance',None)
        player.pop('specTemplate',None)
        player['findActorInContextParams'].pop('contextualName',None)
        actors.append(typed('scnActorDef',actorId=typed('scnActorId',id=0),actorName='announcer',
            acquisitionPlan='findInContext',
            findActorInContextParams=typed('scnFindEntityInContextParams',
                contextualName='Voice',
                voiceVagId=typed('scnVoicetagId',id='1796388644539244544'),
                specRecordId={'$type':'TweakDBID','$storage':'uint64','$value':'129901368005'}),
            voicetagId=typed('scnVoicetagId',id='1796388644539244544'),
            lipsyncAnimSet=typed('scnLipsyncAnimSetSRRefId',id=0),**arrays))
        # Native Voice has no world-entity binding in its performer symbol.
        symbols.append(typed('scnPerformerSymbol',editorPerformerId='4118870146959667200',
            performerId=typed('scnPerformerId',id=1)))

    if result:
        actors.append(typed('scnActorDef',actorId=typed('scnActorId',id=0),actorName='Johnny',
            acquisitionPlan='community',communityParams=typed('scnCommunityParams',entryName=cname('johnny'),
                reference=node_ref(bindings['crowd']),forceMaxVisibility=0),
            voicetagId=typed('scnVoicetagId',id='1103967280742240508'),
            lipsyncAnimSet=typed('scnLipsyncAnimSetSRRefId',id=0),**arrays))
        symbols.append(typed('scnPerformerSymbol',editorPerformerId='0',
            entityRef=empty_entity_ref(bindings['crowd'],'string',names=['johnny']),
            performerId=typed('scnPerformerId',id=1)))

    def line(locstring, speaker, start, duration, section):
        # Screenplay IDs encode the store index in the high bits and the
        # dialog-line kind (1) in the low byte. They are not arbitrary IDs:
        # the engine indexes lines[item >> 8] when preparing the VO command.
        # Allocate from this scene's actual store, not vanilla's old indexes
        # or the unrelated graph node numbers.
        item = (len(lines) << 8) | 1
        screenplay_line = typed('scnscreenplayDialogLine',itemId=typed('scnscreenplayItemId',id=item),
            speaker=typed('scnActorId',id=speaker),addressee=typed('scnActorId',id=1-speaker),
            locstringId=typed('scnlocLocstringId',ruid=str(locstring)),
            usage=typed('scnscreenplayLineUsage',playerGenderMask=typed('scnGenderMask',mask=3)))
        screenplay_line.update(
            maleLipsyncAnimationName=cname(f'm_{locstring:016X}'),
            femaleLipsyncAnimationName=cname(f'f_{locstring:016X}'))
        lines.append(screenplay_line)
        return alloc.wrap(typed('scnDialogLineEvent',
            id=typed('scnSceneEventId',id=deterministic_event_id(ns,section,item)),
            startTime=start,duration=duration,screenplayLineId=typed('scnscreenplayItemId',id=item),
            voParams=typed('scnDialogLineVoParams',voExpression='Vo_Expression_Phone' if not result else 'Vo_Expression_Spoken')))

    def section(number, duration, events, sockets, *, ff_strategy='automatic'):
        if result:
            sockets = [*sockets,output_socket(1,0,[])]
        graph.append(alloc.wrap(typed('scnSectionNode',nodeId=scene_node_id(number),
            ffStrategy=ff_strategy,events=events,sectionDuration=scene_time(duration),
            actorBehaviors=[typed('scnSectionInternalsActorBehavior',actorId=typed('scnActorId',id=i))
                for i in range(player_id+1)],outputSockets=sockets)))

    def boundary(number, name, *, start=None, nonterminating=False, input_ordinal=0):
        if start is not None:
            graph.append(build_start_node(number,[{'node_id':start,'input_ordinal':input_ordinal}],alloc))
            entries.append(typed('scnEntryPoint',name=cname(name),nodeId=scene_node_id(number)))
        else:
            graph.append(alloc.wrap(typed('scnEndNode',nodeId=scene_node_id(number),
                ffStrategy='automatic',outputSockets=[],type='NonTerminating' if nonterminating else 'Terminating')))
            exits.append(typed('scnExitPoint',name=cname(name),nodeId=scene_node_id(number)))

    if result:
        # Native MQ056 dialogue events end before their five-second sections.
        line_durations = {
            4159347102540754944:2785, 4159349620666658816:1825,
            4159351819706691584:2200, 4159353074558562304:5895,
            4159361710546612224:1770, 4159361737893474304:1620,
            4159361750291836928:1685, 4159362752931819520:2540,
            4159362765078523904:1410, 4159363896584302592:1390,
            4159363909402095616:2575, 4159369413620789248:1390,
            4159369428082749440:1750, 4159369438400737280:2545,
            4159369447779201024:1825, 4159369458030080000:2305,
            4159372547403411456:1410, 4159372566193893376:1805,
            4159372575001931776:1485, 4159372586695651328:1265,
            4159372680513843200:2995}
        for offset, name, strings in [(0,'lose',[4159369413620789248,4159369428082749440,
                4159369438400737280,4159369447779201024,4159369458030080000]),
                (100,'win',[4159372547403411456,4159372566193893376,4159372575001931776,
                            4159372586695651328,4159372680513843200])]:
            boundary(offset+1,name+'_in',start=offset+3)
            boundary(offset+2,name+'_out')
            graph.append(alloc.wrap(typed('scnRandomizerNode',nodeId=scene_node_id(offset+3),
                ffStrategy='automatic',numOutSockets=5,
                outputSockets=[output_socket(0,i,[(offset+10+i,0,0)]) for i in range(5)])))
            for i, string in enumerate(strings):
                section(offset+10+i,5000,[line(string,1,0,line_durations[string],offset+10+i)],
                    [output_socket(0,0,[(offset+2,0,0)])])
        for offset,name,duration,strings in [
                (200,'johnny_win',5000,[4159362752931819520,4159362765078523904]),
                (300,'johnny_lose',5000,[4159363896584302592,4159363909402095616]),
                (400,'you_ready',5000,[4159347102540754944]),
                (500,'car_hp_drop',5000,[4159349620666658816]),
                (600,'sandstorm',5000,[4159351819706691584]),
                (700,'speeding',6170,[4159353074558562304]),
                (800,'destroying_enemy',5000,[4159361710546612224,4159361737893474304,
                                              4159361750291836928])]:
            boundary(offset+1,name+'_in',start=offset+3 if len(strings)>1 else offset+10)
            boundary(offset+2,name+'_out')
            if len(strings)>1:
                graph.append(alloc.wrap(typed('scnRandomizerNode',nodeId=scene_node_id(offset+3),
                    ffStrategy='automatic',numOutSockets=len(strings),
                    outputSockets=[output_socket(0,i,[(offset+10+i,0,0)]) for i in range(len(strings))])))
            for i,string in enumerate(strings):
                section(offset+10+i,duration,[line(string,0,0,line_durations[string],offset+10+i)],
                    [output_socket(0,0,[(offset+2,0,0)])])
    else:
        boundary(1,'announcer_in',start=12)
        boundary(176,'countdown_in',start=189,input_ordinal=1)
        boundary(26,'announcer_out')
        boundary(10,'countdown_go',nonterminating=True)
        boundary(16,'countdown_started',nonterminating=True)
        section(12,13418,[line(string,0,start,duration,12) for string,start,duration in [
            (2008388904462454784,0,4195),(1831399069043400704,4246,3783),
            (1855979224088842240,8029,5389)]],
            [output_socket(0,0,[(195,0,1)]),output_socket(1,0,[])])
        from generate_scene import build_quest_node_base, add_quest_sockets
        data, quest = build_quest_node_base(195,'questPauseConditionNodeDefinition',
            ['CutDestination','In'],['Out'],[{'node_id':189}],alloc)
        quest['condition'] = alloc.wrap(typed('questFactsDBCondition',type=alloc.wrap(
            typed('questVarComparison_ConditionType',factName=ns+'_inside_car',
                comparisonType='Greater',value=0))))
        add_quest_sockets(quest,['CutDestination','In'],['Out'],alloc)
        graph.append(alloc.wrap(data))
        graph.append(alloc.wrap(typed('scnAndNode',nodeId=scene_node_id(189),
            ffStrategy='automatic',numInSockets=2,
            outputSockets=[output_socket(0,0,[(18,666,1)])])))
        graph.append(alloc.wrap(typed('scnDeletionMarkerNode',nodeId=scene_node_id(18),
            ffStrategy='allow_fully',outputSockets=[output_socket(666,0,
                [(14,0,0),(16,0,0),(28,0,1),(38,0,1)])])))
        data, quest = build_quest_node_base(28,'questAudioNodeDefinition',
            ['CutDestination','In'],['Out'],[],alloc)
        quest['type'] = alloc.wrap(typed('questAudioMixNodeType',
            mixSignpost=cname('sq024_city_race_countdown_start')))
        add_quest_sockets(quest,['CutDestination','In'],['Out'],alloc)
        graph.append(alloc.wrap(data))
        # MQ056 section events use socket name 2 with separate ordinals.
        # Keep its zero-time socket before the first VO event as authored.
        events = [alloc.wrap(typed('scneventsSocket',startTime=0,duration=0,
            id=typed('scnSceneEventId',id=deterministic_event_id(ns,14,2)),
            osockStamp=typed('scnOutputSocketStamp',name=2,ordinal=0)))]
        events.extend(line(string,0,start,duration,14) for string,start,duration in [
            (1856145996930748416,0,1539),(1856146462783705088,1539,1405),
            (1856146646410334208,2944,1478)])
        events.append(alloc.wrap(typed('scneventsSocket',startTime=4130,duration=0,
            id=typed('scnSceneEventId',id=deterministic_event_id(ns,14,3)),
            osockStamp=typed('scnOutputSocketStamp',name=2,ordinal=1))))
        countdown_sockets = [output_socket(0,0,[(26,0,0)]),output_socket(1,0,[]),
            output_socket(2,0,[(32,0,1)]),output_socket(2,1,[(20,0,3)])]
        if config.get('vehicle_diagnostics',False):
            # Independent diagnostic outputs: never gate countdown progression.
            for ordinal,(time,stage) in enumerate([
                    (0,'countdown_three'),(1538,'countdown_before_two'),
                    (1540,'countdown_after_two'),(2943,'countdown_before_one'),
                    (2945,'countdown_after_one'),(4130,'countdown_go'),
                    (4421,'countdown_section_end')],2):
                number = 200+ordinal
                events.append(alloc.wrap(typed('scneventsSocket',startTime=time,duration=0,
                    id=typed('scnSceneEventId',id=deterministic_event_id(ns,14,stage)),
                    osockStamp=typed('scnOutputSocketStamp',name=2,ordinal=ordinal))))
                countdown_sockets.append(output_socket(2,ordinal,[(number,0,1)]))
                data, quest = build_quest_node_base(number,'questEventManagerNodeDefinition',
                    ['CutDestination','In'],['Out'],[],alloc)
                quest.update(isObjectPlayer=True,objectRef=empty_entity_ref('#player','string'),
                    managerName='None',event=alloc.wrap(typed('AITaggedAIEvent',
                        name=cname('ghostline_race_vehicle_trace'),
                        tags=[cname(ns),cname(stage),cname('#player')])))
                add_quest_sockets(quest,['CutDestination','In'],['Out'],alloc)
                graph.append(alloc.wrap(data))
            events.sort(key=lambda event:event['Data'].get('startTime',0))
        section(14,4422,events,countdown_sockets,
            ff_strategy='block_fully')
        from generate_scene import build_quest_node_base, add_quest_sockets
        data, quest = build_quest_node_base(32,'questEventManagerNodeDefinition',
            ['CutDestination','In'],['Out'],[{'node_id':34,'input_ordinal':1}],alloc)
        quest.update(objectRef=empty_entity_ref('#mounted_vehicle','string'),managerName='VehicleManager',
            PSClassName=cname('VehicleComponentPS'),componentName=cname('controller'),
            event=alloc.wrap(typed('VehicleRaceQuestEvent',mode='CountdownStart',
                maxCheckpoints=len(bindings['checkpoints'])+1,maxPosition=len(bindings['entrants'])+1)))
        add_quest_sockets(quest,['CutDestination','In'],['Out'],alloc)
        graph.append(alloc.wrap(data))
        # Native node 38 initializes the HUD at the countdown fork itself.
        data, quest = build_quest_node_base(38,'questEventManagerNodeDefinition',
            ['CutDestination','In'],['Out'],[],alloc)
        quest.update(objectRef=empty_entity_ref('#mounted_vehicle','string'),managerName='VehicleManager',
            PSClassName=cname('VehicleComponentPS'),componentName=cname('controller'),
            event=alloc.wrap(typed('VehicleRaceQuestEvent',mode='PreRaceSetup',
                maxCheckpoints=len(bindings['checkpoints'])+1,maxPosition=len(bindings['entrants'])+1)))
        add_quest_sockets(quest,['CutDestination','In'],['Out'],alloc)
        graph.append(alloc.wrap(data))
        # Native CountdownStart continues through checkpoints, then GPS path.
        for number,variants,next_node in [(34,('checkpoints','checkpoints2'),36),
                                          (36,('gps_path',),None)]:
            data, quest = build_quest_node_base(number,'questWorldDataManagerNodeDefinition',
                ['CutDestination','In'],['Out'],
                [{'node_id':next_node,'input_ordinal':1}] if next_node else [],alloc)
            quest['type'] = alloc.wrap(typed('questTogglePrefabVariant_NodeType',params=[
                typed('questTogglePrefabVariant_NodeTypeParams',prefabNodeRef=node_ref(bindings['prefab']),
                    variantStates=[typed('questVariantState',name=cname(name),show=True) for name in variants])]))
            add_quest_sockets(quest,['CutDestination','In'],['Out'],alloc)
            graph.append(alloc.wrap(data))
        for number,path,next_node in [(20,bindings['countdown_objective'],22),
                                      (22,bindings['objective'],24)]:
            inputs = ['CutDestination','Active','Inactive','Succeeded','Failed']
            data, quest = build_quest_node_base(number,'questJournalNodeDefinition',inputs,['Out'],
                [{'node_id':next_node,'input_ordinal':1}],alloc)
            quest['type'] = alloc.wrap(typed('questJournalQuestEntry_NodeType',
                path=alloc.wrap(typed('gameJournalPath',realPath=path,fileEntryIndex=2,
                    className=cname('gameJournalQuestObjective'))),version='OptionalProperty'))
            add_quest_sockets(quest,inputs,['Out'],alloc)
            graph.append(alloc.wrap(data))
        data, quest = build_quest_node_base(24,'questFactsDBManagerNodeDefinition',
            ['CutDestination','In'],['Out'],
            [{'node_id':10},{'node_id':30,'input_ordinal':1}],alloc)
        quest['type'] = alloc.wrap(typed('questSetVar_NodeType',factName=ns+'_countdown_end',
            value=1,setExactValue=True))
        add_quest_sockets(quest,['CutDestination','In'],['Out'],alloc)
        graph.append(alloc.wrap(data))
        data, quest = build_quest_node_base(30,'questEventManagerNodeDefinition',
            ['CutDestination','In'],['Out'],[],alloc)
        quest.update(objectRef=empty_entity_ref('#mounted_vehicle','string'),managerName='VehicleManager',
            PSClassName=cname('VehicleComponentPS'),componentName=cname('controller'),
            event=alloc.wrap(typed('VehicleRaceQuestEvent',mode='RaceStart',
                maxCheckpoints=len(bindings['checkpoints'])+1,maxPosition=len(bindings['entrants'])+1)))
        add_quest_sockets(quest,['CutDestination','In'],['Out'],alloc)
        graph.append(alloc.wrap(data))
    resource_refs = build_resource_refs({'actors':[{'kind':'player','id':player_id,'lipsync':0}]})
    lipsync_scene = 'mq056_00_commentary' if result else 'mq056_01_city_race'
    resource_refs['lipsyncAnimSets'] = [typed('scnLipsyncAnimSetSRRef',
        asyncRefLipsyncAnimSet=resource_path(
            'base\\quest\\minor_quests\\mq056\\scenes\\lipsync\\en\\'+lipsync_scene+'\\'+name+'.anims'))
        for name in (('johnny','v') if result else ('jim_jarry','v'))]
    loc_store = build_loc_store({'name':ns,'choice_line_order':[]},{})
    if result:
        # Native MQ056 commentary descriptors, including the two gendered
        # Polish variants of Johnny's opening line.
        spoken = [
            (4159347102540754944,'So – you ready?',4169929575761231872,'To jak? Gotowa?'),
            (4159349620666658816,'Fuck!',4169929575761231876,'Ja pierdolę!'),
            (4159351819706691584,'Shit, get ready.',4169929575778009088,'Przygotuj się.'),
            (4159353074558562304,'Slow down, turbo. Or you’ll get us killed. Again',4169929575778009092,'Co ty wyprawiasz?! Chcesz nas znowu pozabijać?'),
            (4159361710546612224,'Not half bad, that.',4169929575778009096,'To było dobre.'),
            (4159361737893474304,"Guess it's your lucky day.",4169929575778009100,'No wreszcie!'),
            (4159361750291836928,'Fuck yeah, nice!',4169929575778009104,'Dobra robota.'),
            (4159362752931819520,'Ugh, finally.',4169929575794786304,'To twój szczęśliwy dzień.'),
            (4159362765078523904,'Finally.',4169929575794786308,'Nieźle.'),
            (4159363896584302592,'Ohhh, V…',4169929575794786312,'Kurwa.'),
            (4159363909402095616,'Oh, V…',4169929575794786316,'Oj, V, V...'),
            (4159369413620789248,'Fuck.',4169929575794786320,'Kurwa.'),
            (4159369428082749440,'Great. Just great.',4169929575794786324,'No to pięknie.'),
            (4159369438400737280,'Fan-fucking-tastic.',4169929575811563520,'Wspaniale, kurwa.'),
            (4159369447779201024,'Fucking hell...',4169929575811563524,'Ja pierdolę...'),
            (4159369458030080000,'Goddamnit all...',4169929575811563528,'Szlag by to wszystko.'),
            (4159372547403411456,'Fuuuuuu-uuu--uuuuck! Aaaaaaaaaaugh!',4169929575811563532,'Nieźle!'),
            (4159372566193893376,'Whoooooooo... Aaaaaaah!',4169929575811563536,'Udało się.'),
            (4159372575001931776,'Well, well, well.',4169929575828340736,'Mamy to!'),
            (4159372586695651328,'Gonna be a good day.',4169929575828340740,'Tak!'),
            (4159372680513843200,"Can't have bad luck all the time.",4169929575828340744,'Czasem nawet ja mam szczęście.')]
        descriptors = []
        for locstring,english,polish_id,polish in spoken:
            variants = [(locstring+4,english,None,3),(polish_id,polish,'pl_pl',
                         2 if locstring==4159347102540754944 else 3)]
            if locstring==4159347102540754944:
                variants.append((4169929837569687552,'To jak? Gotowy?','pl_pl',1))
            for variant,text,locale,signature in variants:
                index = len(loc_store['vpEntries'])
                loc_store['vpEntries'].append(typed('scnlocLocStoreEmbeddedVariantPayloadEntry',
                    variantId=typed('scnlocVariantId',ruid=str(variant)),content=text))
                descriptor = typed('scnlocLocStoreEmbeddedVariantDescriptorEntry',
                    variantId=typed('scnlocVariantId',ruid=str(variant)),
                    locstringId=typed('scnlocLocstringId',ruid=str(locstring)),
                    signature=typed('scnlocSignature',val=str(signature)),vpeIndex=index)
                if locale is not None:
                    descriptor['localeId'] = locale
                descriptors.append(descriptor)
        loc_store['vdEntries'].extend(sorted(descriptors,key=lambda entry:'localeId' in entry))
    if not result:
        # MQ056's spoken lines carry embedded locale descriptors as well as
        # global locstring IDs. Generate the same six-line store directly.
        spoken = [
            (1831399069043400704,
             (2241921996463149096,"If someone wants to withdraw, it's too late."),
             (1855808770493517876,'Jeśli ktoś chce się wycofać, to już za późno.'),
             (4118865403789045792,'Not like it matters – too late to back out anyway!')),
            (1855979224088842240,
             (2241921996463149100,"It's time to fasten your seat belts, clench your teeth and get ready to kick."),
             (1855979224088842248,'Czas zapiąć pasy, zacisnąć zęby i przygotować się na kopa.'),
             (4118865403789045796,'Strap in, pray to your gods and get ready to go for pay dirt!')),
            (1856145996930748416,(2241921996496703504,'Start in three ...'),
             (1856145996930748424,'Start za trzy...'),(4118865403805822992,'Three!')),
            (1856146462783705088,(2241921996496703508,'Two...'),
             (1856146462783705096,'Dwa...'),(4118865403805822996,'Two!')),
            (1856146646410334208,(2241921996496703512,'One!'),
             (1856146646410334216,'Jeden!'),(4118865403805823000,'One!')),
            (2008388904462454784,
             (2241921996463149088,"We accept the last bets! Don't be afraid to bet!"),
             (2008389536946720768,'Przyjmujemy ostatnie zakłady! Nie bać się, obstawiać!'),
             (4118865403789045784,"Last bets, last bets! Don't miss your chance to win!"))]
        for column,locale in enumerate(('db_db','pl_pl','en_us'),1):
            for row in spoken:
                variant,text = row[column]
                index = len(loc_store['vpEntries'])
                loc_store['vpEntries'].append(typed('scnlocLocStoreEmbeddedVariantPayloadEntry',
                    variantId=typed('scnlocVariantId',ruid=str(variant)),content=text))
                loc_store['vdEntries'].append(typed('scnlocLocStoreEmbeddedVariantDescriptorEntry',
                    variantId=typed('scnlocVariantId',ruid=str(variant)),
                    locstringId=typed('scnlocLocstringId',ruid=str(row[0])),localeId=locale,
                    signature=typed('scnlocSignature',val='3'),vpeIndex=index))
    root = typed('scnSceneResource',version=5,cookingPlatform='PLATFORM_PC',sceneCategoryTag='minorQuests',
        actors=actors,playerActors=[player],entryPoints=entries,exitPoints=exits,
        sceneGraph=alloc.wrap(typed('scnSceneGraph',graph=graph,
            startNodes=[n['Data']['nodeId'] for n in graph if n['Data']['$type']=='scnStartNode'],
            endNodes=[n['Data']['nodeId'] for n in graph if n['Data']['$type']=='scnEndNode'])),
        screenplayStore=typed('scnscreenplayStore',lines=lines,options=[]),
        locStore=loc_store,
        resouresReferences=resource_refs,
        debugSymbols=typed('scnDebugSymbols',performersDebugSymbols=symbols,
            sceneEventsDebugSymbols=[],sceneNodesDebugSymbols=[],workspotsDebugSymbols=[]),
        **{key:[] for key in ('workspots','workspotInstances','props','localMarkers','effectDefinitions',
            'effectInstances','referencePoints','notablePoints','voInfo','executionTags','executionTagEntries',
            'interruptionScenarios','ridResources')})
    return document(root,archive)
