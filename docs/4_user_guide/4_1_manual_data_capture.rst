.. _4_1:

Guide for Manual Data Capture
===============================

.. hint::
    This section offers detailed guidance for manually entering data into
    RareLink CDM forms:
    
    - For more information about the RareLink CDM, visit :ref:`2_2`. 

    - Instructions for installing the RareLink CDM instruments in REDCap are available at :ref:`3_1`.


General Information (please read!)
-------------------------------------

This section provides general information about the manual data capture
process:

- **Purpose**: The manual data capture guide is designed to facilitate the
  entry of patient data into the :ref:`2_2`. It provides detailed instructions
  for completing each section of the RareLink CDM forms.
- **Feedback**: If you encounter any issues or have suggestions for improving
  the manual data capture process, please find more information in the :ref:`7`
  section or `write a GitHub issue <https://github.com/BIH-CEI/rarelink/issues>`_.
  RareLink is a collaborative effort, and we welcome your feedback.
- **Data Security**: Ensure your local REDCap project is set up, and everything
  is sorted with your local REDCap administrator. When capturing real patient
  data, ensure that the REDCap project is in **Production Mode**! Read the 
  :ref:`1_6`-Background section for more information and discuss this with your
  local REDCap administrator.
- **Searching Terminologies with** `BioPortal <https://bioportal.bioontology.org/>`_: Many RareLink sheets feature 
  integrated BioPortal search functionality. When searching, consider using 
  synonyms or abbreviations, as these are also indexed in BioPortal. If you 
  cannot find the desired term, try searching for broader or related terms.
  Alternatively, use the `OLS Platform <https://www.ebi.ac.uk/ols4/ontologies>`_ 
  to identify the correct code and display for the concept you are looking for.

Types of Fields: 
""""""""""""""""""
- **Mandatory Fields**: Mandatory fields are marked within this guide with a red
  asterisk (``*``). Ensure that all mandatory fields are completed before saving the form.
- **Optional Fields**: Fields that are not mandatory can be left blank if the 
  information is unknown or not required. This flexibility allows for partial 
  data entry while maintaining focus on required fields.

