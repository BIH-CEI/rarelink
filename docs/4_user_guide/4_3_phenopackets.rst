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
  - :ref:`troubleshooting`


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
configurations and mappings of the :ref:`2_2` are within its `GitHub folder <https://github.com/BIH-CEI/rarelink/tree/develop/src/rarelink/rarelink_cdm>`_. 
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
- ``DataProcessor`` (`Python Class <https://github.com/BIH-CEI/rarelink/blob/develop/src/rarelink/utils/processor/processor.py>`_):
  Contains all functions to process any REDCap data to Phenopacket-compliant 
  data, including *field fetching*, *data processing*, *data validation*, 
  *Label & Mapping*, *repeated element*, and *generation* methods.
- ``create`` (`Python function <https://github.com/BIH-CEI/rarelink/blob/develop/src/rarelink/phenopackets/create.py>`_):
  Contains the main function to generate Phenopackets from the processed data.
- ``write`` (`Python function <https://github.com/BIH-CEI/rarelink/blob/develop/src/rarelink/phenopackets/write.py>`_):
  Contains the function to write the generated Phenopackets to a JSON file.
- ``phenopacket pipeline`` (`Python function <https://github.com/BIH-CEI/rarelink/blob/develop/src/rarelink/phenopackets/pipeline.py>`_):
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

1. **Date conversions** 

  The engine converts dates to an
  `a Phenopacket Age element as a ISO8601 duration <https://phenopacket-schema.readthedocs.io/en/latest/age.html#rstage>`_
  with

  - **Year** and 
  - **Month** 

  ... for the following elements:

  - ``Individual.timeAtLastEncounter``
  - ``VitalStatus.timeOfDeath``
  - ``PhenotypicFeature.onset``
  - ``PhenotypicFeature.resolution``
  - ``Disease.onset``

    For example, the resulting ISO8601 duration is formatted as follows:

  .. code-block:: yaml

      age:
        iso8601duration: "P25Y3M"

  - the ``Individual.dateOfBirth`` must be a Phenopacket TimeStamp element. 
    Therefore, for data privacy only the year and month are exported from REDCap.


2. **Preferences**: 

  ``PhenotypicFeature.onset``: The engine prefers the ISO8601Duration
  defined in section 6.2.3 *Phenotype Determination* over the Age.
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

3. Convert your REDCap data model using the ``redcap_to_linkml`` function. This will convert 
   your REDCap data to a JSON schema that handles repeating elements more inherently.

4. Create mapping configurations for your data model.

Mapping Configuration for Custom Data Models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To create a custom mapping configuration, develop a Python file with a 
``create_phenopacket_mappings()`` function. You can use either a single configuration 
approach (standard dictionary) or a multi-configuration approach (list of dictionaries)
for more complex data models.

**Single Configuration Approach (Standard):**

.. code-block:: python

    def create_phenopacket_mappings():
        """
        Create a comprehensive mapping configuration for Phenopacket creation.

        Returns:
            Dict: Mapping configurations for Phenopacket generation
        """
        return {
            "individual": {
                "instrument_name": "your_instrument_name",
                "mapping_block": {
                    "id_field": "your_id_field",
                    "date_of_birth_field": "your_dob_field",
                    # ... other field mappings
                },
                "label_dicts": {
                    "GenderIdentity": {
                        "code1": "label1",
                        "code2": "label2",
                        # ... other labels
                    }
                },
                "mapping_dicts": {
                    "map_sex": {
                        "code1": "FEMALE",
                        "code2": "MALE",
                        # ... other mappings
                    }
                }
            },
            # Add other blocks: vitalStatus, diseases, phenotypicFeatures, etc.
            "metadata": {
                "code_systems": {
                    # Optional: custom code systems
                }
            }
        }

**Multi-Configuration Approach (For Complex Data Models):**

If your data model has multiple instruments for the same phenopacket block (e.g., different
instruments for different types of phenotypic features), you can use the multi-configuration approach:

.. code-block:: python

    def create_phenopacket_mappings():
        """
        Create a comprehensive mapping configuration for Phenopacket creation
        with support for multiple instruments per block.

        Returns:
            Dict: Mapping configurations for Phenopacket generation
        """
        return {
            # Standard blocks
            "individual": {
                # Standard configuration as above
            },
            
            # Multi-configuration for phenotypic features
            "phenotypicFeatures": [
                # First instrument configuration
                {
                    "instrument_name": "first_instrument",
                    "mapping_block": FIRST_FEATURES_BLOCK,
                    "data_model": "first_model",
                    "label_dicts": {
                        # Label dictionaries
                    },
                    "mapping_dicts": {
                        # Mapping dictionaries
                    },
                    # Additional configuration
                },
                # Second instrument configuration
                {
                    "instrument_name": "second_instrument",
                    "mapping_block": SECOND_FEATURES_BLOCK,
                    "data_model": "second_model",
                    # Other configuration
                }
            ],
            
            # Other blocks follow the standard configuration
        }

