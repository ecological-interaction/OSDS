# Changelog

Meaningful changes to research registers, provenance, repository documentation and publication preparation are recorded here. Document, classification and schema versions are separate from research-resource releases and Git tags.

## [Unreleased]

### README and federation illustration — 22 October 2026

- Replaced obsolete Phase 1 status wording with the verified public source repository and initial commit, distinguishing local website integration from verified deployment. Consolidated the README into concise scope, register roles, classifications, federation/DRM, publication, assets and reuse sections.
- Added assets/diagrams/ with the authoritative osds_federation.mmd, a derived osds_federation.svg embedded immediately below the README title, and a dependency-free fixed-layout renderer. Labels, relationships, styling and layout hints are maintained in the Mermaid source; the SVG is regenerated, not independently edited.
- Preserved the requested full explanatory hierarchy: IRKB synthesis, the shared DRM/entities/provenance/interoperability layer, six neighbours in two rows of three, confirmed sibling AMRKB as an additional card, and highlighted OSDS with eight observation categories in two columns and four rows. Included the conceptual-relationships qualification and documented developing research directions without claiming implemented integrations.
- Established diagram maintenance and portable asset-path conventions in AGENTS.md. The website will need explicit asset import and an approved new source pin later; no publication manifest is changed here.

Both research registers and CITATION.cff are unchanged. No scientific records, classifications, evidence or identifiers are changed. No commit, push or deployment is performed by this preparation.

### Editorial review — 22 October 2026

- Made the Scientific Reference Register introduction and reading key neutral and concise, retaining candidate status, unverified coverage/category assignments, the human/machine authority distinction and classification limits. Removed the conversational citation-recovery description and construction-history wording; their substantive provenance limitations remain in the machine reference.
- Removed the scientific subtitle's version/date administration; document version 0.1.2 and its baseline date remain recorded below and in the machine manifest. Kept the discovery-review date alongside the access limitations.
- Removed the scientific register's federation/project-background paragraph, already covered by README.md. Rephrased the standards paragraph as methodological context rather than a contributor instruction. Removed one statement about the absence of editorial reclassification; the unresolved EFAS placement and all overlap questions remain.
- Cleared P01's internal conversation identifier to null without removing its field. Replaced retrieval-tool commentary with the research-relevant fact that the inventory was supplied directly and original citation URLs remain unavailable. These later edits supersede Phase 1's retention of the conversation identifier and failed-retrieval details; no scientific evidence depended on those operational details.
- Relabelled P02's provenance type from conversation_attachment to research_scope_attachment, retaining its attachment label and scientific role. P01's inventory title, version, date and unresolved citation labels, and P03's dated evidence review, remain intact.
- Neutralised two conversational text values in each of the 62 records: source_urls[].origin now refers to original citations, and url_verification.scope refers to original citation-link recovery. These are editorial text substitutions; JSON field structures, scientific values, evidence URLs, IDs, classifications and verification states are unchanged.
- Moved remaining prose maintenance instructions from the machine introduction to AGENTS.md and clarified provenance policy in README.md. Retained the machine manifest's existing version history and structured interpretation metadata.

No scientific table rows, source names, descriptions, URLs, domain assignments or observation categories were moved or removed. No scientific evidence or unresolved identity/classification decision was changed. This is an unreleased editorial cleanup, not a new research release or schema version. No Git initialisation or publication was performed.

### Added — 22 October 2026

- Local Phase 1 supporting files: README.md, AGENTS.md, .gitignore, this changelog and CFF 1.2.0 citation metadata.
- Explicit register authority, maintenance, validation, DRM limitations and owner-managed publication boundaries.
- Attribution copied from the existing EIRKB/EII convention: Jonathan Minchin, Ecological Interaction, ORCID 0000-0001-8152-1796. The OSDS repository URL in citation metadata is the intended destination, not a verified remote.

### Changed — 22 October 2026

- Corrected the project name from “Observational Systems and Data Source” to “Observational Systems and Data Sources” in both register subtitles and the machine manifest's working_name. Retained the historical OSDKB previous_working_name.
- Replaced the machine manifest's absolute local DRM evidence_path with repository-relative `DRM/README.md`, qualified by an added evidence_repository field naming the Ecological Information umbrella repository. The methodology evidence remains the same DRM introduction; the operational filesystem prefix is not retained in public content.
- Replaced P01's session-dependent received_in wording with “user-supplied research inventory transcription”.
- Reworded P01's retrieval_note neutrally while retaining the historical failed-retrieval fact: the referenced retrieval yielded placeholders, the user supplied the inventory text directly, and original citation URLs were not recovered. Removed session and assistant-specific operational wording.

The 62 source-record JSON blocks, scientific tables, identifiers, classifications, anchors, descriptions, references, URLs, candidate statuses, review flags, unresolved questions and research development history are unchanged. P01's conversation identifier, P02's attachment name and all three provenance entries remain traceable. No new ontology, database, research release or standards-conformance claim is introduced.

## Existing document baseline — 0.1.2, 22 October 2026

Both research registers already declared document version 0.1.2 before Phase 1. The machine file contains one manifest and 62 candidate source records; the scientific file is their four-column presentation. The existing change_history records document development through 0.1.0, 0.1.1 and 0.1.2. Those entries are retained as document history, not newly asserted published releases.

Phase 1 retains the 0.1.2 document labels and records the subsequent naming/provenance edits above. No Git repository, commit, tag, remote, website deployment or published release is established by this preparation.
