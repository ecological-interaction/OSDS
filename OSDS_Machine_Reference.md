# OSDS — Machine Reference Register

**Observational Systems and Data Sources** · Version 0.1.2 · 22 October 2026 · Candidate research inventory

Structured companion to [OSDS Scientific Reference Register](OSDS_Scientific_Reference_Register.md). All 62 supplied entries are retained, including possible provider or repository overlaps. Source URL identity has been checked for all 62 entries; no complete source record or dataset is independently verified. This is an inventory of sources, not imported measurements or a certified standard.

## Interpretation and conventions

The first JSON fence is a manifest (`block_type: manifest`); subsequent fences are source records (`block_type: source_record`). Record IDs are locally assigned `SRC-001`–`SRC-062`, preserving the original provisional inventory numbers as suffixes. Qualified references use `OSDS:SRC-001`. These assignments follow EII's stable local ID and namespace pattern but are not prescribed by DRM.

The supplied inventory establishes D01–D08 and O01–O08. Both classifications are many-to-many. `domain` retains the original presentation heading; `related_domains` permits later documented assignments. Category assignments and coverage are inherited inventory assertions, not new scientific verification. OSDS:D01 is not EII:D01: their meanings differ. No equivalence crosswalk is asserted.

The current umbrella calls DRM **Database Reference Methodology** and explicitly states that it does not establish an approved detailed specification. EII's historical “Database Research Methodology v1.0.0” wording is recorded as historical context, not adopted as a verified specification. Classification, schema and document versions are separate.

`null` means unknown or not yet reviewed. An empty array means no items recorded, not confirmed absence. No provider, station, sensor, dataset, measurement, unit, licence, API, extent, quality control, DOI or external identifier is inferred from a source's name. The original inventory supplied no full URLs. Version 0.1.1 adds newly researched official discovery routes with separate URL identity evidence; the original inventory citation URLs remain unavailable. Bare citation labels are preserved as section-level provenance; `+1` and `+2` are unresolved citation display markers, not evidence counts. They cannot be reconstructed into original links.

## Entity and evidence model

A source record may later describe a provider, observing network, coordination infrastructure, site registry, archive, portal, repository or specific dataset. `entity_type` remains null until supported by evidence. Platform/station, sensor/instrument, observed property, feature of interest, observation, sample, datastream, unit and procedure are separate entity slots. They are not instantiated here. SOSA/SSN, SensorThings and OMS are retained as candidate foundations, with editions and formal mappings unresolved.

`candidate` means present in the research inventory without a completed identity and evidence review. A future `verified` source record must document the precise identity, authoritative URL, dated evidence, review scope and supported claims. Verifying a provider does not verify all its datasets, access rights, observation categories or measurement quality. Access, licence, provenance and fitness remain product-level assessment questions. `review_flags` and `candidate_relationships` are explicit editorial questions, not supplied facts or verified relationships.

The original names, coverage strings, heading assignments, category arrays and provisional numbers are preserved in every record. `description` remains null because the supplied source table has no per-entry scientific description. The human register presents the supplied coverage and pathway information without fabricating variables or methods.

## URL review — 22 October 2026

All 62 records now have an official discovery route or an explicitly scoped collection route. Each URL object records its evidence page, review date, retrieval method and limitations. Indexed official excerpts establish identity where direct retrieval was blocked or timed out; they do not prove live availability. `url_verification` is separate from the unchanged candidate `record_status` and incomplete record-level `verification`.

The original `access` fields remain unassigned: a homepage or documentation page is not necessarily a dataset portal or API. OSCAR/Surface operational access remains unresolved. ISC displayed an outage notice. Lincoln is linked as a dataset collection, AG-LOAM to its maintainer's dataset documentation, and the historical NREL label to a current NLR grid data/tools page. Possible duplicate inventory entries are preserved.

## Document manifest

```json
{
  "block_type": "manifest",
  "title": "OSDS — Machine Reference Register",
  "working_name": "Observational Systems and Data Sources",
  "previous_working_name": "Observational Systems and Data Knowledge Base (OSDKB)",
  "document_version": "0.1.2",
  "created": "2026-10-22",
  "schema": "osds.reference-register/0.1-draft",
  "status": "candidate_inventory_not_verified",
  "record_count": 62,
  "verified_record_count": 0,
  "records_with_source_urls": 62,
  "human_file": "OSDS_Scientific_Reference_Register.md",
  "methodology": {
    "name": "Database Reference Methodology",
    "specification_version": null,
    "conformance": "not_assessable_detailed_specification_not_established",
    "evidence_repository": "https://github.com/ecological-interaction/ecological-information",
    "evidence_path": "DRM/README.md",
    "legacy_eii_methodology_name": "Database Research Methodology",
    "legacy_eii_version_reference": "1.0.0"
  },
  "identifier_policy": {
    "namespace": "OSDS",
    "record_pattern": "SRC-NNN",
    "status": "local_draft_assignment_not_DRM_mandated",
    "assignment_basis": "Original inventory numbers 001–062 retained as suffixes.",
    "stability": "Do not recycle or renumber identifiers; record consolidation through explicit redirects after review.",
    "classification_codes": "Preserve original D01–D08 and O01–O08; qualify as OSDS:D01 and OSDS:O01 outside the register.",
    "crosswalk_to_EII": null
  },
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_cardinality": "many_to_many",
  "domain_presentation_rule": "domain retains the original presentation group; related_domains holds additional evidenced assignments. Empty related_domains does not assert domain exclusivity.",
  "domains": [
    {
      "id": "D01",
      "qualified_id": "OSDS:D01",
      "label": "Environmental",
      "scope_as_supplied": "Atmosphere, weather, climate, radiation",
      "record_count": 9
    },
    {
      "id": "D02",
      "qualified_id": "OSDS:D02",
      "label": "Ecological",
      "scope_as_supplied": "Biodiversity, habitats, biological activity",
      "record_count": 9
    },
    {
      "id": "D03",
      "qualified_id": "OSDS:D03",
      "label": "Terrestrial",
      "scope_as_supplied": "Soil, geology, geomorphology",
      "record_count": 8
    },
    {
      "id": "D04",
      "qualified_id": "OSDS:D04",
      "label": "Hydrological",
      "scope_as_supplied": "Freshwater, groundwater, oceans",
      "record_count": 9
    },
    {
      "id": "D05",
      "qualified_id": "OSDS:D05",
      "label": "Agricultural",
      "scope_as_supplied": "Crops, irrigation, livestock",
      "record_count": 7
    },
    {
      "id": "D06",
      "qualified_id": "OSDS:D06",
      "label": "Urban",
      "scope_as_supplied": "Air quality, mobility, infrastructure",
      "record_count": 7
    },
    {
      "id": "D07",
      "qualified_id": "OSDS:D07",
      "label": "Industrial",
      "scope_as_supplied": "Energy, machinery, material flows",
      "record_count": 6
    },
    {
      "id": "D08",
      "qualified_id": "OSDS:D08",
      "label": "Experimental",
      "scope_as_supplied": "Laboratories, field stations, testbeds",
      "record_count": 7
    }
  ],
  "observation_categories": [
    {
      "id": "O01",
      "qualified_id": "OSDS:O01",
      "label": "IoT telemetry",
      "record_count": 11
    },
    {
      "id": "O02",
      "qualified_id": "OSDS:O02",
      "label": "Scientific monitoring",
      "record_count": 42
    },
    {
      "id": "O03",
      "qualified_id": "OSDS:O03",
      "label": "Ground-truth observations",
      "record_count": 23
    },
    {
      "id": "O04",
      "qualified_id": "OSDS:O04",
      "label": "Autonomous observations",
      "record_count": 10
    },
    {
      "id": "O05",
      "qualified_id": "OSDS:O05",
      "label": "Campaign datasets",
      "record_count": 27
    },
    {
      "id": "O06",
      "qualified_id": "OSDS:O06",
      "label": "Citizen sensing",
      "record_count": 6
    },
    {
      "id": "O07",
      "qualified_id": "OSDS:O07",
      "label": "Physical computing",
      "record_count": 13
    },
    {
      "id": "O08",
      "qualified_id": "OSDS:O08",
      "label": "Historical instrumental records",
      "record_count": 26
    }
  ],
  "provenance": [
    {
      "id": "P01",
      "type": "user_supplied_inventory_transcription",
      "title": "OSDKB — Global Observation Source Inventory",
      "version": "0.1",
      "date_as_supplied": "2026-10-22",
      "conversation_id": null,
      "received_in": "user-supplied research inventory transcription",
      "retrieval_note": "The 62-entry inventory was supplied directly for transcription. Original citation URLs are unavailable; subsequently identified official discovery routes have separate dated evidence.",
      "full_source_urls_supplied": false,
      "section_citation_labels": {
        "D01": [
          "World Meteorological Organization",
          "+2"
        ],
        "D02": [
          "DEIMS",
          "+2"
        ],
        "D04": [
          "waterdata.usgs.gov",
          "+2"
        ],
        "D05": [
          "LTAR Network",
          "+2"
        ],
        "D06": [
          "openaq.org",
          "+1"
        ]
      }
    },
    {
      "id": "P02",
      "type": "research_scope_attachment",
      "name": "Pasted text(1).txt",
      "role": "Foundational scope, entity groupings and three standards; not the 62-record inventory."
    },
    {
      "id": "P03",
      "type": "web_url_identity_review",
      "date": "2026-10-22",
      "method": "Primary official pages and indexed official excerpts; per-entry evidence URL, method and limitations recorded.",
      "relation_to_original_citations": "newly_identified_links_not_recovered_original_citations"
    }
  ],
  "foundational_standards": [
    {
      "name": "SOSA / SSN — Semantic Sensor Network Ontology",
      "role": "Candidate semantic entity model",
      "edition": null,
      "url": "https://www.w3.org/TR/vocab-ssn-2017/",
      "conformance_claim": false,
      "url_checked_at": "2026-10-22",
      "url_check_scope": "Official standards reference page; adoption and source-level conformance not asserted.",
      "additional_reference_urls": [
        "https://www.w3.org/TR/vocab-ssn-2023/"
      ],
      "review_note": "2017 Recommendation reference retained; the 2023-edition page retrieved is a 2026 working draft. No new edition adopted."
    },
    {
      "name": "OGC SensorThings API",
      "role": "Candidate discovery and observation access model",
      "edition": null,
      "url": "https://www.ogc.org/standards/sensorthings/",
      "conformance_claim": false,
      "url_checked_at": "2026-10-22",
      "url_check_scope": "Official standards reference page; adoption and source-level conformance not asserted."
    },
    {
      "name": "OGC Observations, Measurements and Samples (OMS)",
      "role": "Candidate conceptual observation and sampling model",
      "edition": null,
      "url": "https://www.ogc.org/standards/om/",
      "conformance_claim": false,
      "url_checked_at": "2026-10-22",
      "url_check_scope": "Official standards reference page; adoption and source-level conformance not asserted."
    }
  ],
  "unresolved_questions": [
    "DRM has no approved detailed code or conformance specification; are local SRC-NNN identifiers to be adopted permanently?",
    "Confirm an OSDS classification version and any explicit crosswalk to EII D01–D15; codes alone do not imply equivalence.",
    "Confirm whether to consolidate EarthScope 022/062 and Zenodo 055/058, or preserve distinct scoped records.",
    "Confirm parent/collection relationships for ICOS 005/040 and portal overlap for NASA 053/057.",
    "Resolve broad or ambiguous source labels, especially AG-LOAM, Lincoln Agricultural Robotics Datasets and NREL Grid Research.",
    "Choose and verify relevant standards editions before formal entity mappings or conformance claims.",
    "Original inventory citation URLs remain unavailable; assigned links are separately researched official discovery routes.",
    "OSCAR/Surface operational application endpoint is unresolved after test-environment notice and circular redirect.",
    "Full dataset-level verification, access checks and licence review remain outstanding."
  ],
  "updated": "2026-10-22",
  "url_identity_checked_count": 62,
  "url_review_scope": "All 62 entries have an official discovery route or scoped collection route. Original hidden citation links remain unavailable. No dataset-level verification is asserted.",
  "change_history": [
    {
      "version": "0.1.0",
      "date": "2026-10-22",
      "change": "Transcribed 62 candidate inventory records without supplied source URLs."
    },
    {
      "version": "0.1.1",
      "date": "2026-10-22",
      "change": "Added official discovery routes, dated URL identity evidence, standards references and access caveats. Preserved all original IDs, classifications, names, coverage and candidate status."
    },
    {
      "version": "0.1.2",
      "date": "2026-10-22",
      "change": "Human tables use four columns: linked ID, linked source name, coverage and plain-language observation description. Retained category key and recorded presentation conventions. Scientific records unchanged."
    }
  ],
  "presentation": {
    "human_columns": [
      "OSDS ID",
      "Source",
      "Coverage as supplied",
      "Observation description"
    ],
    "machine_record_link": "OSDS ID alone links to the matching stable anchor in OSDS_Machine_Reference.md. Preserve this navigation in future revisions.",
    "source_link": "Written source name links to its official discovery URL in a separate column.",
    "observation_display": "Short plain-language descriptions of the inherited category combinations; no observation codes in source-table rows.",
    "category_key": "Retain O01–O08 code structure at the top of the human register.",
    "evidence_display": "Omit per-row evidence-status and separate Source URL columns; retain evidence and URL details in the machine register.",
    "category_display_phrases": {
      "O01": "networked sensor readings",
      "O02": "scientific monitoring",
      "O03": "field reference observations",
      "O04": "autonomous observations",
      "O05": "field-study datasets",
      "O06": "community observations",
      "O07": "embedded-device measurements",
      "O08": "historical instrument records"
    }
  }
}
```

