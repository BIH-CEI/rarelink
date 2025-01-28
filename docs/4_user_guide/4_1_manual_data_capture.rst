.. _4_1:

Manual Data Capture Guide
==========================

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
- **Searching Terminologies with** `BioPortal <https://bioportal.bioontology.org/>`_: 
  Many RareLink sheets feature integrated BioPortal search functionality.
  When searching, consider using synonyms or abbreviations, as these are also 
  indexed in BioPortal. If you cannot find the desired term, try searching for 
  broader or related terms. Alternatively, use the 
  `OLS Platform <https://www.ebi.ac.uk/ols4/ontologies>`_ to identify the 
  correct code and display for the concept you are looking for.
- **Updates**: This section will continue to evolve as RareLink documentation 
  expands. Please  check the :ref:`6` and :ref:`7` sections for updates and 
  additional information.

Types of Fields: 
""""""""""""""""""
- **Mandatory Fields** ``*``: Mandatory fields are marked within this guide with a red
  asterisk (``*``). Ensure that all mandatory fields are completed before saving
  the form.
- **Optional Fields**: Fields that are not mandatory can be left blank if the 
  information is unknown or not required. This flexibility allows for partial 
  data entry while maintaining focus on required fields.

Types of Instruments:
"""""""""""""""""""""""

+-----------------------+
| **Single-Entry Form** |
+-----------------------+ 

--> These forms are designed for one-time data entry and capture information that 
is not expected to change over time, but can be re-edited if necessary.

+-------------------+
| **Repeated Form** |
+-------------------+

--> These forms are designed for capturing information that may change over time, 
such as patient status, care pathway, and disease 
history. You can repeat these forms to reflect changes over time.

- If you are within the form, you can use the **"Save and Add New Instance"**
  at the end of the sheet button to create a new instance of the form directly.
- Alternatively when viewing the individual record, you can click the
  **"+" button next to the form name**. This action will create a new instance
  of the form, allowing you to capture additional data points for the same 
  individual.

.. raw:: html

   <div style="display: flex; justify-content: center; align-items: center; gap: 50px; text-align: center;">
       <img src="../_static/res/redcap_gui_screenshots/repeating_buttons_2.jpg" style="width: 200px;" alt="Image 1">
       <img src="../_static/res/redcap_gui_screenshots/repeating_buttons.jpg" style="width: 200px;" alt="Image 2">
   </div>


_________________________________________________________________________________

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
- **3.5 - Length of Gestation at Birth**: specify exact weeks and days in the
  format ``35+6``.
- Fields that are not mandatory can be left blank if the information is
  unknown or not required.

_________________________________________________________________________________

(4) Care Pathway
--------------------------

+-------------------+
| **Repeated Form** |
+-------------------+

This section provides information about the care pathway:

- It is a **repeated** form, with one encounter per form.
- If possible, use the dates of the encounter. 
- In relation to the **Disease sheet**, you can create a comprehensive overview 
  of a patient's disease history with encounters.
- If the specific month or day is not known, select the 1st day of the
  month or the 1st month of the year, respectively (e.g., ``01.June.2022``,
  ``01.01.2014``).
- **4.3 Encounter Status** ``*``: mandatory to ensure alignment with the IPS-FHIR profiles.
- **4.4 Encounter Type** ``*``: mandatory to ensure alignment with the IPS-FHIR profiles.

_________________________________________________________________________________

(5) Disease
----------------------

+-------------------+
| **Repeated Form** |
+-------------------+

.. hint::
    If you have difficlties finding the rare disease, use the `OLS Platform <https://www.ebi.ac.uk/ols4/ontologies>`_ for
    ontology-specific searches, for example the `OLS-MONDO Search <https://www.ebi.ac.uk/ols4/ontologies/mondo>`_ 

This section provides details about diseases:

- It is a **repeated** form; you can enter as many diseases as you wish with one
  disease per form
- **5.1 Disease** ``*``: one ontologies can be selected for encoding. We recommend
  using *MONDO* to encode a disease.

    - To link a disease to genetic variant(s) in Section **6.1 Genetic Findings**,
      enter the same *MONDO* or *OMIM_p* codes here. (*OMIM_g* codes refer to genes,
      while *OMIM_p* codes refer to phenotypes (see `OMIM <https://www.omim.org/>`_).)
    - The **ICD-11** is not integrated into BioPortal; use the `ICD-11 Browser
      <https://icd.who.int/browse/2024-01/mms/en>`_ for codes like `AA10`.
- If information for a specific field is not known, leave it blank.
- **5.3 Age at Onset** and **5.5 Age at Diagnosis**: select "prenatal" or "birth"
  where applicable, and always enter dates if available. 
- If the specific month or day is not known, select the 1st day of the
  month or the 1st month of the year (e.g., ``01.June.2022``, ``01.01.2014``).

_________________________________________________________________________________

(6.1) Genetic Findings
------------------------------

+-------------------+
| **Repeated Form** |
+-------------------+

.. hint::
    If you have difficlties finding concepts, use the `OLS Platform <https://www.ebi.ac.uk/ols4/ontologies>`_ for
    ontology-specific search!

This section provides details about genetic findings:

- **Note:** Fields that are not mandatory can be left blank if the information is
  unknown or not required .Fill in all other fields about the variant, 
  depending on the information available and your current use case. It is a
  **repeated** form; you can enter as many variants as needed.
- **6.1.1 Genomic Diagnosis**: To link a variant to a genetic diagnosis, 
  select the corresponding disease, if applicable, also to the **5.1 Disease**. 
  You can also link multiple variants to a single disease by repeating the form!
- **6.1.2 Progress Status of interpretaion**: required when creating GA4GH 
  Phenopackets - You cand find the exact definitions here: `GA4GH ProgressStatus <https://phenopacket-schema.readthedocs.io/en/latest/interpretation.html#rstprogressstatus> `_ 
- **6.1.3 Interpretation Status**: required when creating GA4GH Phenopackets -
  you can find the exact definitions here: `GA4GH InterpretationStatus <https://phenopacket-schema.readthedocs.io/en/latest/genomic-interpretation.html#rstinterpretationstatus> `_
- **6.1.6 - .9 Variant Expression**: Please select the appropriate HGVS 
  nomenclature for the variant. 

  > **If you are unsure, prioritize** ``c.HGVS``.

    - Provide validated HGVS values (`HGVS Nomenclature <https://hgvs-
      nomenclature.org/stable/>`_) for genomic (g.HGVS), DNA (c.HGVS), or
      protein (p.HGVS) changes.
    - If the variant is not validated or you are unsure how to validate, enter 
      all information in the **6.1.6 Genetic Mutation String** field.

- **HGVS Validation**: 

    1. Validate mutations using `ClinVar <https://www.ncbi.nlm.nih.gov/clinvar/>`_
       or `Varsome <https://varsome.com/>`_
    2. Confirm the expression with the `HGVS Validator <https://lhcforms.nlm.nih.gov/fhir/hgvs-validator/>`_.
    3. If the validation fails, enter the details in the **6.1.6 Genetic Mutation String** field.
    4. ``*``: **Are you sure the entered HGVS expression was validated using 
       the variant validator?** - this field is mandatory to ensure the
       validation status.

- **6.1.15 Therapeutic Actionability**: recommended when creating GA4GH 
  Phenopackets - you can find the exact definitions here: `GA4GH TherapeuticActionability <https://phenopacket-schema.readthedocs.io/en/latest/variant-interpretation.html#rsttherapeuticactionability> `_

.. attention::
    The quality of the variant's validated HGVS expression is crucial for the 
    correct interpretation of the genetic findings and creation of GA4GH 
    Phenopackets. If you are unsure about the validation, enter all information
    in the **6.1.6 Genetic Mutation String** field and consult a geneticist.

_________________________________________________________________________________

(6.2) Phenotypic Features
---------------------------------

+-------------------+
| **Repeated Form** |
+-------------------+

.. tip:: 
    Try to define consistent guidelines for capturing phenotypic features and 
    their modifiers within your cohort to improve subsequent analyses.

This section provides details about phenotypic features:


- **6.2.1 Phenotypic Feature** ``*``: It is a **repeated** form; enter as many
  phenotypic features as needed.
- **6.2.2 Status** ``*``: Always enter the status as either confirmed or refuted.
- **6.2.3 Determination Date**: If the specific month or day is not known for
  the determination date, select the 1st day of the month or the 1st month of 
  the year (e.g., ``01.June.2022``, ``01.01.2014``).

    - **Note:** If possible, capture the time a characteristic was observed by
      the individual, *not* the time it was recorded.
- Use the `OLS Platform <https://www.ebi.ac.uk/ols4/ontologies>`_ for
  ontology-specific searches, or visit `HPO <https://hpo.jax.org/app/>`_ for
  HPO codes.
- **6.2.8 Clinical Modifiers**: Encode modifiers for more detailed deep phenotyping, e.g.:
    - subclasses of `HP:0012823 (Clinical modifier) <https://hpo.jax.org/browse/term/HP:0012823>`_, 
    - infectious agents using NCBITAXON,
    - or the body site using SNOMED.
- **6.2.9 Evidence**: as recommended by the Phenopacket Scehma, try to provide 
  the evidence code for the phenotypic feature, *e.g. ECO:0006017 ("author 
  statement from published clinical study used in manual assertion")*.

_________________________________________________________________________________

(6.3) Measurements
----------------------------

+-------------------+
| **Repeated Form** |
+-------------------+


.. tip::
  Define a set of rules for capturing measurements within a cohort to
  improve subsequent analyses.

This section provides information about measurements:


- It is a **repeated** form; capture information for one measurement and
  repeat as many times as necessary. - Fields that are not mandatory can be left blank if the information is
  unknown or not required.
- **6.3.0 Category** ``*``: mandatory to ensure alignment with the IPS-FHIR profiles.
- **6.3.1 Assay** ``*``: encoded with LOINC codes. Use the `LOINC Search <https://loinc.org/search/>`_
  to find the correct code if you cannot find it in the embedded search.
- **6.3.2 Value** ``*``: must be a value two digit decimal number.
- **6.3.3 Value Unit** ``*``: encoded with the Units of measurement ontology (UO)
  codes. Use the `OLS-UO Search <https://www.ebi.ac.uk/ols4/ontologies/uo>`_ to 
  find the correct code if you cannot find it in the embedded search.
- **6.3.4 Interpretation**: NCIT encoded interpretation of the measurement. Try 
  remain consistent with the interpretation codes used in your cohort, 
  for example using the concepts `Above Refernce Range <https://www.ebi.ac.uk/ols4/ontologies/ncit/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FNCIT_C78800>`_
  or `Below Reference Range <https://www.ebi.ac.uk/ols4/ontologies/ncit/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FNCIT_C78801?lang=en>`_.
- **6.3.5 Time Observed**: ``*``: mandatory to ensure alignment with the IPS-FHIR profiles.

.. note:: 
  `OLS Platform <https://www.ebi.ac.uk/ols4/ontologies>`_ for
  ontology-specific searches if you cannot find the concepts you are looking for.

_________________________________________________________________________________

(6.4) Family History
----------------------------

+-------------------+
| **Repeated Form** |
+-------------------+

This section captures family history details:

- It is a **repeated** form; capture information for one family member per
  sheet. Fields that are not mandatory can be left blank if the information is
  unknown or not required.
- **6.4.0 Pseudonym** ``*``: The pseudonym assigned to the family member must be
  entered.
- **6.4.4 Family Member Relationship** ``*``: the relationship of the family 
  member to the individual captured - mandatory to ensure alignment with the 
  IPS-FHIR profiles.
- **6.4.5 Family Member Record Status** ``*``: the record's status - mandatory 
  to ensure alignment with the IPS-FHIR profiles.
- Use the `OLS Platform <https://www.ebi.ac.uk/ols4/ontologies>`_ for
  ontology-specific searches.

_________________________________________________________________________________

(7) Consent
---------------------

+-----------------------+
| **Single-Entry Form** |
+-----------------------+

This section captures consent-specific data:

- Specify consent details for registry use.
- **7.1 Consent Status**: ``*```
- **7.3 Health Policy Monitoring** ``*``: if unsure, you can enter any string 
  that indicates an unknown status for this field.
- **7.4 Agreement to be contacted for research purposes** ``*``: this field 
  is mandatory to ensure align with the European Registry Registration!
- **7.5 Consent to the reuse of data** ``*``: this field 
  is mandatory to ensure align with the European Registry Registration!
- **7.7 Link to a biobank**: Provide a link to the BioBank, if applicable.

_________________________________________________________________________________

(8) Disability
-------------------------

+-----------------------+
| **Single-Entry Form** |
+-----------------------+

This section provides details about disabilities:

- Enter the disability code from the ICF (International Classification of
  Functioning, Disability, and Health).
- Ensure the data corresponds to the date of admission or data entry.

_________________________________________________________________________________

 