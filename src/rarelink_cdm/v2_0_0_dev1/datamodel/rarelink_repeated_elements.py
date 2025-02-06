# # Auto generated from rarelink_repeated_elements.yaml by pythongen.py version: 0.0.1
# # Generation date: 2024-12-14T23:57:05
# # Schema: rarelink_repeated_elements
# #
# # id: https://github.com/BIH-CEI/RareLink/blob/develop/src/rarelink_cdm_linkml/v2.0.0.dev1/linkml/rarelink_repeated_elements.yaml
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

# from linkml_runtime.linkml_model.types import Date, Integer, String
# from linkml_runtime.utils.metamodelcore import XSDDate

# import pytest

# pytestmark = pytest.mark.skip(reason="Skipping due to uninitialized SNOMED dictionary")


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
# class RepeatedElement(YAMLRoot):
#     """
#     A generic container for repeated elements such as instruments and their instances used to define repeating data
#     structures across the RareLink-CDM.
#     """
#     _inherited_slots: ClassVar[List[str]] = []

#     class_class_uri: ClassVar[URIRef] = RARELINK["RepeatedElement"]
#     class_class_curie: ClassVar[str] = "rarelink:RepeatedElement"
#     class_name: ClassVar[str] = "RepeatedElement"
#     class_model_uri: ClassVar[URIRef] = RARELINK.RepeatedElement

#     redcap_repeat_instrument: Optional[str] = None
#     redcap_repeat_instance: Optional[int] = None
#     patient_status: Optional[Union[dict, "PatientStatus"]] = None

#     def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
#         if self.redcap_repeat_instrument is not None and not isinstance(self.redcap_repeat_instrument, str):
#             self.redcap_repeat_instrument = str(self.redcap_repeat_instrument)

#         if self.redcap_repeat_instance is not None and not isinstance(self.redcap_repeat_instance, int):
#             self.redcap_repeat_instance = int(self.redcap_repeat_instance)

#         if self.patient_status is not None and not isinstance(self.patient_status, PatientStatus):
#             self.patient_status = PatientStatus(**as_dict(self.patient_status))

#         super().__post_init__(**kwargs)


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
# class PatientStatus(YAMLRoot):
#     """
#     The section Patient Status (3) of the RareLink CDM.
#     """
#     _inherited_slots: ClassVar[List[str]] = []

#     class_class_uri: ClassVar[URIRef] = RARELINK["PatientStatus"]
#     class_class_curie: ClassVar[str] = "rarelink:PatientStatus"
#     class_name: ClassVar[str] = "PatientStatus"
#     class_model_uri: ClassVar[URIRef] = RARELINK.PatientStatus

#     rarelink_3_patient_status_complete: str = None
#     patient_status_date: Optional[Union[str, XSDDate]] = None
#     snomedct_278844005: Optional[Union[str, "ClinicalVitalStatus"]] = None
#     snomedct_398299004: Optional[Union[str, UnionDateString]] = None
#     snomedct_184305005: Optional[str] = None
#     snomedct_105727008: Optional[Union[str, "AgeCategory"]] = None
#     snomedct_412726003: Optional[str] = None
#     snomedct_723663001: Optional[Union[str, "YesNo"]] = None

#     def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
#         if self._is_empty(self.rarelink_3_patient_status_complete):
#             self.MissingRequiredField("rarelink_3_patient_status_complete")
#         if not isinstance(self.rarelink_3_patient_status_complete, str):
#             self.rarelink_3_patient_status_complete = str(self.rarelink_3_patient_status_complete)

#         if self.patient_status_date is not None and not isinstance(self.patient_status_date, XSDDate):
#             self.patient_status_date = XSDDate(self.patient_status_date)

#         if self.snomedct_278844005 is not None and not isinstance(self.snomedct_278844005, ClinicalVitalStatus):
#             self.snomedct_278844005 = ClinicalVitalStatus(self.snomedct_278844005)

#         if self.snomedct_398299004 is not None and not isinstance(self.snomedct_398299004, UnionDateString):
#             self.snomedct_398299004 = UnionDateString(self.snomedct_398299004)

#         if self.snomedct_184305005 is not None and not isinstance(self.snomedct_184305005, str):
#             self.snomedct_184305005 = str(self.snomedct_184305005)

#         if self.snomedct_105727008 is not None and not isinstance(self.snomedct_105727008, AgeCategory):
#             self.snomedct_105727008 = AgeCategory(self.snomedct_105727008)

#         if self.snomedct_412726003 is not None and not isinstance(self.snomedct_412726003, str):
#             self.snomedct_412726003 = str(self.snomedct_412726003)

#         if self.snomedct_723663001 is not None and not isinstance(self.snomedct_723663001, YesNo):
#             self.snomedct_723663001 = YesNo(self.snomedct_723663001)

#         super().__post_init__(**kwargs)


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

# class ClinicalVitalStatus(EnumDefinitionImpl):

#     snomedct_438949009 = PermissibleValue(
#         text="snomedct_438949009",
#         description="Alive",
#         meaning=SNOMED["438949009"])
#     snomedct_419099009 = PermissibleValue(
#         text="snomedct_419099009",
#         description="Dead",
#         meaning=SNOMED["419099009"])
#     snomedct_399307001 = PermissibleValue(
#         text="snomedct_399307001",
#         description="Unknown - Lost in follow-up",
#         meaning=SNOMED["399307001"])
#     snomedct_185924006 = PermissibleValue(
#         text="snomedct_185924006",
#         description="Unknown - Opted-out",
#         meaning=SNOMED["185924006"])
#     snomedct_261665006 = PermissibleValue(
#         text="snomedct_261665006",
#         description="Unknown - Other Reason",
#         meaning=SNOMED["261665006"])

