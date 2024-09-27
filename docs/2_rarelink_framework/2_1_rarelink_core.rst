RareLink Core
=============

RareLink maximizes the utility of REDCap by providing a comprehensive framework 
designed specifically for rare disease (RD) research and care. At the core of 
RareLink is the Rare Disease Common Data Model (RD CDM), which integrates 
pre-configured REDCap sheets, instruments, and project setups. This framework 
ensures that data capture is both consistent and compliant with international 
standards, such as HL7 FHIR and GA4GH Phenopackets, without the need for 
additional coding or mapping. As a result, RareLink allows researchers and 
clinicians to collect and process rare disease data seamlessly within the REDCap 
environment.

By embedding standardized data collection instruments and native data processing 
pipelines, RareLink addresses one of the primary limitations of REDCap—its lack 
of native variable definitions. With RareLink, data can be captured, processed, 
and exported in interoperable formats suitable for rare disease registries and 
healthcare information systems. The integration of FHIR resources and 
Phenopackets enables rare disease data to be shared across institutions, 
facilitating collaboration and improving the potential for meaningful research 
and clinical advancements in RD care.

RareLink enhances the functionality of REDCap by transforming it into a powerful 
tool for rare disease data management. By leveraging the REDCap API and built-in 
tools, RareLink ensures that the data captured in REDCap can be seamlessly 
integrated into broader research ecosystems, maximizing its utility and 
interoperability for rare disease research and patient care.


RareLink and the RD CDM
------------------------

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


RareLink and HL7 FHIR
_____________________

RareLink incorporates FHIR to enhance its data processing capabilities, enabling
the conversion of clinical and research data into FHIR-compatible formats. This
allows data to be exported for use in registries, uploaded to FHIR servers, or
adopted by other healthcare systems. By supporting FHIR, RareLink ensures
that rare disease data can enrich routine healthcare datasets, helping to bridge
the gap between clinical care and research. Additionally, the ability to process
and export data into FHIR enables RD researchers to leverage existing FHIR
tools, thereby expanding the utility of their data across different applications.

Although FHIR may not cover all the nuanced aspects required for in-depth RD
analysis, it is indispensable for achieving interoperability within healthcare
systems. Its integration in RareLink ensures that data collected from rare
disease patients can be reused effectively across various platforms, thereby
supporting both clinical care and bioinformatic research into rare conditions.


RareLink and the GA4GH Phenopacket Schema
__________________________________________

RareLink integrates the Phenopacket schema to streamline RD data management by 
ensuring that clinical and genomic data from patients are encoded in a 
standardized format. By adopting this schema, RareLink allows for more precise 
and seamless sharing of patient data across different healthcare institutions 
and research projects. This integration helps overcome the challenge of 
fragmented RD data, as Phenopackets offer a universal language for describing 
the clinical characteristics of RD patients. In doing so, RareLink significantly
enhances the bioinformatic output, making it easier to connect RD patient 
registries with broader genomic research databases, improving the potential for
discovering new therapies.