.. _1_5: 

RD-CDM
=======

.. tip::
   The RD-CDM v2.0.2 has been published in Nature Scientific Data. You can read 
   it here: https://www.nature.com/articles/s41597-025-04558-z.

_________________________________________________________________________________

RD-CDM v2.0.2 Overview
-----------------------

The ontology-based Rare Diseases Common Data Model (RD CDM) v2.0 was developed to address
the complexity and variability inherent in rare diseases, which number over
6,000 and often require unique approaches to research and clinical care. This
model is based on the Common Data Set from the European Rare
Disease Registry Infrastructure (ERDRI-CDS), providing a standardized structure
for data capture and analysis. We expanded on these elements to meet the
needs of international interoperability standards, aligning with both HL7 FHIR
and the GA4GH Phenopacket Schema. The development of this model
involved overcoming challenges such as the lack of standardized terms for
disease characteristics and the need to represent highly variable clinical data
across different rare diseases.

.. figure:: ../_static/res/rd_cdm_v2_0_2.svg

   Depicts version 2.0.2 of our ontology-based rare disease common data model (RD-CDM) based on the European Rare Disease Registry Infrastructure - Common Data Set (ERDRI-CDS), HL7 FHIR base resources v4.0.1 and the GA4GH Phenopacket Schema v2.0. The sections are derived from the ERDRI-CDS, and the section Diagnosis is extended by four subsections. For each section, all data elements and their data types. This data model does not define any cardinalities of relationships between elements or sections.


.. tip:: 
   Further Links: 

   - `RD-CDM Paper <https://www.nature.com/articles/s41597-025-04558-z>`_
   - `RD-CDM GitHub Repository <https://github.com/BIH-CEI/rd-cdm>`_
   - `RD-CDM Documentation <https://rd-cdm.readthedocs.io/en/latest/>`_
   - `RD-CDM Resources and Downloads <https://rd-cdm.readthedocs.io/en/latest/resources/resources_file.html>`_

_________________________________________________________________________________

Key Success Factors of a Rare Disease Common Data Model
-------------------------------------------------------

Developing an RD-CDM also requires balancing between complexity and
usability. A successful model must be comprehensive enough to capture the
nuances of each rare disease, yet simple enough to be adopted across various
healthcare systems. One key difficulty is finding a common denominator for the
unique clinical requirements of diverse rare diseases while maintaining
flexibility for future expansions. Additionally, ensuring that the data can be
seamlessly integrated into existing healthcare systems without exceeding the 
avaliable resources is also essential. Addressing these complexities, the 
RD CDM v2.0 provides a framework that enhances the consistency of rare disease 
data, enabling better comparative analysis across research institutions and 
healthcare settings. While the RD-CDM v2.0.2 is not a balloted version, it can 
serve as a template for future standardization efforts in rare disease research.

Key success factors for the RD-CDM include its ability to support secondary
uses of data, such as transferring data to central registries or enabling
federated analyses. By adhering to international interoperability standards, the
model ensures that data captured locally can be reused in broader contexts,
such as global research initiatives. This not only improves the efficiency of 
rare disease research but also helps preserve the unique aspects of each 
condition. The RD CDM's flexibility allows it to evolve with the growing needs 
of the rare disease community.

.. tip::
   Read `Review of Key Elements in Developing a Common Data Model for Rare Diseases: Identifying Common Success Factors (Graefe ASL, et al. 2024) <https://ebooks.iospress.nl/doi/10.3233/SHTI240672>`_.

_________________________________________________________________________________

Further Reading
---------------
- `European Rare Disease Infrastructure Common Data Set (ERDRI-CDS) <https://www.erdri-cds.eu>`_
- `An ontology-based rare disease common data model harmonising international registries, FHIR, and Phenopackets <https://www.nature.com/articles/s41597-025-04558-z>`_
- `A Common Data Model for Rare Diseases based on the ERDRI-CDS, HL7 FHIR, and the GA4GH Phenopackets Schema v2.0 <https://figshare.com/articles/dataset/_b_Common_Data_Model_for_Rare_Diseases_b_based_on_the_ERDRI-CDS_HL7_FHIR_and_the_GA4GH_Phenopackets_Schema_v2_0_/26509150>`_
- `Review of Key Elements in Developing a Common Data Model for Rare Diseases: Identifying Common Success Factors <https://ebooks.iospress.nl/doi/10.3233/SHTI240672>`_