## Source records

<a id="src-001"></a>

### SRC-001 — WMO WIGOS / GBON

```json
{
  "block_type": "source_record",
  "id": "SRC-001",
  "qualified_id": "OSDS:SRC-001",
  "name": "WMO WIGOS / GBON",
  "original_inventory_id": "001",
  "original_inventory_row": "001\tWMO WIGOS / GBON\tGlobal\tO02, O08",
  "domain": "D01",
  "related_domains": [],
  "observation_categories": [
    "O02",
    "O08"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Global",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://wmo.int/activities/wmo-integrated-global-observing-system-wigos/wmo-integrated-global-observing-system",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://wmo.int/activities/wmo-integrated-global-observing-system-wigos/wmo-integrated-global-observing-system",
      "evidence_method": "official_indexed_excerpt",
      "notes": "Official page identifies the named source. URL identity check only; datasets, access conditions and scientific classifications were not audited."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D01",
    "section_citation_labels": [
      "World Meteorological Organization",
      "+2"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://wmo.int/activities/wmo-integrated-global-observing-system-wigos/wmo-integrated-global-observing-system"
    ]
  }
}
```

<a id="src-002"></a>

### SRC-002 — WMO OSCAR

```json
{
  "block_type": "source_record",
  "id": "SRC-002",
  "qualified_id": "OSDS:SRC-002",
  "name": "WMO OSCAR",
  "original_inventory_id": "002",
  "original_inventory_row": "002\tWMO OSCAR\tGlobal station metadata\tO02",
  "domain": "D01",
  "related_domains": [],
  "observation_categories": [
    "O02"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Global station metadata",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://oscar.wmo.int/surface/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://public.wmo.int/activities/global-observing-system-gos/global-observing-system-gos",
      "evidence_method": "official_indexed_excerpt",
      "notes": "Official WMO documentation identifies OSCAR/Surface. Direct application fetch displayed a test-environment notice, and its operational link redirected to the same page. Identity confirmed; operational endpoint remains unresolved."
    }
  ],
  "url_status": "official_route_identified_operational_status_unresolved",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D01",
    "section_citation_labels": [
      "World Meteorological Organization",
      "+2"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [
    "Station metadata does not establish access to measurements.",
    "Official WMO documentation identifies OSCAR/Surface. Direct application fetch displayed a test-environment notice, and its operational link redirected to the same page. Identity confirmed; operational endpoint remains unresolved."
  ],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://oscar.wmo.int/surface/",
      "https://public.wmo.int/activities/global-observing-system-gos/global-observing-system-gos"
    ]
  }
}
```

<a id="src-003"></a>

### SRC-003 — NOAA NCEI

```json
{
  "block_type": "source_record",
  "id": "SRC-003",
  "qualified_id": "OSDS:SRC-003",
  "name": "NOAA NCEI",
  "original_inventory_id": "003",
  "original_inventory_row": "003\tNOAA NCEI\tGlobal / US\tO02, O05, O08",
  "domain": "D01",
  "related_domains": [],
  "observation_categories": [
    "O02",
    "O05",
    "O08"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Global / US",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://www.ncei.noaa.gov/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://www.ncei.noaa.gov/",
      "evidence_method": "official_page_content",
      "notes": "Official page identifies the named source. URL identity check only; datasets, access conditions and scientific classifications were not audited."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D01",
    "section_citation_labels": [
      "World Meteorological Organization",
      "+2"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://www.ncei.noaa.gov/"
    ]
  }
}
```

<a id="src-004"></a>

### SRC-004 — NOAA Global Monitoring Laboratory

```json
{
  "block_type": "source_record",
  "id": "SRC-004",
  "qualified_id": "OSDS:SRC-004",
  "name": "NOAA Global Monitoring Laboratory",
  "original_inventory_id": "004",
  "original_inventory_row": "004\tNOAA Global Monitoring Laboratory\tGlobal\tO02, O05, O08",
  "domain": "D01",
  "related_domains": [],
  "observation_categories": [
    "O02",
    "O05",
    "O08"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Global",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://gml.noaa.gov/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://gml.noaa.gov/",
      "evidence_method": "official_page_content",
      "notes": "Official page identifies the named source. URL identity check only; datasets, access conditions and scientific classifications were not audited."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D01",
    "section_citation_labels": [
      "World Meteorological Organization",
      "+2"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://gml.noaa.gov/"
    ]
  }
}
```

<a id="src-005"></a>

### SRC-005 — ICOS

```json
{
  "block_type": "source_record",
  "id": "SRC-005",
  "qualified_id": "OSDS:SRC-005",
  "name": "ICOS",
  "original_inventory_id": "005",
  "original_inventory_row": "005\tICOS\tEurope\tO02, O03",
  "domain": "D01",
  "related_domains": [],
  "observation_categories": [
    "O02",
    "O03"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Europe",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://www.icos-cp.eu/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://www.icos-cp.eu/",
      "evidence_method": "official_page_content",
      "notes": "Official page identifies the named source. URL identity check only; datasets, access conditions and scientific classifications were not audited."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D01",
    "section_citation_labels": [
      "World Meteorological Organization",
      "+2"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [],
  "candidate_relationships": [
    {
      "target_id": "OSDS:SRC-040",
      "relation": "possible_parent_or_collection_overlap",
      "status": "editorial_review_question_unverified"
    }
  ],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://www.icos-cp.eu/"
    ]
  }
}
```

