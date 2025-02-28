.. _4_3:

Phenopackets Module
======================

The RareLink-Phenopacket module allows users to generate :ref:`1_3`
from data stored in a local REDCap project. For the :ref:`2_2` the engine is
preconfigured so that Phenopackets can be instantly exported via the :ref:`2_3`. 

The RareLink-Phenopacket module is designed to be modular and flexible so that
it can be adapted to other REDCap data structures. Please see the section below.

_____________________________________________________________________________________

**Overview**:

- :ref:`get_started`
- :ref:`rarelink-phenopacket-export`
- :ref:`rarelink-phenopacket-engine`

  - :ref:`phenopacket-validation`
  - :ref:`rarelink-phenopacket-preconfigurations`
  - :ref:`phenopackets-other-redcap-data-models`
  - :ref:`phenopacket-mappings`
  - :ref:`label-dicts`
  - :ref:`mapping-dicts`

_____________________________________________________________________________________

.. _get_started:

Get started
-------------------

To use the Phenopacket export, you need a running REDCap project with API access 
and the RareLink-CDM instruments set up. You also need the framework and all its
components running. You can run the following commands to set everything up: 

- ``rarelink framework update`` to update the framework and all components.
- ``rarelink setup redcap-project`` to set up a REDCap project with your REDCap 
  administrator. 
- ``rarelink setup keys`` to set up the REDCap API access locally.

_____________________________________________________________________________________


.. _rarelink-phenopacket-export:


RareLink-CDM to Phenopackets
-----------------------------

Once you have data captured in you REDCap project using the :ref:`2_2` REDCap 
instruments, you can export the data to Phenopackets. The data is exported to 
one Phenopacket JSON file per individual and can be used for further analysis.

- For this, simply run: 

.. code-block:: bash

    rarelink phenopackets export

And you will be guided through the exporting process. The Phenopackets will be
exported to the configured output directory (default is your Downloads folder).

.. note::
    - Make sure you **comply with your local data protection regulations and ethical   
      agreements** before exporting the data!
    - The section :ref:`family-history` is not implemented yet. This section may 
      be included in future versions of the RareLink-Phenopacket module.

.. hint:: 
    Read the :ref:`rarelink-phenopacket-preconfigurations` below to see how the
    RareLink-Phenopacket modules is configured to handle specific fields for 
    dates, data privacy, and preferences over certain fields for the Phenopacket
    export.


_____________________________________________________________________________________


.. _rarelink-phenopacket-engine:


RareLink-Phenopacket engine
---------------------------

The RareLink-Phenopacket module is developed in a modular way to allow for easy
adaptation to other REDCap data structures. All data model specific 
configurations and mappings of the :ref:`2_2` are within its `GitHub folder <https://github.com/BIH-CEI/rarelink/tree/develop/src/rarelink_cdm>`_. 
Therefore, all functions and modules we developed can be used or adapted for 
other REDCap data models extending the :ref:`2_2` once the data model is
converted to a similar :ref:`LinkML schema <rarelink_cdm_linkml>`. 

Overview 
_________

To provide an overview, the RareLink-Phenopacket module consists of the following
components:

- ``mappings`` (`GitHub Folder <https://github.com/BIH-CEI/rarelink/tree/develop/src/rarelink/phenopackets/mappings>`_):
  Contains all the mappings from the REDCap data model to the 
  respective blocks in the Phenopacket schema without containing data-model 
  specific values or codes.
- ``DataProcessor`` Class (`GitHub Folder <https://github.com/BIH-CEI/rarelink/blob/develop/src/rarelink/utils/processor/processor.py>`_):
  Contains all functions to process any REDCap data to Phenopacket-compliant 
  data, including *field fetching*, *data drocessing*, *data validation*, 
  *Label & Mapping*, *repeated element*, and *generation* methods.
- ``create`` (`GitHub Folder <https://github.com/BIH-CEI/rarelink/blob/develop/src/rarelink/phenopackets/create.py>`_):
  Contains the main function to generate Phenopackets from the processed data.
- ``write`` (`GitHub Folder <https://github.com/BIH-CEI/rarelink/blob/develop/src/rarelink/phenopackets/write.py>`_):
  Contains the function to write the generated Phenopackets to a JSON file.
