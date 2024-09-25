from phenopackets.schema.v2 import Phenopacket
from phenopackets.schema.v2 import phenopackets
from phenopacket_mapper.mapping.mapper import PhenopacketMapper, PhenopacketElement
from rarelink.rarelink_cdm import RARELINK_CDM_V2_0_0



class rarelink_cdm_multiple_fields:
    def pref_disease_onset(values):
        date_of_diagnosis, date_of_onset, age_at_onset = values
        if date_of_diagnosis:
            return date_of_diagnosis
        elif date_of_onset:
            return date_of_onset
        elif age_at_onset:
            return age_at_onset
        else:
            raise ValueError("All values passed are None")
            
    def pref_hgvs_code(values):
        g_HGVS, c_HGVS, p_HGVS = values
        if g_HGVS:
            return g_HGVS
        elif c_HGVS:
            return c_HGVS
        elif p_HGVS:
            return p_HGVS
        else:
            raise ValueError("All values passed are None")
        
    def pref_zygosity_code(values):
        zygosity, zygosity_other = values
        if zygosity:
            return zygosity
        elif zygosity_other:
            return zygosity_other
        else:
            raise ValueError("All values passed are None")
        

    def pref_code_disease(values):
        mondo, ordo, icd10cm, icd11, omim = values
        if mondo:
            return mondo
        elif omim:
            return omim
        elif ordo:
            return ordo
        elif icd11:
            return icd11
        elif icd10cm:
            return icd10cm
        else:
            raise ValueError("All values passed are None")
        

RARELINK_CDM_v2_0_0_REPEATING_FIELDS = rarelink_cdm_multiple_fields()



# def map_rarelink_cdm_to_phenopacket(self, data_model: RARELINK_CDM_V2_0_0) -> Phenopacket:
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
#     )

