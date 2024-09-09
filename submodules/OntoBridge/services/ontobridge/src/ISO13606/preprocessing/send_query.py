import csv
from SPARQLWrapper import SPARQLWrapper
import logging

from src.ISO13606.preprocessing.config import get_endpoint
from src.ISO13606.preprocessing.query import query_iso13606

def send_query_ISO13606(query_options, namefile):
    """Send SPARQL query and save response to a CSV file."""
    logging.info(f"Sending query and writing results to {namefile}")
    sparql = SPARQLWrapper(get_endpoint())
    sparql.setQuery(query_options)
    sparql.setReturnFormat("csv")
    
    response = sparql.query().response
    if response:
        with open(namefile, "w", encoding='utf-8') as file:
            file.write(response.read().decode('utf-8').replace(',', ';'))

def get_query_ISO13606(read_folder):
    """Run all SPARQL queries for the OMOP clinical CDM model."""
    logging.info("Starting to run SPARQL queries for all data tables.")

    # ISO13606 query completa
    query_options = query_iso13606() 
    send_query_ISO13606(query_options, read_folder + "ISO13606.csv")

    logging.info("All queries have been executed and data written.")

