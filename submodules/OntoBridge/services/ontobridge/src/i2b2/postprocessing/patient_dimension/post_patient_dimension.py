import pandas as pd 
from datetime import datetime
from src.i2b2.postprocessing.share.utils import *

from datetime import datetime

def calculate_age(birth_date, death_date=None):
    if not isinstance(birth_date, str):
        raise TypeError(f"Expected a string for birth_date, got {type(birth_date)} instead.")
    if death_date is not None and not isinstance(death_date, str):
        raise TypeError(f"Expected a string for death_date, got {type(death_date)} instead.")
    
    birth_date = birth_date.replace('T', ' ')
    birth_datetime = datetime.strptime(birth_date.split(" ")[0], "%Y-%m-%d")
    
    if death_date:
        death_date = death_date.replace('T', ' ')
        death_datetime = datetime.strptime(death_date.split(" ")[0], "%Y-%m-%d")
    else:
        death_datetime = datetime.today()
    
    age = death_datetime.year - birth_datetime.year
    
    if (death_datetime.month, death_datetime.day) < (birth_datetime.month, birth_datetime.day):
        age -= 1 
    
    return age

def post_patient_dimension(table_df):
    table_df = erase_column_unnamed(table_df)
    table_df = erase_quotes(table_df)

    if "birth_date" in table_df.columns:
        def safe_calculate_age(row):
            birth_date = row["birth_date"]
            death_date = row.get("death_date")  # Usamos .get para evitar errores si "death_date" no existe
            if isinstance(birth_date, str) and (death_date is None or isinstance(death_date, str)):
                return calculate_age(birth_date, death_date)
            else:
                return None

        table_df["age_in_years_num"] = table_df.apply(lambda row: safe_calculate_age(row), axis=1)

    if "vital_status_cd" in table_df.columns:
        table_df.loc[table_df["death_date"].notna(), "vital_status_cd"] = "D"

    return table_df
