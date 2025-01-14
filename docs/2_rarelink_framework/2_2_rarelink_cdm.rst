.. _2_2:

RareLink-CDM
=============================

.. warning:: 
   RareLink v2.0.0.dev0 is under development (the REDCap sheets may be subject
   to change). Please :ref:`12` us before using it to ensure you have the latest 
   updates and guidance.


In this section, we provide an overview of the instruments that are part of the
RareLink Common Data Model (CDM), which is based on the :ref:`1_5`. 
We have implemented the :ref:`1_5`'s definitions, codes, and mappins 
into the REDCap instruments by encoding the variables and value sets in the
REDCap data dictionary. Each section of the model corresponds to a distinct
instrument, ensuring consistency and comprehensive data capture.

.. hint:: 
    - Read the :ref:`1_6` page to understand how REDCap instruments data dictionaries work.
    - Read the :ref:`1_5` page for more information on the Rare Disease Common Data Model.


RareLink-CDM Data Dictionary
----------------------------

- :download:`RareLink-CDM Data Dictionary (v2.0.0.dev0) <../../res/rarelink_cdm_datadictionary - v2_0_0_dev0.csv>`


RuleSet for Codes and Codesystems
__________________________________

REDCap variables and choice codes have specific limitations and requirements:

- REDCap recommends a maximum of 26 characters for variable names. We have shortened the variable names to adhere to this limitation.
- REDCap variables must be unique and must not contain spaces or special characters, i.e. only alphanumeric characters and underscores.
- REDCap choice codes must be unique and must not contain spaces or special characters, i.e. only alphanumeric characters and underscores.

To address these, we have defined a set of rules for the REDCap variables and
choice codes in the RareLink CDM Data Dictionary. The rules are as follows:

1) The REDCap variable names are based on the :ref:`1_5` codes and display names.
2) The REDCap choices are based on the :ref:`1_5` codes and display names.
3) The REDCap variable names are shortened to adhere to the 26-character limit.
4) The REDCap variable names are unique and do not contain spaces or special characters.
5) The REDCap choice codes are unique and do not contain spaces or special characters.
6) All codes begin with the official codesystem prefix (e.g. HP, SNOMED, etc.) as a lower case string followed by an underscore and the code.
7) All codes are defined in the Field Annotations of each data element.

Return to `Top <#top>`_.

Download
________

The RareLink CDM Data Dictionary is available for download as a CSV file:

:download:`Download RareLink CDM Data Dictionary v2.0.0.dev0 <../..//res/rarelink_v2_0_0_dev0_datadictionary.csv>`

.. tip::
    Read :ref:`3_1` for more information on how to import the RareLink CDM Data Dictionary into your local REDCap project.

Return to `Top <#top>`_.

Field Annotations
_________________

Witin the Field Annotation field of each REDCap element, we have defined each 
element's metadata according to the :ref:`1_5` standard, including the following:

- **Variable**: Corresponding to the data element code, codesystem, and display name.
- **Choices**: If applicable, the corresponding choices codesystem, and display name.
- **Version(s)**: If applicable, the corresponding codesystem versions used in the REDCap data element
- **Mapping**: If applicable, the corresponding mapping to the :ref:`1_4` or :ref:`1_3` standard.

Example Field Annotation of 6.2.6 Temporal Pattern:

.. code-block:: text

    Variable: 
    HP:0011008 | Temporal Pattern  
    Choices: 
    - HP:0011009 | Acute  
    - HP:0011010 | Chronic  
    - HP:0031914 | Fluctuating  
    - HP:0025297 | Prolonged  
    - HP:0031796 | Recurrent  
    - HP:0031915 | Stable  
    - HP:0011011 | Subactue  
    - HP:0025153 | Transient  
    Version(s): 
    - HPO Version 2024-08-13  
    Mapping: 
    - HL7 FHIR Expression v4.0.1: Observation.interpretation  
    - GA4GH Phenopacket Schema v2.0 Element: PhenotypicFeature.modifiers