- ``phenopacket pipeline`` (`GitHub Folder <https://github.com/BIH-CEI/rarelink/blob/develop/src/rarelink/phenopackets/pipeline.py>`_):
  Contains the pipeline to generate Phenopackets from the processed data.

________

.. _phenopacket-validation:

Phenopackets validation
________________________

The engine utilizes the `Phenopackets Python Library <https://phenopacket-schema.readthedocs.io/en/latest/python.html>`_
and its Python classes to generate Phenopackets. These classes include inherent 
validation mechanisms, which raise errors if a required field is missing or if a
field is not in the correct format.

If further validation is needed, you can use the
`Validation Module <https://monarch-initiative.github.io/pyphetools/api/validation/>`_ of the
`pyphetools Python Package <https://monarch-initiative.github.io/pyphetools/>`_.

_____________________________________________________________________________________

.. _rarelink-phenopacket-preconfigurations:

Preconfigurations
____________________

The engine provides several preconfigurations to streamline data processing. 
These include:

- **Date Conversion**: Automatically converting dates to an
  `ISO8601 duration <https://phenopacket-schema.readthedocs.io/en/latest/age.html#rstage>`_
  for the following elements:

  - ``PhenotypicFeature.onset``
  - ``PhenotypicFeature.resolution``
  - ``Disease.onset``

  For example, the resulting ISO8601 duration is formatted as follows:

  .. code-block:: yaml

      age:
        iso8601duration: "P25Y3M2D"

- **PhenotypicFeature.onset Preference**: The engine prefers the ISO8601Duration defined in
  section 6.2.3 *Phenotype Determination* over the Age 
_________


.. _phenopackets-other-redcap-data-models:

Usage for other REDCap data models
____________________________________

If you want to adapt the RareLink-Phenopacket module to another REDCap data model,
you can follow these steps:

1. Develop your REDCap sheets and instruments according to the :ref:`4_5` 
   section. Try to use the RareLink-CDM for as much as you can - this will
   make the mapping and export process easier.

2. (OPTIONAL): Convert your REDCap data model to a :ref:`LinkML schema <rarelink_cdm_linkml>`. 
   This can be done by following the instructions in the :ref:`2_2` section.

3. Convert your REDCap data model using the ``redcap_to_linkml`` function you 
   in the RareLink Utils. This will convert your REDCap data to a
   JSON schema that handles repeating elements more inherently. This allows
   the ``mappings`` to handle repeating elements and Phenopacket Blocks.

4. Write the specific mappings from your REDCap data model to the Phenopacket
   schema, using the templates for the mappings below (:ref:`phenopacket-mappings`).

5. Develop label dictionaries for all value sets of your data model, 
   mapping codes to human-readable labels (best to use the ontologie's 
   `preferred label`) . Use the templates for the label dictionaries below (
   :ref:`label-dicts`). This will allow the ``DataProcessor`` class to fetch 
   the labels for the codes in your data model using the ``fetch_label`` method.
   
   - For REDCap fields that are connected to BIOPORTAL directly, the label will
     be automatically fetched via the BIOPORTAL API.  

6. Develop mapping dictionaries for your data model, mapping codes to 
   standardized terms or enums. Use the templates for the mapping dictionaries 
   below (:ref:`mapping-dicts`).

7. Use the mappings in the ``mappings`` folder of the RareLink-Phenopacket
   module as a template to adapt the mappings to other Phenopacket blocks or 
   extensions in your model.

8. Adapt the ``create`` function to your needs, if necessary extending it with
   the relevant Phenopacket blocks and elements and importing your additional 
   mapping dictionaries.

9. Run the Phenopacket pipleine by running: 

.. code:: bash

    rarelink phenopackets export

_____________________________________________________________________________________

.. _phenopacket-mappings:

Mapping example to Phenopacket Blocks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section provides general examples of how to structure repeating and 
non-repeating data blocks. Customize the right-hand side values to fit specific 
user fields. The left-hand values are derived from the respective Phenopacket 
blocks `Disease <https://phenopacket-schema.readthedocs.io/en/latest/disease.html>`_
and `Individual <https://phenopacket-schema.readthedocs.io/en/latest/individual.html>`_.

