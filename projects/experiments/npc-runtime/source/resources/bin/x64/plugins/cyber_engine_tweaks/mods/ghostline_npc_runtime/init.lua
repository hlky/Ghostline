local dialogue = require("dialogue")
local job = require("job")
local contract, utterances = nil, {}
local state, paused, overlay = "idle", false, false
local npcID, target, sound, line, subtitleID = nil, nil, nil, nil, nil
local elapsed, preparing, poll, frame = 0, 0, 0, 1
local sequence, requestToken, requestPoll = 0, nil, 0
local lastValues = {}
local stop, showChoices
local SLOT = "ghostline_npc_runtime_slot_0"

local function log(message) print("[NPC Runtime] " .. message) end

local function readJSON(path)
  local file = io.open(path, "rb")
  if not file then return nil end
  local contents = file:read("*a")
  file:close()
  local ok, value = pcall(json.decode, contents)
  if ok then return value end
  return nil
end

local function writeRequest(value)
  local temporary = "slot-request.json.tmp"
  local file, error = io.open(temporary, "wb")
  if not file then return false, error end
  local written, writeError = file:write(json.encode(value))
  local closed, closeError = file:close()
  if not written or not closed then return false, writeError or closeError end
  os.remove("slot-request.json")
  return os.rename(temporary, "slot-request.json")
end

local function resolveTarget()
  if not npcID then return nil end
  return Game.GetDynamicEntitySystem():GetEntity(npcID)
end

local function input(name, value)
  AnimationControllerComponent.SetInputFloat(target, CName.new(name), value)
end

local function releaseFace()
  if target and contract then
    pcall(input, contract.gate, 0)
  end
  lastValues = {}
end

stop = function(reason)
  state, requestToken = "idle", nil
  dialogue.hide("npc")
  if sound then pcall(function() sound:Stop() end) end
  if target and subtitleID then
    pcall(function() target:GhostlineNPCPrototypeHideSubtitle(subtitleID) end)
  end
  releaseFace()
  if target then pcall(function() target:GhostlineNPCPrototypeUnregister() end) end
  sound, line, subtitleID = nil, nil, nil
  if reason then log("Stopped: " .. reason) end
end

local function play(id)
  if paused or overlay then log("Close the overlay and resume before playback."); return end
  stop()
  target = resolveTarget()
  if not target then log("Spawn the experiment NPC first."); return end
  line = utterances[id]
  if not line then log("Unknown utterance: " .. tostring(id)); return end
  sequence = sequence + 1
  -- Startup nonce prevents acknowledgements from earlier CET reloads matching.
  requestToken = tostring(os.time()) .. ":" .. tostring(math.random(1, 1000000000)) .. ":" .. tostring(sequence)
  local ok, error = writeRequest({token = requestToken, utterance_id = id})
  if not ok then stop("Cannot publish slot request: " .. tostring(error)); return end
  elapsed, preparing, poll, requestPoll, frame = 0, 0, 0, 0, 1
  state = "preparing"
end

showChoices = function()
  if paused or overlay then return end
  target = resolveTarget()
  if not target then stop("NPC is unavailable"); return end
  state = "choices"
  local ok, error = dialogue.show({
    { label = "Why pull me in?", callback = function() play("why_you") end },
    { label = "Who's behind it?", callback = function() play("client") end },
    { label = "That's all for now.", callback = function() stop("conversation ended") end }
  })
  if not ok then stop(error) end
end

local function spawn()
  stop()
  local player = Game.GetPlayer()
  local system = Game.GetDynamicEntitySystem()
  if not player or not system:IsReady() then log("Load a save first."); return end
  if npcID then system:DeleteEntity(npcID) end
  local position, forward, orientation = player:GetWorldPosition(), player:GetWorldForward(), player:GetWorldOrientation()
  local spec = DynamicEntitySpec.new()
  spec.recordID = TweakDBID.new(contract.record)
  spec.appearanceName = CName.new("ghostline_patch_default")
  spec.position = Vector4.new(position.x + forward.x * 2.0, position.y + forward.y * 2.0, position.z, 1)
  spec.orientation = Quaternion.new(-orientation.j, orientation.i, orientation.r, -orientation.k)
  spec.persistState, spec.persistSpawn = false, false
  spec.alwaysSpawned, spec.spawnInView, spec.active = true, true, true
  npcID = system:CreateEntity(spec)
  target = nil
  log("Spawn requested. Wait for Patch, then open the conversation or run the jaw probe.")
end

local function jawProbe()
  stop()
  target = resolveTarget()
  if not target then log("Spawn the experiment NPC first."); return end
  local name = contract.inputs.jaw_mid_openLipsyncPoseOutput
  if not name then log("Graph contract has no jaw track."); return end
  -- Populate the complete override branch before enabling it.
  for _, key in pairs(contract.inputs) do input(key, 0) end
  input(name, 0.7)
  input(contract.inputs.jaw_mid_openAnimOverrideWeight, -0.7)
  input(contract.gate, 1)
  state, elapsed = "jaw_probe", 0
  log("Jaw input requested for 1.5 seconds; visible motion must be confirmed in-game.")
end

