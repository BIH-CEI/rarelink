

import pandas as pd
from pathlib import Path
from typing import Union



class DataSet:
    # TODO replace with import from phenopacket_mapper.data_standards later
    pass


def preprocess_redcap_for_phenopacket_pipeline(
        input_path: Union[str, Path], 
        output_path: Union[str, Path]
) -> Union[str, Path]:
    """Preprocess REDCap data for the phenopacket pipeline.

    :param ds: A pandas DataFrame with REDCap data loaded in the Rarelink data model.
    """
    # TODO @aslgrafe: handle ds.data_frame preprocessing
    # 1. read csv file from inputpath
    # 2. preprocess the data frame
    # 3. save the preprocessed data frame to output path
    # 4. return the output path
    raise NotImplementedError


# product of this function is the preprocessed data frame saved a csv or what ever to be used by the phenopaxcket pipeline.py 
# upload data -> preprocess -> output locally -> output of this function: path of precprocessed data