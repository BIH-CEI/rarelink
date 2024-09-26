Ontologies
===========

RareLink uses a variety of ontologies and terminologies to standardise the 
representation of data and facilitate interoperability between different data 
sources. These ontologies and terminologies are used to describe the phenotypic 
and genotypic features of rare diseases (RDs) and their associated genes, as 
well as the relationships between them. The use of standardised vocabularies 
ensures that data can be easily integrated and queried across different 
databases and platforms.

- **Terminology**:
    refers to a collection of preferred or officially recognized 
    terms within a specific domain. In the medical field, one of the most 
    significant terminologies for information retrieval is the Medical Subject 
    Headings (MeSH), which serves as a framework for indexing and searching 
    literature in Medline.

- **Ontologies**:
    ...on the other hand, go beyond mere vocabulary. They establish and define 
    relationships between concepts, enabling computational reasoning and 
    inference. 

.. tip::
    For more detail please read: `Classification, Ontology, and 
    Precision Medicine (Haendel MA et al., 2018) <https://pubmed.ncbi.nlm.nih.gov/30304648/>`_


Ontologies used in RareLink
----------------------------

The following codesystems are used in the RareLink Core Framework:

.. fields: Ontologies Used in RareLink
:`ICD-10 & ICD-11 <https://www.who.int/standards/classifications/classification-of-diseases>`_: 
    The **International Statistical Classification of Diseases** is used for 
    documenting morbidity in healthcare systems, encoding mortality statistics, 
    and billing purposes. The **ICD-11** encodes rare diseases more 
    comprehensively.

:`ORDO <https://www.orpha.net/consor/cgi-bin/index.php>`_: 
    The **Orphanet Rare Disease Ontology** is an open-access ontology for rare 
    diseases enabling queries of rare disorders and capturing relationships 
    between diseases.

:`MONDO <https://mondo.monarchinitiative.org/>`_: 
    The **Monarch Initiative Disease Ontology** aims to harmonize disease 
    definitions across the world. It is a semi-automatically constructed 
    ontology merging multiple disease resources.

:`OMIM <https://omim.org/>`_: 
    **Online Mendelian Inheritance in Man** is an authoritative catalogue 
    focusing on genetic variation and phenotypic expressions. While **OMIM_g** 
    codes refer to specific genes, **OMIM_p** codes refer to phenotypes or 
    clinical manifestations associated with genetic disorders.

:`SNOMED CT <https://www.snomed.org/>`_: 
    The **Systematized Nomenclature of Medicine Clinical Terms** is a 
    comprehensive clinical health terminology providing codes, terms, and 
    definitions used in documentation.

:`LOINC <https://loinc.org/>`_: 
    **Logical Observation Identifiers Names and Codes** is widely used 
    terminology for clinical observations and laboratory identifiers.

:`UO <http://purl.obolibrary.org/obo/uo.owl>`_: 
    The **Units of Measurement Ontology** is an ontology for units of 
    measurement used in scientific data.

:`NCBITaxon <https://www.ncbi.nlm.nih.gov/taxonomy>`_: 
    The **NCBI Taxonomy** is a hierarchical classification of living organisms.

:`HGNC <https://www.genenames.org/>`_: 
    The **Human Genome Organisation - Gene Nomenclature Committee** approves 
    unique symbols and names for human loci.

:`HGVS <https://varnomen.hgvs.org/>`_: 
    The **Human Genome Variation Society** provides guidelines for cataloguing 
    variations in DNA, RNA, and protein sequences.

:`NCIT <https://ncithesaurus.org/>`_: 
    The **National Cancer Institute Thesaurus** is a reference terminology for 
    cancer and biomedical research.

:`GENO <http://www.genoontology.org/>`_: 
    The **Genotype Ontology** is an ontology for describing genetic variation 
    and related concepts.

:`SO <http://www.sequenceontology.org/>`_: 
    The **Sequence Ontology** provides standardized vocabulary for genomic 
    annotation components, enhancing sharing and analysis of genomic information.


.. note:: The versions used by the RareLink Core Framework can be found here: 
    `RareLink Ontologies <

Further Reading
---------------
- `The human phenotype ontology in 2021 <https://academic.oup.com/nar/article/52/D1/D1333/7416384?login=false>`_
- `The Sequence Ontology: a tool for the unification of genome annotations <https://doi.org/10.1186/gb-2005-6-5-r44>`_
- `Rare diseases in ICD11: making rare diseases visible in health information systems through appropriate coding <https://doi.org/10.1186/s13023-015-0251-8>`_
- `Mondo: Unifying diseases for the world, by the world <https://www.medrxiv.org/content/10.1101/2022.04.13.22273750v3>`_
- `Ordo: an ontology connecting rare disease, epidemiology and genetic data <https://www.researchgate.net/publication/287218703_Ordo_an_ontology_connecting_rare_disease_epidemiology_and_genetic_data>`_
- `The use of SNOMED CT, 2013-2020: a literature review <https://doi.org/10.1093/jamia/ocab140>`_
- `A 20-year evaluation of LOINC in the United States' largest integrated health system <https://doi.org/10.5858/arpa.2019-0045-OA>`_
- `Genenames.org: the HGNC resources in 2023 <https://doi.org/10.1093/nar/gkac1102>`_
- `HGVS recommendations for the description of sequence variants: 2016 update <https://doi.org/10.1002/humu.22981>`_
- `OMIM.org: Online Mendelian Inheritance in Man (OMIM®), an online catalog of human genes and genetic disorders <https://doi.org/10.1093/nar/gku1205>`_
