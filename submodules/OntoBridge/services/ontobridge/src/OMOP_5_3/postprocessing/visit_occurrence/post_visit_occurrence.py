from src.OMOP_5_3.postprocessing.share.utils import erase_column_unnamed, erase_quotes, change_hour

def post_visit_occurrence(table_df):
    table_df = erase_column_unnamed(table_df)
    table_df = erase_quotes(table_df)
    table_df = change_hour(table_df)

    if "visit_source_concept_id" in table_df.columns:
        table_df["visit_source_concept_id"] = table_df["visit_source_concept_id"].fillna("0")
    if "admitting_concept_id" in table_df.columns:
        table_df["admitting_concept_id"] = table_df["admitting_concept_id"].fillna("0")
    if "discharge_to_concept_id" in table_df.columns:
        table_df["discharge_to_concept_id"] = table_df["discharge_to_concept_id"].fillna("0")
    if "visit_type_concept_id" in table_df.columns:
        table_df["visit_type_concept_id"]=table_df["visit_type_concept_id"].fillna("32817")

    return table_df
