import pandas as pd 

from src.OMOP_5_4.postprocessing.share.utils import erase_column_unnamed, erase_quotes, change_hour

NAMEFILE1 = "OBSERVATION-concept"
NAMEFILE2 = "OBSERVATION-number"
NAMEFILE3 = "OBSERVATION-string"

def get_dataframe(read_folder):
    # TODO: Check if neither file exists 
    data_concept = read_dataframe(read_folder, NAMEFILE1)
    print(data_concept)
    data_number = read_dataframe(read_folder, NAMEFILE2)
    print(data_number)
    table_df = pd.concat([data_concept, data_number])

    # data_string = read_dataframe(read_folder, NAMEFILE3)
    # if data_string != None:
    #     table_df = pd.concat([table_df, data_string])

    return table_df

def read_dataframe(read_folder, namefile):
    print(read_folder + namefile +".csv")
    try:
        data = pd.read_csv(read_folder + namefile +".csv", dtype = {'value_as_concept_id':int}) 
        ##data = erase_column_unnamed(data)
        # return erase_quotes(data)
        return data
    except Exception as e:
        print(e)
        print("Does not exist the file:")
        print(namefile)
        return None

def handle_duplicate_ids(table_df, id_column='observation_id'):
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


def post_observation(read_folder):
    table_df = get_dataframe(read_folder)
    table_df = change_hour(table_df)
    print(table_df.head())
    if "observation_source_concept_id" in table_df.columns:
        table_df["observation_source_concept_id"] = table_df["observation_source_concept_id"].fillna("0")
    if "observation_type_concept_id" in table_df.columns:
        table_df["observation_type_concept_id"]=table_df["observation_type_concept_id"].fillna("32817")

    table_df = handle_duplicate_ids(table_df)

    return table_df
