import logging

# URL ROUTES
HOME = '/home'
ONTOP_MATERIALIZE = '/run_ontop'
EXECUTE_CHOSEN_MODEL = '/execute_chosen_model'

# HTMLs
INDEX = 'index.html'
TRANSFORMATION_SUCCES = "transformation_success.html"

# FUSEKI PARAMETERS
FUSEKI_URL = "http://10.0.0.6:3030/"
FUSEKI_DB_NAME = 'name1'

# DIRECOTIRES
ONTOBRIGE_PROPERTIES_SAVING = 'data/ontobridge.properties'
PREPROCESSED_TABLES = "data/output/Pre-processing/"
POSTPROCESSED_TABLE = "data/output/Post-processing/"
ONTOLOGIES_PATH = "./data/Ontologies/"
REGISTER_ONTOLOGY = "reg_datanex.owl"
ONTOLOGY_EXTENSION = ".owl"
EMPTY_REG = "reg_datanex_vacia.owl"

VOLUME_PATH = './data/'
ONTOLOGY_FORMAT = 'xml'
RDF_FORMAT = 'ttl'
RDF_EXTENSION = '*.ttl'
ONTOLOGY_EXTENSION = '*.owl'


# LOGGING CONFIG
LOGGING_CONFIG = logging.basicConfig(level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s', 
    handlers=[logging.StreamHandler()])

# ONTOP
ONTOP_DIRECTORY = "./ontop-cli-5.0.2"
ONTOP_SH = "/ontop_materialize.sh"
