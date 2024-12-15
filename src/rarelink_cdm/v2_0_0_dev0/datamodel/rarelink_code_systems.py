# # Auto generated from rarelink_code_systems.yaml by pythongen.py version: 0.0.1
# # Generation date: 2024-12-14T23:56:16
# # Schema: code_systems_data
# #
# # id: https://github.com/BIH-CEI/RareLink/code_systems_data
# # description:
# # license: https://creativecommons.org/publicdomain/zero/1.0/

# import dataclasses
# import re
# from dataclasses import dataclass
# from datetime import (
#     date,
#     datetime,
#     time
# )
# from typing import (
#     Any,
#     ClassVar,
#     Dict,
#     List,
#     Optional,
#     Union
# )

# from jsonasobj2 import (
#     JsonObj,
#     as_dict
# )
# from linkml_runtime.linkml_model.meta import (
#     EnumDefinition,
#     PermissibleValue,
#     PvFormulaOptions
# )
# from linkml_runtime.utils.curienamespace import CurieNamespace
# from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
# from linkml_runtime.utils.enumerations import EnumDefinitionImpl
# from linkml_runtime.utils.formatutils import (
#     camelcase,
#     sfx,
#     underscore
# )
# from linkml_runtime.utils.metamodelcore import (
#     bnode,
#     empty_dict,
#     empty_list
# )
# from linkml_runtime.utils.slot import Slot
# from linkml_runtime.utils.yamlutils import (
#     YAMLRoot,
#     extended_float,
#     extended_int,
#     extended_str
# )
# from rdflib import (
#     Namespace,
#     URIRef
# )

# from linkml_runtime.linkml_model.types import String

# metamodel_version = "1.7.0"
# version = None

# # Overwrite dataclasses _init_fn to add **kwargs in __init__
# dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# # Namespaces
# LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
# RARELINK = CurieNamespace('rarelink', 'https://github.com/BIH-CEI/rarelink/')
# XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
# DEFAULT_ = RARELINK


# # Types
# class UnionDateString(String):
#     """ A field that allows both dates and empty strings. """
#     type_class_uri = XSD["string"]
#     type_class_curie = "xsd:string"
#     type_name = "union_date_string"
#     type_model_uri = RARELINK.UnionDateString


# # Class references



# @dataclass(repr=False)
# class CodeSystemsContainer(YAMLRoot):
#     """
#     A container class for all code systems used in RareLink.
#     """
#     _inherited_slots: ClassVar[List[str]] = []

#     class_class_uri: ClassVar[URIRef] = RARELINK["CodeSystemsContainer"]
#     class_class_curie: ClassVar[str] = "rarelink:CodeSystemsContainer"
#     class_name: ClassVar[str] = "CodeSystemsContainer"
#     class_model_uri: ClassVar[URIRef] = RARELINK.CodeSystemsContainer

#     ncbi_taxon: Union[str, "NCBITaxon"] = None
#     snomed: Union[str, "SNOMED"] = None
#     mondo: Union[str, "MONDO"] = None
#     hpo: Union[str, "HPO"] = None
#     loinc: Union[str, "LOINC"] = None
#     omim: Union[str, "OMIM"] = None
#     orpha: Union[str, "ORPHA"] = None
#     ncit: Union[str, "NCIT"] = None
#     uo: Union[str, "UO"] = None
#     hgnc: Union[str, "HGNC"] = None
#     hgvs: Union[str, "HGVS"] = None
#     ga4gh: Union[str, "GA4GH"] = None
#     hl7fhir: Union[str, "HL7FHIR"] = None
#     icd11: Union[str, "ICD11"] = None
#     icd10cm: Union[str, "ICD10CM"] = None
#     icd10gm: Union[str, "ICD10GM"] = None
#     so: Union[str, "SO"] = None
#     geno: Union[str, "GENO"] = None
#     icd9: Union[str, "ICD9"] = None
#     iso3166: Union[str, "ISO3166"] = None
#     icf: Union[str, "ICF"] = None

# @dataclass(repr=False)
# class CodeSystem(YAMLRoot):
#     """
#     A class that represents a CodeSystem, including metadata such as name, prefix, URL, version, and synonyms. This is
#     reusable across schemas that involve code system definitions.
#     """
#     _inherited_slots: ClassVar[List[str]] = []

#     class_class_uri: ClassVar[URIRef] = RARELINK["CodeSystem"]
#     class_class_curie: ClassVar[str] = "rarelink:CodeSystem"
#     class_name: ClassVar[str] = "CodeSystem"
#     class_model_uri: ClassVar[URIRef] = RARELINK.CodeSystem

#     name: str = None
#     prefix: str = None
#     version: str = None
#     url: Optional[str] = None
#     iri_prefix: Optional[str] = None
#     synonyms: Optional[Union[str, List[str]]] = empty_list()

