# RareLink REDCap

Rare Disease Interoperability Framework in REDCap linking international
 registries, FHIR and Phenopackets.

> ⚠️ **Note:** RareLink v2.0.0.dev0 is currently under development, and many things are subject to change. Please reach out before implementing or using the software to ensure you have the latest updates and guidance.


[![Python CI](https://github.com/BIH-CEI/rarelink/actions/workflows/python_ci.yml/badge.svg)](https://github.com/BIH-CEI/rarelink/actions/workflows/python_ci.yml)
[![Documentation Status](https://readthedocs.org/projects/rarelink/badge/?version=latest)](https://rarelink.readthedocs.io/en/latest/?badge=latest)
![CLI Tests](https://img.shields.io/github/actions/workflow/status/BIH-CEI/rarelink/cli_tests.yml?label=CLI%20Tests&color=purple)
![Python Versions](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)


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

RareLink - A Rare Disease Framework in REDCap that connects international 
registries, FHIR standards, and Phenopackets. It provides comprehensive 
documentation and user guides to enable sustainable data management for your 
local rare disease REDCap project.

Built on the [RD-CDM](https://rarelink.readthedocs.io/en/latest/1_background/1_5_rd_cdm.html), 
all RareLink-CDM pipelines are preconfigured to generate FHIR resources compliant
with the [HL7 International Patient Summary](https://build.fhir.org/ig/HL7/fhir-ips/) 
or validated GA4GH Phenopackets. For disease-specific extensions, detailed guides  
are available to help you develop sheets that integrate seamlessly with the 
RareLink framework.

If you are familiar with REDCap but lack coding experience, you can still set up 
your local RareLink REDCap project and begin capturing data. However, some coding 
experience is recommended for accessing advanced functionalities.

## Features

REDCap is a widely-used clinical electronic data capture system, licensed by 
institutions worldwide. RareLink enhances REDCap by providing detailed 
guidelines for structuring and encoding data to ensure seamless integration 
with its preconfigured FHIR and Phenopacket pipelines. Built on the 
[Rare Disease Common Data Model v2.0 (RD-CDM)](https://rarelink.readthedocs.io/en/latest/1_background/1_5_rd_cdm.html)
RareLink is ready-to-use and extensible for disease-specific requirements.

![RareLink](https://github.com/user-attachments/assets/b5a09b05-68c8-43ef-b624-e11bd8bda475)

RareLink integrates the following features for rare disease data management in 
REDCap: 

1. **RareLink CLI**: Set up and manage your project via the 
   [Command Line Interface](https://rarelink.readthedocs.io/en/latest/2_rarelink_framework/2_4_rarelink_cli.html), 
   including API setup, instrument configuration, and running FHIR or Phenopacket 
   pipelines.
2. **Native REDCap Usage**: Downloadable REDCap forms for all [RD-CDM sections](https://rarelink.readthedocs.io/en/latest/1_background/1_5_rd_cdm.html), 
   complete with installation guides and manuals for manual data capture and 
   BioPortal connection.
3. **Semi-Automated Data Capture**: Use a template script to map your tabular
   data to the RareLink-CDM, which is in [LinkML](https://github.com/linkml/).
   This process includes syntactic mapping, local semantic encoding, validation,
   and data upload to REDCap for FHIR or Phenopacket export.
4. **Phenopacket Export**: Predefined configurations enable seamless export of 
   the RD-CDM data to validated Phenopackets utilising the [Phenopacket Mapper]((https://github.com/BIH-CEI/phenopacket_mapper)).
   RareLink guides ensure compatibility for developing custom REDCap instruments
   and [LinkML-based](https://github.com/linkml/) extensions.
5. **HL7 FHIR Export**: RareLink uses the open-source 
   [_toFHIR_ Engine](https://github.com/srdc/tofhir) to export data to any FHIR 
   server, supporting profiles based on the 
   [International Patient Summary v2.0.0.ballot](https://build.fhir.org/ig/HL7/fhir-ips/) 
   or FHIR Base Resources (v4.0.1).
6. **RD-CDM Extensions**: [Guidelines for modeling and encoding custom data](https://rarelink.readthedocs.io/en/latest/4_user_guide/4_5_develop_redcap_instruments.html)
   extensions ensure compatibility with the RareLink framework and its pipelines.

## Getting Started

Begin by exploring the RareLink [Background section](https://rarelink.readthedocs.io/en/latest/1_background/1_0_background_file.html) 
to understand the framework's scope and components.

To start using RareLink, ensure you have access to a local REDCap license and a 
running REDCap server. For more information, visit the official REDCap site: 
[https://projectredcap.org/partners/join/](https://projectredcap.org/partners/join/). 
If your institution already provides a REDCap instance, proceed to the RareLink 
Documentation on [Setting Up a REDCap Project](https://rarelink.readthedocs.io/en/latest/3_installation/3_2_setup_redcap_project.html#).

## Installation

RareLink can be set up using various Python project management approaches. One 
common method is to use a virtual environment. Below is an example where the 
virtual environment is named `rarelink-venv`, but you can name it as you prefer:

```bash
python3 -m venv rarelink-venv
source rarelink-venv/bin/activate
pip install --upgrade pip
```

Next, clone the RareLink repository, navigate to its root directory, and install RareLink using:
```bash
pip install rarelink
```

### Framework setup 

To ensure you have the latest version of RareLink installed and to check the current version, run:
```bash
rarelink framework update
rarelink framework status
```

### REDCap setup

To set up your local REDCap project, run:
```bash
rarelink redcap-setup start
```

For additional setup guidance, use:
```bash
rarelink redcap-setup --help
```

This will provide details about available commands, such as:

- `rarelink redcap-setup api-config --help` for configuring, viewing, or 
  reseting your local API config file.
- `rarelink redcap-setup download --help` for downloading RareLink REDCap sheets.
- `rarelink redcap-setup data-dictionary upload` to upload the RareLink-CDM sheets 
  to your REDCap project.

> **Note**: Ensure that your local REDCap administrator has granted you API 
  access to your REDCap project. Remember that the API token is sensitive 
  information, so store it securely!

### Semi-Automated Import to REDCap

To process and import your local (tabular) rare disease datasets into your 
RareLink REDCap project, refer to the user guide on 
[Semi-Automatic Data Capture](https://rarelink.readthedocs.io/en/latest/4_user_guide/4_2_import_mapper.html).

### Export REDCap Data to FHIR

To export [IPS](https://build.fhir.org/ig/HL7/fhir-ips/)-based FHIR resources to 
your local FHIR server, refer to the user guide on the 
[IPS RareLink FHIR Export](https://rarelink.readthedocs.io/en/latest/user_guide/tofhir_module.html).

### Export REDCap Data to Phenopackets

To export your REDCap RareLink data to validated Phenopackets, refer to the user 
guide on the 
[RareLink Phenopacket Export](https://rarelink.readthedocs.io/en/latest/4_user_guide/4_3_phenopacket_mapper.html).

### Extensional Data Modeling in REDCap

To develop your local REDCap database for disease-specific extensions around the 
[RD-CDM](https://rarelink.readthedocs.io/en/latest/1_background/1_5_rd_cdm.html), 
refer to the guide on how to develop and model REDCap sheets for processing by 
the RareLink framework: 
[RD-CDM RareLink Extension Guide](https://rarelink.readthedocs.io/en/latest/4_user_guide/4_5_develop_redcap_instruments.html).

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
- [toFHIR](https://github.com/srdc/tofhir)
- [toFHIR-redcap](https://github.com/srdc/tofhir-redcap)
- [Phenopacket Mapper](https://github.com/BIH-CEI/phenopacket_mapper)
- [HL7 FHIR-IPS](https://github.com/HL7/fhir-ips)
- [LinkML](https://github.com/linkml/linkml)

## License

This project is licensed under the terms of the [MIT License](https://github.com/BIH-CEI/RareLink/blob/develop/LICENSE)

## Acknowledgements

We would like to extend our thanks to everyone in the last three years for their
 support in the development of this project.

---

- Authors:
  - [Adam Graefe](https://github.com/aslgraefe)
  - [Filip Rehburg](https://github.com/frehburg)
  - Daniel Danis, PhD
  - Prof. Peter N. Robinson
  - Prof. Sylvia Thun
  - Prof. Oya Beyan