<a id="src-006"></a>

### SRC-006 — AERONET

```json
{
  "block_type": "source_record",
  "id": "SRC-006",
  "qualified_id": "OSDS:SRC-006",
  "name": "AERONET",
  "original_inventory_id": "006",
  "original_inventory_row": "006\tAERONET\tGlobal\tO02, O03",
  "domain": "D01",
  "related_domains": [],
  "observation_categories": [
    "O02",
    "O03"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Global",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://aeronet.gsfc.nasa.gov/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://aeronet.gsfc.nasa.gov/",
      "evidence_method": "official_page_content",
      "notes": "Official page identifies the named source. URL identity check only; datasets, access conditions and scientific classifications were not audited."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D01",
    "section_citation_labels": [
      "World Meteorological Organization",
      "+2"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://aeronet.gsfc.nasa.gov/"
    ]
  }
}
```

<a id="src-007"></a>

### SRC-007 — IAGOS

```json
{
  "block_type": "source_record",
  "id": "SRC-007",
  "qualified_id": "OSDS:SRC-007",
  "name": "IAGOS",
  "original_inventory_id": "007",
  "original_inventory_row": "007\tIAGOS\tInternational aircraft\tO02, O04",
  "domain": "D01",
  "related_domains": [],
  "observation_categories": [
    "O02",
    "O04"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "International aircraft",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://www.iagos.org/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://www.iagos.org/",
      "evidence_method": "official_indexed_excerpt",
      "notes": "Official indexed IAGOS page matches the source; direct fetch timed out."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D01",
    "section_citation_labels": [
      "World Meteorological Organization",
      "+2"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [
    "Official indexed IAGOS page matches the source; direct fetch timed out."
  ],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://www.iagos.org/"
    ]
  }
}
```

<a id="src-008"></a>

### SRC-008 — NDACC

```json
{
  "block_type": "source_record",
  "id": "SRC-008",
  "qualified_id": "OSDS:SRC-008",
  "name": "NDACC",
  "original_inventory_id": "008",
  "original_inventory_row": "008\tNDACC\tGlobal\tO02, O08",
  "domain": "D01",
  "related_domains": [],
  "observation_categories": [
    "O02",
    "O08"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Global",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://ndacc.larc.nasa.gov/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://ndacc.larc.nasa.gov/",
      "evidence_method": "official_page_content",
      "notes": "Official page identifies the named source. URL identity check only; datasets, access conditions and scientific classifications were not audited."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D01",
    "section_citation_labels": [
      "World Meteorological Organization",
      "+2"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://ndacc.larc.nasa.gov/"
    ]
  }
}
```

<a id="src-009"></a>

### SRC-009 — Copernicus Atmosphere Monitoring Service

```json
{
  "block_type": "source_record",
  "id": "SRC-009",
  "qualified_id": "OSDS:SRC-009",
  "name": "Copernicus Atmosphere Monitoring Service",
  "original_inventory_id": "009",
  "original_inventory_row": "009\tCopernicus Atmosphere Monitoring Service\tGlobal / Europe\tO02, O03",
  "domain": "D01",
  "related_domains": [],
  "observation_categories": [
    "O02",
    "O03"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Global / Europe",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://atmosphere.copernicus.eu/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://atmosphere.copernicus.eu/",
      "evidence_method": "official_page_content",
      "notes": "Official page identifies the named source. URL identity check only; datasets, access conditions and scientific classifications were not audited."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D01",
    "section_citation_labels": [
      "World Meteorological Organization",
      "+2"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [
    "Separate observations, assimilation and model products; inventory categories require product-level review."
  ],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://atmosphere.copernicus.eu/"
    ]
  }
}
```

<a id="src-010"></a>

### SRC-010 — NEON

```json
{
  "block_type": "source_record",
  "id": "SRC-010",
  "qualified_id": "OSDS:SRC-010",
  "name": "NEON",
  "original_inventory_id": "010",
  "original_inventory_row": "010\tNEON\tUnited States\tO02, O03, O05",
  "domain": "D02",
  "related_domains": [],
  "observation_categories": [
    "O02",
    "O03",
    "O05"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "United States",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://www.neonscience.org/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://www.neonscience.org/",
      "evidence_method": "official_page_content",
      "notes": "Official page identifies the named source. URL identity check only; datasets, access conditions and scientific classifications were not audited."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D02",
    "section_citation_labels": [
      "DEIMS",
      "+2"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://www.neonscience.org/"
    ]
  }
}
```

<a id="src-011"></a>

### SRC-011 — FLUXNET

```json
{
  "block_type": "source_record",
  "id": "SRC-011",
  "qualified_id": "OSDS:SRC-011",
  "name": "FLUXNET",
  "original_inventory_id": "011",
  "original_inventory_row": "011\tFLUXNET\tGlobal\tO02, O08",
  "domain": "D02",
  "related_domains": [],
  "observation_categories": [
    "O02",
    "O08"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Global",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://fluxnet.org/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://fluxnet.org/",
      "evidence_method": "official_page_content",
      "notes": "Official page identifies the named source. URL identity check only; datasets, access conditions and scientific classifications were not audited."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D02",
    "section_citation_labels": [
      "DEIMS",
      "+2"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://fluxnet.org/"
    ]
  }
}
```

<a id="src-012"></a>

### SRC-012 — ILTER

```json
{
  "block_type": "source_record",
  "id": "SRC-012",
  "qualified_id": "OSDS:SRC-012",
  "name": "ILTER",
  "original_inventory_id": "012",
  "original_inventory_row": "012\tILTER\tInternational\tO02, O03, O08",
  "domain": "D02",
  "related_domains": [],
  "observation_categories": [
    "O02",
    "O03",
    "O08"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "International",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://www.ilter.network/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://www.ilter.network/",
      "evidence_method": "official_page_content",
      "notes": "Official page identifies the named source. URL identity check only; datasets, access conditions and scientific classifications were not audited."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D02",
    "section_citation_labels": [
      "DEIMS",
      "+2"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://www.ilter.network/"
    ]
  }
}
```

<a id="src-013"></a>

### SRC-013 — DEIMS-SDR

```json
{
  "block_type": "source_record",
  "id": "SRC-013",
  "qualified_id": "OSDS:SRC-013",
  "name": "DEIMS-SDR",
  "original_inventory_id": "013",
  "original_inventory_row": "013\tDEIMS-SDR\tInternational site registry\tO02, O05",
  "domain": "D02",
  "related_domains": [],
  "observation_categories": [
    "O02",
    "O05"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "International site registry",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://deims.org/about",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://deims.org/about",
      "evidence_method": "official_indexed_excerpt",
      "notes": "Linked to the official DEIMS about page, which establishes its site-registry role."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D02",
    "section_citation_labels": [
      "DEIMS",
      "+2"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [
    "Site registry records do not establish downloadable observations.",
    "Linked to the official DEIMS about page, which establishes its site-registry role."
  ],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://deims.org/about"
    ]
  }
}
```

<a id="src-014"></a>

### SRC-014 — GBIF

```json
{
  "block_type": "source_record",
  "id": "SRC-014",
  "qualified_id": "OSDS:SRC-014",
  "name": "GBIF",
  "original_inventory_id": "014",
  "original_inventory_row": "014\tGBIF\tGlobal\tO03, O05, O06",
  "domain": "D02",
  "related_domains": [],
  "observation_categories": [
    "O03",
    "O05",
    "O06"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Global",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://www.gbif.org/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://www.gbif.org/",
      "evidence_method": "official_indexed_excerpt",
      "notes": "Official GBIF search result confirms identity; direct homepage fetch was forbidden."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D02",
    "section_citation_labels": [
      "DEIMS",
      "+2"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [
    "Official GBIF search result confirms identity; direct homepage fetch was forbidden."
  ],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://www.gbif.org/"
    ]
  }
}
```

<a id="src-015"></a>

### SRC-015 — eBird

```json
{
  "block_type": "source_record",
  "id": "SRC-015",
  "qualified_id": "OSDS:SRC-015",
  "name": "eBird",
  "original_inventory_id": "015",
  "original_inventory_row": "015\teBird\tGlobal\tO03, O06",
  "domain": "D02",
  "related_domains": [],
  "observation_categories": [
    "O03",
    "O06"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Global",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://support.ebird.org/en/support/solutions/articles/48000838205-download-ebird-data",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://support.ebird.org/en/support/solutions/articles/48000838205-download-ebird-data",
      "evidence_method": "official_indexed_excerpt",
      "notes": "Official eBird download guidance used because the homepage presented bot protection."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D02",
    "section_citation_labels": [
      "DEIMS",
      "+2"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [
    "Official eBird download guidance used because the homepage presented bot protection."
  ],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://support.ebird.org/en/support/solutions/articles/48000838205-download-ebird-data"
    ]
  }
}
```

<a id="src-016"></a>

### SRC-016 — Wildlife Insights