Command-Line Usage
~~~~~~~~~~~~~~~~~~

Export Phenopackets using the command-line interface with various options:

.. code-block:: bash

    # Basic export using default RareLink mappings
    rarelink phenopackets export

    # Specify a custom input file
    rarelink phenopackets export --input-path /path/to/custom/input.json

    # Specify a custom output directory
    rarelink phenopackets export --output-dir /path/to/custom/output

    # Use custom mapping configuration
    rarelink phenopackets export --mappings /path/to/custom_mappings.py
    
    # Enable debug mode for verbose logging
    rarelink phenopackets export --debug
    
    # Skip environment validation
    rarelink phenopackets export --skip-validation
    
    # Override CREATED_BY from .env
    rarelink phenopackets export --created-by "Your Name"
    
    # Set custom timeout (in seconds)
    rarelink phenopackets export --timeout 7200

All Command-Line Options
------------------------

.. list-table::
   :widths: 20 10 15 55
   :header-rows: 1

   * - Option
     - Short Flag
     - Type
     - Description
   * - ``--input-path``
     - ``-i``
     - PATH
     - Path to the input LinkML JSON file
   * - ``--output-dir``
     - ``-o``
     - PATH
     - Directory to save Phenopackets
   * - ``--mappings``
     - ``-m``
     - PATH
     - Path to custom mapping configuration module
   * - ``--debug``
     - ``-d``
     - FLAG
     - Enable debug mode for verbose logging
   * - ``--skip-validation``
     - 
     - FLAG
     - Skip environment validation
   * - ``--created-by``
     - 
     - TEXT
     - Override CREATED_BY from .env
   * - ``--timeout``
     - ``-t``
     - INTEGER
     - Timeout in seconds (default: 3600)
   * - ``--help``
     -
     - FLAG
     - Show help message and exit

Data Model Compatibility
~~~~~~~~~~~~~~~~~~~~~~~

The Phenopacket engine is designed to work with multiple data models:

**RareLink CDM Structure**:
   In the RareLink CDM, data is organized by instrument name with a specific data field:

   .. code-block:: json

      {
        "repeated_elements": [
          {
            "redcap_repeat_instrument": "rarelink_6_2_phenotypic_feature",
            "redcap_repeat_instance": 1,
            "phenotypic_feature": {
              "snomedct_8116006": "HP:0001059",
              "other_fields": "..."
            }
          }
        ]
      }

**Custom Data Model Structure**:
   For custom data models like CIEINR, data may be organized differently:

   .. code-block:: json

      {
        "repeated_elements": [
          {
            "redcap_repeat_instrument": "infections_initial_form",
            "redcap_repeat_instance": 1,
            "infections_initial_form": {
              "snomedct_21483005": "hp_0002383",
              "other_fields": "..."
            }
          }
        ]
      }

The engine automatically detects the data model structure and accesses the fields accordingly.

Mapping Configuration Structure
-------------------------------

The mapping configuration is a nested dictionary with the following key components:

1. **Block-level Configuration**
   - ``instrument_name``: REDCap instrument name for repeated elements
   - ``mapping_block``: Dictionary mapping REDCap fields to Phenopacket schema
   - ``label_dicts``: Dictionaries for human-readable labels
   - ``mapping_dicts``: Dictionaries for code mappings

2. **Supported Blocks**
   - ``individual``
   - ``vitalStatus``
   - ``diseases``
   - ``phenotypicFeatures``
   - ``measurements``
   - ``variationDescriptor``
   - ``interpretations``
   - ``metadata``

Advanced Configuration Options
-------------------------------

1. **Multiple Instruments**
   
   You can specify multiple instruments for a block using a set or list:

   .. code-block:: python

       "instrument_name": {"instrument1", "instrument2"}

2. **Data Model Specification**
   
   For custom data models, specify the model:

   .. code-block:: python

       "data_model": "infections"  # or "conditions", "rarelink_cdm", etc.

3. **Type Fields**
   
   Specify explicit type fields to scan:

   .. code-block:: python

       "type_fields": [
           "field1",
           "field2",
           "field3"
       ]

4. **Multi-onset Support**
   
   Enable multi-onset for features with multiple onset dates:

   .. code-block:: python

       "multi_onset": True,
       "onset_date_fields": [
           "onset_date_1",
           "onset_date_2"
       ]

5. **Field Scanning Control**
   
   Disable automatic field scanning:

   .. code-block:: python

       "enable_field_scanning": False

