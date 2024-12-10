.. _3_1:

Set up the RareLink Framework
=============================

.. warning:: 
    RareLink v2.0.0.dev0 is currently under development, and many things are 
    subject to change. Please reach out before implementing or using the 
    software to ensure you have the latest updates and guidance.

To set up the RareLink framework, follow these steps:

**Install the RareLink framework dependencies.**
-------------------------------------------------

Clone the repository and install the dependencies:

.. code-block:: bash

    pip install -e .

Via the RareLink CLI, type:

.. code-block:: bash

    pip install rarelink

This command installs all necessary RareLink framework dependencies and functionalities.

To update the RareLink framework:

.. code-block:: bash

    pip install --upgrade rarelink

This command updates the framework to the latest version.

To check the current framework status:

.. code-block:: bash

    pip show rarelink

    or

    python -m rarelink --version

This command provides a summary of the framework's current status.

To reset the framework to its initial state:

.. code-block:: bash

    pip uninstall rarelink -y && pip install rarelink

This command clears all framework configurations and reverts it to its initial setup state.


Import Mapper Configuration
___________________________

Via the RareLink CLI type:

.. code-block:: bash

    rarelink setup -pipeline import_mapper

This command guides you through setting up the Import Mapper pipeline for RareLink.
You will be prompted to enter:
- Your location of your local (tabular) database.
- Your REDCap project URL and API token.
- Your location where to store the Import Mapper configurations.

Phenopacket Pipeline Configuration
________________________________

Via the RareLink CLI type:

.. code-block:: bash

    rarelink setup -pipeline phenopackets

This command guides you through setting up the Phenopacket pipeline for RareLink.
You will be prompted to enter:
- Your location where to store the Phenopackets.

FHIR Pipeline Configuration
___________________________

.. code-block:: bash

    rarelink setup -pipeline fhir

This command guides you through setting up the FHIR pipeline for RareLink. 
You will be prompted to enter:
- Your FHIR server URL.
- If required, your FHIR server username & password.

