"""
This dictionary contains the "description field" of the RareLink-CDM v2.0.0.dev1
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
    },
    "InactivatedVaccineType": {
        "vo_0000738": "DTap (Diphtheria, Tetanus, Acellular Pertussis)",
        "vo_0000662": "Haemophilus Influenza Type b",
        "vo_0010211": "PrevNar/Pneu-C-13",
        "vo_0006041": "PrevNar/Pneu-C-15",
        "vo_0010356": "PrevNar/Pneu-C-20",
        "vo_0010440": "V116, Pneu-21",
        "vo_0006033": "Men-C",
        "vo_0010205": "Men-B",
        "vo_0010727": "Meningococcal Quadrivalent Vaccine",
        "vo_0000667": "HPV",
        "vo_0000644": "Hepatitis B",
        "vo_0003196": "Acellular Pertussis",
        "vo_0000664": "IPV (Polio)",
        "vo_0000088": "Pneumovax",
        "vo_0004908": "COVID-19",
        "vo_0000642": "Flu",
        "other": "Other"
    },
    "LiveVaccineType": {
        "vo_0010209": "Oral Polio vaccine",
        "vo_0000731": "MMR (Measles, Mumps, Rubella)",
        "vo_0021165": "Varicella",
        "vo_0000433": "Vaccinia",
        "vo_0000771": "BCG",
        "vo_0000123": "Yellow Fever",
        "vo_0003495": "Influenza",
        "vo_0000658": "Rotavirus",
        "other": "Other"
    },
    "UnitOfMeasure": {
        "uo_0000208": "gram per deciliter",
        "uo_0000179": "count per microliter",
        "uo_0000187": "percentage",
        "uo_0000176": "picomole per liter",
        "uo_0000098": "millimole per liter",
        "uo_0000064": "microgram per deciliter",
        "uo_0000228": "ratio",
        "uo_0010004": "international unit per liter",
        "uo_0000275": "nanogram per milliliter"
    },
    "LabAssayType": {
        "loinc_718_7": "Hemoglobin Concentration",
        "loinc_777-3": "Platelet Count",
        "loinc_6690_2": "White Blood Cell Count",
        "loinc_26499_4": "Neutrophil Count",
        "loinc_26449_9": "Eosinophil Count",
        "loinc_26474_7": "Lymphocyte Count",
        "loinc_26484_6": "Monocyte Count", 
        "loinc_8122_4": "CD3 Lymphocytes",
        "loinc_24467_3": "CD4 Lymphocytes",
        "loinc_14135_8": "CD8 Lymphocytes", 
        "loinc_8116_6": "CD19 B-Lymphocytes",
        "loinc_9558_8": "Natural Killer Cells",
        "loinc_9728_7": "T-cell Function",
        "ncit_c88791": "NK Cytotoxicity",
        "ncit_c74017": "CD4 Function",
        "ncit_c88774": "TNF Response to LPS",
        "ncit_c88789": "IL-12 Response",
        "ncit_c17166": "Lymphocyte Proliferation",
        "ncit_c85185": "T-cell Response",
        "ncit_c34541": "B-cell Function",
        "ncit_c77163": "IFN-gamma Production",
        "ncit_c116203": "STAT Phosphorylation"
    },
    "LabValueStatus": {
        "ncit_c54722": "Low",
        "ncit_c14165": "Normal",
        "ncit_c48190": "Absent",
        "ncit_c25482": "High"
    },
    "InterpretationStatus": {
        "ncit_c78800": "Normal",
        "ncit_c78801": "Abnormal",
        "ncit_c78727": "Pending"
    }
}

