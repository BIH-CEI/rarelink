from phenopacket_mapper.data_standards.code import Coding, CodeSystem


class RareLink_CDM_v2_0_0_CodeSystems:
    """
    This class is a container for the additional code systems used in the RareLink CDM.
    """
    NCBITaxon = CodeSystem(
        name='NCBI organismal classification', 
        namespace_prefix='ncbitaxon', 
        url='https://www.ncbi.nlm.nih.gov/taxonomy',
        version="2024-07-03"
    )

    GENO = CodeSystem(
        name='GENO: The Genotype Ontology', 
        namespace_prefix='geno', 
        url='http://www.genoontology.org/',
        version="2023-10-08"
    )

    SO = CodeSystem(
        name='Sequence Ontology (SO)', 
        namespace_prefix='so', 
        url='http://www.sequenceontology.org/',
        version="2.6"
    )

    ICD10CM = CodeSystem(
        name='ICD-10-CM', 
        namespace_prefix='icd10cm', 
        url='https://www.cdc.gov/nchs/icd/icd10cm.htm',
        version="2024-09-01"
    )

    SNOMED = CodeSystem(
        name='SNOMED CT', 
        namespace_prefix='snomed', 
        url='https://www.snomed.org/snomed-ct',
        version="2024-09-01"
    )

    ICD11 = CodeSystem(
        name='ICD-11', 
        namespace_prefix='icd11', 
        url='https://icd.who.int/en',
        version="2024-09-01"
    )

    HL7FHIR = CodeSystem(
        name='HL7 FHIR', 
        namespace_prefix='hl7fhir', 
        url='https://www.hl7.org/fhir/',
        version="v4.0.1"
    )

    GA4GH = CodeSystem(
        name='Global Alliance for Genomics and Health - Phenopacket Schema', 
        namespace_prefix='ga4gh', 
        url='https://www.ga4gh.org/',
        version="v2.0"
    )

    ISO3166 = CodeSystem(
        name='ISO 3166-1:2020(en) alpha-2 and alpha-3 country codes', 
        namespace_prefix='iso3166', 
        url='https://www.iso.org/iso-3166-country-codes.html',
        version="2020(en)"
    )

    ICF = CodeSystem(
        name='International Classification of Functioning, Disability and Health (ICF)', 
        namespace_prefix='icf', 
        url='https://www.who.int/classifications/icf/en/',
        version="1.0.2"
    )

rarelink_cdm_codesystems = RareLink_CDM_v2_0_0_CodeSystems()