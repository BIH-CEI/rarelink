# Project Management
https://github.com/BIH-CEI/RareDIF

### Features

#### 1. Epics (Labels)

- A) Native REDCap (manual) data capture and project set up
- B) Semi-Automated data capture (from tabular data)
- C) Phenopacket Pipeline von RD CDM tabular --> local Phenopackets (with possibility for extension)
- D) REDCap to HL7 FHIR  (local FHIR resources & existing FHIR servers and back)
- E) HL7 FHIR to REDCap (from FHIR Servers to REDCap)

#### 2. User Stories (Milestones)

##### A)
> start developing now
- A1) REDCap Implementation & Installation: most native usage of REDCap
- A2) User Docs: for implementation, installation, and set up in your local REDCap server & project (e.g. Connection with BioPortal)
- A3) User Docs: for manual data capture (e.g. for HGVS validation)
##### B)
> start developing now
- B1) [Mapping Utils (](https://github.com/BIH-CEI/RareDIF/milestone/3)
    - Functions that enable mapping in general
    - copy some from ERKER2Phenopackets
- B2) [Mapper for Tabular Data to RD CDM](https://github.com/BIH-CEI/RareDIF/milestone/4)
    - step through sections of RD CDM
    - link columns in entry data with RD CDM columns
- B3) [GUI for Mapper](https://github.com/BIH-CEI/RareDIF/milestone/13)
    - fetch from API / upload of import CSV template
    - develop GUI for data mapper for existing tabular databases
    - include clear instructions for each section, especially genetics
- [B4) Documentation for Mapper](https://github.com/BIH-CEI/RareDIF/milestone/14)
    - instructions for each sections
    - instructions for usage and installation
    - instructions for linkage of API & API Token
##### C)
> start developing when Epic B is finished
- [C0) Adapt ERKER2Phenopacket Code](https://github.com/BIH-CEI/RareDIF/milestone/15)
-  [C1) Implement phenopackets pipeline](https://github.com/BIH-CEI/RareDIF/milestone/16)
    - Extend pipeline to all RD CDM data elements
- [C2) Create GUI](https://github.com/BIH-CEI/RareDIF/milestone/17)
- [C3) Extendability of RD CDM for Specific Usecases](https://github.com/BIH-CEI/RareDIF/milestone/18)
- [C4) Documentation](https://github.com/BIH-CEI/RareDIF/milestone/19)
######  D)
- generate local HL7 FHIR resources from form
- HL7 FHIR
- Automated export to local HL7 FHIR resources or an HL7 FHIR server using the toFHIR Module

######  E)
- Automated import of HL7 FHIR resources to a local RECap project & database using the CDIS-Module


##### 3. Tasks 

