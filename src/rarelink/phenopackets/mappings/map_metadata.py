from phenopackets import MetaData, Resource
from datetime import datetime
import dataclasses
from rarelink.utils.processing.dates.timestamp import date_to_timestamp
from rarelink_cdm.v2_0_0_dev1.datamodel import CodeSystemsContainer, CodeSystem

def map_metadata(created_by: str, code_systems: CodeSystemsContainer) -> MetaData:
    """
    Maps resources and creator info to a MetaData block.

    Args:
        created_by (str): Creator's name.
        code_systems (CodeSystemsContainer): An instance of CodeSystemsContainer.

    Returns:
        MetaData: Metadata block for the Phenopacket.
    """
    # Fetching and preparation
    # --------------------------------------------------------------------------
    created_time = datetime.utcnow().isoformat() + "Z"
    created_timestamp = date_to_timestamp(created_time)

    # Resources
    # --------------------------------------------------------------------------
    resources = []
    for field in dataclasses.fields(CodeSystemsContainer):
        value = getattr(code_systems, field.name, None)

        if not value or not isinstance(value, CodeSystem):
            continue

        resource = Resource(
            id=field.name.lower(), 
            name=value.name,
            url=value.url,
            version=value.version,
            namespace_prefix=value.prefix,
            iri_prefix=value.iri_prefix,
        )
        resources.append(resource)

    # Create MetaData block
    # --------------------------------------------------------------------------
    return MetaData(
        created_by=created_by,
        created=created_timestamp,
        resources=resources,
        phenopacket_schema_version="2.0"
    )
