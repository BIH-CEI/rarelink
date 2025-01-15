import typer
from pathlib import Path
from rarelink.phenopackets import (
    create_phenopacket,
    write_phenopackets
)
from rarelink.phenopackets.validate import validate_phenopackets
import logging


app = typer.Typer()

DEFAULT_OUTPUT_DIR = Path.home() / "Downloads" / "phenopackets"

logger = logging.getLogger(__name__)

def phenopacket_pipeline(input_data: list, output_dir: str, created_by: str):
    """
    Pipeline to process input data, create Phenopackets, and write them to files.

    Args:
        input_data (list): List of dictionaries containing individual records.
        output_dir (str): Directory to save Phenopacket JSON files.
        created_by (str): Name of the creator (for metadata).

    Returns:
        None
    """
    logger.info("Starting the Phenopacket pipeline...")
    
    # Create Phenopackets
    phenopackets = []
    for record in input_data:
        try:
            phenopacket = create_phenopacket(record, {}, created_by)
            phenopackets.append(phenopacket)
            logger.info(f"Successfully created Phenopacket for record ID: {record['record_id']}")
        except Exception as e:
            logger.error(f"Error creating Phenopacket for record ID: {record['record_id']} - {e}")

    # Write Phenopackets to files
    logger.info("Writing Phenopackets to files...")
    write_phenopackets(phenopackets, output_dir)

    logger.info("Phenopacket pipeline completed successfully.")
    
        # Validate Phenopackets
    logger.info("Validating Phenopackets...")
    try:
        validation_results = validate_phenopackets(Path(output_dir))
        if isinstance(validation_results, list):
            for success, details in validation_results:
                if success:
                    logger.info(f"Validation successful for file: {details}")
                else:
                    logger.error(f"Validation failed for file: {details}")
        else:
            success, details = validation_results
            if success:
                logger.info(f"Validation successful for file: {details}")
            else:
                logger.error(f"Validation failed for file: {details}")
    except ValueError as ve:
        logger.error(f"Validation error: {ve}")
    except Exception as e:
        logger.error(f"Unexpected error during validation: {e}")

    logger.info("Phenopacket pipeline completed successfully.")
    
    


# def pipeline(data_path: str, output_path: str = None):
#     """
#     End-to-end pipeline for processing JSON (REDCap) data into Phenopackets.

#     Args:
#         data_path (str): Path to the input data file.
#         output_path (str): Path to save the Phenopackets. Default is None.
#     """
#     logger.info("Starting pipeline...")

#     # Step 1: Load Data
#     with open(data_path, "r") as file:
#         data = json.load(file)
#     logger.info(f"Loaded {len(data)} records")

#     # Step 2: Define the Mapping
    
#     mapping_config = INDIVIDUAL_BLOCK

#     # Step 3: Preprocessing
#     logger.info("Step 3: Preprocessing data")
#     processed_data = process_redcap_code(data)

#     # Step 4: Run Mapping
#     logger.info("Step 4: Running mapping and writing Phenopackets")
#     phenopackets_list = []
#     for record in processed_data:
#         phenopacket = run_mapping(record, mapping_config)
#         phenopackets_list.append(phenopacket)

#     # Step 5: Write Phenopackets to File
#     logger.info("Step 5: Writing Phenopackets to file")
#     if output_path is None:
#         output_path = DEFAULT_OUTPUT_DIR / "phenopackets.json"
#     else:
#         output_path = Path(output_path)

#     output_path.parent.mkdir(parents=True, exist_ok=True)

#     with open(output_path, "w") as file:
#         json.dump([MessageToDict(pp) for pp in phenopackets_list], file, indent=2)

#     logger.info(f"Phenopackets written to {output_path}")
#     logger.info("Pipeline completed")
#     return phenopackets_list


# 1. load data
# 2. Define the Mapping
# 3. Preprocessing
# - in here is also part the mapping of the mapping_dicts.py file
# - then processing of all remaining REDCap codes
# 4. run mapping while writing to phenopackets.json
# - mapping of blocks itself
# 5. Validate Phenopackets
# 6. Write Phenopackets to file
#   #  if output_path is not None:
#         # Write phenopackets to file
#    #     write(phenopackets_list, output_path)


#     for pp in phenopackets_list:
#         print(pp)
# 7. eturn phenopackets_list




# from pathlib import Path
# from typing import Union, List, Optional
# from phenopackets.schema.v2 import Phenopacket

# #from phenopacket_mapper import write
# #from rarelink.rarelink_cdm import RARELINK_CDM_V2_0_0
# from rarelink.utils.rarelink_cdm.rarelink_cdm import load_rarelink_data

# # TODO: implement functions from processing and preferencing for multiple values
# # TODO: create another class for the Mapping Definition 

# def rarelink_cdm_phenopacket_pipeline(
#         input_path: Union[str, Path],
#         output_path: Optional[Union[str, Path]] = None
# ) -> List[Phenopacket]:
#     if isinstance(input_path, str):
#         input_path = Path(input_path)
#     if output_path is not None and isinstance(output_path, str):
#         output_path = Path(output_path)

#     # 1. load data
#     #data_model = RARELINK_CDM_V2_0_0
#     data_set = load_rarelink_data(input_path)
#    # print("ids of the fields in the data model: \n",
#         #data_model.get_field_ids())
    
#     # 2. Define the Mapping
#     phenopacket_mapper_obj = rarelink_cdm_phenopackets_mapping(data_set)

#     # 3. Preprocessing
#     # preprocess_redcap_for_phenopackets(data_set)

#     # 4. Perform the Mapping
#     phenopackets_list = phenopacket_mapper_obj.map(data_set)

#     # 5. Validate Phenopackets
#     # TODO: validate phenopackets

#     # 6. [Optional] Write Phenopackets to file
#   #  if output_path is not None:
#         # Write phenopackets to file
#    #     write(phenopackets_list, output_path)


#     for pp in phenopackets_list:
#         print(pp)

#     # 7. Return Phenopackets
#     return phenopackets_list


# def main():
#     arg_parser = argparse.ArgumentParser(
#         prog='pipeline',
#         description='A pipeline to map RareLink data in .csv format to phenopackets.'
#     )

#     arg_parser.add_argument('-p', '--publish', action='store_true',
#                             help='Write phenopackets to out instead of test')

#     arg_parser.add_argument('-v', '--validate', action='store_true',
#                             help='Validate the created phenopackets')

#     # positional arguments
#     arg_parser.add_argument('data_path', help='The path to the data')
#     arg_parser.add_argument('out_dir_name', nargs='?', default='',
#                             help='The name of the output directory')

#     args = arg_parser.parse_args()

#     rarelink_cdm_phenopacket_pipeline(args.data_path)


# if __name__ == "__main__":
#     rarelink_cdm_phenopacket_pipeline(
#         r"res/rarelink_cdm_v2_0_0_test_data.csv",
#         r"res/output/phenopackets_test_data",
#     )

