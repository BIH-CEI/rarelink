from rarelink_cdm.v2_0_4.python_datamodel import CodeSystemsContainer
from dataclasses import dataclass

@dataclass
class CodeSystem:
    name: str
    prefix: str
    version: str
    url: str
    iri_prefix: str

# Define the CodeSystemsContainer with all code systems
RARELINK_CODE_SYSTEMS = CodeSystemsContainer(
    hpo=CodeSystem(
        name="Human Phenotype Ontology",
        prefix="HPO",
        version="2025-05-06",
        url="http://purl.obolibrary.org/obo/hp.owl",
        iri_prefix="http://purl.obolibrary.org/obo/HP_"
    ),
    loinc=CodeSystem(
        name="Logical Observation Identifiers Names and Codes",
        prefix="LOINC",
        version="LNC278",
        url="https://loinc.org",
        iri_prefix="http://loinc.org"
    ),
    icd10cm=CodeSystem(
        name="ICD-10 Clinical Modification",
        prefix="ICD10CM",
        version="2023",
        url="https://www.cdc.gov/nchs/icd/icd10cm.htm",
        iri_prefix="http://hl7.org/fhir/sid/icd-10-cm"
    ),
    icd11=CodeSystem(
        name="International Classification of Diseases, Eleventh Revision",
        prefix="ICD11",
        version="SNOMEDCT_US_2024_09_01",
        url="https://icd.who.int/en",
        iri_prefix="http://hl7.org/fhir/sid/icd-11"
    ),
    mondo=CodeSystem(
        name="Monarch Disease Ontology",
        prefix="MONDO",
        version="2025-06-03",
        url="https://purl.obolibrary.org/obo/MONDO/",
        iri_prefix="http://purl.obolibrary.org/obo/MONDO_"
    ),
    omim=CodeSystem(
        name="Online Mendelian Inheritance",
        prefix="OMIM",
        version="OMIM2024_08_09",
        url="https://omim.org/",
        iri_prefix="https://www.omim.org/entry/"
    ),
    orpha=CodeSystem(
        name="Orphanet Rare Disease Ontology",
        prefix="ORPHA",
        version="OMIM2024_08_09",
        url="https://www.orpha.net/",
        iri_prefix="https://www.orpha.net/ORDO/Orphanet_"
    ),
    ncit=CodeSystem(
        name="NCI Thesaurus OBO Edition",
        prefix="NCIT",
        version="24.01e",
        url="http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl",
        iri_prefix="http://purl.obolibrary.org/obo/NCIT_"
    ),
    uo=CodeSystem(
        name="Units of Measurement Ontology",
        prefix="UO",
        version="OMIM2024_08_09",
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
    ),
    ga4gh=CodeSystem(
        name="Global Alliance for Genomics and Health",
        prefix="GA4GH",
        version="v2.0",
        url="https://www.ga4gh.org/",
        iri_prefix="https://www.ga4gh.org/"
    ),
    SNOMEDCT=CodeSystem(
        name="Systematized Medical Nomenclature for Medicine–Clinical Terminology",
        prefix="SNOMEDCT",
        version="SNOMEDCT_US_2024_09_01",
        url="http://snomed.info/sct",
        iri_prefix="http://snomed.info/sct"
    ),
    so=CodeSystem(
        name="Sequence types and features ontology",
        prefix="SO",
        version="2.6",
        url="https://www.sequenceontology.org/",
        iri_prefix="http://purl.obolibrary.org/obo/SO_"
    ),
    geno=CodeSystem(
        name="GENO - The Genotype Ontology",
        prefix="GENO",
        version="2023-10-08",
        url="https://www.genoontology.org/",
        iri_prefix="http://purl.obolibrary.org/obo/GENO_"
    ),
    iso3166=CodeSystem(
        name="ISO 3166-1:2020(en) alpha-2 and alpha-3 country codes",
        prefix="ISO3166",
        version="2020(en)",
        url="https://www.iso.org/iso-3166-country-codes.html",
        iri_prefix="https://www.iso.org/iso-3166-country-codes.html#alpha2"
    ),
    icf=CodeSystem(
        name="International Classification of Functioning, Disability and Health",
        prefix="ICF",
        version="1.0.2",
        url="https://www.who.int/classifications/icf/en/",
        iri_prefix="http://hl7.org/fhir/sid/icf"
    )
)
