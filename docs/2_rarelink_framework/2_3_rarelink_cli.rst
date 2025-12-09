.. _2_3:

RareLink CLI
=============

The RareLink Command Line Interface (CLI) is a tool that allows you to interact
with the RareLink framework. The CLI provides a set of commands that allow you
to set up and manage the RareLink framework, as well as to interact with the 
data stored in the framework. The CLI is designed to be user-friendly and
intuitive, and it provides a simple and efficient way to work with the RareLink
framework.

**Overview**

- :ref:`rarelink_cli_framework`
- :ref:`rarelink_cli_setup`
- :ref:`rarelink_cli_redcap`
- :ref:`rarelink_cli_fhir`
- :ref:`rarelink_cli_phenopackets`

_____________________________________________________________________________________


.. _rarelink_cli_framework:

1. Framework Setup (``framework``)
_________________________________

Commands related to setting up and managing the overall RareLink framework:

_____________________________________________________________________________________

.. code-block:: console

    rarelink framework reset

This command clears all framework configurations and reverts it to its initial
setup state.

_____________________________________________________________________________________

.. code-block:: console

    rarelink framework status

This command provides a summary of the framework's current status and 
version installed.
   
_____________________________________________________________________________________

.. code-block:: console

    rarelink framework update

This command updates the framework, submodules and other components
to the latest version.

_____________________________________________________________________________________

.. _rarelink_cli_setup:

2. REDCap Setup (``setup``)
________________________________

Commands focused on configuring REDCap, setting up projects, and initializing 
API access:

_____________________________________________________________________________________


.. code-block:: console

    rarelink setup --help

- guided project setup, documentation links, admin instructions

_____________________________________________________________________________________


.. code-block:: console

    rarelink setup redcap-project

- Start here if you want to set up your local REDCap Project for RareLink!

_____________________________________________________________________________________

.. code-block:: console

    rarelink setup keys 

- Configure the RareLink framework by setting up API keys and variables. This
  process ensures the .env file contains necessary configurations - see :ref:`3_4`
  for more details, functionalities, and instructions.

_____________________________________________________________________________________


.. code-block:: console

    rarelink setup dictionary-dictionary

- Upload the most current RareLink-CDM Data Dictionary to an existing 
  REDCap project.

_____________________________________________________________________________________

.. code-block:: console

    rarelink setup view

- View the current RareLink API configuration and its location.


_____________________________________________________________________________________

.. code-block:: console

    rarelink setup reset

- Reset all RareLink configuration by wiping the .env and JSON files.

.. note::
    The API Keys are sensitive information and should be stored securely.
    Do not share them with anyone outside your organisation. Within this  
    repository the .env file and the JSON files are ignored by the .gitignore
    file to prevent accidental sharing of sensitive information.


.. _rarelink_cli_redcap:


3. REDCap Tools (``redcap``)
___________________________________

Commands for interacting with an already-configured REDCap instance, i.e. your
local REDCap project. 

.. code-block:: console

    rarelink redcap --help

The overview of all redcap-tools functionalities and commands.

_____________________________________________________________________________________

Download REDCap Records Command
---------------------------------

.. code-block:: console

    rarelink redcap download-records [OPTIONS]

Options:
  -o, --output-dir PATH       Directory to save fetched and processed records
  -r, --records TEXT          Record IDs to fetch (comma-separated, e.g. “101,102”)
  -i, --instruments TEXT      Instruments/forms to fetch (comma-separated)
  -l, --linkml PATH           Custom LinkML schema for validation
      --rarelink-cdm          Use RareLink-CDM instruments and schema
      --filter TEXT           REDCap filter logic to apply (e.g. “[age] > 30”)
  --help                      Show this message and exit

Description
~~~~~~~~~~~

Download REDCap records, arms, and events, process them into the RareLink-CDM schema,
validate the result against a LinkML schema (either RareLink-CDM or a custom one),
and save JSON outputs.

.. attention::
    If your project is in PRODUCTION mode, the downloaded data may be sensitive.
    Store it only in approved, secure storage. See the REDCap “Project Status” docs
    for more guidance.

