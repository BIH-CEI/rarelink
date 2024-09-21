from pathlib import Path
from typing import Union, List

from phenopackets.schema.v2 import Phenopacket

from rarelink.pipelines import rarelink_cdm_2_0

from rarelink.preprocessing import preprocess_redcap_for_phenopacket_pipeline


def phenopacket_pipeline(path: Union[str, Path], rarelink_data_model=rarelink_cdm_2_0) -> List[Phenopacket]:
    # 0. load data using data model
    # rl_data_set = rarelink_data_model.load_data(path)  # TODO: once implemented in phenopacket_mapper,
                                                        #  TODO: uncomment this line
    # 1. preprocessing
    # df = preprocess_redcap_for_phenopacket_pipeline(rl_data_set)  # TODO: uncomment
    # 2. mapping
    raise NotImplementedError