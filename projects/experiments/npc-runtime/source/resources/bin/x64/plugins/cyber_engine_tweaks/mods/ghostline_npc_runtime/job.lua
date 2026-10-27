-- UI is disposable; the REDscript system owns save-specific gameplay state.
local M = {}
local plan, dialogue, log, paused, epoch = nil, nil, print, false, 0
local context = {owner = "job", title = "Borrowed Credentials", id = 187320002}
local phases = {[0]="idle", "offered", "reach target", "download credentials", "delivery choice",
  "completed", "abandoned", "unavailable", "declined"}

local function player() return Game.GetPlayer() end
local function snapshot()
  local p = player()
  return p and p:GhostlineDataTheftState() or nil
end
local function guarded(s, callback)
  local turn, sequence, phase = epoch, s.sequence, s.phase
  return function()
    local current = snapshot()
    if paused or turn ~= epoch or not current or current.sequence ~= sequence
      or current.phase ~= phase or current.revision ~= plan.revision then return end
    if not callback(player(), sequence) then log("Job action rejected; reopen choices to refresh.") end
  end
end

function M.init(value, ui, logger)
  plan, dialogue, log = value, ui, logger
end
function M.hide()
  epoch = epoch + 1
  if dialogue then dialogue.hide("job") end
end
function M.pause(value)
  paused = value
  if value then M.hide() end
end
function M.reset()
  M.hide()
  paused = false
end
function M.offer()
  if not plan then log("Job contract is missing."); return end
  local p = player()
  if not p then log("Load a save first."); return end
  if not p:GhostlineDataTheftOffer() then
    local s = snapshot()
    log(s and s.error or "Job offer failed.")
    return
  end
  log(plan.offer)
  M.choices()
end
function M.choices()
  if paused or not plan or not dialogue then return end
  M.hide()
  local s = snapshot()
  if not s then log("Load a save first."); return end
  if s.revision ~= plan.revision then log("Saved job has a different contract. Offer a fresh job."); return end
  local options
  if s.phase == 1 then
    options = {
      {label="Accept job (500 eddies)", callback=guarded(s, function(p, n) return p:GhostlineDataTheftAccept(n) end)},
      {label="Decline job", callback=guarded(s, function(p, n) return p:GhostlineDataTheftDecline(n) end)}
    }
  elseif s.phase == 4 then
    options = {
      {label=plan.choice_labels.deliver, callback=guarded(s, function(p, n) return p:GhostlineDataTheftChoose(1, n) end)},
      {label=plan.choice_labels.keep_copy, callback=guarded(s, function(p, n) return p:GhostlineDataTheftChoose(2, n) end)}
    }
  else
    log(M.status())
    return
  end
  local ok, reason = dialogue.show(options, context)
  if not ok then log(reason) end
end
function M.abandon()
  M.hide()
  local p, s = player(), snapshot()
  if p and s then p:GhostlineDataTheftAbandon(s.sequence) end
end
function M.update(delta)
  if paused or not plan then return end
  local p = player()
  if not p then return end
  local ok, reason = pcall(function() p:GhostlineDataTheftTick(delta) end)
  if not ok then M.pause(true); log("Job runtime error: " .. tostring(reason)) end
end
function M.status()
  if not plan then return "Job: unavailable (missing contract)" end
  local s = snapshot()
  if not s then return "Job: no loaded save" end
  local value = "Job: " .. (phases[s.phase] or "unknown") .. " / run " .. tostring(s.sequence)
  if s.transferring then value = value .. " / " .. tostring(math.floor(s.progress * 100)) .. "%" end
  if s.error and s.error ~= "" then value = value .. " / " .. s.error end
  return value
end

return M
