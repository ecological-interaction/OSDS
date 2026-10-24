# OSDS — Research and Publication Notes

[Current OSDS Overview](README.md). The following material preserves the earlier Overview’s research context and dated publication-preparation statements; its former diagram layout is historical.

**Work in Progress — Academic Research Resource**

Jonathan Minchin · Ecological Interaction · [ORCID 0000-0001-8152-1796](https://orcid.org/0000-0001-8152-1796).

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

The **Database Reference Methodology (DRM)** is maintained in the [Ecological Information umbrella](https://github.com/ecological-interaction/ecological-information), at `DRM/README.md`. It is under development and provides no approved detailed specification or certification of OSDS conformance.

Source IDs remain stable (`SRC-001`–`SRC-062`), with qualified references such as `OSDS:SRC-001`, `OSDS:D01` and `OSDS:O01`. OSDS and EII domain codes are not equivalent because their numbers match. Future interoperability requires explicit record identities, evidence-backed relationships and documented mappings. Document versions, `osds.inventory-classification/0.1` and `osds.reference-register/0.1-draft` remain separate.

W3C SOSA/SSN, OGC SensorThings API and OGC Observations, Measurements and Samples (OMS) are foundations for later review. No ontology mappings, API implementation, adopted standards editions or conformance claims are established here.

## Repository and website publication

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
