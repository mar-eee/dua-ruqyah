#!/usr/bin/env python3
"""
Build the standard translation workspace from the English and Bengali databases.

Chunks are sized by *translatable character count*, not by row count, so every
work file is a comfortable single-pass unit. Rows that are larger than one
budget on their own are split at paragraph boundaries into ordered parts; a
paragraph is never split.

Run from the folder that holds dua_main_en.sqlite and dua_main_bn.sqlite:
    python3 translation_base/scripts/generate.py
"""
import json, os, re, sqlite3, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)
ROOT = os.path.dirname(BASE)

EN = os.path.join(ROOT, 'dua_main_en.sqlite')
BN = os.path.join(ROOT, 'dua_main_bn.sqlite')

# ---------------------------------------------------------------- settings --
BUDGET    = 6000   # translatable source characters per work file
MAX_ROWS  = 50     # never put more than this many rows in one file
PART_SIZE = 2000   # target size of one part when a big row is split

# Book tables are excluded by instruction.
EXCLUDE = {'books', 'book_details'}
# No translatable text at all.
NO_TEXT = {'ids', 'drawer_item_actions'}

# Which database is the source of truth for each table.
#   EN is the default (it is the more reliable translation source).
#   dua_infos and ruqyah_videos are BN: the English DB holds a *different*
#   dataset for these two, not a translation of the same rows.
SOURCE = {
    'categories': 'en', 'subcategories': 'en', 'sections': 'en',
    'dua_infos': 'bn',
    'duas': 'en',
    'ruqyah_categories': 'en', 'ruqyah_subcategories': 'en',
    'ruqyah_details': 'en', 'ruqyah_instants': 'en',
    'ruqyah_videos': 'bn',
    'drawer_items': 'bn',
}

TRANSLATE = {
    'categories': ['name'],
    'subcategories': ['name'],
    'sections': ['name'],
    'dua_infos': ['name', 'description'],
    'duas': ['name', 'content', 'translation', 'note'],
    'ruqyah_categories': ['name'],
    'ruqyah_subcategories': ['name'],
    'ruqyah_details': ['topic_name', 'text'],
    'ruqyah_instants': ['topic_name', 'name', 'content', 'translation'],
    'ruqyah_videos': ['name', 'author'],
    'drawer_items': ['title', 'hero_title1', 'hero_title2', 'content'],
}

# Fields copied through untouched. Everything not in TRANSLATE is frozen.
FROZEN_NOTE = [
    'id', 'groups', 'uthmani', 'indopak', 'clean', 'transliteration',
    'reference', 'audio', 'cat_id', 'subcat_id', 'topic_id', 'icon',
    'link', 'link_id', 'book_id', 'section_id', 'display_order',
    'created_at', 'updated_at', 'item_type', 'type', 'dua_count', 'subcat_count',
]

# Tables where the Bengali wording is the more accurate description and should
# be shown next to the English while translating. Restricted to tables where
# BN and EN are actually the same rows at the same id - verified by spot
# checking real content, not just row counts (which can coincidentally match
# while the rows are reordered or a different dataset; see below).
SHOW_BN = {'categories', 'subcategories', 'sections', 'ruqyah_instants', 'duas'}

# ruqyah_categories and ruqyah_subcategories are deliberately NOT in SHOW_BN.
# Their Bengali tables are a differently curated dataset, not a translation of
# the same rows: ruqyah_subcategories has 117 BN rows vs 163 EN rows, and
# ruqyah_categories has 15 rows in both but in a different order (e.g. EN id 6
# "About Raqi" lines up with BN id 10, and BN's icon "next_step" is reused
# across two unrelated EN rows). Joining these by id, as SHOW_BN does for
# every other table, silently shows the wrong Bengali sentence next to the
# right English one - worse than showing nothing, because it looks trustworthy.

# duas.groups is a JSON string holding whole nested dua records. Its inner
# name/content/translation/note are user-visible text, not metadata, so they
# have to be translated too. Shipping them untranslated is a real bug: the
# Japanese and Indonesian databases both carry Bengali here.
GROUP_FIELDS = ['name', 'content', 'translation', 'note']

# Longest prose field per table, used when a row must be split into parts.
SPLIT_FIELD = {'dua_infos': 'description', 'ruqyah_details': 'text',
               'duas': 'translation', 'ruqyah_instants': 'translation'}

# Row identity. `sections` is keyed on (id, book_id): it has 21 rows but only
# 12 distinct ids, so keying on id alone would silently merge rows.
KEY = {'sections': ('id', 'book_id')}


def keyof(table, row):
    return tuple(row[k] for k in KEY.get(table, ('id',)))


