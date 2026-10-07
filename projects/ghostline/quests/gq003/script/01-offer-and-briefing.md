# Act I Script

## Act I Text

### Patch job offer

**Patch:** Need you to meet Iris. Quiet Spine finally opened.

**Patch:** She says the cache contained a person who is still alive.

**V choice:** Send the location.

**Patch:** Same place as before. Go easy on the door. She has not slept since
you delivered that cache.

### Opening Iris scene

#### Opening

**Iris:** The cache was not carrying one identity. It was carrying pieces of
several. One of them is still moving through the city.

#### Choice group one

**Optional choice: “What did Quiet Spine move?”**

**V:** Start clean. What did Quiet Spine actually move?

**Iris:** Instructions for rebuilding people. Habits, sensory anchors,
reflexes, the memories that tell you a room is yours. Split apart, they look
like damaged braindances. Put together, they can impersonate a life.

**Optional choice: “How does someone carry a memory?”**

**V:** How do you hide somebody else's memories in a courier?

**Iris:** You do not hide them. You make the courier experience them. A smell
that feels familiar. A route home they have never walked. The implant calls it
memory because the body cannot file it anywhere else.

**Progression choice: “Where did the Kabuki relay fit?”**

**V:** Common Ground's relay. Where did it fit?

**Iris:** Selection. Its tenant classifier found people with debt, unstable
housing, obsolete implants, missing legal identities. People whose absence
would be recorded as a database correction.

**Iris:** Cinder shut the relay down. Black Lantern moved its next pair early.

#### Choice group two

**Optional pressure: “How much did Patch know?”**

**V:** Patch knew Quiet Spine used flesh couriers. How much did he tell you?

**Iris:** Less than he knew and more than he admits. Ask him after we have the
woman back. Right now his shame is less urgent than her pulse.

**Progression choice: “Where is Mara?”**

**V:** Name and location.

**Iris:** Mara Venn. Apartment systems tech. Pair Zero-Seven-A. A scav clinic
is holding her until tonight's handoff.

**Iris:** Pair Zero-Seven-B is moving separately inside a freight vehicle. It
carries the reconstruction cipher. Dispatch authority is K. Morita.

#### Close

**Progression choice: “I'll bring her out.”**

**V:** Send me the clinic.

**Iris:** Not yet. Mark the paired shipment first. If we touch Mara before I
can follow the cipher, they wipe her and move the vehicle.

**V:** Then I mark the shipment and bring her out.

**Iris:** Read my report. The transfer window opens tonight.

Scene exit: `job_accept`.

### Reconstruction report

**Title:** QUIET SPINE RECONSTRUCTION / BLACK LANTERN

```text
AUTHOR: IRIS
STATUS: PARTIAL RECONSTRUCTION
SOURCE: QUIET SPINE CACHE

The source does not contain complete personality engrams. It contains indexed
mnemonic fragments and the route metadata required to recombine them.

BLACK LANTERN uses paired biological transport:

PAIR 07-A
MNEMONIC SUBJECT: MARA VENN
FUNCTION: carries autobiographical fragments embedded as personal experience
CURRENT STATE: active / graft rejection detected

PAIR 07-B
CIPHER SUBJECT: FREIGHT VEHICLE BL-07B
FUNCTION: carries reconstruction key, fragment index, and route attestation
CURRENT STATE: expedited handoff

Neither half is sufficient alone. The mnemonic subject cannot identify the
foreign fragments. The cipher can identify them but contains no experiential
payload.

ROUTING ALIAS: BLACK LANTERN
DISPATCH AUTHORITY: K. MORITA
TRIGGER FOR EXPEDITED HANDOFF: KABUKI CLASSIFIER OFFLINE

ASSESSMENT:
Quiet Spine did not move files. It moved the instructions for rebuilding
people.
```

### Transfer-window message

**Patch:** Yard calls itself Kuroda Municipal Salvage. It is neither Kuroda,
municipal, nor interested in salvage.

**Patch:** Freight gate phrase is BLACK LANTERN, PAIR SEVEN, PRIORITY WEATHER.

**Patch:** If anybody asks what that means, look annoyed and tell them Morita
changed it twice already.
