# RareLink

Rare Disease Interoperability Framework in REDCap linking Registry Use, HL7 FHIR® and the GA4GH Phenopacket Schema©

[![Python CI](https://github.com/BIH-CEI/rarelink/actions/workflows/python_ci.yml/badge.svg)](https://github.com/BIH-CEI/rarelink/actions/workflows/python_ci.yml)
[![Documentation Status](https://readthedocs.org/projects/rd-cdm/badge/?version=latest)](https://rd-cdm.readthedocs.io/en/latest/?badge=latest)

[Stable Documentation](https://rarelink.readthedocs.io/en/stable/)  
[Latest Documentation](https://rarelink.readthedocs.io/en/latest/) 

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
- [Contributing](#contributing)
- [Resources](#resources-)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Project Description

RareLink - A Rare Disease Interoperability Framework in REDCap to enable 
Registry Use, HL7 FHIR® and the GA4GH Phenopacket Schema© including 
comprehensive documentation for data management and user guides.
This includes data capture, import, export, project set up and and is ready for 
clinical use management in clinical care or research.

## Features

REDCap is a widely-used clinical electronic data capture system, licensed by 
numerous university hospitals and institutions worldwide. RareLink provides 
detailed specifications on how REDCap sheets and data should be structured and 
encoded to ensure seamless integration with both the HL7 FHIR and GA4GH 
Phenopacket pipelines. RareLink is built upon the [Rare Disease Common Data 
Model v2.0](https://figshare.com/articles/dataset/_b_Common_Data_Model_for_Rare_Diseases_b_based_on_the_ERDRI-CDS_HL7_FHIR_and_the_GA4GH_Phenopackets_Schema_v2_0_/26509150), with all functionalities preconfigured for ease of use. 
For disease-specific extensions, such as [Domain Specific Data Elements](https://pubmed.ncbi.nlm.nih.gov/35594066/), we offer clear rules and specifications to facilitate the 
development of additional REDCap sheets, ensuring their seamless integration 
into RareLink's preconfigured data pipelines.

![RareLink](https://github.com/user-attachments/assets/b5a09b05-68c8-43ef-b624-e11bd8bda475)

RareLink integrates the following features for Rare Disease data management in 
REDCap: 
1. *Native REDCap usage*: downloadable REDCap forms of all RD CDM sections 
including documentation and manuals for installing and setting up your local 
REDCap project, manual data capture guides, connecting BioPortal.
2. *Semi-Automated Data Capture (from Tabluar Data) with [OntoBridge](https://github.com/InformaticaClinica/OntoBridge)*: Our RD CDM is defined as an SQL-based common 
data model for OntoBridge usage. This allows the syntactic mapping of 
existing tabular data bases with our RD CDM. While the semantinc mapping and 
encoding must be done locally, we provide guidelines on how to process your 
local data according to our specifications. This enables the subsequent 
validation, upload to your local REDCap project, and the usage of the HL7 FHIR 
and GA4GH Phenopacket pipelines. 
3. *GA4GH Phenopacket Mapper*: RareLink utilises the [Phenopacket Mapper](https://github.com/BIH-CEI/phenopacket_mapper) and predefines its configuration for all native RareLink 
REDCap instruments that allow the procesing of the entire RD CDM viable for 
Phenopacket export. To allow for data capture around the RD CDM, we provide
precise guidelines on how to develop REDCap instruments and sheets, specifically 
the encoding of all variables and data elements, to also enable the data export 
to validated Phenopackets.
4. *Automated Export to local HL7 FHIR Resources or HL7 FHIR server*: utilising 
the integrated [_toFHIR_ Module](https://github.com/srdc/tofhir), RareLink
provides the preconfiguration for all native RareLink REDCap instruments that
allow the procesing of the entire RD CDM viable for HL7 FHIR v4.0.1 export. 


## Getting Started

Instructions on how to set up and run your project locally please read the docs 
here(tbc). To provide a short overview:
1. Set up your local REDCap license and project, if desired using RareLink's 
project set up
2. Install packages necessary and activate REDCap API for you project
3. Run the installation packages defined for the specific functionalities
you want to use linked to your local REDCap API.
4. Run the functionalities you need to generate HL7 FHIR resources 
or GA4GH Phenopackets. 

### Prerequisites

You need a local REDCap license and REDCap server running. For more information
please see: https://projectredcap.org/partners/join/

### Installation



#### RareLink REDCap Project

RareLink provides an entire REDCap project structure that can be downloaded
here. For more information please see our documenation here.

#### Semi-Automated Import from existing tabular data bases

To process and capture existing local tabular data bases of rare disease data
using OntoBridge please see our detailed user guide [here](https://rarelink.readthedocs.io/en/latest/user_guide/ontobridge.html)

#### Generation of HL7 FHIR v4.0.1 Resources

To generate HL7 FHIR Resources, please find more information in our
documentation [here](https://rarelink.readthedocs.io/en/latest/user_guide/tofhir_module.html)

#### Phenopackets Pipeline

To utilise the RareLink configuration of the Phenopacket Pipeline for 
the native RareLink sheets, or other REDCap data, please find detailed 
information [here](https://rarelink.readthedocs.io/en/latest/user_guide/phenopacket_mapper.html).

## Contributing

Please write an issue or exchange with other users in the discussions if you
encounter any problems or wish to give feedback. Feel free to reach out to us, 
if you are interested in collaborating and improve the use of REDCap for rare 
disease research and care.

## Resources 

### Ontologies
- Human Phenotype Ontology (HP, Version 2024-08-13) [🔗](http://www.human-phenotype-ontology.org)
- Monarch Initiative Disease Ontology (MONDO, Version Version 2024-09-03) [🔗](https://mondo.monarchinitiative.org/)
- Online Mendelian Inheritance in Man (OMIM, Version 2024-09-12) [🔗](https://www.omim.org/)
- Orphanet Rare Disease Ontology (OPRHA, Version 2024-09-12) [🔗](https://www.orpha.net/)
- National Center for Biotechnology Information Taxonomy (NCBITaxon, Version 2024-07-03) [🔗](https://www.ncbi.nlm.nih.gov/taxonomy)
- Logical Observation Identifiers Names and Codes (LOINC, Version 2.78) [🔗](https://loinc.org/)
- HUGO Gene Nomenclature Committee (HGNC, Version 2024-08-23) [🔗](https://www.genenames.org/)
- Gene Ontology (GENO, Version 2023-10-08) [🔗](https://geneontology.org/)
- NCI Thesaurus OBO Edition (NCIT, Version Version 24.04e ) [🔗](https://obofoundry.org/ontology/ncit.html)

### Submodules
- [RD-CDM](https://github.com/BIH-CEI/rd-cdm)
- [toFHIR](https://github.com/srdc/tofhir?tab=readme-ov-file)
- [Phenopacket Mapper](https://github.com/BIH-CEI/phenopacket_mapper)


## License

This project is licensed under the terms of the [MIT License](https://github.com/BIH-CEI/RareLink/blob/develop/LICENSE)

## Acknowledgements

We would like to extend our thanks to ... for his support in the development of this project.

---

- Authors:
  - [Adam Graefe](https://github.com/aslgraefe)
  - [Filip Rehburg](https://github.com/frehburg)
  - Daniel Danis, PhD
  - Prof. Peter N. Robinson
  - Prof. Sylvia Thun
  - Prof. Oya Beyan
