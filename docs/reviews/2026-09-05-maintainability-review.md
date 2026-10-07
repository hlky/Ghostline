# Ghostline project maintainability review

Implementation update: all R01–R27 changes are recorded in the [completion report](2026-09-05-maintainability-fixes.md). The findings and counts below describe the original review baseline.

Reviewed 2026-09-05, against the current working tree based on commit `29bdc504cad11fa5e7bcb3e435b93f83eb5f376b`.

Ghostline's largest maintainability problem is duplicated ownership of contracts: stage definitions, resource paths, cache validity, output publication, and build instructions. Several copies already disagree. Consolidating those contracts will remove more costly complexity than general formatting, wholesale directory deletion, or adding a new framework.

The recommended order is to restore the test gate, repair the demonstrated contract failures, consolidate existing helpers, and then split the largest modules along their actual responsibilities. Release payload reduction should use explicit dependency-aware profiles. The current `source/archive` tree is also an authoring and testing workspace, so packing everything is not a reliable definition of a release.

This review produced this report and ignored analysis artifacts only. It did not refactor project source, regenerate packed resources, install anything into the game, or discard existing changes.

## Scope, measurements, and limits

The inventory covers 1,825 existing tracked and non-ignored untracked files, approximately 439.9 MiB. Submodule contents and ignored build/cache directories are excluded from these measurements. Existing uncommitted work, including GQT006, Kimodo, story lipsync, and character changes, was included.

| Area | Measured current content | Review coverage |
| --- | --- | --- |
| Python | 137 files, 80,342 physical lines, including tests and quest scripts | Module/function inventory, dependency boundaries, focused implementation reads, full test discovery, and isolated probes |
| Rust voice crate | 10 source files, 1,783 lines | All modules, tests, Clippy, manifest validation, backend and publication boundaries |
| Quest authoring | Story/prototype quests, examples, GQT harnesses; 14 typed manifests | Compiler/schema agreement, all ten build-script dependency maps, representative content builders and current runtime contract |
| Characters and local UI | Manifests, catalogs, donor/shell templates, Python server, JavaScript, HTML/CSS | Identity, trusted paths, component assembly, previews, state handling, dependencies |
| Braindance/motion | Scene/RID pipelines, Blender adapters, rig contracts, previews, Kimodo | Construction/auditing, codec boundaries, caches, defaults, preflight |
| World discovery/capture | Capture package, Lua runtime, geometry/navigation, render adapter, asset/drop-point indexes, scout/collision helpers | Public boundaries, persistence/protocol, representative algorithms, configuration, tests |
| Item database/gallery | Parser, database, export/render orchestration, HTTP handler and browser script | Cache validation, dependency resolution, module responsibilities, isolated cache probe |
| Packed resources | 507 files; 228.5 MiB | Ownership, registration, release selection, exact-byte duplication; no exhaustive binary semantic audit |
| Editable resources | 227 raw files; 24.4 MiB | Targeted explorer/spec/test evidence; large JSON was not treated as ordinary handwritten code |
| Loose runtime resources | ArchiveXL, TweakXL, autosave config/REDscript | Registration overlap, development/release scope, staging ownership |
| Documentation/reference | 97 Markdown files across the project; 25,923 lines | Routing, active commands, contract drift, generated reference ownership and history |
| External/editor tooling | WolvenKit, modding_docs, ghostline-red submodule boundaries; C# adapter; Wwise; editor state | Integration and provenance, without proposing edits to dependency internals |

This was a section-by-section architectural and correctness review, with deeper inspection of high-maintenance paths. It was not a claim that every binary, every narrative sentence, or every runtime route was independently validated. File and function length helped select inspection targets; length alone is not a finding.

Evidence logs and measurements are under [generated/review](../../generated/review/inventory.json). Exact function-body comparison found 14 duplicate groups of at least 12 lines. Archive hashing found 34 exact duplicate groups containing 9,344,447 bytes of extra copies, approximately 8.91 MiB before archive compression. Different resource paths may still be required, so this is a candidate pool rather than an approved deletion list.

Priorities: **P1** should be addressed before relying on the affected workflow or using it as a refactoring baseline; **P2** is a concrete maintenance/correctness improvement; **P3** is lower-risk cleanup or structural improvement after the contract repairs.

## 1. Repository setup and test baseline

### R01 — P1: Restore the advertised test gate before broad refactoring

The full command documented in the README reports **471 tests, 7 failures, and 6 errors**. Three errors prevent entire modules from loading:

