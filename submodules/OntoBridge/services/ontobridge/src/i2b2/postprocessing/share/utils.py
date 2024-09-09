def erase_column_unnamed(table_df):
    columnas_unnamed = [col for col in table_df.columns if col.startswith('Unnamed')]
    if columnas_unnamed:
        num_cols = str(len(table_df.columns) - 1)
        table_df = table_df.drop(columns=['Unnamed: ' + num_cols])
    else:
        return table_df

def erase_quotes(table_df):
    table_df.columns = table_df.columns.str.strip(' "')
    table_df = table_df.applymap(lambda x: x.strip(' "') if isinstance(x, str) else x)
    return table_df

def erase_columns(table_df, columns_to_erase):
    table_df = table_df.drop(columns=columns_to_erase, errors='ignore')
    return table_df

def replace_column_value(table_df, column_to_check, column_to_extract):
    mask = table_df[column_to_check] == "None:No matching concept"
    table_df.loc[mask, column_to_check] = table_df.loc[mask, column_to_extract].str.split('#').str[-1]
    return table_df

def add_missing_time(table_df):
    def add_time_if_missing(cell):
        if isinstance(cell, str) and cell != '' and ':' not in cell:
            return cell + 'T00:00:00'
        else:
            return cell
    
    date_columns = [col for col in table_df.columns if '_date' in col]
    table_df[date_columns] = table_df[date_columns].applymap(add_time_if_missing)
    return table_df

