

import pandas as pd


class DataSet:
    # TODO replace with import from phenopacket_mapper.data_standards later
    pass


def preprocess_redcap_for_phenopacket_pipeline(ds: DataSet) -> pd.DataFrame:
    """Preprocess REDCap data for the phenopacket pipeline.

    :param ds: A pandas DataFrame with REDCap data loaded in the Rarelink data model.
    """
    # TODO @aslgrafe: handle ds.data_frame preprocessing
    # df = ds.data_frame
    raise NotImplementedError