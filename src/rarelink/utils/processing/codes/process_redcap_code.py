def process_redcap_code(code: str) -> str:
    """
    Processes a REDCap code by dynamically extracting the prefix and ensuring it 
    has the correct format, applying specific transformations based on the prefix type.

    Args:
        code (str): The code to process. Expected formats include:
            - "prefix_code" (e.g., "UO_1234", "loinc_81304_8")
            - "prefix:code" (e.g., "HP:0004322")
            - Mixed case inputs for prefixes (e.g., "Loinc_81304_8", 
              "ICD10cm_r51_1")

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
        >>> process_redcap_code("loinc_81304_8")
        'LOINC:81304-8'

        >>> process_redcap_code("icd10cm_r51_1")
        'ICD10CM:R51.1'

        >>> process_redcap_code("HP:0004322")
        'HP:0004322'

        >>> process_redcap_code("ORDO_56789")
        'ORDO:56789'
    """
    if not code:
        return code  # Return the original code if input is invalid.

    # Determine prefix from the code
    delimiter = "_" if "_" in code else ":" if ":" in code else None
    if not delimiter:
        return code  # Return as-is if no valid delimiter found.

    prefix, rest = code.split(delimiter, 1)
    prefix_upper = prefix.upper()

    # Handle the transformation based on prefix
    if delimiter == "_":
        # Replace the first "_" with ":"
        processed_code = f"{prefix_upper}:{rest}"

        # Special handling for LOINC: Replace subsequent "_" with "-"
        if prefix_upper == "LOINC":
            processed_code = processed_code.replace("_", "-")

        # Special handling for ICD codes: Replace subsequent "_" with "."
        elif prefix_upper in ["ICD10CM", "ICD11", "ICD10", "ICD9"]:
            processed_code = f"{prefix_upper}:{rest.replace('_', '.').upper()}"
            
        elif prefix_upper == "SNOMED":
            prefix_upper = "SNOMEDCT"
            processed_code = f"{prefix_upper}:{rest}"
            
        return processed_code

    elif delimiter == ":":
        # Ensure prefix is uppercase and return
        return f"{prefix_upper}:{rest}"

    return code  # Default case: return as-is if no transformations apply.
