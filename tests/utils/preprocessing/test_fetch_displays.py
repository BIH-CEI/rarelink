from rarelink.utils.preprocessing.fetch_displays import fetch_display_for_code

def main():
    # Replace with your actual BioPortal API token

    bioportal_token = "459b70e9-ac04-4d33-b9e8-22f953af4105"

    # Sample ontology codes to fetch labels for
    codes = ["MONDO:0019391", "SNOMED:106221001", "HP:0000118"]

    for code in codes:
        label = fetch_display_for_code(code, bioportal_token)
        print(f"Code: {code}, Label: {label}")

if __name__ == "__main__":
    main()
