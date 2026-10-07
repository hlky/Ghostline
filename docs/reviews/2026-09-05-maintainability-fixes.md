# Maintainability review: completed fixes

Implemented the changes for R01–R27 from the [original review](2026-09-05-maintainability-review.md).
Existing user changes were preserved. No game installation, source WAV replacement,
or authored binary regeneration was performed; package outputs are isolated under
`generated/packages`.

## Validation

- Locked project gate: **540 Python tests passed** in 51.670 seconds, Ruff F passed, and **6 model-free Rust tests passed**.
- Full-feature voice: **11 Rust tests passed**; strict Clippy passed in full and minimal configurations.
- C# import transaction harness, real helper build, and character UI JavaScript syntax check passed.
- All 14 typed quest manifests agree with the schema/compiler. All 20 journal/onscreen outputs retain exact pre-refactor content.
- Offline reference generation produces the same category pages (57 main jobs, 85 side jobs, 85 gigs) and repeatable input/provenance artifacts without fetching the network.

The focused suites overlap the central suite; their counts are not additive.
Full central output is retained in `generated/fixes/project-gate.log`.

## Finding-by-finding completion

| Finding | Implemented change | Evidence |
| --- | --- | --- |
| R01 | Completed the documented retirement of the deleted world catalog/direct pipeline and its orphan tests/schemas; fixed the scene fixture and reconciled GQT006 tests with its authored graph. | Full Python suite; explicit replacement GQT006 route and corruption assertions. |
| R02 | Added Python 3.12 project extras, uv.lock, centralized offline checks and a clean Ruff F gate. | Fresh locked environment; Python, lint and model-free Rust gates. |
| R03 | Separated quest types, schema-driven stage fields, stage registry and semantic validators; corrected editor schema parity and meeting objective/mappin bindings. | All 14 manifests agree with schema/compiler; corruption tests and registry-document parity. |
| R04 | Construct complete quest artifact sets before publication; stage and roll back JSON writes; retain explicit ownership and obsolete-output records. | Late child/serialization/replacement failure, duplicate path and rollback-recovery tests. |
| R05 | Replaced cross-quest journal output chains with reviewed minimal donors and a provenance catalog. | All 20 journal/onscreen outputs remain exactly equal, including handles. |
| R06 | Moved graph wiring and typed node primitives into phase_graph; reused quest_content and shared onscreen construction. | Generator/template golden tests and all quest builder suites. |
| R07 | Validate emitted scene exits, actor resource-set references and descriptor/payload/variant relationships for every locale. | Missing exit, wrong target type, out-of-range index and variant mismatch regressions. |
| R08 | Use full world NodeRef identity across sectors, validate aliases, and make default timestamps deterministic. | Duplicate/cross-sector/alias rejection, valid distinct paths, deterministic generation. |
| R09 | Lock character ID/namespace in the UI and enforce generated path/appearance identity on the server. | Input/output identity mismatch regressions; JavaScript syntax check. |
| R10 | Use staged character cache publication with complete input/output checks and nested archive identities. | Failed refresh, rollback, missing output and nested-input invalidation tests. |
| R11 | Parse character inputs once per request/build and materialize only selected donor copies. | Parse-count and mutation-isolation regressions. |
| R12 | Split braindance clues, graph inspection, independent auditing, RID types/codec/compiler/validation and publication into domain modules. | Existing public entry points retained; RID and pipeline suites. |
| R13 | Correct the default braindance fixture and reject incompatible Kimodo bake/output combinations before work starts. | Default-path and no-subprocess-on-invalid-input tests. |
| R14 | Use Rust as the canonical localization constructor with a single-manifest CLI and Python compatibility adapter; provide a model-free core. | Gendered/shared audio parity, invalid-input publication and minimal-feature Rust tests. |
| R15 | Key voice reuse by complete synthesis request and backend content identity; force always rerenders. | Fake backend tests for text/settings/model/embedding changes, corruption, subsets and force. |
| R16 | Drive review CSVs from render reports and validate selected voice design per speaker, with an explicit legacy adapter. | Iris/Patch report-to-CSV-to-promotion fixtures and changed-audio rejection. |
| R17 | Separate alignment and sampling checkpoint identities; share one lipsync compilation/GLB core across single and batch CLIs. | FPS/track resampling reuse, audio/text invalidation and byte-identical single/batch fixtures. |
| R18 | Use fresh Wwise run inputs/outputs, exact platform lookup and complete-set publication with rollback. | Missing/duplicate outputs and injected late publication failures; no source WAV changes. |
| R19 | Validate exact, compatible and new item render reports; handle failed workers and per-item outcomes without stale complete records. | Real SQLite tests for missing images, malformed reports, valid reuse, startup failure and partial batches. |
| R20 | Split item catalog/export/render/gallery/CLI responsibilities and extract capture metadata/store plus pure world-render contracts. | Existing item, renderer and 34 capture lifecycle/persistence tests. |
| R21 | Share scalar explorer search and atomic JSON artifact writers where their contracts match. | Explorer behavior preserved; publication failure tests. Specialized protocol writers retained. |
| R22 | Centralize tool resolution and explicit overrides; fingerprint RED schema writer, WolvenKit pin/worktree/type files and cached schema content. | Precedence/no-fallback tests, schema invalidation and transactional schema/receipt rollback. |
| R23 | Make the C# animation import operate on a staged candidate before replacing the original. | Real helper build: zero warnings/errors; rejection/exception/success/cleanup harness. |
| R24 | Add story, individual test and development profiles; close named/numeric authoring dependencies, retain opaque character bundles, and deduplicate identical meshes through checked aliases. | All profile audits; excluded tests/overrides/preproduction tweaks; verified packages below. |
| R25 | Use one pack/list/extract/hash/ZIP gate for shared and standalone builds; verify staged hashes again before installation. | Real WolvenKit packages; failure injection, path validation, overrides and no-publication-on-failure tests. |
| R26 | Make build-and-package the owner of the runtime WolvenKit packing rule and move native pack experiments into history. | Current guide, agent skill and tool catalog agree. |
| R27 | Correct capture/lifecycle prose, remove inert FOV configuration, split dated runtime history, record reproducible reference inputs, trim ignores and untrack local editor state. | Offline reference output parity; local editor file retained; current documentation and whitespace checks. |