- [test_world_asset_catalog.py:8](H:/projects/Ghostline/tests/test_world_asset_catalog.py:8) imports absent `tools.world_asset_catalog`.
- [test_world_location_database.py:17](H:/projects/Ghostline/tests/test_world_location_database.py:17) imports absent `world_location_database`.
- [test_world_location_dependencies.py:8](H:/projects/Ghostline/tests/test_world_location_dependencies.py:8) imports absent `tools.world_location_dependencies`.

The world-asset catalog is still presented as an active tool in [world-assets.md:82](H:/projects/Ghostline/docs/authoring/world-assets.md:82). This is an incomplete interface retirement or missing implementation, rather than evidence that those tests are disposable. Restore the supported implementation, or explicitly retire its commands, imports, documentation, and tests together after deciding that the capability is no longer wanted.

Of the remaining results, nine failures/errors are current GQT006 content disagreements, and one is the scene actor success fixture. The latter supplies RID/facial indices beyond its fixture arrays in [test_generate_scene.py:589](H:/projects/Ghostline/tests/test_generate_scene.py:589), then expects validation success at line 642. Correct that fixture and retain the validator. Reconcile GQT006 against its intended current graph; blindly deleting assertions or regenerating content would conceal the disagreement.

The 471 count includes failed module imports as test entries; it does not mean the tests inside those missing modules ran. Full output: [python-tests.log](../../generated/review/python-tests.log).

### R02 — P2: Declare the reproducible Python development environment

[README.md:29](H:/projects/Ghostline/README.md:29) goes from submodule initialization to the full test command, but the only Python requirements file is [requirements-world-locations.txt](../../tools/requirements-world-locations.txt). The suite also imports `jsonschema` and `yaml`; the reference generator imports `requests` and Beautiful Soup. These dependencies are not covered by that requirements file.

Introduce one small project environment definition with test dependencies and optional capture/research groups. Record the supported Python version, and make one lightweight check command run the Python suite, authored-manifest/schema parity, and Rust voice tests. GPU synthesis, Blender, Wwise, and game-installed integration checks should remain explicit separate gates. This makes setup reproducible without burdening pure unit tests with every workstation dependency.

The focused Ruff correctness scan found only 20 diagnostics: 16 unused imports, two unused locals, one redundant f-string, and one repeated dictionary key. This is a small cleanup, not the main source of bloat. The repeated `name` key is at [GQT001 build.py:433](H:/projects/Ghostline/projects/test-quests/gqt001/implementation/build.py:433). Review unused assignments for side effects before removing them. Results: [ruff.json](../../generated/review/ruff.json).

## 2. Quest compiler and content generation

### R03 — P2: Give each stage contract one owner

[quest_compiler.py](H:/projects/Ghostline/tools/quest_compiler.py:49) repeats stage knowledge in supported/direct stage lists, implementation modes, required fields, allowed fields, the 1,551-line `load_spec`, output contract validation, template bindings, and builder dispatch. The schema and prose specification add more copies.

All 14 typed manifests load through the compiler, yet current GQT006 fails the editor schema twice. [quest-schema-v1.json:1983](H:/projects/Ghostline/tools/quest-schema-v1.json:1983) rejects supported aftermath/continuation/completion fields in `player_defeat_scene`; [line 582](H:/projects/Ghostline/tools/quest-schema-v1.json:582) rejects supported `opening_branches[].unless`. Stage documentation also disagrees about vehicle fields and whether some stages are template-backed.

There is a second consequence: [validate_stage_contract:2455](H:/projects/Ghostline/tools/quest_compiler.py:2455) does not verify meeting objective and mappin bindings. Changing those manifest fields while leaving the generated child phase unchanged passed validation in both GQ001 meetings: the root can activate the new paths while the child completes/hides old template paths. Required typed fields and separate scalar replacement maps can therefore drift independently. The description entry is legitimately root-owned and should be validated there.

Extract per-stage validation functions and a simple explicit registry for structural fields, builder selection, template policy, and plan metadata. Choose a structural authority for schema generation or parity testing; retain semantic Python checks. Validate owned output properties directly instead of global string membership. This removes repeated synchronization work without introducing a plugin system.

### R04 — P2: Build and validate the complete output set before publishing it

[quest_compiler.py:5910](H:/projects/Ghostline/tools/quest_compiler.py:5910) writes the root before it constructs all child phases. GQT006 and GQT007 repeat this orchestration in their build scripts. A later child failure leaves mixed old/new generation. Removed or renamed stages also leave prior output paths behind.

Expose a shared compile operation returning a validated collection of destination paths and documents. Build everything first, then publish through a shared writer. Add an ownership manifest so obsolete generated paths can be reviewed or excluded from staging. Do not recursively clean `source/raw` or `source/archive`: those directories also contain authored and template-dependent resources.

