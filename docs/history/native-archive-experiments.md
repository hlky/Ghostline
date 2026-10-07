# Historical Native Archive Experiments

An earlier 301-payload Ghostline archive packed with `ghostline-red` extracted
byte-identically. That result established an extraction/interoperability probe,
not game startup compatibility. A later GQT007 lipsync test reproduced a game
startup crash with native packing; see the dated runtime evidence archive.

The current runtime rule is owned by the
[build/package guide](../workflows/build-and-package.md): pack with WolvenKit,
then verify the exact selected depot paths and extracted payload hashes before
staging or installing. Native pack experiments belong in isolated scratch output.

## 2026-10-05 encoder repair

Repacking the WolvenKit-built `gqt005-wolvenkit-pack-20260727-122605` archive
reproduced decompression failures in WolvenKit. Direct checks with the game's
`oo2ext_7_win64.dll` rejected 267 of 304 compressed main payloads. The native
encoder had two compatibility defects:

- General LZ matches could reach the chunk end. The encoder now reserves a
  16-byte literal tail for the decoder's short-match wide copies.
- Every 256 KiB block advertised a history restart, while subsequent LZ chunks
  omitted initial history bytes. Only the first block now sets the restart bit.

After repair, Oodle decoded all 304 payloads and WolvenKit extracted the archive.
The independent Oodle boundary test is in
`tools/ghostline-red/tests/kraken_oodle.rs`; the historical-archive regression
runner is `tools/ghostline-red/scripts/archive_regression.py`. The runner
extracts an old archive with WolvenKit, repacks those inputs with both tools,
then checks WolvenKit-extracted SHA-256 payloads and logical index layouts.

| Historical build | Files | Segments | Original / WolvenKit bytes | Native bytes |
| --- | ---: | ---: | ---: | ---: |
| lipsync-slot0-20260722-000338 | 173 | 567 | 63,737,856 | 97,882,112 |
| gqt005-wolvenkit-pack-20260727-122605 | 353 | 1,029 | 71,630,848 | 107,069,440 |
| lipsync-pma-control-clean-20260811-153227 | 443 | 1,306 | 76,943,360 | 112,889,856 |

All 969 files matched exactly, including depot paths, archive entry hashes,
inline-buffer counts and uncompressed segment sizes. Physical offsets,
compressed sizes, timestamps and SHA1 conventions are not equality criteria.
Native compression still produces larger archives; archive size equality is
not required for compatibility.

Local logs, index dumps and payload hashes are retained under
`generated/archive-regression/corpus-fixed`, with results in `report.json`.
The full Rust suite passed 111 tests, and the explicit Oodle oracle test passed.
Game startup has not been tested with these repaired archives. Keep the
WolvenKit runtime packaging rule until that separate validation is completed.
