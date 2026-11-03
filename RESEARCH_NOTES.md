# OSDS — Research and Publication Notes

[Current OSDS Overview](README.md). The following material preserves the earlier Overview’s research context and dated publication-preparation statements; its former diagram layout is historical.

**Work in Progress — Academic Research Resource**

Jonathan Minchin · Ecological Interaction · [ORCID 0000-0001-8152-1796](https://orcid.org/0000-0001-8152-1796).

## Current candidate-research edition — 3 November 2026

Document 0.2.0 adds one `osds.documentary-research/0.1.0` block inside the
existing authoritative Machine Reference. Original source schema and inventory
classification identities remain unchanged. Original source objects and raw
JSON, source memberships, URLs, provenance and candidate questions are preserved.
Concepts, research assertions and proposed theme associations have separate counts.
RC/RA/OR/EVD identifiers are OSDS-local documentary conventions, not DRM codes.
Keep IDs stable; source aliases SRC001–SRC062 map to existing qualified IDs.

A01 and the preserved retrospective history audit are byte-identical copies of
one edition. A02 supplies richer fields but reports direct original-conversation
access that this task cannot authenticate. The fresh bounded retrieval exposes
five later turns and no older cursor; it supplies audit preparation/handoff
context, not the original scientific discussion. No full October recovery or
scientific approval follows. The existing conversation identifier remains null.

## Evidence and intake limits

Immediate editions: A01 SHA-256
`3ccfde241f06e9a8d329e679e6369f52a3319b6cab0a7d7bd5ada8bdad3d43a0`;
A02 SHA-256 `36c2add69e3656632abaa1d6dc1f5669524eacefa546103fe25a8b797a6588b1`.
Machine origins retain exact source fields, quotations, section/line locators and
quote hashes. A private ledger outside the repository accounts for all source
units, including administrative context/quoted reconstruction instructions not
republished as scientific assertions. These are secondary audits, not transcripts.
Original-message chronology, unavailable attachments, original citations and
scientific completeness remain unresolved. Administrative scores are not imported
as scientific confidence; no independent review of this implementation is claimed.

A01 missing-detail statements remain alongside A02's examples and reported
confirmations. Generic Raspberry Pi and Raspberry Pi 5, Jetson Nano and Orin Nano
remain distinct. Embedded inference placement, umbrella assignments, biological
namespace suggestions, aircraft/marine/subsurface scope and PROV-O's later origin
are explicit qualified proposals/conflicts. No existing provider is excluded.

DRM-MSP 0.1.0 review revision 2 remains an unadopted candidate. DRM-ING-01–10 are
experimental local safeguards for this intake, not adopted clauses or a new
service. Identity, provenance, status/authority, versions, local classifications,
typed relationships and preservation checks are applied within this task only.
DRM Phase 4 closure does not authorise Phase 5. No DRM or neighbouring research
content, website pins/checksums/importers or diagram asset has been modified.
The central website still publishes its pinned source edition; local 0.2.0 is not
a new deployment. No resource release, licence, DOI or standards compliance added.

Scientific source tables are preserved manually. The new research section and
Machine locator index are generated from Machine JSON by
`scripts/render_osds_research.py --write`; never edit those generated sections
independently. `scripts/validate_osds.py --profile research-0.1` checks the
explicit profile, original sources and generated presentation. Optional `--baseline`
compares an actual preserved working edition; `--evidence-dir` checks quotes
against exact audit files and `--ledger` checks private source-unit accounting.
Local schema checking is separate from scientific and owner review. Original
source-schema identity is not itself an executable JSON Schema.

## Earlier documentary and publication context — 2 November 2026

Both registers retain document version 0.1.2; maintenance revision
`2026-11-02-documentary` identifies this documentation-only patch. The schema
`osds.reference-register/0.1-draft` and classification
`osds.inventory-classification/0.1` are unchanged. All 62 candidate source records,
220 memberships and eight directed candidate questions retain their evidence
and uncertainty. This is not a resource release or scientific acceptance event.

DRM-MSP 0.1.0 review revision 2 is an unadopted methodological candidate. Later
DRM decisions record the bounded Phase 4 documentary-preservation pilots as
completed and closed. Their scope does not establish scientific verification,
general MSP adoption/release, full DRM conformance or authorisation for Phase 5.
The retained historical methodology object/locators in the machine manifest are
not silently redirected; current context is a separate metadata addition.

The local repository is on main with a configured OSDS origin and committed
baseline. At inspection, the central website manifest pins source commit
`48b5d7f131ae4b86557d4a7b58a1371cacd3cd6c`; it maps README to the OSDS landing
page and the Scientific Register to `scientific-reference-register/`, with
research notes and authoritative pinned machine access handled centrally.
This describes inspected configuration, not newly verified live deployment.
Local maintenance now differs from that pinned edition. No website pin,
checksum, importer or deployment was changed.

Incomplete OSDS research-chat materials are historical context, not an alternative
authority to the registers. The missing sixteen instrument families, four theme
umbrellas and unavailable decisions are not reconstructed. Dataset-level
scientific/rights review, original citation recovery, ambiguous identities,
classification questions and standards-edition choices remain unresolved.

## Purpose and scope

OSDS catalogues global observational systems, IoT data sources, physical sensor networks, scientific monitoring, ground-truth observations and physical computing datasets. Its 62 entries are candidate sources, not 62 verified measurement datasets. Source discovery and URL identity review do not establish dataset availability, calibration, measurement quality, access rights or fitness for analysis.

## Research registers

- [Scientific Reference Register](OSDS_Scientific_Reference_Register.md): concise human-readable, four-column catalogue organised by disciplinary domain.
- [Machine Reference](OSDS_Machine_Reference.md): authoritative structured register containing one manifest and 62 source records in 63 JSON fences inside Markdown. It is not standalone JSON.
- [Citation metadata](CITATION.cff) and [Changelog](CHANGELOG.md): attribution and research/documentation history.

The scientific register presents the machine register's research content; it is not a competing inventory. Provider, observing network, site registry, archive, repository and individual dataset identities remain distinct. Candidate status, evidence limitations and unresolved overlap questions are retained. No automatic synchronisation or ingestion service is implemented.

## Disciplinary domains and observation categories

The eight disciplinary domains are **Environmental, Ecological, Terrestrial, Hydrological, Agricultural, Urban, Industrial and Experimental** (D01–D08).

The eight observation categories are **IoT telemetry, Scientific monitoring, Ground-truth observations, Autonomous observations, Campaign datasets, Citizen sensing, Physical computing and Historical instrumental records** (O01–O08).

Both classifications permit multiple memberships. The illustration uses shorter explanatory labels for several categories; the registers retain the authoritative labels and codes. The eight observation categories are distinct from the eight disciplinary domains.

## Federation and research methodology

OSDS contributes observation-system discovery and provenance to the Ecological Information federation. EII concerns ecological indicators; GISDS catalogues geographic resources; EIRKB, AMRKB and other neighbouring databases retain their own research responsibilities and authoritative records.

The illustration places comparative interdisciplinary synthesis in IRKB, shared methodology and interoperability in DRM, and observation-source discovery in OSDS. IRKB, SSKB and DPRKB remain developing research directions in the umbrella architecture; PBCKA's scope is still being defined. AMRKB is an established sibling project. The layout expresses conceptual relationships, not dependency, control, completed database implementations or verified cross-project data bindings.

Historical context: earlier preparation referenced the Ecological Information umbrella at `DRM/README.md` and its then-current detailed-specification limitation. That source locator remains in historical manifest evidence. The current candidate/Phase 4 context is distinguished above; OSDS conformance is not certified.

Source IDs remain stable (`SRC-001`–`SRC-062`), with qualified references such as `OSDS:SRC-001`, `OSDS:D01` and `OSDS:O01`. OSDS and EII domain codes are not equivalent because their numbers match. Future interoperability requires explicit record identities, evidence-backed relationships and documented mappings. Document versions, `osds.inventory-classification/0.1` and `osds.reference-register/0.1-draft` remain separate.

W3C SOSA/SSN, OGC SensorThings API and OGC Observations, Measurements and Samples (OMS) are foundations for later review. No ontology mappings, API implementation, adopted standards editions or conformance claims are established here.

## Repository and website publication — historical preparation context

The following paragraphs retain earlier preparation statements and route expectations; the current configuration summary above supersedes them as present-state guidance.

The source repository is [ecological-interaction/OSDS](https://github.com/ecological-interaction/OSDS). Its initial research/documentation commit, `dab53c4d0e88cfb3512a56311c488afa87183850`, was verified on public `main`. Both registers retain document version **0.1.2**, dated **22 October 2026**; no research-resource release or DOI is assigned.

The central [Ecological Interaction website](https://ecological-interaction.github.io/) publishes approved source editions through a shared MkDocs Material build. OSDS integration has been prepared locally for `/information/OSDS/`, with `research-guide/` and `machine-reference/` pages; deployment of those routes has not been verified by this preparation.

Publication uses a full source commit pin and SHA-256 allowlist, rather than automatically following the latest source revision. The machine-reference page links to the authoritative pinned source without duplicating its research body. This README and diagram are a subsequent local revision: inclusion requires a reviewed source commit, updated publication checksums and explicit asset handling in the central importer. No separate OSDS MkDocs site is required.

## Diagram and asset source

`assets/diagrams/osds_federation.mmd` is the single authoritative diagram source, including labels, conceptual connections, styles and fixed-layout hints. The embedded SVG is a derived portable rendering for GitHub Markdown and MkDocs, without a Mermaid plugin. Regenerate it after source edits with:

```sh
python3 assets/diagrams/render_osds_federation.py
```

The small, dependency-free renderer handles this diagram's fixed-layout Mermaid subset, rather than acting as a general Mermaid engine. Do not edit the SVG independently. Diagram and future visual research assets belong under `assets/diagrams/`.

## Reuse and research status

No licence has been selected for this repository or its research documentation. Public accessibility and citation metadata do not grant reuse permission. Third-party works and datasets retain their own access, licence and attribution conditions. Each dataset requires product-level review of methods, units, quality, time span and rights before analytical use.