Acceptance should include failure while constructing a later child, unchanged-input output comparison, and a stage rename whose obsolete output is reported. Preserve the custom GQT006 phase hook rather than copying another entire compile loop.

### R05 — P2: Replace cross-quest output dependencies with stable reusable templates

Journal construction currently follows chains such as GQ000 → GQ001 → GQ002 → GQ003 and GQ001 → GQT001 → GQT004 → GQT003 → GQT002. See [GQ003 build.py:26](H:/projects/Ghostline/projects/ghostline/quests/gq003/implementation/build.py:26) and [GQT002 build.py:71](H:/projects/Ghostline/projects/test-quests/gqt002/implementation/build.py:71).

These dependencies use earlier quests' specific objective/contact/message IDs, not just resource types. For example, [GQ003 build.py:327](H:/projects/Ghostline/projects/ghostline/quests/gq003/implementation/build.py:327) requires the GQ002 meet-Cinder objective. Editing one quest can break an unrelated generator, and a clean build has an implicit order.

Promote the smallest proven journal/objective/contact/conversation/readable shapes into an owned reusable template catalog with provenance. Have `quest_content` consume that catalog. Keep narrative text, objective identities, and quest-specific exceptions in their owning quests. **Do not delete GQ000 first**: its superseded narrative status does not make its runtime templates unused.

### R06 — P2/P3: Finish shared-helper extraction already started in the project

The compiler imports generic graph infrastructure from the GQ000-specific [generate_cache_phase.py:102](H:/projects/Ghostline/tools/generate_cache_phase.py:102) and delivery generator. Template generators then copy device and completion constructors again. The three device-manager bodies at [generate_quest_block_templates.py:68](H:/projects/Ghostline/tools/generate_quest_block_templates.py:68), [generate_advanced_quest_block_templates.py:114](H:/projects/Ghostline/tools/generate_advanced_quest_block_templates.py:114), and [quest_compiler.py:3773](H:/projects/Ghostline/tools/quest_compiler.py:3773) are exact duplicates.

Move handle allocation, `PhaseGraphBuilder`, common node constructors, and phase document assembly into a focused library. Keep existing command filenames as wrappers. Preserve backward-resolvable handles and the proven resource shapes.

Separately, use the existing [quest_content.py](H:/projects/Ghostline/tools/quest_content.py:15) helpers instead of local copies in GQ002/GQ003/GQT001. Six GQT `generate_onscreens` implementations have identical bodies. One resource-construction helper with entries/template/target arguments can replace them. This is a good first behavior-preserving cleanup after restoring the baseline; it requires no new abstraction framework.

## 3. Scene and world resource generators

### R07 — P2: Make scene validation cover every locale and every exit target

[generate_scene.py:2255](H:/projects/Ghostline/tools/generate_scene.py:2255) checks exit names but does not validate their target nodes as it does for entries. Localization descriptor checking at [line 2468](H:/projects/Ghostline/tools/generate_scene.py:2468) handles `db_db`, leaving other locale indices and descriptor/payload variant agreement unchecked.

Three isolated corruptions of a valid GQ000 scene were accepted: an `en_us` payload index of `999999`, a mismatched descriptor variant ID, and an exit pointing to nonexistent node `999999`.

Extract small output-reference validators for all locale descriptors, matching payload variants, and existing `scnEndNode` exit targets. Keep these independent from the construction code. Add corruption tests for these relationships before decomposing scene assembly. Padded sockets, full-width IDs, locale ordering, and lifecycle structures are known resource contracts and should remain.

### R08 — P2/P3: Centralize world identity insertion and stabilize header metadata

[generate_world.py:162](H:/projects/Ghostline/tools/generate_world.py:162) overwrites duplicate anchor names. Node insertion later appends full references without a general uniqueness check. An in-memory dry run accepted a duplicated GQ000 marker and emitted two identical full NodeRefs in the AlwaysLoaded sector.

Give the world builder one insertion operation that records full identities and reports both conflicting source locations. Explicitly represent intentional contextual aliases; do not reject all shorthand reuse indiscriminately.

The same generator uses the current time in headers at [line 127](H:/projects/Ghostline/tools/generate_world.py:127). Two identical-input sector constructions differed only in `Header.ExportedDateTime`. Use a stable or explicitly supplied export timestamp so regeneration produces useful diffs. Keep provenance fields, and normalize machine-specific header paths only when performing cross-checkout comparisons.

Preserve the distinction between Quest and AlwaysLoaded sectors, community readiness gates, device buffers, coordinate handling, and independent graph checks. Their complexity has a runtime purpose.

