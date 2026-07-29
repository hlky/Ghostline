# Black Lantern Voice Notes

Recurring voices follow the
[series voice guide](../../shared/voice-guide.md). These notes describe their
Black Lantern state and the quest-specific Mara voice.

### Iris

Iris is angrier and more personally invested than in `gq001`. She insists that
reconstruction is a second violation rather than recovery, and her sentences
shorten whenever Patch or Morrow turns harm into operational language.

### Patch

Patch tries to reduce his moral failure to missing technical details. During
the confession, his normal evasive humor becomes self-directed.

### Morrow

Morrow never says the couriers do not matter. He argues that destroying the
route protects the organization that created them, expressing disapproval as
lost leverage and future casualties.

### Mara Venn

Practical, exhausted, and frightened by specificity rather than spectacle.
She can describe the humidity setting in apartments she has never seen but
cannot immediately recall her own front door. Her systems-maintenance
background gives her concrete language for memory: vents, filters, false
readings, duplicated control loops.

### V

V's optional questions focus on Patch's hidden knowledge and the euphemisms
used for human couriers. Progression choices remain terse.

## Production Inventory

[`voice-production.json`](voice-production.json) is the source of truth for
the 128 spoken lines across all six acts. `gq003_02` and `gq003_20` are formal
scene deliveries. The other six sets are authored for journal-phone VO,
holocalls, scanner feedback, combat/escort ambient, vehicle ambient, and
device/system playback, but their runtime hooks remain pending.

Use [`tools/ghostline-voice`](../../../../../tools/ghostline-voice/README.md)
for native DinoML Qwen3-TTS auditions, manifest validation, and localization
generation. V and Patch use the reviewed shared embeddings; generate Iris from
her designed reference. Mara, Morrow, and the reconstruction system require
separate designed references and approval before batch rendering. Derived
DinoML JSON embeddings belong in the ignored `generated-voices` cache rather
than beside the canonical SafeTensors assets.

Keep each audition at or below the manifest's estimated duration and the
20-second generation ceiling. Branch conditions in the manifests are delivery
metadata: do not render them as spoken prefixes, and do not concatenate clean,
detected, preserve, or burn variants into a single clip.

### Sequence state

- Freight-yard responses are observational and controlled; Iris becomes terse
  only when the detected branch warns that the clinic is awake.
- Mara's rescue performance is lucid at the sentence level but uncertain about
  ownership. Avoid dreamlike slurring; the fear comes from precise details.
- Patch's vehicle humor should collapse after V says Mara had one of his cases.
  Leave the acknowledgement short and unprotected.
- The relay argument is not a shouting match. Morrow stays measured while Iris
  removes euphemisms; their pressure comes from incompatible certainties.
- The debrief is aftermath, not a victory speech. Preserve and burn variants
  should both leave a cost in the room.
