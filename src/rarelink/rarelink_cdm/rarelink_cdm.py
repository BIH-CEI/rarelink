from importlib import resources
from pathlib import Path
from typing import Union
from phenopacket_mapper.data_standards import DataModel, DataField
from rarelink.rarelink_cdm.rarelink_cdm_vs import RARELINK_CDM_V2_0_0_VS as VS

RARELINK_CDM_V2_0_0 = DataModel(
    data_model_name="RareLink Common Data Model 2.0",
    resources=resources,
    fields=[
        # 1. Formal Criteria
        DataField(section="1. Formal Criteria", ordinal="1.1", 
                   name="Pseudonym", value_set=VS.vs_1_1),
        DataField(section="1. Formal Criteria", ordinal="1.2", 
                   name="Date of Admission", value_set=VS.vs_1_2),

        # 2. Personal Information
        DataField(section="2. Personal Information", ordinal="2.1", 
                   name="Date of Birth", value_set=VS.vs_2_1),
        DataField(section="2. Personal Information", ordinal="2.2", 
                   name="Sex at Birth", value_set=VS.vs_2_2),
        DataField(section="2. Personal Information", ordinal="2.3", 
                   name="Karyotypic Sex", value_set=VS.vs_2_3),
        DataField(section="2. Personal Information", ordinal="2.4", 
                   name="Gender Identity", value_set=VS.vs_2_4),
        DataField(section="2. Personal Information", ordinal="2.5", 
                   name="Country of Birth", value_set=VS.vs_2_5),

        # 3. Patient Status
        DataField(section="3. Patient Status", ordinal="3.1", 
                   name="Vital Status", value_set=VS.vs_3_1),
        DataField(section="3. Patient Status", ordinal="3.2", 
                   name="Time of Death", value_set=VS.vs_3_2),
        DataField(section="3. Patient Status", ordinal="3.3", 
                   name="Cause of Death", value_set=VS.vs_3_3),
        DataField(section="3. Patient Status", ordinal="3.4", 
                   name="Age Category", value_set=VS.vs_3_4),
        DataField(section="3. Patient Status", ordinal="3.5", 
                   name="Length of Gestation at Birth", value_set=VS.vs_3_5),
        DataField(section="3. Patient Status", ordinal="3.6", 
                   name="Undiagnosed RD Case", value_set=VS.vs_3_6),

        # 7. Consent
        DataField(section="7. Consent", ordinal="7.1", 
                  name="Consent Status", value_set=VS.vs_7_1),
        DataField(section="7. Consent", ordinal="7.2", 
                  name="Consent Date", value_set=VS.vs_7_2),
        DataField(section="7. Consent", ordinal="7.3", 
                  name="Health Policy Monitoring", value_set=VS.vs_7_3),
        DataField(section="7. Consent", ordinal="7.4", name="Agreement to be contacted for research purposes", value_set=VS.vs_7_4), 
        DataField(section="7. Consent", ordinal="7.5", 
                  name="Consent to the reuse of data", 
                  value_set=VS.vs_7_5),
        DataField(section="7. Consent", ordinal="7.6", 
                  name="Biological sample", 
                  value_set=VS.vs_7_6),
        DataField(section="7. Consent", ordinal="7.7", 
                  name="Link to a biobank", 
                  value_set=VS.vs_7_7),
    
        # 8. Classification of functioning / disability
        DataField(section="8. Classification", ordinal="8.1", 
                  name="Classification of functioning / disability", 
                  value_set=VS.vs_8_1), 
    ]
)
# repeating fields:
# 4. Care Pathway
def append_care_pathway_fields(data_model, n=9999):
    for i in range(n):
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="4. Care Pathway", ordinal="4.1", 
                      name=f"Encounter Start_{i}", value_set=VS.vs_4_1)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="4. Care Pathway", ordinal="4.2", 
                      name=f"Encounter End_{i}", value_set=VS.vs_4_2)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="4. Care Pathway", ordinal="4.3", 
                      name=f"Encounter Status_{i}", value_set=VS.vs_4_3)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="4. Care Pathway", ordinal="4.4", 
                      name=f"Encounter Class_{i}", value_set=VS.vs_4_4)
        )

