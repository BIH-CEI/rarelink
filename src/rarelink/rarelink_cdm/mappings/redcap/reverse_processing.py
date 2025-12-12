from rarelink.utils.code_processing import remove_prefix_from_code

REVERSE_PROCESSING = {
    "snomedct_184305005": lambda x: remove_prefix_from_code(x, "ICD10CM"),
    "snomedct_64572001_icd10cm": lambda x: remove_prefix_from_code(x, "ICD10CM"),
    "snomedct_64572001_icd11": lambda x: remove_prefix_from_code(x, "ICD11"),
    "snomedct_64572001_omim_p": lambda x: remove_prefix_from_code(x, "OMIM"),
    "snomedct_363698007": lambda x: remove_prefix_from_code(x, "SNOMEDCT"),
    "snomedct_106221001_omim_p": lambda x: remove_prefix_from_code(x, "OMIM"),
    "variant_validation": lambda x: {True: "yes", False: "no"}.get(x, None),
    "loinc_53034_5_other": lambda x: remove_prefix_from_code(x, "LOINC"),
    "loinc_48019_4_other": lambda x: remove_prefix_from_code(x, "LOINC"),
    "hp_0012823_ncbitaxon": lambda x: remove_prefix_from_code(x, "NCBITAXON"),
    "hp_0012823_snomed": lambda x: remove_prefix_from_code(x, "SNOMEDCT"),
    "ncit_c60819": lambda x: remove_prefix_from_code(x, "LOINC"),
    "ln_85353_1": lambda x: remove_prefix_from_code(x, "LOINC"),
    "ncit_c25712": lambda x: str(x) if x is not None else None,
    "snomedct_122869004_snomed": lambda x: remove_prefix_from_code(x, "SNOMEDCT"),
    "snomedct_122869004_bdsite": lambda x: remove_prefix_from_code(x, "SNOMEDCT"),
    "loinc_54112_8": lambda x: remove_prefix_from_code(x, "ICD10CM"),
    "loinc_54141_7": lambda x: str(x) if x is not None else None,
    "loinc_92662_6": lambda x: str(x) if x is not None else None,
}