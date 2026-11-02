-- Exercise lease-file read failures without a running game.
local callbacks,files={},{}
local now,released=100,0
local realOpen=io.open
os.time=function() return now end
json={encode=function(v) return v end,decode=function(v) return v end}
io.open=function(path,mode)
    if mode=='r' then
        if not files[path] then return nil end
        return {read=function() return files[path] end,close=function() end}
    end
    return {write=function(_,v) files[path]=v end,close=function() end}
end
os.remove=function(path) files[path]=nil end
os.rename=function(a,b) files[b]=files[a]; files[a]=nil; return true end
registerForEvent=function(name,fn) callbacks[name]=fn end
registerHotkey=function() end
package.preload.engine=function() return {new=function() return {
    status=function() return {} end,observers=function() end,
    begin=function() end,release=function() released=released+1; return {} end,
    update=function() end,hide=function() end,
} end} end
local runtime=dofile(arg[1])
callbacks.onInit()
local boot=files['runtime/state.json'].boot
local function begin(id)
    files['runtime/lease.json']={session=id,timestamp=now}
    files['runtime/command.json']={id=id,boot=boot,session=id,kind='begin',arguments={},expires=now+40}
    callbacks.onUpdate(.1)
    assert(runtime.status().session==id)
end
begin('one')
files['runtime/lease.json']=nil
now=102; callbacks.onUpdate(.1)
assert(runtime.status().session=='one','one unreadable lease must not release control')
files['runtime/lease.json']={session='one',timestamp=102}
now=104; callbacks.onUpdate(.1)
assert(runtime.status().session=='one','heartbeat must renew the cached lease')
files['runtime/lease.json']=nil
now=108; callbacks.onUpdate(.1)
assert(runtime.status().session==nil and released==1,'missing heartbeat must still expire')
begin('two')
files['runtime/stop.json']={id='stop',session='two'}
callbacks.onUpdate(.1)
assert(runtime.status().session==nil and released==2,'explicit stop must remain immediate')
io.open=realOpen
print('PASS: transient read, renewal, watchdog expiry, immediate stop')
