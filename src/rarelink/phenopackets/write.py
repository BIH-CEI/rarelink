import json
from pathlib import Path
from google.protobuf.json_format import MessageToDict

def write_phenopackets(phenopackets: list, output_dir: str):
    """
    Writes Phenopackets to JSON files.

    Args:
        phenopackets (list): List of Phenopacket objects.
        output_dir (str): Directory to save Phenopacket JSON files.
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for phenopacket in phenopackets:
        file_name = f"{phenopacket.id}.json"
        file_path = output_path / file_name
        with open(file_path, "w") as f:
            json.dump(MessageToDict(phenopacket, preserving_proto_field_name=True), f, indent=2)