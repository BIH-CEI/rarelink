from pathlib import Path
from typing import Union, List

from phenopackets.schema.v2 import Phenopacket

from rarelink.pipelines import RARELINK_DATAMODEL_2_0

from rarelink.preprocessing import preprocess_redcap_for_phenopacket_pipeline


def phenopacket_pipeline(path: Union[str, Path], rarelink_data_model=RARELINK_DATAMODEL_2_0) -> List[Phenopacket]:
    # 0. load data using data model
    rl_data_set = rarelink_data_model.load_data(path)
    # 1. preprocessing
    df = preprocess_redcap_for_phenopacket_pipeline(rl_data_set)  # TODO: uncomment
    # 2. mapping
    raise NotImplementedError