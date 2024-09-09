from src.OMOP_6_0.postprocessing.share.utils import erase_column_unnamed, erase_quotes, change_hour
import pandas as pd

def post_observation_period(table_df):
    #table_df = erase_column_unnamed(table_df)
    #table_df = erase_quotes(table_df)
    table_df = change_hour(table_df)



    table_df = table_df.groupby("person_id").agg(
        observation_period_start_date=("visit_start_date", "min"),
        observation_period_end_date=("visit_end_date", "max"),
    ).reset_index()


    # Agregar la columna "observation_period_id" con valores incrementales
    table_df.insert(0, "observation_period_id", range(1, len(table_df) + 1))

    # Agregar la columna "period_type_concept_id" con el valor "32817"
    table_df["period_type_concept_id"] = "32817"
    
    # Generar id obvservation
    return table_df

