# `gq000` State

## Runtime Facts

- `gq000_job_accepted`: Patch's scene exited through `job_accept`.
- `gq000_02_started`: the cache stage has initialized.
- `gq000_cache_acquired`: the relay's hacking minigame succeeded.
- `gq000_cache_delivered`: the cache was deposited at the selected drop point.
- `gq000_completed`: Morrow's completion thread has finished.

All five facts are wired across the root, meeting, cache, and delivery phases.
The drop-point controller additionally raises `gq000_datacache` from the quest
package's `friendlyName`; that engine-facing fact is distinct from the authored
`gq000_cache_delivered` milestone.
