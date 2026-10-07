@replaceMethod(FullscreenVendorGameController)
  protected cb func OnBeforeLeaveScenario(userData: ref<IScriptable>) -> Bool {
    return false;
  }

@replaceMethod(RipperDocGameController)
  protected cb func OnBeforeLeaveScenario(userData: ref<IScriptable>) -> Bool {
    return false;
  }