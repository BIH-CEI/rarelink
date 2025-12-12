.. _3_3:


Set up the Data Dictionary
==========================


To install the RareLink-CDM instruments, you will need to download the 
instruments from here and follow the steps below. Make sure your REDCap project
is set up and running, otherwise follow the :ref:`3_2` section to set up a 
REDCap project. Read the :ref:`2_2` section to learn more about the RareLink CDM
Instruments. In case you have any questions, please contact your local REDCap 
administrator, or :ref:`12` us. 

- :ref:`data_dictionary_installation`
- :ref:`data_dictionary_customise`

_____________________________________________

.. _data_dictionary_installation:

Installation
-------------

_____________________________________________________________________________________

1. **Download the instruments from the RareLink REDCap project.**

- |data_dict_download|

2. **Upload the data dictionary to your REDCap project**

To upload your data dictionary to your REDCap project automatically, type:

.. code-block:: console

    rarelink setup data-dictionary

Otherwise you can also import the instruments manually:

- Go to your REDCap project.
- Click on the "Designer" tab on the left side of the screen.

.. image:: ../_static/res/redcap_gui_screenshots/DesignerTab.jpg
  :alt: Designer tab
  :align: center
  :width: 400px

_____________________________________________________________________________________

- Click on the "Data Dictionary" tab on the top of the screen.


.. image:: ../_static/res/redcap_gui_screenshots/DataDictionary.jpg
  :alt: Data Dictionary tab
  :align: center
  :width: 400px
  
_____________________________________________________________________________________

- Select the RareLink CDM Data Dictionary CSV file, or the separate instrument csv files.
- Click on the "Import" button.

_____________________________________________________________________________________

3. **Verify that the instruments have been imported correctly.**

- Go to the "Online Designer" tab and check the data elements in each instrument.
- check with the :ref:`2_2` page to verify that
    - the instruments have been imported correctly.
    - the instruments are consistent with the RareLink CDM Data Dictionary.
    - the fields with BioPortal are connected properly.


_____________________________________________________________________________________  

4. **Activate the repeating instruments feature**

- Go to the ``Project Setup`` tab.
- Within the section Enable optional modules and customizations click 
  on the **`Enable` Repeating Instruments** checkbox.
- Enable repeating instruments for the following instruments: 

.. image:: ../_static/res/rarelink-cdm-repeating-instruments.jpg
   :alt: RareLink CDM Repeating Instruments
   :align: center
   :width: 400px

_____________________________________________________________________________________

5. **Start capturing data with the RareLink CDM instruments.**

Check out the :ref:`4_1` or the :ref:`4_2` section to learn more about the 
semi-automatic import of data.

_____________________________________________________________________________________ 

.. admonition:: Continue here...

    - :ref:`4_1` section to learn on how to use the RareLink CDM instruments.
    - :ref:`4_2` section to learn on how to import data from tabular databases.
    - :ref:`4_3` section to learn on how to export data to Phenopackets.
    - :ref:`4_3` section to learn on how to export data to FHIR.

.. admonition:: Further reading...

    - Read pages 25 & 26 of the `Comprehensive Guide to REDCap <https://www.unmc.edu/vcr/_documents/unmc_redcap_usage.pdf>`_ for more information. 
    - Read the :ref:`1_6` section to learn more about the general REDCap Setup, 
        among others how to connect BioPortal to REDCap.

Separate RareLink-CDM Instruments
----------------------------------

The :ref:`2_2` section provides an overview of the RareLink-CDM which is
based on the **ontology-based rare disease common data model** harmonising
international registries, FHIR, and Phenopackets (:ref:`1_5`). However, for many
use cases, it may be necessary to use only a subset of the instruments. 

For such cases, please note:

1. If you use the RareLink-CDM instruments, you will **not need to enter data 
   for all instruments** - many of these instruments can be left empty or deleted.
2. The RareLink-CDM instruments are designed to be used in a **modular way**, 
   so you can use only the instruments that are relevant to your study.
3. However, if an instrument is used in your study, it is important to fill 
   in all ``mandatory`` the fields in that instrument to ensure correct FHIR 
   and Phenopacket export. Please read:

   - Section :ref:`cdm-instruments-overview`
   - & :ref:`4_1` 
4. The sheets ``(1) Formal Criteria`` and ``(2) Personal Information`` **must**
   always be filled in to ensure correct FHIR and Phenopacket export!
5. Feel free to :ref:`12` us in case you have any questions or need help.

Extensional RareLink-CDM Instruments
------------------------------------

The :ref:`2_2` section provides an overview of the RareLink-CDM which is 
based on the **ontology-based rare disease common data model** (:ref:`1_5`). 
However, for many use cases, it is necessary to extend the data model with
additional fields or instruments. This can be done by following the
established RareLink guidelines given in the :ref:`4_5` section. Feel free to 
:ref:`12` us in case you have any questions or need help.

________________________________

.. _data_dictionary_customise:

Customise the Data Dictionary
-----------------------------

In many cases it may be necessary to customise the RareLink-CDM Data Dictionary
to suit your specific needs or simplify manual data capture. To ensure that the FHIR 
and Phenopacket modules work correctly, it is important to follow the guidelines below. 

To customise your RareLink-CDM Data Dictionary, you can... 

Hide fields 
^^^^^^^^^^^^^^^

- ...add the ``@HIDDEN`` actiontag to fields that you do not want to display in the REDCap project.
  This can be useful for fields that are not required in your specific profect for manual data entry and 
  can therefore be hidden from the user interface.
  - You can find more information on the ``@HIDDEN`` action tag in the  
    `ActionTag REDCap documentation <https://www.ctsi.ufl.edu/wordpress/files/2019/02/Using-Action-Tags-in-REDCap.pdf>`_.
  
  .. note::
      Make sure you do not hide fields that are marked as ``required`` within the REDCap instrument and RareLink-CDM. 
      You can find all the required fields in the :ref:`cdm_overview` subsection of the :ref:`2_2` section.


Change labels & descriptions 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ...change the field labels or field descriptions to better suit your project needs. 
  This can be useful to clarify the meaning of a field or to provide additional information to the user.
  - You can find more information on how to change field labels and descriptions in the 
    `REDCap documentation <https://kb.wisc.edu/smph/informatics/page.php?id=92573>`_.

   .. important:: 
      **Do not change the field name or variable**: The field variables/names in the RareLink-CDM Data Dictionary are 
      used to map the data to FHIR and Phenopackets. Changing the field names will break the mapping.


Multi-language management
^^^^^^^^^^^^^^^^^^^^^^^^^^

- ...edit and add the language settings for the RareLink-CDM using the REDCap 
  `Multi-language Management feature <https://kb.wisc.edu/smph/informatics/page.php?id=115603>`_.
  This can be useful to provide the RareLink-CDM instruments in multiple languages for your users.

.. note:: 
   Feel free to :ref:`12` in case you are interested in creating official language versions of the RareLink-CDM Instruments
   or RareLink. We are happy to collaborate with you on this and support you in the process.

Add new fields & instruments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ... add new fields and instruments to the RareLink-CDM as extensions:
  This can be useful to capture additional information that is not included in the RareLink-CDM Data Dictionary.
  For this please refer to the guidelines in the :ref:`4_5` section on how to extend the RareLink-CDM Data Dictionary.

.. hint::
   In case you have questions, please :ref:`12` directly or `write an issue on GitHub <https://github.com/BIH-CEI/rarelink/issues/new>`_
   to ensure you make use of the RareLink framework in the best possible way. 
   We are happy to help you with any questions you may have and collaborate on extensions and improvements.

