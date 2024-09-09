from utils.config_utils import LOGGING_CONFIG, FUSEKI_URL, ONTOLOGIES_PATH, FUSEKI_DB_NAME, PREPROCESSED_TABLES, POSTPROCESSED_TABLE
from utils.Graph_utils import add_rdf_to_owl
from utils.Fuseki_utils import load_owl_fuseki

from src.OMOP_5_3.preprocessing.send_query import get_query_OMOP_5_3
from src.OMOP_5_3.postprocessing.post_omop import post_OMOP_5_3
from src.OMOP_5_4.preprocessing.send_query import get_query_OMOP_5_4
from src.OMOP_5_4.postprocessing.post_omop import post_OMOP_5_4
from src.OMOP_6_0.preprocessing.send_query import get_query_OMOP_6_0
from src.OMOP_6_0.postprocessing.post_omop import post_OMOP_6_0
from src.i2b2.preprocessing.send_query import get_query_i2b2
from src.i2b2.postprocessing.post_i2b2 import post_i2b2_core
from src.ISO13606.preprocessing.send_query import get_query_ISO13606
from src.ISO13606.postprocessing.post_iso13606 import post_ISO13606

LOGGING_CONFIG

def execute_chosen_model(chosen_model):

    get_query = None
    post_processing = None

    model_to_functions = {
        'OMOP_5_3': (get_query_OMOP_5_3, post_OMOP_5_3),
        'OMOP_5_4': (get_query_OMOP_5_4, post_OMOP_5_4),
        'OMOP_6_0': (get_query_OMOP_6_0, post_OMOP_6_0),
        'i2b2': (get_query_i2b2, post_i2b2_core),
        'ISO13606': (get_query_ISO13606, post_ISO13606)
    }

    get_query, post_processing = model_to_functions[chosen_model]
    add_rdf_to_owl(chosen_model)  
    load_owl_fuseki(FUSEKI_URL, ONTOLOGIES_PATH + chosen_model, FUSEKI_DB_NAME)
    get_query(PREPROCESSED_TABLES+chosen_model+"/")
    post_processing(PREPROCESSED_TABLES+chosen_model+"/", 
                    POSTPROCESSED_TABLE+chosen_model+"/")