#     def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
#         if self._is_empty(self.name):
#             self.MissingRequiredField("name")
#         if not isinstance(self.name, str):
#             self.name = str(self.name)

#         if self._is_empty(self.prefix):
#             self.MissingRequiredField("prefix")
#         if not isinstance(self.prefix, str):
#             self.prefix = str(self.prefix)

#         if self._is_empty(self.version):
#             self.MissingRequiredField("version")
#         if not isinstance(self.version, str):
#             self.version = str(self.version)

#         if self.url is not None and not isinstance(self.url, str):
#             self.url = str(self.url)

#         if self.iri_prefix is not None and not isinstance(self.iri_prefix, str):
#             self.iri_prefix = str(self.iri_prefix)

#         if not isinstance(self.synonyms, list):
#             self.synonyms = [self.synonyms] if self.synonyms is not None else []
#         self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

#         super().__post_init__(**kwargs)


# # Enumerations
# class NCBITaxon(EnumDefinitionImpl):
#     """
#     NCBI organismal classification
#     """
#     _defn = EnumDefinition(
#         name="NCBITaxon",
#         description="NCBI organismal classification",
#         code_set_version="2024-07-03",
#     )

# class SNOMED(EnumDefinitionImpl):
#     """
#     SNOMED CT
#     """
#     _defn = EnumDefinition(
#         name="SNOMED",
#         description="SNOMED CT",
#         code_set_version="2024-09-01",
#     )

# class MONDO(EnumDefinitionImpl):
#     """
#     Monarch Disease Ontology
#     """
#     _defn = EnumDefinition(
#         name="MONDO",
#         description="Monarch Disease Ontology",
#         code_set_version="2024-09-03",
#     )

# class HPO(EnumDefinitionImpl):
#     """
#     Human Phenotype Ontology
#     """
#     _defn = EnumDefinition(
#         name="HPO",
#         description="Human Phenotype Ontology",
#         code_set_version="2024-08-13",
#     )

# class LOINC(EnumDefinitionImpl):
#     """
#     Logical Observation Identifiers Names and Codes
#     """
#     _defn = EnumDefinition(
#         name="LOINC",
#         description="Logical Observation Identifiers Names and Codes",
#         code_set_version="2.78",
#     )

# class OMIM(EnumDefinitionImpl):
#     """
#     Online Mendelian Inheritance
#     """
#     _defn = EnumDefinition(
#         name="OMIM",
#         description="Online Mendelian Inheritance",
#         code_set_version="2024-09-12",
#     )

# class ORPHA(EnumDefinitionImpl):
#     """
#     Orphanet Rare Disease Ontology
#     """
#     _defn = EnumDefinition(
#         name="ORPHA",
#         description="Orphanet Rare Disease Ontology",
#         code_set_version="2024-09-12",
#     )

# class NCIT(EnumDefinitionImpl):
#     """
#     NCI Thesaurus OBO Edition
#     """
#     _defn = EnumDefinition(
#         name="NCIT",
#         description="NCI Thesaurus OBO Edition",
#         code_set_version="24.04e",
#     )

# class UO(EnumDefinitionImpl):
#     """
#     Units of Measurement Ontology
#     """
#     _defn = EnumDefinition(
#         name="UO",
#         description="Units of Measurement Ontology",
#         code_set_version="2024-09-12",
#     )

# class HGNC(EnumDefinitionImpl):
#     """
#     HUGO Gene Nomenclature Committee
#     """
#     _defn = EnumDefinition(
#         name="HGNC",
#         description="HUGO Gene Nomenclature Committee",
#         code_set_version="2024-08-23",
#     )

# class HGVS(EnumDefinitionImpl):
#     """
#     Human Genome Variation Society
#     """
#     _defn = EnumDefinition(
#         name="HGVS",
#         description="Human Genome Variation Society",
#         code_set_version="21.0.0",
#     )

# class GA4GH(EnumDefinitionImpl):
#     """
#     Global Alliance for Genomics and Health
#     """
#     _defn = EnumDefinition(
#         name="GA4GH",
#         description="Global Alliance for Genomics and Health",
#         code_set_version="v2.0",
#     )

# class HL7FHIR(EnumDefinitionImpl):
#     """
#     Health Level 7 Fast Healthcare Interoperability Resources
#     """
#     _defn = EnumDefinition(
#         name="HL7FHIR",
#         description="Health Level 7 Fast Healthcare Interoperability Resources",
#         code_set_version="v4.0.1",
#     )

# class ICD11(EnumDefinitionImpl):
#     """
#     International Classification of Diseases, Eleventh Revision
#     """
#     _defn = EnumDefinition(
#         name="ICD11",
#         description="International Classification of Diseases, Eleventh Revision",
#         code_set_version="2024-09-01",
#     )

