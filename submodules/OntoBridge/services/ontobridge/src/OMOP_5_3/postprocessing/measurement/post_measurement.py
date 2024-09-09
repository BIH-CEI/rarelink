import pandas as pd
from src.OMOP_5_3.postprocessing.share.utils import erase_column_unnamed, erase_quotes, change_hour

NAMEFILE1 = "MEASUREMENT-concept"
NAMEFILE2 = "MEASUREMENT-number"

CODS_EXCEPTIONS = ["3003396",
                    "3004959",
                    "3012501",
                    "3003129",
                    "3002032",
                    "3007435",
                    "3051343",
                    "21494211",
                    "21494205",
                    "21492970",
                    "21494210",
                    "21494204",
                    "21492969",
                    "3052504",
                    "3049581",
                    "21494209",
                    "21494203",
                    "21492968",
                    "21494208",
                    "21494202",
                    "21494199",
                    "3021722",
                    "3051450",
                    "21494100",
                    "3051938",
                    "21494201",
                    "21494198",
                    "3049418",
                    "21494200",
                    "21494197",
                    "3052486",
                    "3049278",
                    "21494099",
                    "36203243",
                    "36203246",
                    "36204416",
                    "36203244",
                    "36203245",
                    "36204415",
                    "36203242",
                    "36204445",
                    "36204414",
                    "3033804",
                    "3049654",
                    "36204417",
                    "21494207",
                    "21492972",
                    "21494196",
                    "21494206",
                    "21492971",
                    "21494101",
                    "3002101",
                    "3049273",
                    "21494098",
                    "3006277",
                    "3028303",
                    "3025448"
                    ]

def read_dataframe(file_path, dtype=None):
    try:
        data = pd.read_csv(file_path, dtype=dtype)
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

def get_dataframe(read_folder):
    data_concept = read_dataframe(read_folder + "/" + NAMEFILE1 + ".csv", dtype={"value_as_concept_id": pd.Int64Dtype()})
    data_number = read_dataframe(read_folder + "/" + NAMEFILE2 + ".csv", dtype={"value_as_number": float})
    
    if data_concept is None or data_number is None:
        return None
    
    table_df = pd.concat([data_concept, data_number], ignore_index=True)
    return table_df

def handle_value_as_concept_id(table_df):
    if "value_as_concept_id" in table_df.columns:
        table_df["value_as_concept_id"] = table_df["value_as_concept_id"].astype(pd.Int64Dtype())
    return table_df

def handle_duplicate_ids(table_df, id_column='measurement_id'):
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

def post_measurement(read_folder):
    table_df = get_dataframe(read_folder)
    table_df = change_hour(table_df)
    if "value_as_number" in table_df.columns:
        table_df["value_as_number"] = pd.to_numeric(table_df["value_as_number"], errors = "coerce")
        condition = (table_df["value_as_number"] < 0) & (~table_df['measurement_concept_id'].isin(CODS_EXCEPTIONS)
)
        table_df.loc[condition, "value_as_number"] = None 
    if "range_high" in table_df.columns:
       condition = pd.isnull(table_df["range_high"]) & pd.notnull(table_df['value_as_number'])
       table_df.loc[condition, "range_high"] = None 

    if "range_low" in table_df.columns:
       condition = pd.isnull(table_df["range_low"]) & pd.notnull(table_df['value_as_number'])
       table_df.loc[condition, "range_low"] = None 

    if "measurement_type_concept_id" in table_df.columns:
        table_df["measurement_type_concept_id"]=table_df["measurement_type_concept_id"].fillna("32817")  

    table_df = handle_value_as_concept_id(table_df)
    table_df = handle_duplicate_ids(table_df)

    return table_df
