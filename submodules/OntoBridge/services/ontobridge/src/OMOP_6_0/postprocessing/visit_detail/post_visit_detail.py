from src.OMOP_6_0.postprocessing.share.utils import erase_column_unnamed, erase_quotes, change_hour

def post_visit_detail(table_df):
    table_df = erase_column_unnamed(table_df)
    table_df = erase_quotes(table_df)
    table_df = change_hour(table_df)
    if "visit_detail_source_concept_id" in table_df.columns:
        table_df["visit_detail_source_concept_id"] = table_df["visit_detail_source_concept_id"].fillna("0")
    if "admitted_from_source_value" in table_df.columns:
        table_df["admitted_from_source_value"] = table_df["admitted_from_source_value"].fillna("0")
    if "discharge_to_concept_id" in table_df.columns:
        table_df["discharge_to_concept_id"] = table_df["discharge_to_concept_id"].fillna("0")
    if "visit_detail_type_concept_id" in table_df.columns:
        table_df["visit_detail_type_concept_id"] = table_df["visit_detail_type_concept_id"].fillna("32817")

    return table_df
