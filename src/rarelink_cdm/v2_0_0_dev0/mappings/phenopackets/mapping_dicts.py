
"""
These are specific mappings from the Rarelink CDM v2.0.0 to the Phenopackets 
schema where specific codes are required. These mappings are used to convert
the codes in the CDM to the required codes in the Phenopackets schema.
"""

mapping_dicts = [
    {
        "name": "map_sex",
        "mapping": {
            "snomed_248152002": "FEMALE",
            "snomed_248153007": "MALE",
            "snomed_184115007": "UNKNOWN_SEX",
            "snomed_32570691000036108": "OTHER_SEX",
            "snomed_1220561009": "UNKNOWN_SEX"
        },
    },
    {
        "name": "map_karyotypic_sex",
        "mapping": {
            "snomed_261665006": "UNKNOWN_KARYOTYPE",
            "snomed_734875008": "XX",
            "snomed_734876009": "XY",
            "snomed_80427008": "XO",
            "snomed_65162001": "XXY",
            "snomed_35111009": "XXX",
            "snomed_403760006": "XXYY",
            "snomed_78317008": "XXXY",
            "snomed_10567003": "XXXX",
            "snomed_48930007": "XYY",
            "snomed_74964007": "OTHER_KARYOTYPE"
        },
    },
    {
        "name": "map_vital_status",
        "mapping": {
            "snomed_438949009": "ALIVE",
            "snomed_419099009": "DECEASED",
            "snomed_399307001": "UNKNOWN_STATUS",
            "snomed_185924006": "UNKNOWN_STATUS",
            "snomed_261665006": "UNKNOWN_STATUS"
        },
    },
    {
        "name": "map_disease_verification_status",
        "mapping": {
            "hl7fhir_unconfirmed": "",
            "hl7fhir_provisional": "",
            "hl7fhir_differential": "",
            "hl7fhir_confirmed": "false",
            "hl7fhir_refuted": "true",
            "hl7fhir_entered-in-error": ""
        },
    },
    {
        "name": "map_progress_status",
        "mapping": {
            "ga4gh_unknown_progress": "UNKNOWN_PROGRESS",
            "ga4gh_in_progress": "IN_PROGRESS",
            "ga4gh_completed": "COMPLETED",
            "ga4gh_solved": "SOLVED",
            "ga4gh_unsolved": "UNSOLVED"
        }
    },
    {
    "name": "map_interpretation_status",
    "mapping": {
        "ga4gh_unknown_status": "UNKNOWN_STATUS",
        "ga4gh_rejected": "REJECTED",
        "ga4gh_candidate": "CANDIDATE",
        "ga4gh_contributory": "CONTRIBUTORY",
        "ga4gh_causative": "CAUSATIVE"
        }
    },
    {
        "name": "map_acmg_classification",
        "mapping": {
            "loinc_la6668-3": "PATHOGENIC",
            "loinc_la26332-9": "LIKELY_PATHOGENIC",
            "loinc_la26333-7": "UNCERTAIN_SIGNIFICANCE",
            "loinc_la26334-5": "LIKELY_BENIGN",
            "loinc_la6675-8": "BENIGN",
            "loinc_la4489-6": "NOT_PROVIDED"
        }
    },
    {
        "name": "map_therapeutic_actionability",
        "mapping": {"ga4gh_unknown_actionability": "UNKNOWN_ACTIONABILITY",
                    "ga4gh_not_actionable": "NOT_ACTIONABLE",
                    "ga4gh_actionable": "ACTIONABLE",
        }
    },
    {
        "name": "phenotypic_feature_status",
        "mapping": {
            "snomed_410605003" : "false",
            "snomed_723511001" : "true"
        }
    }
]

# Utility function to fetch a mapping by name
def get_mapping_by_name(name, to_boolean=False):
    """
    Fetches a mapping by its name and optionally applies a boolean conversion.

    Args:
        name (str): The name of the mapping to fetch.
        to_boolean (bool): Whether to convert the mapping values to booleans.

    Returns:
        dict: The requested mapping, optionally converted to booleans.

    Raises:
        KeyError: If no mapping is found for the given name.
    """
    for mapping_dict in mapping_dicts:
        if mapping_dict["name"] == name:
            mapping = mapping_dict["mapping"]
            if to_boolean:
                # Apply boolean conversion to the mapping values
                return {key: value.lower() == "true" for key, value in mapping.items()}
            return mapping
    raise KeyError(f"No mapping found for name: {name}")