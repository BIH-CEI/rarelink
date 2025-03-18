from rarelink_cdm.v2_0_0_dev1.datamodel import CodeSystemsContainer
from dataclasses import dataclass

@dataclass
class CodeSystem:
    name: str
    prefix: str
    version: str
    url: str
    iri_prefix: str


CIEINR_CODE_SYSTEMS = CodeSystemsContainer(
    hpo=CodeSystem(
        name="Human Phenotype Ontology",
        prefix="HPO",
        version="2024-08-13",
        url="http://purl.obolibrary.org/obo/hp.owl",
        iri_prefix="http://purl.obolibrary.org/obo/HP_"
    ),
    loinc=CodeSystem(
        name="Logical Observation Identifiers Names and Codes",
        prefix="LOINC",
        version="2.78",
        url="https://loinc.org",
        iri_prefix="http://loinc.org"
    ),
    mondo=CodeSystem(
        name="Monarch Disease Ontology",
        prefix="MONDO",
        version="2024-09-03",
        url="https://purl.obolibrary.org/obo/MONDO/",
        iri_prefix="http://purl.obolibrary.org/obo/MONDO_"
    ),
    omim=CodeSystem(
        name="Online Mendelian Inheritance",
        prefix="OMIM",
        version="2024-09-12",
        url="https://omim.org/",
        iri_prefix="https://www.omim.org/entry/"
    ),
    ncit=CodeSystem(
        name="NCI Thesaurus OBO Edition",
        prefix="NCIT",
        version="24.04e",
        url="https://ncit.nci.nih.gov/",
        iri_prefix="http://purl.obolibrary.org/obo/NCIT_"
    ),
    uo=CodeSystem(
        name="Units of Measurement Ontology",
        prefix="UO",
        version="2024-09-12",
        url="https://www.ontobee.org/ontology/UO",
        iri_prefix="http://purl.obolibrary.org/obo/UO_"
    ),
    hgnc=CodeSystem(
        name="HUGO Gene Nomenclature Committee",
        prefix="HGNC",
        version="2024-08-23",
        url="https://www.genenames.org/",
        iri_prefix="https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/"
    ),
    hgvs=CodeSystem(
        name="Human Genome Variation Society",
        prefix="HGVS",
        version="21.0.0",
        url="https://varnomen.hgvs.org/",
        iri_prefix="https://varnomen.hgvs.org/recommendations/variant/"
    )
)