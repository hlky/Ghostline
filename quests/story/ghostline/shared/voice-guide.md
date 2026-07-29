# Ghostline Voice Guide

These are the durable voice rules for recurring characters. Quest-local notes
should record only the emotional state or deliberate deviation for that story.

## Speaker Embeddings

Reusable Qwen3-TTS speaker embeddings are stored in
[`voice/embeddings`](voice/README.md):

- `voice/embeddings/patch.safetensors`
- `voice/embeddings/v.safetensors`

These SafeTensors files are the canonical copies. Do not reintroduce
pickle-backed `.pt` embeddings.

Iris does not yet have a persisted embedding. Do not substitute one of her
finished quest WAVs without recording that a new embedding was derived.

## Iris

Precise without sounding clinical. She corrects language when euphemism hides
harm: a cache contains people, a route is made of couriers, and reconstruction
can be another violation. Her anger makes her sentences shorter. She does not
plead.

## Patch

Fast, defensive, and funny when cornered. He fills silence with explanations
and tries to reduce moral failures to missing technical details. Humor is both
his social lubricant and his evasive maneuver.

## Morrow

Calm, exact, and operational. He expresses approval and disapproval as cost,
leverage, exposure, and future casualties. He does not deny human harm; he
argues about which response produces less of it.

## V

Direct and skeptical. Optional questions pressure euphemisms and hidden
knowledge. Progression choices remain short enough to scan during play.
