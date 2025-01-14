.. _4_2:

Semi-Automatic Data Capture
===========================

.. warning:: 
   RareLink v2.0.0.dev0 is under development. Please :ref:`12` us before using
   it to ensure you have the latest updates and guidance.


While there are many existing data bases in rare disease centres and hospitals, 
the data is often not in a structured format. RareLink provides a semi-automatic
data capture configuration using the Schema Automator that allows users to 
capture data from existing databases and convert it into a structured format - 
in our case the RareLink-CDM LinkML schema.

.. attention::
    This section is still to be implemented in the docuemntation and the RareLink
    command line interface.


Via the RareLink CLI type:

.. code-block:: bash

    rarelink import -file <path_to_excel_file> -map <mapping_config>
