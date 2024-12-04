.. _4_3:

Generate GA4GH Phenopackets
============================

.. attention::
    This section is still to be implemented in the docuemntation and the RareLink
    command line interface.

The Phenopacket Mapper allows users to generate validated GA4GH Phenopackets 
from any tabular data. Rarelink specifies the how the data should be formatted 
and coded and sheet should be built within REDCap to generate validated GA4GH
Phenopackets. These specifications were preconfigured into the Phenopacket 
Mapper for seamless generation of GA4GH Phenopackets from REDCap data. 

Via the RareLink CLI type:

.. code-block:: bash

    rarelink setup -pipeline Phenopacket
    rarelink pipeline -run Phenopacket

Further Links Phenopacket Mapper
---------------------------------

- `Phenopacket Mapper Documentation <https://bih-cei.github.io/phenopacket_mapper/stable/>`_
- `Phenopacket Mapper GitHub <https://github.com/BIH-CEI/phenopacket_mapper>`_


RareLink Phenopacket Mapper Configuration
_________________________________________

RareLink - RD CDM v2.0
----------------------

RareLink provides all REDCap sheets that displa data in the Rare Disease
Common Data Model v2.0 (RD CDM) with predefined mappings to generate GA4GH
Phenopackets. These mappings are defined in a configuration file that is
provided with the Phenopacket Mapper module. All data from the RD CDM can be
exported to GA4GH Phenopackets using the Phenopacket Mapper module. 

RD CDM v2.0 -> RareLink Sheets -> preconfigured Phenopacket 
--> validated GA4GH Phenopackets


RareLink - Data Extending RD CDM
--------------------------------

For all data extending the RD CDM, we predefined a set of rules that can be used
to develop further REDCap forms. If these rules are followed, the sheet 
variables can be used to map the REDCap data to the GA4GH Phenopackets Schema. 
We provide example sheets that can be used to capture data that extends the RD
CDM to capture specific Phenopacket Building Blocks. 


Extensions around RD CDM --> Rules for REDCap Sheets -> (example sheets to
download and use) -> RareLink preconfiguration in Phenopacket Mapper 
--> validated GA4GH Phenopackets



Definition REDCap variable suffixes for Phenopacket Mapper
__________________________________________________________

The Phenopacket Mapper can prinicapally process any kind of data to generate GA4GH Phenopackets 
if mapped and processed correctly. 
As elaborated in the REDCap section, REDCap variables and choice codes have specific 
limitations and requirements: 

- REDCap variables
    - must be unique
    - must not contain spaces or special characters, i.e. only alphanumeric characters and underscores
    - should not be longer than 26 characters



Disease Block
-------------


PhenotypicFeature Block
------------------------






