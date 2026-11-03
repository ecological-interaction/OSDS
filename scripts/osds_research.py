"""Bounded checks for OSDS's candidate research profile, not ingestion infrastructure."""
from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path
import re

PROFILE = 'osds.documentary-research/0.1.0'
PINS = {'OSDS:EVD-0001': ('20261103_OSDS_a01.md', '3ccfde241f06e9a8d329e679e6369f52a3319b6cab0a7d7bd5ada8bdad3d43a0', 596),
        'OSDS:EVD-0002': ('20261103_OSDS_a02.md', '36c2add69e3656632abaa1d6dc1f5669524eacefa546103fe25a8b797a6588b1', 312)}
STATES = {'documentary_inclusion': 'candidate_documentary', 'canonical_research_status': 'candidate',
          'identity_verification': 'unverified', 'scientific_verification': 'not_independently_verified',
          'reported_authority': 'audit_reported_or_author_analysis', 'authority_evidence': 'original_scientific_turns_unavailable',
          'relationship_review': 'proposed', 'access': 'not_assessed', 'rights': 'unknown'}


def renderer():
    spec = importlib.util.spec_from_file_location('osds_research_renderer', Path(__file__).with_name('render_osds_research.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def canonical(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':'))


def section(text, start, end):
    if text.count(start) != 1 or text.count(end) != 1:
        raise ValueError('Missing/duplicate generated research markers.')
    return start + text.split(start, 1)[1].split(end, 1)[0] + end + '\n'


def check_research(root, manifest, research, require, evidence_dir=None, ledger_path=None, records=None):
    require(research.get('schema') == PROFILE and research.get('document_version') == '0.2.0' and
            research.get('status') == 'candidate_documentary_research', 'Wrong research profile/version/status.')
    entries = research['concepts'] + research['assertions']
    origins = research['origins']
    ids = [x['id'] for x in entries + origins + research['evidence_editions']]
    require(len(ids) == len(set(ids)), 'Duplicate research IDs.')
    for collection,prefix in [('concepts','RC'),('assertions','RA'),('origins','OR'),('evidence_editions','EVD')]:
        require(all(re.fullmatch('OSDS:'+prefix+r'-[0-9]{4}', x['id']) for x in research[collection]), 'Malformed local research ID.')
    byid = {x['id']: x for x in entries}
    byorigin = {x['id']: x for x in origins}
    editions = {x['id']:x for x in research['evidence_editions']}
    require(set(editions) == set(PINS), 'Evidence-edition set changed.')
    source_lines = {}
    require(manifest['research_profile'].get('schema') == PROFILE and manifest['research_profile'].get('schema_file') == 'OSDS_Research.schema.json' and manifest['research_profile'].get('block_type') == 'documentary_research' and manifest['research_profile'].get('source_records_unchanged') == 62, 'Unexpected manifest research declaration.')
    for ident,(filename,pin,count) in PINS.items():
        e = editions.get(ident,{})
        require((e.get('source_file'),e.get('sha256'),e.get('line_count')) == (filename,pin,count), 'Wrong source edition/hash: '+ident)
        require(e.get('authority') == 'secondary_documentary_audit_not_authenticated_original_transcript' and e.get('rights') == 'not_assessed_for_redistribution', 'Unsupported evidence authority/rights upgrade.')
        if evidence_dir:
            path = evidence_dir/filename
            raw = path.read_bytes()
            require(hashlib.sha256(raw).hexdigest() == pin, 'Evidence bytes do not match edition: '+filename)
            source_lines[ident] = raw.decode('utf-8').splitlines()
    for o in origins:
        require(o['edition_id'] in editions and 1 <= o['line_start'] <= o['line_end'] <= editions[o['edition_id']]['line_count'], 'Wrong evidence locator: '+o['id'])
        require(hashlib.sha256(o['quote'].encode()).hexdigest() == o['quote_sha256'], 'Quotation hash changed: '+o['id'])
        require(all(isinstance(k,str) and isinstance(v,str) for k,v in o['fields'].items()), 'Wrong evidence field types.')
        claim = next((value for key,value in o['fields'].items() if key in ['Authority','Authority / status','Defensible evidence/status']),None)
        role = 'audit_reported_user_decision' if 'Decision ID' in o['fields'] else 'audit_reported_exchange' if 'Thread' in o['fields'] else 'reconstruction_and_audit_analysis' if o['edition_id']=='OSDS:EVD-0001' else 'audit_author_account'
        require(o.get('authority_context') == {'reported_role':role,'claim_basis':'audit_field' if claim else 'audit_prose',
                'source_claim':claim or 'Source-author account or analysis; not individually attributed to an authenticated original speaker.',
                'authenticated':False,'original_message_locator':None}, 'Source-scoped authority changed or improperly authenticated: '+o['id'])
        if source_lines:
            quote = '\n'.join(source_lines[o['edition_id']][o['line_start']-1:o['line_end']])
            require(quote == o['quote'], 'Quotation/locator does not match exact source: '+o['id'])
        require('/Users/' not in o['quote'] and not re.search(r'[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}',o['quote']), 'Private operational detail in new research evidence.')
    for x in entries:
        require(x['states'] == STATES, 'Unsupported authority/scientific/status upgrade: '+x['id'])
        require(x['origin_ids'] and len(x['origin_ids']) == len(set(x['origin_ids'])) and
                [c['origin_id'] for c in x['content']] == x['origin_ids'], 'Lost/mismatched research evidence: '+x['id'])
        for c in x['content']:
            require(c['origin_id'] in byorigin, 'Unresolved research provenance: '+x['id'])
            if c['origin_id'] not in byorigin:
                continue
            o=byorigin[c['origin_id']]
            require(canonical(c['fields']) == canonical(o['fields']) and c['text'] == (None if o['fields'] else o['quote']),
                    'Lost/rewritten source field or qualification: '+x['id'])
        if x['kind'] in {'reported_decision','correction_or_conflict','federation_relationship_proposal'}:
            require(bool(x['qualifications']), 'Lost authority/conflict qualification: '+x['id'])
        if 'internal_targets' in x:
            require(all(i in byid for i in x['internal_targets']), 'Broken research relationship target: '+x['id'])
            if x['kind']=='theme_membership_proposal':
                require(x['predicate']=='proposed_theme_association' and x['internal_targets']==[x['subject'],x['object']] and
                        x['object'] in byid and byid[x['object']]['kind']=='theme_umbrella_candidate', 'Unsourced/incorrect theme association: '+x['id'])
                require(any(o['edition_id']=='OSDS:EVD-0002' and 'Four **proposed' in o['quote'] for o in [byorigin[i] for i in x['origin_ids'] if i in byorigin]), 'Theme association lacks A02 source.')
                proposed = {}
                for origin_id in x['origin_ids']:
                    o = byorigin.get(origin_id,{})
                    if o.get('edition_id')=='OSDS:EVD-0002':
                        for parent, members in re.findall(r'\*\*([^*]+)\*\* \(([^)]+)\)',o['quote']):
                            proposed[parent.casefold()] = {name.strip().casefold() for name in members.split(',')}
                parent = byid.get(x['object'],{}).get('label','').casefold()
                child = byid.get(x['subject'],{}).get('label','').casefold()
                require(child in proposed.get(parent,set()), 'Unsourced theme assignment for actual subject/object: '+x['id'])
        if x['kind']=='federation_relationship_proposal':
            f=x['content'][0]['fields']
            require([x['subject'],x['predicate'],x['object']]==[f['Subject'],f['Predicate'],f['Object']], 'Relationship lost subject/predicate/object: '+x['id'])
    aliases=research['source_aliases']
    require(len(aliases)==62 and {a['audit_alias'] for a in aliases}=={f'SRC{i:03}' for i in range(1,63)}, 'Lost/duplicate source audit aliases.')
    source_names = {r['qualified_id']:r['name'] for r in (records or [])}
    for a in aliases:
        require(a['source_id']=='OSDS:SRC-'+a['audit_alias'][3:] and a['origin_id'] in byorigin and
                a['status']=='row_alias_mapping_only_not_external_identity_verification' and a['canonical_name']==source_names.get(a['source_id']), 'Invalid/reassigned audit alias.')
    actual={'concepts':len(research['concepts']),'assertions':len(research['assertions']),'origins':len(origins),'source_aliases':len(aliases),
            'concept_types':dict(Counter(x['kind'] for x in research['concepts'])),
            'assertion_types':dict(Counter(x['kind'] for x in research['assertions']))}
    require(actual==research['counts']==manifest['research_profile']['counts'], 'Research counts differ; keep source/research/membership totals separate.')
    for kind,count in [('instrument_family_candidate',16),('observation_method_context',8),('theme_umbrella_candidate',4),('descriptive_dimension_candidate',6),('computing_platform_candidate',6)]:
        require(actual['concept_types'].get(kind)==count, 'Lost required research family: '+kind)
    platforms=[x['label'] for x in research['concepts'] if x['kind']=='computing_platform_candidate']
    require(len(platforms)==len(set(platforms)) and {'Raspberry Pi','Raspberry Pi 5','Jetson Nano','Jetson Orin Nano'} <= set(platforms), 'Hardware identities merged or lost.')
    render=renderer()
    human=(root/'OSDS_Scientific_Reference_Register.md').read_text()
    machine=(root/'OSDS_Machine_Reference.md').read_text()
    try:
        expected_presentation = render.scientific_section(research)
    except (KeyError, IndexError, TypeError, StopIteration) as exc:
        require(False, 'Research presentation cannot render invalid source fields: '+str(exc))
    else:
        require(section(human,render.START,render.END)==expected_presentation, 'Machine–Scientific research parity failed; regenerate owned section.')
    require(section(machine,render.INDEX_START,render.INDEX_END)==render.machine_index(research), 'Machine record locator index differs from research records.')
    readme=(root/'README.md').read_text()
    require('document version 0.2.0' in readme and 'sixteen provisional instrument families' in readme and
            'four proposed theme umbrellas and six descriptive dimensions' in readme, 'README research summary/version mismatch.')
    if ledger_path:
        ledger=json.loads(ledger_path.read_text())
        for tag,ident in [('A01','OSDS:EVD-0001'),('A02','OSDS:EVD-0002')]:
            units=[u for u in ledger['units'] if u['edition']==tag]
            require([n for u in units for n in range(u['line_start'],u['line_end']+1)]==list(range(1,PINS[ident][2]+1)), 'Private ledger source accounting gap/overlap.')
            for u in units:
                require(u['disposition'] in {'incorporated_candidate','already_represented','corrected_qualified','duplicate_mention','contextual_material','deferred','excluded'} and u['reason'] and u['targets'], 'Source item lacks disposition/target/reason.')
                if source_lines:
                    require(u['quote']=='\n'.join(source_lines[ident][u['line_start']-1:u['line_end']]), 'Private ledger quotation/locator mismatch.')
                if u['disposition']=='incorporated_candidate':
                    matched=[o for o in origins if o['edition_id']==ident and o['line_start']==u['line_start'] and o['line_end']==u['line_end']]
                    require(len(matched)==1 and canonical(matched[0]['fields'])==canonical(u['fields']) and matched[0]['quote']==u['quote'], 'Incorporated source field/qualification omitted.')
                    require(all(t in byid and matched[0]['id'] in byid[t]['origin_ids'] for t in u['targets']), 'Ledger destination missing scientific evidence.')
    return actual
