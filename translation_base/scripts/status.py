#!/usr/bin/env python3
"""Progress report:  python3 translation_base/scripts/status.py"""
import json, os, glob, collections
HERE = os.path.dirname(os.path.abspath(__file__)); BASE = os.path.dirname(HERE)
idx = json.load(open(os.path.join(BASE, 'metadata', 'chunk_index.json'), encoding='utf-8'))
print(f'{"table":22s} {"files":>6s} {"done":>5s} {"rows":>6s} {"chars":>9s}  progress')
gf = gd = 0
for t, info in idx['tables'].items():
    files = sorted(glob.glob(os.path.join(BASE, 'work', t, '*.json')))
    done = 0
    for p in files:
        doc = json.load(open(p, encoding='utf-8'))
        filled = total = 0
        for it in doc['items']:
            for f, v in it['target'].items():
                if v is None: continue
                total += 1; filled += 1 if str(v).strip() else 0
            for s in it.get('content_sections', []):
                if s['source']:
                    total += 1; filled += 1 if str(s.get('target', '')).strip() else 0
        if total and filled == total: done += 1
    gf += len(files); gd += done
    bar = '#' * int(20 * done / max(1, len(files)))
    print(f'{t:22s} {len(files):6d} {done:5d} {info["total_rows"]:6d} '
          f'{info["total_source_chars"]:9d}  [{bar:<20}] {100*done//max(1,len(files)):3d}%')
print(f'\n{"TOTAL":22s} {gf:6d} {gd:5d}   ->  {100*gd//max(1,gf)}% of files complete')