Return to `Top <#top>`_.

.. _cdm-instruments-overview:

RareLink-CDM Instruments
------------------------

The RareLink-CDM instruments translate the `ontology-based Rare Disease Common Data Model (RD-CDM) <https://rarelink.readthedocs.io/en/latest/1_background/1_5_rd_cdm.html>`_
into REDCap instruments, ensuring usability for registry implementation while 
aligning with the `HL7 FHIR International Patient Summary (IPS) <https://build.fhir.org/ig/HL7/fhir-ips/>`_
and the `GA4GH Phenopacket Schema <https://rarelink.readthedocs.io/en/latest/1_background/1_3_ga4gh_phenopacket_schema.html>`_.
Each instrument corresponds to a specific section of the RD-CDM and has been 
adapted for REDCap's technical requirements.

- `1. Formal Criteria <#formal-criteria>`_
- `2. Personal Information <#personal-information>`_
- `3. Patient Status <#patient-status>`_
- `4. Care Pathway <#care-pathway>`_
- `5. Disease <#disease>`_
- `6.1 Genetic Findings <#genetic-findings>`_
- `6.2 Phenotypic Features <#phenotypic-features>`_
- `6.3 Measurements <#measurements>`_
- `6.4 Family History <#family-history>`_
- `7. Consent <#consent>`_
- `8. Disability <#disability>`_

Return to `Top <#top>`_.

.. note:: 
    to be implemented.

.. _formal-criteria:

(1) Formal Criteria
-------------------

**Purpose**: Captures eligibility and registration information for individuals.

**Core Variables**:
- [Insert Core Variables Here]

**Adjustments for REDCap**:
- [Insert Adjustments for REDCap Here]

**Adjustments from the RD-CDM**:
- [Insert Adjustments from the RD-CDM Here]

Return to `RareLink-CDM Instruments Overview <#cdm-instruments-overview>`_.

.. _personal-information:

(2) Personal Information
------------------------

**Purpose**: Records demographic and personal data.

**Core Variables**:
- [Insert Core Variables Here]

**Adjustments for REDCap**:
- [Insert Adjustments for REDCap Here]

**Adjustments from the RD-CDM**:
- [Insert Adjustments from the RD-CDM Here]

Return to `RareLink-CDM Instruments Overview <#cdm-instruments-overview>`_.

.. _patient-status:

(3) Patient Status
------------------

**Purpose**: Tracks changes in patient conditions over time.

**Core Variables**:
- [Insert Core Variables Here]

**Adjustments for REDCap**:
- [Insert Adjustments for REDCap Here]

**Adjustments from the RD-CDM**:
- [Insert Adjustments from the RD-CDM Here]

Return to `RareLink-CDM Instruments Overview <#cdm-instruments-overview>`_.

.. _care-pathway:

(4) Care Pathway
----------------

**Purpose**: Logs encounter-specific data.

**Core Variables**:
- [Insert Core Variables Here]

**Adjustments for REDCap**:
- [Insert Adjustments for REDCap Here]

**Adjustments from the RD-CDM**:
- [Insert Adjustments from the RD-CDM Here]

Return to `RareLink-CDM Instruments Overview <#cdm-instruments-overview>`_.

.. _disease:

(5) Disease
-----------

**Purpose**: Details disease history and ontology mappings.

**Core Variables**:
- [Insert Core Variables Here]

**Adjustments for REDCap**:
- [Insert Adjustments for REDCap Here]

**Adjustments from the RD-CDM**:
- [Insert Adjustments from the RD-CDM Here]

Return to `RareLink-CDM Instruments Overview <#cdm-instruments-overview>`_.

.. _genetic-findings:

(6.1) Genetic Findings
-----------------------

**Purpose**: Captures genetic variant information.

**Core Variables**:
- [Insert Core Variables Here]

**Adjustments for REDCap**:
- [Insert Adjustments for REDCap Here]

