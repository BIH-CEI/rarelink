from typing import List

from phenopacket_mapper.data_standards import Coding, CodeSystem


def parse_redcap_code(redcap_code: str, resources: List[CodeSystem]) -> Coding:
    """This method parses a string representation of a code in the REDCap format to a Coding object.

    # >>> parse_redcap_code("snomed_12345", [CodeSystem(name="SNOMED CT", namespace_prefix="SNOMED")])
    # Coding(system=CodeSystem(name='SNOMED CT', namespace_prefix='SNOMED'), code='12345')
    """
    raise NotImplementedError
