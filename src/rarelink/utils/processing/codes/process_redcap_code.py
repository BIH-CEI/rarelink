def process_redcap_code(code: str, prefix: str) -> str:
    """
    Processes a REDCap code by ensuring it has the correct prefix format and 
    applies specific transformations based on the prefix type.

    This function supports a variety of transformations commonly required for 
    REDCap codes to ensure standardization across different code systems.

    Args:
        code (str): The code to process. Expected formats include:
            - "prefix_code" (e.g., "UO_1234", "loinc_81304_8")
            - "prefix:code" (e.g., "HP:0004322")
            - Mixed case inputs for prefixes (e.g., "Loinc_81304_8", 
              "ICD10cm_r51_1")
        prefix (str): The expected prefix for the code. Examples:
            - "UO" for Units of Measurement Ontology
            - "LOINC" for Logical Observation Identifiers Names and Codes
            - "ICD10CM" for ICD-10 Clinical Modification
            - "HP" for Human Phenotype Ontology

    Returns:
        str: The processed code with the correct prefix format. Specific 
             transformations:
            - Prefix is converted to uppercase (e.g., "loinc" -> "LOINC").
            - The first "_" in the code is replaced with ":" 
              (e.g., "UO_1234" -> "UO:1234").
            - For "LOINC", additional "_" in the code part are replaced with 
              "-" (e.g., "loinc_81304_8" -> "LOINC:81304-8").
            - For ICD codes ("ICD10CM", "ICD11", "ICD10", "ICD9"), additional 
              "_" in the code part are replaced with "." and the code part is 
              capitalized (e.g., "icd10cm_r51_1" -> "ICD10CM:R51.1").
            - Already formatted codes ("prefix:code") are returned with an 
              uppercase prefix.

    Notes:
        - This function assumes the input `code` contains a valid prefix 
          (either before "_" or before ":").
        - If the input code does not match expected formats, it is returned 
          unchanged.
        - Supports common ontologies like SNOMED, LOINC, MONDO, ICD, and HP.

    Examples:
        >>> process_redcap_code("loinc_81304_8", "loinc")
        'LOINC:81304-8'

        >>> process_redcap_code("icd10cm_r51_1", "icd10cm")
        'ICD10CM:R51.1'

        >>> process_redcap_code("HP:0004322", "hp")
        'HP:0004322'

        >>> process_redcap_code("ORDO_56789", "ordo")
        'ORDO:56789'
    """
    if not code or not prefix:
        return code  # Return the original code if inputs are invalid.

    # Capitalize the prefix
    prefix_upper = prefix.upper()

    # Handle the transformation based on prefix
    if code.startswith(f"{prefix}_") or code.startswith(f"{prefix.upper()}_"):
        # Replace the first "_" with ":"
        processed_code = code.replace("_", ":", 1)

        # Special handling for LOINC: Replace subsequent "_" with "-"
        if prefix_upper == "LOINC":
            processed_code = processed_code.replace("_", "-")

        # Special handling for ICD codes: Replace subsequent "_" with "."
        elif prefix_upper in ["ICD10CM", "ICD11", "ICD10", "ICD9"]:
            processed_code = processed_code.replace("_", ".").upper()

        return f"{prefix_upper}:{processed_code.split(':', 1)[1]}"

    # If the code is already in the correct format, ensure prefix is uppercase
    if ":" in code:
        parts = code.split(":", 1)
        return f"{prefix_upper}:{parts[1]}"

    return code  # Default case: return as-is if no transformations apply.