```json
{
  "block_type": "source_record",
  "id": "SRC-016",
  "qualified_id": "OSDS:SRC-016",
  "name": "Wildlife Insights",
  "original_inventory_id": "016",
  "original_inventory_row": "016\tWildlife Insights\tInternational\tO03, O04, O05",
  "domain": "D02",
  "related_domains": [],
  "observation_categories": [
    "O03",
    "O04",
    "O05"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "International",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://www.wildlifeinsights.org/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://www.wildlifeinsights.org/",
      "evidence_method": "official_page_content",
      "notes": "Official page identifies the named source. URL identity check only; datasets, access conditions and scientific classifications were not audited."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D02",
    "section_citation_labels": [
      "DEIMS",
      "+2"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://www.wildlifeinsights.org/"
    ]
  }
}
```

<a id="src-017"></a>

### SRC-017 — LifeWatch ERIC

```json
{
  "block_type": "source_record",
  "id": "SRC-017",
  "qualified_id": "OSDS:SRC-017",
  "name": "LifeWatch ERIC",
  "original_inventory_id": "017",
  "original_inventory_row": "017\tLifeWatch ERIC\tEurope\tO02, O03, O05",
  "domain": "D02",
  "related_domains": [],
  "observation_categories": [
    "O02",
    "O03",
    "O05"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Europe",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://www.lifewatch.eu/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://www.lifewatch.eu/",
      "evidence_method": "official_indexed_excerpt",
      "notes": "Official indexed LifeWatch page matches; direct fetch timed out."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D02",
    "section_citation_labels": [
      "DEIMS",
      "+2"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [
    "Official indexed LifeWatch page matches; direct fetch timed out."
  ],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://www.lifewatch.eu/"
    ]
  }
}
```

<a id="src-018"></a>

### SRC-018 — GLEON

```json
{
  "block_type": "source_record",
  "id": "SRC-018",
  "qualified_id": "OSDS:SRC-018",
  "name": "GLEON",
  "original_inventory_id": "018",
  "original_inventory_row": "018\tGLEON\tInternational lakes\tO01, O02",
  "domain": "D02",
  "related_domains": [],
  "observation_categories": [
    "O01",
    "O02"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "International lakes",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://gleon.org/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://gleon.org/",
      "evidence_method": "official_page_content",
      "notes": "Official page identifies the named source. URL identity check only; datasets, access conditions and scientific classifications were not audited."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D02",
    "section_citation_labels": [
      "DEIMS",
      "+2"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://gleon.org/"
    ]
  }
}
```

<a id="src-019"></a>

### SRC-019 — International Soil Moisture Network

```json
{
  "block_type": "source_record",
  "id": "SRC-019",
  "qualified_id": "OSDS:SRC-019",
  "name": "International Soil Moisture Network",
  "original_inventory_id": "019",
  "original_inventory_row": "019\tInternational Soil Moisture Network\tGlobal\tO02, O03, O08",
  "domain": "D03",
  "related_domains": [],
  "observation_categories": [
    "O02",
    "O03",
    "O08"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Global",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://ismn.earth/en/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://ismn.earth/en/",
      "evidence_method": "official_page_content",
      "notes": "Official page identifies the named source. URL identity check only; datasets, access conditions and scientific classifications were not audited."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D03",
    "section_citation_labels": [],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://ismn.earth/en/"
    ]
  }
}
```

<a id="src-020"></a>

### SRC-020 — TERENO

```json
{
  "block_type": "source_record",
  "id": "SRC-020",
  "qualified_id": "OSDS:SRC-020",
  "name": "TERENO",
  "original_inventory_id": "020",
  "original_inventory_row": "020\tTERENO\tGermany\tO01, O02, O03",
  "domain": "D03",
  "related_domains": [],
  "observation_categories": [
    "O01",
    "O02",
    "O03"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Germany",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://www.tereno.net/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://www.tereno.net/",
      "evidence_method": "official_indexed_excerpt",
      "notes": "Official indexed TERENO homepage matches; direct fetch timed out."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D03",
    "section_citation_labels": [],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [
    "Official indexed TERENO homepage matches; direct fetch timed out."
  ],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://www.tereno.net/"
    ]
  }
}
```

<a id="src-021"></a>

### SRC-021 — ISRIC World Soil Information

```json
{
  "block_type": "source_record",
  "id": "SRC-021",
  "qualified_id": "OSDS:SRC-021",
  "name": "ISRIC World Soil Information",
  "original_inventory_id": "021",
  "original_inventory_row": "021\tISRIC World Soil Information\tGlobal\tO03, O05, O08",
  "domain": "D03",
  "related_domains": [],
  "observation_categories": [
    "O03",
    "O05",
    "O08"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Global",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://isric.org/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://isric.org/",
      "evidence_method": "official_page_content",
      "notes": "Official page identifies the named source. URL identity check only; datasets, access conditions and scientific classifications were not audited."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D03",
    "section_citation_labels": [],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [
    "Distinguish underlying observations from derived or modelled soil information."
  ],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://isric.org/"
    ]
  }
}
```

<a id="src-022"></a>

### SRC-022 — EarthScope

```json
{
  "block_type": "source_record",
  "id": "SRC-022",
  "qualified_id": "OSDS:SRC-022",
  "name": "EarthScope",
  "original_inventory_id": "022",
  "original_inventory_row": "022\tEarthScope\tUnited States / international\tO02, O05",
  "domain": "D03",
  "related_domains": [],
  "observation_categories": [
    "O02",
    "O05"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "United States / international",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://www.earthscope.org/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://www.earthscope.org/",
      "evidence_method": "official_page_content",
      "notes": "Official page identifies the named source. URL identity check only; datasets, access conditions and scientific classifications were not audited."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D03",
    "section_citation_labels": [],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [],
  "candidate_relationships": [
    {
      "target_id": "OSDS:SRC-062",
      "relation": "possible_same_provider",
      "status": "editorial_review_question_unverified"
    }
  ],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://www.earthscope.org/"
    ]
  }
}
```

<a id="src-023"></a>

### SRC-023 — International Seismological Centre

```json
{
  "block_type": "source_record",
  "id": "SRC-023",
  "qualified_id": "OSDS:SRC-023",
  "name": "International Seismological Centre",
  "original_inventory_id": "023",
  "original_inventory_row": "023\tInternational Seismological Centre\tGlobal\tO02, O08",
  "domain": "D03",
  "related_domains": [],
  "observation_categories": [
    "O02",
    "O08"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Global",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://www.isc.ac.uk/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://www.isc.ac.uk/",
      "evidence_method": "official_page_content",
      "notes": "Official ISC page identifies the organisation but displays a temporary offline notice. No data availability is confirmed."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D03",
    "section_citation_labels": [],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [
    "Official ISC page identifies the organisation but displays a temporary offline notice. No data availability is confirmed."
  ],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://www.isc.ac.uk/"
    ]
  }
}
```

<a id="src-024"></a>

### SRC-024 — GTN-P

```json
{
  "block_type": "source_record",
  "id": "SRC-024",
  "qualified_id": "OSDS:SRC-024",
  "name": "GTN-P",
  "original_inventory_id": "024",
  "original_inventory_row": "024\tGTN-P\tCircumpolar / global\tO02, O08",
  "domain": "D03",
  "related_domains": [],
  "observation_categories": [
    "O02",
    "O08"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Circumpolar / global",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://gtnp.arcticportal.org/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://gtnp.arcticportal.org/",
      "evidence_method": "official_page_content",
      "notes": "Official page identifies the named source. URL identity check only; datasets, access conditions and scientific classifications were not audited."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D03",
    "section_citation_labels": [],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://gtnp.arcticportal.org/"
    ]
  }
}
```

<a id="src-025"></a>

### SRC-025 — World Glacier Monitoring Service

```json
{
  "block_type": "source_record",
  "id": "SRC-025",
  "qualified_id": "OSDS:SRC-025",
  "name": "World Glacier Monitoring Service",
  "original_inventory_id": "025",
  "original_inventory_row": "025\tWorld Glacier Monitoring Service\tGlobal\tO03, O05, O08",
  "domain": "D03",
  "related_domains": [],
  "observation_categories": [
    "O03",
    "O05",
    "O08"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Global",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://wgms.ch/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://wgms.ch/",
      "evidence_method": "official_page_content",
      "notes": "Official page identifies the named source. URL identity check only; datasets, access conditions and scientific classifications were not audited."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D03",
    "section_citation_labels": [],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://wgms.ch/"
    ]
  }
}
```

<a id="src-026"></a>

### SRC-026 — GLORIA

```json
{
  "block_type": "source_record",
  "id": "SRC-026",
  "qualified_id": "OSDS:SRC-026",
  "name": "GLORIA",
  "original_inventory_id": "026",
  "original_inventory_row": "026\tGLORIA\tGlobal mountain sites\tO03, O05, O08",
  "domain": "D03",
  "related_domains": [],
  "observation_categories": [
    "O03",
    "O05",
    "O08"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Global mountain sites",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://www.gloria.ac.at/contact/office",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://www.gloria.ac.at/contact/office",
      "evidence_method": "official_indexed_excerpt",
      "notes": "Official GLORIA office page confirms network identity; initial homepage fetch timed out."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D03",
    "section_citation_labels": [],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [
    "Official GLORIA office page confirms network identity; initial homepage fetch timed out."
  ],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://www.gloria.ac.at/contact/office"
    ]
  }
}
```

<a id="src-027"></a>

### SRC-027 — USGS Water Data

