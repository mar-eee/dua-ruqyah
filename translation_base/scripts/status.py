#!/usr/bin/env python3
"""
Progress report and, more importantly, where to start next.

    python3 scripts/status.py

Reads the work files themselves, so it can never go stale the way a hand-kept
note does. A file counts as done when every non-null target is filled.
"""
import json, os, glob

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)

# Small tables first: they settle the vocabulary the long prose has to match.
ORDER = ['categories', 'ruqyah_categories', 'sections', 'subcategories',
         'ruqyah_subcategories', 'ruqyah_videos', 'drawer_items',
         'duas', 'ruqyah_instants', 'ruqyah_details', 'dua_infos']


def counts(path):
    """(filled, total) translatable slots in one work file."""
    doc = json.load(open(path, encoding='utf-8'))
    filled = total = 0
    for it in doc['items']:
        for v in it['target'].values():
            if v is None:
                continue
            total += 1
            filled += 1 if str(v).strip() else 0
        for s in it.get('content_sections', []) + it.get('group_items', []):
            if s.get('source'):
                total += 1
                filled += 1 if str(s.get('target', '')).strip() else 0
    return filled, total


def main():
    idx = json.load(open(os.path.join(BASE, 'metadata', 'chunk_index.json'), encoding='utf-8'))
    tables = [t for t in ORDER if t in idx['tables']] + \
             [t for t in idx['tables'] if t not in ORDER]

    print(f'{"table":22s} {"files":>6s} {"done":>5s} {"rows":>6s} {"chars":>9s}  progress')
    gf = gd = 0
    next_file = None
    partial = []
    for t in tables:
        info = idx['tables'][t]
        files = sorted(glob.glob(os.path.join(BASE, 'work', t, '*.json')))
        done = 0
        for p in files:
            f, n = counts(p)
            if n and f == n:
                done += 1
            else:
                rel = os.path.relpath(p, BASE)
                if next_file is None:
                    next_file = (rel, f, n)
                if f:
                    partial.append((rel, f, n))
        gf += len(files); gd += done
        bar = '#' * int(20 * done / max(1, len(files)))
        pct = 100 * done // max(1, len(files))
        print(f'{t:22s} {len(files):6d} {done:5d} {info["total_rows"]:6d} '
              f'{info["total_source_chars"]:9d}  [{bar:<20}] {pct:3d}%')

    print(f'\n{"TOTAL":22s} {gf:6d} {gd:5d}   ->  {100 * gd // max(1, gf)}% of files complete')

    if partial:
        print('\nIN PROGRESS (started, not finished):')
        for rel, f, n in partial:
            print(f'  {rel}   {f}/{n} fields')

    print('\n' + '-' * 62)
    if next_file is None:
        print('ALL FILES COMPLETE.  Next:')
        print('  python3 scripts/verify.py')
        print('  python3 scripts/build.py <lang>')
    else:
        rel, f, n = next_file
        state = f'{f}/{n} fields done' if f else 'not started'
        print(f'START HERE:  {rel}   ({state})')
        print(f'  then:      python3 scripts/verify.py {rel}')
    print('-' * 62)


if __name__ == '__main__':
    main()