# class ICD10CM(EnumDefinitionImpl):
#     """
#     International Classification of Diseases, Tenth Revision, Clinical Modification
#     """
#     _defn = EnumDefinition(
#         name="ICD10CM",
#         description="International Classification of Diseases, Tenth Revision, Clinical Modification",
#         code_set_version="2024-09-01",
#     )

# class ICD10GM(EnumDefinitionImpl):
#     """
#     International Classification of Diseases, Tenth Revision, German Modification
#     """
#     _defn = EnumDefinition(
#         name="ICD10GM",
#         description="International Classification of Diseases, Tenth Revision, German Modification",
#         code_set_version="2024-09-01",
#     )

# class SO(EnumDefinitionImpl):
#     """
#     Sequence types and features ontology
#     """
#     _defn = EnumDefinition(
#         name="SO",
#         description="Sequence types and features ontology",
#         code_set_version="2.6",
#     )

# class GENO(EnumDefinitionImpl):
#     """
#     GENO - The Genotype Ontology
#     """
#     _defn = EnumDefinition(
#         name="GENO",
#         description="GENO - The Genotype Ontology",
#         code_set_version="2023-10-08",
#     )

# class ICD9(EnumDefinitionImpl):
#     """
#     International Classification of Diseases, Ninth Revision
#     """
#     _defn = EnumDefinition(
#         name="ICD9",
#         description="International Classification of Diseases, Ninth Revision",
#         code_set_version="2024-09-01",
#     )

# class ISO3166(EnumDefinitionImpl):
#     """
#     ISO 3166-1:2020(en) alpha-2 and alpha-3 country codes
#     """
#     _defn = EnumDefinition(
#         name="ISO3166",
#         description="ISO 3166-1:2020(en) alpha-2 and alpha-3 country codes",
#         code_set_version="2020(en)",
#     )

# class ICF(EnumDefinitionImpl):
#     """
#     International Classification of Functioning, Disability and Health
#     """
#     _defn = EnumDefinition(
#         name="ICF",
#         description="International Classification of Functioning, Disability and Health",
#         code_set_version="1.0.2",
#     )

# # Slots
# class slots:
#     pass

# slots.name = Slot(uri=RARELINK.name, name="name", curie=RARELINK.curie('name'),
#                    model_uri=RARELINK.name, domain=None, range=str)

# slots.prefix = Slot(uri=RARELINK.prefix, name="prefix", curie=RARELINK.curie('prefix'),
#                    model_uri=RARELINK.prefix, domain=None, range=str)

# slots.url = Slot(uri=RARELINK.url, name="url", curie=RARELINK.curie('url'),
#                    model_uri=RARELINK.url, domain=None, range=Optional[str])

# slots.version = Slot(uri=RARELINK.version, name="version", curie=RARELINK.curie('version'),
#                    model_uri=RARELINK.version, domain=None, range=str)

# slots.iri_prefix = Slot(uri=RARELINK.iri_prefix, name="iri_prefix", curie=RARELINK.curie('iri_prefix'),
#                    model_uri=RARELINK.iri_prefix, domain=None, range=Optional[str])

# slots.synonyms = Slot(uri=RARELINK.synonyms, name="synonyms", curie=RARELINK.curie('synonyms'),
#                    model_uri=RARELINK.synonyms, domain=None, range=Optional[Union[str, List[str]]])

# slots.codeSystemsContainer__ncbi_taxon = Slot(uri=RARELINK.ncbi_taxon, name="codeSystemsContainer__ncbi_taxon", curie=RARELINK.curie('ncbi_taxon'),
#                    model_uri=RARELINK.codeSystemsContainer__ncbi_taxon, domain=None, range=Union[str, "NCBITaxon"])

# slots.codeSystemsContainer__snomed = Slot(uri=RARELINK.snomed, name="codeSystemsContainer__snomed", curie=RARELINK.curie('snomed'),
#                    model_uri=RARELINK.codeSystemsContainer__snomed, domain=None, range=Union[str, "SNOMED"])

# slots.codeSystemsContainer__mondo = Slot(uri=RARELINK.mondo, name="codeSystemsContainer__mondo", curie=RARELINK.curie('mondo'),
#                    model_uri=RARELINK.codeSystemsContainer__mondo, domain=None, range=Union[str, "MONDO"])

# slots.codeSystemsContainer__hpo = Slot(uri=RARELINK.hpo, name="codeSystemsContainer__hpo", curie=RARELINK.curie('hpo'),
#                    model_uri=RARELINK.codeSystemsContainer__hpo, domain=None, range=Union[str, "HPO"])

# slots.codeSystemsContainer__loinc = Slot(uri=RARELINK.loinc, name="codeSystemsContainer__loinc", curie=RARELINK.curie('loinc'),
#                    model_uri=RARELINK.codeSystemsContainer__loinc, domain=None, range=Union[str, "LOINC"])