Mapping Strategies
------------------

1. **Label Dictionaries**
   Provide human-readable labels for codes:

   .. code-block:: python

       "label_dicts": {
           "GenderIdentity": {
               "code1": "Female",
               "code2": "Male"
           }
       }

2. **Mapping Dictionaries**
   Map local codes to standardized terms:

   .. code-block:: python

       "mapping_dicts": {
           "map_sex": {
               "local_code1": "FEMALE",
               "local_code2": "MALE"
           }
       }

3. **Instrument Names**
   Specify the correct REDCap instrument for repeated elements:

   .. code-block:: python

       "instrument_name": "your_repeat_instrument_name"

Best Practices
--------------

- Use ontology codes where possible
- Provide comprehensive label and mapping dictionaries
- Ensure instrument names match REDCap configuration
- Use the RareLink-CDM as a reference for mapping structure
- Enable multi-onset for features with multiple occurrence dates
- Set appropriate data model for specialized instruments
- Use explicit type fields to control which fields generate features

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

    PHENOTYPIC_FEATURES_BLOCK = {
        "redcap_repeat_instrument": "<instrument_name>",
        "type_field": "<feature_type_field>",
        "excluded_field": "<excluded_feature_field>",
        "onset_date_field": "<onset_date_field>",
        "onset_age_field": "<onset_age_field>",
        "resolution_field": "<resolution_field>",
        "severity_field": "<severity_field>",
        "evidence_field": "<evidence_field>",
        "modifier_field_1": "<modifier_field_1>",
        "modifier_field_2": "<modifier_field_2>",
        # For multi-onset support
        "multi_onset": True,
        "onset_date_fields": ["<date_field_1>", "<date_field_2>", "<date_field_3>"]
    }

**Notes**:

- Replace `<instrument_name>` and other placeholders with the specific field 
  names or codes used in your REDCap project or dataset.
- For repeating blocks, ensure the `redcap_repeat_instrument` value matches the 
  instrument name configured in REDCap.
- For multi-onset features, set "multi_onset": True and provide a list of date fields.
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
the BioPortal API by the ``DataProcessor``.

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


_____________________________________________________________________________________

.. _factory-approach:

Using the Factory Approach
~~~~~~~~~~~~~~~~~~~~~~~~~~

For more advanced use cases, you can use the PhenopacketMappingFactory to create
mappings for different data models:

.. code-block:: python

    from rarelink.phenopackets.factory import PhenopacketMappingFactory, get_phenopacket_mappings

    # Get mappings for RareLink CDM (default)
    rarelink_mappings = get_phenopacket_mappings()

    # Get mappings for a custom data model
    custom_mappings = get_phenopacket_mappings(model_name="your_model")

    # Creating phenopackets with specific model mappings
    from rarelink.phenopackets import create_phenopacket

    # Create phenopacket using the specified mappings
    phenopacket = create_phenopacket(
        data=record_data,
        created_by="Your Name",
        mapping_configs=custom_mappings
    )

The factory approach provides additional helper functions for working with different
data models:

1. **Converting to Multi-Instrument Format**
   
   .. code-block:: python
   
       updated_config = PhenopacketMappingFactory.convert_to_multi_instrument_format(
           config=mappings,
           block_name="phenotypicFeatures"
       )

2. **Merging Configurations**
   
   .. code-block:: python
   
       merged_config = PhenopacketMappingFactory.merge_configurations(
           base_config=base_mappings,
           override_config=custom_overrides
       )

_____________________________________________________________________________________

.. _troubleshooting:

Troubleshooting
~~~~~~~~~~~~~~~

Common issues and their solutions:

1. **No phenotypic features or diseases are generated**

   - Check that the instrument names in your mapping configuration match the actual 
     instrument names in your data
   - Verify that the field paths in your mapping block point to the correct fields
   - Enable debug mode (``--debug``) for more detailed logs

2. **Field values not found**

   - For RareLink CDM, remember that data is in a field named differently from the 
     instrument (e.g., "rarelink_5_disease" instrument has data in "disease" field)
   - For CIEINR-like models, data is in a field with the same name as the instrument

3. **Multi-onset features not working**

   - Ensure "multi_onset" is set to True in your configuration
   - Verify that "onset_date_fields" contains the correct field names
   - Check that the date fields contain valid date values

4. **Error: "No mapping found for name"**

   - Ensure your mapping dictionaries include the requested mapping name
   - Verify that the get_mapping_by_name function is properly implemented

5. **Timeout errors**

   - Increase the timeout value with ``--timeout 7200`` or higher
   - Process fewer records at a time

6. **Missing labels for codes**

   - Add the codes to your label dictionaries
   - Check BIOPORTAL API access if using external label lookups