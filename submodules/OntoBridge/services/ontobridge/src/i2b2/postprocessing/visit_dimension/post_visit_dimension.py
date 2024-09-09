import pandas as pd 
from src.i2b2.postprocessing.share.utils import *

def post_visit_dimension(table_df):
    table_df = erase_column_unnamed(table_df)
    table_df = erase_quotes(table_df)   
    return table_df
