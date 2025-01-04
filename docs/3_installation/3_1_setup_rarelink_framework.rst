.. _3_1:

Set up the RareLink Framework
=============================

.. warning:: 
    RareLink v2.0.0.dev0 is currently under development, and many things are 
    subject to change. Please reach out before implementing or using the 
    software to ensure you have the latest updates and guidance.

Getting Started
---------------

Follow these steps to set up the project locally and run tests.

1. Clone the repository:

.. code-block:: bash

      git clone https://github.com/BIH-CEI/rarelink.git
      cd rarelink

2. Create a virtual environment:

.. code-block:: bash

      python3 -m venv .venv
      source .venv/bin/activate  # On macOS/Linux
      .venv\Scripts\activate     # On Windows

3. Install dependencies:

.. code-block:: bash

      pip install .

4. Configure the `.env` file:
   Create a `.env` file in the project root directory. Add the following line:

.. code-block:: ini

    BIOPORTAL_API_TOKEN=your_api_token_here

   Replace `your_api_token_here` with your actual BioPortal API token.

5. Run tests:
   Use `pytest` to run the test suite.
   
.. code-block:: bash

      pytest


.. note:: 
    

_____________________________________________________________________________________

RareLink-CLI Framework Configuration
------------------------------------

To update the RareLink framework:

.. code-block:: bash

    rarelink framework update

This command updates the framework to the latest version.

To check the current framework status:

.. code-block:: bash

    rarelink framework status

This command provides a summary of the framework's current status.

To reset the framework to its initial state:

.. code-block:: bash

    rarelink framework reset

This command clears all framework configurations and reverts it to its initial setup state.


_____________________________________________________________________________________


Import Mapper Configuration
___________________________

Via the RareLink CLI type:

.. code-block:: bash

    to be implemented

This command guides you through setting up the Import Mapper pipeline for RareLink.
You will be prompted to enter:
- Your location of your local (tabular) database.
- Your REDCap project URL and API token.
- Your location where to store the Import Mapper configurations.

_____________________________________________________________________________________

Phenopacket Pipeline Configuration
___________________________________

Via the RareLink CLI type:

.. code-block:: bash

    to be implemented

This command guides you through setting up the Phenopacket pipeline for RareLink.
You will be prompted to enter:
- Your location where to store the Phenopackets.

_____________________________________________________________________________________

FHIR Pipeline Configuration
___________________________

.. code-block:: bash

    to be implemented

This command guides you through setting up the FHIR pipeline for RareLink. 
You will be prompted to enter:
- Your FHIR server URL.
- If required, your FHIR server username & password.

