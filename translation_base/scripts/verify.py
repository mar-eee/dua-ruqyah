#!/usr/bin/env python3
"""
Check translated work files before building.

    python3 translation_base/scripts/verify.py            # all files
    python3 translation_base/scripts/verify.py duas       # one table
    python3 translation_base/scripts/verify.py work/duas/duas_003.json

Every check here exists because it caught a real defect in an earlier
translation. Read CHECKS below before removing any of them.
"""
import json, os, re, sys, glob, collections

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)

BENGALI = re.compile(r'[ঀ-৿]')
ARABIC  = re.compile(r'[؀-ۿݐ-ݿﭐ-﷿ﹰ-﻿]')
TAG     = re.compile(r'</?(?:ar1?|b|i|u|br|p)\s*/?>')
NUMBER  = re.compile(r'\d+')
LATIN_W = re.compile(r'(?<![A-Za-z])[A-Za-z]{4,}')

# Patterns that were real machine-translation corruptions. See PLAN.md.
CORRUPTION = [
    ('hadith number turned into a date',  re.compile(r'\d{3,4}\s*年\s*\d{1,2}\s*月')),
    ('verse/page number turned into an age', re.compile(r'[：:]\s?\d+\s*歳')),
    ('Biblical Psalms instead of a surah', re.compile(r'詩篇')),
]


def load_glossary():
    p = os.path.join(BASE, 'GLOSSARY.json')
    if not os.path.exists(p):
        return {}, {}
    with open(p, encoding='utf-8') as f:
        g = json.load(f)
    canonical = {k: v for k, v in g.get('canonical', {}).items() if v}
    return canonical, g.get('watch_variants', {})


def files_for(arg):
    if arg and arg.endswith('.json'):
        return [arg if os.path.isabs(arg) else os.path.join(BASE, arg)]
    pat = os.path.join(BASE, 'work', arg or '*', '*.json')
    return sorted(glob.glob(pat))


def check_pair(where, src, tgt, problems):
    """Checks that compare one source string against its translation."""
    if src is None or tgt is None:
        if (src is None) != (tgt is None):
            problems.append((where, 'null rule', 'source and target must both be null or both be text'))
        return
    if not str(tgt).strip():
        problems.append((where, 'untranslated', 'target is empty'))
        return
    if BENGALI.search(tgt):
        problems.append((where, 'bengali left in target', tgt[:60]))
    # structural markup must survive
    if TAG.findall(src) != TAG.findall(tgt):
        problems.append((where, 'html tags changed',
                         f'source={TAG.findall(src)} target={TAG.findall(tgt)}'))
    # Arabic passages inside prose must be copied through untouched
    sa, ta = ARABIC.findall(src), ARABIC.findall(tgt)
    if len(sa) > 20 and len(ta) < len(sa) * 0.8:
        problems.append((where, 'arabic text lost', f'{len(sa)} arabic chars in source, {len(ta)} in target'))
    # digits carry hadith / verse / volume numbers
    sn, tn = NUMBER.findall(src), NUMBER.findall(tgt)
    if collections.Counter(sn) != collections.Counter(tn):
        lost = collections.Counter(sn) - collections.Counter(tn)
        added = collections.Counter(tn) - collections.Counter(sn)
        if lost or added:
            problems.append((where, 'numbers changed',
                             f'missing={dict(lost)} added={dict(added)}'))
    for label, rx in CORRUPTION:
        if rx.search(tgt):
            problems.append((where, label, rx.search(tgt).group()))


def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    canonical, watch = load_glossary()
    problems, seen_terms = [], collections.defaultdict(collections.Counter)
    n_files = n_items = n_done = 0

    for path in files_for(arg):
        n_files += 1
        rel = os.path.relpath(path, BASE)
        try:
            doc = json.load(open(path, encoding='utf-8'))
        except Exception as e:
            problems.append((rel, 'invalid json', str(e)))
            continue
        parts = collections.defaultdict(set)
        for it in doc['items']:
            n_items += 1
            tag = f"{rel} id={it['id']} part={it['part']}/{it['of']}"
            parts[tuple(it['key'])].add((it['part'], it['of']))
            if set(it['source']) != set(it['target']):
                problems.append((tag, 'field set changed',
                                 f"source={sorted(it['source'])} target={sorted(it['target'])}"))
            for f in it['source']:
                check_pair(f'{tag} .{f}', it['source'][f], it['target'].get(f), problems)
                t = it['target'].get(f)
                if t:
                    n_done += 1
                    src_text = it['source'][f] or ''
                    for term, want in canonical.items():
                        if re.search(r'(?<![A-Za-z])' + re.escape(term) + r'(?![A-Za-z])',
                                     src_text, re.I) and want not in t:
                            problems.append((f'{tag} .{f}', 'glossary term not used',
                                             f'source mentions "{term}" so target should contain "{want}"'))
                    for label, variants in watch.items():
                        for v in variants:
                            if v in t:
                                seen_terms[label][v] += t.count(v)
            for s in it.get('content_sections', []):
                if s['source']:
                    check_pair(f"{tag} content[{s['index']}].{s['key']}",
                               s['source'], s.get('target'), problems)

    # a term must be rendered one way across the whole workspace
    for term, variants in seen_terms.items():
        if len(variants) > 1:
            best = variants.most_common(1)[0][0]
            others = {k: v for k, v in variants.items() if k != best}
            problems.append(('GLOSSARY', f'inconsistent term "{term}"',
                             f'used {dict(variants)} - pick one (most common: {best})'))

    print(f'files {n_files}   items {n_items}   translated fields {n_done}')
    if not problems:
        print('OK - no problems found')
        return 0
    bucket = collections.Counter(p[1] for p in problems)
    print(f'\n{len(problems)} problem(s):')
    for k, v in bucket.most_common():
        print(f'  {v:5d}  {k}')
    print('\nfirst 25:')
    for w, k, d in problems[:25]:
        print(f'  [{k}] {w}\n         {d}')
    return 1


if __name__ == '__main__':
    sys.exit(main())