def rows_of(db, table):
    c = sqlite3.connect(db)
    c.row_factory = sqlite3.Row
    try:
        return [dict(r) for r in c.execute(f'select * from "{table}"')]
    except sqlite3.OperationalError:
        return []


def tsize(row, fields):
    return sum(len(row.get(f) or '') for f in fields if f in row)


def split_paragraphs(text, target=PART_SIZE):
    """Group paragraphs into parts of about `target` chars. Never splits a
    paragraph. Returns a list of strings that rejoin with '\\n\\n'."""
    paras = text.split('\n\n')
    parts, cur, n = [], [], 0
    for p in paras:
        if cur and n + len(p) + 2 > target:
            parts.append('\n\n'.join(cur)); cur, n = [], 0
        cur.append(p); n += len(p) + 2
    if cur:
        parts.append('\n\n'.join(cur))
    assert '\n\n'.join(parts) == text, 'paragraph split is not lossless'
    return parts


def group_items(groups):
    """duas.groups -> the translatable strings inside each nested record."""
    out = []
    for gi, rec in enumerate(json.loads(groups)):
        for f in GROUP_FIELDS:
            if rec.get(f):
                out.append({'group': gi, 'key': f, 'source': rec[f], 'target': ''})
    return out


def drawer_sections(content):
    """drawer_items.content is a JSON string. Expose only the human strings."""
    doc = json.loads(content)
    out = []
    for i, s in enumerate(doc.get('sections', [])):
        if s.get('type') == 'spacer':
            continue
        if s.get('type') == 'bullet':
            out.append({'index': i, 'key': 'header', 'source': s.get('header', ''), 'target': ''})
            out.append({'index': i, 'key': 'details', 'source': s.get('details', ''), 'target': ''})
        else:
            out.append({'index': i, 'key': 'text', 'source': s.get('text', ''), 'target': ''})
    return out


def build_units(table):
    """One unit = one work item: a whole row, or one part of a big row."""
    src = SOURCE[table]
    data = rows_of(EN if src == 'en' else BN, table)
    fields = TRANSLATE[table]
    # the other language, keyed the same way, for cross-reference
    other = {}
    if table in SHOW_BN:
        okey = KEY.get(table, ('id',))
        for r in rows_of(BN if src == 'en' else EN, table):
            other[tuple(r[k] for k in okey)] = r
    units = []
    for r in data:
        frozen = {k: v for k, v in r.items() if k not in fields}
        size = tsize(r, fields)

        if table == 'drawer_items':
            secs = drawer_sections(r['content'])
            head = {f: r.get(f) for f in fields if f != 'content'}
            # one unit per group of sections, plus the headline fields on part 1
            parts, cur, n = [], [], 0
            for s in secs:
                if cur and n + len(s['source']) > PART_SIZE:
                    parts.append(cur); cur, n = [], 0
                cur.append(s); n += len(s['source'])
            if cur:
                parts.append(cur)
            for pi, group in enumerate(parts, 1):
                u = {'key': list(keyof(table, r)), 'id': r['id'], 'part': pi,
                     'of': len(parts), 'frozen': frozen,
                     'source': {}, 'target': {}, 'content_sections': group}
                if pi == 1:
                    for f in head:
                        u['source'][f] = head[f]
                        u['target'][f] = '' if head[f] is not None else None
                u['size'] = sum(len(s['source']) for s in group) + tsize(r, list(head))
                units.append(u)
            continue

        gitems = group_items(r['groups']) if table == 'duas' and r.get('groups') else []
        ref = other.get(keyof(table, r))
        if size + sum(len(g['source']) for g in gitems) <= BUDGET:
            u = {
                'key': list(keyof(table, r)), 'id': r['id'], 'part': 1, 'of': 1, 'frozen': frozen,
                'source': {f: r.get(f) for f in fields},
                'target': {f: ('' if r.get(f) is not None else None) for f in fields},
                'size': size + sum(len(g['source']) for g in gitems),
            }
            if ref:
                u['reference_bn' if src == 'en' else 'reference_en'] = {
                    f: ref.get(f) for f in fields if ref.get(f)}
            if gitems:
                u['group_items'] = gitems
            units.append(u)
            continue

        # too big for one file: split the long prose field into parts
        big = SPLIT_FIELD.get(table)
        if not big or not r.get(big):
            big = max(fields, key=lambda f: len(r.get(f) or ''))
        chunks = split_paragraphs(r[big])
        others = {f: r.get(f) for f in fields if f != big}
        for pi, txt in enumerate(chunks, 1):
            u = {'key': list(keyof(table, r)), 'id': r['id'], 'part': pi,
                 'of': len(chunks), 'frozen': frozen,
                 'source': {big: txt}, 'target': {big: ''},
                 'size': len(txt), 'split_field': big}
            if pi == 1:
                for f, v in others.items():
                    u['source'][f] = v
                    u['target'][f] = '' if v is not None else None
                u['size'] += tsize(r, list(others))
            units.append(u)
    return units


