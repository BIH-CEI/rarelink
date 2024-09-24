from pathlib import Path
from typing import Union, List

from phenopackets.schema.v2 import Phenopacket

from phenopacket_mapper.mapping.mapper import PhenopacketMapper, PhenopacketElement
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
    
    # 3. Define the Mapping 
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
                phenopacket_element=phenopackets.VitalStatus,
                status=data_model.vital_status,
                time_of_death=data_model.time_of_death,
                cause_of_death=data_model.cause_of_death,
                time_at_last_encounter=data_model.age_category,
            )
        ),
        interpretations = [
            PhenopacketElement(
                phenopacket_element=phenopackets.Interpretation,
                id=getattr(data_model, f"pseudonym_{i}", None),
                progress_status=getattr(data_model, f"progress_status_of_interpretation_{i}", None),
                diagnosis=PhenopacketElement(
                    phenopacket_element=phenopacket.Diagnosis,
                    disease=getattr(data_model, f"genomic_diagnosis_{i}", None),
                    genomic_interpretations=[
                        PhenopacketElement(
                            phenopacket_element=phenopackets.GenomicInterpretation,
                            subject_or_biosample_id=getattr(data_model, f"pseudonym_{i}", None),
                            interpretation_status=PhenopacketElement(
                                phenopacket_element=phenopackets.InterpretationStatus,
                                interpretation_status=getattr(data_model, f"interpretation_status_{i}", None),
                            ),
                            call=PhenopacketElement(
                                phenopacket_element=phenopackets.VariationInterpretation,
                                acmg_pathogenicity_classification=PhenopacketElement(
                                    phenopacket_element=phenopackets.AcmgPathogenicityClassification,
                                    acmg_pathogenicity_classification=getattr(data_model, f"clinical_significance_acmg_{i}", None),
                                ),
                                therapeutic_actionability=PhenopacketElement(
                                    phenopacket_element=phenopackets.TherapeuticActionability,
                                    therapeutic_actionability=getattr(data_model, f"therapeutic_actionability_{i}", None),
                                ),
                                variation_descriptor=PhenopacketElement(
                                    phenopacket_element=phenopackets.VariationDescriptor,
                                    vrs_ref_allele_seq=getattr(data_model, f"reference_genome_{i}", None),
                                    allelic_state=getattr(data_model, f"zygosity_{i}", None),
                                    extensions=PhenopacketElement(
                                        phenopacket_element=phenopackets.Extension,
                                        name=getattr(data_model, f"genetic_mutation_string_{i}", None),
                                        value=getattr(data_model, f"genetic_mutation_string_{i}", None),
                                    ),
                                    expression=PhenopacketElement(
                                        phenopacket_element=phenopackets.Expression,
                                        syntax='hgvs',
                                        value=getattr(data_model, f"genomic_dna_change_{i}", None),
                                        value=getattr(data_model, f"sequence_dna_change_{i}", None),
                                        value=getattr(data_model, f"amino_acid_change_{i}", None),
                                    ),
                                    gene_context=PhenopacketElement(
                                        phenopacket_element=phenopackets.GeneDescriptor,
                                        value_id=getattr(data_model, f"gene_{i}", None),
                                        symbol=getattr(data_model, f"gene_symbol_{i}", None),
                                    ),
                                ),
                            )
                        )
                    ]
                )
            )
            for i in range(n=9999)
        ],
        diseases = [
            PhenopacketElement(
                phenopacket_element=phenopackets.Disease,
                # (3) Patient Status
                term=getattr(data_model, f"undiagnosed_rd_case_{i}", None),
                # (5) Disease
                term=getattr(data_model, f"disease_{i}", None),
                excluded=getattr(data_model, f"verification_status_{i}", None),
                onset=getattr(data_model, f"age_at_onset_{i}", None),
                onset=getattr(data_model, f"date_of_onset_{i}", None),
                onset=getattr(data_model, f"date_of_diagnosis_{i}", None),
                primary_site=getattr(data_model, f"body_site_{i}", None)
            )
            for i in range(n=9999)
        ],
        phenotypic_features=[
            PhenopacketElement(
                phenopacket_element=phenopackets.PhenotypicFeature,
                type=getattr(data_model, f"phenotypic_feature_{i}", None),
                onset=getattr(data_model, f"determination_date_{i}", None),
                excluded=getattr(data_model, f"status_{i}", None),
                modifier=getattr(data_model, f"modifier_{i}", None),
            )
            for i in range(n=9999)
        ],
        family=[
            PhenopacketElement(
                phenopacket_element=phenopacket.Family,
                id=data_model.family_history_pseudonym,
                proband=data_model.propositus_a,
                consanguinous_parents=data_model.consanguinity,
                pedigree=[
                    PhenopacketElement(
                        phenopacket_element=phenopackets.Pedigree,
                        persons=PhenopacketElement(
                            phenopacket_element=phenopackets.Person,
                            individual_id=data_model.family_member_pseudonym,
                            paternal_id=data_model.family_member_relationship,
                            maternal_id=data_model.family_member_relationship,
                            sex=data_model.family_member_sex,
                        )
                    )
                ],
            )
        ]
    )

    # return phenopackets
    # return NotImplementedError