Types of Instruments:
"""""""""""""""""""""""
- **Single-Entry Forms**: These forms are designed for one-time data entry and
  capture information that is not expected to change over time.
- **Repeated Forms**: These forms are designed for capturing information that
  may change over time, such as patient status, care pathway, and disease 
  history. You can repeat these forms to reflect changes over time.

  - If you are within the form, you can use the "Save and Add New Instance" button
    to create a new instance of the form directly.
  - To repeat a new instance of a form, click the **"+" button next to the form
    name**. This action will create a new instance of the form, allowing you to
    capture additional data points for the same individual.

.. image:: ../docs/_static/res/redcap_gui_screenshots/repeating_buttons_2.jpg
    :alt: Repeating Buttons
    :align: center
    
.. image:: docs/_static/res/redcap_gui_screenshots/repeating_buttons.jpg
    :alt: Repeating Buttons
    :align: top




_________________________________________________________________________________

(1) Formal Criteria
-----------------------------

+-----------------------+
| **Single-Entry Form** |
+-----------------------+

This section contains information related to the formal criteria of
individuals:

- **Record ID**: Unique identifier for the record automatically assigned by the
  local REDCap project. It is not editable, but can be used for reference within
  your REDCap project, study, or registry.
- **1.1 - Pseudonym** (``*``): Unique identifier for the individual, often used as a local
  patient-related identification code or registry ID
- **1.2 - Date of Admission** (``*``): The date of admission or data
  capture. Ensure the format is YYYY-MM-DD.

_________________________________________________________________________________

(2) Personal Information
----------------------------------

+-----------------------+
| **Single-Entry Form** |
+-----------------------+

This section captures personal details about the individual:

- **2.1 - Date of Birth** (``*``): The individual's date of birth.
  If exact dates are not allowed to be entered, enter approximate dates in the
  format ``01.MM.YYYY`` or ``01.01.YYYY``.
- **2.5 - Country of Birth**: Refer to the `ISO 3166 Country Codes <https://www.iso.org/obp/ui/#search/
  code/>`_ to search for the country code. Enter only the three- letter ISO 
  code (e.g., ``CAN``, ``TUR``).
- Fields that are not mandatory can be left blank if the information is
  unknown or not required.

_________________________________________________________________________________

(3) Patient Status
-----------------------------

+-------------------+
| **Repeated Form** |
+-------------------+

This section tracks the status of the patient over time:

- Forms can be **repeated** to reflect changes over time (e.g., vital status,
  rare disease cases).
- For ontology-specific searches, use `OLS Platform <https://www.ebi.ac.uk/
  ols4/ontologies>`_ for a smoother experience.
- If exact dates are unknown, enter approximate dates in the format
  ``01.MM.YYYY`` or ``01.01.YYYY``.
- For "Length of Gestation at Birth," specify exact weeks and days in the
  format ``35+6``.
- Fields that are not mandatory can be left blank if the information is
  unknown or not required.

_________________________________________________________________________________

(4) Care Pathway
--------------------------

This section provides information about the care pathway:

- Notes for entering data:
  - It is a repeated form, with one encounter per form.
  - If possible, use the dates. In relation to the Disease sheet, you can
    create a comprehensive overview of a patient's disease history with
    encounters.
  - If the specific month or day is not known, select the 1st day of the
    month or the 1st month of the year, respectively (e.g., ``01.June.2022``,
    ``01.01.2014``).
  - Fields that are not mandatory can be left blank if the information is
    unknown or not required.

_________________________________________________________________________________

(5) Disease
----------------------

This section provides details about diseases:

- Notes for entering data:
  - It is a repeated form; you can enter as many diseases as you wish, one
    disease per form, each encodable with multiple ontologies. We recommend
    using MONDO for disease encoding.
  - Use the `OLS Platform <https://www.ebi.ac.uk/ols4/ontologies>`_ for
    ontology-specific searches.
  - To link a disease to genetic variant(s) in Section 6.1 Genetic Findings,
    enter the same MONDO or OMIM_p codes here.
  - OMIM_g codes refer to genes, while OMIM_p codes refer to phenotypes (see
    `OMIM <https://www.omim.org/>`_).
  - If information for a specific field is not known, leave it blank.
  - The ICD-11 is not integrated into BioPortal; use the `ICD-11 Browser
    <https://icd.who.int/browse/2024-01/mms/en>`_ for codes like ``AA10``.
  - For "Age at Onset" and "Age at Diagnosis," select "prenatal" or "birth"
    where applicable, and always enter dates if available.
  - If the specific month or day is not known, select the 1st day of the
    month or the 1st month of the year (e.g., ``01.June.2022``, ``01.01.2014``).

_________________________________________________________________________________

(6.1) Genetic Findings
------------------------------

This section provides details about genetic findings:

- Notes for entering data:
  - It is a repeated form; you can enter as many variants as needed, linking
    them to a genomic disease if applicable.
  - Use the `OLS Platform <https://www.ebi.ac.uk/ols4/ontologies>`_ for
    ontology-specific searches.
  - Fields that are not mandatory can be left blank if the information is
    unknown or not required.
  - To link a variant to a genetic diagnosis, select the corresponding IEI
    disease. Multiple variants can be linked to a disease by repeating the
    form.
  - OMIM_g codes refer to genes, while OMIM_p codes refer to phenotypes (see
    `OMIM <https://www.omim.org/>`_).
  - Provide validated HGVS values (`HGVS Nomenclature <https://hgvs-
    nomenclature.org/stable/>`_) for genomic (g.HGVS), DNA (c.HGVS), or
    protein (p.HGVS) changes. Prioritize c.HGVS.
  - Validate mutations using `ClinVar <https://www.ncbi.nlm.nih.gov/clinvar/>`_
    or `Varsome <https://varsome.com/>`_, and check with the `HGVS Validator
    <https://lhcforms.nlm.nih.gov/fhir/hgvs-validator/>`_.
  - If validation fails, enter details in the "Unvalidated Variant Text"
    field for subsequent review.

_________________________________________________________________________________

(6.2) Phenotypic Features
---------------------------------

This section provides details about phenotypic features:

- Notes for entering data:
  - It is a repeated form; enter as many phenotypic features as needed.
  - If the specific month or day is not known for the determination date,
    select the 1st day of the month or the 1st month of the year (e.g.,
    ``01.June.2022``, ``01.01.2014``).
  - Capture the time a characteristic was observed.
  - Always enter the status as either confirmed or refuted.
  - Use the `OLS Platform <https://www.ebi.ac.uk/ols4/ontologies>`_ for
    ontology-specific searches.
  - Encode modifiers (e.g., HP:0012823 modifiers, infectious agents using
    NCBITAXON, or SNOMED).
  - For effective analysis, ensure consistent definitions for clinical
    modifiers within a cohort.

_________________________________________________________________________________

(6.3) Measurements
----------------------------

This section provides information about measurements:

- Notes and Tips for entering data:
  - It is a repeated form; capture information for one measurement and
    repeat as many times as necessary.
  - Fields that are not mandatory can be left blank if the information is
    unknown or not required.
  - Define a set of rules for capturing measurements within a cohort to
    improve subsequent analyses.
  - Use the `OLS Platform <https://www.ebi.ac.uk/ols4/ontologies>`_ for
    ontology-specific searches.
  - For LOINC searches, visit `LOINC Search <https://loinc.org/search/>`_
    (an account may be required).

_________________________________________________________________________________

(6.4) Family History
----------------------------

This section captures family history details:

- Notes for entering data:
  - It is a repeated form; capture information for one family member per
    sheet.
  - Use the `OLS Platform <https://www.ebi.ac.uk/ols4/ontologies>`_ for
    ontology-specific searches.
  - Fields that are not mandatory can be left blank if the information is
    unknown or not required.
  - If a pseudonym was assigned to a family member, include it to ensure
    consistency across records.

_________________________________________________________________________________

(7) Consent
---------------------

This section captures consent-specific data:

- Notes for entering data:
  - Specify consent details for registry use.
  - Provide a link to the BioBank, if applicable.

_________________________________________________________________________________

(8) Disability
-------------------------

This section provides details about disabilities:

- Notes for entering data:
  - Enter the disability code from the ICF (International Classification of
    Functioning, Disability, and Health).
  - Use the `OLS Platform <https://www.ebi.ac.uk/ols4/ontologies>`_ for
    ontology-specific searches.
  - Ensure the data corresponds to the date of admission or data entry.

_________________________________________________________________________________
---

This section will continue to evolve as RareLink documentation expands. For
additional help, consult our full documentation at `RareLink User Guide
<https://rarelink.readthedocs.io/en/latest/4_user_guide/4_0_guide_file.html>`_.
