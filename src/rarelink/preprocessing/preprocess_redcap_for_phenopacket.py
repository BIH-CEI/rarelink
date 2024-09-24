

import pandas as pd
from pathlib import Path
from typing import List, Union

from phenopacket_mapper.data_standards import DataSet
from phenopacket_mapper.data_standards.code_system import CodeSystem
from rarelink.preprocessing import preprocess_redcap_codes


def preprocess_redcap_for_phenopackets(
        data_set: DataSet,
        resources: List[CodeSystem]
):
    """Preprocess REDCap data for the phenopacket pipeline.

    :param ds: A pandas DataFrame with REDCap data loaded in the Rarelink data model.
    """
    data_model = data_set.data_model

    # preprocess using dict
    data_set.preprocess(
        fields=data_model.karyotypic_sex,
        mapping={
            "snomed_734875008": "XX",
            # TODO:  ADD THE REST
        }
    )
    # preprocess using func
    data_set.preprocess(
        fields=data_model.gender_identity,
        mapping=preprocess_redcap_codes,
        resources=resources,
    )
    # preprocess mutliple cols
    def preferable_codesystem(values):
        orpha, snomed, c, d = values
        if orpha:
            return orpha
        elif snomed:
            return snomed
        elif c:
            return c
        elif d:
            return d
        raise ValueError("All values passed are None")

    data_set.preprocess(
        fields=[
            data_model.age_at_event,
            data_model.age_at_event_years,
            data_model.age_at_event_months,
            data_model.age_at_event_days,
        ],
        mapping=preferable_codesystem,
    )
        

    # TODO @aslgrafe: handle ds.data_frame preprocessing
    # 1. read csv file from inputpath
    # 2. preprocess the data frame
    # 3. save the preprocessed data frame to output path
    # 4. return the output path
    raise NotImplementedError


# product of this function is the preprocessed data frame saved a csv or what ever to be used by the phenopaxcket pipeline.py 
# upload data -> preprocess -> output locally -> output of this function: path of precprocessed data