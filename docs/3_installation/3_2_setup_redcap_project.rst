.. _3_3:

Setup a REDCap Project
========================

.. attention::
   To use your local REDCap project, you will need to set up a local REDCap 
   instance. For this please contact your local REDCap administratior. A project
   name could for example be "RareLink - Your local REDCap location". 

.. note::
    This section is still to be implemented in the docuemntation and the RareLink
    command line interface.

Via the RareLink CLI type:

.. code-block:: bash

    rarelink framework-setup redcap-project-setup start


This command guides you through the steps to set up your REDCap project, 
including contacting your local REDCap administrator and ensuring API access for your project.

_____________________________________________________________________________________

.. tip:: 
  Read the :ref:`1_6` section to learn more about the REDCap API access.

.. attention::
    The REDCap API token is a sensitive information. Keep it secure and do not share it with others.

👉 For more information on REDCap, read :ref:`1_6`. 
_____________________________________________________________________________________

To create a REDCap project, please follow these steps:

0. Check if your instituion hase a REDCap instance - if not read above documentation.
1. Contact your local REDCap administrator to create your REDCap project.
2. Name your REDCap project, e.g.: 'RareLink - NameofyourInstitution'.
3. Let your institutional account be added and provide you API access for the project.
4. Follow the instructions given to you by your REDCap administator to further set up your project.
👉 Be aware of development and production mode. Read the docs and discuss this with your REDCap admin!
5. Copy the API token for the project and keep it secure.
6. Run 'rarelink redcap-api-setup start' to set up the REDCap API access.