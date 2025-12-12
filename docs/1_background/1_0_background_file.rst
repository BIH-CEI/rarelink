.. _1_0:

Background
=============

.. tip:: 
   - **Manuscript:** RareLink was recently published in npj Genomic Medicine: https://www.nature.com/articles/s41525-025-00534-z

RareLink was developed as a response to the widespread challenges in rare 
disease (RD) data management, specifically the lack of interoperability and 
standardization in healthcare information systems. As REDCap is widely used 
in clinical studies and registries for data collection, RareLink was designed
to leverage REDCap's capabilities to facilitate the collection, processing,
and sharing of RD data. The framework ensures that RD data is 
captured, processed, and exported following a predefined common data model
that facilitates downstream analysis using international standards. Furthermore,
RareLink provides a rule-based approach for the design of REDCap instruments 
to extend the RD common data model with additional data elements.

The integration of ontology codes and the connection to the BioPortal Ontology 
Server enables researchers and clinicians to use standardized terminologies, 
ensuring that data can be easily shared and reused across different platforms 
and research networks. By leveraging HL7 FHIR and the GA4GH Phenopacket Schema, 
RareLink supports the creation of interoperable and reusable RD datasets.

In the following we provide an overview of the different components of the
RareLink framework, including the interoperability features, the supported
ontologies, the GA4GH Phenopacket Schema, the HL7 FHIR standard, the RD CDM,
and the REDCap data collection platform.

.. toctree::
   :maxdepth: 4
   :caption: Contents

   1_1_rd_interoperability
   1_2_ontologies
   1_3_ga4gh_phenopacket_schema
   1_4_hl7_fhir
   1_5_rd_cdm
   1_6_redcap


