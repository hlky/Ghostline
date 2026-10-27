// Persistent gameplay state belongs to the save, never to CET's JSON files.
// Phase: 0 idle, 1 offered, 2 reach_area, 3 interact_device, 4 choice_gate,
//        5 completed, 6 abandoned, 7 unavailable/failed, 8 declined.
public class GhostlineDataTheftSnapshot extends IScriptable {
  public let phase: Int32;
  public let sequence: Int32;
  public let revision: Int32;
  public let target: EntityID;
  public let position: Vector4;
  public let outcome: Int32;
  public let dataAcquired: Bool;
  public let rewardApplied: Bool;
  public let deliveredCount: Int32;
  public let keptCopyCount: Int32;
  public let abandonedCount: Int32;
  public let transferring: Bool;
  public let progress: Float;
  public let error: String;
}

public class GhostlineDataTheftSystem extends ScriptableSystem {
  private persistent let phase: Int32;
  private persistent let sequence: Int32;
  private persistent let revision: Int32;
  private persistent let target: EntityID;
  private persistent let position: Vector4;
  private let transferActive: Bool;
  private let transferElapsed: Float;
  private let progressOwned: Bool;
  private persistent let outcome: Int32;
  private persistent let dataAcquired: Bool;
  private persistent let rewardApplied: Bool;
  private persistent let deliveredCount: Int32;
  private persistent let keptCopyCount: Int32;
  private persistent let abandonedCount: Int32;
  private let error: String;
  private let marker: NewMappinID;
  private let markerRegistered: Bool;

  public static func Get(game: GameInstance) -> ref<GhostlineDataTheftSystem> {
    return GameInstance.GetScriptableSystemsContainer(game).Get(n"GhostlineDataTheftSystem") as GhostlineDataTheftSystem;
  }

  private func OnAttach() {
    GameInstance.GetCallbackSystem().RegisterCallback(n"Session/BeforeSave", this, n"BeforeSave");
    this.markerRegistered = false;
  }

  private func OnDetach() {
    this.StopTransfer();
    this.RemoveMarker();
  }

  private cb func BeforeSave(event: ref<GameSessionEvent>) {
    // Recreated by Tick after saving/loading; do not persist ephemeral marker IDs.
    this.StopTransfer();
    this.RemoveMarker();
  }

  public func Snapshot() -> ref<GhostlineDataTheftSnapshot> {
    let result = new GhostlineDataTheftSnapshot();
    result.phase = this.phase;
    result.sequence = this.sequence;
    result.revision = this.revision;
    result.target = this.target;
    result.position = this.position;
    result.outcome = this.outcome;
    result.dataAcquired = this.dataAcquired;
    result.rewardApplied = this.rewardApplied;
    result.deliveredCount = this.deliveredCount;
    result.keptCopyCount = this.keptCopyCount;
    result.abandonedCount = this.abandonedCount;
    result.transferring = this.transferActive;
    result.progress = this.transferElapsed / GhostlineDataTheftConfig.Duration();
    result.error = this.error;
    return result;
  }

  private func Notify(text: String) -> Void {
    let message: SimpleScreenMessage;
    message.isShown = true;
    message.duration = 5.0;
    message.message = text;
    message.type = SimpleMessageType.Undefined;
    GameInstance.GetBlackboardSystem(this.GetGameInstance()).Get(GetAllBlackboardDefs().UI_Notifications)
      .SetVariant(GetAllBlackboardDefs().UI_Notifications.OnscreenMessage, ToVariant(message), true);
  }

  private func Active() -> Bool = this.phase >= 1 && this.phase <= 4;

  private func Compatible() -> Bool {
    if this.Active() && this.revision != GhostlineDataTheftConfig.Revision() {
      this.Fail("The saved job uses a different contract version. Offer a new job.");
      return false;
    }
    return true;
  }

  private func Point() -> ref<AccessPoint> {
    return GameInstance.FindEntityByID(this.GetGameInstance(), this.target) as AccessPoint;
  }

