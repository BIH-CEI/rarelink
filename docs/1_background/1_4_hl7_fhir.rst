.. _1_4: 

HL7 FHIR
==========

________

FHIR (Fast Healthcare Interoperability Resources) is an international standard
developed by HL7 for exchanging healthcare information electronically. Initially
designed as a transaction format to facilitate data exchanges between healthcare
systems, FHIR provides a flexible and modular framework. While it is essential
for ensuring interoperability across healthcare information systems, its role as
a transaction format means that it may not always provide the precision needed
for complex rare disease (RD) analysis. However, it remains a critical tool for
enabling the smooth exchange of healthcare data between different platforms
and applications.

.. note:: 
    For our :ref:`1_5` and RareLink we use the `HL7 FHIR v4.0.1 base resources <https://hl7.org/fhir/R4/resourcelist.html>`_ 
    and the `International Patient Summary (IPS) <https://build.fhir.org/ig/HL7/fhir-ips/>`_.

FHIR and Rare Diseases
-----------------------

In the context of rare diseases, FHIR plays a key role in improving data sharing
across institutions and research centers. Due to the scarcity and fragmentation
of RD data, standardized data exchange is crucial. FHIR enables the
standardization of clinical and genomic data, ensuring that RD-specific
information, such as phenotypic traits and genetic variants, can be captured and
shared in a structured manner. Despite its limitations in handling the 
complexity of some RD data, FHIR's widespread adoption ensures that RD data can 
be integrated with other healthcare information systems, making it easier to
collaborate and share insights across various fields.

The `International Patient Summary (IPS) <https://build.fhir.org/ig/HL7/fhir-ips/>`_ 
is a FHIR-based standard that aims to 
provide a concise, standardized summary of a patient's key health information. 
This summary is designed to facilitate seamless healthcare transitions, 
particularly for patients with complex health needs, such as those with rare 
diseases. By standardizing data elements such as medications, allergies, and 
relevant medical history, the IPS enhances communication between international 
healthcare providers. This is especially important for RD patients, as the 
inherent data scarcity requires data exchange and research on an international
level - such as by the `European Reference Networks (ERNs) <https://health.ec.europa.eu/rare-diseases-and-european-reference-networks_en>`_.

FHIR Overview - Clinicians
---------------------------
FHIR (Fast Healthcare Interoperability Resources) facilitates the exchange of 
healthcare information, including clinical, administrative, public health, and 
research data across various settings, such as in-patient and community care. 
It is applicable to both human and veterinary medicine and aims for global 
usability.

Targeted at software developers and organizations creating interoperable 
solutions, FHIR does not prescribe clinical best practices or provide user 
interface and workflow guidance, as these are outside its scope. The 
specification focuses on the technical aspects of exchanging clinical 
information between electronic systems, presenting an overview that prioritizes 
relevant content for the clinical community while allowing for deeper 
exploration of technical details if desired.

.. tip::
    - Read more on `FHIR Overview for Clinicians <hhttps://hl7.org/fhir/R4/overview-dev.html>`_

FHIR Overview - Developers
---------------------------

FHIR (Fast Healthcare Interoperability Resources) is designed to enable 
information exchange to support the provision of healthcare in a wide variety 
of settings. The specification builds on and adapts modern, widely used RESTful 
practices to enable the provision of integrated healthcare across a wide range 
of teams and organizations.

The intended scope of FHIR is broad, covering human and veterinary, clinical 
care, public health, clinical trials, administration and financial aspects. 
The standard is intended for global use and in a wide variety of architectures 
and scenarios.

.. tip:: 
    - Read more on `FHIR Overview for Developers <https://hl7.org/fhir/R4/overview-dev.html>`_

FHIR Overview - Architects
---------------------------

FHIR comprises two main components: Resources and APIs. Resources are 
information models that define the essential data elements, constraints, 
and relationships relevant to healthcare, analogous to physical models in XML 
or JSON. APIs offer well-defined interfaces for application interoperability, 
primarily using RESTful methods. Together, they establish a framework for 
defining healthcare business objects, such as patients and procedures, 
facilitating their computable implementation and sharing through standardized 
interfaces.

Operationally, HL7 governs the standards development process that determines 
the definition and existence of resources. Additionally, FHIR provides 
mechanisms to tailor resources for specific contexts, ensuring adaptability 
to diverse healthcare needs through Profiling Resources.

.. tip::
    - Read more on `FHIR Overview for Architects <https://hl7.org/fhir/R4/overview-arch.html>`_

Further Reading
---------------
- `Why digital medicine depends on interoperability <https://www.nature.com/articles/s41746-019-0158-1>`_
- `HL7 FHIR-based tools and initiatives to support clinical research: a scoping review <https://academic.oup.com/jamia/article-abstract/29/9/1642/6639865>`_
- `HL7 FHIR Overview <https://www.hl7.org/fhir/overview.html>`_
- `FHIR Genomics Implementation Guide <https://build.fhir.org/ig/HL7/genomics-reporting/index.html>`_


