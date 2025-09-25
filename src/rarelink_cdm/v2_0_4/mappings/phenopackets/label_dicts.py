"""
This dictionary contains the "description field" of the RareLink-CDM v2.0.4
LinkML schema, to fetch the label for writing Phenopackets.
    
"""

label_dicts = {
    "GenderIdentity": {
        "snomedct_446141000124107": "Female gender identity",
        "snomedct_446151000124109": "Male gender identity",
        "snomedct_394743007": "Gender unknown",
        "snomedct_33791000087105": "Identifies as nonbinary gender",
        "snomedct_1220561009": "Not recorded",
    },
    "AgeAtOnset": {
        "snomedct_118189007": "Prenatal",
        "snomedct_3950001": "Birth",
        "snomedct_410672004": "Date",
        "snomedct_261665006": "Unknown",
    },
    "Zygosity": {
        "GENO:0000136": "Homozygous",
        "GENO:0000458": "simple Heterozygous",
        "GENO:0000402": "compound heterozygous",
        "GENO:0000135": "Heterozygous",
        "GENO:0000134": "Hemizygous",
        "GENO:0000603": "Heteroplasmic",
        "GENO:0000602": "Homoplasmic",
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
    },
    "AgeOfOnset": {
        "hp_0011460": "Embryonal onset (0w-8w embryonal)",
        "hp_0011461": "Fetal onset (8w embryonal - birth)",
        "hp_0003577": "Congenital onset (at birth)",
        "hp_0003623": "Neonatal onset (0d-28d)",
        "hp_0003593": "Infantile onset (28d-1y)",
        "hp_0011463": "Childhood onset (1y-5y)",
        "hp_0003621": "Juvenile onset (5y-15y)",
        "hp_0011462": "Young adult onset (16y-40y)",
        "hp_0003596": "Middle age adult onset (40y-60y)",
        "hp_0003584": "Late adult onset (60y+)"
    },
    "TemporalPattern": {
        "hp_0011009": "Acute",
        "hp_0011010": "Chronic",
        "hp_0031914": "Fluctuating",
        "hp_0025297": "Prolonged",
        "hp_0031796": "Recurrent",
        "hp_0031915": "Stable",
        "hp_0011011": "Subacute",
        "hp_0025153": "Transient"
    },
    "PhenotypeSeverity": {
        "hp_0012827": "Borderline",
        "hp_0012825": "Mild",
        "hp_0012826": "Moderate",
        "hp_0012829": "Profound",
        "hp_0012828": "Severe"
    }
}

