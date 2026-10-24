# OSDS project instructions

Read README.md, CHANGELOG.md and both reference registers before working on this project.

- Use the approved name Observational Systems and Data Sources (OSDS).
- Treat OSDS_Machine_Reference.md as the authoritative structured register and OSDS_Scientific_Reference_Register.md as its human-readable presentation. Parse JSON fences by block_type; the Markdown file is not standalone JSON.
- Preserve all 62 source records, issued IDs, anchors, classifications, scientific wording, references, discovery URLs, candidate status, evidence gaps and unresolved identity questions unless a scoped research change is authorised. Do not merge apparent duplicates automatically.
- Preserve internal development provenance needed for traceability. Keep absolute local paths and session-dependent operational metadata out of public documents; record any approved provenance edits explicitly.
- Retain the eight disciplinary domains and eight observation categories. Qualify cross-project identifiers as OSDS:SRC-001, OSDS:D01 and OSDS:O01. Never infer equivalence to EII codes.
- DRM means Database Reference Methodology. Its introduction does not establish an approved detailed specification. Do not claim conformance or invent shared identifiers, taxonomy mappings or federation services.
- Keep document, classification and schema versions separate. SOSA/SSN, SensorThings and OMS are future reference foundations, not implemented ontology mappings or verified standards compliance.
- Validate unique and matching source IDs, all JSON blocks, domain/category counts, machine anchors and research-content preservation after changes. Compare with preserved originals until Git history is established.
- Use stable filenames and record meaningful research, editorial and provenance changes in CHANGELOG.md. Do not invent releases, DOIs, historical commits or licences.
- Git initialisation and commits require a subsequent explicit instruction. Do not stage, commit, alter Git configuration or initialise Git during Phase 1.
- GitHub creation, connection and publication are managed separately by the owner. Do not configure remotes, push, transfer repositories or deploy without a new explicit instruction.
- Do not change the umbrella or website repository as part of OSDS-only work. Publication is intended through the central MkDocs build; do not install independent MkDocs or duplicate authoritative research files in a website docs directory.

## Editorial separation

- Keep the Scientific Reference Register focused on scope, source tables, classifications, scientific interpretation and dated verification limitations. Keep project background in README.md, attribution in CITATION.cff and administrative changes in CHANGELOG.md.
- Keep source-inventory references, unresolved citation labels and dated discovery evidence in the machine reference. Do not retain conversation identifiers or retrieval-tool commentary merely as operational history. The existing conversation_id field remains null; do not populate it with internal session identifiers.
- Preserve the original inventory assertions when adding evidence and maintain both registers together. Do not convert original-citation uncertainty into a claim of verified provenance.

## Diagrams and visual research assets

- Keep diagrams and related visual research assets in assets/diagrams/. The authoritative source for the federation illustration is osds_federation.mmd, including its fixed-layout hints.
- Regenerate osds_federation.svg with `python3 assets/diagrams/render_osds_federation.py` after editing the source. Do not maintain independent SVG text, labels or relationships. The renderer supports this diagram's Mermaid subset only.
- Maintain the approved four-stage Overview: blue OSDS title, orange illustrative source examples with separate domain/category dimensions, compact DRM output, and analysis/application cards. Match the final GISDS typography and palette; preserve candidate status and conceptual relationship qualifications.
- Do not infer implemented integrations or equivalence of domain codes from conceptual connectors. Keep the conceptual-status note and distinguish developing databases from populated resources in the README.
- Keep README asset paths repository-relative. Central publication must explicitly allowlist, checksum and import the derived asset with the README; do not advance publication pins, edit the website or deploy as part of source-only diagram work.

- Match the umbrella/GISDS visual palette exactly: blue synthesis, lavender shared methodology, green knowledge-base cards, amber scientific/geographic/observation-source cards and neutral grey PBCKA. Preserve current labels, classification distinctions and conceptual edges when changing styling.

- Keep README.md as the concise Overview and RESEARCH_NOTES.md as supporting research context, version distinctions and historical publication notes. Neither supporting document replaces an authoritative register.
