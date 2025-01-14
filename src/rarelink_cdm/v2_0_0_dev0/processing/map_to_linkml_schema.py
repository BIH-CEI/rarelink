from rarelink.utils.preprocessing.add_prefixes import add_prefix_to_code, process_prefix


def map_formal_criteria(entry):
    """
    Maps a flat REDCap entry to the FormalCriteria schema.
    """
    return {
        "snomed_422549004": entry.get("snomed_422549004", ""),
        "snomed_399423000": entry.get("snomed_399423000", ""),
        "rarelink_1_formal_criteria_complete": entry.get(
            "rarelink_1_formal_criteria_complete", "")
    }


def map_personal_information(entry):
    """
    Maps a flat REDCap entry to the PersonalInformation schema.
    """
    return {
        "snomed_184099003": entry.get("snomed_184099003", ""),
        "snomed_281053000": entry.get("snomed_281053000", ""),
        "snomed_1296886006": entry.get("snomed_1296886006", ""),
        "snomed_263495000": entry.get("snomed_263495000", ""),
        "snomed_370159000": entry.get("snomed_370159000", ""),
        "rarelink_2_personal_information_complete": entry.get(
            "rarelink_2_personal_information_complete", "")
    }


def map_patient_status(entry):
    """
    Maps a flat REDCap entry to the PatientStatus schema.
    """
    def convert_to_boolean(value):
        """
        Convert SNOMED codes for yes/no to Boolean values.
        """
        yes_no_mapping = {
            "snomed_373066001": True,  # Yes
            "snomed_373067005": False  # No
        }
        return yes_no_mapping.get(value, None)

    return {
        "patient_status_date": entry.get("patient_status_date", ""),
        "snomed_278844005": entry.get("snomed_278844005", ""),
        "snomed_398299004": entry.get("snomed_398299004", ""),
        "snomed_184305005": add_prefix_to_code(entry.get(
            "snomed_184305005", ""), "ICD10CM"),
        "snomed_105727008": entry.get("snomed_105727008", ""),
        "snomed_412726003": entry.get("snomed_412726003", ""),
        "snomed_723663001": convert_to_boolean(entry.get(
            "snomed_723663001", "")),
        "rarelink_3_patient_status_complete": entry.get(
            "rarelink_3_patient_status_complete", "")
    }


def map_care_pathway(entry):
    """
    Maps a flat REDCap entry to the CarePathway schema.
    """
    return {
        "hl7fhir_enc_period_start": entry.get("hl7fhir_enc_period_start", ""),
        "hl7fhir_enc_period_end": entry.get("hl7fhir_enc_period_end", ""),
        "snomed_305058001": entry.get("snomed_305058001", ""),
        "hl7fhir_encounter_class": entry.get("hl7fhir_encounter_class", ""),
        "rarelink_4_care_pathway_complete": entry.get(
            "rarelink_4_care_pathway_complete", "")
    }

def map_disease(entry):
    """
    Maps a flat REDCap entry to the Disease schema.
    """
    return {
        "disease_coding": entry.get("disease_coding", ""),
        "snomed_64572001_mondo": entry.get("snomed_64572001_mondo", ""),
        "snomed_64572001_ordo": entry.get("snomed_64572001_ordo", ""),
        "snomed_64572001_icd10cm": add_prefix_to_code(entry.get(
            "snomed_64572001_icd10cm", ""), "ICD10CM"),
        "snomed_64572001_icd11": add_prefix_to_code(entry.get(
            "snomed_64572001_icd11", ""), "ICD11"),
        "snomed_64572001_omim_p": add_prefix_to_code(entry.get(
            "snomed_64572001_omim_p", ""), "OMIM"),
        "loinc_99498_8": entry.get("loinc_99498_8", ""),
        "snomed_424850005": entry.get("snomed_424850005", ""),
        "snomed_298059007": entry.get("snomed_298059007", ""),
        "snomed_423493009": entry.get("snomed_423493009", ""),
        "snomed_432213005": entry.get("snomed_432213005", ""),
        "snomed_363698007": add_prefix_to_code(entry.get("snomed_363698007", ""),
                                               "SNOMEDCT"),
        "snomed_263493007": entry.get("snomed_263493007", ""),
        "snomed_246112005": entry.get("snomed_246112005", ""),
        "rarelink_5_disease_complete": entry.get("rarelink_5_disease_complete", "")
    }

