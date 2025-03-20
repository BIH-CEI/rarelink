"""
Mapping function for the GeneticFindings schema.

This module defines a function to map flat REDCap data entries to the
GeneticFindings schema defined in the RareLink-CDM LinkML model.

Field mappings are explicitly defined, and additional processing is applied
for Boolean conversions and prefix additions.
"""

from rarelink.utils.processing.codes import add_prefix_to_code

"""
Mapping function for genetic findings REDCap data to LinkML format.
"""

def map_genetic_findings(record):
    """
    Map REDCap record data to the GeneticFindings LinkML class format.
    
    Args:
        record (dict): The REDCap record data
        
    Returns:
        dict: The mapped data in LinkML format
    """
    # Fields that might contain HGNC identifiers
    hgnc_fields = ["loinc_48018_6"]
    
    return {
        "g_iei_deficiency": record.get("g_iei_deficiency", ""),
        "other_non_g_iei": record.get("other_non_g_iei", ""),
        "g_other_iei_deficiency": record.get("g_other_iei_deficiency", ""),
        "ga4gh_progress_status": record.get("ga4gh_progress_status", ""),
        "ga4gh_interp_status": record.get("ga4gh_interp_status", ""),
        "loinc_81304_8": record.get("loinc_81304_8", ""),
        "loinc_62374_4": record.get("loinc_62374_4", ""),
        "loinc_lp7824_8": record.get("loinc_lp7824_8", ""),
        "variant_expression": record.get("variant_expression", ""),
        "loinc_81290_9": record.get("loinc_81290_9", ""),
        "loinc_48004_6": record.get("loinc_48004_6", ""),
        "loinc_48005_3": record.get("loinc_48005_3", ""),
        "variant_validation": record.get("variant_validation", ""),
        "loinc_48018_6": record.get("loinc_48018_6", ""),
        "loinc_53034_5": record.get("loinc_53034_5", ""),
        "loinc_53034_5_other": record.get("loinc_53034_5_other", ""),
        "loinc_48002_0": record.get("loinc_48002_0", ""),
        "loinc_48019_4": record.get("loinc_48019_4", ""),
        "loinc_48019_4_other": record.get("loinc_48019_4_other", ""),
        "loinc_53037_8": record.get("loinc_53037_8", ""),
        "ga4gh_therap_action": record.get("ga4gh_therap_action", ""),
        "loinc_93044_6": record.get("loinc_93044_6", ""),
        "rarelink_6_1_genetic_findings_complete": record.get("rarelink_6_1_genetic_findings_complete", "0")
    }
    

# Additional processing for Boolean conversion and prefix additions.
ADDITIONAL_PROCESSING = {
    "snomedct_106221001_omim_p": lambda x: add_prefix_to_code(x, "OMIM"),
    "variant_validation": lambda x: {"yes": True, "no": False}.get(x.lower(), None),
    "loinc_53034_5_other": lambda x: add_prefix_to_code(x, "LOINC"),
    "loinc_48019_4_other": lambda x: add_prefix_to_code(x, "LOINC")
}