def pack(units):
    files, cur, n, ids = [], [], 0, set()
    for u in units:
        if cur and (n + u['size'] > BUDGET or len(ids) >= MAX_ROWS):
            files.append(cur); cur, n, ids = [], 0, set()
        cur.append(u); n += u['size']; ids.add(tuple(u['key']))
    if cur:
        files.append(cur)
    return files


def main():
    for d in ('work', 'source', 'metadata'):
        shutil.rmtree(os.path.join(BASE, d), ignore_errors=True)

    index, totals = {}, {'files': 0, 'chars': 0, 'rows': 0}

    # read-only source dumps, so a translator can always see both languages
    for lang, db in (('en', EN), ('bn', BN)):
        for t in TRANSLATE:
            rows = rows_of(db, t)
            if not rows:
                continue
            p = os.path.join(BASE, 'source', lang)
            os.makedirs(p, exist_ok=True)
            with open(os.path.join(p, f'{t}.json'), 'w', encoding='utf-8') as f:
                json.dump(rows, f, ensure_ascii=False, indent=2)
                f.write('\n')

    for t in TRANSLATE:
        units = build_units(t)
        if not units:
            continue
        files = pack(units)
        outdir = os.path.join(BASE, 'work', t)
        os.makedirs(outdir, exist_ok=True)
        entries = []
        for i, group in enumerate(files, 1):
            name = f'{t}_{i:03d}.json'
            ids = sorted({u['id'] for u in group})
            nkeys = len({tuple(u['key']) for u in group})
            doc = {
                'table': t,
                'chunk': name,
                'source_language': SOURCE[t],
                'target_language': 'TARGET',
                'status': 'pending',
                'rows': nkeys,
                'id_range': f'{ids[0]}-{ids[-1]}',
                'source_chars': sum(u['size'] for u in group),
                'items': [{k: v for k, v in u.items() if k != 'size'} for u in group],
            }
            with open(os.path.join(outdir, name), 'w', encoding='utf-8') as f:
                json.dump(doc, f, ensure_ascii=False, indent=2)
                f.write('\n')
            entries.append({'file': f'work/{t}/{name}', 'rows': nkeys,
                            'id_range': doc['id_range'],
                            'source_chars': doc['source_chars'],
                            'items': len(group), 'status': 'pending'})
            totals['files'] += 1
            totals['chars'] += doc['source_chars']
        totals['rows'] += len({tuple(u['key']) for u in units})
        index[t] = {'source': SOURCE[t], 'translate_fields': TRANSLATE[t],
                    'key_fields': list(KEY.get(t, ('id',))),
                    'total_rows': len({tuple(u['key']) for u in units}),
                    'total_source_chars': sum(u['size'] for u in units),
                    'files': entries}

    os.makedirs(os.path.join(BASE, 'metadata'), exist_ok=True)
    with open(os.path.join(BASE, 'metadata', 'chunk_index.json'), 'w', encoding='utf-8') as f:
        json.dump({'budget_chars': BUDGET, 'max_rows_per_file': MAX_ROWS,
                   'part_size_chars': PART_SIZE,
                   'excluded_tables': sorted(EXCLUDE),
                   'tables_without_text': sorted(NO_TEXT),
                   'frozen_fields': FROZEN_NOTE,
                   'totals': totals, 'tables': index}, f, ensure_ascii=False, indent=2)
        f.write('\n')

    # schema, so the build script can recreate the database exactly
    schema = {}
    for lang, db in (('en', EN), ('bn', BN)):
        c = sqlite3.connect(db)
        schema[lang] = {
            'tables': {r[0]: r[1] for r in
                       c.execute("select name,sql from sqlite_master where type='table' and name not like 'sqlite_%'")},
            'indexes': [r[0] for r in
                        c.execute("select sql from sqlite_master where type='index' and sql is not null")],
        }
    with open(os.path.join(BASE, 'metadata', 'schema.json'), 'w', encoding='utf-8') as f:
        json.dump(schema, f, ensure_ascii=False, indent=2)
        f.write('\n')

    print(f"work files : {totals['files']}")
    print(f"rows       : {totals['rows']}")
    print(f"source chars: {totals['chars']}")
    for t, v in index.items():
        print(f"  {t:22s} {len(v['files']):4d} files  {v['total_rows']:5d} rows  {v['total_source_chars']:8d} chars  src={v['source']}")


if __name__ == '__main__':
    main()
