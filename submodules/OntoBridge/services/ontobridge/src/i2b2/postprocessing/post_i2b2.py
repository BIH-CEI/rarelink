import pandas as pd
from src.i2b2.postprocessing.share.utils import add_missing_time
from src.i2b2.postprocessing.concept_dimension.post_concept_dimension import post_concept_dimension
from src.i2b2.postprocessing.modifier_dimension.post_modifier_dimension import post_modifier_dimension
from src.i2b2.postprocessing.observation_fact.post_observation_fact import post_observation_fact
from src.i2b2.postprocessing.patient_dimension.post_patient_dimension import post_patient_dimension
from src.i2b2.postprocessing.visit_dimension.post_visit_dimension import post_visit_dimension
from datetime import datetime

now = datetime.now()
timestamp_str = now.strftime("%Y_%m_%d_%H_%M_%S")

def post_i2b2_core(read_folder, write_folder):
    
    container_df = pd.read_csv(read_folder +"CONCEPT_DIMENSION.csv") 
    container_df = post_concept_dimension(container_df)
    container_df = add_missing_time(container_df)
    container_df.to_csv(path_or_buf = write_folder + "CONCEPT_DIMENSION_"+timestamp_str+".csv", index=False) 

    container_df = pd.read_csv(read_folder +"MODIFIER_DIMENSION.csv") 
    container_df = post_modifier_dimension(container_df)
    container_df = add_missing_time(container_df)
    container_df.to_csv(path_or_buf = write_folder + "MODIFIER_DIMENSION_"+timestamp_str+".csv", index=False) 
        
    container_df = pd.read_csv(read_folder + "OBSERVATION_FACT.csv") 
    container_df = post_observation_fact(container_df)
    container_df = add_missing_time(container_df)
    container_df.to_csv(path_or_buf = write_folder + "OBSERVATION_FACT_"+timestamp_str+".csv", index=False) 

    container_df = pd.read_csv(read_folder +"PATIENT_DIMENSION.csv") 
    container_df = post_patient_dimension(container_df)
    container_df = add_missing_time(container_df)
    container_df.to_csv(path_or_buf = write_folder + "PATIENT_DIMENSION_"+timestamp_str+".csv", index=False) 

    container_df = pd.read_csv(read_folder + "VISIT_DIMENSION.csv") 
    container_df = post_visit_dimension(container_df)
    container_df = add_missing_time(container_df)
    container_df.to_csv(path_or_buf = write_folder + "VISIT_DIMENSION_"+timestamp_str+".csv", index=False) 
