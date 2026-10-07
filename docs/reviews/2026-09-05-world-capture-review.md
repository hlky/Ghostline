# World database capture and candidate review — 2026-09-05

Scope: improve reliable captures and useful screenshots, with supporting fixes
to planning, candidate evidence, retry selection, and export. This pass changes
Python tools, the repository CET runtime, tests, and documentation. It does not
install the runtime, execute an in-game capture, replan the production database,
or modify packed resources. Existing work from the quest migration is preserved.

## Existing evidence

The production database was opened read-only. Its 14,948 places contained 1,603
captured, 161 failed, 12,861 pending, 322 disabled, and one interrupted location.
All places still needed metadata; all 1,603 images needed visual UI review.
Historical attempts recorded 350 protocol, 340 validation, 172 capture, and 79
runtime timeout failures. Several blur failures had discarded readiness evidence.
Accepted historical sidecars could report `ui_suppressed=false`, and the latest
session had not verified restoration. These records remain unchanged.

## Changes

| Area | Finding and resulting behavior |
| --- | --- |
| Readiness | Python now requires UI and weapon suppression, correct dimensions, finite pose values, and position tolerance. Readiness is checked through settling and frame acquisition. |
| Frame delivery | Capture has an external deadline even when WGC delivers no frames, and requires advancing presentation timestamps. |
| Runtime recovery | Protocol messages must match schema, session, and command. Retries require verified restoration; failed restoration retains recovery state. CET also restores after a lost controller between destinations. |
| Capture lifetime | Controller heartbeats continue through slow validation, encoding, storage, and acknowledgement. Persisted pose, readiness, FOV, and runtime area use the verified capture-time snapshot while retaining the initial ready event. |
| Failure evidence | Attempts retain ready/actual-pose evidence, precise failure codes, structured validation details, and bounded lossless WebP previews of rejected frames. |
| Duplicate images | New images record pixel and perceptual fingerprints. Exact repeated pixels at another destination are rejected; perceptual similarity alone remains review evidence. |
| Planning | Unchanged replans preserve queue, failure, capture, and runtime metadata history. Changed viewpoints or anchors require recapture and cannot reuse publication eligibility. Scope filtering precedes spacing; unchanged captured representatives are preferred. |
| Spatial selection | Nearest fast-travel and road selection searches far enough to prove the nearest result, including candidates beyond the first occupied R-tree window. Numeric inputs and source positions reject malformed/nonfinite values. |
| Object viewpoints | Object offsets use reviewed family calibration rather than treating streamed bounds as local mesh extents. The current 115,531 calibrated, capture-enabled features had no nondegenerate XY bounds, so this correction does not shift their present offsets. |
| Candidate provenance | Indoor records retain source SHA-256/size, explicitly scope quest evidence to their source sector, and mark walkability and visibility unverified. Spatial cache fingerprints detect individual file changes and renames. |
| Retry selection | Captures accept explicit location/category filters. Recapturing successful images requires explicit IDs. Queue changes refuse active sessions and retain evidence history. |
| Publication/export | Each image is checked against its own files, hashes, sidecar identity, validation, and session restoration, plus the current location binding. Exported observed pose and FOV belong to that image, not a later attempt. Report paths cannot overwrite database or capture evidence. |
| Visual review | A static HTML/JSON gallery shows latest images, failures, diagnostic previews, measurements, source details, and publication blockers. Search, filters, pagination, full-size links, and selected retry commands support focused recapture. |

Shared capture assessment is used by session publication, export, and the gallery.
The planner reset helper and CLI share one retry operation. These boundaries keep
eligibility and recovery rules from drifting across separate tools.

## Verification

The real-data gallery at `generated/world-capture-review/review.html` includes
all 1,764 captured/failed locations. Browser checks covered loaded thumbnails,
single-ID search, combined category/area filters, failed-location diagnostics,
pagination, expanded publication blockers, and the exact quoted retry command.
No browser errors were reported. The gallery is a read-only snapshot and its
default mode explicitly states that image hashes were not recalculated.

Focused regression tests cover capture/runtime behavior, Lua restoration with
mocked game APIs, planning and nearest selection, evidence isolation, protected
report destinations, gallery publication rollback, and CLI selectors.

Final project gate: **733 Python tests, six Rust tests, and Ruff passed**.
`git diff --check` passed. Independent re-probes verified source-binding
invalidation, per-image export metadata, protected report destinations,
heartbeats during a simulated slow save, and capture-time pose persistence.
The complete baseline query snapshot still matched after gallery generation.
Logs and comparison evidence are under `generated/world-capture-review/`.

## Runtime validation still needed

The offline tests do not establish live CET/WGC behavior. Install the updated CET
runtime and run a small representative batch before expanding capture. Confirm
HUD suppression, stable frames, wrong/unreachable destinations, interruption
recovery, and restoration in the game. Configure representative HUD templates
before publication; missing templates continue to require visual review.

Heading and FOV differences remain diagnostics. Existing samples showed roughly
51 degrees observed against 80 requested, but camera conventions have not been
calibrated in-game. Candidate rankings and technical image scores do not prove
accessibility, unobstructed framing, or suitability for a quest.

Commands and operation details: [world location authoring](../authoring/world-locations.md).