  private func NearTarget() -> Bool {
    let player = GetPlayer(this.GetGameInstance());
    return IsDefined(player) && Vector4.Distance(player.GetWorldPosition(), this.position) <= GhostlineDataTheftConfig.Radius();
  }

  private func SetFact(name: String, value: Int32) -> Void {
    GameInstance.GetQuestsSystem(this.GetGameInstance()).SetFactStr(name, value);
  }

  private func ClearRunFacts() -> Void {
    this.SetFact("gq_runtime_theft_accepted", 0);
    this.SetFact("gq_runtime_theft_reached", 0);
    this.SetFact("gq_runtime_theft_completed", 0);
    this.SetFact("gq_runtime_theft_abandoned", 0);
    this.SetFact(GhostlineDataTheftConfig.TransferFact(), 0);
    this.SetFact(GhostlineDataTheftConfig.DeliveredFact(), 0);
    this.SetFact(GhostlineDataTheftConfig.KeptCopyFact(), 0);
    this.SetFact(GhostlineDataTheftConfig.DeliverCondition(), 0);
    this.SetFact(GhostlineDataTheftConfig.KeepCondition(), 0);
  }

  public func Offer() -> Bool {
    if this.Active() { this.error = "Finish or abandon the active job first."; return false; }
    let target = Cast<EntityID>(ResolveNodeRef(GhostlineDataTheftConfig.TargetRef(), Cast<GlobalNodeRef>(GlobalNodeID.GetRoot())));
    if !EntityID.IsDefined(target) { this.error = "Catalogue NodeRef did not resolve in this world."; return false; }
    let point = GameInstance.FindEntityByID(this.GetGameInstance(), target) as AccessPoint;
    if IsDefined(point) && !point.GhostlineDataTheftAvailable() {
      this.error = "The catalogue access point is unpowered or reserved by another quest in this save.";
      return false;
    }
    this.RemoveMarker();
    this.sequence += 1;
    this.revision = GhostlineDataTheftConfig.Revision();
    this.target = target;
    this.position = GhostlineDataTheftConfig.Position();
    this.transferActive = false;
    this.transferElapsed = 0.0;
    this.outcome = 0;
    this.dataAcquired = false;
    this.rewardApplied = false;
    this.error = "";
    this.ClearRunFacts();
    this.phase = 1;
    this.Notify("Borrowed Credentials: a data-theft job is available. Open the job choices to accept.");
    return true;
  }

  public func Accept(expected: Int32) -> Bool {
    if !this.Compatible() || expected != this.sequence || this.phase != 1 { return false; }
    let point = this.Point();
    if IsDefined(point) && !point.GhostlineDataTheftAvailable() {
      this.Fail("The reserved target became unavailable before acceptance.");
      return false;
    }
    this.phase = 2;
    this.SetFact("gq_runtime_theft_accepted", 1);
    this.Notify("Borrowed Credentials: reach the marked access point in Little China.");
    this.Tick(0.0);
    return true;
  }

  public func Decline(expected: Int32) -> Bool {
    if expected != this.sequence || this.phase != 1 { return false; }
    this.phase = 8;
    this.RemoveMarker();
    return true;
  }

  public func Abandon(expected: Int32) -> Bool {
    if expected != this.sequence || !this.Active() { return false; }
    this.StopTransfer();
    this.phase = 6;
    this.abandonedCount += 1;
    this.SetFact("gq_runtime_theft_abandoned", 1);
    this.RemoveMarker();
    this.Notify("Borrowed Credentials abandoned. No job payment awarded.");
    return true;
  }

  private func Fail(reason: String) -> Void {
    this.StopTransfer();
    this.phase = 7;
    this.error = reason;
    this.RemoveMarker();
    this.Notify(reason);
  }

  // Exact device and run identity guard all injected actions and completion.
  public func InteractionSequence(id: EntityID) -> Int32 {
    if this.Compatible() && this.phase == 3 && id == this.target && this.NearTarget() {
      return this.sequence;
    }
    return 0;
  }

