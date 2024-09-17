RareLink REDCap Instruments
============================

The RareLink REDCap Instruments are a collection of REDCap instruments designed 
to implement the `Rare Disease Common Data Model (RD CDM) <rd_cdm.rst>`_ within 
REDCap. These instruments mirror the exact structure of the RD CDM, which is 
based on the ERDRI-CDS standard. Each section of the model corresponds to a 
distinct instrument, ensuring consistency and comprehensive data capture.

- `1. Formal Criteria <#formal-criteria>`_
- `2. Personal Information <#personal-information>`_
- `3. Patient Status <#patient-status>`_
- `4. Care Pathway <#care-pathway>`_
- `5. Disease <#disease>`_
- `6.1 Genetic Findings <#genetic-findings>`_
- `6.2 Phenotypic Features <#phenotypic-features>`_
- `6.3 Family History <#family-history>`_
- `7. Consent <#consent>`_
- `8. Disability <#disability>`_

In the following, we will describe the structure of each instrument and the 
fields that are included in each one. Specifically, we will describe how the 
implementation of the RD CDM in REDCap is structured and how the data variables 
are organized in each instrument. The instruments are designed to be used in a 
REDCap project. To adhere to REDCap's limitations on variable names and field 
types, we have made some modifications to the original RD CDM. These 
modifications are described in the following sections.

.. note::

  REDCap recommends a maximum of 26 characters for variable names. We have 
  shortened the variable names to adhere to this limitation.



.. _formal-criteria:

(1) Formal Criteria
--------------------
Content for Formal Criteria goes here.

.. _go-back-top:

Return to `Top <#top>`_.

.. _personal-information:

(2) Personal Information
------------------------
Content for Personal Information goes here.

Return to `Top <#top>`_.

.. _patient-status:

(3) Patient Status
------------------
Content for Patient Status goes here.

Return to `Top <#top>`_.

.. _care-pathway:

(4) Care Pathway
----------------
Content for Care Pathway goes here.

hl7fhir_encounter_period_start -> hl7fhir_enc_period_start
hl7fhir_encounter_period_end -> hl7fhir_enc_period_end

Return to `Top <#top>`_.



.. _disease:

(5) Disease
-----------
Content for Disease goes here.

Return to `Top <#top>`_.

.. _genetic-findings:

(6.1) Genetic Findings
-----------------------
Content for Genetic Findings goes here.


ga4gh_interpretation_status -> ga4gh_interp_status
ga4gh_therapeutic_actionability -> ga4gh_therap_action


Return to `Top <#top>`_.


.. _phenotypic-features:

(6.2) Phenotypic Features
--------------------------
Content for Phenotypic Features goes here.

snomed_439272007_704321009_363778006 -> snomed_8116006_date
ga4gh_phenotypicfeature_excluded -> ga4gh_pheno_excluded
ga4gh_phenotypicfeature_modifier_hp_1 -> ga4gh_pheno_mod_hp1
ga4gh_phenotypicfeature_modifier_hp_2 -> ga4gh_pheno_mod_hp2
ga4gh_phenotypicfeature_modifier_hp_3 -> ga4gh_pheno_mod_hp3
ga4gh_phenotypicfeature_modifier_ncbitaxon_1 -> ga4gh_pheno_mod_ncbitax1
ga4gh_phenotypicfeature_modifier_ncbitaxon_2 -> ga4gh_pheno_mod_ncbitax2
ga4gh_phenotypicfeature_modifier_ncbitaxon_3 -> ga4gh_pheno_mod_ncbitax3
ga4gh_phenotypicfeature_modifier_snomed_1 -> ga4gh_pheno_mod_snomed1
ga4gh_phenotypicfeature_modifier_snomed_2 -> ga4gh_pheno_mod_snomed2
ga4gh_phenotypicfeature_modifier_snomed_3 -> ga4gh_pheno_mod_snomed3

.. _go-back-top:


.. _family-history:

(6.3) Family History
---------------------
Content for Family History goes here.

hl7fhir_familymemberhistory_status -> hl7fhir_fmh_status

.. _go-back-top:


.. _consent:

(7) Consent
-----------
Content for Consent goes here.
customcode_consent_contact_research -> customcode_consent_contact
customcode_conset_data_reuse -> customcode_consent_data

.. _go-back-top:


.. _disability:

(8) Disability
--------------
Content for Disability goes here.

.. _go-back-top:

