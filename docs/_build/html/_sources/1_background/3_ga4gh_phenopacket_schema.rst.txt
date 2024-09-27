GA4GH Phenopacket Schema
========================


The Phenopacket schema, developed by the Global Alliance for Genomics and Health
(GA4GH), is an open standard designed to facilitate the exchange of detailed 
phenotypic and genomic data. It is particularly useful for capturing rich 
clinical data and complex phenotypes in a structured format, making it ideal 
for rare disease (RD) research. The schema enables the precise description of 
a patient's clinical features, genetic information, diagnoses, and disease 
progression, all of which are critical for understanding rare diseases. 
Phenopackets are widely adopted in bioinformatics pipelines to ensure the 
standardization of data across different institutions and studies, enhancing 
data reusability and interoperability.

.. tip:: 
   Read the GA4GH Phenopacket Schema Paper here:
      `The GA4GH Phenopacket schema defines a computable representation of clinical data <https://www.nature.com/articles/s41587-022-01357-4>`_


Phenopacket Building Blocks
---------------------------

The GA4GH Phenopcaket Schema v2.0:

.. image:: ../images/phenopacket-schema-v2.png
   :alt: GA4GH Phenopacket Schema
   :width: 1000px  
   :height: 300px  
   :align: center


A Phenopacket characterizes an individual or biosample, linking it to detailed 
phenotypic descriptions, genetic information, diagnoses, and treatments, all 
structured as `building blocks <https://phenopacket-schema.readthedocs.io/en/latest/building-blocks.html>`_.
These cover topics such as phenotype, medical actions, measurements, variant, 
and pedigree, enabling a rich representation of data that can easily integrate 
into larger schemas for specific use cases.

Central to the Phenopacket schema is the `PhenotypicFeature <https://phenopacket-schema.readthedocs.io/en/latest/phenotype.html>`_,
which describes various characteristics such as signs, symptoms, and laboratory 
findings using ontology, like the Human Phenotype Ontology (HPO). The schema 
also allows for the documentation of exclusions, severity, frequency, and onset 
of features. Other essential components inclute `Measurement <https://phenopacket-schema.readthedocs.io/en/latest/measurement.html>`_,
for capturing data, `Biosample <https://phenopacket-schema.readthedocs.io/en/latest/biosample.html>`_,
for biological materials, and `MedicalAction <https://phenopacket-schema.readthedocs.io/en/latest/medical-action.html>`_, 
which includes the hierarchical representation of medical interventions. 
The `Treatment <https://phenopacket-schema.readthedocs.io/en/latest/treatment.html>`_
element encompasses a range of therapeutic agents, from medications to advanced 
therapies. Together, these building blocks create a comprehensive framework for 
clinical information.

.. note::
   `Here you find the GA4GH Phenopacket Schema Documentation <https://phenopacket-schema.readthedocs.io/en/latest/index.html>`_



Phenopacket Tools
-----------------

Several tools have been developed around the Phenopacket schema, supporting the 
collection, analysis, and dissemination of RD data. Tools such as the 
Phenopacket validator ensure that data adhere to the schema's strict standards, 
preventing inconsistencies and improving data quality. Additionally, the GA4GH 
Beacon network allows researchers to query datasets to find specific genomic 
variants associated with phenotypic data encoded in Phenopackets. These tools 
have helped to broaden the impact of Phenopackets in RD research by promoting 
data accuracy, accessibility, and reusability across multiple platforms and 
projects.







Further Reading
---------------
- `The GA4GH Phenopacket schema defines a computable representation of clinical data <https://www.nature.com/articles/s41587-022-01357-4>`_
- `GA4GH Phenopackets: A Practical Introduction <https://onlinelibrary.wiley.com/doi/full/10.1002/ggn2.202200016>`_
- `A corpus of GA4GH Phenopackets: case-level phenotyping for genomic diagnostics and discovery <https://www.medrxiv.org/content/10.1101/2024.05.29.24308104v1>`_
- `Phenopacket-tools: Building and validating GA4GH Phenopackets <https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0285433>`_
