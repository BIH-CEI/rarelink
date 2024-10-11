from pathlib import Path
from phenopackets.schema.v2 import Phenopacket
import phenopackets
from phenopacket_mapper.data_standards import DataSet, CodeSystem
from phenopacket_mapper.mapping.mapper import PhenopacketMapper, PhenopacketElement
from rarelink.rarelink_cdm.rarelink_cdm import load_rarelink_data
from rarelink.rarelink_cdm import pref_code_disease, pref_disease_onset, pref_hgvs_code, pref_zygosity_code


def rarelink_cdm_phenopackets_mapping(data_set: DataSet) -> PhenopacketMapper:

    data_model = data_set.data_model

    return PhenopacketMapper(
        data_model=data_model,
        id=data_model.pseudonym,
        # subject=PhenopacketElement(
        #     phenopacket_element=phenopackets.Individual,
        #     # (1) Formal Criteria
        #     id=data_model.pseudonym,
        #     time_at_last_encounter=data_model.date_of_admission,
        #     # (2) Personal Information
        #     date_of_birth=data_model.date_of_birth,
        #     sex=data_model.sex_at_birth,
        #     karyotypic_sex=data_model.karyotypic_sex,
        #     gender=data_model.gender_identity,
        #     vital_status=PhenopacketElement(
        #         phenopacket_element=phenopackets.VitalStatus,
        #         status=data_model.vital_status,
        #         time_of_death=data_model.time_of_death,
        #         cause_of_death=data_model.cause_of_death,
        #         time_at_last_encounter=data_model.age_category,
        #     )
        # ),
        # interpretations=[
        #     PhenopacketElement(
        #         phenopacket_element=phenopackets.Interpretation,
        #         id=getattr(data_model, f"pseudonym_{i}", None),
        #         progress_status=getattr(data_model, f"progress_status_of_interpretation_{i}", None),
        #         diagnosis=PhenopacketElement(
        #             phenopacket_element=Phenopacket.Diagnosis,
        #             disease=getattr(data_model, f"genomic_diagnosis_{i}", None),
        #             genomic_interpretations=[
        #                 PhenopacketElement(
        #                     phenopacket_element=phenopackets.GenomicInterpretation,
        #                     subject_or_biosample_id=getattr(data_model, f"pseudonym_{i}", None),
        #                     interpretation_status=PhenopacketElement(
        #                         phenopacket_element=Phenopacket.InterpretationStatus,
        #                         interpretation_status=getattr(data_model, f"interpretation_status_{i}", None),
        #                     ),
        #                     call=PhenopacketElement(
        #                         phenopacket_element=Phenopacket.VariationInterpretation,
        #                         acmg_pathogenicity_classification=PhenopacketElement(
        #                             phenopacket_element=phenopackets.AcmgPathogenicityClassification,
        #                             acmg_pathogenicity_classification=getattr(data_model, f"clinical_significance_acmg_{i}", None),
        #                         ),
        #                         therapeutic_actionability=PhenopacketElement(
        #                             phenopacket_element=phenopackets.TherapeuticActionability,
        #                             therapeutic_actionability=getattr(data_model, f"therapeutic_actionability_{i}", None),
        #                         ),
        #                         variation_descriptor=PhenopacketElement(
        #                             phenopacket_element=phenopackets.VariationDescriptor,
        #                             vrs_ref_allele_seq=getattr(data_model, f"reference_genome_{i}", None),
        #                             allelic_state=pref_zygosity_code([
        #                                 getattr(data_model, f"zygosity_{i}", None),
        #                                 getattr(data_model, f"zygosity_other_{i}", None)
        #                             ]),  # Call pref_zygosity_code function
        #                             extensions=PhenopacketElement(
        #                                 phenopacket_element=phenopackets.Extension,
        #                                 name=getattr(data_model, f"genetic_mutation_string_{i}", None),
        #                                 value=getattr(data_model, f"genetic_mutation_string_{i}", None),
        #                             ),
        #                             expression=PhenopacketElement(
        #                                 phenopacket_element=phenopackets.Expression,
        #                                 syntax="hgvs",
        #                                 value=pref_hgvs_code([
        #                                     getattr(data_model, f"genomic_dna_change_{i}", None),
        #                                     getattr(data_model, f"sequence_dna_change_{i}", None),
        #                                     getattr(data_model, f"amino_acid_dna_change_{i}", None)
        #                                 ]),  # Call pref_hgvs_code function
        #                             ),
        #                             gene_context=PhenopacketElement(
        #                                 phenopacket_element=phenopackets.GeneDescriptor,
        #                                 value_id=getattr(data_model, f"gene_{i}", None),
        #                                 symbol=getattr(data_model, f"gene_symbol_{i}", None),
        #                             ),
        #                         ),
        #                     )
        #                 )
        #             ]
        #         )
        #     )
        #     for i in range(9999)  # Assuming an upper bound
        # ],
        #
        # # Diseases list
        # diseases=[
        #     PhenopacketElement(
        #         phenopacket_element=phenopackets.Disease,
        #         term=pref_code_disease([
        #             getattr(data_model, f"disease_mondo_{i}", None),
        #             getattr(data_model, f"disease_ordo_{i}", None),
        #             getattr(data_model, f"disease_omim_{i}", None),
        #             getattr(data_model, f"disease_icd10cm_{i}", None),
        #             getattr(data_model, f"disease_icd11_{i}", None)
        #         ]),
        #         onset=pref_disease_onset([
        #             getattr(data_model, f"date_of_diagnosis_{i}", None),
        #             getattr(data_model, f"date_of_onset_{i}", None),
        #             getattr(data_model, f"age_at_onset_{i}", None),
        #         ]),
        #         excluded=getattr(data_model, f"verification_status_{i}", None),
        #         primary_site=getattr(data_model, f"body_site_{i}", None)
        #     )
        #     for i in range(9999)
        #     if any([
        #         getattr(data_model, f"disease_mondo_{i}", None),
        #         getattr(data_model, f"disease_ordo_{i}", None),
        #         getattr(data_model, f"disease_omim_{i}", None),
        #         getattr(data_model, f"disease_icd10cm_{i}", None),
        #         getattr(data_model, f"disease_icd11_{i}", None)
        #     ])
        # ],
        #
        # # Phenotypic features list
        # phenotypic_features=[
        #     PhenopacketElement(
        #         phenopacket_element=phenopackets.PhenotypicFeature,
        #         type=getattr(data_model, f"phenotypic_feature_{i}", None),
        #         onset=getattr(data_model, f"determination_date_{i}", None),
        #         excluded=getattr(data_model, f"status_{i}", None),
        #         modifier=[
        #             modifier
        #             for modifier in [
        #                 getattr(data_model, f"modifier_hpo_{j}_{i}", None) for j in range(1, 4)
        #             ] + [
        #                 getattr(data_model, f"modifier_ncbitaxon_{j}_{i}", None) for j in range(1, 4)
        #             ] + [
        #                 getattr(data_model, f"modifier_snomed_{j}_{i}", None) for j in range(1, 4)
        #             ]
        #             if modifier
        #         ] or None  # If no modifiers, pass None
        #     )
        #     for i in range(9999)
        #     if getattr(data_model, f"phenotypic_feature_{i}", None)
        # ]
    )

    #    # family=[
    #     #     PhenopacketElement(
    #     #         phenopacket_element=Phenopacket.Family,
    #     #         id=data_model.family_history_pseudonym,
    #     #     #    proband=data_model.propositus_a,
    #     #         consanguinous_parents=data_model.consanguinity,
    #     #         pedigree=[
    #     #             PhenopacketElement(
    #     #                 phenopacket_element=Phenopacket.Pedigree,
    #     #                 persons=PhenopacketElement(
    #     #                     phenopacket_element=Phenopacket.Person,
    #     #                     individual_id=data_model.family_member_pseudonym,
    #     #                     paternal_id=data_model.family_member_relationship,
    #     #                     maternal_id=data_model.family_member_relationship,
    #     #                     sex=data_model.family_member_sex,
    #     #                 )
    #     #             )
    #     #         ],
    #     #     )
    #     # ]
    
