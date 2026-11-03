"""Render only the candidate-research sections from the authoritative Machine Reference.

Original source tables/record fences are outside these generated sections.
--write is deliberate local presentation generation, not research acceptance.
"""
import argparse
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
START = '<!-- BEGIN GENERATED OSDS RESEARCH -->'
END = '<!-- END GENERATED OSDS RESEARCH -->'
INDEX_START = '<!-- BEGIN GENERATED OSDS RESEARCH INDEX -->'
INDEX_END = '<!-- END GENERATED OSDS RESEARCH INDEX -->'
GROUPS = [
    ('Instrumentation families', ['instrument_family_candidate']),
    ('Observation methods and validation', ['observation_method_context']),
    ('Computing platforms and research resources', ['computing_platform_candidate', 'research_resource_candidate']),
    ('Methods capabilities and reference frameworks', ['method_capability_candidate', 'method_framework_candidate', 'standards_framework_candidate', 'framework_reference_group', 'technical_interface_group']),
    ('Themes and descriptive dimensions', ['theme_umbrella_candidate', 'descriptive_dimension_candidate']),
]


def load_research(root=ROOT):
    objects = [json.loads(m[1]) for m in re.finditer(r'^```json[ \t]*\n(.*?)^```[ \t]*$', (root / 'OSDS_Machine_Reference.md').read_text(), re.M | re.S)]
    return next(obj for obj in objects if obj.get('block_type') == 'documentary_research')


def anchor(ident):
    return ident.split(':', 1)[1].lower()


def cell(value):
    return str(value).replace('|', '&#124;').replace('\n', '<br>')


def link(ident):
    return f'[{ident}](OSDS_Machine_Reference.md#{anchor(ident)})'


def evidence_links(ids):
    return ', '.join(f'[{i}](#evidence-{anchor(i)})' for i in ids)


def table(headers, rows):
    return '| ' + ' | '.join(headers) + ' |\n|' + '|'.join('---' for _ in headers) + '|\n' + ''.join('| ' + ' | '.join(cell(x) for x in row) + ' |\n' for row in rows) + '\n'


