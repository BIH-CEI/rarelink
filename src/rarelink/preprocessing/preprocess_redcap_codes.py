from typing import List
from phenopacket_mapper.data_standards import Coding, CodeSystem

def parse_redcap_code(redcap_code: str, resources: List[CodeSystem]) -> Coding:
    """
    This method parses a string representation of a code in the REDCap format to
      a Coding object.
    
    :param redcap_code: A string with format like 'snomed_1234567', 
                        'mondo_1234567', or any prefix followed by '_'
                        and the code. Special cases:
                        1. 'loinc_81304_8' should convert the underscore in the 
                        code part to a hyphen.
                        2. If the code comes preformatted as 'HP:123456' or 
                        'MONDO:12456', no transformation is needed.
                        3. For 'ICD10CM', 'ICD11', 'ICD10', and 'ICD9' codes, 
                        underscores in the code part should be replaced with 
                        periods, and the prefix must be uppercased.
    :param resources: A list of available CodeSystems that the redcap_code 
        prefix can be matched to.
    :return: A Coding object with the matching CodeSystem and the extracted code.
    
    Example:
    # parse_redcap_code("snomed_1234567", [CodeSystem(name="SNOMED CT", 
        namespace_prefix="SNOMED")])
    # Coding(system=CodeSystem(name='SNOMED CT', namespace_prefix='SNOMED'), 
        code='1234567')
    """

    # Check if the code is already in the correct format (e.g., 'HP:123456')
    if ":" in redcap_code:
        prefix, code = redcap_code.split(':', 1)
        for resource in resources:
            if resource.namespace_prefix.lower() == prefix.lower():
                return Coding(system=resource, code=code)
    
    # Otherwise, assume it's in 'prefix_code' format and split by '_'
    try:
        prefix, code = redcap_code.split('_', 1)
    except ValueError:
        raise ValueError(f"Invalid format for redcap_code: {redcap_code}. 
                         Expected format: 'prefix_code'.")

    # Special case for 'loinc' to replace '_' with '-'
    if prefix.lower() == "loinc":
        code = code.replace('_', '-')

    # Special case for 'ICD10CM', 'ICD11', 'ICD10', and 'ICD9' to replace '_' 
    # with '.' and ensure uppercase prefix
    if prefix.lower() in ["icd10cm", "icd11", "icd10", "icd9"]:
        code = code.replace('_', '.')
        prefix = prefix.upper()  # Ensure the prefix is in uppercase

    # Find the matching CodeSystem based on the prefix
    for resource in resources:
        if resource.namespace_prefix.lower() == prefix.lower():
            return Coding(system=resource, code=code)
    
    # Raise an error if no matching CodeSystem was found
    raise ValueError(f"No matching CodeSystem found for prefix: {prefix}")
