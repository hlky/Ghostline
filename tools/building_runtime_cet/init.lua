-- Optional, manually operated native navigation / NPC traversal test harness.
-- The default Building Lab package excludes this diagnostic mod.
local contract, actor, actorID, command, playerReturn, actorReturn, active = nil, nil, nil, nil, nil, nil, nil
local playerStage, pendingSpawn, pendingQuery = nil, nil, nil
local visible, message, startIndex, endIndex, npcRecord = false, 'Load a save and choose two test points.', 1, 2, ''
local shutterElapsed, shutterEntities, shutterReports = 0, {}, {}

-- Opt-in migration for a saved door whose PS predates its auto-close setup.
-- Restore once per streamed entity; leave subsequent intentional quickhacks
-- alone. Native DoorTriggerDelayedEvent checks occupancy before closing.
local function restoreDoorAutoClose(delta)
  if not contract or not Game.GetPlayer() then
    shutterEntities = {}
    return
  end
  shutterElapsed = shutterElapsed + delta
  if shutterElapsed < .5 then return end
  shutterElapsed = 0
  for _, ref in ipairs(contract.restore_auto_close or {}) do
    local row = {ref=ref, observed_at=os.date('!%Y-%m-%dT%H:%M:%SZ')}
    local ok, err = pcall(function()
      local resolved = ResolveNodeRef(CreateEntityReference(ref,{}).reference,GlobalNodeID.GetRoot())
      local entity = Game.FindEntityByID(EntityID.new({hash=resolved.hash}))
      if not entity then shutterEntities[ref]=nil; return end
      row.entity_found=true
      local ps=entity:GetDevicePS()
      if shutterEntities[ref] ~= entity then
        row.auto_close_before=ps:IsClosingAutomatically()
        ps:SetCloseItself(true)
        if ps:IsOpen() then entity:QueueEvent(DoorTriggerDelayedEvent.new()) end
        shutterEntities[ref]=entity
        row.restored=true
      end
      row.auto_close=ps:IsClosingAutomatically()
      row.open=ps:IsOpen(); row.busy=ps:IsBusy(); row.powered_on=ps:IsON()
      local trigger=entity:FindComponentByName('trigger')
      if trigger then row.trigger_occupants=trigger:GetNumberOverlappingActivators() end
    end)
    if not ok then row.error=tostring(err) end
    -- Keep the initial migration evidence while refreshing observed state.
    local previous=shutterReports[ref]
    if previous and previous.restored and not row.restored then
      row.restored=true; row.auto_close_before=previous.auto_close_before
    end
    local changed=not previous or row.open~=previous.open or row.auto_close~=previous.auto_close
      or row.trigger_occupants~=previous.trigger_occupants or row.error~=previous.error
      or row.busy~=previous.busy or row.entity_found~=previous.entity_found
    shutterReports[ref]=row
    if changed then
      local file=io.open('garage-door-report.json','w')
      if file then file:write(json.encode({layout=contract.layout_id,doors=shutterReports}));file:close() end
    end
  end
end

local function writeReport(report)
  report.layout = contract and contract.layout_id or 'unloaded'
  report.observed_at = os.date('!%Y-%m-%dT%H:%M:%SZ')
  local file = io.open('runtime-report.json', 'w')
  if file then file:write(json.encode(report)); file:close() end
  message = report.message or report.error or 'Report written'
  print('[Building Lab] ' .. message)
end

local function vector(point)
  return Vector4.new(point[1], point[2], point[3], 1)
end

local function position(value)
  return {value.x, value.y, value.z}
end

local function distance(a, b)
  return math.sqrt((a[1]-b[1])^2 + (a[2]-b[2])^2 + (a[3]-b[3])^2)
end

local function target()
  if actorID then actor = Game.GetDynamicEntitySystem():GetEntity(actorID) end
  return actor
end

local function cancelQuery()
  if pendingQuery then pcall(function() Game.GetAINavigationSystem():StopPathfinding(pendingQuery.id) end) end
  pendingQuery=nil
end

