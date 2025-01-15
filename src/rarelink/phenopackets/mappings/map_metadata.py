from phenopackets import MetaData, Resource
from datetime import datetime
from rarelink.utils.processing.dates.timestamp import date_to_timestamp

def map_metadata(created_by: str, resources_config: dict) -> MetaData:
    """
    Maps resources and creator info to a MetaData block.

    Args:
        created_by (str): Creator's name.
        resources_config (dict): Configuration for resources.

    Returns:
        MetaData: Metadata block for the Phenopacket.
    """
    created_time = datetime.utcnow().isoformat() + "Z"
    created_timestamp = date_to_timestamp(created_time)

    resources = [
        Resource(
            id=namespace_prefix.strip(),
            name=name.strip(),
            namespace_prefix=namespace_prefix.strip(),
            url=url.strip(),
            version=version.strip(),
            iri_prefix=iri_prefix.strip(),
        )
        for name, namespace_prefix, url, version, iri_prefix in zip(
            resources_config["names"],
            resources_config["namespace_prefixes"],
            resources_config["urls"],
            resources_config["versions"],
            resources_config["iri_prefixes"],
        )
    ]

    return MetaData(
        created_by=created_by,
        created=created_timestamp,
        resources=resources,
        phenopacket_schema_version="2.0"
    )
