"""Native MQ056 lifecycle operations, with race-owned sources and references."""
from phase_graph import cname, entity_reference


RESTRICTIONS = ('163802172868','151159473294','131161243162',
                '175584140294','122023708999')


def checkpoint(b, number, source, locked):
    return b.node(number,'questCheckpointNodeDefinition',input_names=('In',),properties={
        'saveLock':int(locked),'debugString':source})


def restrictions(b, number, source, enable, group='grid'):
    groups = {
        'grid':('163802172868','151159473294','131161243162'),
        'preparation':('175584140294','122023708999'),
        'mounted':('158010230621','151247563188','182938465435'),
        'countdown':('158010230621',)}
    return b.node(number,'questGameManagerNodeDefinition',input_names=('In',),properties={
        'type':b.handles.wrap({'$type':'questGameplayRestrictions_NodeType',
            'source':cname(source+'_'+group),'action':'AddRestriction' if enable else 'RemoveRestriction',
            'restrictionIDs':[{'$type':'TweakDBID','$storage':'uint64','$value':value}
                              for value in groups[group]]})})


def mortality(b, number, reference, source, enable, player=False):
    return b.node(number,'questCharacterManagerNodeDefinition',input_names=('In',),properties={
        'type':b.handles.wrap({'$type':'questCharacterManagerParameters_NodeType',
            'subtype':b.handles.wrap({'$type':'questCharacterManagerParameters_SetMortality',
                'puppetRef':entity_reference(reference),'isPlayer':int(player),
                'state':'Immortal' if enable else 'Mortal','source':cname(source),
                'resetToDefault':0})})})


def game_time_delay(b, number, days):
    return b.node(number,'questPauseConditionNodeDefinition',input_names=('In',),properties={
        'condition':b.handles.wrap({'$type':'questTimeCondition','type':b.handles.wrap({
            '$type':'questGameTimeDelay_ConditionType','days':days,'hours':0,'minutes':0,'seconds':0})})})


def content_ready(b, number):
    return b.node(number,'questPauseConditionNodeDefinition',input_names=('In',),properties={
        'condition':b.handles.wrap({'$type':'questContentCondition','type':b.handles.wrap({
            '$type':'questContentLock_ConditionType','isContentBlocked':0})})})


def stop_workspot(b, number):
    return b.node(number,'questUseWorkspotNodeDefinition',input_names=('In',),output_names=('Success',),
        properties={'entityReference':entity_reference('#player'),
            'paramsV1':b.handles.wrap({'$type':'questUseWorkspotParamsV1','function':'StopWorkspot',
                'instant':1,'finishAnimation':0})})


def health_drop(b, number, percent=90.0):
    return b.node(number,'questPauseConditionNodeDefinition',input_names=('In',),properties={
        'condition':b.handles.wrap({'$type':'questCharacterCondition','type':b.handles.wrap({
            '$type':'questCharacterHealth_ConditionType','objectRef':entity_reference('#mounted_vehicle'),
            'isPlayer':False,'comparisonType':'LessOrEqual','percent':percent})})})


def speeding(b, number):
    return b.node(number,'questPauseConditionNodeDefinition',input_names=('In',),properties={
        'condition':b.handles.wrap({'$type':'questVehicleCondition','type':b.handles.wrap({
            '$type':'questVehicleSpeed_ConditionType','vehicleRef':entity_reference('#mounted_vehicle'),
            'comparisonType':'CT_GREATER_EQUAL','speed':90})})})


def sandstorm(b, number):
    return b.node(number,'questPauseConditionNodeDefinition',input_names=('In',),properties={
        'condition':b.handles.wrap({'$type':'questFactsDBCondition','type':b.handles.wrap({
            '$type':'questVarComparison_ConditionType',
            'factName':'sq024_badlands_sandstorm_entered','comparisonType':'Greater','value':0})})})


def destroyed(b, number, ref):
    return b.node(number,'questPauseConditionNodeDefinition',input_names=('In',),properties={
        'condition':b.handles.wrap({'$type':'questCharacterCondition','type':b.handles.wrap({
            '$type':'questCharacterHealth_ConditionType','objectRef':ref,
            'isPlayer':False})})})
