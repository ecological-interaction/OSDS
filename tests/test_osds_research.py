"""Candidate-profile regressions; corruptions are confined to temporary copies."""
import copy
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('osds_checks', ROOT/'scripts/validate_osds.py')
checks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checks)


class ResearchProfileTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)/'OSDS'
        shutil.copytree(ROOT,self.root,ignore=shutil.ignore_patterns('.git','__pycache__'))
        self.original = (self.root/checks.MACHINE).read_text()

    def mutate(self, role, change):
        text = self.original
        match = next(m for m in checks.FENCE.finditer(text) if checks.strict_json(m[1])['block_type']==role)
        data = checks.strict_json(match[1])
        change(data)
        text = text[:match.start(1)]+json.dumps(data,ensure_ascii=False,indent=2)+'\n'+text[match.end(1):]
        (self.root/checks.MACHINE).write_text(text)

    def expect(self, needle, baseline=None):
        errors = checks.check(self.root,baseline,profile='research-0.1')
        self.assertTrue(any(needle in error for error in errors),errors)

    def test_profile_and_documented_cli(self):
        self.assertEqual(checks.check(self.root,profile='research-0.1'),[])
        result = subprocess.run([sys.executable,'-B',str(self.root/'scripts/validate_osds.py'),'--profile','research-0.1'],text=True,capture_output=True)
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)
        self.assertIn('64 JSON fences',result.stdout)

    def test_original_source_objects_and_nulls_are_protected(self):
        baseline = Path(self.tmp.name)/'before'
        shutil.copytree(self.root,baseline)
        self.mutate('source_record',lambda d:d.update(description='Invented observation'))
        self.expect('Preservation: source-record values/types/order changed',baseline)
        self.mutate('source_record',lambda d:d['observation_categories'].pop())
        self.expect('Membership counts differ',baseline)

    def test_lost_fields_and_qualifications_are_rejected(self):
        self.mutate('documentary_research',lambda d:d['concepts'][0]['content'][0]['fields'].pop('Methodological review needed'))
        self.expect('Lost/rewritten source field or qualification')
        self.mutate('documentary_research',lambda d:next(x for x in d['assertions'] if x['kind']=='reported_decision').update(qualifications=[]))
        self.expect('Lost authority/conflict qualification')
        self.mutate('documentary_research',lambda d:d['origins'][0].update(quote=d['origins'][0]['quote']+' changed'))
        self.expect('Quotation hash changed')

    def test_duplicate_ids_and_wrong_editions_are_rejected(self):
        self.mutate('documentary_research',lambda d:d['concepts'][1].update(id=d['concepts'][0]['id']))
        self.expect('Duplicate research IDs')
        self.mutate('documentary_research',lambda d:d['evidence_editions'][0].update(sha256='0'*64))
        self.expect('Wrong source edition/hash')

    def test_relationships_authority_and_membership_need_evidence(self):
        self.mutate('documentary_research',lambda d:next(x for x in d['assertions'] if x['kind']=='theme_membership_proposal')['internal_targets'].append('OSDS:RC-9999'))
        self.expect('Broken research relationship target')
        self.mutate('documentary_research',lambda d:d['concepts'][0]['states'].update(reported_authority='authenticated_owner_approval'))
        self.expect('Unsupported authority/scientific/status upgrade')
        self.mutate('documentary_research',lambda d:d['origins'][0]['authority_context'].update(authenticated=True))
        self.expect('Source-scoped authority changed or improperly authenticated')
        def remove_source(d):
            x=next(x for x in d['assertions'] if x['kind']=='theme_membership_proposal')
            x['origin_ids']=[d['concepts'][0]['origin_ids'][0]]
            o=next(o for o in d['origins'] if o['id']==x['origin_ids'][0])
            x['content']=[{'origin_id':o['id'],'fields':o['fields'],'text':None}]
        self.mutate('documentary_research',remove_source)
        self.expect('Theme association lacks A02 source')
        def wrong_parent(d):
            x=next(x for x in d['assertions'] if x['kind']=='theme_membership_proposal')
            parent=next(c for c in d['concepts'] if c['kind']=='theme_umbrella_candidate' and c['id']!=x['object'])
            x['object']=parent['id'];x['internal_targets']=[x['subject'],x['object']]
        self.mutate('documentary_research',wrong_parent)
        self.expect('Unsourced theme assignment for actual subject/object')

    def test_source_and_research_navigation_and_determinism(self):
        path=self.root/checks.SCIENTIFIC
        original=path.read_text()
        path.write_text(original.replace('OSDS_Machine_Reference.md#src-001','OSDS_Machine_Reference.md#src-002',1))
        self.expect('Scientific/Machine identity')
        path.write_text(original.replace('OSDS_Machine_Reference.md#rc-0001','OSDS_Machine_Reference.md#rc-0002',1))
        self.expect('Machine–Scientific research parity failed')
        path.write_text(original)
        module=checks.research_tools().renderer()
        data=module.load_research(self.root)
        self.assertEqual(module.scientific_section(data),module.scientific_section(copy.deepcopy(data)))
        self.assertEqual(checks.check(self.root,profile='research-0.1'),[])


if __name__=='__main__':
    unittest.main()