  public func Transferred(id: EntityID) -> Bool = id == this.target && this.dataAcquired;

  public func BeginTransfer(id: EntityID, expected: Int32) -> Bool {
    if expected <= 0 || expected != this.InteractionSequence(id) || this.transferActive { return false; }
    let board = GameInstance.GetBlackboardSystem(this.GetGameInstance()).Get(GetAllBlackboardDefs().UI_HUDProgressBar);
    let def = GetAllBlackboardDefs().UI_HUDProgressBar;
    if board.GetBool(def.Active) {
      this.Notify("Another transfer owns the progress bar. Disconnect and try again.");
      return false;
    }
    this.transferElapsed = 0.0;
    this.transferActive = true;
    this.progressOwned = true;
    board.SetString(def.Header, "Borrowed Credentials: downloading", true);
    board.SetString(def.BottomText, "Do not disconnect", true);
    board.SetString(def.CompletedText, "Credentials downloaded", true);
    board.SetString(def.FailedText, "Transfer interrupted", true);
    board.SetVariant(def.MessageType, ToVariant(SimpleMessageType.Connection), true);
    board.SetFloat(def.Progress, 0.0, true);
    board.SetBool(def.Active, true, true);
    return true;
  }

  public func CancelTransfer(id: EntityID) -> Void {
    if id == this.target { this.StopTransfer(); }
  }

  private func StopTransfer() -> Void {
    let wasActive = this.transferActive;
    this.transferActive = false;
    if this.progressOwned {
      let board = GameInstance.GetBlackboardSystem(this.GetGameInstance()).Get(GetAllBlackboardDefs().UI_HUDProgressBar);
      let def = GetAllBlackboardDefs().UI_HUDProgressBar;
      if Equals(board.GetString(def.Header), "Borrowed Credentials: downloading") {
        board.SetBool(def.Active, false, true);
      }
      this.progressOwned = false;
    }
    if wasActive {
      let point = this.Point();
      if IsDefined(point) { point.GetDevicePS().DisconnectPersonalLink(GetPlayer(this.GetGameInstance()), n"", true); }
    }
    this.transferElapsed = 0.0;
  }

  public func Tick(delta: Float) -> Void {
    if !this.Compatible() { return; }
    if this.phase == 2 || this.phase == 3 {
      this.EnsureMarker();
      let point = this.Point();
      if this.NearTarget() && IsDefined(point) {
        if !point.GhostlineDataTheftAvailable() {
          this.Fail("The catalogue target is unpowered or controlled by another quest.");
          return;
        }
        if this.phase == 2 {
          this.phase = 3;
          this.SetFact("gq_runtime_theft_reached", 1);
          point.GhostlineDataTheftRefresh();
          this.Notify("Borrowed Credentials: select Download credentials on the marked access point.");
        }
      }
      if this.transferActive {
        let board = GameInstance.GetBlackboardSystem(this.GetGameInstance()).Get(GetAllBlackboardDefs().UI_HUDProgressBar);
        let def = GetAllBlackboardDefs().UI_HUDProgressBar;
        if !this.NearTarget() || !IsDefined(point) || !point.GetDevicePS().IsPersonalLinkConnected()
          || !board.GetBool(def.Active) || NotEquals(board.GetString(def.Header), "Borrowed Credentials: downloading") {
          this.StopTransfer();
          this.Notify("Transfer interrupted. Reconnect to download the credentials.");
          return;
        }
        // CET supplies unpaused frame time; cap stalls so a single late tick cannot finish it.
        if delta > 0.0 { this.transferElapsed += MinF(delta, 0.25); }
        board.SetFloat(def.Progress, MinF(this.transferElapsed / GhostlineDataTheftConfig.Duration(), 1.0), true);
        if this.transferElapsed >= GhostlineDataTheftConfig.Duration() {
          this.dataAcquired = true;
          this.SetFact(GhostlineDataTheftConfig.TransferFact(), 1);
          this.phase = 4;
          this.StopTransfer();
          this.RemoveMarker();
          this.Notify("Credentials extracted. Open the job choices to decide what to deliver.");
        }
      }
    }
  }