def map_genetic_findings(entry):
    """
    Maps a flat REDCap entry to the GeneticFindings schema.
    """
    
    def convert_to_boolean(value):
        """
        Convert SNOMED codes for yes/no to Boolean values.
        """
        yes_no_mapping = {
            "yes": True,  # Yes
            "no": False  # No
        }
        return yes_no_mapping.get(value, None)

    return {
        "genetic_diagnosis_code": entry.get("genetic_diagnosis_code", ""),
        "snomed_106221001_mondo": entry.get("snomed_106221001_mondo", ""),
        "snomed_106221001_omim_p": add_prefix_to_code(entry.get(
            "snomed_106221001_omim_p", ""), "OMIM"),
        "ga4gh_progress_status": entry.get("ga4gh_progress_status", ""),
        "ga4gh_interp_status": entry.get("ga4gh_interp_status", ""),
        "loinc_81304_8": entry.get("loinc_81304_8", ""),
        "loinc_62374_4": entry.get("loinc_62374_4", ""),
        "loinc_lp7824_8": entry.get("loinc_lp7824_8", ""),
        "variant_expression": entry.get("variant_expression", ""),
        "loinc_81290_9": entry.get("loinc_81290_9", ""),
        "loinc_48004_6": entry.get("loinc_48004_6", ""),
        "loinc_48005_3": entry.get("loinc_48005_3", ""),
        "variant_validation": convert_to_boolean(entry.get(
            "variant_validation", "")),
        "loinc_48018_6": entry.get("loinc_48018_6", ""),
        "loinc_53034_5": entry.get("loinc_53034_5", ""),
        "loinc_53034_5_other": add_prefix_to_code(entry.get(
            "loinc_53034_5_other", ""), "LOINC"),
        "loinc_48002_0": entry.get("loinc_48002_0", ""),
        "loinc_48019_4": entry.get("loinc_48019_4", ""),
        "loinc_48019_4_other": add_prefix_to_code(entry.get(
            "loinc_48019_4_other", ""), "LOINC"),
        "loinc_53037_8": entry.get("loinc_53037_8", ""),
        "ga4gh_therap_action": entry.get("ga4gh_therap_action", ""),
        "loinc_93044_6": entry.get("loinc_93044_6", ""),
        "rarelink_6_1_genetic_findings_complete": entry.get(
            "rarelink_6_1_genetic_findings_complete", "")
    }

def map_phenotypic_feature(entry):
    """
    Maps a flat REDCap entry to the PhenotypicFeature schema.
    """
    return {
        "snomed_8116006": entry.get("snomed_8116006", ""),
        "snomed_363778006": entry.get("snomed_363778006", ""),
        "snomed_8116006_onset": entry.get("snomed_8116006_onset", ""),
        "snomed_8116006_resolution": entry.get("snomed_8116006_resolution", ""),
        "hp_0003674": entry.get("hp_0003674", ""),
        "hp_0011008": entry.get("hp_0011008", ""),
        "hp_0012824": entry.get("hp_0012824", ""),
        "hp_0012823_hp1": entry.get("hp_0012823_hp1", ""),
        "hp_0012823_hp2": entry.get("hp_0012823_hp2", ""),
        "hp_0012823_hp3": entry.get("hp_0012823_hp3", ""),
        "hp_0012823_ncbitaxon": add_prefix_to_code(
            entry.get("hp_0012823_ncbitaxon", ""), "NCBITAXON"),
        "hp_0012823_snomed": add_prefix_to_code(
            entry.get("hp_0012823_snomed", ""), "SNOMEDCT"),
        "phenotypicfeature_evidence": entry.get("phenotypicfeature_evidence", ""),
        "rarelink_6_2_phenotypic_feature_complete": entry.get(
            "rarelink_6_2_phenotypic_feature_complete", "")
    }


