import pandas as pd
from src.i2b2.postprocessing.share.utils import erase_quotes, erase_column_unnamed

# Definir la ruta al archivo de MODIFIER_DIMENSION
MODIFIER_DIMENSION_PATH = '/app/data/output/Pre-processing/i2b2/MODIFIER_DIMENSION.csv'

def process_instance_num(table_df):
    if "instance_num" in table_df.columns:
        table_df["instance_num"] = table_df["instance_num"].fillna("1").astype(str)
    non_empty_mask = table_df['instance_num'] != ''
    no_comparison_mask = ~table_df['instance_num'].str.contains('[<>]=?', regex=True)
    mask = non_empty_mask & no_comparison_mask
    table_df.loc[mask & table_df['tval_char'].isna(), 'tval_char'] = 'E'
    comparisons = {'>=': 'GE', '<=': 'LE', '>': 'G', '<': 'L'}
    for symbol, value in comparisons.items():
        mask = table_df['instance_num'].str.contains(symbol)
        table_df.loc[mask, 'tval_char'] = value
        table_df.loc[mask, 'instance_num'] = table_df.loc[mask, 'instance_num'].str.replace(symbol, '')
    return table_df

def filter_observation_fact_with_modifiers(table_df, modifier_df):
    # Identificar registros sin modifier_cd o donde modifier_cd es "@"
    no_modifier_df = table_df[(table_df['modifier_cd'].isna()) | (table_df['modifier_cd'] == "")]

    # Filtrar registros con modifier_cd válido
    has_modifier_df = table_df[(table_df['modifier_cd'].notna()) & (table_df['modifier_cd'] != "@") & (table_df['modifier_cd'] != "")]

    if not has_modifier_df.empty:
        # Filtrar las columnas relevantes de ambas tablas
        table_relevant_columns = ['encounter_num', 'patient_num', 'concept_cd', 'start_date', 'modifier_cd', 'tval_char']
        modifier_relevant_columns = ['modifier_cd', 'name_char']

        # Realizar un merge entre la tabla observation_fact y modifier_dimension en modifier_cd
        merged_df = pd.merge(
            has_modifier_df[table_relevant_columns],
            modifier_df[modifier_relevant_columns],
            how='left',
            on='modifier_cd',
            suffixes=('_obs', '_mod')
        )

        # Filtrar solo las filas donde tval_char coincida con name_char
        matched_df = merged_df[merged_df['tval_char'] == merged_df['name_char']]

        # Mantener solo las columnas originales de observation_fact
        filtered_df = matched_df[table_relevant_columns].copy()

        # Eliminar duplicados para evitar registros repetidos
        filtered_df.drop_duplicates(inplace=True)

        # Combinar nuevamente los datos filtrados con el resto de las columnas originales
        has_modifier_df = pd.merge(has_modifier_df, filtered_df, how='inner', on=table_relevant_columns)

    # Combinar nuevamente las partes con y sin modifier_cd
    table_df_filtered = pd.concat([has_modifier_df, no_modifier_df])

    return table_df_filtered

def post_observation_fact(table_df):
    # Cargar la tabla modifier_dimension desde el archivo CSV
    modifier_df = pd.read_csv(MODIFIER_DIMENSION_PATH)

    # Realizar limpieza y procesamiento de los datos antes de cambiar los modifier_cd vacíos
    table_df = erase_quotes(table_df)
    table_df = process_instance_num(table_df)
    table_df = erase_column_unnamed(table_df)

    # Aplicar el filtro para eliminar registros incorrectos solo para aquellos con modifier_cd válido
    table_df = filter_observation_fact_with_modifiers(table_df, modifier_df)

    # Ahora sí, reemplazamos los modifier_cd vacíos por "@"
    if "modifier_cd" in table_df.columns:
        table_df["modifier_cd"] = table_df["modifier_cd"].fillna("@")

    if "provider_id" in table_df.columns:
        table_df["provider_id"] = table_df["provider_id"].fillna("@")
    if "instance_num" in table_df.columns:
        table_df["instance_num"] = table_df["instance_num"].fillna("1").astype(str)
    if "valtype_cd" in table_df.columns:
        def set_valtype_cd_and_tval_char(row):
            if pd.notna(row["nval_num"]) and str(row["nval_num"]).strip() != '':
                return "N", row["tval_char"]
            elif pd.notna(row["tval_char"]) and str(row["tval_char"]).strip() != '':
                return "T", row["tval_char"]
            else:
                return pd.NA, pd.NA

        table_df[["valtype_cd", "tval_char"]] = table_df.apply(lambda row: set_valtype_cd_and_tval_char(row), axis=1, result_type="expand")

        table_df.loc[(table_df["valtype_cd"] == "T") & (table_df["tval_char"] == "E"), ["valtype_cd", "tval_char"]] = ""


    return table_df
