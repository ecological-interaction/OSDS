"""Read-only OSDS documentary checks; no scientific, rights or MSP certification."""
import argparse
from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MACHINE = 'OSDS_Machine_Reference.md'
SCIENTIFIC = 'OSDS_Scientific_Reference_Register.md'
REVISION = '2026-11-02-documentary'
FENCE = re.compile(r'^```json[ \t]*\n(.*?)^```[ \t]*$', re.M | re.S)
HEADINGS = re.compile(r'^(#{1,6})[ \t]+(.+?)[ \t]*$', re.M)
ALLOWED_MANIFEST_ADDITIONS = {'current_methodological_context', 'maintenance'}
DOCUMENTS = {'README.md', MACHINE, SCIENTIFIC, 'RESEARCH_NOTES.md',
             'CHANGELOG.md', 'CITATION.cff', 'AGENTS.md'}


def strict_json(text):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError('Duplicate JSON key: ' + key)
            result[key] = value
        return result
    def invalid(value):
        raise ValueError('Non-JSON constant: ' + value)
    return json.loads(text, object_pairs_hook=unique, parse_constant=invalid)


def blocks(text):
    matches = list(FENCE.finditer(text))
    if len(matches) != len(re.findall(r'^```json[ \t]*$', text, re.M)):
        raise ValueError('Malformed or unclosed JSON fence.')
    parsed = [(strict_json(m[1]), m[1]) for m in matches]
    if any(not isinstance(obj, dict) for obj, _ in parsed):
        raise ValueError('Every JSON fence must contain an object.')
    manifests = [obj for obj, _ in parsed if obj.get('block_type') == 'manifest']
    if len(manifests) != 1:
        raise ValueError('Expected exactly one manifest.')
    manifest = manifests[0]
    expected = {'manifest': 1, 'source_record': 62}
    if manifest.get('research_profile'):
        if manifest['research_profile'].get('schema') != 'osds.documentary-research/0.1.0':
            raise ValueError('Unsupported declared research profile.')
        expected['documentary_research'] = 1
    if Counter(obj.get('block_type') for obj, _ in parsed) != expected:
        raise ValueError('Expected 62 original source_record fences and exactly the declared profile blocks.')
    records = [obj for obj, _ in parsed if obj['block_type'] == 'source_record']
    return manifest, records, parsed


