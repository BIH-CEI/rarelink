Generate GA4GH Phenopackets
============================

The Phenopacket Mapper module allows users to generate GA4GH Phenopackets from REDCap data.

Rarelink predefines a set of mappings between REDCap data and GA4GH Phenopacket fields. 
The Phenopacket Mapper module uses these mappings to generate GA4GH Phenopackets from REDCap data.

These mappings are defined in a configuration file that is provided with the Phenopacket Mapper module. 
All data from the RD CDM can be exported to GA4GH Phenopackets using the Phenopacket Mapper module.
For all data extending the RD CDM, we predefined a set of mappings that can be used to generate GA4GH Phenopackets.
These mappings specify how data in REDCap should be coded and formatted to generate GA4GH Phenopackets.

RD CDM --> RareLink Sheets --> predefined Phenopacket pipeline --> GA4GH Phenopackets

Extensions around RD CDM --> RareLink Sheets with Phenopacket codes --> preconfiguration in Phenopacket Mapper --> GA4GH Phenopackets
- extension based on CEIENR use case



Definition REDCap variable suffixes for Phenopacket Mapper
__________________________________________________________

The Phenopacket Mapper module uses the following suffixes to identify REDCap variables that should be included in the GA4GH Phenopacket.
These suffixes should be after the encoding of a term in the REDCap variable name. 
e.g. mondo_0005265 is a term for "Inflammatory Bowel Disease" in the MONDO ontology.

generally there are two ways to ask for data in a REDCap form: 
1. Ask for a specific term within a specific Phenopacket block:
- e.g. Disease: you have a list of diseases encoded with "mondo_", or "ordo_"

2. You have a specific term and you want to ask for all the data related to this term:
- e.g. diease xyz "monndo_" and then you want to ask for all the data related to this disease: 
"mondo_0005265_modifier", "mondo_0005265_severity", "mondo_0005265_onset", "mondo_0005265_evidence"


Disease Block
-------------


PhenotypicFeature Block
------------------------

- "_modifier" - Modifier
- "_severity" - Severity
- "_onset" - Onset
- "_evidence" - Evidence





