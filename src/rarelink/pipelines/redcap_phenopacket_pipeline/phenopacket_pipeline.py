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

    # Group by record_id and redcap_repeat_instrument to handle repeated instruments
    grouped_data = df.groupby(['record_id', 'redcap_repeat_instrument'])

    # 2. mapping
    phenopackets = []

    # Iterate over each group (i.e., each combination of record and instrument)
    for (record_id, instrument), group in grouped_data:
        # Initialize placeholders for the mapped data
        subject_data = {}
        disease_data = {}
        phenotypic_features = []
        
        # Iterate over the rows in the group (each row is a repeated instance)
        for _, row in group.iterrows():
            # Example: Map relevant fields based on the instrument type and instance
            if instrument == 'formal_criteria':
                subject_data['id'] = row.get('snomed_422549004')  # Pseudonym
                subject_data['date_of_birth'] = row.get('snomed_184099003')  # Date of Birth
            
            elif instrument == 'disease':
                disease_data['id'] = row.get('snomed_64572001_mondo')  # Disease MONDO
                disease_data['verification_status'] = row.get('snomed_64572001_ordo')  # Verification status (example)
                
            elif instrument == 'phenotypic_feature':
                phenotypic_features.append({
                    'id': row.get('ga4gh_pheno_mod_hp1'),  # Phenotypic feature HP
                    'status': row.get('ga4gh_pheno_mod_hp2')  # Phenotypic status (example)
                })

        # Create the Phenopacket object after gathering all relevant data for this record
        phenopacket = Phenopacket(
            id=f"phenopacket-{record_id}-{instrument}",  # Create a unique ID
            subject=subject_data,  # Subject information
            disease=[disease_data],  # Disease information (can be a list of diseases)
            phenotypic_features=phenotypic_features  # List of phenotypic features
        )
        
        # Append the created Phenopacket to the list
        phenopackets.append(phenopacket)
    
    return phenopackets