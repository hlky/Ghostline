# Act II Script: Relay Choice

## Relay Choice Phone Thread

### Opening

**Cinder:** Saw the scan. Tenant classifier and clinic telemetry share one
relay. Deliberate hostage circuit.

**Cinder:** Two options: destroy it after I warn the clinic, or blind the
classifier and spoof a failure.

### Main choice A: “Destroy the relay.”

**V choice text:** Destroy the relay.

**Cinder:** Hard stop. I'll warn the clinic and reroute what I can before you
pull it.

Sets `gq002_choice_destroy = 1`.

### Main choice B: “Spoof the shutdown.”

**V choice text:** Spoof the shutdown.

**Cinder:** Quiet cut. I'll feed the owners a clean failure report while you
blind the classifier.

Sets `gq002_choice_spoof = 1`.

**Cinder:** Make the call real. Jack in.