# 5. Disease
def append_disease_fields(data_model, n=9999):
    for i in range(n):
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="5. Disease", ordinal="5.1A", 
                      name=f"Disease MONDO_{i}", value_set=VS.vs_5_1a)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="5. Disease", ordinal="5.1B", 
                      name=f"Disease ORDO_{i}", value_set=VS.vs_5_1b)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="5. Disease", ordinal="5.1C", 
                      name=f"Disease ICD10CM_{i}", value_set=VS.vs_5_1c)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="5. Disease", ordinal="5.1D", 
                      name=f"Disease ICD11_{i}", value_set=VS.vs_5_1d)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="5. Disease", ordinal="5.1E", 
                      name=f"Disease OMIM_P_{i}", value_set=VS.vs_5_1e)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="5. Disease", ordinal="5.2", 
                      name=f"Verification Status_{i}", value_set=VS.vs_5_2)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="5. Disease", ordinal="5.3", 
                      name=f"Age at Onset_{i}", value_set=VS.vs_5_3)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="5. Disease", ordinal="5.4", 
                      name=f"Date of Onset_{i}", value_set=VS.vs_5_4)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="5. Disease", ordinal="5.5", 
                      name=f"Age at Diagnosis_{i}", value_set=VS.vs_5_5)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="5. Disease", ordinal="5.6", 
                      name=f"Date of Diagnosis_{i}", value_set=VS.vs_5_6)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="5. Disease", ordinal="5.7", 
                      name=f"Body Site_{i}", value_set=VS.vs_5_7)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="5. Disease", ordinal="5.8", 
                      name=f"Clinical Status_{i}", value_set=VS.vs_5_8)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="5. Disease", ordinal="5.9", 
                      name=f"Severity_{i}", value_set=VS.vs_5_9)
        )

# 6.1 Genetic Findings
def append_genetic_findings_fields(data_model, n=9999):
    for i in range(n):
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.1 Genetic Findings", ordinal="6.1.1", 
                      name=f"Genomic Diagnosis_MONDO_{i}", value_set=VS.vs_6_1_1a)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.1 Genetic Findings", ordinal="6.1.1", 
                      name=f"Genomic Diagnosis_OMIM_P_{i}", value_set=VS.vs_6_1_1b)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.1 Genetic Findings", ordinal="6.1.2", 
                      name=f"Progress Status of Interpretation_{i}", value_set=VS.vs_6_1_2)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.1 Genetic Findings", ordinal="6.1.3", 
                      name=f"Interpretation Status_{i}", value_set=VS.vs_6_1_3)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.1 Genetic Findings", ordinal="6.1.4", 
                      name=f"Structural Variant Analysis Method_{i}", value_set=VS.vs_6_1_4)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.1 Genetic Findings", ordinal="6.1.4a", 
                      name=f"Structural Variant Analysis Method_other_{i}", value_set=VS.vs_6_1_4a)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.1 Genetic Findings", ordinal="6.1.5", 
                      name=f"Reference Genome_{i}", value_set=VS.vs_6_1_5)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.1 Genetic Findings", ordinal="6.1.6", 
                      name=f"Genetic Mutation String_{i}", value_set=VS.vs_6_1_6)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.1 Genetic Findings", ordinal="6.1.7", 
                      name=f"Genomic DNA Change [g.HGVS]_{i}", value_set=VS.vs_6_1_7)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.1 Genetic Findings", ordinal="6.1.8", 
                      name=f"Sequence DNA Change [c.HGVS]_{i}", value_set=VS.vs_6_1_8)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.1 Genetic Findings", ordinal="6.1.9", 
                      name=f"Amino Acid Change [p.HGVS]_{i}", value_set=VS.vs_6_1_9)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.1 Genetic Findings", ordinal="6.1.10", 
                      name=f"Gene_{i}", value_set=VS.vs_6_1_10)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.1 Genetic Findings", ordinal="6.1.10a", 
                      name=f"Gene Label_{i}", value_set=VS.vs_6_1_10a)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.1 Genetic Findings", ordinal="6.1.11", 
                      name=f"Zygosity_{i}", value_set=VS.vs_6_1_11)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.1 Genetic Findings", ordinal="6.1.11a", 
                      name=f"Zygosity_other_{i}", value_set=VS.vs_6_1_11a)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.1 Genetic Findings", ordinal="6.1.12", 
                      name=f"Genomic Source Class_{i}", value_set=VS.vs_6_1_12)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.1 Genetic Findings", ordinal="6.1.13", 
                      name=f"DNA Change Type_{i}", value_set=VS.vs_6_1_13)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.1 Genetic Findings", ordinal="6.1.13a", 
                      name=f"DNA Change Type_other_{i}", value_set=VS.vs_6_1_13a)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.1 Genetic Findings", ordinal="6.1.14", 
                      name=f"Clinical Significance [ACMG]_{i}", value_set=VS.vs_6_1_14)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.1 Genetic Findings", ordinal="6.1.15", 
                      name=f"Therapeutic Actionability_{i}", value_set=VS.vs_6_1_15)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.1 Genetic Findings", ordinal="6.1.16", 
                      name=f"Clinical Annotation Level Of Evidence_{i}", value_set=VS.vs_6_1_16)
        )

