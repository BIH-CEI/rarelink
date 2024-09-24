from pathlib import Path
from typing import Union, List

from phenopackets.schema.v2 import Phenopacket

from phenopacket_mapper.mapping.mapper import PhenopacketMapper
from rarelink.rarelink_cdm import RARELINK_CDM_V2_0_0

from rarelink.preprocessing import preprocess_redcap_for_phenopacket_pipeline


def phenopacket_pipeline(path: Union[str, Path]) -> List[Phenopacket]:
    # 1. preprocess data 
    preprocessed_path = preprocess_redcap_for_phenopacket_pipeline(path)
    # 2. load preprocessed data
    data_model = RARELINK_CDM_V2_0_0
    data_set = data_model.load_data(preprocessed_path, compliance="soft")
    print("idsd of the fields in the data model: \n", 
          data_model.data_model.get_field_ids())
    #
    # 3. Define the Mapping 
    # WIP in Phenopacket_Mapper
    phenopacket_mapper = PhenopacketMapper(
        data_set,
        id=data_model.pseudonym,
        subject=PhenopacketElement(
            phenopacket_element=phenopackets.Individual,
            # (1) Formal Criteria
                id=data_model.pseudonym,
                time_at_last_encounter=data_model.date_of_admission,
            # (2) Personal Information
                date_of_birth=data_model.date_of_birth,
                sex=data_model.sex_at_birth,
                karyotypic_sex=data_model.karyotypic_sex,
                gender=data_model.gender_identity,
                vital_status=PhenopacketElement(
                    phenopacket_element=phenopacket.VitalStatus,
                    status=data_model.vital_status,
                    time_of_death=data_model.time_of_death,
                    cause_of_death=data_model.cause_of_death,
                    time_at_last_encounter=data_model.age_category,
                )
        )
        phenotypic_features=[
            PhenopacketElement(
                phenopacket_element=phenopacket.PhenotypicFeature,
                type=getattr(data_model, f"phenotypic_feature_{i}", None),
                onset=getattr(data_model, f"determination_date_{i}", None),
                excluded=getattr(data_model, f"status_{i}", None),
                modifier=getattr(data_model, f"modifier_{i}", None),
            )
            for i in range(n:=9999)
        ]
                
    
    
            
        

            # (3) Patient Status
            

            phenopacket_element=phenopacket.Disease,
                term=data_model.undiagnosed_rd_case,
            # (4) Encounter
            # n/a
            # (5) Disease
                term=data_model.disease,
                excluded=data_model.verification_status,
                onset=data_model.age_at_onset,
                onset=data_model.date_of_onset,
                onset=data_model.date_of_diagnosis,
                primary_site=data_model.body_site,
            phenopacket_element=phenopacket.Interpretation,
                progress_status=data_model.clinical_status,
            # (6.1) Genetic Findings
                diagnosis_disease=data_model.genomic_diagnosis,
                progress_status=data_model.progress_status_of_interpretation,
            phenopacket_element=phenopacket.GenomicInterpretation,
                interpretation_status=data_model.interpretation_status,
            phenopacket_element=phenopacket.VariationDescriptor,
                vrs_ref_allele_seq=data_model.reference_genome,
            phenopacket_element=phenopacket.VariationDescriptor.Extension,
                name=data_model.genetic_mutation_string,
                value=data_model.genetic_mutation_string,
            phenopacket_element=phenopacket.VariationDescriptor.Expression,
                syntax='hgvs',
                value=data_model.genomic_dna_change,
                value=data_model.sequence_dna_change,
                value=data_model.amino_acid_change,
            phenopacket_element=phenopacket.VariationDescriptor.GeneDescriptor,
                value_id=data_model.gene,
            phenopacket_element=phenopackets.VariationDescriptor,
                allelic_state=data_model.zygosity,
            phenopacket_element=phenopackets.VariantInterpretation,
                acmg_pathogenicity_classification=data_model.clinical_significance_acmg,
                therapeutic_actionability=data_model.therapeutic_actionability,
            # (6.2) Phenotypic Findings
            phenopacket_element=phenopacket.PhenotypicFeature,
                type=data_model.phenotypic_feature,
                onset=data_model.determination_date,
                excluded=data_model.status,
                modifier=data_model.modifier,
           # (6.3) Family History
            phenopacket_element=phenopacket.Family,
                id=data_model.family_history_pseudonym,
            phenopacket_element=phenopacket.Family,
                consanguinous_parents=data_model.consanguinity,
            phenopacket_element=phenopacket.Pedigree.Person,
                individual_id=data_model.family_member_pseudonym,
                paternal_id=data_model.family_member_relationship,
                maternal_id=data_model.family_member_relationship,
                sex=data_model.family_member_sex,




            



            # 
            # TODO do tthis for entire data model
        )                       
    )
    # 4. map data
    # 5. Validate Phenoppackets
    # 6. return Phenopackets  phenopacket_mapper.map()
,
    #     family_member_age_column="loinc_54141_7",
    #     family_member_date_of_birth_column="loinc_54124_3",
    #     family_member_deceased_column="snomed_740604001",
    #     family_member_cause_of_death_column="loinc_54112_8",
    #     family_member_deceased_age_column="loinc_92662_6",
    #     family_member_disease_column="loinc_75315_2",
    #     consent_status_column="snomed_309370004",
    #     consent_date_column="hl7fhir_consent_datetime",
    #     health_policy_monitoring_column="snomed_386318002",
    #     agreement_to_be_contacted_for_research_purposes="rarelink_consent_contact",
    #     consent_to_the_reuse_of_data_column="rarelink_consent_data",
    #     biological_sample_column="snomed_123038009",
    #     link_to_a_biobankcolumn="rarelink_biobank_link",
    #     classification_of_functioning_disability_column="rarelink_icf_score"
    # )
    
    # return phenopackets
    return NotImplementedError