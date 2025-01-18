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
    },
    "Zygosity": {
        "loinc_53034_5_other": "Other",
        "loinc_la6705-3": "Homozygous",
        "loinc_la6706-1": "(simple) Heterozygous",
        "loinc_la26217-2": "Compound heterozygous",
        "loinc_la26220-6": "Double heterozygous",
        "loinc_la6707-9": "Hemizygous",
        "loinc_la6703-8": "Heteroplasmic",
        "loinc_la6704-6": "Homoplasmic",
    },
    "DNAChangeType": {
        "loinc_la9658-1": "Wild type",
        "loinc_la6692-3": "Deletion",
        "loinc_la6686-5": "Duplication",
        "loinc_la6687-3": "Insertion",
        "loinc_la6688-1": "Insertion/Deletion",
        "loinc_la6689-9": "Inversion",
        "loinc_la6690-7": "Substitution",
    },
    "ReferenceGenome": {
        "loinc_la14032-9": "NCBI Build 34 (hg16)",
        "loinc_la14029-5": "GRCh37 (hg19)",
        "loinc_la14030-3": "NCBI Build 36.1 (hg18)",
        "loinc_la14031-1": "NCBI Build 35 (hg17)",
        "loinc_la26806-2": "GRCh38 (hg38)",
    }
}