```json
{
  "block_type": "source_record",
  "id": "SRC-027",
  "qualified_id": "OSDS:SRC-027",
  "name": "USGS Water Data",
  "original_inventory_id": "027",
  "original_inventory_row": "027\tUSGS Water Data\tUnited States\tO01, O02, O03, O08",
  "domain": "D04",
  "related_domains": [],
  "observation_categories": [
    "O01",
    "O02",
    "O03",
    "O08"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "United States",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://waterdata.usgs.gov/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://waterdata.usgs.gov/",
      "evidence_method": "official_page_content",
      "notes": "Official page identifies the named source. URL identity check only; datasets, access conditions and scientific classifications were not audited."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D04",
    "section_citation_labels": [
      "waterdata.usgs.gov",
      "+2"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://waterdata.usgs.gov/"
    ]
  }
}
```

<a id="src-028"></a>

### SRC-028 — Argo

```json
{
  "block_type": "source_record",
  "id": "SRC-028",
  "qualified_id": "OSDS:SRC-028",
  "name": "Argo",
  "original_inventory_id": "028",
  "original_inventory_row": "028\tArgo\tGlobal oceans\tO02, O04",
  "domain": "D04",
  "related_domains": [],
  "observation_categories": [
    "O02",
    "O04"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Global oceans",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://argo.ucsd.edu/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://argo.ucsd.edu/",
      "evidence_method": "official_page_content",
      "notes": "Official page identifies the named source. URL identity check only; datasets, access conditions and scientific classifications were not audited."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D04",
    "section_citation_labels": [
      "waterdata.usgs.gov",
      "+2"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://argo.ucsd.edu/"
    ]
  }
}
```

<a id="src-029"></a>

### SRC-029 — Copernicus Marine

```json
{
  "block_type": "source_record",
  "id": "SRC-029",
  "qualified_id": "OSDS:SRC-029",
  "name": "Copernicus Marine",
  "original_inventory_id": "029",
  "original_inventory_row": "029\tCopernicus Marine\tGlobal / Europe\tO02, O04, O08",
  "domain": "D04",
  "related_domains": [],
  "observation_categories": [
    "O02",
    "O04",
    "O08"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Global / Europe",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://marine.copernicus.eu/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://atmosphere.copernicus.eu/",
      "evidence_method": "official_indexed_excerpt",
      "notes": "Official Copernicus site links to the Marine service. Direct Marine homepage fetch was forbidden."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D04",
    "section_citation_labels": [
      "waterdata.usgs.gov",
      "+2"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [
    "Official Copernicus site links to the Marine service. Direct Marine homepage fetch was forbidden."
  ],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://marine.copernicus.eu/",
      "https://atmosphere.copernicus.eu/"
    ]
  }
}
```

<a id="src-030"></a>

### SRC-030 — EMODnet

```json
{
  "block_type": "source_record",
  "id": "SRC-030",
  "qualified_id": "OSDS:SRC-030",
  "name": "EMODnet",
  "original_inventory_id": "030",
  "original_inventory_row": "030\tEMODnet\tEuropean seas\tO02, O03, O04",
  "domain": "D04",
  "related_domains": [],
  "observation_categories": [
    "O02",
    "O03",
    "O04"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "European seas",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://emodnet.ec.europa.eu/en",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://emodnet.ec.europa.eu/en",
      "evidence_method": "official_page_content",
      "notes": "Official page identifies the named source. URL identity check only; datasets, access conditions and scientific classifications were not audited."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D04",
    "section_citation_labels": [
      "waterdata.usgs.gov",
      "+2"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://emodnet.ec.europa.eu/en"
    ]
  }
}
```

<a id="src-031"></a>

### SRC-031 — OceanOPS

```json
{
  "block_type": "source_record",
  "id": "SRC-031",
  "qualified_id": "OSDS:SRC-031",
  "name": "OceanOPS",
  "original_inventory_id": "031",
  "original_inventory_row": "031\tOceanOPS\tGlobal\tO02, O04",
  "domain": "D04",
  "related_domains": [],
  "observation_categories": [
    "O02",
    "O04"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Global",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://www.ocean-ops.org/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://www.ioc.unesco.org/en/joint-centre-oceanographic-marine-meteorological-observing-programme",
      "evidence_method": "official_indexed_excerpt",
      "notes": "Official IOC/UNESCO page identifies OceanOPS; direct service fetch was forbidden."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D04",
    "section_citation_labels": [
      "waterdata.usgs.gov",
      "+2"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [
    "Distinguish observing-platform metadata from observation data.",
    "Official IOC/UNESCO page identifies OceanOPS; direct service fetch was forbidden."
  ],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://www.ocean-ops.org/",
      "https://www.ioc.unesco.org/en/joint-centre-oceanographic-marine-meteorological-observing-programme"
    ]
  }
}
```

<a id="src-032"></a>

### SRC-032 — GOOS

```json
{
  "block_type": "source_record",
  "id": "SRC-032",
  "qualified_id": "OSDS:SRC-032",
  "name": "GOOS",
  "original_inventory_id": "032",
  "original_inventory_row": "032\tGOOS\tGlobal\tO02, O04",
  "domain": "D04",
  "related_domains": [],
  "observation_categories": [
    "O02",
    "O04"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Global",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://goosocean.org/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://goosocean.org/",
      "evidence_method": "official_page_content",
      "notes": "Official page identifies the named source. URL identity check only; datasets, access conditions and scientific classifications were not audited."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D04",
    "section_citation_labels": [
      "waterdata.usgs.gov",
      "+2"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [
    "Distinguish coordinating infrastructure from individual data services."
  ],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://goosocean.org/"
    ]
  }
}
```

<a id="src-033"></a>

### SRC-033 — US IOOS

```json
{
  "block_type": "source_record",
  "id": "SRC-033",
  "qualified_id": "OSDS:SRC-033",
  "name": "US IOOS",
  "original_inventory_id": "033",
  "original_inventory_row": "033\tUS IOOS\tUnited States\tO01, O02, O04",
  "domain": "D04",
  "related_domains": [],
  "observation_categories": [
    "O01",
    "O02",
    "O04"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "United States",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://ioos.noaa.gov/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://ioos.noaa.gov/",
      "evidence_method": "official_page_content",
      "notes": "Official page identifies the named source. URL identity check only; datasets, access conditions and scientific classifications were not audited."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D04",
    "section_citation_labels": [
      "waterdata.usgs.gov",
      "+2"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://ioos.noaa.gov/"
    ]
  }
}
```

<a id="src-034"></a>

### SRC-034 — GLOSS

```json
{
  "block_type": "source_record",
  "id": "SRC-034",
  "qualified_id": "OSDS:SRC-034",
  "name": "GLOSS",
  "original_inventory_id": "034",
  "original_inventory_row": "034\tGLOSS\tGlobal coastal\tO02, O08",
  "domain": "D04",
  "related_domains": [],
  "observation_categories": [
    "O02",
    "O08"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Global coastal",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://gloss-sealevel.org/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://gloss-sealevel.org/",
      "evidence_method": "official_page_content",
      "notes": "Official page identifies the named source. URL identity check only; datasets, access conditions and scientific classifications were not audited."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D04",
    "section_citation_labels": [
      "waterdata.usgs.gov",
      "+2"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://gloss-sealevel.org/"
    ]
  }
}
```

<a id="src-035"></a>

### SRC-035 — British Oceanographic Data Centre

```json
{
  "block_type": "source_record",
  "id": "SRC-035",
  "qualified_id": "OSDS:SRC-035",
  "name": "British Oceanographic Data Centre",
  "original_inventory_id": "035",
  "original_inventory_row": "035\tBritish Oceanographic Data Centre\tInternational / UK\tO02, O05, O08",
  "domain": "D04",
  "related_domains": [],
  "observation_categories": [
    "O02",
    "O05",
    "O08"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "International / UK",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://www.bodc.ac.uk/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://www.bodc.ac.uk/",
      "evidence_method": "official_page_content",
      "notes": "Official page identifies the named source. URL identity check only; datasets, access conditions and scientific classifications were not audited."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D04",
    "section_citation_labels": [
      "waterdata.usgs.gov",
      "+2"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://www.bodc.ac.uk/"
    ]
  }
}
```

<a id="src-036"></a>

### SRC-036 — USDA LTAR

```json
{
  "block_type": "source_record",
  "id": "SRC-036",
  "qualified_id": "OSDS:SRC-036",
  "name": "USDA LTAR",
  "original_inventory_id": "036",
  "original_inventory_row": "036\tUSDA LTAR\tUnited States\tO02, O03, O05, O08",
  "domain": "D05",
  "related_domains": [],
  "observation_categories": [
    "O02",
    "O03",
    "O05",
    "O08"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "United States",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://ltar.ars.usda.gov/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://ltar.ars.usda.gov/",
      "evidence_method": "official_page_content",
      "notes": "Official page identifies the named source. URL identity check only; datasets, access conditions and scientific classifications were not audited."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D05",
    "section_citation_labels": [
      "LTAR Network",
      "+2"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://ltar.ars.usda.gov/"
    ]
  }
}
```

<a id="src-037"></a>

### SRC-037 — USDA NASS

