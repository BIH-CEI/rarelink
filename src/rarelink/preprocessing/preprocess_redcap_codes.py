from typing import List
from phenopacket_mapper.data_standards import Coding, CodeSystem


def parse_redcap_code(redcap_code: str, resources: List[CodeSystem]) -> Coding:
    """
    This method parses a string representation of a code in the REDCap format to a Coding object.
    
    :param redcap_code: A string with format like 'snomed_1234567', 'mondo_1234567', or any prefix followed by '_'
                        and the code.
    :param resources: A list of available CodeSystems that the redcap_code prefix can be matched to.
    :return: A Coding object with the matching CodeSystem and the extracted code.
    
    Example:
    # parse_redcap_code("snomed_1234567", [CodeSystem(name="SNOMED CT", namespace_prefix="SNOMED")])
    Coding(system=CodeSystem(name='SNOMED CT', namespace_prefix='SNOMED'), code='1234567')
    """

    # Split the redcap_code into its prefix and code part
    try:
        prefix, code = redcap_code.split('_', 1)
    except ValueError:
        raise ValueError(f"Invalid format for redcap_code: {redcap_code}. Expected format: 'prefix_code'.")

    # Find the matching CodeSystem based on the prefix
    for resource in resources:
        if resource.namespace_prefix.lower() == prefix.lower():
            return Coding(system=resource, code=code)
    
    # Raise an error if no matching CodeSystem was found
    raise ValueError(f"No matching CodeSystem found for prefix: {prefix}")
