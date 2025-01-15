from phenopackets import Phenopacket
from rarelink.phenopackets.mappings.map_individual import map_individual
from rarelink.phenopackets.mappings.map_metadata import map_metadata


def create_phenopacket(data: dict, mapping_config: dict, created_by: str) -> Phenopacket:
    individual = map_individual(data, mapping_config)
    metadata = map_metadata(created_by)

    return Phenopacket(
        id=data["record_id"],
        subject=individual,
        meta_data=metadata
    )