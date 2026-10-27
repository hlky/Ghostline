-- Exercises the real frontend against save-owned system snapshots.
local job = dofile("projects/experiments/npc-runtime/source/resources/bin/x64/plugins/cyber_engine_tweaks/mods/ghostline_npc_runtime/job.lua")
local state = {phase=0, sequence=0, revision=42, error="", transferring=false}
local choices, payouts, ticks = nil, 0, 0
local player = {
  GhostlineDataTheftState=function() return state end,
  GhostlineDataTheftOffer=function() state.phase=1; state.sequence=state.sequence+1; return true end,
  GhostlineDataTheftAccept=function(_, n) assert(n==state.sequence); state.phase=2; return true end,
  GhostlineDataTheftDecline=function() state.phase=8; return true end,
  GhostlineDataTheftAbandon=function() state.phase=6; return true end,
  GhostlineDataTheftChoose=function(_, outcome, n)
    assert(n==state.sequence and state.phase==4)
    state.phase=5; state.outcome=outcome; payouts=payouts+1; return true
  end,
  GhostlineDataTheftTick=function() ticks=ticks+1 end
}
Game={GetPlayer=function() return player end}
local dialogue={hide=function(owner) assert(owner=="job") end,
  show=function(options, context) assert(context.owner=="job"); choices=options; return true end}
job.init({revision=42, offer="Offer", choice_labels={deliver="Deliver", keep_copy="Keep copy"}}, dialogue, function() end)
job.offer()
local stale=choices[1].callback
job.reset() -- A saved run may have identical sequence numbers after loading.
state={phase=1, sequence=1, revision=42, error=""}
stale()
assert(state.phase==1, "old save's callback cannot accept the new save's job")
job.choices(); choices[1].callback(); assert(state.phase==2)
state.phase=4
job.choices(); local deliver=choices[1].callback; deliver(); deliver()
assert(payouts==1 and state.outcome==1, "duplicate callback must not pay twice")
job.offer(); state.phase=4; job.choices(); choices[2].callback()
assert(payouts==2 and state.outcome==2)
job.offer(); local invalid=choices[1].callback; state.revision=43; invalid(); assert(state.phase==1)
job.pause(true); job.update(1); assert(ticks==0)
job.pause(false); job.update(0.1); assert(ticks==1)
job.abandon(); assert(state.phase==6)
print("Job frontend save-boundary, stale-choice, duplicate-outcome and pause checks passed")
