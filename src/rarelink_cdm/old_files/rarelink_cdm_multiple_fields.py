# def pref_disease_onset(values):
#         date_of_diagnosis, date_of_onset, age_at_onset = values
#         if date_of_diagnosis:
#             return date_of_diagnosis
#         elif date_of_onset:
#             return date_of_onset
#         elif age_at_onset:
#             return age_at_onset
#         else:
#             raise ValueError("All values passed are None")

# def pref_hgvs_code(values):
#     g_HGVS, c_HGVS, p_HGVS = values
#     if g_HGVS:
#         return g_HGVS
#     elif c_HGVS:
#         return c_HGVS
#     elif p_HGVS:
#         return p_HGVS
#     else:
#         raise ValueError("All values passed are None")

# def pref_zygosity_code(values):
#     zygosity, zygosity_other = values
#     if zygosity:
#         return zygosity
#     elif zygosity_other:
#         return zygosity_other
#     else:
#         raise ValueError("All values passed are None")

# def pref_code_disease(values):
#     mondo, ordo, icd10cm, icd11, omim = values
#     if mondo:
#         return mondo
#     elif omim:
#         return omim
#     elif ordo:
#         return ordo
#     elif icd11:
#         return icd11
#     elif icd10cm:
#         return icd10cm
#     else:
#         raise ValueError("All values passed are None")