#!/usr/bin/env python3
"""
Build the translated SQLite database from work/.

    python3 translation_base/scripts/build.py <lang> [--partial]

<lang> is a short code used for the output file name, e.g.  ur  ->  dua_main_ur.sqlite

The source database is copied first, so every table, index and frozen field is
preserved exactly; only translated fields are overwritten. Rows that have not
been translated yet keep their source text unless --partial is given, in which
case the build stops and reports what is missing.
"""
import json, os, sqlite3, shutil, sys, glob, collections

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)
ROOT = os.path.dirname(BASE)

def load_index():
    with open(os.path.join(BASE, 'metadata', 'chunk_index.json'), encoding='utf-8') as f:
        return json.load(f)

def main():
    if len(sys.argv) < 2:
        sys.exit('usage: build.py <lang-code> [--partial]')
    lang = sys.argv[1]
    partial = '--partial' in sys.argv
    idx = load_index()

    out = os.path.join(ROOT, f'dua_main_{lang}.sqlite')
    # the English DB carries the fuller ruqyah section; it is the structural base
    shutil.copyfile(os.path.join(ROOT, 'dua_main_en.sqlite'), out)
    db = sqlite3.connect(out)

    # tables whose source is Bengali must be replaced wholesale, because the
    # English DB holds a different set of rows for them
    for table, info in idx['tables'].items():
        if info['source'] != 'bn':
            continue
        src = sqlite3.connect(os.path.join(ROOT, 'dua_main_bn.sqlite'))
        src.row_factory = sqlite3.Row
        rows = [dict(r) for r in src.execute(f'select * from "{table}"')]
        cols = [r[1] for r in db.execute(f'PRAGMA table_info("{table}")')]
        db.execute(f'delete from "{table}"')
        db.executemany(
            f'insert into "{table}" ({",".join(chr(34)+c+chr(34) for c in cols)}) '
            f'values ({",".join("?" * len(cols))})',
            [tuple(r.get(c) for c in cols) for r in rows])
    db.commit()

    missing = []
    # (table, key) -> {field: {part: text}}
    acc = collections.defaultdict(lambda: collections.defaultdict(dict))
    sections = collections.defaultdict(dict)   # (table,key) -> {(idx,key): text}

    for table, info in idx['tables'].items():
        keyf = info.get('key_fields', ['id'])
        for path in sorted(glob.glob(os.path.join(BASE, 'work', table, '*.json'))):
            doc = json.load(open(path, encoding='utf-8'))
            for it in doc['items']:
                k = (table, tuple(it['key']))
                for field, tgt in it.get('target', {}).items():
                    if tgt is None:
                        acc[k][field][it['part']] = None
                        continue
                    if not str(tgt).strip():
                        missing.append((path, it['id'], it['part'], field))
                        src = it['source'].get(field)
                        acc[k][field][it['part']] = src
                    else:
                        acc[k][field][it['part']] = tgt
                for s in it.get('content_sections', []):
                    t = s.get('target', '')
                    if s['source'] and not str(t).strip():
                        missing.append((path, it['id'], it['part'], f"content[{s['index']}].{s['key']}"))
                        t = s['source']
                    sections[k][(s['index'], s['key'])] = t

    if missing and not partial:
        print(f'{len(missing)} untranslated item(s). Showing first 15:')
        for m in missing[:15]:
            print(f'  {os.path.relpath(m[0], BASE)}  id={m[1]} part={m[2]} field={m[3]}')
        print('\nRun again with --partial to build anyway (untranslated text stays in the source language).')
        sys.exit(1)

    updated = 0
    for (table, key), fields in acc.items():
        info = idx['tables'][table]
        keyf = info.get('key_fields', ['id'])
        where = ' and '.join(f'"{k}"=?' for k in keyf)
        sets, vals = [], []
        for field, parts in fields.items():
            if all(v is None for v in parts.values()):
                value = None
            else:
                value = '\n\n'.join(parts[p] for p in sorted(parts) if parts[p] is not None)
            sets.append(f'"{field}"=?'); vals.append(value)
        if table == 'drawer_items' and sections.get((table, key)):
            row = db.execute(f'select content from drawer_items where {where}', key).fetchone()
            doc = json.loads(row[0])
            for (i, sk), text in sections[(table, key)].items():
                doc['sections'][i][sk] = text
            sets.append('"content"=?'); vals.append(json.dumps(doc, ensure_ascii=False))
        if not sets:
            continue
        db.execute(f'update "{table}" set {", ".join(sets)} where {where}', vals + list(key))
        updated += 1
    db.commit()

    ok = db.execute('PRAGMA integrity_check').fetchone()[0]
    print(f'wrote {out}')
    print(f'rows updated    : {updated}')
    print(f'untranslated    : {len(missing)}')
    print(f'integrity_check : {ok}')
    if ok != 'ok':
        sys.exit(1)

if __name__ == '__main__':
    main()