  public func Choose(selected: Int32, expected: Int32) -> Bool {
    if !this.Compatible() || expected != this.sequence || this.phase != 4 || !this.dataAcquired
      || (selected != 1 && selected != 2) || this.rewardApplied { return false; }
    let player = GetPlayer(this.GetGameInstance());
    if !IsDefined(player) { return false; }
    let amount = GhostlineDataTheftConfig.Reward();
    if amount > 0 && !GameInstance.GetTransactionSystem(this.GetGameInstance()).GiveItem(player, ItemID.FromTDBID(t"Items.money"), amount) {
      this.error = "The job payment failed. The outcome has not been committed.";
      return false;
    }
    // One synchronous main-thread commit: payout, outcome and checkpoint save together.
    this.rewardApplied = true;
    this.outcome = selected;
    this.phase = 5;
    if selected == 1 {
      this.deliveredCount += 1;
      this.SetFact(GhostlineDataTheftConfig.DeliverCondition(), 1);
      this.SetFact(GhostlineDataTheftConfig.DeliveredFact(), 1);
    } else {
      this.keptCopyCount += 1;
      this.SetFact(GhostlineDataTheftConfig.KeepCondition(), 1);
      this.SetFact(GhostlineDataTheftConfig.KeptCopyFact(), 1);
    }
    this.SetFact("gq_runtime_theft_completed", 1);
    this.RemoveMarker();
    this.Notify("Borrowed Credentials complete. Job payment received.");
    return true;
  }

  private func EnsureMarker() -> Void {
    if this.markerRegistered { return; }
    let data: MappinData;
    data.mappinType = t"Mappins.DefaultStaticMappin";
    data.variant = gamedataMappinVariant.DefaultQuestVariant;
    data.active = true;
    data.visibleThroughWalls = true;
    data.debugCaption = "Borrowed Credentials";
    this.marker = GameInstance.GetMappinSystem(this.GetGameInstance()).RegisterMappin(data, this.position);
    this.markerRegistered = true;
  }

  private func RemoveMarker() -> Void {
    if this.markerRegistered {
      GameInstance.GetMappinSystem(this.GetGameInstance()).UnregisterMappin(this.marker);
      this.markerRegistered = false;
    }
  }
}

// Native personal-link animation/state handling stays intact. Tagged job links
// bypass ResolvePersonalLinkConnection's netrunner rewards and minigame route.
@addField(TogglePersonalLink)
public let ghostlineTheftSequence: Int32;
@addField(ScriptableDeviceComponentPS)
private let ghostlineTheftLinkSequence: Int32;

@addMethod(ScriptableDeviceComponentPS)
public func GhostlineDataTheftUsable() -> Bool {
  return this.IsPoweredAndEnabled() && this.HasPersonalLinkSlot()
    && !this.m_personalLinkForced && !this.m_disablePersonalLinkAutoDisconnect
    && (!TDBID.IsValid(this.m_personalLinkCustomInteraction) || this.m_personalLinkCustomInteraction == t"Interactions.None");
}

@addMethod(AccessPoint)
public func GhostlineDataTheftAvailable() -> Bool = IsDefined(this.GetDevicePS()) && this.GetDevicePS().GhostlineDataTheftUsable();

@addMethod(AccessPoint)
public func GhostlineDataTheftRefresh() -> Void {
  this.UpdateDeviceState();
  this.DetermineInteractionStateByTask();
}

@addMethod(ScriptableDeviceComponentPS)
public final const quest func GhostlineDataTheftTransferred() -> Bool {
  return GhostlineDataTheftSystem.Get(this.GetGameInstance()).Transferred(PersistentID.ExtractEntityID(this.GetID()));
}

