import json
from pathlib import Path
from google.protobuf.json_format import MessageToDict
from phenopackets import VitalStatus as VitalStatusEnum

def write_phenopackets(phenopackets: list, output_dir: str):
    """
    Writes Phenopackets to JSON files, emitting only the `status` field
    (including default) in the `vital_status` block.
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for phenopacket in phenopackets:
        # 1) Serialize entire phenopacket normally (no default fields)
        full = MessageToDict(
            phenopacket,
            preserving_proto_field_name=True,
            including_default_value_fields=False
        )

        # 2) Extract the raw integer enum value
        raw_status_int = phenopacket.subject.vital_status.status

        # 3) Map back to the enum name
        try:
            status_name = VitalStatusEnum.Status.Name(raw_status_int)
        except Exception:
            status_name = "UNKNOWN_STATUS"

        # 4) Overwrite the vital_status block with just {"status": name}
        full["subject"]["vital_status"] = {"status": status_name}

        # 5) Write to disk
        file_name = f"{phenopacket.id}.json"
        file_path = output_path / file_name
        with open(file_path, "w") as f:
            json.dump(full, f, indent=2)
