"""
This dictionary contains the "description field" of the RareLink-CDM v2.0.0.dev0
LinkML schema, to fetch the label for writing Phenopackets.
    
"""

label_dicts = {
    "GenderIdentity": {
        "snomed_446141000124107": "Female gender identity",
        "snomed_446151000124109": "Male gender identity",
        "snomed_394743007": "Gender unknown",
        "snomed_33791000087105": "Identifies as nonbinary gender",
        "snomed_1220561009": "Not recorded",
    },
    "AgeAtOnset": {
        "snomed_118189007": "Prenatal",
        "snomed_3950001": "Birth",
        "snomed_410672004": "Date",
        "snomed_261665006": "Unknown",
    }
}
