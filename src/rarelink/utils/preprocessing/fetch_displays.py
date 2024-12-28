from oaklib import get_adapter

def fetch_display_for_code(code: str, bioportal_token: str) -> str:
    """
    Fetch the display name (label) for a given ontology code using OAK and BioPortal.
    """
    try:
        print(f"Fetching label for code: {code}")

        if code.startswith("RARELINK:"):
            return None
        
        # Initialize the adapter
        adapter = get_adapter(f"bioportal:{bioportal_token}")

        # Fetch the label
        label = adapter.label(code)
        print(f"Fetched label: {label}")

        return label
    except Exception as e:
        print(f"Error fetching display for {code}: {e}")
        return None

if __name__ == "__main__":
    import sys

    # Ensure the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python fetch_displays.py <CODE> <BIOPORTAL_TOKEN>")
        sys.exit(1)

    # Extract arguments from the command line
    code = sys.argv[1]
    bioportal_token = sys.argv[2]

    # Call the function and print the result
    label = fetch_display_for_code(code, bioportal_token)
    print(f"Code: {code}, Label: {label}")


def fetch_displays_for_records(records: list, bioportal_token: str) -> list:
    """
    Fetch display names for all ontology codes in a list of records.

    Args:
        records (list): List of records containing ontology codes.
        bioportal_token (str): BioPortal API token.

    Returns:
        list: Records enriched with display names.
    """
    enriched_records = []
    for record in records:
        enriched_record = record.copy()
        for key, value in record.items():
            if isinstance(value, str) and ':' in value:
                display = fetch_display_for_code(value, bioportal_token)
                enriched_record[f"{key}_display"] = display
        enriched_records.append(enriched_record)
    return enriched_records
