.. _4_6:

REDCap Tools
==============

Once you have your API access set up, you can interact with your REDCap project: 


API Endpoints
----------------

**Download Records**

The `download-records` command allows users to export records from REDCap, process them into LinkML format, and optionally validate them against a schema.

.. code-block:: bash

    # Basic usage - downloads and processes data without validation
    rarelink redcap download-records
    
    # Validate against the RareLink CDM schema
    rarelink redcap download-records --rarelink-cdm
    
    # Validate against a custom LinkML schema
    rarelink redcap download-records --linkml /path/to/custom-schema.yaml
    
    # Specify custom output directory
    rarelink redcap download-records --output-dir /path/to/output/dir

Options:
  - ``--output-dir, -o``: Directory to save fetched and processed records
  - ``--linkml, -l``: Path to custom LinkML schema for validation
  - ``--rarelink-cdm``: Validate against the RareLink CDM schema

Validation is optional but recommended to ensure data quality and compatibility with downstream tools.


**Fetch Metadata**

The `fetch-metadata` command allows users to fetch metadata from REDCap.

.. code-block:: bash

    rarelink redcap fetch-metadata


**Import Records**

The `import-records` command allows users to import records into REDCap.

.. code-block:: bash

    rarelink redcap upload-records


**Validate HGVS** 

The `validate-hgvs` command allows users to validate HGVS strings.

.. code-block:: bash

    rarelink redcap validate-hgvs