#     _defn = EnumDefinition(
#         name="ClinicalVitalStatus",
#     )

# class AgeCategory(EnumDefinitionImpl):

#     snomedct_3658006 = PermissibleValue(
#         text="snomedct_3658006",
#         description="Infancy",
#         meaning=SNOMED["3658006"])
#     snomedct_713153009 = PermissibleValue(
#         text="snomedct_713153009",
#         description="Toddler",
#         meaning=SNOMED["713153009"])
#     snomedct_255398004 = PermissibleValue(
#         text="snomedct_255398004",
#         description="Childhood",
#         meaning=SNOMED["255398004"])
#     snomedct_263659003 = PermissibleValue(
#         text="snomedct_263659003",
#         description="Adolescence",
#         meaning=SNOMED["263659003"])
#     snomedct_41847000 = PermissibleValue(
#         text="snomedct_41847000",
#         description="Adulthood",
#         meaning=SNOMED["41847000"])
#     snomedct_303112003 = PermissibleValue(
#         text="snomedct_303112003",
#         description="Fetal period",
#         meaning=SNOMED["303112003"])
#     snomedct_419099009 = PermissibleValue(
#         text="snomedct_419099009",
#         description="Dead",
#         meaning=SNOMED["419099009"])
#     snomedct_261665006 = PermissibleValue(
#         text="snomedct_261665006",
#         description="Unknown",
#         meaning=SNOMED["261665006"])

#     _defn = EnumDefinition(
#         name="AgeCategory",
#     )

# class YesNo(EnumDefinitionImpl):

#     snomedct_373066001 = PermissibleValue(
#         text="snomedct_373066001",
#         description="True",
#         meaning=SNOMED["373066001"])
#     snomedct_373067005 = PermissibleValue(
#         text="snomedct_373067005",
#         description="False",
#         meaning=SNOMED["373067005"])

#     _defn = EnumDefinition(
#         name="YesNo",
#     )

# # Slots
# class slots:
#     pass

# slots.patient_status = Slot(uri=RARELINK.patient_status, name="patient_status", curie=RARELINK.curie('patient_status'),
#                    model_uri=RARELINK.patient_status, domain=None, range=Optional[Union[dict, PatientStatus]])

# slots.redcap_repeat_instrument = Slot(uri=RARELINK.redcap_repeat_instrument, name="redcap_repeat_instrument", curie=RARELINK.curie('redcap_repeat_instrument'),
#                    model_uri=RARELINK.redcap_repeat_instrument, domain=None, range=Optional[str])

# slots.redcap_repeat_instance = Slot(uri=RARELINK.redcap_repeat_instance, name="redcap_repeat_instance", curie=RARELINK.curie('redcap_repeat_instance'),
#                    model_uri=RARELINK.redcap_repeat_instance, domain=None, range=Optional[int])

# slots.patient_status_date = Slot(uri=RARELINK.patient_status_date, name="patient_status_date", curie=RARELINK.curie('patient_status_date'),
#                    model_uri=RARELINK.patient_status_date, domain=None, range=Optional[Union[str, XSDDate]])

# slots.snomedct_278844005 = Slot(uri=RARELINK.snomedct_278844005, name="snomedct_278844005", curie=RARELINK.curie('snomedct_278844005'),
#                    model_uri=RARELINK.snomedct_278844005, domain=None, range=Optional[Union[str, "ClinicalVitalStatus"]])

# slots.snomedct_398299004 = Slot(uri=RARELINK.snomedct_398299004, name="snomedct_398299004", curie=RARELINK.curie('snomedct_398299004'),
#                    model_uri=RARELINK.snomedct_398299004, domain=None, range=Optional[Union[str, UnionDateString]])

# slots.snomedct_184305005 = Slot(uri=RARELINK.snomedct_184305005, name="snomedct_184305005", curie=RARELINK.curie('snomedct_184305005'),
#                    model_uri=RARELINK.snomedct_184305005, domain=None, range=Optional[str])

# slots.snomedct_105727008 = Slot(uri=RARELINK.snomedct_105727008, name="snomedct_105727008", curie=RARELINK.curie('snomedct_105727008'),
#                    model_uri=RARELINK.snomedct_105727008, domain=None, range=Optional[Union[str, "AgeCategory"]])

# slots.snomedct_412726003 = Slot(uri=RARELINK.snomedct_412726003, name="snomedct_412726003", curie=RARELINK.curie('snomedct_412726003'),
#                    model_uri=RARELINK.snomedct_412726003, domain=None, range=Optional[str])

# slots.snomedct_723663001 = Slot(uri=RARELINK.snomedct_723663001, name="snomedct_723663001", curie=RARELINK.curie('snomedct_723663001'),
#                    model_uri=RARELINK.snomedct_723663001, domain=None, range=Optional[Union[str, "YesNo"]])

# slots.rarelink_3_patient_status_complete = Slot(uri=RARELINK.rarelink_3_patient_status_complete, name="rarelink_3_patient_status_complete", curie=RARELINK.curie('rarelink_3_patient_status_complete'),
#                    model_uri=RARELINK.rarelink_3_patient_status_complete, domain=None, range=str)

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
