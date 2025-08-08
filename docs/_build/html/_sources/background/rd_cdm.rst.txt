Rare Disease Common Data Model v2.0
===================================

The Rare Diseases Common Data Model (RD CDM) v2.0 was developed to address
the complexity and variability inherent in rare diseases, which number over
6,000 and often require unique approaches to research and clinical care. This
model is based on the Common Data Elements (CDEs) from the European Rare
Disease Registry Infrastructure (ERDRI-CDS), providing a standardized structure
for data capture and analysis. We expanded on these elements to meet the
needs of international interoperability standards, aligning with both HL7 FHIR
and the GA4GH Phenopacket Schema. The development of this model
involved overcoming challenges such as the lack of standardized terms for
disease characteristics and the need to represent highly variable clinical data
across different rare diseases.

Developing an RD CDM also requires balancing between complexity and
usability. A successful model must be comprehensive enough to capture the
nuances of each rare disease, yet simple enough to be adopted across various
healthcare systems. One key difficulty is finding a common denominator for the
unique clinical requirements of diverse rare diseases while maintaining
flexibility for future expansions. Additionally, ensuring that the data can be
seamlessly integrated into existing healthcare systems without exceeding the 
avaliable resources is also essential. Addressing these complexities, the 
RD CDM v2.0 provides a framework that enhances the consistency of rare disease 
data, enabling better comparative analysis across research institutions and 
healthcare settings. While the RD CDM v2.0 is not a balloted version, it can 
serve as a template for future standardization efforts in rare disease research.

Key success factors for the RD CDM include its ability to support secondary
uses of data, such as transferring data to central registries or enabling
federated analyses. By adhering to international interoperability standards, the
model ensures that data captured locally can be reused in broader contexts,
such as global research initiatives. This not only improves the efficiency of 
rare disease research but also helps preserve the unique aspects of each 
condition. The RD CDM's flexibility allows it to evolve with the growing needs 
of the rare disease community.

RareLink integrates this RD CDM v2.0 at its core, utilizing its REDCap sheets,
instruments, and project setup to streamline data management processes. The
native data processing pipelines within RareLink ensure that clinicians and
researchers can generate Phenopackets and FHIR resources without needing
additional coding or mapping. This seamless integration allows for immediate
use of the system, saving time and effort while ensuring that data can be
captured in a standard-compliant format from the start.

By leveraging the RD CDM v2.0, RareLink provides a comprehensive platform for
managing rare disease data. Its integration with FHIR and the GA4GH
Phenopacket Schema allows for the processing and export of rare disease data
into formats suitable for registry use and broader healthcare information
systems. This makes RareLink a critical tool for ensuring that rare disease data
is interoperable, reusable, and can be effectively utilized for research and
clinical care. For disease-specific extensions around the RD CDM v2.0, RareLink
provides a rule-based approach to customize REDCap instruments and
ensure that the model can be adapted to meet the unique needs of different rare
diseases.

.. image:: ../images/rd_cdm_v2.0_overview.png
   :alt: Overview RD CDM v2.0
   :width: 700px
   :height: 500px
   :align: center


Further Reading
---------------
- `European Rare Disease Infrastructure Common Data Set (ERDRI-CDS) <https://www.erdri-cds.eu>`_
- `A Common Data Model for Rare Diseases based on the ERDRI-CDS, HL7 FHIR, and the GA4GH Phenopackets Schema v2.0 <https://figshare.com/articles/dataset/_b_Common_Data_Model_for_Rare_Diseases_b_based_on_the_ERDRI-CDS_HL7_FHIR_and_the_GA4GH_Phenopackets_Schema_v2_0_/26509150>`_
- `Review of Key Elements in Developing a Common Data Model for Rare Diseases: Identifying Common Success Factors <https://ebooks.iospress.nl/doi/10.3233/SHTI240672>`_

