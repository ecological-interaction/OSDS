# OSDS project instructions

Read README.md, CHANGELOG.md and both reference registers before working on this project.

- Use the approved name Observational Systems and Data Sources (OSDS).
- Treat OSDS_Machine_Reference.md as the authoritative structured register and OSDS_Scientific_Reference_Register.md as its human-readable presentation. Parse JSON fences by block_type; the Markdown file is not standalone JSON.
- Preserve all 62 source records, issued IDs, anchors, classifications, scientific wording, references, discovery URLs, candidate status, evidence gaps and unresolved identity questions unless a scoped research change is authorised. Do not merge apparent duplicates automatically.
- Preserve internal development provenance needed for traceability. Keep absolute local paths and session-dependent operational metadata out of public documents; record any approved provenance edits explicitly.
- Retain the eight disciplinary domains and eight observation categories. Qualify cross-project identifiers as OSDS:SRC-001, OSDS:D01 and OSDS:O01. Never infer equivalence to EII codes.
- DRM means Database Reference Methodology. DRM-MSP 0.1.0 review revision 2 remains an unadopted methodological candidate. Later DRM decisions record bounded Phase 4 documentary pilots as closed; older pending/pre-pilot statements remain dated evidence. This grants no scientific verification, general MSP adoption, full conformance or Phase 5 authority. Do not claim conformance or invent shared identifiers, taxonomy mappings or federation services.
- Keep document, classification and schema versions separate. SOSA/SSN, SensorThings and OMS are future reference foundations, not implemented ontology mappings or verified standards compliance.
- Validate unique and matching source IDs, all JSON blocks, domain/category counts, machine anchors and research-content preservation after changes. Capture actual working-file hashes and parsed records outside the repository before maintenance; use the validator preservation mode against that baseline, not merely HEAD.
- Use stable filenames and record meaningful research, editorial and provenance changes in CHANGELOG.md. Do not invent releases, DOIs, historical commits or licences.
- The repository is already initialised. Staging, commits, Git configuration changes and publication still require explicit scoped instructions; documentary maintenance does not authorise them.
- GitHub creation, connection and publication are managed separately by the owner. Do not configure remotes, push, transfer repositories or deploy without a new explicit instruction.
- Do not change the umbrella or website repository as part of OSDS-only work. Publication is intended through the central MkDocs build; do not install independent MkDocs or duplicate authoritative research files in a website docs directory.

## Editorial separation

- Keep the Scientific Reference Register focused on scope, source tables, classifications, scientific interpretation and dated verification limitations. Keep project background in README.md, attribution in CITATION.cff and administrative changes in CHANGELOG.md.
- Keep source-inventory references, unresolved citation labels and dated discovery evidence in the machine reference. Do not retain conversation identifiers or retrieval-tool commentary merely as operational history. The existing conversation_id field remains null; do not populate it with internal session identifiers.
- Preserve the original inventory assertions when adding evidence and maintain both registers together. Do not convert original-citation uncertainty into a claim of verified provenance.

## Diagrams and visual research assets

- Keep diagrams and related visual research assets in assets/diagrams/. The authoritative source for the federation illustration is osds_federation.mmd, including its fixed-layout hints.
- Regenerate osds_federation.svg with `python3 assets/diagrams/render_osds_federation.py` after editing the source. Do not maintain independent SVG text, labels or relationships. The renderer supports this diagram's Mermaid subset only.
- Maintain the approved four-stage Overview: blue OSDS title, orange eight-category content block with separate domain/category dimensions retained in the documentation, compact DRM output, and analysis/application cards. Match the final GISDS typography and palette; preserve candidate status and conceptual relationship qualifications.
- Do not infer implemented integrations or equivalence of domain codes from conceptual connectors. Keep the conceptual-status note and distinguish developing databases from populated resources in the README.
- Keep README asset paths repository-relative. Central publication must explicitly allowlist, checksum and import the derived asset with the README; do not advance publication pins, edit the website or deploy as part of source-only diagram work.

- Match the umbrella/GISDS visual palette exactly: blue synthesis, lavender shared methodology, green knowledge-base cards, amber scientific/geographic/observation-source cards and neutral grey PBCKA. Preserve current labels, classification distinctions and conceptual edges when changing styling.

- Keep README.md as the concise Overview and RESEARCH_NOTES.md as supporting research context, version distinctions and historical publication notes. Neither supporting document replaces an authoritative register.

## Documentary maintenance validation

- Run `python3 -B scripts/validate_osds.py`; it reads JSON fences by block_type,
  checks the four-column Scientific/Machine parity, classifications, memberships,
  candidate questions, provenance, IDs, anchors and local Markdown links.
- Before editing, preserve the working registers outside this repository. Run
  `python3 -B scripts/validate_osds.py --baseline <preserved-directory>` to compare
  source objects and raw JSON fences, classifications, provenance, scientific
  table rows and the narrowly allowed manifest documentary additions. The validator
  never rewrites files; structural success is not scientific, rights or MSP approval.
- No tool owns the Scientific source tables. Preserve their rows verbatim; edit
  reading guidance/navigation only unless a scoped research change is authorised.
  Keep linked IDs, linked source names, coverage and prose observation descriptions
  in four columns, with O01–O08 key near the top. Validate intended section anchors,
  including duplicate-heading suffixes, not merely the existence of a label.
- Keep private baselines, generated previews and approval evidence outside the
  public repository. No new extraction document, private chat identifier or local
  workstation path belongs in public content. Stage C review and Stage D validation
  are separate owner stages; Stage B implementation does not perform either.

## Candidate research profile 0.1

- Document 0.2.0 retains all 62 original source records/raw JSON, eight domains,
  eight categories, 220 original memberships, eight original directed questions
  and dated provenance. One separate `documentary_research` block uses local schema
  `osds.documentary-research/0.1.0` and OSDS_Research.schema.json. Never force new
  instrument/method/theme/assertion records into the provider inventory.
- RC/RA/OR/EVD IDs are persistent local documentary locators. Reuse exact concepts
  across roles only with retained evidence; no automatic alias/model merging.
  Preserve independent candidate, identity, science, authority, relationship and
  rights/access states. A02 “confirmed” tokens remain audit-reported, not approvals.
- `python3 -B scripts/render_osds_research.py --write` owns only marked Scientific
  research content and Machine research locator index. It never changes source
  tables or JSON. Edit the Machine research authority first, then regenerate.
- Validate with `python3 -B scripts/validate_osds.py --profile research-0.1` and
  optional `--baseline`, `--evidence-dir`, `--ledger` against preserved private
  inputs. Keep all original source guards. Run tests without writing caches.
- Keep full archived editions immutable. Private source accounting and operational
  retrieval records remain outside the public repository; no internal chat IDs.
  Experimental DRM-ING controls are not adopted protocol or infrastructure.
