

import pandas as pd
from pathlib import Path
from typing import List, Union

from phenopacket_mapper.data_standards import DataSet
from phenopacket_mapper.data_standards.code_system import CodeSystem
from rarelink.preprocessing import preprocess_redcap_codes


def preprocess_redcap_for_phenopackets(
        data_set: DataSet,
        resources: List[CodeSystem]
):
    """Preprocess REDCap data for the phenopacket pipeline.

    :param ds: A pandas DataFrame with REDCap data loaded in the Rarelink data model.
    """
    data_model = data_set.data_model

    # (2) Personal Information
    # 2.1 Date of Birth
    # preprocess using dict
    data_set.preprocess(
        fields=data_model.sex_at_birth,
        mapping = {
            "snomed_248152002": "FEMALE",
            "snomed_248153007": "MALE",
            "snomed_184115007": "UNKNOWN_SEX",
            "snomed_32570691000036108": "OTHER_SEX",
            "snomed_1220561009": "UNKNOWN_SEX"
        }
    )
    # 2.3 Karyotypic Sex
    data_set.preprocess(
        fields=data_model.karyotypic_sex,
        mapping = {
            "snomed_261665006": "UNKNOWN_KARYOTYPE",
            "snomed_734875008": "XX",
            "snomed_734876009": "XY",
            "snomed_80427008": "X0",
            "snomed_65162001": "XXY",
            "snomed_35111009": "XXX",
            "snomed_403760006": "XXYY",
            "snomed_78317008": "XXXY",
            "snomed_10567003": "XXXX",
            "snomed_48930007": "XYY",
            "snomed_74964007": "OTHER_KARYOTYPE"
        }
    )
    # 2.4 Gender Identity
    # preprocess using func
    data_set.preprocess(
        fields=data_model.gender_identity,
        mapping=preprocess_redcap_codes,
        resources=resources,
    )

    # (3) Patient Status
    # 3.1 Vital Status
    data_set.preprocess(
        fields=data_model.patient_status,
        mapping = {
            "snomed_438949009": "ALIVE",
            "snomed_419099009": "DECEASED",
            "snomed_399307001": "UNKNOWN_STATUS",
            "snomed_185924006" : "UNKNOWN_STATUS",
            "snomed_261665006": "UNKNOWN_STATUS"
        }
    )
    # 3.4 Age Category
    data_set.preprocess(
        fields=data_model.age_category,
        mapping=preprocess_redcap_codes,
        resources=resources,
    )


    # preprocess mutliple cols

    # 5.1 Disease (include 3.6 Undiagnosed RD Case)

    data_set.preprocess(
        fields=[
            data_model.disease_mondo,
            data_model.disease_ordo,
            data_model.disease_icd10cm,
            data_model.disease_icd11,
            data_model.disease_omim,
        ],
        mapping=pref_code_disease,
        resources=resources,
    )
    
    # 5.2 Verification Status
    data_set.preprocess(
        fields=data_model.verification_status,
        mapping = {
                "hl7fhir_unconfirmed": "false",
                "hl7fhir_provisional": "false",
                "hl7fhir_differential": "false",
                "hl7fhir_confirmed": "false",
                "hl7fhir_refuted": "true",
                "hl7fhir_entered-in-error": "false",
        }
    )

    # 5.3 Age at Onset

    data_set.preprocess(
        fields=[
            data_model.date_of_diagnosis,
            data_model.date_of_onset,
            data_model.age_at_onset,
        ],
        mapping=pref_disease_onset,
        resources=resources,
    )


    # 6.1 Genetic Findings
    # 6.1.5 Reference Genomie
    data_set.preprocess(
        mapping = {
            "loinc_la14032_9": "NCBI Build 34 (hg16)",
            "loinc_la14029_5": "GRCh37 (hg19)",
            "loinc_la14030_3": "NCBI Build 36.1 (hg18)",
            "loinc_la14031_1": "NCBI Build 35 (hg17)",
            "loinc_la26806_2": "GRCh38 (hg38)"
        },
        fields=data_model.reference_genome,
    )

    data_set.preprocess(
        fields=[
            data_model.g_HGVS,
            data_model.c_HGVS,
            data_model.p_HGVS,
        ],
        mapping=pref_hgvs_code,
        resources=resources,
    )
    # 6.1.11 Zygosity 
    data_set.preprocess(
        fields=data_model.zygosity,
        mapping=preprocess_redcap_codes,
        resources=resources,
    )

    # 6.1.14 Clinical Significance [ACMG]
    data_set.preprocess(
        fields=data_model.clinical_significance_acmg_,
        mapping = {
            "loinc_la6668_3": "PATHOGENIC",
            "loinc_la26332_9": "LIKELY_PATHOGENIC",
            "loinc_la26333_7": "UNCERTAIN_SIGNIFICANCE",
            "loinc_la26334_5": "LIKELY_BENIGN",
            "loinc_la6675_8": "BENIGN",
            "loinc_la4489_6": "NOT_PROVIDED"
        }

    )

    # 6.2 Phenotypic Feature
    # 6.2.3 Status

    data_set.preprocess(
        fields=data_model.status,
        mapping = {
            "snomed_410605003" : "false",
            "snomed_723511001" : "true"
        }
    )

    # 6.3 Family History
    # TODO: check with Filip how to do this, perhaps leave it out for now 


    # TODO @aslgrafe: handle ds.data_frame preprocessing
    # 1. read csv file from inputpath
    # 2. preprocess the data frame
    # 3. save the preprocessed data frame to output path
    # 4. return the output path
    raise NotImplementedError


# product of this function is the preprocessed data frame saved a csv or what ever to be used by the phenopaxcket pipeline.py 
# upload data -> preprocess -> output locally -> output of this function: path of precprocessed data