# Reviewed journal authoring templates

`catalog.json` names CR2W-JSON donors in
`quests/templates/source/raw/mod/ghostline/journal_templates`. These are stable authoring inputs,
not runtime outputs. Do not regenerate them as a side effect of a quest build
or include them in a binary import unless adding a specific runtime resource.
The original packed resources remain available to binary conversion tools.

The catalog records each donor's source and SHA-256 at extraction. The source
path is provenance, not a live dependency. Each consumer resolves a catalog name
through `quest_content.journal_template_path`; journal changes in another quest
therefore cannot alter its next build.

The `gq000_shapes` journal and `gq000_onscreens` preserve the whole proven baseline
because GQ001 intentionally rewrites that complete tree before adding Iris.
Other journal donors retain only the first phase, required contact/readable
shapes, and the ancestor folders and POI rewritten by their consumers. Contacts
and phases that are cloned retain their nested structure so handle allocation
and output remain stable. `minimum_next_handle` preserves each original donor's
allocation floor after unused branches have been removed. The small file-group
donor replaces a dependency on the complete vanilla onscreen journal slice.
The empty onscreen container serves builders that replace all localized text.

When updating a donor, review its consumers together, refresh provenance, and
compare generated journals and localization before publishing. The extraction
was verified against all 10 builders: all 20 resulting documents were identical
to their previous generated output, including handle IDs. The catalog is plain
authoring metadata; it lives outside `source/raw`.
