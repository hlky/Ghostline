-- Offline lifecycle/transport check. This does not simulate REDengine facial evaluation.
local events, observers, keys, calls, response = {}, {}, {}, {}, nil
local pending
local track = "jaw_mid_openLipsyncPoseOutput"
local contract = {gate = "gate", record = "Character.GhostlineRuntimePatch", inputs = {
  [track] = "jaw", jaw_mid_openAnimOverrideWeight = "jaw_override"
}}
local line = {utterance_id = "why_you", audio = {sha256 = "digest", duration = 1},
  curves = {tracks = {track}, times = {0, 1}, values = {{0}, {0.5}}},
  subtitles = {{text = "Hello"}}}
local files = { ["graph-contract.json"] = contract, ["utterances/why_you.json"] = line,
  ["utterances/client.json"] = line }
json = {decode = function(path) return path == "slot-ready.json" and response or files[path] end,
  encode = function(value) pending = value; return "request" end}
io.open = function(path, mode)
  if mode == "wb" then return {write = function() return true end, close = function() return true end} end
  if files[path] or path == "slot-ready.json" then
    return {read = function() return path end, close = function() return true end}
  end
end
os.remove, os.rename = function() return true end, function() return true end
registerForEvent = function(name, fn) events[name] = fn end
registerHotkey = function(name, _, fn) keys[name] = fn end
Observe = function(class, name, fn) observers[class .. "." .. name] = fn end
local dialogue = {hide = function() end, reset = function() end, init = function() end,
  show = function(options) calls.choices = options; return true end}
package.preload.dialogue = function() return dialogue end
package.preload.job = function()
  return dofile("projects/experiments/npc-runtime/source/resources/bin/x64/plugins/cyber_engine_tweaks/mods/ghostline_npc_runtime/job.lua")
end
CName, TweakDBID = {new = function(v) return v end}, {new = function(v) return v end}
Vector4, Quaternion, DynamicEntitySpec = {new = function() return {} end},
  {new = function() return {} end}, {new = function() return {} end}
AnimationControllerComponent = {SetInputFloat = function(_, name, value) calls[name] = value end}
local live = true
local sound = {Position = function() return 0.5 end,
  Stop = function() calls.stopped = true end,
  Pause = function() calls.paused = true end,
  Resume = function() calls.resumed = true end}
local target = {GhostlineNPCPrototypePlay = function() calls.plays = (calls.plays or 0) + 1; return sound end,
  GhostlineNPCPrototypeUnregister = function() end,
  GhostlineNPCPrototypeHideSubtitle = function() calls.hidden = true end,
  GhostlineNPCPrototypeSubtitle = function(_, _, text) calls.subtitle = text end}
local system = {IsReady = function() return true end, CreateEntity = function() return 7 end,
  GetEntity = function() return live and target or nil end, DeleteEntity = function() live = false end}
local player = {GetWorldPosition = function() return {x=0,y=0,z=0} end,
  GetWorldForward = function() return {x=0,y=1,z=0} end,
  GetWorldOrientation = function() return {i=0,j=0,k=0,r=1} end}
Game = {GetDynamicEntitySystem = function() return system end, GetPlayer = function() return player end}
local api = dofile("projects/experiments/npc-runtime/source/resources/bin/x64/plugins/cyber_engine_tweaks/mods/ghostline_npc_runtime/init.lua")
events.onInit()
keys.npc_runtime_spawn()
api.play("why_you")
assert(api.state() == "preparing")
response = {token = "old", status = "ready", sha256 = "digest"}
events.onUpdate(0.1)
assert(not calls.plays, "stale acknowledgement must not start audio")
response.token = pending.token
events.onUpdate(0.1)
assert(api.state() == "starting" and calls.plays == 1)
observers["GhostlineNPCPrototypeLifecycle.OnPause"]()
events.onUpdate(2)
assert(api.state() == "starting" and not calls.gate)
observers["GhostlineNPCPrototypeLifecycle.OnResume"]()
events.onUpdate(0.01)
assert(api.state() == "speaking" and calls.gate == 1 and calls.subtitle == "Hello")
api.stop("test interruption")
assert(api.state() == "idle" and calls.stopped and calls.hidden and calls.gate == 0)
local old = pending.token
api.play("client")
response.token = old
events.onUpdate(0.1)
assert(calls.plays == 1, "cancelled turn must not affect its replacement")
live = false
events.onUpdate(0.1)
assert(api.state() == "idle")
print("NPC harness lifecycle and stale-result checks passed")
