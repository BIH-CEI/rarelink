.. _3_3:


Data Dictionary
================

.. warning:: 
   RareLink v2.0.0.dev0 is under development. Please :ref:`12` us before using
   it to ensure you have the latest updates and guidance.



To install the RareLink CDM instruments, you will need to download the 
instruments from the RareLink REDCap project.

.. tip:: 
  Read the :ref:`2_2` section to learn more about the RareLink CDM Instruments.  

1. **Download the instruments from the RareLink REDCap project.**

- :download:`Download RareLink CDM Data Dictionary v2.0.0.dev0 <../../res/rarelink_cdm_v2_0_0_dev0_datadictionary.csv>`

To upload your data dictionary to your REDCap project, type:

.. code-block:: console

    rarelink setup data-dictionary

_____________________________________________________________________________________

2. **Import the instruments into your REDCap project.**

- Go to your REDCap project.
- Click on the "Designer" tab on the left side of the screen.
- Click on the "Data Dictionary" tab on the top of the screen.
- Select the RareLink CDM Data Dictionary CSV file, or the separate instrument csv files.
- Click on the "Import" button.

_____________________________________________________________________________________

.. image:: ../_static/res/redcap_gui_screenshots/DesignerTab.jpg
  :alt: Designer tab
  :align: center
  :width: 400px
  :height: 250px

_____________________________________________________________________________________

.. image:: ../_static/res/redcap_gui_screenshots/DataDictionary.jpg
  :alt: Data Dictionary tab
  :align: center
  :width: 600px

_____________________________________________________________________________________

3. **Verify that the instruments have been imported correctly.**

- Go to the "Online Designer" tab and check the data elements in each instrument.
- check with the :ref:`2_2` page to verify that
    - the instruments have been imported correctly.
    - the instruments are consistent with the RareLink CDM Data Dictionary.
    - the fields with BioPortal are connected properly.

_____________________________________________________________________________________

4. **Start capturing data with the RareLink CDM instruments.**

Check out the : or 
the :ref:`4_2` section to learn more about the semi-automatic import of data.

.. admonition:: Continue here...

    - :ref:`4_1` section to learn on how to use the RareLink CDM instruments.
    - :ref:`4_2` section to learn on how to import data from tabular databases.
    - :ref:`4_3` section to learn on how to export data to Phenopackets.
    - :ref:`4_3` section to learn on how to export data to FHIR.

.. admonition:: Further reading...

    - Read pages 25 & 26 of the `Comprehensive Guide to REDCap <https://www.unmc.edu/vcr/_documents/unmc_redcap_usage.pdf>`_ for more information. 
    - Read the :ref:`1_6` section to learn more about the general REDCap Setup, 
        among others how to connect BioPortal to REDCap.



.. attention::
   To use your local REDCap project, you will need to set up a local REDCap 
   instance. For this please contact your local REDCap administratior. A project
   name could for example be "RareLink - Your local REDCap location". 

This section provides a guide for developing REDCap instruments around the
RareLink CDM that can also be processed by the Phenopacket and FHIR pipeline.
If the rules are followd upon development of the REDCap sheets, another 
subsequent mapping step will be required to convert the data into the
Phenopackets or FHIR format. For this second step guides are given below, too. 


Separate RareLink-CDM Instruments
----------------------------------

The :ref:`2_2` section provides an overview of the RareLink-CDM which is
based on the ontology-based rare disease common data model (:ref:`_1_5`).
However, for many use cases, it may be necessary to use only a subset of the
instruments. 

For such cases, please note:
- If you use the RareLink-CDM instruments, you will not need to enter data 
    for all instruments - many of these instruments can be left empty or deleted.
- The RareLink-CDM instruments are designed to be used in a modular way, 
    so you can use only the instruments that are relevant to your study.
- However, if an instrument is used in your study, it is important to fill 
    in all `mandatory` the fields in that instrument to ensure correct FHIR 
    and Phenopacket export (More Info: :ref:`4_1`)
- The sheets `(1) Formal Criteria` and `(2) Personal Information` must
  always be filled in to ensure correct FHIR and Phenopacket export!
- Feel free to :ref:`12` us in case you have any questions or need help.


Extensional RareLink-CDM Instruments
------------------------------------

The :ref:`2_2` section provides an overview of the RareLink-CDM which is 
based on the ontology-based rare disease common data model (:ref:`_1_5`). 
However, for many use cases, it is necessary to extend the data model with
additional fields or instruments. This can be done by following the
established RareLink guidelines given in the :ref:`4_5` section.

- Feel free to :ref:`12` us in case you have any questions or need help.


