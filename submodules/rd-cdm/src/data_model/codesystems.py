from .base_types import CodeSystem

class CodeSystems:
    """Class that holds all predefined CodeSystems as attributes."""
    
    NCBITaxon = CodeSystem(
        name="NCBI organismal classification",
        namespace_prefix="NCBITaxon",
        url="https://www.ncbi.nlm.nih.gov/taxonomy"
    )
    
    GENO = CodeSystem(
        name="GENO: The Genotype Ontology",
        namespace_prefix="GENO",
        url="http://www.genoontology.org/"
    )

    SO = CodeSystem(
        name="Sequence types and features ontology",
        namespace_prefix="SO",
        url="http://www.sequenceontology.org/"
    )

    ICD9 = CodeSystem(
        name="International Classification of Diseases, Ninth Revision",
        namespace_prefix="ICD9",
        url="https://www.cdc.gov/nchs/icd/icd9.htm",
        synonyms=["ICD-9", "ICD_9"]
    )

    ICD10GM = CodeSystem(
        name="International Classification of Diseases, Tenth Revision, German Modification",
        namespace_prefix="ICD10GM",
        url="https://www.bfarm.de/EN/Code-systems/Classifications/ICD/ICD-10-GM/_node.html",
        synonyms=["ICD10-GM", "ICD-10-GM", "ICD10_GM", "ICD_10_GM"]
    )

    ICD10CM = CodeSystem(
        name="International Classification of Diseases, Tenth Revision, Clinical Modification",
        namespace_prefix="ICD10CM",
        url="https://www.cdc.gov/nchs/icd/icd10cm.htm",
        synonyms=["ICD10-CM", "ICD10_CM", "ICD-10-CM", "ICD_10_CM"]
    )

    SNOMED = CodeSystem(
        name="SNOMED",
        namespace_prefix="SNOMED",
        url="https://www.snomed.org/snomed-ct",
        synonyms=["SCT", "SNOMED CT"]
    )

    ICD11 = CodeSystem(
        name="International Classification of Diseases, Eleventh Revision",
        namespace_prefix="ICD11",
        url="https://icd.who.int/en",
        synonyms=["ICD-11"]
    )

    HL7FHIR = CodeSystem(
        name="Health Level 7 Fast Healthcare Interoperability Resources",
        namespace_prefix="HL7FHIR",
        url="https://www.hl7.org/fhir/"
    )

    GA4GH = CodeSystem(
        name="Global Alliance for Genomics and Health Phenopacket Schema v2.0",
        namespace_prefix="GA4GH",
        url="https://www.ga4gh.org/product/phenopackets/"
    )

    ISO3166 = CodeSystem(
        name="ISO 3166-1:2020(en) alpha-2 and alpha-3 country codes",
        namespace_prefix="ISO3166",
        url="https://www.iso.org/iso-3166-country-codes.html"
    )

    ICF = CodeSystem(
        name="International Classification of Functioning, Disability and Health",
        namespace_prefix="ICF",
        url="https://www.who.int/classifications/icf/en/"
    )

    MONDO = CodeSystem(
        name="Monarch Disease Ontology",
        namespace_prefix="MONDO",
        url="http://purl.obolibrary.org/obo/mondo.owl"
    )

    ORDO = CodeSystem(
        name="Orphanet Rare Disease Ontology",
        namespace_prefix="ORDO",
        url="http://www.orpha.net/",
        synonyms=["ORPHA"]
    )

    OMIM = CodeSystem(
        name="Online Mendelian Inheritance",
        namespace_prefix="OMIM",
        url="https://omim.org/"
    )

    LOINC = CodeSystem(
        name="Logical Observation Identifiers Names and Codes",
        namespace_prefix="LOINC",
        url="https://loinc.org/"
    )

    HGVS = CodeSystem(
        name="Human Genome Variation Society",
        namespace_prefix="HGVS",
        url="http://varnomen.hgvs.org/"
    )

    HGNC = CodeSystem(
        name="HUGO Gene Nomenclature Committee",
        namespace_prefix="HGNC",
        url="https://www.genenames.org/"
    )

    HP = CodeSystem(
        name="Human Phenotype Ontology",
        namespace_prefix="HP",
        url="http://www.human-phenotype-ontology.org",
        iri_prefix="http://purl.obolibrary.org/obo/HP_",
        synonyms=["HPO"]
    )

    UO = CodeSystem(
        name="Units of Measurement Ontology",
        namespace_prefix="UO",
        url="http://www.ontobee.org/ontology/UO"
    )

    NCIT = CodeSystem(
        name="NCI Thesaurus OBO Edition",
        namespace_prefix="NCIT",
        url="https://ncit.nci.nih.gov/"
    )

    ECO = CodeSystem(
        name="Evidence & Conclusion Ontology (ECO)",
        namespace_prefix="ECO",
        url="https://www.evidenceontology.org/"
    )
    
    CustomCode = CodeSystem(
        name="Custom Code System RD CDM v2.0.0",
        namespace_prefix="CustomCode",
        url="https://github.com/BIH-CEI/rd-cdm"
    )
    @classmethod
    def get_all_code_systems(cls):
        """Returns all code systems as a dictionary."""
        return {attr: value for attr, value in cls.__dict__.items() if isinstance(value, CodeSystem)}