## 4. Character resources and local character UI

### R09 — P2: Make character identity, output paths, and references one contract

[character_ui.py:84](H:/projects/Ghostline/tools/character_ui.py:84) accepts edited identity/namespace values while retaining trusted output paths. [character_builder.py:1563](H:/projects/Ghostline/tools/character_builder.py:1563) checks output containment but not agreement with the namespace used in resource references.

A Patch manifest edited to namespace `mod\ghostline\characters\review_clone` passed both validators. Its appearance output still targeted the Patch directory while the entity referenced an appearance in the new namespace.

For the current single-manifest editor, keeping identity read-only is the smallest repair. If cloning is intended, derive dependent paths/references from one server-owned identity and validate the complete mapping. Preserve the server's trusted-path filtering, loopback restriction, and serialization lock.

### R10 — P2: Share a staged preview/export cache contract

Three character paths have different cache rules:

- [character_builder.py:2207](H:/projects/Ghostline/tools/character_builder.py:2207) accepts a failed head export when old GLBs exist, then stamps the new fingerprint. A mocked failure reproduced successful stale-output promotion.
- [character_builder.py:2344](H:/projects/Ghostline/tools/character_builder.py:2344) reuses existing head-build morph GLBs without validating the complete requested set and input identity.
- [character_full_preview.py:158](H:/projects/Ghostline/tools/character_full_preview.py:158) fingerprints the parent archive directory. Changing an archive in a nested content directory did not change that cache key.

Reuse the stronger staged-refresh pattern already implemented in [character_asset_index.py:484](H:/projects/Ghostline/tools/character_asset_index.py:484). A narrow helper should describe input identities, stage fresh exports, verify complete outputs, and promote only after success. Keep format-specific checks in their owning code. This removes divergent policy and protects reviewed caches during failed refreshes.

### R11 — P3: Parse large build inputs once per request

Validation assembles appearances at [character_builder.py:1618](H:/projects/Ghostline/tools/character_builder.py:1618); generation assembles them again, and output validation repeatedly reloads catalogs and donor files. An instrumented three-appearance Goth Baddie build read the shell/component descriptor/883-KB donor seven times each, the 2.2-MB entity shell three times, and the catalog four times before packing or Blender.

Use a build-scoped context of immutable parsed inputs and selected prototype metadata. Validate selection coverage first, then copy only selected components for assembly. Avoid a global mutable JSON cache. The benefit is clearer ownership and less duplicated work; the measured local sequence was about 0.83 seconds, so this is not the highest-priority performance issue.

The plain JavaScript UI and pinned Three.js dependency are appropriately small. A frontend framework, state-management package, or bundler would add maintenance without addressing these defects.

## 5. Braindance, motion, rigs, and previews

### R12 — P2/P3: Split braindance at its existing responsibility boundaries

[braindance_pipeline.py](H:/projects/Ghostline/tools/braindance_pipeline.py:1643) is 4,016 lines; clue configuration is 602 lines and the scene auditor is 1,102. [braindance_rid.py:1842](H:/projects/Ghostline/tools/braindance_rid.py:1842) mixes actor-slot allocation, pose encoding, camera tracks, metadata, and assembly in a 436-line compiler operation.

Keep clue construction and clue auditing near each other in a focused module; separate linkage from conversion, packaging, and runtime evidence; isolate the animation codec as pure code. Preserve existing script entry points. Share indexing/traversal/context records, while keeping the validator independent of the generator's expected output.

Do not merge SIMD preview decoding and compressed animation writing just because both manipulate motion. Do not replace named-joint rig contracts with GLB bone order. Those are materially different representations and authorities.

### R13 — P2: Repair stale defaults and move preflight ahead of mutation

[braindance_scene.py:27](H:/projects/Ghostline/tools/braindance_scene.py:27) points its default spec at `source/braindance/tests/...`, while the fixture now lives under `braindance/tests/...`. Running the default `validate` command fails with a missing-file error. All four default command routes inherit the same stale path.

[kimodo_braindance.py:262](H:/projects/Ghostline/tools/kimodo_braindance.py:262) retargets before rejecting an incompatible `--bake-after`/output combination. Move that check into planning so an invalid request fails before expensive work or a saved blend. Share the fixture default and executable resolution used by the broader authoring pipeline.

Keep Kimodo as a small offline adapter, Blender-specific code separate from pure Python, and full-character preview scoped to its documented silhouette purpose. Expanding preview fidelity is feature work, not cleanup.

## 6. Voice, localization, lipsync, and Wwise

### R14 — P1: Consolidate localization writers; they already emit different voice paths