local function applyCurves(time)
  local curves = line.curves
  while frame < #curves.times - 1 and curves.times[frame + 1] <= time do frame = frame + 1 end
  local nextFrame = math.min(frame + 1, #curves.times)
  local span = curves.times[nextFrame] - curves.times[frame]
  local weight = span > 0 and math.min(1, math.max(0, (time - curves.times[frame]) / span)) or 0
  for index, track in ipairs(curves.tracks) do
    local a, b = curves.values[frame][index], curves.values[nextFrame][index]
    local value = a + (b - a) * weight
    if not lastValues[index] or math.abs(value - lastValues[index]) > 0.0001 then
      input(contract.inputs[track], value)
      lastValues[index] = value
    end
  end
end

local function update(delta)
  if state == "idle" or paused then return end
  target = resolveTarget()
  if not target then stop("NPC detached"); return end
  if state == "choices" then return end
  preparing = preparing + delta
  if state == "jaw_probe" then
    elapsed = elapsed + delta
    if elapsed >= 1.5 then stop("jaw probe finished") end
    return
  end
  if state == "preparing" then
    requestPoll = requestPoll + delta
    if requestPoll >= 0.1 then
      requestPoll = 0
      local response = readJSON("slot-ready.json")
      if response and response.token == requestToken then
        if response.status ~= "ready" then stop(response.error or "slot worker failed"); return end
        if response.sha256 ~= line.audio.sha256 then stop("Slot response has a different audio digest"); return end
        sound = target:GhostlineNPCPrototypePlay(CName.new(SLOT))
        if not sound then stop("Audioware emitter registration failed"); return end
        state, poll, preparing = "starting", 0.25, 0
      end
    end
    if preparing > 10 then stop("Slot worker timed out; start npc_runtime_slot_worker.py") end
    return
  end
  poll = poll + delta
  if state == "speaking" then elapsed = elapsed + delta end
  if poll >= 0.25 then
    poll = 0
    local position = sound:Position()
    if position and position > 0 then
      elapsed = position
      if state == "starting" then
        applyCurves(elapsed)
        input(contract.gate, 1)
        sequence = sequence + 1
        subtitleID = os.time() * 1000000 + math.random(1, 999999)
        target:GhostlineNPCPrototypeSubtitle(subtitleID, line.subtitles[1].text, line.audio.duration - elapsed)
        state = "speaking"
        log("Playback started after " .. string.format("%.3f", preparing) .. "s; " .. line.utterance_id)
      end
    end
  end
  if state == "starting" and preparing > 5 then stop("Audioware playback did not start"); return end
  if state == "speaking" then
    if elapsed >= line.audio.duration then
      stop()
      showChoices()
    else
      applyCurves(elapsed)
    end
  end
end

registerForEvent("onInit", function()
  contract = readJSON("graph-contract.json")
  utterances.why_you = readJSON("utterances/why_you.json")
  utterances.client = readJSON("utterances/client.json")
  if not contract or not utterances.why_you or not utterances.client then
    log("Build/install data is missing; prototype disabled.")
    contract = nil
    return
  end
  job.init(readJSON("job-plan.json"), dialogue, log)
  dialogue.init(function(reason) job.hide(); stop(reason) end)
  Observe("GhostlineNPCPrototypeLifecycle", "OnPause", function()
    paused = true
    job.pause(true)
    dialogue.hide("npc")
    if sound then sound:Pause() end
  end)
  Observe("GhostlineNPCPrototypeLifecycle", "OnResume", function()
    paused = false
    job.pause(false)
    if sound then sound:Resume() end
    if state == "choices" then showChoices() end
  end)
  Observe("GhostlineNPCPrototypeLifecycle", "OnEnd", function()
    job.reset()
    stop("session ended")
    npcID, target, paused = nil, nil, false
    dialogue.reset()
  end)
  Observe("GhostlineNPCPrototypeLifecycle", "OnEntityDetach", function() stop("experiment NPC detached") end)
  log("Loaded. This is an unproven presentation experiment, not an LLM conversation system.")
end)

registerForEvent("onUpdate", function(delta)
  if not contract then return end
  job.update(delta)
  local ok, error = pcall(update, delta)
  if not ok then stop("Runtime API error: " .. tostring(error)) end
end)
registerForEvent("onShutdown", function() job.reset(); stop("CET shutdown") end)
registerForEvent("onOverlayOpen", function() overlay = true; job.pause(true); stop("overlay opened") end)
registerForEvent("onOverlayClose", function() overlay = false; job.pause(paused) end)
registerForEvent("onDraw", function()
  if not overlay then return end
  if ImGui.Begin("Ghostline NPC Runtime") then
    ImGui.Text("State: " .. state)
    ImGui.Text(job.status())
    ImGui.Text("Bind prototype hotkeys under CET Bindings.")
    ImGui.Text("Start the external slot worker before speaking.")
  end
  ImGui.End()
end)

registerHotkey("npc_runtime_spawn", "NPC Runtime: spawn isolated Patch", function() if contract then spawn() end end)
registerHotkey("npc_runtime_jaw", "NPC Runtime: jaw probe", function() if contract then jawProbe() end end)
registerHotkey("npc_runtime_choices", "NPC Runtime: open conversation", function() if contract then stop(); showChoices() end end)
registerHotkey("npc_runtime_line_a", "NPC Runtime: play Why me", function() if contract then play("why_you") end end)
registerHotkey("npc_runtime_line_b", "NPC Runtime: play Client", function() if contract then play("client") end end)
registerHotkey("npc_runtime_stop", "NPC Runtime: stop and release face", function() stop("manual interruption") end)
registerHotkey("npc_runtime_remove", "NPC Runtime: remove experiment NPC", function()
  stop("manual removal")
  if npcID then Game.GetDynamicEntitySystem():DeleteEntity(npcID) end
  npcID, target = nil, nil
end)

registerHotkey("npc_runtime_job_offer", "NPC Runtime: offer fixed data-theft job", function() job.offer() end)
registerHotkey("npc_runtime_job_choices", "NPC Runtime: open data-theft job choices", function() job.choices() end)
registerHotkey("npc_runtime_job_abandon", "NPC Runtime: abandon data-theft job", function() job.abandon() end)

return { job = job, stop = stop, play = play, jawProbe = jawProbe, state = function() return state end }
