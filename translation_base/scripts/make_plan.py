#!/usr/bin/env python3
"""Regenerate PLAN.md from metadata/chunk_index.json."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__)); BASE = os.path.dirname(HERE)
idx = json.load(open(os.path.join(BASE, 'metadata', 'chunk_index.json'), encoding='utf-8'))
ORDER = ['categories', 'ruqyah_categories', 'sections', 'subcategories',
         'ruqyah_subcategories', 'ruqyah_videos', 'drawer_items',
         'duas', 'ruqyah_instants', 'ruqyah_details', 'dua_infos']
L = ['# Translation Plan', '',
     'Tick a file off when `verify.py` passes on it. Work top to bottom: the small',
     'tables settle the vocabulary that the long prose then has to match.', '',
     f"Budget {idx['budget_chars']} source characters per file, "
     f"max {idx['max_rows_per_file']} rows, big rows split at paragraph boundaries.", '',
     '| | Table | Files | Rows | Source chars | Source |', '|---|---|---:|---:|---:|---|']
for t in ORDER:
    if t not in idx['tables']: continue
    v = idx['tables'][t]
    L.append(f"| [ ] | `{t}` | {len(v['files'])} | {v['total_rows']} | "
             f"{v['total_source_chars']:,} | {v['source'].upper()} |")
tot = idx['totals']
L += [f"| | **total** | **{tot['files']}** | **{tot['rows']}** | **{tot['chars']:,}** | |", '',
      '---', '']
for t in ORDER:
    if t not in idx['tables']: continue
    v = idx['tables'][t]
    L += [f"## `{t}`", '',
          f"Source: **{v['source'].upper()}** · fields: {', '.join('`'+f+'`' for f in v['translate_fields'])}"
          f" · key: {', '.join('`'+k+'`' for k in v.get('key_fields', ['id']))}", '',
          '| | File | Rows | IDs | Chars | Items |', '|---|---|---:|---|---:|---:|']
    for f in v['files']:
        L.append(f"| [ ] | `{f['file']}` | {f['rows']} | {f['id_range']} | "
                 f"{f['source_chars']:,} | {f['items']} |")
    L.append('')
open(os.path.join(BASE, 'PLAN.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print('PLAN.md written:', sum(len(v['files']) for v in idx['tables'].values()), 'files listed')
