FIELD_MAPPINGS = {
    "rarelink_1_formal_criteria": {
        "fields": [
            "snomed_422549004",
            "snomed_399423000",
            "rarelink_1_formal_criteria_complete"
        ]
    },
    "rarelink_2_personal_information": {
        "fields": [
            "snomed_184099003",
            "snomed_281053000",
            "snomed_1296886006",
            "snomed_263495000",
            "snomed_370159000",
            "rarelink_2_personal_information_complete"
        ]
    },
    "rarelink_3_patient_status": {
        "fields": [
            "patient_status_date",
            "snomed_278844005",
            "snomed_398299004",
            "snomed_184305005",
            "snomed_105727008",
            "snomed_412726003",
            "snomed_723663001",
            "rarelink_3_patient_status_complete"
        ],
        "repeated": True  # Marks it as repeatable
    }
    # Add future schemas here
}
