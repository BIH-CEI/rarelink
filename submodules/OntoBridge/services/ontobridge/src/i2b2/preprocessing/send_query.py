import logging
from SPARQLWrapper import SPARQLWrapper

from src.i2b2.preprocessing.config import get_endpoint
from src.i2b2.preprocessing.concept_dimension.query import query_concept_dimension
from src.i2b2.preprocessing.modifier_dimension.query import query_modifier_dimension
from src.i2b2.preprocessing.observation_fact.query import query_observation_fact
from src.i2b2.preprocessing.patient_dimension.query import query_patient_dimension
from src.i2b2.preprocessing.provider_dimension.query import query_provider_dimension
from src.i2b2.preprocessing.visit_dimension.query import query_visit_dimension

def send_query_i2b2(query_options, namefile):
    """Send SPARQL query and save response to a CSV file."""
    logging.info(f"Sending query and writing results to {namefile}")
    sparql = SPARQLWrapper(get_endpoint())
    sparql.setQuery(query_options)
    sparql.setReturnFormat("csv")
    
    response = sparql.query().response
    if response:
        with open(namefile, "w", encoding='utf-8') as file:
            file.write(response.read().decode('utf-8'))

def get_query_i2b2(read_folder):
    """Run all SPARQL queries for the i2b2 clinical CDM model."""
    logging.info("Starting to run SPARQL queries for all data tables.")

    # # concept_dimension
    query_options = query_concept_dimension() 
    send_query_i2b2(query_options, read_folder + "CONCEPT_DIMENSION.csv")

    # modifier_dimension
    query_options = query_modifier_dimension()     
    send_query_i2b2(query_options, read_folder + "MODIFIER_DIMENSION.csv")

    # # observation_fact
    query_options = query_observation_fact()     
    send_query_i2b2(query_options, read_folder + "OBSERVATION_FACT.csv")

    # # patient_dimension
    query_options = query_patient_dimension()     
    send_query_i2b2(query_options, read_folder + "PATIENT_DIMENSION.csv")

    # provider_dimension
    query_options = query_provider_dimension()     
    send_query_i2b2(query_options, read_folder + "PROVIDER_DIMENSION.csv")

    # visit_dimension
    query_options = query_visit_dimension()     
    send_query_i2b2(query_options, read_folder + "VISIT_DIMENSION.csv")

    logging.info("All queries have been executed and data written.")