def scientific_section(research):
    origins = {o['id']: o for o in research['origins']}
    text = START + '''
## Candidate research expansion — document 0.2.0

The original 62-source inventory and its 220 memberships are unchanged. The
following are separately typed **documentary candidates**, not new providers,
verified instruments, adopted families, approved scope exclusions or implemented
services. A01 is a retrospective reconstruction with bounded access; A02 supplies
richer audit-reported details and user-decision claims without an authenticated
original transcript. They are complementary, not independent confirmation.
Original scientific turns remain unavailable through the bounded later excerpt.

Documentary inclusion, canonical candidate state, identity, scientific review,
reported authority, relationship review and rights/access are independent.
Every new item remains unverified; a reported “confirmed” decision is not an
authenticated approval. This is author-performed documentary semantic review,
not independent expert review or scientific verification. Source-specific units,
calibration, model performance, standard editions, rights and scope need review.

[Instrument families](#instrumentation-families) · [Observation methods](#observation-methods-and-validation) · [Computing/resources](#computing-platforms-and-research-resources) · [Methods/frameworks](#methods-capabilities-and-reference-frameworks) · [Themes/dimensions](#themes-and-descriptive-dimensions) · [Assertions and gaps](#qualified-assertions-and-research-questions) · [Evidence detail](#research-evidence-details).

'''
    for title, kinds in GROUPS:
        text += '## ' + title + '\n\n'
        entries = [x for x in research['concepts'] if x['kind'] in kinds]
        if title == 'Instrumentation families':
            text += 'Sixteen overlapping family proposals retain A01’s wording and missing-detail qualifications alongside A02’s examples. The “directly observed” column below is **A02’s unverified assertion**, not a certified measurement/derivation classification. Inferences are not measured ecological facts.\n\n'
            rows = []
            for x in entries:
                fields = [c['fields'] for c in x['content']]
                a = next(f for f in fields if 'Family wording supplied in R§3' in f)
                b = next(f for f in fields if 'Family ID' in f)
                rows.append([link(x['id']), x['label'] + ' / A02: ' + b['Instrument family'], b['Examples'], b['Directly observed properties'], b['Candidate indicators / inferences'], a['Methodological review needed'], evidence_links(x['origin_ids'])])
            text += table(['Research ID', 'Family / source variant', 'Instrument examples', 'Properties as asserted in A02', 'Candidate indicators / inferences', 'A01 review question', 'Full source detail'], rows)
        else:
            for x in entries:
                text += f"### {x['label']}\n\n{link(x['id'])} · {x['kind'].replace('_', ' ')} · candidate; identity/science unverified.\n\n"
                if 'existing_category_reference' in x:
                    text += f"Research context for `{x['existing_category_reference']}`; this does not redefine or add source memberships.\n\n"
                # One intelligible source account per record here; exhaustive distinct fields/qualifications are below.
                first = x['content'][0]
                if first['fields']:
                    text += '\n'.join(f"- **{key}:** {value}" for key, value in first['fields'].items()) + '\n\n'
                else:
                    text += first['text'] + '\n\n'
                for note in x['qualifications']:
                    text += '**Qualification:** ' + note + '\n\n'
                text += 'Complete source fields and additional qualified accounts: ' + evidence_links(x['origin_ids']) + '.\n\n'
    text += '''## Qualified assertions and research questions

Original subject/predicate/object and authority wording are retained as reported
assertions, with separate current qualifications. “OSDS measures” refers to the
physical systems described, not to measurements performed by this catalogue.
A02’s provisional theme assignments do not overwrite A01’s lack of assignments.
Aircraft/marine/subsurface/biological boundaries and proposed BIPKB naming are
unresolved; no provider is removed or external namespace adopted. The original
three foundational references remain separate from later PROV-O prompt-origin
material. Conceptual arrows do not establish causation or operational bindings.

'''
    for x in research['assertions']:
        text += f"### {x['label']}\n\n{link(x['id'])} · {x['kind'].replace('_', ' ')} · proposed; science unverified; authority audit-reported.\n\n"
        for key in ['subject', 'predicate', 'object']:
            if x[key] is not None:
                text += f'**{key.capitalize()}:** {x[key]}. '
        if x['subject'] is not None:
            text = text.rstrip() + '\n\n'
        first = x['content'][0]
        if first['fields']:
            text += '\n'.join(f'- **{k}:** {v}' for k, v in first['fields'].items()) + '\n\n'
        else:
            text += first['text'] + '\n\n'
        for q in x['qualifications']:
            text += '**Qualification:** ' + q + '\n\n'
        text += 'Full supporting context: ' + evidence_links(x['origin_ids']) + '.\n\n'
    text += '''## Research evidence details

The following preserves every retained immediate-audit field and non-indexed
qualification, once per evidence slice. A quoted source instruction or proposed
workflow is documentary content, not executable authority. A01 and A02 claims
remain attributed to their own edition, including conflicts. This does not
establish completeness of the original research conversation or external science.

'''
    editions = {e['id']: e for e in research['evidence_editions']}
    for o in research['origins']:
        e = editions[o['edition_id']]
        text += f"<a id=\"evidence-{anchor(o['id'])}\"></a>\n\n### {o['id']} — {e['label']}\n\n{o['section']} / {o['subsection'] or 'section context'}, lines {o['line_start']}–{o['line_end']}. Exact audit edition SHA-256: `{e['sha256']}`.\n\n"
        text += '**Reported authority context:** ' + o['authority_context']['reported_role'].replace('_',' ') + '; original scientific message locator unavailable; not authenticated. Source authority tokens remain reports, not current acceptance.\n\n'
        if o['fields']:
            text += '\n'.join(f'- **{k}:** {v}' for k,v in o['fields'].items()) + '\n\n'
        else:
            text += o['quote'] + '\n\n'
    text += '### Audit alias continuity\n\nA02 `SRC001`–`SRC062` are row aliases for the original qualified source IDs, not replacement identities. Variant audit names are retained in the Machine research block’s `source_aliases`; source names, URLs, objects and anchors remain unchanged.\n\n'
    return text + END + '\n'


def machine_index(research):
    text = INDEX_START + '\n## Research record locators\n\nThe following anchors identify records in the single authoritative research JSON block below. JSON pointers are relative to that block; these are local documentary locators, not verified scientific identities.\n\n'
    for collection in ['concepts', 'assertions']:
        for i,x in enumerate(research[collection]):
            text += f"<a id=\"{anchor(x['id'])}\"></a>\n\n### {x['id']} — {x['label']}\n\nJSON pointer: `/{collection}/{i}`. Candidate documentary record; scientific/identity verification outstanding.\n\n"
    return text + INDEX_END + '\n'


def replace_section(text, start, end, generated):
    if start not in text:
        return text.rstrip() + '\n\n' + generated
    before, tail = text.split(start,1)
    _, after = tail.split(end,1)
    return before + generated.rstrip() + after


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true', help='Regenerate owned sections; never source tables or JSON.')
    args = parser.parse_args()
    data = load_research()
    if args.write:
        p = ROOT/'OSDS_Scientific_Reference_Register.md'
        p.write_text(replace_section(p.read_text(), START, END, scientific_section(data)))
        p = ROOT/'OSDS_Machine_Reference.md'
        # On first write the insertion marker belongs immediately before research JSON.
        text = p.read_text()
        if INDEX_START not in text:
            marker = '## Candidate research block\n'
            text = text.replace(marker, machine_index(data) + '\n' + marker, 1)
        else:
            text = replace_section(text, INDEX_START, INDEX_END, machine_index(data))
        p.write_text(text)
        print('Generated research presentation and locator index only. Source tables and JSON untouched.')
    else:
        print(scientific_section(data))


if __name__ == '__main__':
    main()