```json
{
  "block_type": "source_record",
  "id": "SRC-037",
  "qualified_id": "OSDS:SRC-037",
  "name": "USDA NASS",
  "original_inventory_id": "037",
  "original_inventory_row": "037\tUSDA NASS\tUnited States\tO03, O05, O08",
  "domain": "D05",
  "related_domains": [],
  "observation_categories": [
    "O03",
    "O05",
    "O08"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "United States",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://www.nass.usda.gov/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://www.nass.usda.gov/",
      "evidence_method": "official_page_content",
      "notes": "Official page identifies the named source. URL identity check only; datasets, access conditions and scientific classifications were not audited."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D05",
    "section_citation_labels": [
      "LTAR Network",
      "+2"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [
    "Check statistical estimates and surveys against physical observation scope."
  ],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://www.nass.usda.gov/"
    ]
  }
}
```

<a id="src-038"></a>

### SRC-038 — FAO AQUASTAT

```json
{
  "block_type": "source_record",
  "id": "SRC-038",
  "qualified_id": "OSDS:SRC-038",
  "name": "FAO AQUASTAT",
  "original_inventory_id": "038",
  "original_inventory_row": "038\tFAO AQUASTAT\tGlobal\tO03, O08",
  "domain": "D05",
  "related_domains": [],
  "observation_categories": [
    "O03",
    "O08"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Global",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://www.fao.org/aquastat/en/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://www.fao.org/aquastat/en/",
      "evidence_method": "official_page_content",
      "notes": "Official page identifies the named source. URL identity check only; datasets, access conditions and scientific classifications were not audited."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D05",
    "section_citation_labels": [
      "LTAR Network",
      "+2"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [
    "Check aggregated statistics and reported data against primary observations."
  ],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://www.fao.org/aquastat/en/"
    ]
  }
}
```

<a id="src-039"></a>

### SRC-039 — European Flood Awareness System

```json
{
  "block_type": "source_record",
  "id": "SRC-039",
  "qualified_id": "OSDS:SRC-039",
  "name": "European Flood Awareness System",
  "original_inventory_id": "039",
  "original_inventory_row": "039\tEuropean Flood Awareness System\tEurope\tO02, O08",
  "domain": "D05",
  "related_domains": [],
  "observation_categories": [
    "O02",
    "O08"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Europe",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://european-flood.emergency.copernicus.eu/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://publications.jrc.ec.europa.eu/repository/bitstream/JRC143951/JRC143951_01.pdf",
      "evidence_method": "official_indexed_excerpt",
      "notes": "Former efas.eu redirects to this Copernicus application. JRC documentation confirms the EFAS-IS URL. Forecasting service identity confirmed; observation product selection remains unresolved."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D05",
    "section_citation_labels": [
      "LTAR Network",
      "+2"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [
    "Review agricultural placement and separate forecasts from observations.",
    "Former efas.eu redirects to this Copernicus application. JRC documentation confirms the EFAS-IS URL. Forecasting service identity confirmed; observation product selection remains unresolved."
  ],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://european-flood.emergency.copernicus.eu/",
      "https://publications.jrc.ec.europa.eu/repository/bitstream/JRC143951/JRC143951_01.pdf"
    ]
  }
}
```

<a id="src-040"></a>

### SRC-040 — ICOS Ecosystem Stations

```json
{
  "block_type": "source_record",
  "id": "SRC-040",
  "qualified_id": "OSDS:SRC-040",
  "name": "ICOS Ecosystem Stations",
  "original_inventory_id": "040",
  "original_inventory_row": "040\tICOS Ecosystem Stations\tEurope\tO02, O03",
  "domain": "D05",
  "related_domains": [],
  "observation_categories": [
    "O02",
    "O03"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Europe",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://www.icos-cp.eu/measurements/ecosystem",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://www.icos-cp.eu/measurements/ecosystem",
      "evidence_method": "official_page_content",
      "notes": "Official ICOS ecosystem page confirms the station network. A specific agricultural station or dataset has not been selected."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D05",
    "section_citation_labels": [
      "LTAR Network",
      "+2"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [
    "Official ICOS ecosystem page confirms the station network. A specific agricultural station or dataset has not been selected."
  ],
  "candidate_relationships": [
    {
      "target_id": "OSDS:SRC-005",
      "relation": "possible_parent_or_collection_overlap",
      "status": "editorial_review_question_unverified"
    }
  ],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://www.icos-cp.eu/measurements/ecosystem"
    ]
  }
}
```

<a id="src-041"></a>

### SRC-041 — Lincoln Agricultural Robotics Datasets

```json
{
  "block_type": "source_record",
  "id": "SRC-041",
  "qualified_id": "OSDS:SRC-041",
  "name": "Lincoln Agricultural Robotics Datasets",
  "original_inventory_id": "041",
  "original_inventory_row": "041\tLincoln Agricultural Robotics Datasets\tUK / research sites\tO04, O05, O07",
  "domain": "D05",
  "related_domains": [],
  "observation_categories": [
    "O04",
    "O05",
    "O07"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "UK / research sites",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://lcas.lincoln.ac.uk/wp/research/data-sets-software/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://lcas.lincoln.ac.uk/wp/research/data-sets-software/",
      "evidence_method": "official_indexed_excerpt",
      "notes": "University of Lincoln L-CAS page lists multiple agricultural robotics datasets. The inventory label is treated as a collection, not one uniquely identified dataset."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D05",
    "section_citation_labels": [
      "LTAR Network",
      "+2"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [
    "University of Lincoln L-CAS page lists multiple agricultural robotics datasets. The inventory label is treated as a collection, not one uniquely identified dataset."
  ],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://lcas.lincoln.ac.uk/wp/research/data-sets-software/"
    ]
  }
}
```

<a id="src-042"></a>

### SRC-042 — AG-LOAM

```json
{
  "block_type": "source_record",
  "id": "SRC-042",
  "qualified_id": "OSDS:SRC-042",
  "name": "AG-LOAM",
  "original_inventory_id": "042",
  "original_inventory_row": "042\tAG-LOAM\tUS research dataset\tO03, O04, O05, O07",
  "domain": "D05",
  "related_domains": [],
  "observation_categories": [
    "O03",
    "O04",
    "O05",
    "O07"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "US research dataset",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://github.com/UCR-Robotics/AG-LOAM/blob/main/README.md",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://github.com/UCR-Robotics/AG-LOAM/blob/main/README.md",
      "evidence_method": "official_indexed_excerpt",
      "notes": "Maintainer README identifies AG-LOAM and describes its agricultural robot dataset. Dataset files were not downloaded or tested."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D05",
    "section_citation_labels": [
      "LTAR Network",
      "+2"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [
    "Maintainer README identifies AG-LOAM and describes its agricultural robot dataset. Dataset files were not downloaded or tested."
  ],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://github.com/UCR-Robotics/AG-LOAM/blob/main/README.md"
    ]
  }
}
```

<a id="src-043"></a>

### SRC-043 — OpenAQ

```json
{
  "block_type": "source_record",
  "id": "SRC-043",
  "qualified_id": "OSDS:SRC-043",
  "name": "OpenAQ",
  "original_inventory_id": "043",
  "original_inventory_row": "043\tOpenAQ\tGlobal\tO01, O02, O06",
  "domain": "D06",
  "related_domains": [],
  "observation_categories": [
    "O01",
    "O02",
    "O06"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Global",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://openaq.org/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://openaq.org/",
      "evidence_method": "official_page_content",
      "notes": "Official page identifies the named source. URL identity check only; datasets, access conditions and scientific classifications were not audited."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D06",
    "section_citation_labels": [
      "openaq.org",
      "+1"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://openaq.org/"
    ]
  }
}
```

<a id="src-044"></a>

### SRC-044 — openSenseMap

```json
{
  "block_type": "source_record",
  "id": "SRC-044",
  "qualified_id": "OSDS:SRC-044",
  "name": "openSenseMap",
  "original_inventory_id": "044",
  "original_inventory_row": "044\topenSenseMap\tInternational\tO01, O06, O07",
  "domain": "D06",
  "related_domains": [],
  "observation_categories": [
    "O01",
    "O06",
    "O07"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "International",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://opensensemap.org/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://opensensemap.org/",
      "evidence_method": "official_page_content",
      "notes": "Official application identity is visible but most content requires client-side rendering."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D06",
    "section_citation_labels": [
      "openaq.org",
      "+1"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [
    "Official application identity is visible but most content requires client-side rendering."
  ],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://opensensemap.org/"
    ]
  }
}
```

<a id="src-045"></a>

### SRC-045 — Sensor.Community

```json
{
  "block_type": "source_record",
  "id": "SRC-045",
  "qualified_id": "OSDS:SRC-045",
  "name": "Sensor.Community",
  "original_inventory_id": "045",
  "original_inventory_row": "045\tSensor.Community\tInternational\tO01, O06, O07",
  "domain": "D06",
  "related_domains": [],
  "observation_categories": [
    "O01",
    "O06",
    "O07"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "International",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://sensor.community/en/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://sensor.community/en/",
      "evidence_method": "official_page_content",
      "notes": "Official page identifies the named source. URL identity check only; datasets, access conditions and scientific classifications were not audited."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D06",
    "section_citation_labels": [
      "openaq.org",
      "+1"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://sensor.community/en/"
    ]
  }
}
```

<a id="src-046"></a>

### SRC-046 — Smart Citizen

