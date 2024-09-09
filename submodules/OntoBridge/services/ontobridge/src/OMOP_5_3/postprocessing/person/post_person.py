from src.OMOP_5_3.postprocessing.share.utils import change_hour
import pandas as pd

def post_person(table_df):
    table_df = change_hour(table_df)
    if "race_concept_id" in table_df.columns:
        table_df["race_concept_id"] = table_df["race_concept_id"].fillna("0")
    
    if "gender_source_concept_id" in table_df.columns:
        table_df["gender_source_concept_id"] = table_df["gender_source_concept_id"].fillna("0")

    if "race_source_concept_id" in table_df.columns:
        table_df["race_source_concept_id"] = table_df["race_source_concept_id"].fillna("0")

    if "ethnicity_source_concept_id" in table_df.columns:
        table_df["ethnicity_source_concept_id"] = table_df["ethnicity_source_concept_id"].fillna("0")

    if "ethnicity_concept_id" in table_df.columns:
        table_df["ethnicity_concept_id"] = table_df["ethnicity_concept_id"].fillna("0")

    if "year_of_birth" in table_df.columns:
        table_df["year_of_birth"] = table_df["year_of_birth"].apply(lambda x: int(pd.to_datetime(x).year) if isinstance(x, str) else int(x))

    if "month_of_birth" in table_df.columns:
        table_df["month_of_birth"] = table_df["month_of_birth"].apply(lambda x: int(pd.to_datetime(x).month) if isinstance(x, str) else int(x))

    if "day_of_birth" in table_df.columns:
        table_df["day_of_birth"] = table_df["day_of_birth"].apply(lambda x: int(pd.to_datetime(x).day) if isinstance(x, str) else int(x))
    
    return table_df