# slots.codeSystemsContainer__omim = Slot(uri=RARELINK.omim, name="codeSystemsContainer__omim", curie=RARELINK.curie('omim'),
#                    model_uri=RARELINK.codeSystemsContainer__omim, domain=None, range=Union[str, "OMIM"])

# slots.codeSystemsContainer__orpha = Slot(uri=RARELINK.orpha, name="codeSystemsContainer__orpha", curie=RARELINK.curie('orpha'),
#                    model_uri=RARELINK.codeSystemsContainer__orpha, domain=None, range=Union[str, "ORPHA"])

# slots.codeSystemsContainer__ncit = Slot(uri=RARELINK.ncit, name="codeSystemsContainer__ncit", curie=RARELINK.curie('ncit'),
#                    model_uri=RARELINK.codeSystemsContainer__ncit, domain=None, range=Union[str, "NCIT"])

# slots.codeSystemsContainer__uo = Slot(uri=RARELINK.uo, name="codeSystemsContainer__uo", curie=RARELINK.curie('uo'),
#                    model_uri=RARELINK.codeSystemsContainer__uo, domain=None, range=Union[str, "UO"])

# slots.codeSystemsContainer__hgnc = Slot(uri=RARELINK.hgnc, name="codeSystemsContainer__hgnc", curie=RARELINK.curie('hgnc'),
#                    model_uri=RARELINK.codeSystemsContainer__hgnc, domain=None, range=Union[str, "HGNC"])

# slots.codeSystemsContainer__hgvs = Slot(uri=RARELINK.hgvs, name="codeSystemsContainer__hgvs", curie=RARELINK.curie('hgvs'),
#                    model_uri=RARELINK.codeSystemsContainer__hgvs, domain=None, range=Union[str, "HGVS"])

# slots.codeSystemsContainer__ga4gh = Slot(uri=RARELINK.ga4gh, name="codeSystemsContainer__ga4gh", curie=RARELINK.curie('ga4gh'),
#                    model_uri=RARELINK.codeSystemsContainer__ga4gh, domain=None, range=Union[str, "GA4GH"])

# slots.codeSystemsContainer__hl7fhir = Slot(uri=RARELINK.hl7fhir, name="codeSystemsContainer__hl7fhir", curie=RARELINK.curie('hl7fhir'),
#                    model_uri=RARELINK.codeSystemsContainer__hl7fhir, domain=None, range=Union[str, "HL7FHIR"])

# slots.codeSystemsContainer__icd11 = Slot(uri=RARELINK.icd11, name="codeSystemsContainer__icd11", curie=RARELINK.curie('icd11'),
#                    model_uri=RARELINK.codeSystemsContainer__icd11, domain=None, range=Union[str, "ICD11"])

# slots.codeSystemsContainer__icd10cm = Slot(uri=RARELINK.icd10cm, name="codeSystemsContainer__icd10cm", curie=RARELINK.curie('icd10cm'),
#                    model_uri=RARELINK.codeSystemsContainer__icd10cm, domain=None, range=Union[str, "ICD10CM"])

# slots.codeSystemsContainer__icd10gm = Slot(uri=RARELINK.icd10gm, name="codeSystemsContainer__icd10gm", curie=RARELINK.curie('icd10gm'),
#                    model_uri=RARELINK.codeSystemsContainer__icd10gm, domain=None, range=Union[str, "ICD10GM"])

# slots.codeSystemsContainer__so = Slot(uri=RARELINK.so, name="codeSystemsContainer__so", curie=RARELINK.curie('so'),
#                    model_uri=RARELINK.codeSystemsContainer__so, domain=None, range=Union[str, "SO"])

# slots.codeSystemsContainer__geno = Slot(uri=RARELINK.geno, name="codeSystemsContainer__geno", curie=RARELINK.curie('geno'),
#                    model_uri=RARELINK.codeSystemsContainer__geno, domain=None, range=Union[str, "GENO"])

# slots.codeSystemsContainer__icd9 = Slot(uri=RARELINK.icd9, name="codeSystemsContainer__icd9", curie=RARELINK.curie('icd9'),
#                    model_uri=RARELINK.codeSystemsContainer__icd9, domain=None, range=Union[str, "ICD9"])

# slots.codeSystemsContainer__iso3166 = Slot(uri=RARELINK.iso3166, name="codeSystemsContainer__iso3166", curie=RARELINK.curie('iso3166'),
#                    model_uri=RARELINK.codeSystemsContainer__iso3166, domain=None, range=Union[str, "ISO3166"])

# slots.codeSystemsContainer__icf = Slot(uri=RARELINK.icf, name="codeSystemsContainer__icf", curie=RARELINK.curie('icf'),
#                    model_uri=RARELINK.codeSystemsContainer__icf, domain=None, range=Union[str, "ICF"])