**Adjustments from the RD-CDM**:
- [Insert Adjustments from the RD-CDM Here]

Return to `RareLink-CDM Instruments Overview <#cdm-instruments-overview>`_.

.. _phenotypic-features:

(6.2) Phenotypic Features
-------------------------

**Purpose**: Encodes phenotypes and their modifiers.

**Core Variables**:
- [Insert Core Variables Here]

**Adjustments for REDCap**:
- **Simplified Field Names**: Shortened and formatted for REDCap constraints:
  - `snomed_439272007_704321009_363778006` -> `snomed_8116006_date`
  - `ga4gh_phenotypicfeature_excluded` -> `ga4gh_pheno_excluded`
- **Modifiers Grouping**: Introduced consistent naming for modifiers:
  - HPO Modifiers:
    - `ga4gh_phenotypicfeature_modifier_hp_1` -> `ga4gh_pheno_mod_hp1`
    - `ga4gh_phenotypicfeature_modifier_hp_2` -> `ga4gh_pheno_mod_hp2`
    - `ga4gh_phenotypicfeature_modifier_hp_3` -> `ga4gh_pheno_mod_hp3`
  - NCBITaxon Modifiers:
    - `ga4gh_phenotypicfeature_modifier_ncbitaxon_1` -> `ga4gh_pheno_mod_ncbitax1`
    - `ga4gh_phenotypicfeature_modifier_ncbitaxon_2` -> `ga4gh_pheno_mod_ncbitax2`
    - `ga4gh_phenotypicfeature_modifier_ncbitaxon_3` -> `ga4gh_pheno_mod_ncbitax3`
  - SNOMED Modifiers:
    - `ga4gh_phenotypicfeature_modifier_snomed_1` -> `ga4gh_pheno_mod_snomed1`
    - `ga4gh_phenotypicfeature_modifier_snomed_2` -> `ga4gh_pheno_mod_snomed2`
    - `ga4gh_phenotypicfeature_modifier_snomed_3` -> `ga4gh_pheno_mod_snomed3`

**Adjustments from the RD-CDM**:
- [Insert Adjustments from the RD-CDM Here]

Return to `RareLink-CDM Instruments Overview <#cdm-instruments-overview>`_.

.. _measurements:

(6.3) Measurements
------------------

**Purpose**: Records clinical and laboratory data.

**Core Variables**:
- [Insert Core Variables Here]

**Adjustments for REDCap**:
- [Insert Adjustments for REDCap Here]

**Adjustments from the RD-CDM**:
- [Insert Adjustments from the RD-CDM Here]

Return to `RareLink-CDM Instruments Overview <#cdm-instruments-overview>`_.

.. _family-history:

(6.4) Family History
--------------------

**Purpose**: Details familial relationships and genetic predispositions.

**Core Variables**:
- [Insert Core Variables Here]

**Adjustments for REDCap**:
- [Insert Adjustments for REDCap Here]

**Adjustments from the RD-CDM**:
- [Insert Adjustments from the RD-CDM Here]

Return to `RareLink-CDM Instruments Overview <#cdm-instruments-overview>`_.

.. _consent:

(7) Consent
-----------

**Purpose**: Documents patient consent details.

**Core Variables**:
- [Insert Core Variables Here]

**Adjustments for REDCap**:
- [Insert Adjustments for REDCap Here]

**Adjustments from the RD-CDM**:
- [Insert Adjustments from the RD-CDM Here]

Return to `RareLink-CDM Instruments Overview <#cdm-instruments-overview>`_.

.. _disability:

(8) Disability
--------------

**Purpose**: Captures ICF-encoded functional and disability data.

**Core Variables**:
- [Insert Core Variables Here]

**Adjustments for REDCap**:
- [Insert Adjustments for REDCap Here]

**Adjustments from the RD-CDM**:
- [Insert Adjustments from the RD-CDM Here]

Return to `RareLink-CDM Instruments Overview <#cdm-instruments-overview>`_.