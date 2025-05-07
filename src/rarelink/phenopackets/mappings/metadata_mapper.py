from typing import Dict, Any, Optional
import logging
from datetime import datetime
import dataclasses
from datetime import timezone

from phenopackets import MetaData, Resource
from rarelink.phenopackets.mappings.base_mapper import BaseMapper
from rarelink.utils.date_handling import date_to_timestamp
from rarelink_cdm.v2_0_0.datamodel import CodeSystemsContainer

logger = logging.getLogger(__name__)

class MetadataMapper(BaseMapper[MetaData]):
    """
    Mapper for MetaData entity in the Phenopacket schema.
    This mapper is unique as it doesn't map from a data dictionary but takes
    direct parameters for created_by and code_systems.
    """
    
    def map(self, data: Dict[str, Any], **kwargs) -> MetaData:
        """
        Map metadata information to a MetaData entity.
        
        Args:
            data (Dict[str, Any]): Not used for metadata mapping
            **kwargs: Additional mapping parameters
                - created_by (str): Creator's name
                - code_systems (CodeSystemsContainer): Code systems for resources
            
        Returns:
            MetaData: Mapped MetaData entity
        """
        # Extract required parameters from kwargs
        created_by = kwargs.get('created_by', '')
        code_systems = kwargs.get('code_systems', None)
        
        if not created_by:
            logger.warning("No created_by provided, using empty string")
        
        if not code_systems:
            logger.warning("No code_systems provided, using empty resources list")
            
        # Call the single entity mapper
        return self._map_single_entity(data, [], created_by=created_by, code_systems=code_systems)
    
    def _map_single_entity(self, data: Dict[str, Any], instruments: list, **kwargs) -> MetaData:
        """
        Map metadata to a single MetaData entity.
        
        Args:
            data (Dict[str, Any]): Not used for metadata mapping
            instruments (list): Not used for metadata mapping
            **kwargs: Additional mapping parameters
                - created_by (str): Creator's name
                - code_systems (CodeSystemsContainer): Code systems for resources
            
        Returns:
            MetaData: Mapped MetaData entity
        """
        # Extract required parameters from kwargs
        created_by = kwargs.get('created_by', '')
        code_systems = kwargs.get('code_systems', None)
        
        created_time = datetime.now(timezone.utc).isoformat()
        created_timestamp = date_to_timestamp(created_time)
        
        # Create resources if code_systems provided
        resources = []
        if code_systems:
            resources = self._create_resources(code_systems)
        
        # Create and return the MetaData entity
        metadata = MetaData(
            created_by=created_by,
            created=created_timestamp,
            resources=resources,
            phenopacket_schema_version="2.0"
        )
        
        return metadata
    
    def _map_multi_entity(self, data: Dict[str, Any], instruments: list, **kwargs) -> Optional[MetaData]:
        """
        MetaData is always a single entity, so this method delegates to _map_single_entity.
        
        Args:
            data (Dict[str, Any]): Not used for metadata mapping
            instruments (list): Not used for metadata mapping
            **kwargs: Additional mapping parameters
                - created_by (str): Creator's name
                - code_systems (CodeSystemsContainer): Code systems for resources
            
        Returns:
            Optional[MetaData]: Mapped MetaData entity
        """
        # MetaData is always a single entity, not a list,
        # so we directly call _map_single_entity
        return self._map_single_entity(data, instruments, **kwargs)
    
    def _create_resources(self, code_systems: CodeSystemsContainer) -> list:
        """
        Create Resource entities from code systems.
        
        Args:
            code_systems (CodeSystemsContainer): Code systems container object
            
        Returns:
            list: List of Resource entities
        """
        resources = []
        
        for field in dataclasses.fields(CodeSystemsContainer):
            value = getattr(code_systems, field.name, None)
            # Skip if value is None or doesn't have a 'name' attribute
            if not value or not hasattr(value, "name"):
                continue

            resource = Resource(
                id=field.name.lower(),
                name=value.name,
                url=value.url,
                version=value.version,
                namespace_prefix=value.prefix,
                iri_prefix=value.iri_prefix
            )
            resources.append(resource)
            
        return resources