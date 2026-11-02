-- Independent telemetry/session protocol; actual input is bounded Windows input.
local engine=require('engine').new()
local boot=tostring(os.time())..'_'..tostring(math.random(1,2147483647))
local session,lastCommand,lastStop
local elapsed=0
local function read(name)
    local f=io.open('runtime/'..name..'.json','r'); if not f then return nil end
    local raw=f:read('*a');f:close()
    local ok,value=pcall(json.decode,raw); if ok and type(value)=='table' then return value end
end
local function write(name,value)
    local path='runtime/'..name..'.json'
    local f=io.open(path..'.tmp','w');if not f then return end
    f:write(json.encode(value));f:close();os.remove(path);os.rename(path..'.tmp',path)
end
local function state()
    local s=engine:status();s.boot=boot;s.session=session;return s
end
local function stop() session=nil;write('state',state()) end
local function poll()
    local request=read('stop')
    if request and request.id~=lastStop then
        lastStop=request.id
        if session and request.session==session then stop() end
    end
    if session then
        local lease=read('lease')
        if not lease or lease.session~=session or os.time()-lease.timestamp>2 or not engine:status().ready then stop() end
    end
    local command=read('command')
    if command and command.id~=lastCommand then
        lastCommand=command.id
        local ok,result=pcall(function()
            if command.boot~=boot or type(command.expires)~='number' or command.expires<os.time() then error('Stale command') end
            if command.kind=='begin' then
                if session and session~=command.session then error('Another gameplay session owns the runtime') end
                local lease=read('lease')
                if not lease or lease.session~=command.session or os.time()-lease.timestamp>2 then error('Missing controller lease') end
                engine:begin();session=command.session;return state()
            end
            if not session or command.session~=session then error('Session mismatch') end
            if command.kind=='end' then stop();return {released=true} end
            error('Unknown command')
        end)
        write('response',{id=command.id,session=command.session,boot=boot,ok=ok,
            result=ok and result or nil,error=not ok and tostring(result) or nil})
    end
    write('state',state())
end
registerForEvent('onInit',function() engine:observers();write('state',state()) end)
registerForEvent('onUpdate',function(delta)
    engine.frame=engine.frame+1;elapsed=elapsed+math.max(0,delta)
    if elapsed>=0.05 then elapsed=0;local ok,err=pcall(poll);if not ok then stop();print('[Cyberpunk MCP] '..tostring(err)) end end
end)
registerForEvent('onOverlayOpen',function() engine.overlay=true;stop() end)
registerForEvent('onOverlayClose',function() engine.overlay=false end)
registerForEvent('onShutdown',stop)
registerHotkey('cyberpunk_mcp_stop','Cyberpunk MCP: emergency stop',stop)
return {status=state,stop=stop}