.. code-block:: bash

    INDIVIDUAL_BLOCK = {
        "id_field": "<individual_id>",
        "date_of_birth_field": "<date_of_birth>",
        "time_at_last_encounter_field": "<last_encounter>",
        "sex_field": "<sex>",
        "karyotypic_sex_field": "<karyotypic_sex>",
        "gender_field": "<gender>",
    }

    DISEASE_BLOCK = {
        "redcap_repeat_instrument": "<instrument_name>",
        "term_field_1": "<disease_term_1>",
        "term_field_2": "<disease_term_2>",
        "term_field_3": "<disease_term_3>",
        "term_field_4": "<disease_term_4>",
        "term_field_5": "<disease_term_5>",
        "excluded_field": "<excluded_term>",
        "onset_date_field": "<onset_date>",
        "onset_category_field": "<onset_category>",
        "primary_site_field": "<primary_site>",
    }

**Notes**:

- Replace `<instrument_name>` and other placeholders with the specific field 
  names or codes used in your REDCap project or dataset.
- For repeating blocks, ensure the `redcap_repeat_instrument` value matches the 
  instrument name configured in REDCap.
- Customize as needed for other field mappings.


_____________________________________________________________________________________


.. _label-dicts:

Example for Label Dictionaries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The label dictionaries map codes to human-readable labels defined in your 
value sets. Replace the placeholders with specific codes and labels relevant to 
your use case. Make sure to include the function below in your .py file 
``get_mapping_by_name`` so that the ``DataProcessor`` can access the mappings 
correctly. All codes that are not defined in here, will be fetched from
the BIOPORTAL API by the ``DataProcessor``.

.. code-block:: bash

    label_dicts = {
        "CategoryName1": {
            "<code_1>": "<label_1>",
            "<code_2>": "<label_2>",
            "<code_3>": "<label_3>",
            "<code_4>": "<label_4>",
            "<code_5>": "<label_5>",
        },
        "CategoryName2": {
            "<code_1>": "<label_1>",
            "<code_2>": "<label_2>",
            "<code_3>": "<label_3>",
            "<code_4>": "<label_4>",
        },
    }

    def get_mapping_by_name(name, to_boolean=False):
        for mapping_dict in mapping_dicts:
            if mapping_dict["name"] == name:
                mapping = mapping_dict["mapping"]
                if to_boolean:
                    return {key: value.lower() == "true" for key, value in mapping.items()}
                return mapping
        raise KeyError(f"No mapping found for name: {name}")


_____________________________________________________________________________________

.. _mapping-dicts:

General Example for Mapping Dictionaries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The mapping dictionaries map codes to standardized terms or enums defined, with 
mapped values corresponding to Phenopacket-specific elements. Replace the 
placeholders with relevant codes and Phenopacket terms.

.. code-block:: bash

    mapping_dicts = [
        {
            "name": "<mapping_name_1>",
            "mapping": {
                "<code_1>": "<PHENOPACKET_TERM_1>",  # Example: "FEMALE"
                "<code_2>": "<PHENOPACKET_TERM_2>",  # Example: "MALE"
                "<code_3>": "<PHENOPACKET_TERM_3>",  # Example: "UNKNOWN_SEX"
                "<code_4>": "<PHENOPACKET_TERM_4>",  # Example: "OTHER_SEX"
                "<code_5>": "<PHENOPACKET_TERM_5>",  # Example: "NOT_RECORDED"
            },
        },
        {
            "name": "<mapping_name_2>",
            "mapping": {
                "<code_1>": "<PHENOPACKET_TERM_1>",
                "<code_2>": "<PHENOPACKET_TERM_2>",
                "<code_3>": "<PHENOPACKET_TERM_3>",
            },
        },
    ]

**Notes**:

- **Mapping Name:** Replace `<mapping_name_x>` with descriptive names for the 
  mapping (e.g., `"map_sex"`, `"map_disease"`).
- **Codes:** Replace `<code_x>` with actual codes (e.g., `snomedct_248152002`).
- **Phenopacket Terms:** Replace `<PHENOPACKET_TERM_X>` with specific 
  Phenopacket-standardized terms (e.g., `"FEMALE"`, `"UNKNOWN_SEX"`).
- Add additional mappings as necessary to include all relevant 
  Phenopacket-specific elements.