def map_measurements(entry):
    """
    Maps a flat REDCap entry to the Measurement schema with appropriate prefixes
    and additional fields.
    """
    return {
        "measurement_category": entry.get("measurement_category", ""),
        "measurement_status": entry.get("measurement_status", ""),
        "ncit_c60819": add_prefix_to_code(entry.get("ncit_c60819", ""), "LOINC"),
        "ln_85353_1": add_prefix_to_code(entry.get(
            "ln_85353_1", ""), "LOINC"),
        "ln_85353_1_other": entry.get(
            "ln_85353_1_other", ""),
        "ncit_c25712": float(entry.get(
            "ncit_c25712", 0)) if entry.get("ncit_c25712") else None,
        "ncit_c92571": process_prefix(entry.get("ncit_c92571", ""), "UO"),
        "ncit_c41255": entry.get( "ncit_c41255", ""),
        "ncit_c82577": entry.get("ncit_c82577", ""),
        "snomed_122869004_ncit": entry.get(
            "snomed_122869004_ncit", ""),
        "snomed_122869004_snomed": add_prefix_to_code(entry.get(
            "snomed_122869004_snomed", ""), "SNOMEDCT"),
        "snomed_122869004": add_prefix_to_code(entry.get(
            "snomed_122869004", ""), "SNOMEDCT"),
        "snomed_122869004_bodysite": add_prefix_to_code(entry.get(
            "snomed_122869004_bodysite", ""), "SNOMEDCT"),
        "snomed_122869004_status": entry.get("snomed_122869004_status", ""),
        "rarelink_6_3_measurements_complete": entry.get(
            "rarelink_6_3_measurements_complete", ""),
    }

def map_family_history(entry):
    """
    Maps a flat REDCap entry to the FamilyHistory schema.
    """
    return {
        "family_history_pseudonym": entry.get("family_history_pseudonym", ""),
        "propositus": entry.get("snomed_64245008", ""),
        "relationship_to_index_case": entry.get("snomed_408732007", ""),
        "consanguinity": entry.get("snomed_842009", ""),
        "family_member_relationship": entry.get("snomed_444018008", ""),
        "family_member_record_status": entry.get("hl7fhir_fmh_status", ""),
        "family_member_sex": entry.get("loinc_54123_5", ""),
        "family_member_age": int(entry.get("loinc_54141_7", 0)) if entry.get(
            "loinc_54141_7") else None,
        "family_member_dob": entry.get("loinc_54124_3", ""),
        "family_member_deceased": entry.get("snomed_740604001", ""),
        "family_member_cause_of_death": add_prefix_to_code(entry.get(
            "loinc_54112_8", ""), "ICD10CM"),
        "family_member_deceased_age": int(entry.get(
            "loinc_92662_6", 0)) if entry.get("loinc_92662_6") else None,
        "family_member_disease": entry.get("loinc_75315_2", ""),
        "rarelink_6_4_family_history_complete": entry.get(
            "rarelink_6_4_family_history_complete", "")
    }

def map_consent(entry):
    """
    Maps a flat REDCap entry to the Consent schema.
    """
    return {
        "consent_status": entry.get("snomed_309370004", ""),
        "consent_date": entry.get("hl7fhir_consent_datetime", ""),
        "health_policy_monitoring": entry.get("snomed_386318002", ""),
        "agreement_to_contact": entry.get("rarelink_consent_contact", ""),
        "consent_to_reuse_data": entry.get("rarelink_consent_data", ""),
        "biological_sample": entry.get("snomed_123038009", ""),
        "biobank_link": entry.get("rarelink_biobank_link", ""),
        "rarelink_7_consent_complete": entry.get(
            "rarelink_7_consent_complete", "")
    }

def map_disability(entry):
    """
    Maps a flat REDCap entry to the Disability schema.
    """
    return {
        "icf_score": entry.get("rarelink_icf_score", ""),
        "rarelink_8_disability_complete": entry.get(
            "rarelink_8_disability_complete", "")
    }


MAPPING_FUNCTIONS = {
    "formal_criteria": map_formal_criteria,
    "personal_information": map_personal_information,
    "patient_status": map_patient_status,
    "care_pathway": map_care_pathway,
    "disease": map_disease,
    "genetic_findings": map_genetic_findings,
    "phenotypic_feature": map_phenotypic_feature,
    "measurements": map_measurements,
    "family_history": map_family_history,
    "consent": map_consent,
    "disability": map_disability
}