[generate_dialogue_localization.py:111](H:/projects/Ghostline/tools/generate_dialogue_localization.py:111) writes `audio_path` into both male and female resource paths. [Rust localization.rs:104](H:/projects/Ghostline/tools/ghostline-voice/src/localization.rs:104) honors the explicit male path. Current authored GQT006 lines contain `male_audio_path`, and quest READMEs still advertise the Python generator.

An isolated invocation confirmed that the explicit male resource path is ignored and the female path is emitted instead. Fix that behavior first. Select one localization construction implementation and keep the other CLI as a compatibility adapter. During migration, compare semantic payloads from the same gendered and shared-voice fixtures. Pure localization must not require GPU synthesis.

### R15 — P1: Key audition reuse by the synthesis request

[render.rs:153](H:/projects/Ghostline/tools/ghostline-voice/src/render.rs:153) derives seed identity from seed base, line key, and version. [reusable_output:231](H:/projects/Ghostline/tools/ghostline-voice/src/render.rs:231) checks seed, filename, and the existing audio's own hash, but not changed text, embedding, language, sampling, frame cap, or model identity. The reuse return also precedes the `force` check.

Changing dialogue text or voice settings can therefore report successful reuse of the old take; `--force` cannot bypass a receipt that matches the old seed and audio. A corrupt receipt can error before force is considered.

Keep stable seeds, but add a versioned request fingerprint and require both matching inputs and valid output. Define force behavior explicitly. Use the existing backend seam for fake-backend tests of unchanged reuse, changed text/embedding/settings, corrupt audio/receipt, and force. The current hash-equals-itself test at [render.rs:348](H:/projects/Ghostline/tools/ghostline-voice/src/render.rs:348) does not exercise these behaviors.

### R16 — P2: Use one candidate inventory from render through review and promotion

The Rust renderer writes `<dialogue>/<line>-versionNN.wav` and emits structured candidate reports. [build_voice_selection_csv.py:56](H:/projects/Ghostline/tools/build_voice_selection_csv.py:56) instead scans `<design>/<line>/take-*.wav`. When no design-reference row is selected, [promote_voice_selections.py:63](H:/projects/Ghostline/tools/promote_voice_selections.py:63) assumes Cinder and rejects manifests containing none.

Temporary fixtures reproduced successful CSV generation with zero candidates from the current renderer layout, and rejection of a complete Iris-only selection. Consume the structured renderer report as the canonical inventory, with an explicit historical-layout adapter. Make voice-design consistency a per-speaker configured rule. Retain human-selected takes, receipts, source WAVs, and hashes; do not remove the legacy voice-design operation until its replacement exists.

### R17 — P2: Make lipsync checkpoints and single/batch compilation share explicit settings

[build_lipsync_corpus.py:497](H:/projects/Ghostline/tools/build_lipsync_corpus.py:497) omits FPS, track selection, and input identities from its checkpoint profile. A temporary checkpoint was reused after changing FPS/track set, leaving the old CSV untouched. Separate expensive alignment from curve sampling and key each stage by its actual inputs. Changing sampling should regenerate CSV without unnecessarily repeating alignment.

[compile_lipsync_line.py:473](H:/projects/Ghostline/tools/compile_lipsync_line.py:473) and [compile_lipsync_manifest.py:44](H:/projects/Ghostline/tools/compile_lipsync_manifest.py:44) duplicate synthesis, speech windows, donor controls, track replacement, duration, and reporting. They already differ in exposed policies. Extract an aligned-line-to-animation operation with explicit settings; let each CLI own batching and publication. Preserve the batch command's persistent aligner and compare equivalent single/batch synthetic fixtures.

Keep corpus construction, numerical learning/synthesis, and production compilation distinct. Their different jobs and checks are useful functionality.

### R18 — P2: Validate the whole Wwise result set before publishing WEMs

[convert_wavs_to_wem.ps1:155](H:/projects/Ghostline/tools/convert_wavs_to_wem.ps1:155) recursively selects the first sorted basename match in a shared output tree, copies it immediately, then reports missing later files. Duplicate basenames across runs/platforms can be ambiguous, and an incomplete conversion can partially update the active set.

Use a run-scoped output directory with an exact platform mapping. Resolve one fresh result for every requested output before copying any destination; stage the complete set. Preserve manifest-scoped selection, XML escaping, `-NoCopy`, and original WAVs. A fake conversion tree can test duplicate/missing output without invoking Wwise.

