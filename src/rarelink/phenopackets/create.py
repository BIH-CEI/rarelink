from phenopackets import Phenopacket
from rarelink.phenopackets.mappings.map_individual import map_individual
from rarelink.phenopackets.mappings.map_metadata import map_metadata
from rarelink_cdm.v2_0_0_dev0.mappings.phenopackets import INDIVIDUAL_BLOCK

RESOURCE_CONFIG = {
    "names": [
        "Human Phenotype Ontology",
        "Logical Observation Identifiers Names and Codes",
        "ICD-10 Clinical Modification",
    ],
    "namespace_prefixes": ["HP", "LOINC", "ICD10CM"],
    "urls": [
        "http://purl.obolibrary.org/obo/hp.owl",
        "https://loinc.org",
        "https://www.cdc.gov/nchs/icd/icd10cm.htm",
    ],
    "versions": ["2024-04-26", "2.74", "2023"],
    "iri_prefixes": [
        "http://purl.obolibrary.org/obo/HP_",
        "http://loinc.org",
        "http://hl7.org/fhir/sid/icd-10-cm",
    ],
}


def create_phenopacket(data: dict, mapping_config: dict, created_by: str) -> Phenopacket:
    individual = map_individual(data, mapping_config=INDIVIDUAL_BLOCK)
    metadata = map_metadata(created_by="adam", resources_config=RESOURCE_CONFIG)

    return Phenopacket(
        id=data["record_id"],
        subject=individual,
        meta_data=metadata
    )