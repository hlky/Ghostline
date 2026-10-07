# Patch Reference Asset Provenance

The original head and morphtarget folders contained identical donor readmes.
Their note was: these resources were copied directly from the game's
`base/characters/head/player_base_heads/player_man_average` tree for authoring
convenience, including all variants; only the variants in use are needed.

The profile packager starts at `patch.ent` and follows named and known numeric
resource references. Some mesh material buffers have no parsed raw companion,
so it conservatively retains Patch's owning bundle, including texture and donor
variants. Fine-grained pruning requires decoding those remaining buffers.