## Verified package reductions

The authoring depot contains 505 resource files totaling
228.55 MiB. Profiles retain their required dependencies
and separate runtime content from prototype, development and unvalidated global overrides.

| Candidate | Payloads | Uncompressed payload | Packed archive | Duplicate bytes avoided |
| --- | ---: | ---: | ---: | ---: |
| Story | 174 | 58.59 MiB | 23.33 MiB | 2.01 MiB |
| Standalone GQT006 | 90 | 6.68 MiB | 5.77 MiB | 0.00 MiB |

Both archives were packed with WolvenKit, listed, extracted and compared against
every frozen input by path, length and SHA-256. Both ZIPs were extracted and checked
against their staged install trees. The receipts and logs are retained at:

- Story: `H:\projects\Ghostline\generated\packages\story-efe598f43fbf`
- GQT006: `H:\projects\Ghostline\generated\packages\gqt006-83fe8fd10dc4`

Story archive SHA-256: `48c0c0d1ddd60411c40f0e8c9d1d1b7737f4599a96ed73d55c49fbb34e68aacd`.

GQT006 archive SHA-256: `17b33835549ca5b2f2598b71d9e4a602b31d3512a87865c974bef726a093ddfa`.

Dependency review caught numeric appearance references and opaque mesh material
buffers. Earlier overly small candidates were explicitly invalidated. Final profiles
resolve known numeric references and retain the entire owning character bundle when
a selected mesh lacks parsed raw material evidence. Further fine-grained pruning
requires decoding those buffers. Alias groups are byte-identical and require
ArchiveXL 1.14 or newer; `--keep-duplicate-meshes` creates a comparison candidate.

## Preserved boundaries

Game behavior, save-state effects, GPU synthesis, Blender exports/renders and actual
Wwise conversion were not revalidated in game/runtime applications. These changes
establish source, cache, publication and package integrity; focused in-game checks
remain necessary before release. No package was installed.

The reference corpus, factory Wwise units and unvalidated base-character source
assets remain available for authoring. The review made their deletion conditional
on consumer/conversion/runtime evidence. Production profiles exclude the relevant
development/global-override payloads. Obsolete generated quest outputs are reported
in ownership manifests rather than deleted without provenance.

Use the [build/package guide](../workflows/build-and-package.md) and
[automated gate](../workflows/automated-testing.md) for the maintained commands.