@wrapMethod(ScriptableDeviceComponentPS)
public func GetActions(out outActions: array<ref<DeviceAction>>, context: GetActionsContext) -> Bool {
  let result = wrappedMethod(outActions, context);
  let job = GhostlineDataTheftSystem.Get(this.GetGameInstance());
  let sequence = job.InteractionSequence(PersistentID.ExtractEntityID(this.GetID()));
  if sequence > 0 && this.GhostlineDataTheftUsable() && this.IsPersonalLinkDisconnected()
    && TogglePersonalLink.IsDefaultConditionMet(this, context) && this.CanConnectToPersonalLink() {
    let action = this.ActionTogglePersonalLink(context.processInitiatorObject, false, true);
    action.ghostlineTheftSequence = sequence;
    action.SetDurationValue(2.0);
    action.CreateInteraction();
    action.interactionChoice.caption = "Download credentials";
    InteractionChoiceCaption.Clear(action.interactionChoice.captionParts);
    InteractionChoiceCaption.AddPartFromRecord(action.interactionChoice.captionParts, TweakDBInterface.GetChoiceCaptionIconPartRecord(t"ChoiceCaptionParts.JackInIcon"));
    InteractionChoiceCaption.AddTextPart(action.interactionChoice.captionParts, "Download credentials");
    ArrayPush(outActions, action);
  }
  return result;
}

@wrapMethod(ScriptableDeviceComponentPS)
public final func OnTogglePersonalLink(evt: ref<TogglePersonalLink>) -> EntityNotificationType {
  if evt.ghostlineTheftSequence > 0 && this.IsPersonalLinkDisconnected() {
    this.ghostlineTheftLinkSequence = evt.ghostlineTheftSequence;
  }
  return wrappedMethod(evt);
}

@wrapMethod(ScriptableDeviceComponentPS)
protected func ResolvePersonalLinkConnection(evt: ref<TogglePersonalLink>, abortOperations: Bool) -> Void {
  if evt.ghostlineTheftSequence > 0 || this.ghostlineTheftLinkSequence > 0 {
    let job = GhostlineDataTheftSystem.Get(this.GetGameInstance());
    let id = PersistentID.ExtractEntityID(this.GetID());
    if !abortOperations && this.IsPersonalLinkConnected() {
      this.ghostlineTheftLinkSequence = evt.ghostlineTheftSequence;
      if !job.BeginTransfer(id, evt.ghostlineTheftSequence) {
        this.DisconnectPersonalLink(evt, true);
      }
    } else {
      this.ghostlineTheftLinkSequence = 0;
      job.CancelTransfer(id);
    }
    return;
  }
  wrappedMethod(evt, abortOperations);
}

@addMethod(GameObject)
public func GhostlineDataTheftOffer() -> Bool = GhostlineDataTheftSystem.Get(this.GetGame()).Offer();
@addMethod(GameObject)
public func GhostlineDataTheftState() -> ref<GhostlineDataTheftSnapshot> = GhostlineDataTheftSystem.Get(this.GetGame()).Snapshot();
@addMethod(GameObject)
public func GhostlineDataTheftAccept(expected: Int32) -> Bool = GhostlineDataTheftSystem.Get(this.GetGame()).Accept(expected);
@addMethod(GameObject)
public func GhostlineDataTheftDecline(expected: Int32) -> Bool = GhostlineDataTheftSystem.Get(this.GetGame()).Decline(expected);
@addMethod(GameObject)
public func GhostlineDataTheftAbandon(expected: Int32) -> Bool = GhostlineDataTheftSystem.Get(this.GetGame()).Abandon(expected);
@addMethod(GameObject)
public func GhostlineDataTheftChoose(selected: Int32, expected: Int32) -> Bool = GhostlineDataTheftSystem.Get(this.GetGame()).Choose(selected, expected);
@addMethod(GameObject)
public func GhostlineDataTheftTick(delta: Float) -> Void {
  GhostlineDataTheftSystem.Get(this.GetGame()).Tick(delta);
}