# 6.2 Phenotypic Feature
def append_phenotypic_features(data_model, n=9999):
    for i in range(n):
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.2 Phenotypic Feature", ordinal="6.2.1", 
                      name=f"Phenotypic Feature_{i}", value_set=VS.vs_6_2_1)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.2 Phenotypic Feature", ordinal="6.2.2", 
                      name=f"Determination Date_{i}", value_set=VS.vs_6_2_2)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.2 Phenotypic Feature", ordinal="6.2.3", 
                      name=f"Status_{i}", value_set=VS.vs_6_2_3)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.2 Phenotypic Feature", ordinal="6.2.4a.1", 
                      name=f"Modifier_HPO_1_{i}", value_set=VS.vs_6_2_4a_1)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.2 Phenotypic Feature", ordinal="6.2.4a.2", 
                      name=f"Modifier_HPO_2_{i}", value_set=VS.vs_6_2_4a_2)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.2 Phenotypic Feature", ordinal="6.2.4a.3", 
                      name=f"Modifier_HPO_3_{i}", value_set=VS.vs_6_2_4a_3)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.2 Phenotypic Feature", ordinal="6.2.4b.1", 
                      name=f"Modifier_NCBITaxon_1_{i}", value_set=VS.vs_6_2_4b_1)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.2 Phenotypic Feature", ordinal="6.2.4b.2", 
                      name=f"Modifier_NCBITaxon_2_{i}", value_set=VS.vs_6_2_4b_2)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.2 Phenotypic Feature", ordinal="6.2.4b.3", 
                      name=f"Modifier_NCBITaxon_3_{i}", value_set=VS.vs_6_2_4b_3)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.2 Phenotypic Feature", ordinal="6.2.4c.1", 
                      name=f"Modifier_SNOMED_CT_1_{i}", value_set=VS.vs_6_2_4c_1)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.2 Phenotypic Feature", ordinal="6.2.4c.2", 
                      name=f"Modifier_SNOMED_CT_2_{i}", value_set=VS.vs_6_2_4c_2)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.2 Phenotypic Feature", ordinal="6.2.4c.3", 
                      name=f"Modifier_SNOMED_CT_3_{i}", value_set=VS.vs_6_2_4c_3)
        )
        
# 6.3 Family History
def append_family_history_fields(data_model, n=9999):
    for i in range(n):
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.3 Family History", ordinal="6.3.0", 
                      name=f"Family Member Pseudonym_{i}", value_set=VS.vs_6_3_0)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.3 Family History", ordinal="6.3.1", 
                      name=f"Propositus/-a_{i}", value_set=VS.vs_6_3_1)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.3 Family History", ordinal="6.3.2", 
                      name=f"Relationship of the individual to the index case/propositus/a_{i}", 
                      value_set=VS.vs_6_3_2)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.3 Family History", ordinal="6.3.3", 
                      name=f"Consanguinity_{i}", value_set=VS.vs_6_3_3)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.3 Family History", ordinal="6.3.4", 
                      name=f"Family Member Relationship_{i}", value_set=VS.vs_6_3_4)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.3 Family History", ordinal="6.3.5", 
                      name=f"Family Member Record Status_{i}", value_set=VS.vs_6_3_5)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.3 Family History", ordinal="6.3.6", 
                      name=f"Family Member Sex_{i}", value_set=VS.vs_6_3_6)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.3 Family History", ordinal="6.3.7", 
                      name=f"Family Member Age_{i}", value_set=VS.vs_6_3_7)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.3 Family History", ordinal="6.3.8", 
                      name=f"Family Member Date of Birth_{i}", value_set=VS.vs_6_3_8)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.3 Family History", ordinal="6.3.9", 
                      name=f"Family Member Deceased_{i}", value_set=VS.vs_6_3_9)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.3 Family History", ordinal="6.3.10", 
                      name=f"Family Member Cause of Death_{i}", value_set=VS.vs_6_3_10)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.3 Family History", ordinal="6.3.11", 
                      name=f"Family Member Deceased Age_{i}", value_set=VS.vs_6_3_11)
        )
        RARELINK_CDM_V2_0_0.fields.append(
            DataField(section="6.3 Family History", ordinal="6.3.12", 
                      name=f"Family Member Disease_{i}", value_set=VS.vs_6_3_12)
        )

append_care_pathway_fields(RARELINK_CDM_V2_0_0)
append_disease_fields(RARELINK_CDM_V2_0_0)
append_genetic_findings_fields(RARELINK_CDM_V2_0_0)
append_phenotypic_features(RARELINK_CDM_V2_0_0)
append_family_history_fields(RARELINK_CDM_V2_0_0)



