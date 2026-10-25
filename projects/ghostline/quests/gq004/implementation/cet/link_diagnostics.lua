-- Temporary read-only trace. No overrides, actions, spawning or fact writes.
return function()
  local filename = 'love-actually-link-trace.jsonl'
  local elapsed, lastPoll, lastSnapshot = 0, 0, ''
  local function call(fn)
    local ok, value = pcall(fn)
    if not ok then return 'ERROR: ' .. tostring(value) end
    if value == nil then return 'nil' end
    if type(value) == 'boolean' or type(value) == 'number' then return value end
    return tostring(value)
  end
  local function write(event, data)
    local row = data or {}; row.event = event; row.elapsed = elapsed
    local file = io.open(filename, 'a')
    if file then file:write(json.encode(row) .. '\n'); file:close() end
  end
  local function nearby(entity)
    if not entity then return false end
    local ok, position = pcall(function() return entity:GetWorldPosition() end)
    return ok and position.x > -630 and position.x < -590
      and position.y > 780 and position.y < 820 and position.z > 15 and position.z < 30
  end
  local function playerNearby()
    return nearby(Game.GetPlayer())
  end
  local function psSnapshot(ps)
    if not ps then return {error='No persistent state'} end
    return {
      class=call(function() return ps:GetClassName() end),
      entity=call(function() return ps:GetMyEntityID() end),
      state=call(function() return ps:GetDeviceState() end),
      link=call(function() return ps:GetPersonalLinkStatus() end),
      connected=call(function() return ps:IsPersonalLinkConnected() end),
      connecting=call(function() return ps:IsPersonalLinkConnecting() end),
      breached=call(function() return ps:WasHackingMinigameSucceeded() end),
      slot=call(function() return ps:HasPersonalLinkSlot() end),
      disruptive=call(function() return ps:IsDisruptivePlayerStatusEffectPresent() end),
    }
  end
  local function actionSnapshot(action)
    return {
      class=call(function() return action:GetClassName() end),
      action=call(function() return action:GetActionName() end),
      duration=call(function() return action:GetDurationValue() end),
      persistent=call(function() return action:GetPersistentID() end),
      controller=call(function() return action:GetDeviceClassName() end),
      executor=call(function() return action:GetExecutor():GetEntityID() end),
    }
  end
  local function hook(class, method, callback, before)
    local observer = before and ObserveBefore or ObserveAfter
    local ok, err = pcall(observer, class, method, function(...)
      local success, detail = pcall(callback, ...)
      if not success then write('callback_error', {method=method, detail=tostring(detail)}) end
    end)
    write('hook', {class=class, method=method, ok=ok, error=not ok and tostring(err) or nil})
  end
  hook('InteractiveDevice', 'OnInteractionUsed', function(device, event)
    if not nearby(device) then return end
    local row = psSnapshot(device:GetDevicePS())
    row.choice = call(function() return event.choice.choiceMetaData.tweakDBID end)
    row.actions = call(function() return #event.choice.data end)
    write('interaction_used', row)
  end, true)
  hook('BaseScriptableAction', 'ProcessRPGAction', function(action)
    if playerNearby() then write('process_action', actionSnapshot(action)) end
  end, true)
  hook('ScriptableDeviceComponentPS', 'OnTogglePersonalLink', function(ps, action)
    if not playerNearby() then return end
    local row = psSnapshot(ps); row.action_data = actionSnapshot(action)
    write('link_controller_before', row)
  end, true)
  hook('ScriptableDeviceComponentPS', 'OnTogglePersonalLink', function(ps)
    if playerNearby() then write('link_controller_after', psSnapshot(ps)) end
  end)
  hook('Device', 'OnTogglePersonalLink', function(device)
    if nearby(device) then write('link_entity', psSnapshot(device:GetDevicePS())) end
  end, true)
  hook('ScriptableDeviceComponentPS', 'OnQuestForceON', function(ps)
    if playerNearby() then write('quest_force_on', psSnapshot(ps)) end
  end)
  hook('HUDProgressBarController', 'Outro', function(controller)
    if playerNearby() then write('hud_outro', {
      progress=call(function() return controller.valueSaved end),
      title=call(function() return controller.m_title end)}) end
  end, true)
  hook('GameObject', 'StartStatusEffectVFX', function(target, event)
    local id = call(function() return event.staticData:GetID() end)
    if id ~= tostring(TweakDBID.new('BaseStatusEffect.GhostlineVelvetCrashShortBlind'))
      and id ~= tostring(TweakDBID.new('BaseStatusEffect.GhostlineVelvetCrashVision')) then return end
    write('heartbreaker_vfx', {status=id,
      record=call(function() return target:GetRecordID() end),
      template=call(function() return TweakDB:GetRecord(target:GetRecordID()):EntityTemplatePath() end),
      has_spawner=call(function() return target:FindComponentByName(CName.new('ghostline_velvet_crash_fx')) ~= nil end),
      vfx_count=call(function() return #TweakDB:GetFlat('BaseStatusEffect.GhostlineVelvetCrashShortBlind.VFX') end)})
  end, true)
  local lastQuestState = ''
  local function tick(delta)
    elapsed = elapsed + delta
    if elapsed - lastPoll < 1 then return end
    lastPoll = elapsed
    local state = {}
    for _, fact in ipairs({'gq004_patch_uploaded', 'gq004_operation_left', 'gq004_debrief_done', 'gq004_reward_granted', 'gq004_reward_delivery_verified',
      'gq004_completed', 'gq004_epilogue_started', 'gq004_epilogue_done'}) do
      state[fact] = call(function() return Game.GetQuestsSystem():GetFactStr(fact) end)
    end
    local encodedState = json.encode(state)
    if encodedState ~= lastQuestState then write('quest_finish_state', state); lastQuestState = encodedState end
    if not playerNearby() then return end
    local ok, detail = pcall(function()
      local player = Game.GetPlayer()
      local entity = Game.GetTargetingSystem():GetLookAtObject(player, false, false)
      local row = {facts={}}
      for _, fact in ipairs({'gq004_job_accepted', 'gq004_operation_reached',
          'gq004_prototype_recovered', 'gq004_patch_uploaded', 'gq004_link_interrupted'}) do
        row.facts[fact] = call(function() return Game.GetQuestsSystem():GetFactStr(fact) end)
      end
      if nearby(entity) then
        row.target_class = call(function() return entity:GetClassName() end)
        local hasPS, ps = pcall(function() return entity:GetDevicePS() end)
        if hasPS and ps then row.device = psSnapshot(ps) end
      end
      local encoded = json.encode(row)
      if encoded ~= lastSnapshot then write('snapshot', row); lastSnapshot = encoded end
    end)
    if not ok and tostring(detail) ~= lastSnapshot then
      write('poll_error', {detail=tostring(detail)}); lastSnapshot = tostring(detail)
    end
  end
  local records = {}
  for _, record in ipairs({'Interactions.GhostlineLoveRecover', 'Interactions.GhostlineLoveUpload'}) do
    records[record] = {}
    for _, flat in ipairs({'name', 'action', 'caption'}) do
      records[record][flat] = call(function() return TweakDB:GetFlat(record .. '.' .. flat) end)
    end
  end
  write('trace_started', {interactions=records})
  print('[Love Actually] Read-only link trace: ' .. filename)
  return tick
end
