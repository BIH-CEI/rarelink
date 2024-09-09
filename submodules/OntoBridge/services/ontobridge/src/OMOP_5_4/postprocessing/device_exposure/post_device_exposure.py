from src.OMOP_5_4.postprocessing.share.utils import erase_column_unnamed, erase_quotes, change_hour
import pandas as pd

def handle_duplicate_ids(table_df, id_column='device_exposure_id'):
    table_df[id_column] = pd.to_numeric(table_df[id_column], errors='coerce').astype(pd.Int64Dtype())

    max_id = table_df[id_column].max()
    new_id = max_id + 1

    duplicate_ids = table_df[id_column][table_df[id_column].duplicated(keep='first')].unique()

    for dup_id in duplicate_ids:
        duplicate_indices = table_df.index[table_df[id_column] == dup_id].tolist()
        for idx in duplicate_indices[1:]:  # Leave the first occurrence, update the rest
            table_df.at[idx, id_column] = new_id
            new_id += 1
    return table_df

def post_device_exposure(table_df):
    table_df = erase_column_unnamed(table_df)
    table_df = erase_quotes(table_df)
    table_df = change_hour(table_df)

    if "device_source_concept_id" in table_df.columns:
        table_df["device_source_concept_id"]=table_df["device_source_concept_id"].fillna("0")
    if "device_type_concept_id" in table_df.columns:
        table_df["device_type_concept_id"]=table_df["device_type_concept_id"].fillna("32817")
    if "unit_concept_id" in table_df.columns and "unit_source_value" in table_df.columns:
        table_df.loc[
            (table_df["unit_source_value"].notnull()) & (table_df["unit_concept_id"].isnull()), 
            "unit_concept_id"
        ] = 0
    table_df = handle_duplicate_ids(table_df)

    return table_df