The 23 factory Wwise work units account for about 1.60 MiB and are a lower-priority pruning candidate. Do not delete them wholesale: the active conversion preset is in [Factory Conversion Settings.wwu:110](<H:/projects/Ghostline/wwise_conversion/Conversion Settings/Factory Conversion Settings.wwu:110>). Prune through a minimal saved project only after proving conversion equivalence.

## 7. World discovery/capture and item rendering

### R19 — P2: Apply one item-render report validator everywhere

[item_database.py:1334](H:/projects/Ghostline/tools/item_database.py:1334) treats the existence of an exact-cache report as sufficient for reuse. Later it records that render as complete without verifying image existence. The compatible-cache branch already checks images and settings at [line 1204](H:/projects/Ghostline/tools/item_database.py:1204).

An isolated probe supplied a report naming a nonexistent hero image. The operation returned `reused=1`, `failures=[]`, and wrote a complete database record. Extract the stronger existing report check and use it for exact reuse, compatible reuse, and post-render publication. Invalid caches should become pending; malformed reports should become per-item failures. Evidence: [item_cache_probe.py](../../generated/review/item_cache_probe.py).

### R20 — P3: Extend the existing world package boundaries, and split item orchestration

`world_locations` already has useful separation among configuration, model, extraction, planning, database, protocol, and CLI. Keep its SQLite/R-tree/FTS design, incremental indexing, resumability, and file protocol. An ORM or generic workflow engine would not simplify the current requirements.

The next focused seams are [CaptureController._save_capture:591](H:/projects/Ghostline/tools/world_locations/capture.py:591), which combines metadata resolution, sidecars/images, hashing, and database publication, and [world_location_render_blender.py](H:/projects/Ghostline/tools/world_location_render_blender.py:1073), which combines configuration, add-on compatibility, scene import, diagnostics, rendering, and batch reports. Extract pure metadata/report planning before touching the proven capture lifecycle. Preserve separate completion handling; its stale-error barrier is intentional.

[item_database.py:1226](H:/projects/Ghostline/tools/item_database.py:1226) has a 326-line render orchestrator inside the same module as Tweak parsing, schema, export, HTTP server, and CLI. Separate catalog/database operations, export/render jobs, and gallery serving. Share cache validation first so splitting the file does not merely relocate inconsistent logic.

The indoor browser, Black Lantern scout, collision finder, and offline capture planner serve different tasks. Keep their narrow entry points. Consolidate low-level parsing or CET install helpers only when their contracts match; do not combine manual scouting and automated capture into one larger controller.

## 8. Explorers and common utilities

### R21 — P3: Remove proven helper duplication without creating a miscellaneous utility framework

Five explorer classes contain the same 14-line scalar search loop; examples are [explore_scene.py:439](H:/projects/Ghostline/tools/explore_scene.py:439) and [explore_journal.py:208](H:/projects/Ghostline/tools/explore_journal.py:208). Put that operation alongside the existing `walk` and path formatting in [cr2w_helpers.py](H:/projects/Ghostline/tools/cr2w_helpers.py:27), and preserve each explorer's domain commands.

Character indexing/building and the two resource indexes also repeat the same atomic JSON writer. Consolidate identical policies during nearby work. Do not automatically unify every `walk`, scalar-unwrapper, or `Vec3`: some return paths, some yield objects, and navigation explicitly uses a different stored coordinate order. Shared code needs a shared contract, not a similar name.

Avoid adding a CLI framework merely to remove small argparse wrappers. The current focused explorers are valuable because they keep large resource documents out of routine editing and review.

## 9. Native boundaries, packaging, and release bloat

### R22 — P2: Resolve external tools and generated schema identity centrally

Game/WolvenKit/Blender paths and discovery policies are repeated across character, item, braindance, motion, and packaging tools. Some overrides are not fully honored: [item_database.py:1108](H:/projects/Ghostline/tools/item_database.py:1108) passes the hardcoded `DEFAULT_KRAKEN`, and [package_standalone.py:118](H:/projects/Ghostline/projects/test-quests/gqt006/implementation/package_standalone.py:118) uses `WOLVENKIT_DEFAULT` inside validation despite the command's `--wolvenkit` option.

Use a small immutable toolchain configuration with precedence of explicit arguments, local configuration/environment, then discovery. Resolve once and pass it through. Invalid explicit overrides should fail clearly rather than silently selecting another version. This can extend the existing local-path configuration pattern; it does not require a plugin architecture.

[ghostline_red.py:25](H:/projects/Ghostline/tools/ghostline_red.py:25) accepts an existing ignored schema based only on file existence. Record schema-generation inputs, including pinned WolvenKit and generator identity, so submodule updates invalidate stale schemas. Keep dependency code in its own submodules and test the adapters at their boundaries.

