.. _6:

Changelog
===========

v2.0.2 (inclunding v2.0.1)
----------------------------

The current version now published is v2.0.1.

The following changes have been made since the last version:

Dynamic versioning for code systems:
""""""""""""""""""""""""""""""""""""""
- Implemented dynamic retrieval of the latest CodeSystemsContainer definitions
  from the RD-CDM PyPi package so that Phenopacket metadata always reflects the 
  most current ontology/code system versions from the RareLink-CDM.
- The MetaData mapper now scans actual Phenopacket content to detect which
  code systems (e.g., MONDO, HPO, LOINC, HGVS, GENO) are used and inserts only
  those resources with their correct, up-to-date version identifiers.
  - This ensures generated Phenopackets remain consistent with the latest 
    controlled vocabularies without manual version updates.

Phenopacket Pipeline: 
""""""""""""""""""""""""
- included automatic conversion the zygosity LOINC codes
  from the RareLink-CDM to the GENO ontologies. This ensures compliance with 
  Phenopacket-analysis algorithms such as `GPSEA<https://www.medrxiv.org/content/10.1101/2025.03.05.25323315.abstract>`_.
- deacivated for the Phenopacket pipeline because the HGVS variant remains 
  required for the pipeline and includes the structural variant information.
- included automatic transversion syntax code from ``hgvs`` to ``hgvs.c``, 
  ``hgvs.g``, ``hgvs.p``, and ``hgvs.m`` for HGVS variants depending on the
  variant type. This ensures compliance with Phenopacket-analysis algorithms
  such as GPSEA.
- Fixed serialization of vital_status so that in the case of an empty or unknown
  (3.1) Vital Status within the RareLink-CDM, the default Phenopacket status 
  ``UNKNOWN_STATUS``is passed to the Phenopacket. 

Updated :ref:`_rarelink_redcap_validate_hgvs` command:
""""""""""""""""""""""""""""""""""""""""""""""""""""""""
- Added --hgvs-variable (-v) option to the validate-hgvs CLI command
- Users can now supply one or more custom HGVS field names; if omitted, the default HGVS_VARIABLES list is used.
- Enhanced validate_and_encode_hgvs to recursively scan nested dicts and lists for HGVS variables at any depth
- Refactored the CLI command to pass the user-provided hgvs_variables list (or fall back to defaults) into the validator
- Documentation updated to reflect the new hgvs-variable option and the improved nesting behavior

Customising the RareLink-CDM data dictionary: 
""""""""""""""""""""""""""""""""""""""""""""""""
- Added a section on how to customise the RareLink-CDM data dictionary to suit your 
  specific needs or simplify manual data capture: :ref:`data_dictionary_customise`.
- This includes guidelines on how to hide fields, change field labels and descriptions,
  and add new fields and instruments as extensions to the RareLink-CDM.
- Added the hint on the REDCap Multi-languag Management for the RareLink-CDM

Published on PyPi
"""""""""""""""""""
- The RareLink package is now available on PyPi, making it easier to install and use: 
  `https://pypi.org/project/rarelink/ <https://pypi.org/project/rarelink/>`_.

Fixed bugs:
"""""""""""""
- Fixed the Windows bug within the ``masked_input`` CLI tool function for the CLI command ``rarelink setup keys``.


v2.0.0
-------

First published and stable version of RareLink. This version includes the initial set of features and functionalities that were developed and tested.

Also, the FHIR Implementation Guide is finished, validated through the IG publisher including the test instances, and is available at: https://bih-cei.github.io/rarelink/.


v2.0.0.dev1 (Under Development)
--------------------------------

This version was unstable and was used for testing and development purposes. It is not recommended for production use.


Previous versions (up to v2.0):
--------------------------------

- The ERKER project was the previous version of RareLink and can still be found
  in the `ERKER GitHub repository <https://github.com/BIH-CEI/ERKER>`_. However, the ERKER project is no longer
  maintained and has been replaced by RareLink.