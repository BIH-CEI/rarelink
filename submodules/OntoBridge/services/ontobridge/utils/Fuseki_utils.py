import os
import requests

def load_owl_fuseki(fuseki_url, ontologies_folder, new_dataset_name):
    dataset_url = f'{fuseki_url}{new_dataset_name}/data?default'

    owl_files = [f for f in os.listdir(ontologies_folder) if f.endswith('.owl')]

    for file in owl_files:
        owl_file_path = os.path.join(ontologies_folder, file)
        with open(owl_file_path, 'r', encoding='utf-8') as f:
            owl_data = f.read()
            dataset_url = f'{fuseki_url}{new_dataset_name}'
            response = requests.post(dataset_url, data=owl_data.encode('utf-8'),
                headers={'Content-Type': 'application/rdf+xml; charset=utf-8'})