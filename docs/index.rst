Welcome to the RareLink REDCap Documentation!
=============================================

.. image:: https://readthedocs.org/projects/rarelink/badge/?version=latest
    :target: https://rarelink.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. warning:: 
    RareLink v2.0.0.dev0 is currently under development, and many things are 
    subject to change. Please reach out before implementing or using the 
    software to ensure you have the latest updates and guidance.

RareLink is a novel framework designed for managing and processing rare disease 
(RD) data within the REDCap. Rare diseases affect over 260 million individuals 
worldwide, yet data quality and scarcity pose significant challenges in research 
and clinical care. RareLink aims to standardize and streamline RD data management 
around REDCap by providing a structured project setup that ensures consistency 
across data collection instruments, variables, and data dictionaries. This setup
allows the linkage and export to data the standards HL7 FHIR and the 
GA4GH Phenopacket Schema. In the following you will find detailed information on the RareLink framework,
including its background, components, installation instructions, user guide,
and full examples. 

.. tip::
    GitHub Repository: https://github.com/BIH-CEI/RareLink

.. attention::
    The manuscript for the RareLink REDCap framework is currently being revised 
    for submission.

The documentation is structured as follows:

Sections 
---------
1) :doc:`1_background/1_0_background_file`
    Introduction, definitions, and explanation of all the background information, 
    technologies, and systems used in the RareLink framework.

2) :doc:`2_rarelink_framework/2_0_rarelink_file`
    Overview and detailed information on the RareLink framework, its components,
    and architecture.

3) :doc:`3_installation/3_0_install_file`
    Installation guides for all components of the RareLink framework.

4) :doc:`4_user_guide/4_0_guide_file`
    User guides for all components of the RareLink framework.

5) :doc:`5_examples/5_0_examples_file`
    Full examples of how to use the RareLink framework in practice.

6) :doc:`6_changelog`
7) :doc:`7_faq`
8) :doc:`8_glossary`
9) :doc:`9_acknowledgements`
10) :doc:`10_license`

1) Background
----------

- :doc:`1_background/1_1_rd_interoperability`
- :doc:`1_background/1_2_ontologies`
- :doc:`1_background/1_3_ga4gh_phenopacket_schema`
- :doc:`1_background/1_4_hl7_fhir`
- :doc:`1_background/1_5_rd_cdm`
- :doc:`1_background/1_6_redcap`


2) RareLink Framework
------------------

- :doc:`2_rarelink_framework/2_0_rarelink_file`
- :doc:`2_rarelink_framework/2_1_rarelink_overview`
- :doc:`2_rarelink_framework/2_2_rarelink_cdm_instruments`
- :doc:`2_rarelink_framework/2_3_rarelink_core_redcap_project`
- :doc:`2_rarelink_framework/2_4_rarelink_cli`

3) Installation
------------

- :doc:`3_installation/3_0_install_file`
- :doc:`3_installation/3_1_setup_rarelink_framework`
- :doc:`3_installation/3_2_setup_redcap_project`
- :doc:`3_installation/3_3_setup_rarelink_instruments`
- :doc:`3_installation/3_4_redcap_api`

4) User Guide
----------
- :doc:`4_user_guide/4_0_guide_file`
- :doc:`4_user_guide/4_1_manual_data_capture`
- :doc:`4_user_guide/4_2_import_mapper`
- :doc:`4_user_guide/4_3_phenopacket_mapper`
- :doc:`4_user_guide/4_4_tofhir_module`
- :doc:`4_user_guide/4_5_develop_redcap_instruments`
- :doc:`4_user_guide/4_6_redcap_project_interaction`

5) Full Examples
-------------
- :doc:`5_examples/5_0_examples_file`
- :doc:`5_examples/5_1_example_redcap_project`
- :doc:`5_examples/5_2_example_redcap_instruments`
- :doc:`5_examples/5_3_example_semiaut_import`
- :doc:`5_examples/5_4_example_phenopacket_mapper`
- :doc:`5_examples/5_5_example_tofhir_module`

Additional Information
----------------------
- :doc:`6_changelog`
- :doc:`7_faq`
- :doc:`8_glossary`
- :doc:`9_acknowledgements`
- :doc:`10_license`


.. toctree::
   :caption: Background 
   :maxdepth: 4
   :hidden:

   1_background/1_1_rd_interoperability
   1_background/1_2_ontologies
   1_background/1_3_ga4gh_phenopacket_schema
   1_background/1_4_hl7_fhir
   1_background/1_5_rd_cdm
   1_background/1_6_redcap

.. toctree:: 
   :caption: RareLink Framework 
   :maxdepth: 4
   :hidden:

   2_rarelink_framework/2_1_rarelink_overview
   2_rarelink_framework/2_2_rarelink_cdm_instruments
   2_rarelink_framework/2_3_rarelink_core_redcap_project
   2_rarelink_framework/2_4_rarelink_cli

.. toctree::
   :caption: Installation & Development
   :maxdepth: 4
   :hidden:

   3_installation/3_1_setup_rarelink_framework
   3_installation/3_2_setup_redcap_project
   3_installation/3_3_setup_rarelink_instruments
   3_installation/3_4_redcap_api

.. toctree::
   :caption: User Guide
   :maxdepth: 4
   :hidden:

   4_user_guide/4_1_manual_data_capture
   4_user_guide/4_2_import_mapper
   4_user_guide/4_3_phenopacket_mapper
   4_user_guide/4_4_tofhir_module
   4_user_guide/4_5_develop_redcap_instruments
   4_user_guide/4_6_redcap_project_interaction

.. toctree::
   :caption: Full Examples
   :maxdepth: 4
   :hidden:

   5_examples/5_1_example_redcap_project
   5_examples/5_2_example_redcap_instruments
   5_examples/5_3_example_semiaut_import
   5_examples/5_4_example_phenopacket_mapper
   5_examples/5_5_example_tofhir_module

.. toctree::
   :caption: Additional Information
   :maxdepth: 4
   :hidden:

   6_changelog
   7_faq
   8_glossary
   9_acknowledgements
   10_license


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

