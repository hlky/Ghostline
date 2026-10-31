local Survey=dofile(arg[1])
local callbacks={}
Observe=function(class,event,callback) callbacks[class..':'..event]=callback end
Vector4={new=function(x,y,z,w) return {x=x,y=y,z=z,w=w} end}
EulerAngles={new=function(roll,pitch,yaw) return {roll=roll,pitch=pitch,yaw=yaw,
 ToQuat=function(self) return {pitch=self.pitch,yaw=self.yaw,roll=self.roll} end} end}
local position,bodyYaw={x=0,y=0,z=0},0
local localRotation={pitch=7,yaw=3,roll=0}
local camera={pitchMin=-90,pitchMax=90,GetLocalOrientation=function() return localRotation end,
 ResetPitch=function() end,SetLocalOrientation=function(_,rotation) localRotation=rotation end}
local player={IsAttached=function() return true end,GetWorldPosition=function() return position end,
 GetWorldForward=function() return {x=-math.sin(math.rad(bodyYaw)),y=math.cos(math.rad(bodyYaw)),z=0} end,
 GetFPPCameraComponent=function() return camera end}
local loadingStart,loadingFinish=false,false
local obstruction=false
local rayFailure=false
local teleports=0
Game={GetPlayer=function() return player end,GetCameraSystem=function() return {
 GetActiveCameraForward=function()
  local y,p=math.rad(bodyYaw+localRotation.yaw),math.rad(math.max(camera.pitchMin,math.min(camera.pitchMax,localRotation.pitch)))
  return {x=-math.sin(y)*math.cos(p),y=math.cos(y)*math.cos(p),z=math.sin(p)}
 end,
 GetActiveCameraRight=function() return {z=0} end,GetActiveCameraUp=function() return {z=1} end,
} end,
GetTargetingSystem=function() return {GetCrosshairData=function() return {x=position.x,y=position.y,z=position.z+1.7} end} end,
GetAllBlackboardDefs=function() return {FastTRavelSystem={FastTravelLoadingScreenStarted='start',FastTravelLoadingScreenFinished='finish'}} end,
GetBlackboardSystem=function() return {Get=function() return {GetBool=function(_,key) if key=='start' then return loadingStart else return loadingFinish end end} end} end,
GetSpatialQueriesSystem=function() return {SyncRaycastByCollisionGroup=function(_,a,b,group)
 if rayFailure then error('no spatial queries') end
 return obstruction and group=='Static' and math.abs(a.x)<0.5 and a.y<0.6 and b.y>0.6
end} end,
GetTeleportationFacility=function() return {Teleport=function(_,entity,where,rotation)
 position=where;bodyYaw=rotation.yaw;teleports=teleports+1
end} end}

local state={active=true,snapshot={},command={pose={x=0,y=0,z=0,yaw=90,pitch=-20,roll=0},survey={
 local_move_maximum_m=20,local_move_speed_mps=10,near_obstruction_m=2.5,maximum_recoveries=2,obstruction_enabled=true}}}
state.command.effective_pose=state.command.pose
assert(Survey.holdCamera(state))
local actual=Survey.readPose(player)
assert(math.abs(actual.yaw-90)<1e-6 and math.abs(actual.pitch+20)<1e-6,'camera angles must be measured, not invented')
assert(actual.camera_pose.z==1.7 and actual.z==0,'camera and player positions must be distinguished')
local rotations=teleports
assert(Survey.startMovement(state)=='stationary' and teleports==rotations,'stationary survey must not change position')
state.command.effective_pose={x=10,y=0,z=0,yaw=0,pitch=0,roll=0}
assert(Survey.startMovement(state)=='local_flight')
assert(not Survey.advanceMovement(state,0.5) and position.x==5)
assert(Survey.advanceMovement(state,0.5) and position.x==10)
assert(Survey.restoreCamera(state) and localRotation.pitch==7,'restore original camera orientation')

Survey.installLoadingObservers()
local visible=true
local controller={GetRootWidget=function() return {IsVisible=function() return visible end} end}
callbacks['DefaultLoadingScreenLogicController:OnInitialize'](controller)
assert(Survey.loadingState(),'parent loading controller must gate even without a progress bar')
visible=false;assert(not Survey.loadingState(),'hidden parent must not poison readiness')
callbacks['DefaultLoadingScreenLogicController:OnUninitialize']()
loadingStart=true;loadingFinish=false;assert(Survey.loadingState())
loadingFinish=true;assert(not Survey.loadingState(),'finished transition must release the loading gate')

position={x=0,y=0,z=0};bodyYaw=0;localRotation={pitch=0,yaw=0,roll=0};obstruction=true
state.command.effective_pose={x=0,y=0,z=0,yaw=0,pitch=0,roll=0}
state.command.recovery_candidates={{x=1.5,y=0,z=0,yaw=0,pitch=0,roll=0}}
assert(Survey.recoverObstruction(state),'foreground obstruction must trigger a bounded lateral recovery')
assert(state.command.effective_pose.x==1.5 and state.surveyRecoveries==1)
state.surveyRecoveries=2;state.surveyObstructionChecked=false
assert(not Survey.recoverObstruction(state),'recovery count must remain bounded')
rayFailure=true
assert(not Survey.pathClear({x=0,y=0,z=2},{x=2,y=0,z=2}),'failed collision query must not authorize a movement')
print('Camera readback, loading lifecycle, local flight, and obstruction recovery passed')
