import Audioware.DynamicEmitterEvent
import Audioware.EmitterSettings
import Audioware.AudioSettingsExt

// No authored scene, localization key or WEM is involved in these utterances.
@addMethod(GameObject)
public func GhostlineNPCPrototypePlay(eventName: CName) -> ref<DynamicEmitterEvent> {
  let audio = GameInstance.GetAudioSystemExt(this.GetGame());
  let id = this.GetEntityID();
  let tag = n"ghostline_npc_runtime";
  if !audio.IsRegisteredEmitter(id, tag) && !audio.RegisterEmitter(id, tag) {
    return null;
  }
  let sound = DynamicEmitterEvent.Create(eventName, tag);
  this.QueueEvent(sound);
  return sound;
}

@addMethod(GameObject)
public func GhostlineNPCPrototypeUnregister() -> Void {
  GameInstance.GetAudioSystemExt(this.GetGame()).UnregisterEmitter(this.GetEntityID(), n"ghostline_npc_runtime");
}

@addMethod(GameObject)
public func GhostlineNPCPrototypeSubtitle(id: Uint64, text: String, duration: Float) -> Void {
  let line: scnDialogLineData;
  line.id = CreateCRUID(id);
  line.text = text;
  line.duration = duration;
  line.speaker = this;
  line.speakerName = "Patch";
  line.type = scnDialogLineType.Regular;
  line.isPersistent = false;
  GameInstance.GetBlackboardSystem(this.GetGame()).Get(GetAllBlackboardDefs().UIGameData)
    .SetVariant(GetAllBlackboardDefs().UIGameData.ShowDialogLine, ToVariant([line]), true);
}

@addMethod(GameObject)
public func GhostlineNPCPrototypeHideSubtitle(id: Uint64) -> Void {
  GameInstance.GetBlackboardSystem(this.GetGame()).Get(GetAllBlackboardDefs().UIGameData)
    .SetVariant(GetAllBlackboardDefs().UIGameData.HideDialogLine, ToVariant([CreateCRUID(id)]), true);
}

// Observed by the CET harness; native callback signatures are kept in REDscript.
public class GhostlineNPCPrototypeLifecycle extends ScriptableService {
  private cb func OnLoad() {
    GameInstance.GetCallbackSystem().RegisterCallback(n"Session/Pause", this, n"OnPause");
    GameInstance.GetCallbackSystem().RegisterCallback(n"Session/Resume", this, n"OnResume");
    GameInstance.GetCallbackSystem().RegisterCallback(n"Session/BeforeEnd", this, n"OnEnd");
    GameInstance.GetCallbackSystem().RegisterCallback(n"Entity/Detach", this, n"OnEntityDetach")
      .AddTarget(EntityTarget.RecordID(t"Character.GhostlineRuntimePatch"));
  }
  public cb func OnPause(event: ref<GameSessionEvent>) {}
  public cb func OnResume(event: ref<GameSessionEvent>) {}
  public cb func OnEnd(event: ref<GameSessionEvent>) {}
  public cb func OnEntityDetach(event: ref<EntityLifecycleEvent>) {}
}