def heading_targets(text):
    """GitHub-style duplicate heading suffixes in document order, plus explicit IDs."""
    result, used = [], set()
    # Fenced data/code must not create Markdown headings or links.
    visible = re.sub(r'^```[^\n]*\n.*?^```[ \t]*$', '', text, flags=re.M | re.S)
    for match in HEADINGS.finditer(visible):
        label = match[2]
        plain = re.sub(r'\[([^]]+)\]\([^)]+\)', r'\1', label).replace('`', '')
        base = re.sub(r'[^\w -]', '', plain.lower()).replace(' ', '-')
        anchor, suffix = base, 0
        while anchor in used:
            suffix += 1
            anchor = f'{base}-{suffix}'
        used.add(anchor)
        result.append((len(match[1]), label, anchor))
    explicit = re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)["\']', visible)
    return result, explicit, visible


def observation_description(categories, phrases):
    words = [phrases[c] for c in categories]
    text = words[0] if len(words) == 1 else ' and '.join(words) if len(words) == 2 else ', '.join(words[:-1]) + ', and ' + words[-1]
    return text[0].upper() + text[1:] + '.'


def source_tables(text):
    """Read the four-column tables within their exact disciplinary headings."""
    result, domains, key = [], [], []
    domain, table = None, None
    for line in text.splitlines():
        heading = re.fullmatch(r'### (D\d{2}) — (.+)', line)
        if heading:
            domain = heading.groups()
            domains.append(domain)
            table = None
        elif line.startswith('#'):
            domain, table = None, None
        if not line.startswith('|'):
            if line.strip():
                table = None
            continue
        cells = [x.strip() for x in line.strip().strip('|').split('|')]
        if cells == ['OSDS ID', 'Source', 'Coverage as supplied', 'Observation description']:
            if domain is None:
                raise ValueError('Source table outside its disciplinary domain.')
            table = 'sources'
        elif cells == ['Code', 'Observation category']:
            table = 'key'
        elif all(re.fullmatch(r':?-+:?', c) for c in cells):
            continue
        elif table == 'sources':
            if len(cells) != 4:
                raise ValueError('Source tables must have exactly four columns.')
            result.append((domain, cells))
        elif table == 'key':
            key.append(cells)
        else:
            raise ValueError('Unexpected table columns or unrecognised scientific table.')
    return domains, result, key


def canonical(value):
    # No coercion: null/bool/number/string and array order remain distinguishable.
    return json.dumps(value, ensure_ascii=False, separators=(',', ':'))


def research_tools():
    spec = importlib.util.spec_from_file_location('osds_research_profile', Path(__file__).with_name('osds_research.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def source_human(text):
    return text.split('<!-- BEGIN GENERATED OSDS RESEARCH -->', 1)[0]


def check_preservation(root, baseline, manifest, records, parsed, require):
    old_text = (baseline / MACHINE).read_text()
    old_manifest, old_records, old_parsed = blocks(old_text)
    require(canonical(records) == canonical(old_records), 'Preservation: source-record values/types/order changed.')
    require([raw for obj, raw in parsed if obj['block_type'] == 'source_record'] ==
            [raw for obj, raw in old_parsed if obj['block_type'] == 'source_record'],
            'Preservation: source-record JSON fence bytes changed.')
    research = bool(manifest.get('research_profile'))
    additions = ALLOWED_MANIFEST_ADDITIONS | ({'research_profile'} if research else set())
    changes = {'document_version', 'updated', 'change_history'} if research else set()
    for key in set(manifest) | set(old_manifest):
        if key not in additions | changes:
            require(key in manifest and key in old_manifest and canonical(manifest[key]) == canonical(old_manifest[key]),
                    'Preservation: non-allowlisted manifest field changed: ' + key)
    require(set(manifest) - set(old_manifest) <= additions, 'Preservation: unexpected new manifest field.')
    # Stage B metadata is retained byte-for-value; new profile does not erase that history.
    for key in ALLOWED_MANIFEST_ADDITIONS & set(old_manifest):
        require(canonical(manifest[key]) == canonical(old_manifest[key]), 'Preservation: earlier maintenance metadata changed.')
    if research:
        require(manifest['document_version'] == '0.2.0' and manifest['updated'] == '2026-11-03', 'Wrong research document transition.')
        old_history = old_manifest['change_history']
        if manifest['change_history'] != old_history:
            require(manifest['change_history'][:-1] == old_history and len(manifest['change_history']) == len(old_history)+1 and
                    manifest['change_history'][-1] == {'version':'0.2.0','date':'2026-11-03','change':'Added one versioned candidate documentary research block from complementary pinned A01/A02 audits; original 62 source objects, classifications, memberships, provenance, URLs and candidate questions unchanged. No scientific verification, resource release or protocol adoption.'},
                    'Preservation: historical change entries rewritten or invalid new entry.')
    # Permitted keys are checked for exact documentary purpose in check(), never ignored wholesale.
    old_human = (baseline / SCIENTIFIC).read_text()
    table_lines = lambda t: [line for line in source_human(t).splitlines() if line.startswith('|')]
    require(table_lines((root / SCIENTIFIC).read_text()) == table_lines(old_human),
            'Preservation: Scientific table structure/rows/category key changed.')
    require(re.findall(r'<a id="(src-[0-9]{3})"></a>', (root / MACHINE).read_text()) ==
            re.findall(r'<a id="(src-[0-9]{3})"></a>', old_text), 'Preservation: original machine anchors changed.')
    allowed = DOCUMENTS | {'scripts/validate_osds.py'}
    if research:
        allowed |= {'OSDS_Research.schema.json', 'scripts/osds_research.py', 'scripts/render_osds_research.py', 'tests/test_osds_research.py'}
    old_files = {p.relative_to(baseline) for p in baseline.rglob('*') if p.is_file() and '.git' not in p.relative_to(baseline).parts}
    current = {p.relative_to(root) for p in root.rglob('*') if p.is_file() and '.git' not in p.relative_to(root).parts and '__pycache__' not in p.relative_to(root).parts}
    require(not (old_files - current), 'Preservation: baseline files removed.')
    for path in old_files:
        if str(path) not in allowed:
            require((root / path).is_file() and (root / path).read_bytes() == (baseline / path).read_bytes(),
                    'Preservation: unrelated file changed: ' + str(path))
    require(all(str(p) in allowed for p in current - old_files), 'Preservation: unexpected new files.')


def check(root=ROOT, baseline=None, evidence_dir=None, ledger_path=None, profile=None):
    root = root.resolve()
    baseline = baseline.resolve() if baseline else None
    errors = []
    def require(condition, message):
        if not condition:
            errors.append(message)
    text = (root / MACHINE).read_text()
    manifest, records, parsed = blocks(text)
    research = next((obj for obj, _ in parsed if obj['block_type'] == 'documentary_research'), None)
    require(profile in (None, 'research-0.1' if research else 'source-0.1'), 'Requested profile differs from declared document profile.')
    ids = [r['id'] for r in records]
    require(len(set(ids)) == 62 and set(ids) == {f'SRC-{i:03}' for i in range(1, 63)}, 'Duplicate/missing source IDs.')
    qualified = [r['qualified_id'] for r in records]
    require(len(set(qualified)) == 62 and all(r['qualified_id'] == 'OSDS:' + r['id'] for r in records), 'Duplicate/incorrect qualified IDs.')
    require(manifest['document_version'] == ('0.2.0' if research else '0.1.2') and manifest['schema'] == 'osds.reference-register/0.1-draft' and
            manifest['classification_reference'] == 'osds.inventory-classification/0.1', 'Version/schema/classification identity changed.')
    require(manifest['record_count'] == len(records) == 62 and manifest['verified_record_count'] == 0,
            'Manifest/actual record count mismatch.')
    require(manifest['working_name'] == 'Observational Systems and Data Sources', 'Incorrect project name.')
    domains, categories = manifest['domains'], manifest['observation_categories']
    domain_ids, category_ids = [x['id'] for x in domains], [x['id'] for x in categories]
    require(domain_ids == [f'D{i:02}' for i in range(1, 9)] and category_ids == [f'O{i:02}' for i in range(1, 9)], 'Expected eight unique domains and eight categories.')
    require(all(x['qualified_id'] == 'OSDS:' + x['id'] for x in domains + categories), 'Incorrect qualified classification IDs.')
    require(all(r['classification_reference'] == manifest['classification_reference'] for r in records), 'Record classification reference mismatch.')
    primary = Counter(r['domain'] for r in records)
    secondary = Counter(c for r in records for c in r['related_domains'])
    observations = Counter(c for r in records for c in r['observation_categories'])
    require(set(primary) <= set(domain_ids) and set(secondary) <= set(domain_ids) and set(observations) <= set(category_ids), 'Unresolved classification membership.')
    require((sum(primary.values()), sum(secondary.values()), sum(observations.values())) == (62, 0, 158), 'Membership counts differ from 62 primary / zero secondary / 158 category (220 total).')
    require(all(len(r['related_domains']) == len(set(r['related_domains'])) and
                len(r['observation_categories']) == len(set(r['observation_categories'])) and r['observation_categories'] for r in records), 'Repeated/empty memberships.')
    require(all(primary[x['id']] == x['record_count'] for x in domains) and
            all(observations[x['id']] == x['record_count'] for x in categories), 'Classification per-group count mismatch.')
    prov_ids = [p['id'] for p in manifest['provenance']]
    require(len(set(prov_ids)) == len(prov_ids) == 3 and set(prov_ids) == {'P01', 'P02', 'P03'}, 'Duplicate/missing provenance entries.')
    require(next(p for p in manifest['provenance'] if p['id'] == 'P01')['conversation_id'] is None, 'Historical conversation identifier must remain null.')
    relationships = [(r, rel) for r in records for rel in r['candidate_relationships']]
    require(len(relationships) == 8, 'Expected eight directed candidate relationships.')
    for r in records:
        require(r['record_status'] == 'candidate' and r['verification']['status'] == 'not_verified', 'Candidate/verification status changed: ' + r['id'])
        require(r['provenance']['source_id'] in prov_ids and r['provenance']['url_enrichment_source_id'] in prov_ids and
                r['provenance']['inventory_domain_heading'] == r['domain'], 'Unresolved provenance: ' + r['id'])
        require(len(r['source_urls']) == 1 and bool(r['source_urls'][0]['url']), 'Missing/ambiguous recorded discovery URL: ' + r['id'])
    require(manifest['records_with_source_urls'] == sum(bool(r['source_urls']) for r in records), 'Discovery-URL count mismatch.')
    for r, rel in relationships:
        require(set(rel) == {'target_id', 'relation', 'status'} and rel['target_id'] in qualified and
                rel['relation'] in {'possible_same_repository', 'possible_same_provider', 'possible_portal_overlap', 'possible_parent_or_collection_overlap'} and
                rel['status'] == 'editorial_review_question_unverified', 'Invalid typed candidate relationship: ' + r['id'])
    _, anchors, _ = heading_targets(text)
    require(Counter(a for a in anchors if re.fullmatch(r'src-[0-9]{3}', a)) == Counter(i.lower() for i in ids), 'Missing/duplicate/wrong machine-record anchors.')
    # Associate each explicit anchor with its actual following source fence, not merely an existing ID elsewhere.
    source_matches = [m for m in FENCE.finditer(text) if strict_json(m[1])['block_type'] == 'source_record']
    last_end = 0
    for record, match in zip(records, source_matches):
        local = re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)["\']', text[last_end:match.start()])
        require(local == [record['id'].lower()], 'Anchor does not precede matching machine record: ' + record['id'])
        last_end = match.end()
    human = (root / SCIENTIFIC).read_text()
    human_domains, rows, key = source_tables(source_human(human))
    require(human.count('| OSDS ID | Source | Coverage as supplied | Observation description |') == 8, 'Expected one four-column source table per domain.')
    require(human.index('| Code | Observation category |') < human.index('### D01 — Environmental'), 'Category key must precede the domain inventory.')
    require('Version ' + manifest['document_version'] in text.split('## Interpretation and conventions')[0], 'Machine subtitle version differs from manifest.')
    require(human_domains == [(x['id'], x['label']) for x in domains], 'Scientific domain order/labels mismatch.')
    require(key == [[x['id'], x['label']] for x in categories], 'Scientific O01–O08 category key differs or is missing.')
    require(len(rows) == len(records), 'Scientific/Machine record count mismatch.')
    for (domain, cells), record in zip(rows, records):
        expected = [f"[{record['id']}]({MACHINE}#{record['id'].lower()})",
                    f"[{record['name']}]({record['source_urls'][0]['url']})", record['coverage_as_supplied'],
                    observation_description(record['observation_categories'], manifest['presentation']['category_display_phrases'])]
        require(domain[0] == record['domain'] and cells == expected, 'Scientific/Machine identity/name/URL/coverage/description/domain mismatch: ' + record['id'])
    targets, _, _ = heading_targets(human)
    for d in domains:
        target = [slug for level, label, slug in targets if level == 3 and label == d['id'] + ' — ' + d['label']]
        require(len(target) == 1 and f"[{d['id']} — {d['label']}](#{target[0]})" in human, 'Domain navigation does not target intended heading: ' + d['id'])
    context = manifest.get('current_methodological_context', {})
    require(context == {'name': 'Database Reference Methodology', 'candidate': 'DRM-MSP 0.1.0', 'review_revision': 2,
            'status': 'unadopted_methodological_candidate', 'as_of': '2026-11-02',
            'phase_4': 'Bounded documentary-preservation pilots completed and closed.',
            'limitations': 'Not scientific verification, general MSP adoption or release, full DRM conformance, or authorisation for Phase 5.',
            'historical_evidence': 'The existing methodology object and provenance entries retain their historical assertions and locators; this context does not replace them.'}, 'Unexpected current-methodology metadata or authority claim.')
    require(manifest.get('maintenance') == {'revision': REVISION, 'date': '2026-11-02',
            'scope': 'Documentary and methodological context only; source records, classifications, provenance and scientific assertions unchanged.'}, 'Unexpected documentary maintenance metadata.')
    for name in ['README.md', SCIENTIFIC, 'RESEARCH_NOTES.md']:
        content = (root / name).read_text()
        require((('0.2.0' in content) if research else ('0.1.2' in content and REVISION in content)), 'Document version/maintenance reference missing: ' + name)
    # Cache each document's targets once; duplicate suffixes remain document-local.
    documents = {p.resolve(): heading_targets(p.read_text()) for p in root.rglob('*.md')
                 if '.git' not in p.relative_to(root).parts}
    for path, (_, _, visible) in documents.items():
        for link in re.findall(r'\]\(([^)]+)\)', visible):
            u = urlsplit(link)
            if u.scheme or u.netloc:
                continue
            destination = (path.parent / unquote(u.path)).resolve() if u.path else path.resolve()
            require(destination == root.resolve() or root.resolve() in destination.parents, 'Local link leaves repository: ' + link)
            require(destination.is_file(), 'Missing local link: ' + str(path.relative_to(root)) + ': ' + link)
            if u.fragment and destination.is_file() and destination.suffix == '.md':
                hs, explicit, _ = documents[destination]
                require(unquote(u.fragment) in {a for _, _, a in hs} | set(explicit), 'Missing local anchor: ' + link)
    if research:
        research_tools().check_research(root, manifest, research, require, evidence_dir, ledger_path, records)
    if baseline:
        check_preservation(root, baseline, manifest, records, parsed, require)
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline', type=Path, help='Preserved before-change repository directory; never rewritten.')
    parser.add_argument('--profile', choices=['source-0.1', 'research-0.1'], help='Explicitly select the declared profile; default uses the manifest declaration.')
    parser.add_argument('--evidence-dir', type=Path, help='Read pinned A01/A02 audit filenames here; never modified.')
    parser.add_argument('--ledger', type=Path, help='Private reconciliation ledger; require --evidence-dir for source-slice checking.')
    args = parser.parse_args()
    if args.ledger and not args.evidence_dir:
        parser.error('--ledger requires --evidence-dir')
    try:
        errors = check(ROOT, args.baseline, args.evidence_dir, args.ledger, args.profile)
    except (OSError, ValueError, KeyError, TypeError, IndexError, AttributeError) as exc:
        print('Input/check failure: ' + str(exc), file=sys.stderr)
        return 2
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    manifest, _, parsed = blocks((ROOT / MACHINE).read_text())
    print(f'PASS: {len(parsed)} JSON fences; 62 original candidate sources; eight domains/categories; 220 original memberships; eight directed source questions.')
    if manifest.get('research_profile'):
        print('PASS: research profile identities/statuses, source fields, candidate relationships, alias continuity and deterministic Scientific/README presentation.')
        try:
            from jsonschema import Draft202012Validator
        except ImportError:
            print('Optional full research JSON Schema validation not run: jsonschema is not installed.')
        else:
            schema = json.loads((ROOT / 'OSDS_Research.schema.json').read_text())
            Draft202012Validator.check_schema(schema)
            data = next(obj for obj, _ in parsed if obj['block_type']=='documentary_research')
            failures = list(Draft202012Validator(schema).iter_errors(data))
            if failures:
                for failure in failures:
                    print('Research JSON Schema: '+failure.message, file=sys.stderr)
                return 1
            print('PASS: full Draft 2020-12 research schema and instance (not original source schema).')
    print('PASS: IDs, provenance, record anchors, four-column Scientific parity, category key, intended domain navigation and local links.')
    if args.baseline:
        print('PASS: source-record objects/raw JSON, existing manifest fields/provenance, Scientific tables and unrelated files match the baseline; only explicit version/profile metadata transitions allowed.')
    print('Scope: structural/documentary checks only; not scientific validity, rights, complete source recovery or MSP conformance. No files rewritten.')
    print('Original source full JSON Schema validation not performed: its draft identity has no executable schema.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
