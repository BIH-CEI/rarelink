from pathlib import Path
from typing import Union, List

from phenopackets.schema.v2 import Phenopacket

from rarelink.rarelink_cdm import rarelink_cdm_v2_0_0

from rarelink.preprocessing import preprocess_redcap_for_phenopacket_pipeline


def phenopacket_pipeline(path: Union[str, Path]) -> List[Phenopacket]:
    # 0. load data using data model
    rl_data_set = rarelink_cdm_v2_0_0.load_data(path)
    # 1. preprocessing
    df = preprocess_redcap_for_phenopacket_pipeline(rl_data_set)
    # 2. mapping
    phenopackets = []

    for index, row in df.iterrows():
        # Create a Phenopacket for each row
        phenopacket = Phenopacket(
            id=f"phenopacket-{index}",  # Example ID; you may want to change it
            # Fill in other fields of the Phenopacket based on your DataFrame
            subject={
                "id": row.get("Pseudonym"),
                "date_of_birth": row.get("Date of Birth"),
                "sex": row.get("Sex at Birth"),
            },
            # Add other relevant fields from the DataFrame
            # For example, mapping disease and genetic findings:
            disease={
                "id": row.get("Disease"),
                "verification_status": row.get("Verification Status"),
                "age_at_onset": row.get("Age at Onset"),
            },
            # Add more mapping based on your schema requirements
        )
        
        # Append the Phenopacket to the list
        phenopackets.append(phenopacket)
    
    return phenopackets