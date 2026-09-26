# Urdu review: drawer items

Reviewed on 2026-09-24 against the routed Bengali source,
`GLOSSARY.json`, and the project's natural-Urdu standard.

| File | Rows | Split items | Result |
|---|---:|---:|---|
| `work/drawer_items/drawer_items_001.json` | 3 | 4 | Reviewed; verification passed |
| `work/drawer_items/drawer_items_002.json` | 3 | 4 | Reviewed; verification passed |

## Checks completed

- Translated every user-visible title, hero title, paragraph, heading, and list
  detail in the structured `content` data.
- Read the Urdu continuously for clarity, grammar, respectful address, and
  consistent app terminology.
- Preserved product and website names, Arabic book titles, IRD, IDs, ordering,
  structure, empty source headers, and nullness.
- Converted the Bengali year and quantity to the required ASCII forms (`2012`
  and `200`) without changing their values.
- Ran `verify.py` on both files individually and on the complete
  `drawer_items` table; all checks pass.

This completes the Urdu targets for all six drawer screens, including privacy,
copyright, about, credits, app information, and contact content.
