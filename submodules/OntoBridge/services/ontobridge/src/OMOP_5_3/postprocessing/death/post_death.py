from src.OMOP_5_3.postprocessing.share.utils import change_hour

def post_death(table_df):

    change_hour(table_df)

    if "death_type_concept_id" in table_df.columns:
        table_df["death_type_concept_id"]=table_df["death_type_concept_id"].fillna("32817")  

    return table_df
