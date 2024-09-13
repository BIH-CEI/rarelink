Generate GA4GH Phenopackets
============================

The Phenopacket Mapper allows users to generate validated GA4GH Phenopackets 
from any tabular data. Rarelink specifies the how the data should be formatted 
and coded and sheet should be built within REDCap to generate validated GA4GH
Phenopackets. These specifications were preconfigured into the Phenopacket 
Mapper for seamless generation of GA4GH Phenopackets from REDCap data. 

Further Links Phenopacket Mapper
---------------------------------
- [Phenopacket Mapper Documentation](https://bih-cei.github.io/
phenopacket_mapper/stable/) 
- [Phenopacket Mapper GitHub](https://github.com/BIH-CEI/phenopacket_mapper)


RareLink provides all REDCap sheets that displa data in the Rare Disease
Common Data Model v2.0 (RD CDM) with predefined mappings to generate GA4GH
Phenopackets. These mappings are defined in a configuration file that is
provided with the Phenopacket Mapper module. All data from the RD CDM can be
exported to GA4GH Phenopackets using the Phenopacket Mapper module. 

RD CDM --> RareLink Sheets 
--> predefined Phenopacket pipeline --> GA4GH Phenopackets


For Data extending the 



These specifications were implemented for our RareLink REDCap instruments that
the data capture of the Rare Disease Common Data Model v2.0. 


These mappings are defined in a configuration file that is provided with the Phenopacket Mapper module. 
All data from the RD CDM can be exported to GA4GH Phenopackets using the Phenopacket Mapper module.
For all data extending the RD CDM, we predefined a set of mappings that can be used to generate GA4GH Phenopackets.
These mappings specify how data in REDCap should be coded and formatted to generate GA4GH Phenopackets.



Extensions around RD CDM --> RareLink Sheets with Phenopacket codes --> preconfiguration in Phenopacket Mapper --> GA4GH Phenopackets
- extension based on CEIENR use case



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






