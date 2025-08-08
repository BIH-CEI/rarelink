# src/rarelink/cdm/schema_template.py
from __future__ import annotations
from typing import Dict, Any

def base_schema() -> Dict[str, Any]:
    return {
        "id": "https://github.com/BIH-CEI/RareLink/code_systems_data",
        "name": "code_systems_data",
        "prefixes": {
            "linkml": "https://w3id.org/linkml/",
            "rarelink": "https://github.com/BIH-CEI/rarelink/",
        },
        "imports": [
            "linkml:types",
            "rarelink_types", 
        ],
        "default_prefix": "rarelink",
        "default_range": "string",
        "enums": {
            "NCBITaxon": {
                "description": "NCBI organismal classification",
                "code_set": "https://www.ncbi.nlm.nih.gov/taxonomy",
                "code_set_version": "",
            },
            "SNOMEDCT": {
                "description": "SNOMED CT",
                "code_set": "http://snomed.info/sct",
                "code_set_version": "",
            },
            "MONDO": {
                "description": "Monarch Disease Ontology",
                "code_set": "https://purl.obolibrary.org/obo/MONDO/",
                "code_set_version": "",
            },
            "HP": {
                "description": "Human Phenotype Ontology",
                "code_set": "https://www.human-phenotype-ontology.org",
                "code_set_version": "",
            },
            "LOINC": {
                "description": "Logical Observation Identifiers Names and Codes",
                "code_set": "http://loinc.org",
                "code_set_version": "",
            },
            "OMIM": {
                "description": "Online Mendelian Inheritance",
                "code_set": "https://omim.org/",
                "code_set_version": "",
            },
            "ORPHA": {
                "description": "Orphanet Rare Disease Ontology",
                "code_set": "https://www.orpha.net/",
                "code_set_version": "",
            },
            "NCIT": {
                "description": "NCI Thesaurus OBO Edition",
                "code_set": "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl",
                "code_set_version": "",
            },
            "UO": {
                "description": "Units of Measurement Ontology",
                "code_set": "https://www.ontobee.org/ontology/UO",
                "code_set_version": "",
            },
            "HGNC": {
                "description": "HUGO Gene Nomenclature Committee",
                "code_set": "https://www.genenames.org/",
                "code_set_version": "",
            },
            "HGVS": {
                "description": "Human Genome Variation Society",
                "code_set": "http://varnomen.hgvs.org/",
                "code_set_version": "",
            },
            "GA4GH": {
                "description": "Global Alliance for Genomics and Health",
                "code_set": "https://www.ga4gh.org/",
                "code_set_version": "",
            },
            "HL7FHIR": {
                "description": "Health Level 7 Fast Healthcare Interoperability Resources",
                "code_set": "https://www.hl7.org/fhir",
                "code_set_version": "",
            },
            "ICD11": {
                "description": "International Classification of Diseases, Eleventh Revision",
                "code_set": "https://icd.who.int/en",
                "code_set_version": "",
            },
            "ICD10CM": {
                "description": "International Classification of Diseases, Tenth Revision, Clinical Modification",
                "code_set": "https://icd10cmtool.cdc.gov/",
                "code_set_version": "",
            },
            "ICD10GM": {
                "description": "International Classification of Diseases, Tenth Revision, German Modification",
                "code_set": "https://www.bfarm.de/EN/Code-systems/Classifications/ICD/ICD-10-GM/_node.html",
                "code_set_version": "",
            },
            "SO": {
                "description": "Sequence types and features ontology",
                "code_set": "https://www.sequenceontology.org/",
                "code_set_version": "",
            },
            "GENO": {
                "description": "GENO - The Genotype Ontology",
                "code_set": "https://www.genoontology.org/",
                "code_set_version": "",
            },
            "ISO3166": {
                "description": "ISO 3166-1:2020(en) alpha-2 and alpha-3 country codes",
                "code_set": "https://www.iso.org/iso-3166-country-codes.html",
                "code_set_version": "",
            },
            "ICF": {
                "description": "International Classification of Functioning, Disability and Health",
                "code_set": "https://www.who.int/classifications/icf/en/",
                "code_set_version": "",
            },
        },
        "classes": {
            "CodeSystemsContainer": {
                "description": "A container class for all code systems used in RareLink.",
                "attributes": {
                    "ncbi_taxon": {
                        "description": "NCBI organismal classification",
                        "range": "NCBITaxon",
                        "required": True,
                    },
                    "SNOMEDCT": {
                        "description": "SNOMED CT",
                        "range": "SNOMEDCT",
                        "required": True,
                    },
                    "mondo": {
                        "description": "Monarch Disease Ontology",
                        "range": "MONDO",
                        "required": True,
                    },
                    "hpo": {
                        "description": "Human Phenotype Ontology",
                        "range": "HP",
                        "required": True,
                    },
                    "loinc": {
                        "description": "Logical Observation Identifiers Names and Codes",
                        "range": "LOINC",
                        "required": True,
                    },
                    "omim": {
                        "description": "Online Mendelian Inheritance",
                        "range": "OMIM",
                        "required": True,
                    },
                    "orpha": {
                        "description": "Orphanet Rare Disease Ontology",
                        "range": "ORPHA",
                        "required": True,
                    },
                    "ncit": {
                        "description": "NCI Thesaurus OBO Edition",
                        "range": "NCIT",
                        "required": True,
                    },
                    "uo": {
                        "description": "Units of Measurement Ontology",
                        "range": "UO",
                        "required": True,
                    },
                    "hgnc": {
                        "description": "HUGO Gene Nomenclature Committee",
                        "range": "HGNC",
                        "required": True,
                    },
                    "hgvs": {
                        "description": "Human Genome Variation Society",
                        "range": "HGVS",
                        "required": True,
                    },
                    "ga4gh": {
                        "description": "Global Alliance for Genomics and Health",
                        "range": "GA4GH",
                        "required": True,
                    },
                    "hl7fhir": {
                        "description": "Health Level 7 Fast Healthcare Interoperability Resources",
                        "range": "HL7FHIR",
                        "required": True,
                    },
                    "icd11": {
                        "description": "International Classification of Diseases, Eleventh Revision",
                        "range": "ICD11",
                        "required": True,
                    },
                    "icd10cm": {
                        "description": "International Classification of Diseases, Tenth Revision, Clinical Modification",
                        "range": "ICD10CM",
                        "required": True,
                    },
                    "icd10gm": {
                        "description": "International Classification of Diseases, Tenth Revision, German Modification",
                        "range": "ICD10GM",
                        "required": True,
                    },
                    "so": {
                        "description": "Sequence types and features ontology",
                        "range": "SO",
                        "required": True,
                    },
                    "geno": {
                        "description": "GENO - The Genotype Ontology",
                        "range": "GENO",
                        "required": True,
                    },
                    "iso3166": {
                        "description": "ISO 3166-1:2020(en) alpha-2 and alpha-3 country codes",
                        "range": "ISO3166",
                        "required": True,
                    },
                    "icf": {
                        "description": "International Classification of Functioning, Disability and Health",
                        "range": "ICF",
                        "required": True,
                    },
                },
            }
        },
    }