### R23 — P2: Make C# animation import transactional

[WolvenKit.AnimImport/Program.cs:100](H:/projects/Ghostline/tools/WolvenKit.AnimImport/Program.cs:100) rewrites the existing animset's rig before invoking the actual importer at line 116. Import failure or an exception leaves the original partially changed.

Stage a copy of the existing animset, apply the rig change and import there, verify a readable successful result, then replace the destination. Keep this adapter narrow; its 117 lines do not justify a new C# framework. The dependency service-registration code is appropriate integration glue.

### R24 — P2: Define release profiles instead of shipping the entire authoring tree

The current archive input includes 93 base character resources totaling 155.44 MiB, four base-path lipsync resources totaling 2.03 MiB, eight tutorial resources totaling 4.12 MiB, story assets, test quests, and twelve packed quest-block authoring templates. These have different ownership and shipping purposes.

[Ghostline.archive.xl:7](H:/projects/Ghostline/projects/ghostline/source/resources/Ghostline.archive.xl:7) activates GQT005–GQT007 alongside story quests. The loose-resource tree includes test-time autosave suppression, and the separate Goth Baddie registration overlaps the combined install. The runtime evidence already records disabling that standalone install to avoid competition.

Introduce explicit story, individual test-quest, and development profiles declaring archive roots/files, loose resources, registration, dependencies, and exclusions. Generate staging from a profile and verify its dependency closure. Distinguish the global base character overrides from legitimate base-path lipsync registration; excluding all `base` paths would be incorrect.

The exact-byte duplication pool is 8.91 MiB. Good candidates for investigation include shared character body parts and copied tutorial textures, but path rewrites/resource links and standalone dependency checks must precede removal. The 155.44-MiB base character set is a much larger release-scope decision, not proven removable content. Likewise, the twelve compiler templates are candidates for release exclusion, while their raw and binary authoring templates remain available to builds.

Payload evidence: [archive-duplicates.json](../../generated/review/archive-duplicates.json). No claimed savings here are compressed-download or Git-history savings.

### R25 — P2: Turn packaging verification into a reusable operation

[package_standalone.py:188](H:/projects/Ghostline/projects/test-quests/gqt006/implementation/package_standalone.py:188) packs, checks that an archive exists, stages it, and can install it. It does not perform the listing/extraction/payload comparison required by the [build guide:78](H:/projects/Ghostline/docs/workflows/build-and-package.md:78). Its successful hash describes the produced archive but does not verify its contents.

Extract a shared package operation: select a profile, stage fresh inputs, pack with the supported packer, list and extract, compare intended path sets and payload hashes, then produce a verified install tree and receipt. Installation should consume that verified result. This removes lengthy manual procedure duplication and prevents a smaller convenience script from bypassing the stronger workflow.

Keep packing distinct from loose-resource staging and keep game installation explicit. Preserve prior candidates/evidence when producing a new one.

## 10. Documentation, reference data, and repository hygiene

### R26 — P1: Remove contradictory active packer instructions

The [build guide:47](H:/projects/Ghostline/docs/workflows/build-and-package.md:47) correctly requires WolvenKit packing because the native packer produced a reproducible startup crash. Yet:

- The same guide at [line 73](H:/projects/Ghostline/docs/workflows/build-and-package.md:73) says WolvenKit is not for routine packing.
- The [CR2W skill:96](H:/projects/Ghostline/agent/skills/ghostline-wolvenkit-cr2w/SKILL.md:96) says not to use WolvenKit CLI for routine pack.
- The [tool catalog:138](H:/projects/Ghostline/docs/reference/tool-catalog.md:138) actively demonstrates native packing and describes an older successful extraction baseline.

Make the build guide the sole owner of the runtime packing rule and link to it from skills/catalogs. Keep native pack experiments in dated history with their limits. Byte-identical extraction does not establish a runtime-safe archive; the project already has evidence of that distinction.

### R27 — P3: Complete documentation ownership and prune small real clutter

The routing structure in `README`, `AGENTS`, and the documentation map is useful. Apply its stated ownership consistently:

