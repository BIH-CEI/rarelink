import argparse
from pathlib import Path
from typing import Union, List, Optional
from phenopackets.schema.v2 import Phenopacket
import phenopacket_mapper.pipeline
from phenopacket_mapper.pipeline import write
from rarelink.rarelink_cdm import RARELINK_CDM_V2_0_0
from rarelink.rarelink_cdm.rarelink_cdm import load_rarelink_data
from rarelink.rarelink_cdm import rarelink_cdm_phenopackets_mapping

# TODO: implement functions from processing and preferencing for multiple values
# TODO: create another class for the Mapping Definition 

def rarelink_cdm_phenopacket_pipeline(
        input_path: Union[str, Path],
        output_path: Optional[Union[str, Path]] = None
) -> List[Phenopacket]:
    if isinstance(input_path, str):
        input_path = Path(input_path)
    if output_path is not None and isinstance(output_path, str):
        output_path = Path(output_path)

    # 1. load data
    data_model = RARELINK_CDM_V2_0_0
    data_set = load_rarelink_data(input_path)
    print("ids of the fields in the data model: \n",
          data_model.get_field_ids())
    
    # 2. Define the Mapping
    phenopacket_mapper_obj = rarelink_cdm_phenopackets_mapping(data_set)

    # 3. Preprocessing
    # preprocess_redcap_for_phenopackets(data_set)

    # 4. Perform the Mapping
    phenopackets_list = phenopacket_mapper_obj.map(data_set)

    # 5. Validate Phenopackets
    # TODO: validate phenopackets

    # 6. [Optional] Write Phenopackets to file
    if output_path is not None:
        # Write phenopackets to file
        write(phenopackets_list, output_path)


    for pp in phenopackets_list:
        print(pp)

    # 7. Return Phenopackets
    return phenopackets_list


def main():
    arg_parser = argparse.ArgumentParser(
        prog='pipeline',
        description='A pipeline to map RareLink data in .csv format to phenopackets.'
    )

    arg_parser.add_argument('-p', '--publish', action='store_true',
                            help='Write phenopackets to out instead of test')

    arg_parser.add_argument('-v', '--validate', action='store_true',
                            help='Validate the created phenopackets')

    # positional arguments
    arg_parser.add_argument('data_path', help='The path to the data')
    arg_parser.add_argument('out_dir_name', nargs='?', default='',
                            help='The name of the output directory')

    args = arg_parser.parse_args()

    rarelink_cdm_phenopacket_pipeline(args.data_path)


if __name__ == "__main__":
    rarelink_cdm_phenopacket_pipeline(
        r"C:\Users\filip\OneDrive\Documents\dataspell\RareLink\res\rarelink_cdm_v2_0_0_test_data.csv",
        r"C:\Users\filip\OneDrive\Documents\dataspell\RareLink\res\output",
    )

