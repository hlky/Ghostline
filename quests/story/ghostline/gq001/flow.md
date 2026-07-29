# Ghostline Runtime Flow

| # | Stage | Type | Purpose |
| ---: | --- | --- | --- |
| 1 | `patch_job_offer` | `phone_job_offer` | Patch asks V to meet. |
| 2 | `meet_patch` | `meet_contact` | Reuses the validated `gq000` Patch meeting. |
| 3 | `hack_relay` | `hack_access_point` | Reuses the Quiet Spine cache extraction route. |
| 4 | `meet_iris` | `meet_contact` | Iris inspects the cache and directs its handoff. |
| 5 | `deliver_cache` | `deliver_drop_point` | V deposits the cache and closes the job. |

The canonical distinction from `gq000` is the Iris stage between extraction and
delivery. The complete machine-readable bindings live in
[`implementation/quest.json`](implementation/quest.json).
