.. _3_2:

Set up a REDCap Project
========================

.. warning:: 
   RareLink v2.0.0.dev0 is under development. Please :ref:`12` us before using
   it to ensure you have the latest updates and guidance.



Steps
------

To create a REDCap project, please follow these steps:

0. Check if your instituion hase a REDCap instance.
1. Contact your local REDCap administrator to create your REDCap project.
2. Name your REDCap project, e.g.: 
    - ``RareLink - NameofyourInstitution`` or 
    - ``RareLink - NameofyourProject``.
3. Let your institutional account be added and given API access for the project.
4. Follow the instructions given to you by your **REDCap administator** to 
   further set up your project.
5. Copy the API token for the project and keep it secure.
6. Run ``rarelink setup keys``` to set up the REDCap API access locally.

.. note:: 
    Be aware of the REDCap **development and production mode**. 
    Read the :ref:`1_6` section and discuss this with your REDCap administrator!

_____________________________________________________________________________________

Next Steps and further reading
-------------------------------

- Read the :ref:`1_6` section to learn more about the REDCap API access.
- Read :ref:`2_3` to learn more about the RareLink Command Line Interface (CLI)
- Read :ref:`4_0` to learn more about the RareLink User Guide.
_____________________________________________________________________________________


RareLink CLI Commands
----------------------

.. code-block:: bash

    rarelink setup redcap-project

- This command will guide you through the same steps above. If you have 
  questions, please reach out to us or your local REDCap administrator.


- Make sure to run 

.. code-block:: bash

    rarelink setup keys

after you have set up the REDCap project to store the REDCap API token.

.. attention::
    The REDCap API token is a sensitive information. Keep it secure and do 
    not share it with others.
    
_____________________________________________________________________________________

