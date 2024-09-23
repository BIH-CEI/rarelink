from pathlib import Path
from typing import Union, List

from phenopackets.schema.v2 import Phenopacket

from phenopacket_mapper.mapping.mapper import PhenopacketMapper
from rarelink.rarelink_cdm import rarelink_cdm_v2_0_0

from rarelink.preprocessing import preprocess_redcap_for_phenopacket_pipeline


def phenopacket_pipeline(path: Union[str, Path]) -> List[Phenopacket]:
    # # 1. preprocess data 
    # preprocessed_path = preprocess_redcap_for_phenopacket_pipeline(path)
    # # 2. load preprocessed data
    # data_set = rarelink_cdm_v2_0_0.load_data(preprocessed_path)
    # print("idsd of the fields in the data model: \n", 
    #       data_set.data_model.get_field_ids())
    # #
    # # 3. Define the Mapping 
    # # WIP in Phenopacket_Mapper
    # phenopacket_mapper = PhenopacketMapper(
    #     data_set,
    #     id=data_set.pseudonym,
    #     subject=PhenopacketElement(
    #         phenopacket_element=phenopacket.Individual,
    #         date_of_birth=data_set.date_of_birth,
    #         # TODO do tthis for entire data model
    #     )                       
    # )
    # # 4. map data
    # # 5. Validate Phenoppackets
    # # 6. return Phenopackets  phenopacket_mapper.map()
    
    # return phenopackets
    return NotImplementedError