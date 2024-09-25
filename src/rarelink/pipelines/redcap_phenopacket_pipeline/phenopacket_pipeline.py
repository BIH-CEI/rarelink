from pathlib import Path
from typing import Union, List
from phenopackets.schema.v2 import Phenopacket
from phenopackets.schema.v2 import phenopackets
from phenopacket_mapper.mapping.mapper import PhenopacketMapper, PhenopacketElement
from rarelink.preprocessing.preprocess_redcap_for_phenopackets import preprocess_redcap_for_phenopackets
from rarelink.rarelink_cdm import RARELINK_CDM_V2_0_0
from rarelink.preprocessing import preprocess_redcap_for_phenopackets
from rarelink.rarelink_cdm.rarelink_cdm import load_rarelink_data
from rarelink.rarelink_cdm.rarelink_cdm_phenopacket_mapping import rarelink_cdm_multiple_fields

# TODO: implement functions from processing and preferencing for multiple values
# TODO: create another class for the Mapping Definition 

def phenopacket_pipeline(path: Union[str, Path]) -> List[Phenopacket]:
    # 1. load data
    data_model = RARELINK_CDM_V2_0_0
    data_set = load_rarelink_data(path)
    print("idsd of the fields in the data model: \n", 
          data_model.data_model.get_field_ids())
    # 2. Preprocessing
    preprocess_redcap_for_phenopackets(data_set)
    
    # 3. Define the Mapping 
    

    # return phenopackets
    # return NotImplementedError

