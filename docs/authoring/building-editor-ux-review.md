# Building Lab UX review and React migration

Reviewed on 2026-10-26 in the in-app browser at the working local editor, using
the furnished AKPP layout. This is an editor review, not an in-game playtest.
The three baseline captures were saved and visually inspected before changes.
The existing dark slate palette, lime selection accents, measured geometry and
plan/3D workflow supplied the visual target; this is an evolution of that UI.

## 1. Open the workspace and edit a selection — improved

The baseline's useful plan/3D pairing was dominated by one long sidebar mixing
tools, room properties, module lists, native navigation and quest data. In the
captured state, quest NodeRefs filled most of the sidebar and hid routine
construction controls. Object fields were far from the thing being selected.

The migration introduces Build, Objects, Quest and Project panel navigation,
plus a persistent selection inspector. Scene objects can be filtered, retained
shell references are grouped separately, and expert NodeRefs/navigation use
progressive disclosure. Selection and tool states are explicitly indicated.
The source layout and compiled geometry contract are preserved.

Baseline:
![Original workspace](../../projects/experiments/building-lab/generated/react-migration/audit/01-workspace.png)

Updated workspace:
![React workspace](../../projects/experiments/building-lab/generated/react-migration/01-workspace-after.png)

Browser checks: loaded AKPP; edited desk X from 2.10 to 2.15 m and undid it;
invalid room width 1 m reported the compiler error and restored the valid
field/scene; created an empty building, drew a 6 × 6 m room, and undid both
actions to restore AKPP. Saving the restored unchanged layout succeeded.

Accessibility: labeled form controls, focus outlines, keyboard tool shortcuts,
Escape-to-cancel fields, native dialogs and live status/error text are present.
Canvas-only drawing and some wall operations still require a pointer; numeric
room/object fields provide an alternative for edits after selection, not a
complete keyboard alternative for creating geometry. No WCAG conformance claim.

## 2. Find a module and inspect it before placement — improved

The baseline exposed the full measured corpus and filters, but began with a
dense wall of filenames and an unexplained empty 3D preview. Technical names
and dimensions competed with selection and placement. The type list included
furniture below architecture types, making office dressing less discoverable.

The new library has role badges, clearer names, visible measured dimensions,
preparation status, a selected state, real geometry preview and a placement
action beside that preview. Furniture/equipment types come first. Source paths
remain available on demand. Empty search results offer filter recovery.
Search aborts stale requests so older results cannot replace the latest query.

Baseline:
![Original library](../../projects/experiments/building-lab/generated/react-migration/audit/02-library.png)

Updated library:
![React library](../../projects/experiments/building-lab/generated/react-migration/02-library-after.png)

Browser checks: searched “file cabinet”, received the two measured variants,
selected the tall cabinet, loaded its preview and appearance options, and saw
the placement action enabled. The preview uses neutral materials, not final
game shading. Long native resource names remain technical; the displayed
labels have not been hand-curated for the whole catalogue.

Accessibility: search and filters are labeled, selected results use pressed
state, native modal focus is contained, and errors/loading counts are exposed.
Tiny dimensions and technical paths still need user testing at zoom and on
lower-resolution displays. No screen-reader or contrast certification performed.

## 3. Review and export a native project — verified

The baseline correctly listed compiler warnings, but printed excessive anchor
precision and offered no lasting export receipt in the dialog. It was easy to
confuse native serialization success with runtime readiness.

The new review rounds display coordinates without changing source precision,
groups validation notes, explains that exports do not install the game, reports
progress, and retains a checked readback result with ZIP link and SHA-256.
Errors stay in the dialog. Native export blocks dismissal while its build is
running, so progress is not silently abandoned.

Baseline:
![Original export review](../../projects/experiments/building-lab/generated/react-migration/audit/03-export.png)

Updated result:
![React export result](../../projects/experiments/building-lab/generated/react-migration/03-export-after.png)

Browser export `9b370777bfd3` completed eight native readbacks; its frozen
authoring layout equals the saved AKPP source. The ZIP SHA-256 was
`de0e42eac1efccfa17d6ac7148ef9edeafed51f44d563676c43acc1c75b8f9b7`.
No in-game archive was installed. Compiler notes still require interpretation
and a focused game playtest; this UI does not certify engine reachability.

## Engineering verification and remaining scope

React UI, strict TypeScript contracts/store/API and Tailwind production build
pass. Four new state tests, four retained wall tests and 79 Python building
tests pass. Full dependency audit reports no known vulnerabilities at this
verification. Vite development GET and POST proxy calls were checked against
the guarded loopback Python API. Original installed AKPP archive hash remains
`181706ecb24238ab310fc51261723250a96f996caaa13ac1b385e9a3a29de6f7`.

The measured SVG/Three.js adapters and pure wall helpers remain isolated
JavaScript; React owns the rest of the UI and state. Native building/compiler
semantics were not rewritten. Source saving and installed game mods are separate
operations. The server remains loopback-only; no hosting/deployment was added.
See [frontend ownership and setup](../../tools/building_ui/README.md).
