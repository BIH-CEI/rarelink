# RareDIF

Rare Disease Interoperability Framework in REDCap enabling HL7 FHIR® and the GA4GH Phenopacket Schema©

[![Python CI](https://github.com/BIH-CEI/RareDIF/actions/workflows/python_ci.yml/badge.svg)](https://github.com/BIH-CEI/RareDIF/actions/workflows/python_ci.yml)  
[Stable Documentation](https://BIH-CEI.github.io/RareDIF/stable/)  
[Latest Documentation](https://BIH-CEI.github.io/RareDIF/latest/)  

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

RareDIF (Rare Disease Interoperability Framework) is a comprehensive framework in REDCap for rare disease data 
management in clinical care or research. It enables data capture, processing, import and export to the international
interoperability standards HL7 FHIR® and the GA4GH Phenopacket Schema©.

## Features

REDCap is a clinical electronic data capture system, for which many university hospitals have licenses. RareDIF bases
on our Common Data Model for Rare Diseases based on the ERDRI-CDS, HL7 FHIR, and GA4GH Phenopackets. Our data model can
be found in our ART-DECOR project [_RD CDM_](https://art-decor.org/ad/#/erker-/project/overview) (_you may need to
deactivate your adblock for this website_). For disease-specific data capture and analyses, recommendations to extend
our RD CDM are given here (tbc). For further information regarding DCDEs (Domain Specific Data Elements)
please read: https://pubmed.ncbi.nlm.nih.gov/35594066/

![RareDIF (1)](https://github.com/user-attachments/assets/3f93ca95-dbb8-4b8b-8fdb-bb82168b6074)



This framework encompasses the following features for RD data management: 
1. User guide for implementation and installation in your local REDCap server & project
2. User manuals for manual data capture (e.g. for HGVS validation)
3. (Semi-)Automated import script from retrospective (tabular) databases into your REDCap project 
4. Automated export to validated GA4GH Phenopackets
5. Automated export to local HL7 FHIR resources or an HL7 FHIR server using the toFHIR Module
6. Automated import of HL7 FHIR resources to a local RECap project & database using the CDIS-Module

For further use of GA4GH Phenopackets© please read: https://www.nature.com/articles/s41587-022-01357-4.

## Getting Started

Instructions on how to set up and run your project locally please read the docs here(tbc). To provide a short overview:
1. Set up your local REDCap license and project
2. Install packages necessary and activate REDCAp API for you project
3. Run the installation packages defined below for the specific functionalities you want to use linked to your local 
REDCap API.
4. Run the functionalities you need to generate HL7 FHIR resources or GA4GH Phenopackets 

### Prerequisites

Software, libraries, or dependencies that need to be installed before setting up the project can be found in detail in 
our docs here. As a brief overview you need the following:

### Installation

tbc.

#### RareDIF REDCap Project

tbc. 

#### (Semi-)Automated Import Scripts

tbc.

#### HL7 FHIR Modules 

tbc.

#### Phenopackets Pipeline

tbc. For the time being, please see more details in our previous GitHub Repository [ERKER2Phenopackets](https://github.com/BIH-CEI/ERKER2Phenopackets)

## Contributing

Please write an issue or exchange with other users in the discussions if you encounter any problems.
Feel free to reach out to us, if you are interested in collaborating and improve the use of REDCap for rare disease 
research and care.

## Resources 

### Ontologies
- Human Phenotype Ontology (HP, version: 2023-06-06) [🔗](http://www.human-phenotype-ontology.org)
- Online Mendelian Inheritance in Man (OMIM, version: 2023-09-08) [🔗](https://www.omim.org/)
- Orphanet Rare Disease Ontology (OPRHA, version: 2023-09-10) [🔗](https://www.orpha.net/)
- National Center for Biotechnology Information Taxonomy (NCBITaxon, version: 2023-02-21) [🔗](https://www.ncbi.nlm.nih.gov/taxonomy)
- Logical Observation Identifiers Names and Codes (LOINC, version: 2023-08-15) [🔗](https://loinc.org/)
- HUGO Gene Nomenclature Committee (HGNC, version: 2023-09-10) [🔗](https://www.genenames.org/)
- Gene Ontology (GENO, version: 2023-07-27) [🔗](https://geneontology.org/)

## License

This project is licensed under the terms of the [MIT License](https://github.com/BIH-CEI/RareDIF/blob/main/LICENSE)

## Acknowledgements

We would like to extend our thanks to ... for his support in the development of this project.

---


- Authors:
  - [Adam Graefe](https://github.com/graefea)
  - [Filip Rehburg](https://github.com/frehburg)
  - Daniel Danis, PhD
  - Prof. Peter N. Robinson
  - Prof. Sylvia Thun
  - Prof. Oya Beyan