```json
{
  "block_type": "source_record",
  "id": "SRC-046",
  "qualified_id": "OSDS:SRC-046",
  "name": "Smart Citizen",
  "original_inventory_id": "046",
  "original_inventory_row": "046\tSmart Citizen\tInternational\tO01, O06, O07",
  "domain": "D06",
  "related_domains": [],
  "observation_categories": [
    "O01",
    "O06",
    "O07"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "International",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://smartcitizen.me/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://docs.smartcitizen.me/",
      "evidence_method": "official_page_content",
      "notes": "Official Smart Citizen documentation confirms platform identity; homepage requires a supported browser."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D06",
    "section_citation_labels": [
      "openaq.org",
      "+1"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [
    "Official Smart Citizen documentation confirms platform identity; homepage requires a supported browser."
  ],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://smartcitizen.me/",
      "https://docs.smartcitizen.me/"
    ]
  }
}
```

<a id="src-047"></a>

### SRC-047 — EEA Datahub

```json
{
  "block_type": "source_record",
  "id": "SRC-047",
  "qualified_id": "OSDS:SRC-047",
  "name": "EEA Datahub",
  "original_inventory_id": "047",
  "original_inventory_row": "047\tEEA Datahub\tEurope\tO02, O08",
  "domain": "D06",
  "related_domains": [],
  "observation_categories": [
    "O02",
    "O08"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Europe",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://www.eea.europa.eu/en/datahub",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://www.eea.europa.eu/en/datahub",
      "evidence_method": "official_page_content",
      "notes": "Official page identifies the named source. URL identity check only; datasets, access conditions and scientific classifications were not audited."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D06",
    "section_citation_labels": [
      "openaq.org",
      "+1"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [
    "Select a specific measurement dataset; catalogue coverage is not measurement coverage."
  ],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://www.eea.europa.eu/en/datahub"
    ]
  }
}
```

<a id="src-048"></a>

### SRC-048 — London Datastore

```json
{
  "block_type": "source_record",
  "id": "SRC-048",
  "qualified_id": "OSDS:SRC-048",
  "name": "London Datastore",
  "original_inventory_id": "048",
  "original_inventory_row": "048\tLondon Datastore\tLondon\tO01, O02, O08",
  "domain": "D06",
  "related_domains": [],
  "observation_categories": [
    "O01",
    "O02",
    "O08"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "London",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://data.london.gov.uk/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://data.london.gov.uk/",
      "evidence_method": "official_page_content",
      "notes": "Official page identifies the named source. URL identity check only; datasets, access conditions and scientific classifications were not audited."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D06",
    "section_citation_labels": [
      "openaq.org",
      "+1"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [
    "Select a specific measurement dataset and document access."
  ],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://data.london.gov.uk/"
    ]
  }
}
```

<a id="src-049"></a>

### SRC-049 — Barcelona Open Data

```json
{
  "block_type": "source_record",
  "id": "SRC-049",
  "qualified_id": "OSDS:SRC-049",
  "name": "Barcelona Open Data",
  "original_inventory_id": "049",
  "original_inventory_row": "049\tBarcelona Open Data\tBarcelona\tO01, O02, O08",
  "domain": "D06",
  "related_domains": [],
  "observation_categories": [
    "O01",
    "O02",
    "O08"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Barcelona",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://opendata-ajuntament.barcelona.cat/data/es/dataset",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://datos.gob.es/es/iniciativas/open-data-bcn",
      "evidence_method": "official_indexed_excerpt",
      "notes": "Spanish government open-data catalogue identifies the municipal catalogue URL. Direct municipal homepage fetch timed out; catalogue functionality is not tested."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D06",
    "section_citation_labels": [
      "openaq.org",
      "+1"
    ],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [
    "Select a specific measurement dataset and document access.",
    "Spanish government open-data catalogue identifies the municipal catalogue URL. Direct municipal homepage fetch timed out; catalogue functionality is not tested."
  ],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://opendata-ajuntament.barcelona.cat/data/es/dataset",
      "https://datos.gob.es/es/iniciativas/open-data-bcn"
    ]
  }
}
```

<a id="src-050"></a>

### SRC-050 — Open Power System Data

```json
{
  "block_type": "source_record",
  "id": "SRC-050",
  "qualified_id": "OSDS:SRC-050",
  "name": "Open Power System Data",
  "original_inventory_id": "050",
  "original_inventory_row": "050\tOpen Power System Data\tEurope\tO02, O08",
  "domain": "D07",
  "related_domains": [],
  "observation_categories": [
    "O02",
    "O08"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Europe",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://open-power-system-data.org/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://open-power-system-data.org/",
      "evidence_method": "official_page_content",
      "notes": "Official page identifies the named source. URL identity check only; datasets, access conditions and scientific classifications were not audited."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D07",
    "section_citation_labels": [],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [
    "Separate measured, aggregated, estimated and modelled energy quantities."
  ],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://open-power-system-data.org/"
    ]
  }
}
```

<a id="src-051"></a>

### SRC-051 — ENTSO-E Transparency Platform

```json
{
  "block_type": "source_record",
  "id": "SRC-051",
  "qualified_id": "OSDS:SRC-051",
  "name": "ENTSO-E Transparency Platform",
  "original_inventory_id": "051",
  "original_inventory_row": "051\tENTSO-E Transparency Platform\tEurope\tO01, O02, O08",
  "domain": "D07",
  "related_domains": [],
  "observation_categories": [
    "O01",
    "O02",
    "O08"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Europe",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://www.entsoe.eu/data/transparency-platform/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://www.entsoe.eu/data/transparency-platform/",
      "evidence_method": "official_page_content",
      "notes": "Official ENTSO-E information page is used as a stable discovery route. Interactive platform access is not tested."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D07",
    "section_citation_labels": [],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [
    "Check whether O01 describes a documented measurement pathway rather than publication frequency.",
    "Official ENTSO-E information page is used as a stable discovery route. Interactive platform access is not tested."
  ],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://www.entsoe.eu/data/transparency-platform/"
    ]
  }
}
```

<a id="src-052"></a>

### SRC-052 — NREL Grid Research

```json
{
  "block_type": "source_record",
  "id": "SRC-052",
  "qualified_id": "OSDS:SRC-052",
  "name": "NREL Grid Research",
  "original_inventory_id": "052",
  "original_inventory_row": "052\tNREL Grid Research\tUnited States\tO02, O05, O07",
  "domain": "D07",
  "related_domains": [],
  "observation_categories": [
    "O02",
    "O05",
    "O07"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "United States",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://www.nlr.gov/grid/grid-data-tools",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://www.nlr.gov/grid/grid-data-tools",
      "evidence_method": "official_indexed_excerpt",
      "notes": "Current official NLR grid data/tools page is a scoped discovery route for the broad historical NREL Grid Research label. Original name retained; current naming and specific dataset selection need review."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D07",
    "section_citation_labels": [],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [
    "Broad research label; resolve provider identity and specific dataset.",
    "Current official NLR grid data/tools page is a scoped discovery route for the broad historical NREL Grid Research label. Original name retained; current naming and specific dataset selection need review."
  ],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://www.nlr.gov/grid/grid-data-tools"
    ]
  }
}
```

<a id="src-053"></a>

### SRC-053 — NASA Open Data

```json
{
  "block_type": "source_record",
  "id": "SRC-053",
  "qualified_id": "OSDS:SRC-053",
  "name": "NASA Open Data",
  "original_inventory_id": "053",
  "original_inventory_row": "053\tNASA Open Data\tInternational / US\tO02, O05, O07",
  "domain": "D07",
  "related_domains": [],
  "observation_categories": [
    "O02",
    "O05",
    "O07"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "International / US",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://data.nasa.gov/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://data.nasa.gov/",
      "evidence_method": "official_page_content",
      "notes": "Official page identifies the named source. URL identity check only; datasets, access conditions and scientific classifications were not audited."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D07",
    "section_citation_labels": [],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [
    "Broad portal label; select a specific dataset and establish physical measurement provenance."
  ],
  "candidate_relationships": [
    {
      "target_id": "OSDS:SRC-057",
      "relation": "possible_portal_overlap",
      "status": "editorial_review_question_unverified"
    }
  ],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://data.nasa.gov/"
    ]
  }
}
```

<a id="src-054"></a>

### SRC-054 — UCI Machine Learning Repository

```json
{
  "block_type": "source_record",
  "id": "SRC-054",
  "qualified_id": "OSDS:SRC-054",
  "name": "UCI Machine Learning Repository",
  "original_inventory_id": "054",
  "original_inventory_row": "054\tUCI Machine Learning Repository\tInternational datasets\tO05, O07",
  "domain": "D07",
  "related_domains": [],
  "observation_categories": [
    "O05",
    "O07"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "International datasets",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://archive.ics.uci.edu/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://archive.ics.uci.edu/",
      "evidence_method": "official_page_content",
      "notes": "Official page identifies the named source. URL identity check only; datasets, access conditions and scientific classifications were not audited."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D07",
    "section_citation_labels": [],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [
    "Repository membership does not establish physical observation provenance."
  ],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://archive.ics.uci.edu/"
    ]
  }
}
```

<a id="src-055"></a>

### SRC-055 — Zenodo

