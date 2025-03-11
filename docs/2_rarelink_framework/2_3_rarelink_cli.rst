.. _2_3:

RareLink CLI
=============

.. attention:: 
   RareLink v2.0.0.dev1 is under testing and development. Please :ref:`12` us 
   before using it to ensure you have the latest updates and guidance.


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

    rarelink setup dictionary

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

.. code-block:: console

    rarelink redcap download-records

Download records from your REDCap project as JSON files and save them locally.

.. attention::
    If your project is in PRODUCTION mode, the downloaded data might be sensitive.
    It must only be stored within your organisational site's approved storage.
    Read here more about the :ref:`1_6` project modes and discuss this
    with your REDCap administrator.

.. hint::
    If your dataset includes genetic HGVS mutations, please run 
    ``rarelink redcap validate-hgvs`` after downloading records to ensure proper 
    phenopackets and genomics quality of the genetic data.

_____________________________________________________________________________________

.. code-block:: console

    rarelink redcap validate-hgvs

Validate and encode HGVS strings in the downloaded records to ensure proper 
phenopackets and genomics quality of the genetic data. This command will 
iterate through your downloaded data, validate all HGVS strings and give you a 
summary of the validation process.

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