def load_rarelink_data(path: Union[str, Path], data_model: DataModel = RARELINK_CDM_V2_0_0):
    return data_model.load_data(
        path,
        pseudonym_column="snomed_422549004",
        date_of_admission_column="snomed_399423000",
        date_of_birth_column="snomed_184099003",
        sex_at_birth_column="snomed_281053000",
        karyotypic_sex_column="snomed_1296886006",
        gender_identity_column="snomed_263495000",
        country_of_birth_column="snomed_370159000",
        vital_status_column="snomed_278844005",
        time_of_death_column="snomed_398299004",
        cause_of_death_column="snomed_184305005",
        age_category_column="snomed_105727008",
        length_of_gestation_at_birth_column="snomed_412726003",
        undiagnosed_rd_case_column="snomed_723663001",
        encounter_start_column="hl7fhir_enc_period_start",
        encounter_end_column="hl7fhir_enc_period_end",
        encounter_status_column="snomed_305058001",
        encounter_class_column="hl7fhir_encounter_class",
        disease_mondo_column="snomed_64572001_mondo",
        disease_ordo_column="snomed_64572001_ordo",
        disease_icd10cm_column="snomed_64572001_icd10cm",
        disease_icd11_column="snomed_64572001_icd11",
        disease_omim_p_column="snomed_64572001_omim_p",
        verification_status_column="loinc_99498_8",
        age_at_onset_column="snomed_424850005",
        date_of_onset_column="snomed_298059007",
        age_at_diagnosis_column="snomed_423493009",
        date_of_diagnosis_column="snomed_432213005",
        body_site_column="snomed_363698007",
        clinical_status_column="snomed_263493007",
        severity_column="snomed_246112005",
        genomic_diagnosis_mondo_column="snomed_106221001_mondo",
        genomic_diagnosis_omim_p="snomed_106221001_omim_p",
        progress_status_of_interpretation_column="ga4gh_progress_status",
        interpretation_status_column="ga4gh_interp_status",
        structural_variant_analysis_method_column="loinc_81304_8",
        structural_variant_analysis_method_other_column="loinc_81304_8_other",
        reference_genome_column="loinc_62374_4",
        genetic_mutation_string_column="loinc_lp7824_8",
        genomic_dna_change_column="loinc_81290_9",
        sequence_dna_change_column="loinc_48004_6",
        amino_acid_change_column="loinc_48005_3",
        gene_column="loinc_48018_6",
        gene_label_column="loinc_48018_6_label",
        zygosity_column="loinc_53034_5",
        zygosity_other_column="loinc_53034_5_other",
        genomic_source_class_column="loinc_48002_0",
        dna_change_type_column="loinc_48019_4",
        dna_change_type_other_column="loinc_48019_4_other",
        clinical_significance_acmg_column="loinc_53037_8",
        therapeutic_actionability_column="ga4gh_therap_action",
        clinical_annotation_level_of_evidence_column="loinc_93044_6",
        phenotypic_feature_column="snomed_8116006",
        determination_date_column="snomed_8116006_date",
        status_column="ga4gh_pheno_excluded",
        modifier_hpo_1_column="ga4gh_pheno_mod_hp1", 
        modifier_hpo_2_column="ga4gh_pheno_mod_hp2",
        modifier_hpo_3_column="ga4gh_pheno_mod_hp3",
        modifier_ncbitaxon_1_column="ga4gh_pheno_mod_ncbitax1",
        modifier_ncbitaxon_2_column="ga4gh_pheno_mod_ncbitax2",
        modifier_ncbitaxon_3_column="ga4gh_pheno_mod_ncbitax3",
        modifier_snomed_ct_1_column="ga4gh_pheno_mod_snomed1",
        modifier_snomed_ct_2_column="ga4gh_pheno_mod_snomed2",
        modifier_snomed_ct_3_column="ga4gh_pheno_mod_snomed3",
        family_member_pseudonym_column="family_history_pseudonym",
        propositus_a_column="snomed_64245008",
        relationship_of_the_individual_to_the_index_case_propositus_a_column=
                            "snomed_408732007",
        consanguinity_column="snomed_842009",
        family_member_relationship_column="snomed_444018008",
        family_member_record_status_column="hl7fhir_fmh_status",
        family_member_sex_column="loinc_54123_5",
        family_member_age_column="loinc_54141_7",
        family_member_date_of_birth_column="loinc_54124_3",
        family_member_deceased_column="snomed_740604001",
        family_member_cause_of_death_column="loinc_54112_8",
        family_member_deceased_age_column="loinc_92662_6",
        family_member_disease_column="loinc_75315_2",
        consent_status_column="snomed_309370004",
        consent_date_column="hl7fhir_consent_datetime",
        health_policy_monitoring_column="snomed_386318002",
        agreement_to_be_contacted_for_research_purposes_column="rarelink_consent_contact",
        consent_to_the_reuse_of_data_column="rarelink_consent_data",
        biological_sample_column="snomed_123038009",
        link_to_a_biobank_column="rarelink_biobank_link", 
        classification_of_functioning_disability_column="rarelink_icf_score",
    )

    
