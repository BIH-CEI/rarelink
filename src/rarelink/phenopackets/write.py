import json
from pathlib import Path

def write_phenopackets(phenopackets: list, output_dir: str):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for phenopacket in phenopackets:
        file_name = f"{phenopacket.id}.json"
        file_path = output_path / file_name
        with open(file_path, "w") as f:
            json.dump(phenopacket.to_dict(), f, indent=2)
