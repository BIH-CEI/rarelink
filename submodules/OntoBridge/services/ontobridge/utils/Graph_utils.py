import rdflib
import glob
import logging
from .config_utils import VOLUME_PATH, RDF_EXTENSION, RDF_FORMAT, ONTOLOGIES_PATH, ONTOLOGY_EXTENSION, ONTOLOGY_FORMAT, REGISTER_ONTOLOGY, LOGGING_CONFIG

LOGGING_CONFIG

def add_data_to_graph(files_directory, file_extension, file_format):
    graph = rdflib.Graph()
    files = glob.glob(files_directory + file_extension)
    for file in files:
        graph.parse(file, format=file_format)
    return graph

def add_rdf_to_owl(chosen_model): 
    rdf_graph = add_data_to_graph(VOLUME_PATH, 
        RDF_EXTENSION, RDF_FORMAT)   
    
    ontologies_graph = add_data_to_graph(ONTOLOGIES_PATH,
        ONTOLOGY_EXTENSION, ONTOLOGY_FORMAT)
        
    for rdf_subject, rdf_predicate, rdf_object in rdf_graph:
        ontologies_graph.add((rdf_subject, rdf_predicate, rdf_object))

    ontologies_graph.serialize(ONTOLOGIES_PATH + chosen_model+"/"+ REGISTER_ONTOLOGY, 
        format= ONTOLOGY_FORMAT)
    