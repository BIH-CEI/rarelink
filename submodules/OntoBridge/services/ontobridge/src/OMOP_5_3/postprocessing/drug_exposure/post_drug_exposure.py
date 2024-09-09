import pandas as pd
from src.OMOP_5_3.postprocessing.share.utils import erase_column_unnamed, erase_quotes, change_hour

def handle_duplicate_ids(table_df, id_column='drug_exposure_id'):
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

def post_drug_exposure(table_df):
    table_df = erase_column_unnamed(table_df)
    table_df = erase_quotes(table_df)
    table_df = change_hour(table_df)

    if "drug_concept_id" in table_df.columns:  
        table_df["drug_concept_id"] = table_df["drug_concept_id"].fillna("0")
    if "drug_source_concept_id" in table_df.columns:
        table_df["drug_source_concept_id"] = table_df["drug_source_concept_id"].fillna("0")
    if "days_supply" in table_df.columns:
        table_df["days_supply"] = table_df["days_supply"].fillna("1")
    if "drug_type_concept_id" in table_df.columns:
        table_df["drug_type_concept_id"]=table_df["drug_type_concept_id"].fillna("32817")

    if "drug_exposure_start_datetime" in table_df.columns:
        table_df['drug_exposure_start_datetime'] = pd.to_datetime(table_df['drug_exposure_start_datetime'], errors='coerce')
        table_df['drug_exposure_start_date'] = table_df['drug_exposure_start_datetime'].dt.date

    if "drug_exposure_end_datetime" in table_df.columns:
        table_df['drug_exposure_end_datetime'] = pd.to_datetime(table_df['drug_exposure_end_datetime'], errors='coerce')
        table_df['drug_exposure_end_date'] = table_df['drug_exposure_end_datetime'].dt.date

    table_df = handle_duplicate_ids(table_df)

    return table_df

