import pandas as pd
from datetime import datetime
from src.OMOP_5_3.postprocessing.drug_exposure.post_drug_exposure import post_drug_exposure
from src.OMOP_5_3.postprocessing.person.post_person import post_person 
from src.OMOP_5_3.postprocessing.death.post_death import post_death
from src.OMOP_5_3.postprocessing.observation.post_observation import post_observation 
from src.OMOP_5_3.postprocessing.measurement.post_measurement import post_measurement
from src.OMOP_5_3.postprocessing.condition_occurrence.post_condition_occurrence import post_condition_occurrence 
from src.OMOP_5_3.postprocessing.visit_occurrence.post_visit_occurrence import post_visit_occurrence
from src.OMOP_5_3.postprocessing.procedure_occurrence.post_procedure_occurrence import post_procedure_occurrence
from src.OMOP_5_3.postprocessing.visit_detail.post_visit_detail import post_visit_detail
from src.OMOP_5_3.postprocessing.device_exposure.post_device_exposure import post_device_exposure
from src.OMOP_5_3.postprocessing.observation_period.post_observation_period import post_observation_period

now = datetime.now()
timestamp_str = now.strftime("%Y_%m_%d_%H_%M_%S")

def post_OMOP_5_3(read_folder, write_folder):
    container_df = pd.read_csv(read_folder +"PERSON.csv") 
    container_df = post_person(container_df) 
    container_df.to_csv(path_or_buf = write_folder + "PERSON_"+timestamp_str+".csv", index=False) 

    container_df = post_observation(read_folder)
    container_df.to_csv(path_or_buf = write_folder + "OBSERVATION_"+timestamp_str+".csv", index=False) 

    container_df = post_measurement(read_folder)
    container_df.to_csv(path_or_buf = write_folder + "MEASUREMENT_"+timestamp_str+".csv", index=False) 

    container_df = pd.read_csv(read_folder + "CONDITION_OCCURRENCE.csv") 
    container_df = post_condition_occurrence(container_df)
    container_df.to_csv(path_or_buf = write_folder + "CONDITION_OCCURRENCE_"+timestamp_str+".csv", index=False) 

    container_df = pd.read_csv(read_folder + "VISIT_OCCURRENCE.csv") 
    container_df = post_visit_occurrence(container_df)
    container_df.to_csv(path_or_buf = write_folder + "VISIT_OCCURRENCE_"+timestamp_str+".csv", index=False) 

    container_df = pd.read_csv(read_folder + "VISIT_DETAIL.csv") 
    container_df = post_visit_detail(container_df)
    container_df.to_csv(path_or_buf = write_folder + "VISIT_DETAIL_"+timestamp_str+".csv", index=False) 

    container_df = pd.read_csv(read_folder + "PROCEDURE_OCCURRENCE.csv") 
    container_df = post_procedure_occurrence(container_df)
    container_df.to_csv(path_or_buf = write_folder + "PROCEDURE_OCCURRENCE_"+timestamp_str+".csv", index=False) 

    container_df = pd.read_csv(read_folder + "DEVICE_EXPOSURE.csv") 
    container_df = post_device_exposure(container_df) 
    container_df.to_csv(path_or_buf = write_folder + "DEVICE_EXPOSURE_"+timestamp_str+".csv", index=False) 

    container_df = pd.read_csv(read_folder + "DRUG_EXPOSURE.csv") 
    container_df = post_drug_exposure(container_df) 
    container_df.to_csv(path_or_buf = write_folder + "DRUG_EXPOSURE_"+timestamp_str+".csv", index=False) 

    container_df = pd.read_csv(read_folder + "VISIT_OCCURRENCE.csv") 
    container_df = post_observation_period(container_df) 
    container_df.to_csv(path_or_buf = write_folder + "OBSERVATION_PERIOD_"+timestamp_str+".csv", index=False) 

    container_df = pd.read_csv(read_folder + "DEATH.csv") 
    container_df = post_death(container_df) 
    container_df.to_csv(path_or_buf = write_folder + "DEATH_"+timestamp_str+".csv", index=False) 