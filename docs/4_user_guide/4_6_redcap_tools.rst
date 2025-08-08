.. _4_6:

REDCap Tools
==============

Once you have your API access set up, you can interact with your REDCap project: 


API Endpoints
----------------

**Download Records**

The ``download-records`` command allows users to export records from REDCap, process them into LinkML format, and optionally validate them against a schema. The command now provides an interactive workflow to guide users through the process.

.. code-block:: bash

    # Basic usage - follows interactive prompts for configuration
    rarelink redcap download-records
    
    # Validate against the RareLink CDM schema (automatically selects RareLink instruments)
    rarelink redcap download-records --rarelink-cdm
    
    # Validate against a custom LinkML schema
    rarelink redcap download-records --linkml /path/to/custom-schema.yaml
    
    # Download specific records
    rarelink redcap download-records --records 101,102,103
    
    # Download specific instruments/forms
    rarelink redcap download-records --instruments form1,form2
    
    # Filter records using REDCap logic
    rarelink redcap download-records --filter "[age] > 30"
    
    # Combine multiple options
    rarelink redcap download-records --rarelink-cdm --records 101,102 --instruments additional_form

Options:
  - ``--output-dir, -o``: Directory to save fetched and processed records
  - ``--records, -r``: Specific record IDs to fetch (comma-separated)
  - ``--instruments, -i``: Specific instruments/forms to fetch (comma-separated)
  - ``--linkml, -l``: Path to custom LinkML schema for validation
  - ``--rarelink-cdm``: Use RareLink-CDM instruments and validate against its schema
  - ``--filter``: REDCap filter logic to apply (e.g., ``[age] > 30``)

Interactive Workflow:
  When run without parameters, the command will guide you through these steps:
  
  1. Ask whether you want to use RareLink-CDM instruments
  2. If not using RareLink-CDM, ask if you have a custom LinkML schema for validation
  3. Ask if you want to fetch specific record IDs
  4. Ask if you want to fetch specific instruments/forms (if not using RareLink-CDM)

Using the RareLink-CDM option will automatically select all RareLink instruments, but you can still specify additional instruments to include.

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

The ``validate-hgvs`` command allows users to validate HGVS strings in REDCap 
records. It processes the genetic findings and produces a validation report.

.. code-block:: bash

    # Basic usage - interactively confirms default file location
    rarelink redcap validate-hgvs
    
    # Specify a specific input file
    rarelink redcap validate-hgvs --input-file /path/to/records.json
    
    # Specify a directory containing the records
    rarelink redcap validate-hgvs --input-dir /path/to/records/directory

Options:
  - ``--input-file, -i``: Path to the specific JSON file containing REDCap records
  - ``--input-dir, -d``: Directory containing the REDCap records

Interactive Workflow:
  When run without parameters, the command will:
  
  1. Show the default file path and ask for confirmation
  2. If not confirmed, prompt for a custom file path
  3. Validate the HGVS strings in the records
  4. Provide a validation summary report

The command reports the total number of validations attempted, successes, and 
failures. For any failed validations in genetic findings records, it lists the 
record ID, repeat instance, and specific error.