- [world-locations.md:11](H:/projects/Ghostline/docs/authoring/world-locations.md:11) and line 302 describe `DwmFlush`; the implementation now uses Windows Graphics Capture and a visual settling interval. Its `fov_tolerance_degrees` setting has no consumer, and tests explicitly permit FOV drift. Remove or rename inert configuration instead of leaving a misleading control.
- [runtime-flow.md:331](H:/projects/Ghostline/projects/ghostline/quests/gq000/implementation/runtime-flow.md:331) records a 20-unit someone-coming radius; the current world spec and test use 6. Link current numeric contracts to authoritative specs or generate those tables.
- The 1,340-line runtime-testing document combines an active candidate with extensive dated investigations. Keep a compact current candidate index and move dated records into history with stable links; retain their hashes and explanations.
- The three generated vanilla quest pages total 13,347 lines. They are useful research, not handwritten maintenance debt. Keep them generated and read-only. [build_quest_reference.py:259](H:/projects/Ghostline/tools/build_quest_reference.py:259) depends on an external journal export and live index pages; record input hashes/snapshots and the generation command before treating regeneration as reproducible enough to delete reference output.
- `.projectFiles/fileTreeState.json` is still tracked despite its ignore rule. Stop tracking editor state while retaining each user's local file. Review `layout.xml` as editor state separately; do not confuse it with packed asset data.
- Trim unrelated stock sections in `.gitignore` only as a small hygiene edit. Retain project-specific generated/build/local-path exclusions. Keep the experimental ArchiveXL patch with its investigation provenance until an explicit retirement decision; it is already outside runtime resources.

Do not delete the 148-MiB reference corpus simply because it is large. It includes fixtures and provenance used by generators and tests. First record consumers and reproducible extraction; separate reusable fixtures from optional research caches if that produces a real workflow benefit.

## Recommended implementation sequence

Each step should be independently reviewable. Avoid mixing broad mechanical movement with gameplay changes.

| Order | Scope | Completion evidence |
| --- | --- | --- |
| 1 | R01, R02, R26: test baseline, setup, active packing rule | Missing interfaces deliberately restored/retired; full test gate green; documented commands agree |
| 2 | R14, R15, R16: localization and voice authoring contracts | Gendered/shared localization parity; fake-backend cache tests; a non-Cinder render-report → selection → promotion fixture |
| 3 | R03, R07, R08, R09: authoring identity and validation | All authored manifests pass schema/compiler agreement; deliberate graph/localization/path corruptions are rejected |
| 4 | R04, R10, R18, R19, R23, R25: output and cache publication | Failed refresh/import/late artifact leaves prior valid output intact; incomplete cache never publishes as complete; archive payload comparison gates install staging |
| 5 | R05, R06, R11, R17, R21, R22: shared core operations | Existing CLIs preserved; deterministic generated payloads equivalent; duplicated contract implementations reduced |
| 6 | R12, R20: large-module decomposition | Focused domain modules; independent validators retained; no new framework or new runtime feature |
| 7 | R24, R27: release reduction and documentation cleanup | Profile-specific path/dependency audit; runtime smoke checks for retained resources; measured payload reduction; evidence/history remains accessible |

The immediate low-risk removal work is unused imports, the repeated dictionary key, identical explorer searches, duplicate onscreen builders, superseded active instructions, and tracked editor state. Large resource removal and GQ000 retirement come later because their consumers still exist.

## Validation performed

- `python -B -m unittest discover -s tests -v`: **471 reported tests; 7 failures, 6 errors**, completed in 24.216 seconds. The failures are part of the reviewed starting worktree, not introduced by report generation.
- Focused quest/compiler run: **115 tests, one existing scene-fixture failure**. Focused character/braindance run: **108 passed**. These overlap the full suite and should not be added to its count.
- `cargo test --manifest-path tools/ghostline-voice/Cargo.toml --locked --offline`: **6 library tests passed**, no binary/doc tests.
- Strict Rust Clippy over all voice targets/features: **passed**. Voice CLI validation: **8 GQ003 dialogues, 128 lines passed**.
- All **14 typed quest manifests** passed compiler loading; the current GQT006 manifest had the two described editor-schema disagreements. All **20 raw built-in templates** passed the standalone no-forward-handle-reference validator.
- Focused read-only or isolated probes confirmed scene validation gaps, meeting-field validation gaps, duplicate world identity, timestamp-only drift, character identity/cache failures, item-cache false success, Python localization divergence, candidate-review incompatibility, and lipsync checkpoint reuse.
- Exact-byte archive hashing and a focused Ruff `F` scan supplied the bloat/hygiene measurements. No automatic formatter or linter fix was applied.

No GPU synthesis, Blender render/export, Wwise conversion, game install, archive repack, or in-game playthrough was performed. No conclusion here treats offline validation as runtime proof. External dependency internals were not reviewed as Ghostline-owned code.

The detailed working notes remain in [quest-review.md](../../generated/review/quest-review.md), [character-review.md](../../generated/review/character-review.md), and [voice-review.md](../../generated/review/voice-review.md). They are ignored review scratch; this document is the durable consolidated report.