```json
{
  "block_type": "source_record",
  "id": "SRC-055",
  "qualified_id": "OSDS:SRC-055",
  "name": "Zenodo",
  "original_inventory_id": "055",
  "original_inventory_row": "055\tZenodo\tGlobal repository\tO05, O07",
  "domain": "D07",
  "related_domains": [],
  "observation_categories": [
    "O05",
    "O07"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Global repository",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://zenodo.org/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://zenodo.org/",
      "evidence_method": "official_page_content",
      "notes": "Repository landing page only; no individual research dataset selected."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D07",
    "section_citation_labels": [],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [
    "Repository membership does not establish physical observation provenance.",
    "Repository landing page only; no individual research dataset selected."
  ],
  "candidate_relationships": [
    {
      "target_id": "OSDS:SRC-058",
      "relation": "possible_same_repository",
      "status": "editorial_review_question_unverified"
    }
  ],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://zenodo.org/"
    ]
  }
}
```

<a id="src-056"></a>

### SRC-056 — PANGAEA

```json
{
  "block_type": "source_record",
  "id": "SRC-056",
  "qualified_id": "OSDS:SRC-056",
  "name": "PANGAEA",
  "original_inventory_id": "056",
  "original_inventory_row": "056\tPANGAEA\tGlobal\tO03, O05, O08",
  "domain": "D08",
  "related_domains": [],
  "observation_categories": [
    "O03",
    "O05",
    "O08"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Global",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://www.pangaea.de/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://www.pangaea.de/",
      "evidence_method": "official_page_content",
      "notes": "Official page identifies the named source. URL identity check only; datasets, access conditions and scientific classifications were not audited."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D08",
    "section_citation_labels": [],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://www.pangaea.de/"
    ]
  }
}
```

<a id="src-057"></a>

### SRC-057 — NASA Earthdata

```json
{
  "block_type": "source_record",
  "id": "SRC-057",
  "qualified_id": "OSDS:SRC-057",
  "name": "NASA Earthdata",
  "original_inventory_id": "057",
  "original_inventory_row": "057\tNASA Earthdata\tGlobal\tO02, O03, O05",
  "domain": "D08",
  "related_domains": [],
  "observation_categories": [
    "O02",
    "O03",
    "O05"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Global",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://www.earthdata.nasa.gov/home",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://www.earthdata.nasa.gov/home",
      "evidence_method": "official_indexed_excerpt",
      "notes": "Official indexed Earthdata home page confirms identity; initial root URL fetch was forbidden."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D08",
    "section_citation_labels": [],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [
    "Select a specific dataset; separate remote sensing, derived products and in-situ observations.",
    "Official indexed Earthdata home page confirms identity; initial root URL fetch was forbidden."
  ],
  "candidate_relationships": [
    {
      "target_id": "OSDS:SRC-053",
      "relation": "possible_portal_overlap",
      "status": "editorial_review_question_unverified"
    }
  ],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://www.earthdata.nasa.gov/home"
    ]
  }
}
```

<a id="src-058"></a>

### SRC-058 — Zenodo Research Datasets

```json
{
  "block_type": "source_record",
  "id": "SRC-058",
  "qualified_id": "OSDS:SRC-058",
  "name": "Zenodo Research Datasets",
  "original_inventory_id": "058",
  "original_inventory_row": "058\tZenodo Research Datasets\tGlobal\tO05, O07",
  "domain": "D08",
  "related_domains": [],
  "observation_categories": [
    "O05",
    "O07"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Global",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://zenodo.org/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://zenodo.org/",
      "evidence_method": "official_page_content",
      "notes": "Same repository landing page as SRC-055; original inventory entry retained pending consolidation review."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D08",
    "section_citation_labels": [],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [
    "Repository membership does not establish physical observation provenance.",
    "Same repository landing page as SRC-055; original inventory entry retained pending consolidation review."
  ],
  "candidate_relationships": [
    {
      "target_id": "OSDS:SRC-055",
      "relation": "possible_same_repository",
      "status": "editorial_review_question_unverified"
    }
  ],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://zenodo.org/"
    ]
  }
}
```

<a id="src-059"></a>

### SRC-059 — Mendeley Data

```json
{
  "block_type": "source_record",
  "id": "SRC-059",
  "qualified_id": "OSDS:SRC-059",
  "name": "Mendeley Data",
  "original_inventory_id": "059",
  "original_inventory_row": "059\tMendeley Data\tGlobal\tO05, O07",
  "domain": "D08",
  "related_domains": [],
  "observation_categories": [
    "O05",
    "O07"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Global",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://data.mendeley.com/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://data.mendeley.com/",
      "evidence_method": "official_page_content",
      "notes": "Official page identifies the named source. URL identity check only; datasets, access conditions and scientific classifications were not audited."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D08",
    "section_citation_labels": [],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [
    "Repository membership does not establish physical observation provenance."
  ],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://data.mendeley.com/"
    ]
  }
}
```

<a id="src-060"></a>

### SRC-060 — OpenML

```json
{
  "block_type": "source_record",
  "id": "SRC-060",
  "qualified_id": "OSDS:SRC-060",
  "name": "OpenML",
  "original_inventory_id": "060",
  "original_inventory_row": "060\tOpenML\tGlobal\tO05, O07",
  "domain": "D08",
  "related_domains": [],
  "observation_categories": [
    "O05",
    "O07"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Global",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://docs.openml.org/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://docs.openml.org/",
      "evidence_method": "official_indexed_excerpt",
      "notes": "Official OpenML documentation used because the application requires JavaScript. No specific physical-observation dataset selected."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D08",
    "section_citation_labels": [],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [
    "Check physical observation scope and O07 assignment for the selected dataset.",
    "Official OpenML documentation used because the application requires JavaScript. No specific physical-observation dataset selected."
  ],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://docs.openml.org/"
    ]
  }
}
```

<a id="src-061"></a>

### SRC-061 — AWS Open Data Registry

```json
{
  "block_type": "source_record",
  "id": "SRC-061",
  "qualified_id": "OSDS:SRC-061",
  "name": "AWS Open Data Registry",
  "original_inventory_id": "061",
  "original_inventory_row": "061\tAWS Open Data Registry\tGlobal\tO05, O07",
  "domain": "D08",
  "related_domains": [],
  "observation_categories": [
    "O05",
    "O07"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "Global",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://registry.opendata.aws/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://registry.opendata.aws/",
      "evidence_method": "official_page_content",
      "notes": "Official page identifies the named source. URL identity check only; datasets, access conditions and scientific classifications were not audited."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D08",
    "section_citation_labels": [],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [
    "Registry listing does not establish physical observation provenance or open redistribution rights."
  ],
  "candidate_relationships": [],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://registry.opendata.aws/"
    ]
  }
}
```

<a id="src-062"></a>

### SRC-062 — EarthScope Research Infrastructure

```json
{
  "block_type": "source_record",
  "id": "SRC-062",
  "qualified_id": "OSDS:SRC-062",
  "name": "EarthScope Research Infrastructure",
  "original_inventory_id": "062",
  "original_inventory_row": "062\tEarthScope Research Infrastructure\tUS / international\tO02, O05",
  "domain": "D08",
  "related_domains": [],
  "observation_categories": [
    "O02",
    "O05"
  ],
  "classification_reference": "osds.inventory-classification/0.1",
  "classification_status": "inherited_inventory_unverified",
  "coverage_as_supplied": "US / international",
  "description": null,
  "entity_type": null,
  "record_status": "candidate",
  "verification": {
    "status": "not_verified",
    "checked_at": null,
    "evidence": [],
    "scope": null
  },
  "source_urls": [
    {
      "url": "https://www.earthscope.org/",
      "role": "official_discovery_route",
      "origin": "web_research_2026-10-22_not_recovered_original_citation",
      "identity_check": "confirmed_official_source_or_scoped_collection",
      "checked_at": "2026-10-22",
      "evidence_url": "https://www.earthscope.org/",
      "evidence_method": "official_page_content",
      "notes": "Same EarthScope organisational landing page as SRC-022; original inventory entry retained pending consolidation review."
    }
  ],
  "url_status": "official_discovery_route_identified",
  "provenance": {
    "source_id": "P01",
    "inventory_domain_heading": "D08",
    "section_citation_labels": [],
    "citation_scope": "section_context_not_entry_verification",
    "url_enrichment_source_id": "P03"
  },
  "provider": {
    "name": null,
    "identifier": null
  },
  "observation_entities": {
    "platforms_or_stations": null,
    "sensors_or_instruments": null,
    "observed_properties": null,
    "features_of_interest": null,
    "observations": null,
    "samples": null,
    "datastreams": null,
    "measurement_units": null,
    "procedures": null
  },
  "spatial_extent": null,
  "temporal_extent": null,
  "sampling_frequency": null,
  "quality_control": null,
  "access": {
    "portal_url": null,
    "api_url": null,
    "download_url": null,
    "authentication": null,
    "licence": null,
    "redistribution_rights": null
  },
  "standards_compliance": null,
  "external_identifiers": [],
  "cross_database_links": [],
  "review_flags": [
    "Same EarthScope organisational landing page as SRC-022; original inventory entry retained pending consolidation review."
  ],
  "candidate_relationships": [
    {
      "target_id": "OSDS:SRC-022",
      "relation": "possible_same_provider",
      "status": "editorial_review_question_unverified"
    }
  ],
  "url_verification": {
    "status": "identity_checked_only",
    "checked_at": "2026-10-22",
    "scope": "Source or collection identity and discovery route; not original citation-link recovery, dataset validity, operational availability, category assignment, licence, calibration or complete metadata.",
    "evidence_urls": [
      "https://www.earthscope.org/"
    ]
  }
}
```

