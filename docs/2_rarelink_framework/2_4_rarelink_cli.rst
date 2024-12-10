.. _2_4:

RareLink CLI
=============

.. warning:: 
    RareLink v2.0.0.dev0 is currently under development, and many things are 
    subject to change. Please reach out before implementing or using the 
    software to ensure you have the latest updates and guidance.

The RareLink Command Line Interface (CLI) is a tool that allows you to interact
 with the RareLink framework. The CLI provides a set of commands that allow you
  to set up and manage the RareLink framework, as well as to interact with the 
  data stored in the framework. The CLI is designed to be user-friendly and
   intuitive, and it provides a simple and efficient way to work with the
    RareLink framework.


General CLI Command Groups
--------------------------


Framework Setup (``framework``)
_________________________________

Commands related to setting up and managing the overall RareLink framework:

.. code-block:: console

    rarelink framework reset

This command clears all framework configurations and reverts it to its initial
setup state.

.. code-block:: console

    rarelink framework status

This command provides a summary of the framework's current status and 
version installed.
   

.. code-block:: console

    rarelink framework update

This command updates the framework to the latest version.


REDCap Setup (``redcap-setup``)
________________________________

Commands focused on configuring REDCap, setting up projects, and initializing 
API access:

_____________________________________________________________________________________

.. code-block:: console

    rarelink redcap-setup --help

guided project setup, documentation links, admin instructions

_____________________________________________________________________________________

.. code-block:: console

    rarelink redcap-setup api-config 

- API token configuration and management, see :ref:`3_4` for more details and functionalities, and instructions.

_____________________________________________________________________________________

.. code-block:: console

    rarelink redcap-setup download --help

- Download the most current RareLink-CDM data dictionary, the RareLink-CDM instruments, and the RareLink Template REDCap project. See :ref:`3_2`and :ref:`3_3` for more details and functionalities, and instructions.

_____________________________________________________________________________________

.. code-block:: console

    rarelink redcap-setup data-dictionary upload

Upload the most current custom data dictionary

_____________________________________________________________________________________

REDCap Tools (``redcap-tools``)
________________________________

Commands for interacting with an already-configured REDCap instance, i.e. your
local REDCap project. 

.. note::
    For this you need your REDCap project running and API access configured.
    Run `rarelink redcap-setup redcap-project-setup` and `rarelink redcap-setup 
    redcap-api-setup start` to set up a REDCap project and API access. 

- `download-records` (fetch records as JSON files)
- `upload-records` (upload records from JSON files)
- `fetch-metadata` (download metadata such as field labels and configurations)