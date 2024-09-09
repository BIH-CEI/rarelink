import os
from src.ISO13606.postprocessing.post_iso_extracts import load_iso_data, generate_xml_files_per_ehr_extract
 
 
def post_ISO13606(read_folder, write_folder, option='per_ehr_extract'):
 
    # Leer el dataset de la carpeta de Pre-processing
    iso_data_path = os.path.join(read_folder, "ISO13606.csv")
    container_df = load_iso_data(iso_data_path)
 
    # Generar los XMLs por EHR extract
    generate_xml_files_per_ehr_extract(container_df, write_folder)

