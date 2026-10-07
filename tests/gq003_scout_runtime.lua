-- Executed by Python in an isolated temporary working directory.
local source = assert(arg[1])
local scenario = assert(arg[2])
local events, hotkeys, buttons, labels = {}, {}, {}, {}
local lastTeleport
local player = {
    GetWorldPosition = function() return {x=1,y=2,z=3} end,
    GetWorldForward = function() return {x=0,y=1,z=0} end,
}
math.atan2 = math.atan2 or function(y,x) return math.atan(y,x) end
Game = {GetPlayer=function() return player end, GetTeleportationFacility=function()
    return {Teleport=function(_, _, position) lastTeleport=position end}
end}
Vector4 = {new=function(x,y,z,w) return {x=x,y=y,z=z,w=w} end}
EulerAngles = {new=function() return {} end}
registerForEvent=function(name, fn) events[name]=fn end
registerHotkey=function(name, _, fn) hotkeys[name]=fn end
ImGuiCond={FirstUseEver=1}
ImGui=setmetatable({
    Begin=function() return true end,
    CollapsingHeader=function() return true end,
    Button=function(label) local hit=buttons[label]; buttons[label]=nil; return hit end,
    Selectable=function(label) labels[#labels+1]=label; return false end,
    InputTextWithHint=function(_,_,value) return value,false end,
}, {__index=function() return function() end end})
local original={schema_version=1,quest='gq003',next_id=2,captures={
    {id='gq003-001',slot_id='freight_yard',target_id='site_origin',position={x=4,y=5,z=6}},
}}
json={encode=function(value) return 'saved:' .. #value.captures end,
      decode=function() if scenario=='malformed' then error('bad JSON') end return original end}
local path='black-lantern-locations.json'
local function read(p) local f=io.open(p,'r'); if not f then return nil end local s=f:read('*a'); f:close(); return s end
if scenario~='presets' then local f=assert(io.open(path,'w')); f:write('original'); f:close() end
dofile(source)
events.onInit()
if scenario=='malformed' then
    hotkeys.ghostline_gq003_capture()
    assert(read(path)=='original', 'Malformed log overwritten')
elseif scenario=='rename_failure' then
    local rename=os.rename
    os.rename=function(a,b) if a==path..'.tmp' then return nil,'simulated failure' end return rename(a,b) end
    hotkeys.ghostline_gq003_capture()
    assert(read(path)=='original', 'Previous log not restored')
    assert(read(path..'.tmp')=='saved:2', 'Recovery payload discarded')
elseif scenario=='save' then
    hotkeys.ghostline_gq003_capture()
    assert(read(path)=='saved:2')
    assert(read(path..'.bak.1')=='original')
else
    events.onOverlayOpen()
    local sites={'Iris briefing / safe site','Freight yard','Memory clinic','Freight interchange','Reconstruction relay','Delivery drop point'}
    for i,site in ipairs(sites) do
        if i>1 then buttons[site..'##slot'..i]=true end
        events.onDraw()
        if i==2 then
            buttons['Explore: Anonymous Northside yard##preset2']=true
            events.onDraw()
            assert(lastTeleport.x==-2040 and lastTeleport.y==2665)
            hotkeys.ghostline_gq003_return()
            assert(lastTeleport.x==1 and lastTeleport.y==2)
        end
    end
    local all=table.concat(labels,'\n')
    for _,name in ipairs({'Briefing setup trigger','Safe-site setup trigger','Mara initial spawn','Patch spawn','Defense attacker spawn','Quest mappin'}) do
        assert(all:find(name,1,true), 'Missing target '..name)
    end
    assert(read(path)==nil, 'Exploration should not create captures')
end
print('PASS '..scenario)