.. hint::
    If your dataset includes genetic HGVS mutations, please run 
    ``rarelink redcap validate-hgvs`` after downloading records to ensure proper 
    phenopackets and genomics quality of the genetic data.

_____________________________________________________________________________________

.. _rarelink_redcap_validate_hgvs:

Validate HGVS Strings CLI Command
----------------------------------

.. rubric:: Command

.. code-block:: console

    rarelink redcap validate-hgvs [OPTIONS]

.. rubric:: Description

   Validate and encode HGVS strings in the downloaded records to ensure proper
   phenopackets and genomics quality of the genetic data. This command will
   iterate through your downloaded data, validate all HGVS strings (recursing
   into nested structures), and give you a summary of the validation process.

.. rubric:: Options

.. list-table::
   :header-rows: 1
   :widths: 15 60

   * - Option
     - Description
   * - ``-i, --input-file <PATH>``
     - Path to the specific JSON file containing REDCap records.  
       If omitted, the command will prompt or use the default download directory.
   * - ``-d, --input-dir <DIR>``
     - Directory containing REDCap records; looks for ``<PROJECT_NAME>-records.json`` inside.
   * - ``-v, --hgvs-variable <FIELD_NAME>``
     - (Repeatable) Name of an HGVS field to validate.  
       You can specify this flag multiple times to validate custom HGVS fields.  
       If omitted, defaults to the built-in ``HGVS_VARIABLES`` list.
   * - ``--help``
     - Show this message and exit.

.. rubric:: Examples

Validate using the default HGVS fields:

.. code-block:: console

    rarelink redcap validate-hgvs

Specify a custom set of HGVS fields:

.. code-block:: console

    rarelink redcap validate-hgvs \\
      -i ~/Downloads/MyProject-records.json \\
      -v loinc_81290_9 \\
      -v CUSTOM_HGVS_FIELD \\
      -v OTHER_HGVS_FIELD

_____________________________________________________________________________________

.. code-block:: console 

    rarelink redcap fetch-metadata

- Fetch all metadata from your current REDCap project. 

_____________________________________________________________________________________

.. code-block:: console

    rarelink redcap upload-records

- Upload records to your REDCap project from JSON files stored locally.

.. warning:: 
    This command will overwrite existing records with the same record_id in your
    REDCap project. Make sure have unique ``record_id``s or back up your data
    before running this command, e.g. by running 
    `rarelink redcap download-records`.

_____________________________________________________________________________________


.. _rarelink_cli_fhir:

4. FHIR configuration and pipelines (``fhir``)
______________________________________________

 Setup, manage, and execute the REDCap-FHIR module. 

_____________________________________________________________________________________

.. code-block:: console

    rarelink fhir --help

The overview of all FHIR functionalities and commands.

_____________________________________________________________________________________

.. code-block:: console

    rarelink fhir setup

- Configure the toFHIR pipeline for the RareLink framework.

_____________________________________________________________________________________

.. code-block:: console

    rarelink fhir hapi-server

- Set up a local HAPI FHIR server with Docker, avoiding conflicts.

_____________________________________________________________________________________

.. code-block:: console

    rarelink fhir restart-dockers

- Stop, remove, and restart all relevant Docker containers.

_____________________________________________________________________________________

.. code-block:: console

    rarelink fhir export

- Export data to the configured FHIR server using the toFHIR pipeline.


.. note::
    For this you need your REDCap project running and API access configured.
    Run `rarelink redcap-setup redcap-project-setup` and `rarelink redcap-setup 
    redcap-api-setup start` to set up a REDCap project and API access. 

- `download-records` (fetch records as JSON files)

_____________________________________________________________________________________

.. _rarelink_cli_phenopackets:

5. Phenopacket Export (``phenopackets``)
________________________________________

Export data to Phenopackets using the ToPhenopacket pipeline.

.. code-block:: console

    rarelink phenopackets export

- Exports REDCap from your configured project data to local Phenopackets.