.. _4_2:

Semi-Automatic Data Capture
===========================

.. attention:: 
   RareLink v2.0.0.dev1 is under testing and development. Please :ref:`12` us 
   before using it to ensure you have the latest updates and guidance.


While there are many existing data bases in rare disease centres and hospitals, 
the data is often not in a structured format. As the RareLink-CDM is a modeled 
with LinkML, there are tools to convert existing data into a LinkML schema.
While we currently have not implemented a full conversion tool, we are happy 
to assist you in converting your data into a LinkML schema.

Although the semi-automation can speed up the process of capturing existing data
bases, the semantic mapping will still have to be done by you.
The semantic mapping and encoding of all data elements and value sets 
to :ref:`1_2` and validating genetic mutations with HGVS is a crucial step
in the process of converting data into the RareLink-CDM format for 
Phenopackets of FHIR export. 


____________________________________________________________________________________


RareLink-CDM LinkML
-------------------

In this seciton :ref:`rarelink_cdm_linkml` we elaborate on the development of 
the RareLink-CDM LinkML schema, how it is designed and where it can be found. 
This schema is the basis for REDCap data to be converted to and validated 
against when running ``rarelink redcap export-records``. It was designed to be
light-weight and as close as possible to the original REDCap data model so that
other REDCap projects can also use the :ref:`rarelink-phenopacket-module`.

____________________________________________________________________________________

LinkML schema-automator
------------------------
The LinkML schema-automator is a toolkit that assists with generating and 
enhancing schemas and data models from a variety of sources. The primary end 
target is a LinkML schema, but the framework can be used to generate 
JSON-Schema, SHACL, SQL DDL etc via the LinkML Generator framework. All 
functionality is available via a cli. The functionality is also available 
by using the relevant Python Packages.

- `LinkML Schema-Automator documentation <https://linkml.io/schema-automator/introduction.html#generalization-from-instance-data>`_
- `LinkML Schema-Automator GitHub repository <https://github.com/linkml/schema-automator>`_

.. note:: 
    Feel free to :ref:`12` us in case you would like to be connected to the LinkML 
    community or our colleagues from the `Monarch Initiative <https://monarchinitiative.org/>`_.

____________________________________________________________________________________

Steps when importing data 
--------------------------

1. Annotate and encode your data locally according to the 
   :ref:`rarelink_cdm_linkml` schema. Use the :ref:`4_1` and `Ontology Lookup Service <https://www.ebi.ac.uk/ols4/ontologies>`_

2. Map and process your data acccording to the RareLink-CDM LinkML schema. 
   
.. tip:: 
   Use the RareLink-CDM LinkML python classes for validation and conversion,
   which you can find `HERE <https://github.com/BIH-CEI/rarelink/tree/develop/src/rarelink_cdm/v2_0_0_dev1/datamodel>`_ 

3. Validate your data against the RareLink-CDM LinkML schema: 

.. code-block:: bash

    linkml-validate --schema src/rarelink_cdm/v2_0_0_dev1/schema_definitions/rarelink_cdm.yaml <path_to_your_data.json>


You can find LinkML-validated RareLink-CDM data here `RareLink_Berlin-linkml-records.json <https://github.com/BIH-CEI/rarelink/tree/develop/res/RareLink_Berlin-linkml-records.json>`_ 


4. Once the data is validated, you can upload the data to your REDCap project 
   using the ``rarelink redcap upload-records`` command.

.. warning::
   This command will overwrite existing records with the same record_id in your
   REDCap project. Make sure have unique ``record_id``s or back up your data
   before running this command, e.g. by running 
   `rarelink redcap download-records`.