# def phenopacket_pipeline(path: Union[str, Path]) -> List[Phenopacket]:
#     # 1. preprocess data 
#     preprocessed_path = preprocess_redcap_for_phenopacket_pipeline(path)
#     # 2. load preprocessed data
#     data_model = RARELINK_CDM_V2_0_0
#     data_set = data_model.load_data(preprocessed_path, compliance="soft")
#     print("idsd of the fields in the data model: \n", 
#           data_model.data_model.get_field_ids())
    
#     # 3. Define the Mapping 
#     phenopacket_mapper = PhenopacketMapper(
#         data_set,
#         id=data_model.pseudonym,
#         subject=PhenopacketElement(
#             phenopacket_element=phenopackets.Individual,
#             # (1) Formal Criteria
#             id=data_model.pseudonym,
#             time_at_last_encounter=data_model.date_of_admission,
#             # (2) Personal Information
#             date_of_birth=data_model.date_of_birth,
#             sex=data_model.sex_at_birth,
#             karyotypic_sex=data_model.karyotypic_sex,
#             gender=data_model.gender_identity,
#             vital_status=PhenopacketElement(
#                 phenopacket_element=phenopackets.VitalStatus,
#                 status=data_model.vital_status,
#                 time_of_death=data_model.time_of_death,
#                 cause_of_death=data_model.cause_of_death,
#                 time_at_last_encounter=data_model.age_category,
#             )
#         ),
#         interpretations=[
#             PhenopacketElement(
#                 phenopacket_element=phenopackets.Interpretation,
#                 id=data_model.pseudonym,
#                 progress_status=data_model.progress_status_of_interpretation,
#                 diagnosis=PhenopacketElement(
#                     phenopacket_element=phenopacket.Diagnosis,
#                     disease=data_model.genomic_diagnosis,
#                     genomic_interpretations=[
#                         PhenopacketElement(
#                             phenopacket_element=phenopackets.GenomicInterpretation,
#                             subject_or_biosample_id=data_model.pseudonym,
#                             interpretation_status=PhenopacketElement(
#                                 phenopacket_element=phenopackets.InterpretationStatus,
#                                 interpretation_status=data_model.interpretation_status,
#                             ),
#                             call=PhenopacketElement(
#                                 phenopacket_element=phenopackets.VariationInterpretation,
#                                 acmg_pathogenicity_classification=PhenopacketElement(
#                                     phenopacket_element=phenopackets.AcmgPathogenicityClassification,
#                                     acmg_pathogenicity_classification=data_model.clinical_significance_acmg,
#                                 ),
#                                 therapeutic_actionability=PhenopacketElement(
#                                     phenopacket_element=phenopackets.TherapeuticActionability,
#                                     therapeutic_actionability=data_model.therapeutic_actionability,
#                                 ),
#                                 variation_descriptor=PhenopacketElement(
#                                     phenopacket_element=phenopackets.VariationDescriptor,
#                                     vrs_ref_allele_seq=data_model.reference_genome,
#                                     allelic_state=data_model.zygosity,
#                                     extensions=PhenopacketElement(
#                                         phenopacket_element=phenopackets.Extension,
#                                         name=data_model.genetic_mutation_string,
#                                         value=data_model.genetic_mutation_string,
#                                     ),
#                                     expression=PhenopacketElement(
#                                         phenopacket_element=phenopackets.Expression,
#                                         syntax='hgvs',
#                                         value=data_model.genomic_dna_change,
#                                         value=data_model.sequence_dna_change,
#                                         value=data_model.amino_acid_change,
#                                     ),
#                                     gene_context=PhenopacketElement(
#                                         phenopacket_element=phenopackets.GeneDescriptor,
#                                         value_id=data_model.gene,
#                                         symbol=data_model.gene_symbol,
#                                     ),
#                                 ),
#                             )
#                         )
#                     ]
#                 )                     
#             )
#         ],
#         diseases=[
#             PhenopacketElement(
#                 phenopacket_element=phenopackets.Disease,
#                 # (3) Patient Status
#                 term=data_model.undiagnosed_rd_case,
#                 # (5) Disease
#                 term=data_model.disease,
#                 excluded=data_model.verification_status,
#                 onset=data_model.age_at_onset,
#                 onset=data_model.date_of_onset,
#                 onset=data_model.date_of_diagnosis,
#                 primary_site=data_model.body_site
#             )
#         ],
#         phenotypic_features=[
#             PhenopacketElement(
#                 phenopacket_element=phenopackets.PhenotypicFeature,
#                 type=getattr(data_model, f"phenotypic_feature_{i}", None),
#                 onset=getattr(data_model, f"determination_date_{i}", None),
#                 excluded=getattr(data_model, f"status_{i}", None),
#                 modifier=getattr(data_model, f"modifier_{i}", None),
#             )
#             for i in range(n=9999)
#         ],
#         family=[
#             PhenopacketElement(
#                 phenopacket_element=phenopacket.Family,
#                 id=data_model.family_history_pseudonym,
#                 proband=data_model.propositus_a,
#                 consanguinous_parents=data_model.consanguinity,
#                 pedigree=[
#                     PhenopacketElement(
#                         phenopacket_element=phenopackets.Pedigree,
#                         persons=PhenopacketElement(
#                             phenopacket_element=phenopackets.Person,
#                             individual_id=data_model.family_member_pseudonym,
#                             paternal_id=data_model.family_member_relationship,
#                             maternal_id=data_model.family_member_relationship,
#                             sex=data_model.family_member_sex,
#                         )
#                     )
#                 ],
#             )
#         ]
#     )