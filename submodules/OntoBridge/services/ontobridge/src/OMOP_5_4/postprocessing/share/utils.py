import pandas as pd

def erase_column_unnamed(table_df):
    #num_cols = str(len(table_df.columns) - 1)
    #table_df = table_df.drop(columns=['Unnamed: ' + num_cols])
    return table_df

def erase_quotes(table_df):
    #table_df.columns = table_df.columns.str.strip(' "')
    #table_df = table_df.map(lambda x: x.strip(' "'))
    return table_df

def change_hour(table_df):
    date_columns = table_df.filter(regex='_date$').columns
    for col in date_columns:
        table_df[col] = pd.to_datetime(table_df[col], errors='coerce').dt.date

    #test
    datetime_columns = table_df.filter(regex='datetime$').columns
    for col in datetime_columns:
        table_df[col] = pd.to_datetime(table_df[col], errors='coerce')



#    if "_date" in table_df.columns:
#        table_df["_date"] = table_df["_date"].str.split(' ').str[0]

    return table_df