local function stop()
  cancelQuery()
  if command and target() then pcall(function() target():GetAIControllerComponent():CancelCommand(command) end) end
  command, active = nil, nil
end

local function releaseActor()
  pendingSpawn=nil
  stop()
  if actorID then Game.GetDynamicEntitySystem():DeleteEntity(actorID)
  elseif actor and actorReturn then Game.GetTeleportationFacility():Teleport(actor,vector(actorReturn.point),actorReturn.rotation) end
  actor,actorID,actorReturn=nil,nil,nil
end

local function doorDiagnostics()
  local rows={}
  for _, door in ipairs(contract.doors or {}) do
    local row={id=door.id,ref=door.ref,connection_ref=door.connection_ref}
    local ok,err=pcall(function()
      local resolved=ResolveNodeRef(CreateEntityReference(door.ref,{}).reference,GlobalNodeID.GetRoot())
      row.resolved_hash=tostring(resolved.hash)
      local entity=Game.FindEntityByID(EntityID.new({hash=resolved.hash}))
      row.entity_found=entity~=nil
      if entity then
        local ps=entity:GetDevicePS()
        row.open=ps:IsOpen();row.locked=ps:IsLocked();row.sealed=ps:IsSealed()
        row.powered_on=ps:IsON();row.unpowered=ps:IsUnpowered();row.disabled=ps:IsDisabled()
        local component=entity:FindComponentByName('offMeshConnection')
        row.offmesh_component_found=component~=nil
        local expected=ResolveNodeRef(CreateEntityReference(door.connection_ref,{}).reference,GlobalNodeID.GetRoot())
        row.connection_resolved_hash=tostring(expected.hash)
        if component then
          row.offmesh_agent_size=tostring(component.agentSize)
          row.component_connection_hashes={}
          for _, ref in ipairs(component.offMeshConnectionNodesRefs) do
            local resolvedConnection=ResolveNodeRefWithEntityID(ref,entity:GetEntityID())
            row.component_connection_hashes[#row.component_connection_hashes+1]=tostring(resolvedConnection.hash)
          end
        end
      end
    end)
    if not ok then row.error=tostring(err) end
    rows[#rows+1]=row
  end
  return rows
end

local function probe()
  if not contract or #contract.points < 2 then error('The exported layout needs two walkable room sample points') end
  local owner = target() or Game.GetPlayer()
  if not owner then error('Load a save first') end
  if target() and owner:GetNPCType()~=gamedataNPCType.Human then error('The generated navigation supports human NPCs only') end
  local first, last = contract.points[startIndex], contract.points[endIndex]
  local nav = Game.GetAINavigationSystem()
  local a, b = vector(first.world), vector(last.world)
  local startPoint = nav:FindPointInBoxForCharacter(a, Vector4.new(.3,.3,.35,0), owner)
  local endPoint = nav:FindPointInBoxForCharacter(b, Vector4.new(.3,.3,.35,0), owner)
  local path = nav:CalculatePathForCharacter(a, b, .3, owner)
  local samples = {}
  if path and path.path then for _, point in ipairs(path.path) do samples[#samples+1] = position(point) end end
  local endpointsFound = startPoint and startPoint.point and endPoint and endPoint.point
    and distance(position(startPoint.point),first.world)<=.25 and distance(position(endPoint.point),last.world)<=.25
  local complete = #samples > 0 and distance(samples[#samples], last.world) <= .25 and distance(samples[1], first.world) <= .25
  local report = {message = complete and 'Native game query reached both endpoints' or 'Native query failed or returned a partial/snapped path',
    native_query_passed = complete, endpoints_found = not not endpointsFound, door_diagnostics = doorDiagnostics(), npc_movement_passed = false, owner_kind = target() and 'NPC' or 'player',
    start_name = first.name, end_name = last.name, start = first.world, destination = last.world,
    start_status = tostring(startPoint and startPoint.status), end_status = tostring(endPoint and endPoint.status), path = samples}
  cancelQuery()
  local ok,err=pcall(function()
    local query=AINavigationSystemQuery.new()
    query.source=AIPositionSpec.new();query.target=AIPositionSpec.new()
    local source=WorldPosition.new();local destination=WorldPosition.new()
    WorldPosition.SetVector4(source,a);WorldPosition.SetVector4(destination,b)
    AIPositionSpec.SetWorldPosition(query.source,source);AIPositionSpec.SetWorldPosition(query.target,destination)
    pendingQuery={id=nav:StartPathfinding(query),elapsed=0,report=report}
    report.ai_query={completed=false}
  end)
  if not ok then report.ai_query={completed=false,error=tostring(err)} end
  return report
end

local function guarded(action)
  local ok, error = pcall(action)
  if not ok then
    pendingSpawn=nil
    stop()
    if playerStage and playerReturn and Game.GetPlayer() then pcall(function() Game.GetTeleportationFacility():Teleport(Game.GetPlayer(),vector(playerReturn.point),playerReturn.rotation) end) end
    playerStage=nil
    writeReport({error=tostring(error), native_query_passed=false, npc_movement_passed=false})
  end
end

local function teleportPlayer(point)
  local player = Game.GetPlayer()
  if not player then error('Load a save first') end
  if not playerReturn then playerReturn = {point=position(player:GetWorldPosition()), rotation=Quaternion.ToEulerAngles(player:GetWorldOrientation())} end
  playerStage={point=point,elapsed=0};message='Staging V above the start while native navigation streams in…'
end

registerForEvent('onInit', function()
  local file = io.open('contract.json', 'r')
  if file then local text=file:read('*a'); file:close(); local ok,value=pcall(json.decode,text); if ok then contract=value end end
  if not contract then message='contract.json is missing or malformed' end
end)
registerForEvent('onOverlayOpen', function() visible=true end)
registerForEvent('onOverlayClose', function() visible=false end)

registerForEvent('onDraw', function()
  if not visible or not contract then return end
  if ImGui.Begin('Ghostline Building Lab - runtime proof') then
    ImGui.TextWrapped(message)
    ImGui.TextWrapped('Use a test save. Query success is separate from observed NPC movement. The harness never ignores navigation.')
    for index, point in ipairs(contract.points) do
      if ImGui.RadioButton('Start: '..point.name..'##a'..index,startIndex==index) then startIndex=index end
      ImGui.SameLine()
      if ImGui.RadioButton('End: '..point.name..'##b'..index,endIndex==index) then endIndex=index end
    end
    if ImGui.Button('Teleport V to start') then guarded(function() teleportPlayer(contract.points[startIndex].world) end) end
    ImGui.SameLine()
    if ImGui.Button('Return V') then guarded(function()
      playerStage=nil
      if playerReturn and Game.GetPlayer() then Game.GetTeleportationFacility():Teleport(Game.GetPlayer(),vector(playerReturn.point),playerReturn.rotation); playerReturn=nil end
    end) end
    if ImGui.Button('Bind looked-at NPC') then guarded(function()
      local candidate=Game.GetTargetingSystem():GetLookAtObject(Game.GetPlayer(),false,false)
      if not candidate or not candidate:IsNPC() or candidate:GetNPCType()~=gamedataNPCType.Human then error('Look directly at a disposable human test NPC') end
      releaseActor();actor=candidate
      actorReturn={point=position(actor:GetWorldPosition()),rotation=Quaternion.ToEulerAngles(actor:GetWorldOrientation())}
      message='NPC bound; move it to the test start or use Bring NPC to start.'
    end) end
    npcRecord=ImGui.InputText('Optional generic NPC record',npcRecord,200)
    if ImGui.Button('Spawn nonpersistent test NPC') then guarded(function()
      stop()
      if not npcRecord:match('^Character%.') or not TweakDB:GetRecord(TweakDBID.new(npcRecord)) then error('Enter an existing generic Character record') end
      if not DynamicEntitySpec then error('Codeware DynamicEntitySpec is required for spawning') end
      releaseActor()
      local spec=DynamicEntitySpec.new()
      spec.recordID=TweakDBID.new(npcRecord);spec.position=vector(contract.points[startIndex].world);spec.orientation=Quaternion.new(0,0,0,1)
      spec.persistState=false;spec.persistSpawn=false;spec.alwaysSpawned=true;spec.spawnInView=true;spec.active=true
      actorID=Game.GetDynamicEntitySystem():CreateEntity(spec);actor=nil;actorReturn=nil
      if not actorID then error('The dynamic entity system rejected the spawn request') end
      pendingSpawn={elapsed=0,record=npcRecord}
      message='Spawn requested; checking NPC readiness (up to 20 seconds).'
    end) end
    if ImGui.Button('Bring NPC to start') then guarded(function()
      stop();if not target() then error('Bind or spawn a test NPC first') end
      Game.GetTeleportationFacility():Teleport(target(),vector(contract.points[startIndex].world),EulerAngles.new(0,0,0))
    end) end
    if ImGui.Button('Run native query') then guarded(function() writeReport(probe()) end) end
    ImGui.SameLine()
    ImGui.TextWrapped('Walk tests require a complete native path. Failed paths may trigger engine teleport fallback and are not traversal proof.')
    if ImGui.Button('Walk NPC to end') then guarded(function()
      stop();if not target() then error('Bind or spawn a test NPC first') end
      local report=probe()
      if not report.endpoints_found or not report.native_query_passed then
        report.message='No complete native path; walk not attempted. The engine may teleport when pathfinding fails.'
        report.command_accepted=false
        writeReport(report);return
      end
      report.movement_attempted_after_failed_query=not report.native_query_passed
      if distance(position(target():GetWorldPosition()),contract.points[startIndex].world)>1 then error('Bring the test NPC to the selected start first') end
      local wp=WorldPosition.new();WorldPosition.SetVector4(wp,vector(contract.points[endIndex].world))
      local destination=AIPositionSpec.new();AIPositionSpec.SetWorldPosition(destination,wp)
      command=AIMoveToCommand.new();command.movementTarget=destination;command.movementType=moveMovementType.Walk
      command.ignoreNavigation=false;command.finishWhenDestinationReached=true;command.desiredDistanceFromTarget=.3
      local departure=position(target():GetWorldPosition())
      if not target():GetAIControllerComponent():SendCommand(command) then error('NPC AI rejected the move command') end
      report.command_accepted=true
      report.message='NPC controller accepted a navigation-enabled walk; awaiting observed movement.'
      writeReport(report)
      active={elapsed=0,sampleElapsed=0,report=report,previous=departure,travelled=0,teleport=false,samples={}}
      message='NPC move requested; measuring actual movement for up to 60 seconds.'
    end) end
    if ImGui.Button('Stop and restore / despawn test NPC') then guarded(function()
      pendingSpawn=nil
      stop()
      if actorID then Game.GetDynamicEntitySystem():DeleteEntity(actorID);actorID=nil
      elseif actor and actorReturn then Game.GetTeleportationFacility():Teleport(actor,vector(actorReturn.point),actorReturn.rotation) end
      actor=nil;actorReturn=nil;message='Test NPC cleaned up.'
    end) end
  end
  ImGui.End()
end)

registerForEvent('onUpdate', function(delta)
  restoreDoorAutoClose(delta)
  if pendingQuery then
    local request=pendingQuery
    request.elapsed=request.elapsed+delta
    local ok,err=pcall(function()
      local result=AINavigationSystemResult.new()
      local ready=Game.GetAINavigationSystem():GetResult(request.id,result)
      if ready then
        request.report.ai_query={completed=true,has_failed=result.hasFailed,has_path=result.hasPath,
          has_closest_reachable_point=result.hasClosestReachablePoint,
          closest_reachable=position(WorldPosition.ToVector4(result.closestReachablePoint))}
        cancelQuery();writeReport(request.report)
      elseif request.elapsed>3 then
        request.report.ai_query={completed=false,error='NPC path query timed out after 3 seconds'}
        cancelQuery();writeReport(request.report)
      end
    end)
    if not ok then
      request.report.ai_query={completed=false,error=tostring(err)}
      cancelQuery();writeReport(request.report)
    end
  end
  if pendingSpawn then
    guarded(function()
      pendingSpawn.elapsed=pendingSpawn.elapsed+delta
      local current=target()
      if current and current:IsNPC() and current:GetNPCType()==gamedataNPCType.Human and current:GetAIControllerComponent() then
        local record=pendingSpawn.record
        pendingSpawn=nil
        message=record..' is ready. Use Bring NPC to start, then Walk NPC to end.'
        print('[Building Lab] '..message)
      elseif pendingSpawn.elapsed>=20 then
        local record=pendingSpawn.record
        pendingSpawn=nil
        message=record..' was not ready after 20 seconds. Stop/despawn and try another record or bind a looked-at human NPC.'
        print('[Building Lab] '..message)
      end
    end)
  end
  if playerStage then
    guarded(function()
      playerStage.elapsed=playerStage.elapsed+delta
      local point=playerStage.point;local player=Game.GetPlayer()
      if not player then error('Player unavailable during staging') end
      local found=Game.GetAINavigationSystem():FindPointInBoxForCharacter(vector(point),Vector4.new(.3,.3,.2,0),player)
      Game.GetTeleportationFacility():Teleport(player,Vector4.new(point[1],point[2],point[3]+.5,1),EulerAngles.new(0,0,0))
      if found and found.point and distance(position(found.point),point)<.25 and playerStage.elapsed>=3 then
        Game.GetTeleportationFacility():Teleport(player,Vector4.new(point[1],point[2],point[3]+.05,1),EulerAngles.new(0,0,0))
        playerStage=nil;message='Native start surface detected. Run the route query, then an NPC walk test.'
      elseif playerStage and playerStage.elapsed>20 then
        playerStage=nil
        if playerReturn then Game.GetTeleportationFacility():Teleport(player,vector(playerReturn.point),playerReturn.rotation) end
        error('Native navigation did not stream at the test start; V was returned')
      end
    end)
  end
  if not active then return end
  guarded(function()
    local current=target()
    if not current then stop();error('Test NPC disappeared during movement') end
    active.elapsed=active.elapsed+delta;active.sampleElapsed=active.sampleElapsed+delta
    if active.sampleElapsed<.1 then return end
    active.sampleElapsed=0
    local p=position(current:GetWorldPosition());local step=distance(p,active.previous)
    if step>2 then active.teleport=true end
    active.travelled=active.travelled+step;active.previous=p;active.samples[#active.samples+1]=p
    local destination=contract.points[endIndex].world
    local arrived=math.sqrt((p[1]-destination[1])^2+(p[2]-destination[2])^2)<.6 and math.abs(p[3]-destination[3])<.25
    if arrived or active.elapsed>60 then
      local report=active.report
      report.npc_movement_passed=arrived and active.travelled>.5 and not active.teleport
      report.elapsed=active.elapsed;report.travelled=active.travelled;report.teleport_detected=active.teleport;report.observed_positions=active.samples
      report.door_diagnostics_at_end=doorDiagnostics()
      report.message=active.teleport and 'NPC made a teleport-sized jump; this is not a successful navigation walk.'
        or (report.npc_movement_passed and 'NPC physically reached the destination using navigation' or 'NPC traversal did not pass; inspect the observed positions and door state')
      stop();writeReport(report)
    end
  end)
end)

registerForEvent('onShutdown',function()
  stop()
  if actorID then pcall(function() Game.GetDynamicEntitySystem():DeleteEntity(actorID) end)
  elseif actor and actorReturn then pcall(function() Game.GetTeleportationFacility():Teleport(actor,vector(actorReturn.point),actorReturn.rotation) end) end
  if playerStage and playerReturn then pcall(function() Game.GetTeleportationFacility():Teleport(Game.GetPlayer(),vector(playerReturn.point),playerReturn.rotation) end) end
end)
