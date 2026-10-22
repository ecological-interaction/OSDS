# Observational Systems and Data Sources (OSDS)

**Work in Progress — Academic Research Resource**

Jonathan Minchin · Ecological Interaction · [ORCID 0000-0001-8152-1796](https://orcid.org/0000-0001-8152-1796).

OSDS catalogues global observational systems, IoT data sources, physical sensor networks, scientific monitoring, ground-truth observations and physical computing datasets. The current inventory contains 62 candidate sources, not 62 verified measurement datasets. Discovery URL identity review does not establish dataset availability, measurement quality, access rights or fitness for use.

## Start here

- [Scientific Reference Register](OSDS_Scientific_Reference_Register.md): human-readable four-column presentation, grouped by the eight disciplinary domains.
- [Machine Reference](OSDS_Machine_Reference.md): authoritative structured register, comprising a manifest and 62 source records in fenced JSON blocks inside Markdown. This is not a standalone JSON file.
- [CITATION.cff](CITATION.cff): academic attribution.
- [CHANGELOG.md](CHANGELOG.md): document baseline and local repository preparation.

The machine reference remains authoritative. The scientific register is its human-readable presentation, not a competing source inventory. No automatic synchronisation or ingestion service is implemented.

## Research scope and classifications

The eight disciplinary domains are Environmental, Ecological, Terrestrial, Hydrological, Agricultural, Urban, Industrial and Experimental (D01–D08).

The eight observation categories are IoT telemetry, Scientific monitoring, Ground-truth observations, Autonomous observations, Campaign datasets, Citizen sensing, Physical computing and Historical instrumental records (O01–O08).

Both classifications permit multiple memberships. Preserve the original presentation group and evidence for any additional assignments. Networks, providers, site registries, repositories and particular datasets must remain distinguishable. Do not infer sensors, variables, calibration, licences or access capabilities from a source name.

## Ecological Information federation and DRM

OSDS is independently maintained within Ecological Information. OSDS describes observation sources and provenance; EII describes ecological indicators; GISDS catalogues geographic resources. Future relationships must identify particular records and supporting evidence rather than imply an implemented federation or universal crosswalk.

The shared methodology is the **Database Reference Methodology (DRM)**. Its current introduction is maintained as `DRM/README.md` in the Ecological Information umbrella repository (`ecological-interaction/ecological-information`). It is under development and does not establish an approved detailed specification or certify OSDS conformance.

Preserve stable source IDs (`SRC-001`–`SRC-062`) and qualified references such as `OSDS:SRC-001`, `OSDS:D01` and `OSDS:O01`. OSDS and EII domain codes are not equivalent merely because their numbers match. Record any future crosswalk explicitly with evidence. Keep document versions, `osds.inventory-classification/0.1` and `osds.reference-register/0.1-draft` separate; do not replace them with an assumed DRM version.

W3C SOSA/SSN, OGC SensorThings API and OGC Observations, Measurements and Samples (OMS) remain references for later development. No standards editions, ontology mappings, API implementation or conformance claims are adopted by this preparation.

## Maintenance and provenance

Preserve issued IDs, source names, classifications, descriptions, discovery URLs, candidate status, evidence gaps and unresolved identity or duplication questions. Unknown values and empty collections retain the meanings documented in the machine register. Source identity review must not silently become complete record verification.

Maintain both registers together when research changes are approved. Validate JSON fences by `block_type`, unique and matching IDs, counts, category memberships and all machine-record anchors. Preserve scientific table wording during editorial or publication-only work.

Retain useful internal development provenance in the machine reference, including source-inventory references, research attachment labels, dates, unresolved citation markers and review limitations. Exclude conversation identifiers and retrieval-tool commentary that do not support a scientific claim; the legacy conversation_id field remains null to preserve the existing field structure. These historical references are not guaranteed public retrieval routes. Use portable repository references instead of absolute filesystem paths, and neutral descriptions instead of session-dependent operational wording. Record substantive and provenance edits in the changelog.

Use stable filenames and maintain version notes inside documents. Future Git history will record revisions; uncommitted files are not protected by Git. Generated JSON or CSV exports, if introduced later, must derive from the authoritative register rather than become independently edited copies.

## Versions and publication status

Both research registers retain document version **0.1.2**, dated **22 October 2026**. This phase records naming and provenance edits in the changelog without assigning a new research-resource release, Git tag or schema version.

The intended GitHub repository is `ecological-interaction/OSDS`. The intended reading route is `/information/OSDS/` through the existing central `ecological-interaction.github.io` MkDocs build, following EII's commit-pinned, checksum-verified import pattern. These are intended destinations, not claims of repository creation or website deployment.

Phase 1 is local file preparation only: Git has not been initialised here, no remote has been configured, and nothing has been committed, pushed or published by this phase. GitHub connection and publication remain separately managed by the owner. No independent MkDocs installation is required.

No licence has been selected for this repository or its research documentation. Public accessibility and citation metadata do not grant reuse permission. Referenced third-party works and datasets retain their own access, licence and attribution conditions.
