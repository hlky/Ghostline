# Love, Actually.exe voice production

All synthesis, embedding extraction, reference encoding, and localization use
`tools/ghostline-voice`. Velvet is designed first, then cloned with full
reference conditioning: the exact transcript, acoustic codes and speaker
embedding. V uses the previously selected female/male vanilla reference
recordings, also with full conditioning. V is never voice-designed.

The twins comparison's selected recipe is in
`generated-voices/french-twins/preferred-recipe.json`. It selected full
reference plus delivery instruction for those French-accented performers.
The later selected V recipe uses full reference without an instruction and
natural contractions. Use each performer's own recipe rather than copying a
French-accent instruction onto Velvet or V.

The matching full-length VoiceDesign artifact is linked from Facet's
`consumers/voice-studio/src/model.rs` and lives at:

```text
H:/facet/.work/gui-engine/evidence/voice-studio/coherent/voice_design_generation_p256_f288
```

It supports 256 prompt tokens and 288 generated frames. The adjacent decoder
supports 256 frames. The tiny `.work/attentionsaurus-models` VoiceDesign
qualification artifacts (32 prompt tokens/eight frames) cannot render a
reference performance.

Source `C:/Users/user/Documents/PowerShell/profile.ps1` from the repository root
to activate DinoML's packaged ROCm environment. Precompiled native catalogues
live at `H:/dinoml-native-libraries`; set `DINOML_NATIVE_LIBRARY_DIR` explicitly
when compiling anything that consumes them. Existing artifact libraries are
loaded as built; environment variables cannot change their compiled layouts.

The current DinoML main checkout has refactored model-weight storage. Building
against it rejected existing decoder constants with storage kind
`ck_conv1d_weight`. Build with command-scoped Cargo patches to the older
`H:/dinoml_v2-worktrees/facet-voice-studio` checkout for these artifacts. Keep
the user's `.cargo/config.toml` intact. Record the resolved source commit and
artifact identities in the run receipt before reproducing a render.
`python projects/ghostline/quests/gq004/voice/build_tool.py` replays the compatible
build with scoped overrides and checks the checkout revision first.

`ghostline-voice design-reference` creates an unreviewed custom-character WAV,
with a fixed seed and reproducibility sidecar. Use `extract-embedding` and
`encode-reference` on that WAV, then pass `--reference-prompts` to
`render-local`. A designed reference is a voice candidate, not a reviewed take.

The current batch recipe is checked in as `toolchain.json`. Replay a batch with
`python projects/ghostline/quests/gq004/voice/render.py --batch female` (or
`male`, `velvet-a`); add `--dry-run` to inspect the exact full-reference request.
The wrapper refuses missing transcripts/codes/embeddings. It never silently
falls back to embedding-only synthesis.

The selected voice direction was retained by the user on 2026-10-25. The user subsequently listened to and approved all
60 current takes: 26 Velvet lines and 17 lines for each V. The short Velvet
conditioning reference is 3.52 seconds. Its exact words are “Okay, gorgeous.
The hearts are intentional.” For this older runtime, the static 190,048-sample
encoder input adds trailing silence to the reference; it does not truncate
speech. Preparation hashes are retained with the candidate reference.

Keep candidates under ignored `generated-voices/gq004`. Once listening review
selects takes, use `tools/build_voice_selection_csv.py` and
`tools/promote_voice_selections.py` to copy them to this quest's `voice/source`.
Then convert only those manifest basenames through `convert_wavs_to_wem.ps1`.
Do not promote an audition automatically or overwrite reviewed source WAVs.

Lipsync uses the selected WAV, its exact text and stable locstring ID with
`tools/compile_lipsync_manifest.py`. Candidate curves may be generated for
review but must retain candidate status and audio hashes. Recompile if the
selected audio changes. The final animation/lipmap cooking and scene slot
checks remain separate from producing a GLB with facial curves.

## Current playable build

The user listened to and approved the current takes on 2026-10-25. All 60
version00 takes are promoted under `source`, with selections and SHA-256 receipts
beside this file. `promote.py` reproduces that selection; `review.json` records
the approval. Wwise converted all 60 WAVs. `cook.py` produced the combined
86-clip runtime set, and WolvenKit re-export verified facial keys and durations
within 0.001 ms. Two unused original donor clips remain in the animset.
The ten native scenes and their lipmap use the cooked names explicitly.
The package uses WEM playback throughout, with phone VO parameters for Velvet
during field scenes. No Audioware or runtime voice worker is required.

## Dialogue pass 02

The user listening-approved ten replacement Velvet takes on 2026-10-25:
“Use these revised takes.” `dialogue-review-02.json` records their exact hashes.
`revise_dialogue.py` reproduces the full-reference candidate rendering in a
separate directory; `apply_revision.py` applies only the reviewed hashes and
preserves previous source WAVs. It updates matching spoken text and durations.
`promote.py` reapplies this approved revision after restoring the original batch.

The sparse revised facial set is compiled against the candidate manifests,
not the previous dialogue text. `cook.py` replaces its twenty gender variants
in the combined 86-clip set and verifies both candidate and promoted WAV hashes.
The unchanged female/male V performances remain selected. Field branding is a
separate connection-triggered scene; it uses the same approved V line with the
new, shorter Velvet response. The closing take is replaced rather than leaving
its old long pause in the audio.
