# Auto generated from rarelink_cdm.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-12-15T02:10:01
# Schema: rarelink_cdm
#
# id: https://github.com/BIH-CEI/RareLink/rarelink_cdm.yaml
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Date, Double, Integer, String
from linkml_runtime.utils.metamodelcore import XSDDate

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RARELINK = CurieNamespace('rarelink', 'https://github.com/BIH-CEI/rarelink/')
RARELINK_CDM = CurieNamespace('rarelink_cdm', 'https://github.com/BIH-CEI/RareLink/rarelink_cdm/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = RARELINK_CDM


# Types
class UnionDateString(String):
    """ A field that allows both dates and empty strings. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "union_date_string"
    type_model_uri = RARELINK_CDM.UnionDateString


# Class references
class RecordRecordId(extended_str):
    pass


class FormalCriteriaSnomed422549004(extended_str):
    pass


@dataclass(repr=False)
class Record(YAMLRoot):
    """
    Base class for all records, containing nested data for formal criteria, personal information, patient status, and
    other sections. The record ID uniquely identifies a record.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RARELINK_CDM["Record"]
    class_class_curie: ClassVar[str] = "rarelink_cdm:Record"
    class_name: ClassVar[str] = "Record"
    class_model_uri: ClassVar[URIRef] = RARELINK_CDM.Record

    record_id: Union[str, RecordRecordId] = None
    formal_criteria: Optional[Union[dict, "FormalCriteria"]] = None
    personal_information: Optional[Union[dict, "PersonalInformation"]] = None
    repeated_elements: Optional[Union[Union[dict, "RepeatedElement"], List[Union[dict, "RepeatedElement"]]]] = empty_list()
    consent: Optional[Union[dict, "Consent"]] = None
    disability: Optional[Union[dict, "Disability"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.record_id):
            self.MissingRequiredField("record_id")
        if not isinstance(self.record_id, RecordRecordId):
            self.record_id = RecordRecordId(self.record_id)

        if self.formal_criteria is not None and not isinstance(self.formal_criteria, FormalCriteria):
            self.formal_criteria = FormalCriteria(**as_dict(self.formal_criteria))

        if self.personal_information is not None and not isinstance(self.personal_information, PersonalInformation):
            self.personal_information = PersonalInformation(**as_dict(self.personal_information))

        if not isinstance(self.repeated_elements, list):
            self.repeated_elements = [self.repeated_elements] if self.repeated_elements is not None else []
        self.repeated_elements = [v if isinstance(v, RepeatedElement) else RepeatedElement(**as_dict(v)) for v in self.repeated_elements]

        if self.consent is not None and not isinstance(self.consent, Consent):
            self.consent = Consent(**as_dict(self.consent))

        if self.disability is not None and not isinstance(self.disability, Disability):
            self.disability = Disability(**as_dict(self.disability))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CodeSystemsContainer(YAMLRoot):
    """
    A container class for all code systems used in RareLink.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RARELINK["CodeSystemsContainer"]
    class_class_curie: ClassVar[str] = "rarelink:CodeSystemsContainer"
    class_name: ClassVar[str] = "CodeSystemsContainer"
    class_model_uri: ClassVar[URIRef] = RARELINK_CDM.CodeSystemsContainer

    ncbi_taxon: Union[str, "NCBITaxon"] = None
    snomed: Union[str, "SNOMED"] = None
    mondo: Union[str, "MONDO"] = None
    hpo: Union[str, "HP"] = None
    loinc: Union[str, "LOINC"] = None
    omim: Union[str, "OMIM"] = None
    orpha: Union[str, "ORPHA"] = None
    ncit: Union[str, "NCIT"] = None
    uo: Union[str, "UO"] = None
    hgnc: Union[str, "HGNC"] = None
    hgvs: Union[str, "HGVS"] = None
    ga4gh: Union[str, "GA4GH"] = None
    hl7fhir: Union[str, "HL7FHIR"] = None
    icd11: Union[str, "ICD11"] = None
    icd10cm: Union[str, "ICD10CM"] = None
    icd10gm: Union[str, "ICD10GM"] = None
    so: Union[str, "SO"] = None
    geno: Union[str, "GENO"] = None
    icd9: Union[str, "ICD9"] = None
    iso3166: Union[str, "ISO3166"] = None
    icf: Union[str, "ICF"] = None

@dataclass(repr=False)
class RepeatedElement(YAMLRoot):
    """
    A generic container for repeated elements such as instruments and their instances used to define repeating data
    structures across the RareLink-CDM.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RARELINK["RepeatedElement"]
    class_class_curie: ClassVar[str] = "rarelink:RepeatedElement"
    class_name: ClassVar[str] = "RepeatedElement"
    class_model_uri: ClassVar[URIRef] = RARELINK_CDM.RepeatedElement

    redcap_repeat_instrument: Optional[str] = None
    redcap_repeat_instance: Optional[int] = None
    patient_status: Optional[Union[dict, "PatientStatus"]] = None
    care_pathway: Optional[Union[dict, "CarePathway"]] = None
    disease: Optional[Union[dict, "Disease"]] = None
    genetic_findings: Optional[Union[dict, "GeneticFindings"]] = None
    phenotypic_feature: Optional[Union[dict, "PhenotypicFeature"]] = None
    measruements: Optional[Union[dict, "Measurement"]] = None
    family_history: Optional[Union[dict, "FamilyHistory"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.redcap_repeat_instrument is not None and not isinstance(self.redcap_repeat_instrument, str):
            self.redcap_repeat_instrument = str(self.redcap_repeat_instrument)

        if self.redcap_repeat_instance is not None and not isinstance(self.redcap_repeat_instance, int):
            self.redcap_repeat_instance = int(self.redcap_repeat_instance)

        if self.patient_status is not None and not isinstance(self.patient_status, PatientStatus):
            self.patient_status = PatientStatus(**as_dict(self.patient_status))

        if self.care_pathway is not None and not isinstance(self.care_pathway, CarePathway):
            self.care_pathway = CarePathway(**as_dict(self.care_pathway))

        if self.disease is not None and not isinstance(self.disease, Disease):
            self.disease = Disease(**as_dict(self.disease))

        if self.genetic_findings is not None and not isinstance(self.genetic_findings, GeneticFindings):
            self.genetic_findings = GeneticFindings(**as_dict(self.genetic_findings))

        if self.phenotypic_feature is not None and not isinstance(self.phenotypic_feature, PhenotypicFeature):
            self.phenotypic_feature = PhenotypicFeature(**as_dict(self.phenotypic_feature))

        if self.measruements is not None and not isinstance(self.measruements, Measurement):
            self.measruements = Measurement(**as_dict(self.measruements))

        if self.family_history is not None and not isinstance(self.family_history, FamilyHistory):
            self.family_history = FamilyHistory(**as_dict(self.family_history))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FormalCriteria(YAMLRoot):
    """
    Section containing the RareLink (1) Formal Criteria Sheet
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RARELINK["FormalCriteria"]
    class_class_curie: ClassVar[str] = "rarelink:FormalCriteria"
    class_name: ClassVar[str] = "FormalCriteria"
    class_model_uri: ClassVar[URIRef] = RARELINK_CDM.FormalCriteria

    snomed_422549004: Union[str, FormalCriteriaSnomed422549004] = None
    snomed_399423000: Union[str, XSDDate] = None
    rarelink_1_formal_criteria_complete: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.snomed_422549004):
            self.MissingRequiredField("snomed_422549004")
        if not isinstance(self.snomed_422549004, FormalCriteriaSnomed422549004):
            self.snomed_422549004 = FormalCriteriaSnomed422549004(self.snomed_422549004)

        if self._is_empty(self.snomed_399423000):
            self.MissingRequiredField("snomed_399423000")
        if not isinstance(self.snomed_399423000, XSDDate):
            self.snomed_399423000 = XSDDate(self.snomed_399423000)

        if self.rarelink_1_formal_criteria_complete is not None and not isinstance(self.rarelink_1_formal_criteria_complete, str):
            self.rarelink_1_formal_criteria_complete = str(self.rarelink_1_formal_criteria_complete)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PersonalInformation(YAMLRoot):
    """
    The section Personal Information (2) of the RareLink CDM
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RARELINK["PersonalInformation"]
    class_class_curie: ClassVar[str] = "rarelink:PersonalInformation"
    class_name: ClassVar[str] = "PersonalInformation"
    class_model_uri: ClassVar[URIRef] = RARELINK_CDM.PersonalInformation

    snomed_184099003: Union[str, XSDDate] = None
    rarelink_2_personal_information_complete: str = None
    snomed_281053000: Optional[Union[str, "SexAtBirth"]] = None
    snomed_1296886006: Optional[Union[str, "KaryotypicSex"]] = None
    snomed_263495000: Optional[Union[str, "GenderIdentity"]] = None
    snomed_370159000: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.snomed_184099003):
            self.MissingRequiredField("snomed_184099003")
        if not isinstance(self.snomed_184099003, XSDDate):
            self.snomed_184099003 = XSDDate(self.snomed_184099003)

        if self._is_empty(self.rarelink_2_personal_information_complete):
            self.MissingRequiredField("rarelink_2_personal_information_complete")
        if not isinstance(self.rarelink_2_personal_information_complete, str):
            self.rarelink_2_personal_information_complete = str(self.rarelink_2_personal_information_complete)

        if self.snomed_281053000 is not None and not isinstance(self.snomed_281053000, SexAtBirth):
            self.snomed_281053000 = SexAtBirth(self.snomed_281053000)

        if self.snomed_1296886006 is not None and not isinstance(self.snomed_1296886006, KaryotypicSex):
            self.snomed_1296886006 = KaryotypicSex(self.snomed_1296886006)

        if self.snomed_263495000 is not None and not isinstance(self.snomed_263495000, GenderIdentity):
            self.snomed_263495000 = GenderIdentity(self.snomed_263495000)

        if self.snomed_370159000 is not None and not isinstance(self.snomed_370159000, str):
            self.snomed_370159000 = str(self.snomed_370159000)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PatientStatus(YAMLRoot):
    """
    The section Patient Status (3) of the RareLink CDM.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RARELINK["PatientStatus"]
    class_class_curie: ClassVar[str] = "rarelink:PatientStatus"
    class_name: ClassVar[str] = "PatientStatus"
    class_model_uri: ClassVar[URIRef] = RARELINK_CDM.PatientStatus

    rarelink_3_patient_status_complete: str = None
    patient_status_date: Optional[Union[str, XSDDate]] = None
    snomed_278844005: Optional[Union[str, "ClinicalVitalStatus"]] = None
    snomed_398299004: Optional[Union[str, UnionDateString]] = None
    snomed_184305005: Optional[str] = None
    snomed_105727008: Optional[Union[str, "AgeCategory"]] = None
    snomed_412726003: Optional[str] = None
    snomed_723663001: Optional[Union[str, "YesNo"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.rarelink_3_patient_status_complete):
            self.MissingRequiredField("rarelink_3_patient_status_complete")
        if not isinstance(self.rarelink_3_patient_status_complete, str):
            self.rarelink_3_patient_status_complete = str(self.rarelink_3_patient_status_complete)

        if self.patient_status_date is not None and not isinstance(self.patient_status_date, XSDDate):
            self.patient_status_date = XSDDate(self.patient_status_date)

        if self.snomed_278844005 is not None and not isinstance(self.snomed_278844005, ClinicalVitalStatus):
            self.snomed_278844005 = ClinicalVitalStatus(self.snomed_278844005)

        if self.snomed_398299004 is not None and not isinstance(self.snomed_398299004, UnionDateString):
            self.snomed_398299004 = UnionDateString(self.snomed_398299004)

        if self.snomed_184305005 is not None and not isinstance(self.snomed_184305005, str):
            self.snomed_184305005 = str(self.snomed_184305005)

        if self.snomed_105727008 is not None and not isinstance(self.snomed_105727008, AgeCategory):
            self.snomed_105727008 = AgeCategory(self.snomed_105727008)

        if self.snomed_412726003 is not None and not isinstance(self.snomed_412726003, str):
            self.snomed_412726003 = str(self.snomed_412726003)

        if self.snomed_723663001 is not None and not isinstance(self.snomed_723663001, YesNo):
            self.snomed_723663001 = YesNo(self.snomed_723663001)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CarePathway(YAMLRoot):
    """
    The section Care Pathway (4) of the RareLink CDM, documenting encounters including their start and end dates,
    status, and class.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RARELINK["CarePathway"]
    class_class_curie: ClassVar[str] = "rarelink:CarePathway"
    class_name: ClassVar[str] = "CarePathway"
    class_model_uri: ClassVar[URIRef] = RARELINK_CDM.CarePathway

    snomed_305058001: Union[str, "EncounterStatus"] = None
    hl7fhir_encounter_class: Union[str, "EncounterClass"] = None
    rarelink_4_care_pathway_complete: str = None
    hl7fhir_enc_period_start: Optional[Union[str, UnionDateString]] = None
    hl7fhir_enc_period_end: Optional[Union[str, UnionDateString]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.snomed_305058001):
            self.MissingRequiredField("snomed_305058001")
        if not isinstance(self.snomed_305058001, EncounterStatus):
            self.snomed_305058001 = EncounterStatus(self.snomed_305058001)

        if self._is_empty(self.hl7fhir_encounter_class):
            self.MissingRequiredField("hl7fhir_encounter_class")
        if not isinstance(self.hl7fhir_encounter_class, EncounterClass):
            self.hl7fhir_encounter_class = EncounterClass(self.hl7fhir_encounter_class)

        if self._is_empty(self.rarelink_4_care_pathway_complete):
            self.MissingRequiredField("rarelink_4_care_pathway_complete")
        if not isinstance(self.rarelink_4_care_pathway_complete, str):
            self.rarelink_4_care_pathway_complete = str(self.rarelink_4_care_pathway_complete)

        if self.hl7fhir_enc_period_start is not None and not isinstance(self.hl7fhir_enc_period_start, UnionDateString):
            self.hl7fhir_enc_period_start = UnionDateString(self.hl7fhir_enc_period_start)

        if self.hl7fhir_enc_period_end is not None and not isinstance(self.hl7fhir_enc_period_end, UnionDateString):
            self.hl7fhir_enc_period_end = UnionDateString(self.hl7fhir_enc_period_end)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Disease(YAMLRoot):
    """
    Captures details of diseases encoded using various terminologies and provides relevant metadata such as age at
    onset, verification status, etc.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RARELINK["Disease"]
    class_class_curie: ClassVar[str] = "rarelink:Disease"
    class_name: ClassVar[str] = "Disease"
    class_model_uri: ClassVar[URIRef] = RARELINK_CDM.Disease

    disease_coding: str = None
    loinc_99498_8: Union[str, "VerificationStatus"] = None
    rarelink_5_disease_complete: str = None
    snomed_64572001_mondo: Optional[str] = None
    snomed_64572001_ordo: Optional[str] = None
    snomed_64572001_icd10cm: Optional[str] = None
    snomed_64572001_icd11: Optional[str] = None
    snomed_64572001_omim_p: Optional[str] = None
    snomed_424850005: Optional[Union[str, "AgeCategory"]] = None
    snomed_298059007: Optional[Union[str, XSDDate]] = None
    snomed_423493009: Optional[Union[str, "AgeCategory"]] = None
    snomed_432213005: Optional[Union[str, XSDDate]] = None
    snomed_363698007: Optional[str] = None
    snomed_263493007: Optional[Union[str, "ClinicalStatus"]] = None
    snomed_246112005: Optional[Union[str, "DiseaseSeverity"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.disease_coding):
            self.MissingRequiredField("disease_coding")
        if not isinstance(self.disease_coding, str):
            self.disease_coding = str(self.disease_coding)

        if self._is_empty(self.loinc_99498_8):
            self.MissingRequiredField("loinc_99498_8")
        if not isinstance(self.loinc_99498_8, VerificationStatus):
            self.loinc_99498_8 = VerificationStatus(self.loinc_99498_8)

        if self._is_empty(self.rarelink_5_disease_complete):
            self.MissingRequiredField("rarelink_5_disease_complete")
        if not isinstance(self.rarelink_5_disease_complete, str):
            self.rarelink_5_disease_complete = str(self.rarelink_5_disease_complete)

        if self.snomed_64572001_mondo is not None and not isinstance(self.snomed_64572001_mondo, str):
            self.snomed_64572001_mondo = str(self.snomed_64572001_mondo)

        if self.snomed_64572001_ordo is not None and not isinstance(self.snomed_64572001_ordo, str):
            self.snomed_64572001_ordo = str(self.snomed_64572001_ordo)

        if self.snomed_64572001_icd10cm is not None and not isinstance(self.snomed_64572001_icd10cm, str):
            self.snomed_64572001_icd10cm = str(self.snomed_64572001_icd10cm)

        if self.snomed_64572001_icd11 is not None and not isinstance(self.snomed_64572001_icd11, str):
            self.snomed_64572001_icd11 = str(self.snomed_64572001_icd11)

        if self.snomed_64572001_omim_p is not None and not isinstance(self.snomed_64572001_omim_p, str):
            self.snomed_64572001_omim_p = str(self.snomed_64572001_omim_p)

        if self.snomed_424850005 is not None and not isinstance(self.snomed_424850005, AgeCategory):
            self.snomed_424850005 = AgeCategory(self.snomed_424850005)

        if self.snomed_298059007 is not None and not isinstance(self.snomed_298059007, XSDDate):
            self.snomed_298059007 = XSDDate(self.snomed_298059007)

        if self.snomed_423493009 is not None and not isinstance(self.snomed_423493009, AgeCategory):
            self.snomed_423493009 = AgeCategory(self.snomed_423493009)

        if self.snomed_432213005 is not None and not isinstance(self.snomed_432213005, XSDDate):
            self.snomed_432213005 = XSDDate(self.snomed_432213005)

        if self.snomed_363698007 is not None and not isinstance(self.snomed_363698007, str):
            self.snomed_363698007 = str(self.snomed_363698007)

        if self.snomed_263493007 is not None and not isinstance(self.snomed_263493007, ClinicalStatus):
            self.snomed_263493007 = ClinicalStatus(self.snomed_263493007)

        if self.snomed_246112005 is not None and not isinstance(self.snomed_246112005, DiseaseSeverity):
            self.snomed_246112005 = DiseaseSeverity(self.snomed_246112005)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeneticFindings(YAMLRoot):
    """
    Captures details about genetic findings and associated metadata like genomic diagnoses, interpretation, zygosity,
    clinical significance, and more.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RARELINK["GeneticFindings"]
    class_class_curie: ClassVar[str] = "rarelink:GeneticFindings"
    class_name: ClassVar[str] = "GeneticFindings"
    class_model_uri: ClassVar[URIRef] = RARELINK_CDM.GeneticFindings

    genetic_diagnosis_code: str = None
    rarelink_6_1_genetic_findings_complete: str = None
    snomed_106221001_mondo: Optional[str] = None
    snomed_106221001_omim_p: Optional[str] = None
    ga4gh_progress_status: Optional[Union[str, "InterpretationProgressStatus"]] = None
    ga4gh_interp_status: Optional[Union[str, "InterpretationStatus"]] = None
    loinc_81304_8: Optional[Union[str, "StructuralVariantMethod"]] = None
    loinc_62374_4: Optional[Union[str, "ReferenceGenome"]] = None
    loinc_lp7824_8: Optional[str] = None
    variant_expression: Optional[Union[str, "VariantExpressionType"]] = None
    loinc_81290_9: Optional[str] = None
    loinc_48004_6: Optional[str] = None
    loinc_48005_3: Optional[str] = None
    variant_validation: Optional[Union[str, "YesNo"]] = None
    loinc_48018_6: Optional[str] = None
    loinc_48018_6_label: Optional[str] = None
    loinc_53034_5: Optional[Union[str, "Zygosity"]] = None
    loinc_53034_5_other: Optional[str] = None
    loinc_48002_0: Optional[Union[str, "GenomicSourceClass"]] = None
    loinc_48019_4: Optional[Union[str, "DNAChangeType"]] = None
    loinc_48019_4_other: Optional[str] = None
    loinc_53037_8: Optional[Union[str, "ClinicalSignificance"]] = None
    ga4gh_therap_action: Optional[Union[str, "TherapeuticActionability"]] = None
    loinc_93044_6: Optional[Union[str, "LevelOfEvidence"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.genetic_diagnosis_code):
            self.MissingRequiredField("genetic_diagnosis_code")
        if not isinstance(self.genetic_diagnosis_code, str):
            self.genetic_diagnosis_code = str(self.genetic_diagnosis_code)

        if self._is_empty(self.rarelink_6_1_genetic_findings_complete):
            self.MissingRequiredField("rarelink_6_1_genetic_findings_complete")
        if not isinstance(self.rarelink_6_1_genetic_findings_complete, str):
            self.rarelink_6_1_genetic_findings_complete = str(self.rarelink_6_1_genetic_findings_complete)

        if self.snomed_106221001_mondo is not None and not isinstance(self.snomed_106221001_mondo, str):
            self.snomed_106221001_mondo = str(self.snomed_106221001_mondo)

        if self.snomed_106221001_omim_p is not None and not isinstance(self.snomed_106221001_omim_p, str):
            self.snomed_106221001_omim_p = str(self.snomed_106221001_omim_p)

        if self.ga4gh_progress_status is not None and not isinstance(self.ga4gh_progress_status, InterpretationProgressStatus):
            self.ga4gh_progress_status = InterpretationProgressStatus(self.ga4gh_progress_status)

        if self.ga4gh_interp_status is not None and not isinstance(self.ga4gh_interp_status, InterpretationStatus):
            self.ga4gh_interp_status = InterpretationStatus(self.ga4gh_interp_status)

        if self.loinc_81304_8 is not None and not isinstance(self.loinc_81304_8, StructuralVariantMethod):
            self.loinc_81304_8 = StructuralVariantMethod(self.loinc_81304_8)

        if self.loinc_62374_4 is not None and not isinstance(self.loinc_62374_4, ReferenceGenome):
            self.loinc_62374_4 = ReferenceGenome(self.loinc_62374_4)

        if self.loinc_lp7824_8 is not None and not isinstance(self.loinc_lp7824_8, str):
            self.loinc_lp7824_8 = str(self.loinc_lp7824_8)

        if self.variant_expression is not None and not isinstance(self.variant_expression, VariantExpressionType):
            self.variant_expression = VariantExpressionType(self.variant_expression)

        if self.loinc_81290_9 is not None and not isinstance(self.loinc_81290_9, str):
            self.loinc_81290_9 = str(self.loinc_81290_9)

        if self.loinc_48004_6 is not None and not isinstance(self.loinc_48004_6, str):
            self.loinc_48004_6 = str(self.loinc_48004_6)

        if self.loinc_48005_3 is not None and not isinstance(self.loinc_48005_3, str):
            self.loinc_48005_3 = str(self.loinc_48005_3)

        if self.variant_validation is not None and not isinstance(self.variant_validation, YesNo):
            self.variant_validation = YesNo(self.variant_validation)

        if self.loinc_48018_6 is not None and not isinstance(self.loinc_48018_6, str):
            self.loinc_48018_6 = str(self.loinc_48018_6)

        if self.loinc_48018_6_label is not None and not isinstance(self.loinc_48018_6_label, str):
            self.loinc_48018_6_label = str(self.loinc_48018_6_label)

        if self.loinc_53034_5 is not None and not isinstance(self.loinc_53034_5, Zygosity):
            self.loinc_53034_5 = Zygosity(self.loinc_53034_5)

        if self.loinc_53034_5_other is not None and not isinstance(self.loinc_53034_5_other, str):
            self.loinc_53034_5_other = str(self.loinc_53034_5_other)

        if self.loinc_48002_0 is not None and not isinstance(self.loinc_48002_0, GenomicSourceClass):
            self.loinc_48002_0 = GenomicSourceClass(self.loinc_48002_0)

        if self.loinc_48019_4 is not None and not isinstance(self.loinc_48019_4, DNAChangeType):
            self.loinc_48019_4 = DNAChangeType(self.loinc_48019_4)

        if self.loinc_48019_4_other is not None and not isinstance(self.loinc_48019_4_other, str):
            self.loinc_48019_4_other = str(self.loinc_48019_4_other)

        if self.loinc_53037_8 is not None and not isinstance(self.loinc_53037_8, ClinicalSignificance):
            self.loinc_53037_8 = ClinicalSignificance(self.loinc_53037_8)

        if self.ga4gh_therap_action is not None and not isinstance(self.ga4gh_therap_action, TherapeuticActionability):
            self.ga4gh_therap_action = TherapeuticActionability(self.ga4gh_therap_action)

        if self.loinc_93044_6 is not None and not isinstance(self.loinc_93044_6, LevelOfEvidence):
            self.loinc_93044_6 = LevelOfEvidence(self.loinc_93044_6)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhenotypicFeature(YAMLRoot):
    """
    The section Phenotypic Feature (6.2) of the RareLink CDM.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RARELINK["PhenotypicFeature"]
    class_class_curie: ClassVar[str] = "rarelink:PhenotypicFeature"
    class_name: ClassVar[str] = "PhenotypicFeature"
    class_model_uri: ClassVar[URIRef] = RARELINK_CDM.PhenotypicFeature

    snomed_8116006: str = None
    rarelink_6_2_phenotypic_feature_complete: str = None
    snomed_363778006: Optional[Union[str, "PhenotypicFeatureStatus"]] = None
    snomed_8116006_onset: Optional[Union[str, XSDDate]] = None
    snomed_8116006_resolution: Optional[Union[str, XSDDate]] = None
    hp_0003674: Optional[Union[str, "AgeOfOnset"]] = None
    hp_0011008: Optional[Union[str, "TemporalPattern"]] = None
    hp_0012824: Optional[Union[str, "PhenotypeSeverity"]] = None
    hp_0012823_hp1: Optional[str] = None
    hp_0012823_hp2: Optional[str] = None
    hp_0012823_hp3: Optional[str] = None
    hp_0012823_ncbitaxon: Optional[str] = None
    hp_0012823_snomed: Optional[str] = None
    phenotypicfeature_evidence: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.snomed_8116006):
            self.MissingRequiredField("snomed_8116006")
        if not isinstance(self.snomed_8116006, str):
            self.snomed_8116006 = str(self.snomed_8116006)

        if self._is_empty(self.rarelink_6_2_phenotypic_feature_complete):
            self.MissingRequiredField("rarelink_6_2_phenotypic_feature_complete")
        if not isinstance(self.rarelink_6_2_phenotypic_feature_complete, str):
            self.rarelink_6_2_phenotypic_feature_complete = str(self.rarelink_6_2_phenotypic_feature_complete)

        if self.snomed_363778006 is not None and not isinstance(self.snomed_363778006, PhenotypicFeatureStatus):
            self.snomed_363778006 = PhenotypicFeatureStatus(self.snomed_363778006)

        if self.snomed_8116006_onset is not None and not isinstance(self.snomed_8116006_onset, XSDDate):
            self.snomed_8116006_onset = XSDDate(self.snomed_8116006_onset)

        if self.snomed_8116006_resolution is not None and not isinstance(self.snomed_8116006_resolution, XSDDate):
            self.snomed_8116006_resolution = XSDDate(self.snomed_8116006_resolution)

        if self.hp_0003674 is not None and not isinstance(self.hp_0003674, AgeOfOnset):
            self.hp_0003674 = AgeOfOnset(self.hp_0003674)

        if self.hp_0011008 is not None and not isinstance(self.hp_0011008, TemporalPattern):
            self.hp_0011008 = TemporalPattern(self.hp_0011008)

        if self.hp_0012824 is not None and not isinstance(self.hp_0012824, PhenotypeSeverity):
            self.hp_0012824 = PhenotypeSeverity(self.hp_0012824)

        if self.hp_0012823_hp1 is not None and not isinstance(self.hp_0012823_hp1, str):
            self.hp_0012823_hp1 = str(self.hp_0012823_hp1)

        if self.hp_0012823_hp2 is not None and not isinstance(self.hp_0012823_hp2, str):
            self.hp_0012823_hp2 = str(self.hp_0012823_hp2)

        if self.hp_0012823_hp3 is not None and not isinstance(self.hp_0012823_hp3, str):
            self.hp_0012823_hp3 = str(self.hp_0012823_hp3)

        if self.hp_0012823_ncbitaxon is not None and not isinstance(self.hp_0012823_ncbitaxon, str):
            self.hp_0012823_ncbitaxon = str(self.hp_0012823_ncbitaxon)

        if self.hp_0012823_snomed is not None and not isinstance(self.hp_0012823_snomed, str):
            self.hp_0012823_snomed = str(self.hp_0012823_snomed)

        if self.phenotypicfeature_evidence is not None and not isinstance(self.phenotypicfeature_evidence, str):
            self.phenotypicfeature_evidence = str(self.phenotypicfeature_evidence)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Measurement(YAMLRoot):
    """
    The section Measurements (6.3) of the RareLink CDM. This section captures assay-related measurements and their
    corresponding values, units, interpretations, and procedures.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RARELINK["Measurement"]
    class_class_curie: ClassVar[str] = "rarelink:Measurement"
    class_name: ClassVar[str] = "Measurement"
    class_model_uri: ClassVar[URIRef] = RARELINK_CDM.Measurement

    assay: str = None
    value: float = None
    value_unit: str = None
    rarelink_6_3_measurements_complete: str = None
    interpretation: Optional[str] = None
    time_observed: Optional[Union[str, XSDDate]] = None
    procedure_ncit: Optional[str] = None
    procedure_snomed: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.assay):
            self.MissingRequiredField("assay")
        if not isinstance(self.assay, str):
            self.assay = str(self.assay)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, float):
            self.value = float(self.value)

        if self._is_empty(self.value_unit):
            self.MissingRequiredField("value_unit")
        if not isinstance(self.value_unit, str):
            self.value_unit = str(self.value_unit)

        if self._is_empty(self.rarelink_6_3_measurements_complete):
            self.MissingRequiredField("rarelink_6_3_measurements_complete")
        if not isinstance(self.rarelink_6_3_measurements_complete, str):
            self.rarelink_6_3_measurements_complete = str(self.rarelink_6_3_measurements_complete)

        if self.interpretation is not None and not isinstance(self.interpretation, str):
            self.interpretation = str(self.interpretation)

        if self.time_observed is not None and not isinstance(self.time_observed, XSDDate):
            self.time_observed = XSDDate(self.time_observed)

        if self.procedure_ncit is not None and not isinstance(self.procedure_ncit, str):
            self.procedure_ncit = str(self.procedure_ncit)

        if self.procedure_snomed is not None and not isinstance(self.procedure_snomed, str):
            self.procedure_snomed = str(self.procedure_snomed)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FamilyHistory(YAMLRoot):
    """
    Captures the family history of the individual, detailing relationships, consanguinity, and specific family member
    details like diseases, age, sex, and cause of death.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RARELINK["FamilyHistory"]
    class_class_curie: ClassVar[str] = "rarelink:FamilyHistory"
    class_name: ClassVar[str] = "FamilyHistory"
    class_model_uri: ClassVar[URIRef] = RARELINK_CDM.FamilyHistory

    family_history_pseudonym: Optional[str] = None
    propositus: Optional[Union[str, "PropositusStatus"]] = None
    relationship_to_index_case: Optional[Union[str, "RelationshipToIndexCase"]] = None
    consanguinity: Optional[Union[str, "YesNoUnknown"]] = None
    family_member_relationship: Optional[Union[str, "FamilyRelationship"]] = None
    family_member_record_status: Optional[Union[str, "FamilyRecordStatus"]] = None
    family_member_sex: Optional[Union[str, "FamilyMemberSex"]] = None
    family_member_age: Optional[int] = None
    family_member_dob: Optional[Union[str, XSDDate]] = None
    family_member_deceased: Optional[Union[str, "YesNoUnknown"]] = None
    family_member_cause_of_death: Optional[str] = None
    family_member_deceased_age: Optional[int] = None
    family_member_disease: Optional[str] = None
    rarelink_6_4_family_history_complete: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.family_history_pseudonym is not None and not isinstance(self.family_history_pseudonym, str):
            self.family_history_pseudonym = str(self.family_history_pseudonym)

        if self.propositus is not None and not isinstance(self.propositus, PropositusStatus):
            self.propositus = PropositusStatus(self.propositus)

        if self.relationship_to_index_case is not None and not isinstance(self.relationship_to_index_case, RelationshipToIndexCase):
            self.relationship_to_index_case = RelationshipToIndexCase(self.relationship_to_index_case)

        if self.consanguinity is not None and not isinstance(self.consanguinity, YesNoUnknown):
            self.consanguinity = YesNoUnknown(self.consanguinity)

        if self.family_member_relationship is not None and not isinstance(self.family_member_relationship, FamilyRelationship):
            self.family_member_relationship = FamilyRelationship(self.family_member_relationship)

        if self.family_member_record_status is not None and not isinstance(self.family_member_record_status, FamilyRecordStatus):
            self.family_member_record_status = FamilyRecordStatus(self.family_member_record_status)

        if self.family_member_sex is not None and not isinstance(self.family_member_sex, FamilyMemberSex):
            self.family_member_sex = FamilyMemberSex(self.family_member_sex)

        if self.family_member_age is not None and not isinstance(self.family_member_age, int):
            self.family_member_age = int(self.family_member_age)

        if self.family_member_dob is not None and not isinstance(self.family_member_dob, XSDDate):
            self.family_member_dob = XSDDate(self.family_member_dob)

        if self.family_member_deceased is not None and not isinstance(self.family_member_deceased, YesNoUnknown):
            self.family_member_deceased = YesNoUnknown(self.family_member_deceased)

        if self.family_member_cause_of_death is not None and not isinstance(self.family_member_cause_of_death, str):
            self.family_member_cause_of_death = str(self.family_member_cause_of_death)

        if self.family_member_deceased_age is not None and not isinstance(self.family_member_deceased_age, int):
            self.family_member_deceased_age = int(self.family_member_deceased_age)

        if self.family_member_disease is not None and not isinstance(self.family_member_disease, str):
            self.family_member_disease = str(self.family_member_disease)

        if self.rarelink_6_4_family_history_complete is not None and not isinstance(self.rarelink_6_4_family_history_complete, str):
            self.rarelink_6_4_family_history_complete = str(self.rarelink_6_4_family_history_complete)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Consent(YAMLRoot):
    """
    The section Consent (7) of the RareLink CDM.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RARELINK["Consent"]
    class_class_curie: ClassVar[str] = "rarelink:Consent"
    class_name: ClassVar[str] = "Consent"
    class_model_uri: ClassVar[URIRef] = RARELINK_CDM.Consent

    consent_status: Union[str, "ConsentStatus"] = None
    health_policy_monitoring: str = None
    agreement_to_contact: Union[str, "YesNoUnknown"] = None
    consent_to_reuse_data: Union[str, "YesNoUnknown"] = None
    rarelink_7_consent_complete: str = None
    consent_date: Optional[Union[str, XSDDate]] = None
    biological_sample: Optional[Union[str, "YesNoUnknown"]] = None
    biobank_link: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.consent_status):
            self.MissingRequiredField("consent_status")
        if not isinstance(self.consent_status, ConsentStatus):
            self.consent_status = ConsentStatus(self.consent_status)

        if self._is_empty(self.health_policy_monitoring):
            self.MissingRequiredField("health_policy_monitoring")
        if not isinstance(self.health_policy_monitoring, str):
            self.health_policy_monitoring = str(self.health_policy_monitoring)

        if self._is_empty(self.agreement_to_contact):
            self.MissingRequiredField("agreement_to_contact")
        if not isinstance(self.agreement_to_contact, YesNoUnknown):
            self.agreement_to_contact = YesNoUnknown(self.agreement_to_contact)

        if self._is_empty(self.consent_to_reuse_data):
            self.MissingRequiredField("consent_to_reuse_data")
        if not isinstance(self.consent_to_reuse_data, YesNoUnknown):
            self.consent_to_reuse_data = YesNoUnknown(self.consent_to_reuse_data)

        if self._is_empty(self.rarelink_7_consent_complete):
            self.MissingRequiredField("rarelink_7_consent_complete")
        if not isinstance(self.rarelink_7_consent_complete, str):
            self.rarelink_7_consent_complete = str(self.rarelink_7_consent_complete)

        if self.consent_date is not None and not isinstance(self.consent_date, XSDDate):
            self.consent_date = XSDDate(self.consent_date)

        if self.biological_sample is not None and not isinstance(self.biological_sample, YesNoUnknown):
            self.biological_sample = YesNoUnknown(self.biological_sample)

        if self.biobank_link is not None and not isinstance(self.biobank_link, str):
            self.biobank_link = str(self.biobank_link)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Disability(YAMLRoot):
    """
    The section for capturing the classification of functioning or disability for an individual using the
    International Classification of Functioning, Disability and Health (ICF).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RARELINK["Disability"]
    class_class_curie: ClassVar[str] = "rarelink:Disability"
    class_name: ClassVar[str] = "Disability"
    class_model_uri: ClassVar[URIRef] = RARELINK_CDM.Disability

    icf_score: str = None
    rarelink_8_disability_complete: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.icf_score):
            self.MissingRequiredField("icf_score")
        if not isinstance(self.icf_score, str):
            self.icf_score = str(self.icf_score)

        if self._is_empty(self.rarelink_8_disability_complete):
            self.MissingRequiredField("rarelink_8_disability_complete")
        if not isinstance(self.rarelink_8_disability_complete, str):
            self.rarelink_8_disability_complete = str(self.rarelink_8_disability_complete)

        super().__post_init__(**kwargs)


# Enumerations
class NCBITaxon(EnumDefinitionImpl):
    """
    NCBI organismal classification
    """
    _defn = EnumDefinition(
        name="NCBITaxon",
        description="NCBI organismal classification",
        code_set_version="2024-07-03",
    )

class SNOMED(EnumDefinitionImpl):
    """
    SNOMED CT
    """
    _defn = EnumDefinition(
        name="SNOMED",
        description="SNOMED CT",
        code_set_version="2024-09-01",
    )

class MONDO(EnumDefinitionImpl):
    """
    Monarch Disease Ontology
    """
    _defn = EnumDefinition(
        name="MONDO",
        description="Monarch Disease Ontology",
        code_set_version="2024-09-03",
    )

class HP(EnumDefinitionImpl):
    """
    Human Phenotype Ontology
    """
    _defn = EnumDefinition(
        name="HP",
        description="Human Phenotype Ontology",
        code_set_version="2024-08-13",
    )

class LOINC(EnumDefinitionImpl):
    """
    Logical Observation Identifiers Names and Codes
    """
    _defn = EnumDefinition(
        name="LOINC",
        description="Logical Observation Identifiers Names and Codes",
        code_set_version="2.78",
    )

class OMIM(EnumDefinitionImpl):
    """
    Online Mendelian Inheritance
    """
    _defn = EnumDefinition(
        name="OMIM",
        description="Online Mendelian Inheritance",
        code_set_version="2024-09-12",
    )

class ORPHA(EnumDefinitionImpl):
    """
    Orphanet Rare Disease Ontology
    """
    _defn = EnumDefinition(
        name="ORPHA",
        description="Orphanet Rare Disease Ontology",
        code_set_version="2024-09-12",
    )

class NCIT(EnumDefinitionImpl):
    """
    NCI Thesaurus OBO Edition
    """
    _defn = EnumDefinition(
        name="NCIT",
        description="NCI Thesaurus OBO Edition",
        code_set_version="24.04e",
    )

class UO(EnumDefinitionImpl):
    """
    Units of Measurement Ontology
    """
    _defn = EnumDefinition(
        name="UO",
        description="Units of Measurement Ontology",
        code_set_version="2024-09-12",
    )

class HGNC(EnumDefinitionImpl):
    """
    HUGO Gene Nomenclature Committee
    """
    _defn = EnumDefinition(
        name="HGNC",
        description="HUGO Gene Nomenclature Committee",
        code_set_version="2024-08-23",
    )

class HGVS(EnumDefinitionImpl):
    """
    Human Genome Variation Society
    """
    _defn = EnumDefinition(
        name="HGVS",
        description="Human Genome Variation Society",
        code_set_version="21.0.0",
    )

class GA4GH(EnumDefinitionImpl):
    """
    Global Alliance for Genomics and Health
    """
    _defn = EnumDefinition(
        name="GA4GH",
        description="Global Alliance for Genomics and Health",
        code_set_version="v2.0",
    )

class HL7FHIR(EnumDefinitionImpl):
    """
    Health Level 7 Fast Healthcare Interoperability Resources
    """
    _defn = EnumDefinition(
        name="HL7FHIR",
        description="Health Level 7 Fast Healthcare Interoperability Resources",
        code_set_version="v4.0.1",
    )

class ICD11(EnumDefinitionImpl):
    """
    International Classification of Diseases, Eleventh Revision
    """
    _defn = EnumDefinition(
        name="ICD11",
        description="International Classification of Diseases, Eleventh Revision",
        code_set_version="2024-09-01",
    )

class ICD10CM(EnumDefinitionImpl):
    """
    International Classification of Diseases, Tenth Revision, Clinical Modification
    """
    _defn = EnumDefinition(
        name="ICD10CM",
        description="International Classification of Diseases, Tenth Revision, Clinical Modification",
        code_set_version="2024-09-01",
    )

class ICD10GM(EnumDefinitionImpl):
    """
    International Classification of Diseases, Tenth Revision, German Modification
    """
    _defn = EnumDefinition(
        name="ICD10GM",
        description="International Classification of Diseases, Tenth Revision, German Modification",
        code_set_version="2024-09-01",
    )

class SO(EnumDefinitionImpl):
    """
    Sequence types and features ontology
    """
    _defn = EnumDefinition(
        name="SO",
        description="Sequence types and features ontology",
        code_set_version="2.6",
    )

class GENO(EnumDefinitionImpl):
    """
    GENO - The Genotype Ontology
    """
    _defn = EnumDefinition(
        name="GENO",
        description="GENO - The Genotype Ontology",
        code_set_version="2023-10-08",
    )

class ICD9(EnumDefinitionImpl):
    """
    International Classification of Diseases, Ninth Revision
    """
    _defn = EnumDefinition(
        name="ICD9",
        description="International Classification of Diseases, Ninth Revision",
        code_set_version="2024-09-01",
    )

class ISO3166(EnumDefinitionImpl):
    """
    ISO 3166-1:2020(en) alpha-2 and alpha-3 country codes
    """
    _defn = EnumDefinition(
        name="ISO3166",
        description="ISO 3166-1:2020(en) alpha-2 and alpha-3 country codes",
        code_set_version="2020(en)",
    )

class ICF(EnumDefinitionImpl):
    """
    International Classification of Functioning, Disability and Health
    """
    _defn = EnumDefinition(
        name="ICF",
        description="International Classification of Functioning, Disability and Health",
        code_set_version="1.0.2",
    )

class SexAtBirth(EnumDefinitionImpl):

    snomed_248152002 = PermissibleValue(
        text="snomed_248152002",
        description="Female",
        meaning=SNOMED["248152002"])
    snomed_248153007 = PermissibleValue(
        text="snomed_248153007",
        description="Male",
        meaning=SNOMED["248153007"])
    snomed_184115007 = PermissibleValue(
        text="snomed_184115007",
        description="Patient sex unknown",
        meaning=SNOMED["184115007"])
    snomed_32570691000036108 = PermissibleValue(
        text="snomed_32570691000036108",
        description="Intersex",
        meaning=SNOMED["32570691000036108"])
    snomed_1220561009 = PermissibleValue(
        text="snomed_1220561009",
        description="Not recorded",
        meaning=SNOMED["1220561009"])

    _defn = EnumDefinition(
        name="SexAtBirth",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

class KaryotypicSex(EnumDefinitionImpl):

    snomed_261665006 = PermissibleValue(
        text="snomed_261665006",
        description="Unknown",
        meaning=SNOMED["261665006"])
    snomed_734875008 = PermissibleValue(
        text="snomed_734875008",
        description="XX",
        meaning=SNOMED["734875008"])
    snomed_734876009 = PermissibleValue(
        text="snomed_734876009",
        description="XY",
        meaning=SNOMED["734876009"])
    snomed_80427008 = PermissibleValue(
        text="snomed_80427008",
        description="X0",
        meaning=SNOMED["80427008"])
    snomed_65162001 = PermissibleValue(
        text="snomed_65162001",
        description="XXY",
        meaning=SNOMED["65162001"])
    snomed_35111009 = PermissibleValue(
        text="snomed_35111009",
        description="XXX",
        meaning=SNOMED["35111009"])
    snomed_403760006 = PermissibleValue(
        text="snomed_403760006",
        description="XXYY",
        meaning=SNOMED["403760006"])
    snomed_78317008 = PermissibleValue(
        text="snomed_78317008",
        description="XXXY",
        meaning=SNOMED["78317008"])
    snomed_10567003 = PermissibleValue(
        text="snomed_10567003",
        description="XXXX",
        meaning=SNOMED["10567003"])
    snomed_48930007 = PermissibleValue(
        text="snomed_48930007",
        description="XYY",
        meaning=SNOMED["48930007"])
    snomed_74964007 = PermissibleValue(
        text="snomed_74964007",
        description="Other",
        meaning=SNOMED["74964007"])

    _defn = EnumDefinition(
        name="KaryotypicSex",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

class GenderIdentity(EnumDefinitionImpl):

    snomed_446141000124107 = PermissibleValue(
        text="snomed_446141000124107",
        description="Female gender identity",
        meaning=SNOMED["446141000124107"])
    snomed_446151000124109 = PermissibleValue(
        text="snomed_446151000124109",
        description="Male gender identity",
        meaning=SNOMED["446151000124109"])
    snomed_394743007 = PermissibleValue(
        text="snomed_394743007",
        description="Gender unknown",
        meaning=SNOMED["394743007"])
    snomed_33791000087105 = PermissibleValue(
        text="snomed_33791000087105",
        description="Identifies as nonbinary gender",
        meaning=SNOMED["33791000087105"])
    snomed_1220561009 = PermissibleValue(
        text="snomed_1220561009",
        description="Not recorded",
        meaning=SNOMED["1220561009"])

    _defn = EnumDefinition(
        name="GenderIdentity",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

class ClinicalVitalStatus(EnumDefinitionImpl):

    snomed_438949009 = PermissibleValue(
        text="snomed_438949009",
        description="Alive",
        meaning=SNOMED["438949009"])
    snomed_419099009 = PermissibleValue(
        text="snomed_419099009",
        description="Dead",
        meaning=SNOMED["419099009"])
    snomed_399307001 = PermissibleValue(
        text="snomed_399307001",
        description="Unknown - Lost in follow-up",
        meaning=SNOMED["399307001"])
    snomed_185924006 = PermissibleValue(
        text="snomed_185924006",
        description="Unknown - Opted-out",
        meaning=SNOMED["185924006"])
    snomed_261665006 = PermissibleValue(
        text="snomed_261665006",
        description="Unknown - Other Reason",
        meaning=SNOMED["261665006"])

    _defn = EnumDefinition(
        name="ClinicalVitalStatus",
    )

class AgeCategory(EnumDefinitionImpl):

    snomed_3658006 = PermissibleValue(
        text="snomed_3658006",
        description="Infancy",
        meaning=SNOMED["3658006"])
    snomed_713153009 = PermissibleValue(
        text="snomed_713153009",
        description="Toddler",
        meaning=SNOMED["713153009"])
    snomed_255398004 = PermissibleValue(
        text="snomed_255398004",
        description="Childhood",
        meaning=SNOMED["255398004"])
    snomed_263659003 = PermissibleValue(
        text="snomed_263659003",
        description="Adolescence",
        meaning=SNOMED["263659003"])
    snomed_41847000 = PermissibleValue(
        text="snomed_41847000",
        description="Adulthood",
        meaning=SNOMED["41847000"])
    snomed_303112003 = PermissibleValue(
        text="snomed_303112003",
        description="Fetal period",
        meaning=SNOMED["303112003"])
    snomed_419099009 = PermissibleValue(
        text="snomed_419099009",
        description="Dead",
        meaning=SNOMED["419099009"])
    snomed_261665006 = PermissibleValue(
        text="snomed_261665006",
        description="Unknown",
        meaning=SNOMED["261665006"])

    _defn = EnumDefinition(
        name="AgeCategory",
    )

class YesNo(EnumDefinitionImpl):

    snomed_373066001 = PermissibleValue(
        text="snomed_373066001",
        description="True",
        meaning=SNOMED["373066001"])
    snomed_373067005 = PermissibleValue(
        text="snomed_373067005",
        description="False",
        meaning=SNOMED["373067005"])

    _defn = EnumDefinition(
        name="YesNo",
    )

class EncounterStatus(EnumDefinitionImpl):

    hl7fhir_planned = PermissibleValue(
        text="hl7fhir_planned",
        description="Planned",
        meaning=HL7FHIR["planned"])
    hl7fhir_arrived = PermissibleValue(
        text="hl7fhir_arrived",
        description="Arrived",
        meaning=HL7FHIR["arrived"])
    hl7fhir_triaged = PermissibleValue(
        text="hl7fhir_triaged",
        description="Triaged",
        meaning=HL7FHIR["triaged"])
    hl7fhir_onleave = PermissibleValue(
        text="hl7fhir_onleave",
        description="On Leave",
        meaning=HL7FHIR["onleave"])
    hl7fhir_finished = PermissibleValue(
        text="hl7fhir_finished",
        description="Finished",
        meaning=HL7FHIR["finished"])
    hl7fhir_cancelled = PermissibleValue(
        text="hl7fhir_cancelled",
        description="Cancelled",
        meaning=HL7FHIR["cancelled"])
    hl7fhir_unknown = PermissibleValue(
        text="hl7fhir_unknown",
        description="Unknown",
        meaning=HL7FHIR["unknown"])

    _defn = EnumDefinition(
        name="EncounterStatus",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "hl7fhir_in-progress",
            PermissibleValue(
                text="hl7fhir_in-progress",
                description="In Progress",
                meaning=HL7FHIR["in-progress"]))
        setattr(cls, "hl7fhir_entered-in-error",
            PermissibleValue(
                text="hl7fhir_entered-in-error",
                description="Entered in Error",
                meaning=HL7FHIR["entered-in-error"]))

class EncounterClass(EnumDefinitionImpl):

    hl7fhir_amb = PermissibleValue(
        text="hl7fhir_amb",
        description="Ambulatory",
        meaning=HL7FHIR["amb"])
    hl7fhir_imp = PermissibleValue(
        text="hl7fhir_imp",
        description="Inpatient",
        meaning=HL7FHIR["imp"])
    hl7fhir_obsenc = PermissibleValue(
        text="hl7fhir_obsenc",
        description="Observation",
        meaning=HL7FHIR["obsenc"])
    hl7fhir_emer = PermissibleValue(
        text="hl7fhir_emer",
        description="Emergency",
        meaning=HL7FHIR["emer"])
    hl7fhir_vr = PermissibleValue(
        text="hl7fhir_vr",
        description="Virtual",
        meaning=HL7FHIR["vr"])
    hl7fhir_hh = PermissibleValue(
        text="hl7fhir_hh",
        description="Home Health",
        meaning=HL7FHIR["hh"])
    rarelink_rdc = PermissibleValue(
        text="rarelink_rdc",
        description="RD Specialist Center",
        meaning=RARELINK["rdc"])
    snomed_261665006 = PermissibleValue(
        text="snomed_261665006",
        description="Unknown",
        meaning=SNOMED["261665006"])

    _defn = EnumDefinition(
        name="EncounterClass",
    )

class VerificationStatus(EnumDefinitionImpl):

    hl7fhir_unconfirmed = PermissibleValue(
        text="hl7fhir_unconfirmed",
        description="Unconfirmed",
        meaning=HL7FHIR["unconfirmed"])
    hl7fhir_provisional = PermissibleValue(
        text="hl7fhir_provisional",
        description="Provisional",
        meaning=HL7FHIR["provisional"])
    hl7fhir_differential = PermissibleValue(
        text="hl7fhir_differential",
        description="Differential",
        meaning=HL7FHIR["differential"])
    hl7fhir_confirmed = PermissibleValue(
        text="hl7fhir_confirmed",
        description="Confirmed",
        meaning=HL7FHIR["confirmed"])
    hl7fhir_refuted = PermissibleValue(
        text="hl7fhir_refuted",
        description="Refuted",
        meaning=HL7FHIR["refuted"])

    _defn = EnumDefinition(
        name="VerificationStatus",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "hl7fhir_entered-in-error",
            PermissibleValue(
                text="hl7fhir_entered-in-error",
                description="Entered in Error",
                meaning=HL7FHIR["entered-in-error"]))

class AgeAtOnset(EnumDefinitionImpl):

    snomed_118189007 = PermissibleValue(
        text="snomed_118189007",
        description="Prenatal",
        meaning=SNOMED["118189007"])
    snomed_3950001 = PermissibleValue(
        text="snomed_3950001",
        description="Birth",
        meaning=SNOMED["3950001"])
    snomed_410672004 = PermissibleValue(
        text="snomed_410672004",
        description="Date",
        meaning=SNOMED["410672004"])
    snomed_261665006 = PermissibleValue(
        text="snomed_261665006",
        description="Unknown",
        meaning=SNOMED["261665006"])

    _defn = EnumDefinition(
        name="AgeAtOnset",
    )

class AgeAtDiagnosis(EnumDefinitionImpl):

    snomed_118189007 = PermissibleValue(
        text="snomed_118189007",
        description="Prenatal",
        meaning=SNOMED["118189007"])
    snomed_3950001 = PermissibleValue(
        text="snomed_3950001",
        description="Birth",
        meaning=SNOMED["3950001"])
    snomed_410672004 = PermissibleValue(
        text="snomed_410672004",
        description="Date",
        meaning=SNOMED["410672004"])
    snomed_261665006 = PermissibleValue(
        text="snomed_261665006",
        description="Unknown",
        meaning=SNOMED["261665006"])

    _defn = EnumDefinition(
        name="AgeAtDiagnosis",
    )

class ClinicalStatus(EnumDefinitionImpl):

    hl7fhir_active = PermissibleValue(
        text="hl7fhir_active",
        description="Active",
        meaning=HL7FHIR["active"])
    hl7fhir_recurrence = PermissibleValue(
        text="hl7fhir_recurrence",
        description="Recurrence",
        meaning=HL7FHIR["recurrence"])
    hl7fhir_relapse = PermissibleValue(
        text="hl7fhir_relapse",
        description="Relapse",
        meaning=HL7FHIR["relapse"])
    hl7fhir_inactive = PermissibleValue(
        text="hl7fhir_inactive",
        description="Inactive",
        meaning=HL7FHIR["inactive"])
    hl7fhir_remission = PermissibleValue(
        text="hl7fhir_remission",
        description="Remission",
        meaning=HL7FHIR["remission"])
    hl7fhir_resolved = PermissibleValue(
        text="hl7fhir_resolved",
        description="Resolved",
        meaning=HL7FHIR["resolved"])

    _defn = EnumDefinition(
        name="ClinicalStatus",
    )

class DiseaseSeverity(EnumDefinitionImpl):

    snomed_24484000 = PermissibleValue(
        text="snomed_24484000",
        description="Severe",
        meaning=SNOMED["24484000"])
    snomed_6736007 = PermissibleValue(
        text="snomed_6736007",
        description="Moderate",
        meaning=SNOMED["6736007"])
    snomed_255604002 = PermissibleValue(
        text="snomed_255604002",
        description="Mild",
        meaning=SNOMED["255604002"])

    _defn = EnumDefinition(
        name="DiseaseSeverity",
    )

class InterpretationProgressStatus(EnumDefinitionImpl):

    ga4gh_unknown_progress = PermissibleValue(
        text="ga4gh_unknown_progress",
        description="No information is available about the diagnosis",
        meaning=GA4GH["unknown_progress"])
    ga4gh_in_progress = PermissibleValue(
        text="ga4gh_in_progress",
        description="Additional differential diagnostic work is in progress",
        meaning=GA4GH["in_progress"])
    ga4gh_completed = PermissibleValue(
        text="ga4gh_completed",
        description="The work on the interpretation is complete",
        meaning=GA4GH["completed"])
    ga4gh_solved = PermissibleValue(
        text="ga4gh_solved",
        description="The interpretation is complete and definitive diagnosis made",
        meaning=GA4GH["solved"])
    ga4gh_unsolved = PermissibleValue(
        text="ga4gh_unsolved",
        description="The interpretation is complete but no definitive diagnosis",
        meaning=GA4GH["unsolved"])

    _defn = EnumDefinition(
        name="InterpretationProgressStatus",
    )

class InterpretationStatus(EnumDefinitionImpl):

    ga4gh_unknown_status = PermissibleValue(
        text="ga4gh_unknown_status",
        description="No information available about the status",
        meaning=GA4GH["unknown_status"])
    ga4gh_rejected = PermissibleValue(
        text="ga4gh_rejected",
        description="Variant not related to the diagnosis",
        meaning=GA4GH["rejected"])
    ga4gh_candidate = PermissibleValue(
        text="ga4gh_candidate",
        description="Variant possibly related to the diagnosis",
        meaning=GA4GH["candidate"])
    ga4gh_contributory = PermissibleValue(
        text="ga4gh_contributory",
        description="Variant related to the diagnosis",
        meaning=GA4GH["contributory"])
    ga4gh_causative = PermissibleValue(
        text="ga4gh_causative",
        description="Variant causative of the diagnosis",
        meaning=GA4GH["causative"])

    _defn = EnumDefinition(
        name="InterpretationStatus",
    )

class StructuralVariantMethod(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="StructuralVariantMethod",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "loinc_la26406-1",
            PermissibleValue(
                text="loinc_la26406-1",
                description="Karyotyping",
                meaning=LOINC["LA26406-1"]))
        setattr(cls, "loinc_la26404-6",
            PermissibleValue(
                text="loinc_la26404-6",
                description="FISH",
                meaning=LOINC["LA26404-6"]))
        setattr(cls, "loinc_la26418-6",
            PermissibleValue(
                text="loinc_la26418-6",
                description="PCR",
                meaning=LOINC["LA26418-6"]))
        setattr(cls, "loinc_la26419-4",
            PermissibleValue(
                text="loinc_la26419-4",
                description="qPCR (real-time PCR)",
                meaning=LOINC["LA26419-4"]))
        setattr(cls, "loinc_la26400-4",
            PermissibleValue(
                text="loinc_la26400-4",
                description="SNP array",
                meaning=LOINC["LA26400-4"]))
        setattr(cls, "loinc_la26813-8",
            PermissibleValue(
                text="loinc_la26813-8",
                description="Restriction fragment length polymorphism (RFLP)",
                meaning=LOINC["LA26813-8"]))
        setattr(cls, "loinc_la26810-4",
            PermissibleValue(
                text="loinc_la26810-4",
                description="DNA hybridization",
                meaning=LOINC["LA26810-4"]))
        setattr(cls, "loinc_la26398-0",
            PermissibleValue(
                text="loinc_la26398-0",
                description="Sequencing",
                meaning=LOINC["LA26398-0"]))
        setattr(cls, "loinc_la26415-2",
            PermissibleValue(
                text="loinc_la26415-2",
                description="MLPA",
                meaning=LOINC["LA26415-2"]))
        setattr(cls, "loinc_la46-8",
            PermissibleValue(
                text="loinc_la46-8",
                description="Other",
                meaning=LOINC["LA46-8"]))

class ReferenceGenome(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="ReferenceGenome",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "loinc_la14032-9",
            PermissibleValue(
                text="loinc_la14032-9",
                description="NCBI Build 34 (hg16)",
                meaning=LOINC["LA14032-9"]))
        setattr(cls, "loinc_la14029-5",
            PermissibleValue(
                text="loinc_la14029-5",
                description="GRCh37 (hg19)",
                meaning=LOINC["LA14029-5"]))
        setattr(cls, "loinc_la14030-3",
            PermissibleValue(
                text="loinc_la14030-3",
                description="NCBI Build 36.1 (hg18)",
                meaning=LOINC["LA14030-3"]))
        setattr(cls, "loinc_la14031-1",
            PermissibleValue(
                text="loinc_la14031-1",
                description="NCBI Build 35 (hg17)",
                meaning=LOINC["LA14031-1"]))
        setattr(cls, "loinc_la26806-2",
            PermissibleValue(
                text="loinc_la26806-2",
                description="GRCh38 (hg38)",
                meaning=LOINC["LA26806-2"]))

class VariantExpressionType(EnumDefinitionImpl):

    ghgvs = PermissibleValue(
        text="ghgvs",
        description="Genomic DNA change [g.HGVS]",
        meaning=RARELINK_CDM["g.HGVS"])
    chgvs = PermissibleValue(
        text="chgvs",
        description="Sequence DNA change [c.HGVS]",
        meaning=RARELINK_CDM["c.HGVS"])
    phgvs = PermissibleValue(
        text="phgvs",
        description="Amino Acid Change [p.HGVS]",
        meaning=RARELINK_CDM["p.HGVS"])

    _defn = EnumDefinition(
        name="VariantExpressionType",
    )

class Zygosity(EnumDefinitionImpl):

    loinc_53034_5_other = PermissibleValue(
        text="loinc_53034_5_other",
        description="Other",
        meaning=LOINC["53034-5"])

    _defn = EnumDefinition(
        name="Zygosity",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "loinc_la6705-3",
            PermissibleValue(
                text="loinc_la6705-3",
                description="Homozygous",
                meaning=LOINC["LA6705-3"]))
        setattr(cls, "loinc_la6706-1",
            PermissibleValue(
                text="loinc_la6706-1",
                description="(simple) Heterozygous",
                meaning=LOINC["LA6706-1"]))
        setattr(cls, "loinc_la26217-2",
            PermissibleValue(
                text="loinc_la26217-2",
                description="Compound heterozygous",
                meaning=LOINC["LA26217-2"]))
        setattr(cls, "loinc_la26220-6",
            PermissibleValue(
                text="loinc_la26220-6",
                description="Double heterozygous",
                meaning=LOINC["LA26220-6"]))
        setattr(cls, "loinc_la6707-9",
            PermissibleValue(
                text="loinc_la6707-9",
                description="Hemizygous",
                meaning=LOINC["LA6707-9"]))
        setattr(cls, "loinc_la6703-8",
            PermissibleValue(
                text="loinc_la6703-8",
                description="Heteroplasmic",
                meaning=LOINC["LA6703-8"]))
        setattr(cls, "loinc_la6704-6",
            PermissibleValue(
                text="loinc_la6704-6",
                description="Homoplasmic",
                meaning=LOINC["LA6704-6"]))

class GenomicSourceClass(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="GenomicSourceClass",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "loinc_la6683-2",
            PermissibleValue(
                text="loinc_la6683-2",
                description="Germline",
                meaning=LOINC["LA6683-2"]))
        setattr(cls, "loinc_la6684-0",
            PermissibleValue(
                text="loinc_la6684-0",
                description="Somatic",
                meaning=LOINC["LA6684-0"]))
        setattr(cls, "loinc_la10429-1",
            PermissibleValue(
                text="loinc_la10429-1",
                description="Fetal",
                meaning=LOINC["LA10429-1"]))
        setattr(cls, "loinc_la18194-3",
            PermissibleValue(
                text="loinc_la18194-3",
                description="Likely germline",
                meaning=LOINC["LA18194-3"]))
        setattr(cls, "loinc_la18195-0",
            PermissibleValue(
                text="loinc_la18195-0",
                description="Likely somatic",
                meaning=LOINC["LA18195-0"]))
        setattr(cls, "loinc_la18196-8",
            PermissibleValue(
                text="loinc_la18196-8",
                description="Likely fetal",
                meaning=LOINC["LA18196-8"]))
        setattr(cls, "loinc_la18197-6",
            PermissibleValue(
                text="loinc_la18197-6",
                description="Unknown genomic origin",
                meaning=LOINC["LA18197-6"]))
        setattr(cls, "loinc_la26807-0",
            PermissibleValue(
                text="loinc_la26807-0",
                description="De novo",
                meaning=LOINC["LA26807-0"]))

class DNAChangeType(EnumDefinitionImpl):

    loinc_48019_4_other = PermissibleValue(
        text="loinc_48019_4_other",
        description="Other",
        meaning=LOINC["48019-4"])

    _defn = EnumDefinition(
        name="DNAChangeType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "loinc_la9658-1",
            PermissibleValue(
                text="loinc_la9658-1",
                description="Wild type",
                meaning=LOINC["LA9658-1"]))
        setattr(cls, "loinc_la6692-3",
            PermissibleValue(
                text="loinc_la6692-3",
                description="Deletion",
                meaning=LOINC["LA6692-3"]))
        setattr(cls, "loinc_la6686-5",
            PermissibleValue(
                text="loinc_la6686-5",
                description="Duplication",
                meaning=LOINC["LA6686-5"]))
        setattr(cls, "loinc_la6687-3",
            PermissibleValue(
                text="loinc_la6687-3",
                description="Insertion",
                meaning=LOINC["LA6687-3"]))
        setattr(cls, "loinc_la6688-1",
            PermissibleValue(
                text="loinc_la6688-1",
                description="Insertion/Deletion",
                meaning=LOINC["LA6688-1"]))
        setattr(cls, "loinc_la6689-9",
            PermissibleValue(
                text="loinc_la6689-9",
                description="Inversion",
                meaning=LOINC["LA6689-9"]))
        setattr(cls, "loinc_la6690-7",
            PermissibleValue(
                text="loinc_la6690-7",
                description="Substitution",
                meaning=LOINC["LA6690-7"]))

class ClinicalSignificance(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="ClinicalSignificance",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "loinc_la6668-3",
            PermissibleValue(
                text="loinc_la6668-3",
                description="Pathogenic",
                meaning=LOINC["LA6668-3"]))
        setattr(cls, "loinc_la26332-9",
            PermissibleValue(
                text="loinc_la26332-9",
                description="Likely pathogenic",
                meaning=LOINC["LA26332-9"]))
        setattr(cls, "loinc_la26333-7",
            PermissibleValue(
                text="loinc_la26333-7",
                description="Uncertain significance",
                meaning=LOINC["LA26333-7"]))
        setattr(cls, "loinc_la26334-5",
            PermissibleValue(
                text="loinc_la26334-5",
                description="Likely benign",
                meaning=LOINC["LA26334-5"]))
        setattr(cls, "loinc_la6675-8",
            PermissibleValue(
                text="loinc_la6675-8",
                description="Benign",
                meaning=LOINC["LA6675-8"]))
        setattr(cls, "loinc_la4489-6",
            PermissibleValue(
                text="loinc_la4489-6",
                description="Unknown",
                meaning=LOINC["LA4489-6"]))

class TherapeuticActionability(EnumDefinitionImpl):

    ga4gh_unknown_actionability = PermissibleValue(
        text="ga4gh_unknown_actionability",
        description="No therapeutic actionability available",
        meaning=GA4GH["unknown_actionability"])
    ga4gh_not_actionable = PermissibleValue(
        text="ga4gh_not_actionable",
        description="No therapeutic actionability",
        meaning=GA4GH["not_actionable"])
    ga4gh_actionable = PermissibleValue(
        text="ga4gh_actionable",
        description="Therapeutically actionable",
        meaning=GA4GH["actionable"])

    _defn = EnumDefinition(
        name="TherapeuticActionability",
    )

class LevelOfEvidence(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="LevelOfEvidence",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "loinc_la30200-2",
            PermissibleValue(
                text="loinc_la30200-2",
                description="Very strong evidence pathogenic",
                meaning=LOINC["LA30200-2"]))
        setattr(cls, "loinc_la30201-0",
            PermissibleValue(
                text="loinc_la30201-0",
                description="Strong evidence pathogenic",
                meaning=LOINC["LA30201-0"]))
        setattr(cls, "loinc_la30202-8",
            PermissibleValue(
                text="loinc_la30202-8",
                description="Moderate evidence pathogenic",
                meaning=LOINC["LA30202-8"]))
        setattr(cls, "loinc_la30203-6",
            PermissibleValue(
                text="loinc_la30203-6",
                description="Supporting evidence pathogenic",
                meaning=LOINC["LA30203-6"]))
        setattr(cls, "loinc_la30204-4",
            PermissibleValue(
                text="loinc_la30204-4",
                description="Supporting evidence benign",
                meaning=LOINC["LA30204-4"]))
        setattr(cls, "loinc_la30205-1",
            PermissibleValue(
                text="loinc_la30205-1",
                description="Strong evidence benign",
                meaning=LOINC["LA30205-1"]))
        setattr(cls, "loinc_la30206-9",
            PermissibleValue(
                text="loinc_la30206-9",
                description="Stand-alone evidence pathogenic",
                meaning=LOINC["LA30206-9"]))

class PhenotypicFeatureStatus(EnumDefinitionImpl):

    snomed_410605003 = PermissibleValue(
        text="snomed_410605003",
        description="Confirmed present",
        meaning=SNOMED["410605003"])
    snomed_723511001 = PermissibleValue(
        text="snomed_723511001",
        description="Refuted",
        meaning=SNOMED["723511001"])

    _defn = EnumDefinition(
        name="PhenotypicFeatureStatus",
    )

class AgeOfOnset(EnumDefinitionImpl):

    hp_0011460 = PermissibleValue(
        text="hp_0011460",
        description="Embryonal onset (0w-8w embryonal)",
        meaning=HP["0011460"])
    hp_0011461 = PermissibleValue(
        text="hp_0011461",
        description="Fetal onset (8w embryonal - birth)",
        meaning=HP["0011461"])
    hp_0003577 = PermissibleValue(
        text="hp_0003577",
        description="Congenital onset (at birth)",
        meaning=HP["0003577"])
    hp_0003623 = PermissibleValue(
        text="hp_0003623",
        description="Neonatal onset (0d-28d)",
        meaning=HP["0003623"])
    hp_0003593 = PermissibleValue(
        text="hp_0003593",
        description="Infantile onset (28d-1y)",
        meaning=HP["0003593"])
    hp_0011463 = PermissibleValue(
        text="hp_0011463",
        description="Childhood onset (1y-5y)",
        meaning=HP["0011463"])
    hp_0003621 = PermissibleValue(
        text="hp_0003621",
        description="Juvenile onset (5y-15y)",
        meaning=HP["0003621"])
    hp_0011462 = PermissibleValue(
        text="hp_0011462",
        description="Young adult onset (16y-40y)",
        meaning=HP["0011462"])
    hp_0003596 = PermissibleValue(
        text="hp_0003596",
        description="Middle age adult onset (40y-60y)",
        meaning=HP["0003596"])
    hp_0003584 = PermissibleValue(
        text="hp_0003584",
        description="Late adult onset (60y+)",
        meaning=HP["0003584"])

    _defn = EnumDefinition(
        name="AgeOfOnset",
    )

class TemporalPattern(EnumDefinitionImpl):

    hp_0011009 = PermissibleValue(
        text="hp_0011009",
        description="Acute",
        meaning=HP["0011009"])
    hp_0011010 = PermissibleValue(
        text="hp_0011010",
        description="Chronic",
        meaning=HP["0011010"])
    hp_0031914 = PermissibleValue(
        text="hp_0031914",
        description="Fluctuating",
        meaning=HP["0031914"])
    hp_0025297 = PermissibleValue(
        text="hp_0025297",
        description="Prolonged",
        meaning=HP["0025297"])
    hp_0031796 = PermissibleValue(
        text="hp_0031796",
        description="Recurrent",
        meaning=HP["0031796"])
    hp_0031915 = PermissibleValue(
        text="hp_0031915",
        description="Stable",
        meaning=HP["0031915"])
    hp_0011011 = PermissibleValue(
        text="hp_0011011",
        description="Subacute",
        meaning=HP["0011011"])
    hp_0025153 = PermissibleValue(
        text="hp_0025153",
        description="Transient",
        meaning=HP["0025153"])

    _defn = EnumDefinition(
        name="TemporalPattern",
    )

class PhenotypeSeverity(EnumDefinitionImpl):

    hp_0012827 = PermissibleValue(
        text="hp_0012827",
        description="Borderline",
        meaning=HP["0012827"])
    hp_0012825 = PermissibleValue(
        text="hp_0012825",
        description="Mild",
        meaning=HP["0012825"])
    hp_0012826 = PermissibleValue(
        text="hp_0012826",
        description="Moderate",
        meaning=HP["0012826"])
    hp_0012829 = PermissibleValue(
        text="hp_0012829",
        description="Profound",
        meaning=HP["0012829"])
    hp_0012828 = PermissibleValue(
        text="hp_0012828",
        description="Severe",
        meaning=HP["0012828"])

    _defn = EnumDefinition(
        name="PhenotypeSeverity",
    )

class PropositusStatus(EnumDefinitionImpl):
    """
    Indicates whether the individual is the first affected family member who seeks medical attention.
    """
    snomed_373066001 = PermissibleValue(
        text="snomed_373066001",
        description="True",
        meaning=SNOMED["373066001"])
    snomed_373067005 = PermissibleValue(
        text="snomed_373067005",
        description="False",
        meaning=SNOMED["373067005"])
    snomed_261665006 = PermissibleValue(
        text="snomed_261665006",
        description="Unknown",
        meaning=SNOMED["261665006"])
    snomed_1220561009 = PermissibleValue(
        text="snomed_1220561009",
        description="Not recorded",
        meaning=SNOMED["1220561009"])

    _defn = EnumDefinition(
        name="PropositusStatus",
        description="""Indicates whether the individual is the first affected family member who seeks medical attention.""",
    )

class RelationshipToIndexCase(EnumDefinitionImpl):
    """
    Specifies the relationship of the individual to the index case.
    """
    snomed_65656005 = PermissibleValue(
        text="snomed_65656005",
        description="Natural mother",
        meaning=SNOMED["65656005"])
    snomed_9947008 = PermissibleValue(
        text="snomed_9947008",
        description="Natural father",
        meaning=SNOMED["9947008"])
    snomed_83420006 = PermissibleValue(
        text="snomed_83420006",
        description="Natural daughter",
        meaning=SNOMED["83420006"])
    snomed_113160008 = PermissibleValue(
        text="snomed_113160008",
        description="Natural son",
        meaning=SNOMED["113160008"])
    snomed_60614009 = PermissibleValue(
        text="snomed_60614009",
        description="Natural brother",
        meaning=SNOMED["60614009"])
    snomed_73678001 = PermissibleValue(
        text="snomed_73678001",
        description="Natural sister",
        meaning=SNOMED["73678001"])
    snomed_11286003 = PermissibleValue(
        text="snomed_11286003",
        description="Twin sibling",
        meaning=SNOMED["11286003"])
    snomed_45929001 = PermissibleValue(
        text="snomed_45929001",
        description="Half-brother",
        meaning=SNOMED["45929001"])
    snomed_2272004 = PermissibleValue(
        text="snomed_2272004",
        description="Half-sister",
        meaning=SNOMED["2272004"])
    snomed_62296006 = PermissibleValue(
        text="snomed_62296006",
        description="Natural grandfather",
        meaning=SNOMED["62296006"])
    snomed_17945006 = PermissibleValue(
        text="snomed_17945006",
        description="Natural grandmother",
        meaning=SNOMED["17945006"])
    snomed_1220561009 = PermissibleValue(
        text="snomed_1220561009",
        description="Not recorded",
        meaning=SNOMED["1220561009"])

    _defn = EnumDefinition(
        name="RelationshipToIndexCase",
        description="""Specifies the relationship of the individual to the index case.""",
    )

class FamilyRelationship(EnumDefinitionImpl):
    """
    Specifies the relationship of the selected family member to the patient.
    """
    snomed_65656005 = PermissibleValue(
        text="snomed_65656005",
        description="Natural mother",
        meaning=SNOMED["65656005"])
    snomed_9947008 = PermissibleValue(
        text="snomed_9947008",
        description="Natural father",
        meaning=SNOMED["9947008"])
    snomed_83420006 = PermissibleValue(
        text="snomed_83420006",
        description="Natural daughter",
        meaning=SNOMED["83420006"])
    snomed_113160008 = PermissibleValue(
        text="snomed_113160008",
        description="Natural son",
        meaning=SNOMED["113160008"])
    snomed_60614009 = PermissibleValue(
        text="snomed_60614009",
        description="Natural brother",
        meaning=SNOMED["60614009"])
    snomed_73678001 = PermissibleValue(
        text="snomed_73678001",
        description="Natural sister",
        meaning=SNOMED["73678001"])
    snomed_11286003 = PermissibleValue(
        text="snomed_11286003",
        description="Twin sibling",
        meaning=SNOMED["11286003"])
    snomed_45929001 = PermissibleValue(
        text="snomed_45929001",
        description="Half-brother",
        meaning=SNOMED["45929001"])
    snomed_2272004 = PermissibleValue(
        text="snomed_2272004",
        description="Half-sister",
        meaning=SNOMED["2272004"])
    snomed_62296006 = PermissibleValue(
        text="snomed_62296006",
        description="Natural grandfather",
        meaning=SNOMED["62296006"])
    snomed_17945006 = PermissibleValue(
        text="snomed_17945006",
        description="Natural grandmother",
        meaning=SNOMED["17945006"])
    snomed_1220561009 = PermissibleValue(
        text="snomed_1220561009",
        description="Not recorded",
        meaning=SNOMED["1220561009"])

    _defn = EnumDefinition(
        name="FamilyRelationship",
        description="""Specifies the relationship of the selected family member to the patient.""",
    )

class FamilyRecordStatus(EnumDefinitionImpl):
    """
    Specifies the record’s status of the family history.
    """
    hl7fhir_partial = PermissibleValue(
        text="hl7fhir_partial",
        description="Partial",
        meaning=HL7FHIR["partial"])
    hl7fhir_completed = PermissibleValue(
        text="hl7fhir_completed",
        description="Completed",
        meaning=HL7FHIR["completed"])

    _defn = EnumDefinition(
        name="FamilyRecordStatus",
        description="""Specifies the record’s status of the family history.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "hl7fhir_entered-in-error",
            PermissibleValue(
                text="hl7fhir_entered-in-error",
                description="Entered in Error",
                meaning=HL7FHIR["entered-in-error"]))
        setattr(cls, "hl7fhir_health-unknown",
            PermissibleValue(
                text="hl7fhir_health-unknown",
                description="Health Unknown",
                meaning=HL7FHIR["health-unknown"]))

class FamilyMemberSex(EnumDefinitionImpl):
    """
    Specifies the sex (or gender) of the specific family member.
    """
    snomed_248152002 = PermissibleValue(
        text="snomed_248152002",
        description="Female",
        meaning=SNOMED["248152002"])
    snomed_248153007 = PermissibleValue(
        text="snomed_248153007",
        description="Male",
        meaning=SNOMED["248153007"])
    snomed_184115007 = PermissibleValue(
        text="snomed_184115007",
        description="Patient sex unknown",
        meaning=SNOMED["184115007"])
    snomed_32570691000036108 = PermissibleValue(
        text="snomed_32570691000036108",
        description="Intersex",
        meaning=SNOMED["32570691000036108"])
    snomed_1220561009 = PermissibleValue(
        text="snomed_1220561009",
        description="Not recorded",
        meaning=SNOMED["1220561009"])

    _defn = EnumDefinition(
        name="FamilyMemberSex",
        description="""Specifies the sex (or gender) of the specific family member.""",
    )

class ConsentStatus(EnumDefinitionImpl):
    """
    The status of the consent provided.
    """
    hl7fhir_draft = PermissibleValue(
        text="hl7fhir_draft",
        description="Pending",
        meaning=HL7FHIR["draft"])
    hl7fhir_proposed = PermissibleValue(
        text="hl7fhir_proposed",
        description="Proposed",
        meaning=HL7FHIR["proposed"])
    hl7fhir_active = PermissibleValue(
        text="hl7fhir_active",
        description="Active",
        meaning=HL7FHIR["active"])
    hl7fhir_rejected = PermissibleValue(
        text="hl7fhir_rejected",
        description="Rejected",
        meaning=HL7FHIR["rejected"])
    hl7fhir_inactive = PermissibleValue(
        text="hl7fhir_inactive",
        description="Inactive",
        meaning=HL7FHIR["inactive"])

    _defn = EnumDefinition(
        name="ConsentStatus",
        description="""The status of the consent provided.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "hl7fhir_entered-in-error",
            PermissibleValue(
                text="hl7fhir_entered-in-error",
                description="Entered in Error",
                meaning=HL7FHIR["entered-in-error"]))

class YesNoUnknown(EnumDefinitionImpl):
    """
    Indicates yes, no, or unknown status.
    """
    snomed_373066001 = PermissibleValue(
        text="snomed_373066001",
        description="True",
        meaning=SNOMED["373066001"])
    snomed_373067005 = PermissibleValue(
        text="snomed_373067005",
        description="False",
        meaning=SNOMED["373067005"])
    snomed_261665006 = PermissibleValue(
        text="snomed_261665006",
        description="Unknown",
        meaning=SNOMED["261665006"])

    _defn = EnumDefinition(
        name="YesNoUnknown",
        description="""Indicates yes, no, or unknown status.""",
    )

# Slots
class slots:
    pass

slots.record_id = Slot(uri=RARELINK_CDM.record_id, name="record_id", curie=RARELINK_CDM.curie('record_id'),
                   model_uri=RARELINK_CDM.record_id, domain=None, range=URIRef)

slots.formal_criteria = Slot(uri=RARELINK_CDM.formal_criteria, name="formal_criteria", curie=RARELINK_CDM.curie('formal_criteria'),
                   model_uri=RARELINK_CDM.formal_criteria, domain=None, range=Optional[Union[dict, FormalCriteria]])

slots.personal_information = Slot(uri=RARELINK_CDM.personal_information, name="personal_information", curie=RARELINK_CDM.curie('personal_information'),
                   model_uri=RARELINK_CDM.personal_information, domain=None, range=Optional[Union[dict, PersonalInformation]])

slots.repeated_elements = Slot(uri=RARELINK_CDM.repeated_elements, name="repeated_elements", curie=RARELINK_CDM.curie('repeated_elements'),
                   model_uri=RARELINK_CDM.repeated_elements, domain=None, range=Optional[Union[Union[dict, RepeatedElement], List[Union[dict, RepeatedElement]]]])

slots.consent = Slot(uri=RARELINK_CDM.consent, name="consent", curie=RARELINK_CDM.curie('consent'),
                   model_uri=RARELINK_CDM.consent, domain=None, range=Optional[Union[dict, Consent]])

slots.disability = Slot(uri=RARELINK_CDM.disability, name="disability", curie=RARELINK_CDM.curie('disability'),
                   model_uri=RARELINK_CDM.disability, domain=None, range=Optional[Union[dict, Disability]])

slots.redcap_repeat_instrument = Slot(uri=RARELINK.redcap_repeat_instrument, name="redcap_repeat_instrument", curie=RARELINK.curie('redcap_repeat_instrument'),
                   model_uri=RARELINK_CDM.redcap_repeat_instrument, domain=None, range=Optional[str])

slots.redcap_repeat_instance = Slot(uri=RARELINK.redcap_repeat_instance, name="redcap_repeat_instance", curie=RARELINK.curie('redcap_repeat_instance'),
                   model_uri=RARELINK_CDM.redcap_repeat_instance, domain=None, range=Optional[int])

slots.patient_status = Slot(uri=RARELINK.patient_status, name="patient_status", curie=RARELINK.curie('patient_status'),
                   model_uri=RARELINK_CDM.patient_status, domain=None, range=Optional[Union[dict, PatientStatus]])

slots.care_pathway = Slot(uri=RARELINK.care_pathway, name="care_pathway", curie=RARELINK.curie('care_pathway'),
                   model_uri=RARELINK_CDM.care_pathway, domain=None, range=Optional[Union[dict, CarePathway]])

slots.disease = Slot(uri=RARELINK.disease, name="disease", curie=RARELINK.curie('disease'),
                   model_uri=RARELINK_CDM.disease, domain=None, range=Optional[Union[dict, Disease]])

slots.genetic_findings = Slot(uri=RARELINK.genetic_findings, name="genetic_findings", curie=RARELINK.curie('genetic_findings'),
                   model_uri=RARELINK_CDM.genetic_findings, domain=None, range=Optional[Union[dict, GeneticFindings]])

slots.phenotypic_feature = Slot(uri=RARELINK.phenotypic_feature, name="phenotypic_feature", curie=RARELINK.curie('phenotypic_feature'),
                   model_uri=RARELINK_CDM.phenotypic_feature, domain=None, range=Optional[Union[dict, PhenotypicFeature]])

slots.measruements = Slot(uri=RARELINK.measruements, name="measruements", curie=RARELINK.curie('measruements'),
                   model_uri=RARELINK_CDM.measruements, domain=None, range=Optional[Union[dict, Measurement]])

slots.family_history = Slot(uri=RARELINK.family_history, name="family_history", curie=RARELINK.curie('family_history'),
                   model_uri=RARELINK_CDM.family_history, domain=None, range=Optional[Union[dict, FamilyHistory]])

slots.snomed_422549004 = Slot(uri=RARELINK.snomed_422549004, name="snomed_422549004", curie=RARELINK.curie('snomed_422549004'),
                   model_uri=RARELINK_CDM.snomed_422549004, domain=None, range=URIRef)

slots.snomed_399423000 = Slot(uri=RARELINK.snomed_399423000, name="snomed_399423000", curie=RARELINK.curie('snomed_399423000'),
                   model_uri=RARELINK_CDM.snomed_399423000, domain=None, range=Union[str, XSDDate])

slots.rarelink_1_formal_criteria_complete = Slot(uri=RARELINK.rarelink_1_formal_criteria_complete, name="rarelink_1_formal_criteria_complete", curie=RARELINK.curie('rarelink_1_formal_criteria_complete'),
                   model_uri=RARELINK_CDM.rarelink_1_formal_criteria_complete, domain=None, range=Optional[str])

slots.snomed_184099003 = Slot(uri=RARELINK.snomed_184099003, name="snomed_184099003", curie=RARELINK.curie('snomed_184099003'),
                   model_uri=RARELINK_CDM.snomed_184099003, domain=None, range=Union[str, XSDDate])

slots.snomed_281053000 = Slot(uri=RARELINK.snomed_281053000, name="snomed_281053000", curie=RARELINK.curie('snomed_281053000'),
                   model_uri=RARELINK_CDM.snomed_281053000, domain=None, range=Optional[Union[str, "SexAtBirth"]])

slots.snomed_1296886006 = Slot(uri=RARELINK.snomed_1296886006, name="snomed_1296886006", curie=RARELINK.curie('snomed_1296886006'),
                   model_uri=RARELINK_CDM.snomed_1296886006, domain=None, range=Optional[Union[str, "KaryotypicSex"]])

slots.snomed_263495000 = Slot(uri=RARELINK.snomed_263495000, name="snomed_263495000", curie=RARELINK.curie('snomed_263495000'),
                   model_uri=RARELINK_CDM.snomed_263495000, domain=None, range=Optional[Union[str, "GenderIdentity"]])

slots.snomed_370159000 = Slot(uri=RARELINK.snomed_370159000, name="snomed_370159000", curie=RARELINK.curie('snomed_370159000'),
                   model_uri=RARELINK_CDM.snomed_370159000, domain=None, range=Optional[str])

slots.rarelink_2_personal_information_complete = Slot(uri=RARELINK.rarelink_2_personal_information_complete, name="rarelink_2_personal_information_complete", curie=RARELINK.curie('rarelink_2_personal_information_complete'),
                   model_uri=RARELINK_CDM.rarelink_2_personal_information_complete, domain=None, range=str)

slots.patient_status_date = Slot(uri=RARELINK.patient_status_date, name="patient_status_date", curie=RARELINK.curie('patient_status_date'),
                   model_uri=RARELINK_CDM.patient_status_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.snomed_278844005 = Slot(uri=RARELINK.snomed_278844005, name="snomed_278844005", curie=RARELINK.curie('snomed_278844005'),
                   model_uri=RARELINK_CDM.snomed_278844005, domain=None, range=Optional[Union[str, "ClinicalVitalStatus"]])

slots.snomed_398299004 = Slot(uri=RARELINK.snomed_398299004, name="snomed_398299004", curie=RARELINK.curie('snomed_398299004'),
                   model_uri=RARELINK_CDM.snomed_398299004, domain=None, range=Optional[Union[str, UnionDateString]])

slots.snomed_184305005 = Slot(uri=RARELINK.snomed_184305005, name="snomed_184305005", curie=RARELINK.curie('snomed_184305005'),
                   model_uri=RARELINK_CDM.snomed_184305005, domain=None, range=Optional[str])

slots.snomed_105727008 = Slot(uri=RARELINK.snomed_105727008, name="snomed_105727008", curie=RARELINK.curie('snomed_105727008'),
                   model_uri=RARELINK_CDM.snomed_105727008, domain=None, range=Optional[Union[str, "AgeCategory"]])

slots.snomed_412726003 = Slot(uri=RARELINK.snomed_412726003, name="snomed_412726003", curie=RARELINK.curie('snomed_412726003'),
                   model_uri=RARELINK_CDM.snomed_412726003, domain=None, range=Optional[str])

slots.snomed_723663001 = Slot(uri=RARELINK.snomed_723663001, name="snomed_723663001", curie=RARELINK.curie('snomed_723663001'),
                   model_uri=RARELINK_CDM.snomed_723663001, domain=None, range=Optional[Union[str, "YesNo"]])

slots.rarelink_3_patient_status_complete = Slot(uri=RARELINK.rarelink_3_patient_status_complete, name="rarelink_3_patient_status_complete", curie=RARELINK.curie('rarelink_3_patient_status_complete'),
                   model_uri=RARELINK_CDM.rarelink_3_patient_status_complete, domain=None, range=str)

slots.hl7fhir_enc_period_start = Slot(uri=RARELINK.hl7fhir_enc_period_start, name="hl7fhir_enc_period_start", curie=RARELINK.curie('hl7fhir_enc_period_start'),
                   model_uri=RARELINK_CDM.hl7fhir_enc_period_start, domain=None, range=Optional[Union[str, UnionDateString]])

slots.hl7fhir_enc_period_end = Slot(uri=RARELINK.hl7fhir_enc_period_end, name="hl7fhir_enc_period_end", curie=RARELINK.curie('hl7fhir_enc_period_end'),
                   model_uri=RARELINK_CDM.hl7fhir_enc_period_end, domain=None, range=Optional[Union[str, UnionDateString]])

slots.snomed_305058001 = Slot(uri=RARELINK.snomed_305058001, name="snomed_305058001", curie=RARELINK.curie('snomed_305058001'),
                   model_uri=RARELINK_CDM.snomed_305058001, domain=None, range=Union[str, "EncounterStatus"])

slots.hl7fhir_encounter_class = Slot(uri=RARELINK.hl7fhir_encounter_class, name="hl7fhir_encounter_class", curie=RARELINK.curie('hl7fhir_encounter_class'),
                   model_uri=RARELINK_CDM.hl7fhir_encounter_class, domain=None, range=Union[str, "EncounterClass"])

slots.rarelink_4_care_pathway_complete = Slot(uri=RARELINK.rarelink_4_care_pathway_complete, name="rarelink_4_care_pathway_complete", curie=RARELINK.curie('rarelink_4_care_pathway_complete'),
                   model_uri=RARELINK_CDM.rarelink_4_care_pathway_complete, domain=None, range=str)

slots.disease_coding = Slot(uri=RARELINK.disease_coding, name="disease_coding", curie=RARELINK.curie('disease_coding'),
                   model_uri=RARELINK_CDM.disease_coding, domain=None, range=str)

slots.snomed_64572001_mondo = Slot(uri=RARELINK.snomed_64572001_mondo, name="snomed_64572001_mondo", curie=RARELINK.curie('snomed_64572001_mondo'),
                   model_uri=RARELINK_CDM.snomed_64572001_mondo, domain=None, range=Optional[str])

slots.snomed_64572001_ordo = Slot(uri=RARELINK.snomed_64572001_ordo, name="snomed_64572001_ordo", curie=RARELINK.curie('snomed_64572001_ordo'),
                   model_uri=RARELINK_CDM.snomed_64572001_ordo, domain=None, range=Optional[str])

slots.snomed_64572001_icd10cm = Slot(uri=RARELINK.snomed_64572001_icd10cm, name="snomed_64572001_icd10cm", curie=RARELINK.curie('snomed_64572001_icd10cm'),
                   model_uri=RARELINK_CDM.snomed_64572001_icd10cm, domain=None, range=Optional[str])

slots.snomed_64572001_icd11 = Slot(uri=RARELINK.snomed_64572001_icd11, name="snomed_64572001_icd11", curie=RARELINK.curie('snomed_64572001_icd11'),
                   model_uri=RARELINK_CDM.snomed_64572001_icd11, domain=None, range=Optional[str])

slots.snomed_64572001_omim_p = Slot(uri=RARELINK.snomed_64572001_omim_p, name="snomed_64572001_omim_p", curie=RARELINK.curie('snomed_64572001_omim_p'),
                   model_uri=RARELINK_CDM.snomed_64572001_omim_p, domain=None, range=Optional[str])

slots.loinc_99498_8 = Slot(uri=RARELINK.loinc_99498_8, name="loinc_99498_8", curie=RARELINK.curie('loinc_99498_8'),
                   model_uri=RARELINK_CDM.loinc_99498_8, domain=None, range=Union[str, "VerificationStatus"])

slots.snomed_424850005 = Slot(uri=RARELINK.snomed_424850005, name="snomed_424850005", curie=RARELINK.curie('snomed_424850005'),
                   model_uri=RARELINK_CDM.snomed_424850005, domain=None, range=Optional[Union[str, "AgeCategory"]])

slots.snomed_298059007 = Slot(uri=RARELINK.snomed_298059007, name="snomed_298059007", curie=RARELINK.curie('snomed_298059007'),
                   model_uri=RARELINK_CDM.snomed_298059007, domain=None, range=Optional[Union[str, XSDDate]])

slots.snomed_423493009 = Slot(uri=RARELINK.snomed_423493009, name="snomed_423493009", curie=RARELINK.curie('snomed_423493009'),
                   model_uri=RARELINK_CDM.snomed_423493009, domain=None, range=Optional[Union[str, "AgeCategory"]])

slots.snomed_432213005 = Slot(uri=RARELINK.snomed_432213005, name="snomed_432213005", curie=RARELINK.curie('snomed_432213005'),
                   model_uri=RARELINK_CDM.snomed_432213005, domain=None, range=Optional[Union[str, XSDDate]])

slots.snomed_363698007 = Slot(uri=RARELINK.snomed_363698007, name="snomed_363698007", curie=RARELINK.curie('snomed_363698007'),
                   model_uri=RARELINK_CDM.snomed_363698007, domain=None, range=Optional[str])

slots.snomed_263493007 = Slot(uri=RARELINK.snomed_263493007, name="snomed_263493007", curie=RARELINK.curie('snomed_263493007'),
                   model_uri=RARELINK_CDM.snomed_263493007, domain=None, range=Optional[Union[str, "ClinicalStatus"]])

slots.snomed_246112005 = Slot(uri=RARELINK.snomed_246112005, name="snomed_246112005", curie=RARELINK.curie('snomed_246112005'),
                   model_uri=RARELINK_CDM.snomed_246112005, domain=None, range=Optional[Union[str, "DiseaseSeverity"]])

slots.rarelink_5_disease_complete = Slot(uri=RARELINK.rarelink_5_disease_complete, name="rarelink_5_disease_complete", curie=RARELINK.curie('rarelink_5_disease_complete'),
                   model_uri=RARELINK_CDM.rarelink_5_disease_complete, domain=None, range=str)

slots.genetic_diagnosis_code = Slot(uri=RARELINK.genetic_diagnosis_code, name="genetic_diagnosis_code", curie=RARELINK.curie('genetic_diagnosis_code'),
                   model_uri=RARELINK_CDM.genetic_diagnosis_code, domain=None, range=str)

slots.snomed_106221001_mondo = Slot(uri=RARELINK.snomed_106221001_mondo, name="snomed_106221001_mondo", curie=RARELINK.curie('snomed_106221001_mondo'),
                   model_uri=RARELINK_CDM.snomed_106221001_mondo, domain=None, range=Optional[str])

slots.snomed_106221001_omim_p = Slot(uri=RARELINK.snomed_106221001_omim_p, name="snomed_106221001_omim_p", curie=RARELINK.curie('snomed_106221001_omim_p'),
                   model_uri=RARELINK_CDM.snomed_106221001_omim_p, domain=None, range=Optional[str])

slots.ga4gh_progress_status = Slot(uri=RARELINK.ga4gh_progress_status, name="ga4gh_progress_status", curie=RARELINK.curie('ga4gh_progress_status'),
                   model_uri=RARELINK_CDM.ga4gh_progress_status, domain=None, range=Optional[Union[str, "InterpretationProgressStatus"]])

slots.ga4gh_interp_status = Slot(uri=RARELINK.ga4gh_interp_status, name="ga4gh_interp_status", curie=RARELINK.curie('ga4gh_interp_status'),
                   model_uri=RARELINK_CDM.ga4gh_interp_status, domain=None, range=Optional[Union[str, "InterpretationStatus"]])

slots.loinc_81304_8 = Slot(uri=RARELINK.loinc_81304_8, name="loinc_81304_8", curie=RARELINK.curie('loinc_81304_8'),
                   model_uri=RARELINK_CDM.loinc_81304_8, domain=None, range=Optional[Union[str, "StructuralVariantMethod"]])

slots.loinc_62374_4 = Slot(uri=RARELINK.loinc_62374_4, name="loinc_62374_4", curie=RARELINK.curie('loinc_62374_4'),
                   model_uri=RARELINK_CDM.loinc_62374_4, domain=None, range=Optional[Union[str, "ReferenceGenome"]])

slots.loinc_lp7824_8 = Slot(uri=RARELINK.loinc_lp7824_8, name="loinc_lp7824_8", curie=RARELINK.curie('loinc_lp7824_8'),
                   model_uri=RARELINK_CDM.loinc_lp7824_8, domain=None, range=Optional[str])

slots.variant_expression = Slot(uri=RARELINK.variant_expression, name="variant_expression", curie=RARELINK.curie('variant_expression'),
                   model_uri=RARELINK_CDM.variant_expression, domain=None, range=Optional[Union[str, "VariantExpressionType"]])

slots.loinc_81290_9 = Slot(uri=RARELINK.loinc_81290_9, name="loinc_81290_9", curie=RARELINK.curie('loinc_81290_9'),
                   model_uri=RARELINK_CDM.loinc_81290_9, domain=None, range=Optional[str])

slots.loinc_48004_6 = Slot(uri=RARELINK.loinc_48004_6, name="loinc_48004_6", curie=RARELINK.curie('loinc_48004_6'),
                   model_uri=RARELINK_CDM.loinc_48004_6, domain=None, range=Optional[str])

slots.loinc_48005_3 = Slot(uri=RARELINK.loinc_48005_3, name="loinc_48005_3", curie=RARELINK.curie('loinc_48005_3'),
                   model_uri=RARELINK_CDM.loinc_48005_3, domain=None, range=Optional[str])

slots.variant_validation = Slot(uri=RARELINK.variant_validation, name="variant_validation", curie=RARELINK.curie('variant_validation'),
                   model_uri=RARELINK_CDM.variant_validation, domain=None, range=Optional[Union[str, "YesNo"]])

slots.loinc_48018_6 = Slot(uri=RARELINK.loinc_48018_6, name="loinc_48018_6", curie=RARELINK.curie('loinc_48018_6'),
                   model_uri=RARELINK_CDM.loinc_48018_6, domain=None, range=Optional[str])

slots.loinc_48018_6_label = Slot(uri=RARELINK.loinc_48018_6_label, name="loinc_48018_6_label", curie=RARELINK.curie('loinc_48018_6_label'),
                   model_uri=RARELINK_CDM.loinc_48018_6_label, domain=None, range=Optional[str])

slots.loinc_53034_5 = Slot(uri=RARELINK.loinc_53034_5, name="loinc_53034_5", curie=RARELINK.curie('loinc_53034_5'),
                   model_uri=RARELINK_CDM.loinc_53034_5, domain=None, range=Optional[Union[str, "Zygosity"]])

slots.loinc_53034_5_other = Slot(uri=RARELINK.loinc_53034_5_other, name="loinc_53034_5_other", curie=RARELINK.curie('loinc_53034_5_other'),
                   model_uri=RARELINK_CDM.loinc_53034_5_other, domain=None, range=Optional[str])

slots.loinc_48002_0 = Slot(uri=RARELINK.loinc_48002_0, name="loinc_48002_0", curie=RARELINK.curie('loinc_48002_0'),
                   model_uri=RARELINK_CDM.loinc_48002_0, domain=None, range=Optional[Union[str, "GenomicSourceClass"]])

slots.loinc_48019_4 = Slot(uri=RARELINK.loinc_48019_4, name="loinc_48019_4", curie=RARELINK.curie('loinc_48019_4'),
                   model_uri=RARELINK_CDM.loinc_48019_4, domain=None, range=Optional[Union[str, "DNAChangeType"]])

slots.loinc_48019_4_other = Slot(uri=RARELINK.loinc_48019_4_other, name="loinc_48019_4_other", curie=RARELINK.curie('loinc_48019_4_other'),
                   model_uri=RARELINK_CDM.loinc_48019_4_other, domain=None, range=Optional[str])

slots.loinc_53037_8 = Slot(uri=RARELINK.loinc_53037_8, name="loinc_53037_8", curie=RARELINK.curie('loinc_53037_8'),
                   model_uri=RARELINK_CDM.loinc_53037_8, domain=None, range=Optional[Union[str, "ClinicalSignificance"]])

slots.ga4gh_therap_action = Slot(uri=RARELINK.ga4gh_therap_action, name="ga4gh_therap_action", curie=RARELINK.curie('ga4gh_therap_action'),
                   model_uri=RARELINK_CDM.ga4gh_therap_action, domain=None, range=Optional[Union[str, "TherapeuticActionability"]])

slots.loinc_93044_6 = Slot(uri=RARELINK.loinc_93044_6, name="loinc_93044_6", curie=RARELINK.curie('loinc_93044_6'),
                   model_uri=RARELINK_CDM.loinc_93044_6, domain=None, range=Optional[Union[str, "LevelOfEvidence"]])

slots.rarelink_6_1_genetic_findings_complete = Slot(uri=RARELINK.rarelink_6_1_genetic_findings_complete, name="rarelink_6_1_genetic_findings_complete", curie=RARELINK.curie('rarelink_6_1_genetic_findings_complete'),
                   model_uri=RARELINK_CDM.rarelink_6_1_genetic_findings_complete, domain=None, range=str)

slots.snomed_8116006 = Slot(uri=RARELINK.snomed_8116006, name="snomed_8116006", curie=RARELINK.curie('snomed_8116006'),
                   model_uri=RARELINK_CDM.snomed_8116006, domain=None, range=str)

slots.snomed_363778006 = Slot(uri=RARELINK.snomed_363778006, name="snomed_363778006", curie=RARELINK.curie('snomed_363778006'),
                   model_uri=RARELINK_CDM.snomed_363778006, domain=None, range=Optional[Union[str, "PhenotypicFeatureStatus"]])

slots.snomed_8116006_onset = Slot(uri=RARELINK.snomed_8116006_onset, name="snomed_8116006_onset", curie=RARELINK.curie('snomed_8116006_onset'),
                   model_uri=RARELINK_CDM.snomed_8116006_onset, domain=None, range=Optional[Union[str, XSDDate]])

slots.snomed_8116006_resolution = Slot(uri=RARELINK.snomed_8116006_resolution, name="snomed_8116006_resolution", curie=RARELINK.curie('snomed_8116006_resolution'),
                   model_uri=RARELINK_CDM.snomed_8116006_resolution, domain=None, range=Optional[Union[str, XSDDate]])

slots.hp_0003674 = Slot(uri=RARELINK.hp_0003674, name="hp_0003674", curie=RARELINK.curie('hp_0003674'),
                   model_uri=RARELINK_CDM.hp_0003674, domain=None, range=Optional[Union[str, "AgeOfOnset"]])

slots.hp_0011008 = Slot(uri=RARELINK.hp_0011008, name="hp_0011008", curie=RARELINK.curie('hp_0011008'),
                   model_uri=RARELINK_CDM.hp_0011008, domain=None, range=Optional[Union[str, "TemporalPattern"]])

slots.hp_0012824 = Slot(uri=RARELINK.hp_0012824, name="hp_0012824", curie=RARELINK.curie('hp_0012824'),
                   model_uri=RARELINK_CDM.hp_0012824, domain=None, range=Optional[Union[str, "PhenotypeSeverity"]])

slots.hp_0012823_hp1 = Slot(uri=RARELINK.hp_0012823_hp1, name="hp_0012823_hp1", curie=RARELINK.curie('hp_0012823_hp1'),
                   model_uri=RARELINK_CDM.hp_0012823_hp1, domain=None, range=Optional[str])

slots.hp_0012823_hp2 = Slot(uri=RARELINK.hp_0012823_hp2, name="hp_0012823_hp2", curie=RARELINK.curie('hp_0012823_hp2'),
                   model_uri=RARELINK_CDM.hp_0012823_hp2, domain=None, range=Optional[str])

slots.hp_0012823_hp3 = Slot(uri=RARELINK.hp_0012823_hp3, name="hp_0012823_hp3", curie=RARELINK.curie('hp_0012823_hp3'),
                   model_uri=RARELINK_CDM.hp_0012823_hp3, domain=None, range=Optional[str])

slots.hp_0012823_ncbitaxon = Slot(uri=RARELINK.hp_0012823_ncbitaxon, name="hp_0012823_ncbitaxon", curie=RARELINK.curie('hp_0012823_ncbitaxon'),
                   model_uri=RARELINK_CDM.hp_0012823_ncbitaxon, domain=None, range=Optional[str])

slots.hp_0012823_snomed = Slot(uri=RARELINK.hp_0012823_snomed, name="hp_0012823_snomed", curie=RARELINK.curie('hp_0012823_snomed'),
                   model_uri=RARELINK_CDM.hp_0012823_snomed, domain=None, range=Optional[str])

slots.phenotypicfeature_evidence = Slot(uri=RARELINK.phenotypicfeature_evidence, name="phenotypicfeature_evidence", curie=RARELINK.curie('phenotypicfeature_evidence'),
                   model_uri=RARELINK_CDM.phenotypicfeature_evidence, domain=None, range=Optional[str])

slots.rarelink_6_2_phenotypic_feature_complete = Slot(uri=RARELINK.rarelink_6_2_phenotypic_feature_complete, name="rarelink_6_2_phenotypic_feature_complete", curie=RARELINK.curie('rarelink_6_2_phenotypic_feature_complete'),
                   model_uri=RARELINK_CDM.rarelink_6_2_phenotypic_feature_complete, domain=None, range=str)

slots.assay = Slot(uri=RARELINK.assay, name="assay", curie=RARELINK.curie('assay'),
                   model_uri=RARELINK_CDM.assay, domain=None, range=str)

slots.value = Slot(uri=RARELINK.value, name="value", curie=RARELINK.curie('value'),
                   model_uri=RARELINK_CDM.value, domain=None, range=float)

slots.value_unit = Slot(uri=RARELINK.value_unit, name="value_unit", curie=RARELINK.curie('value_unit'),
                   model_uri=RARELINK_CDM.value_unit, domain=None, range=str)

slots.interpretation = Slot(uri=RARELINK.interpretation, name="interpretation", curie=RARELINK.curie('interpretation'),
                   model_uri=RARELINK_CDM.interpretation, domain=None, range=Optional[str])

slots.time_observed = Slot(uri=RARELINK.time_observed, name="time_observed", curie=RARELINK.curie('time_observed'),
                   model_uri=RARELINK_CDM.time_observed, domain=None, range=Optional[Union[str, XSDDate]])

slots.procedure_ncit = Slot(uri=RARELINK.procedure_ncit, name="procedure_ncit", curie=RARELINK.curie('procedure_ncit'),
                   model_uri=RARELINK_CDM.procedure_ncit, domain=None, range=Optional[str])

slots.procedure_snomed = Slot(uri=RARELINK.procedure_snomed, name="procedure_snomed", curie=RARELINK.curie('procedure_snomed'),
                   model_uri=RARELINK_CDM.procedure_snomed, domain=None, range=Optional[str])

slots.rarelink_6_3_measurements_complete = Slot(uri=RARELINK.rarelink_6_3_measurements_complete, name="rarelink_6_3_measurements_complete", curie=RARELINK.curie('rarelink_6_3_measurements_complete'),
                   model_uri=RARELINK_CDM.rarelink_6_3_measurements_complete, domain=None, range=str)

slots.family_history_pseudonym = Slot(uri=RARELINK.family_history_pseudonym, name="family_history_pseudonym", curie=RARELINK.curie('family_history_pseudonym'),
                   model_uri=RARELINK_CDM.family_history_pseudonym, domain=None, range=Optional[str])

slots.propositus = Slot(uri=RARELINK.propositus, name="propositus", curie=RARELINK.curie('propositus'),
                   model_uri=RARELINK_CDM.propositus, domain=None, range=Optional[Union[str, "PropositusStatus"]])

slots.relationship_to_index_case = Slot(uri=RARELINK.relationship_to_index_case, name="relationship_to_index_case", curie=RARELINK.curie('relationship_to_index_case'),
                   model_uri=RARELINK_CDM.relationship_to_index_case, domain=None, range=Optional[Union[str, "RelationshipToIndexCase"]])

slots.consanguinity = Slot(uri=RARELINK.consanguinity, name="consanguinity", curie=RARELINK.curie('consanguinity'),
                   model_uri=RARELINK_CDM.consanguinity, domain=None, range=Optional[Union[str, "YesNoUnknown"]])

slots.family_member_relationship = Slot(uri=RARELINK.family_member_relationship, name="family_member_relationship", curie=RARELINK.curie('family_member_relationship'),
                   model_uri=RARELINK_CDM.family_member_relationship, domain=None, range=Optional[Union[str, "FamilyRelationship"]])

slots.family_member_record_status = Slot(uri=RARELINK.family_member_record_status, name="family_member_record_status", curie=RARELINK.curie('family_member_record_status'),
                   model_uri=RARELINK_CDM.family_member_record_status, domain=None, range=Optional[Union[str, "FamilyRecordStatus"]])

slots.family_member_sex = Slot(uri=RARELINK.family_member_sex, name="family_member_sex", curie=RARELINK.curie('family_member_sex'),
                   model_uri=RARELINK_CDM.family_member_sex, domain=None, range=Optional[Union[str, "FamilyMemberSex"]])

slots.family_member_age = Slot(uri=RARELINK.family_member_age, name="family_member_age", curie=RARELINK.curie('family_member_age'),
                   model_uri=RARELINK_CDM.family_member_age, domain=None, range=Optional[int])

slots.family_member_dob = Slot(uri=RARELINK.family_member_dob, name="family_member_dob", curie=RARELINK.curie('family_member_dob'),
                   model_uri=RARELINK_CDM.family_member_dob, domain=None, range=Optional[Union[str, XSDDate]])

slots.family_member_deceased = Slot(uri=RARELINK.family_member_deceased, name="family_member_deceased", curie=RARELINK.curie('family_member_deceased'),
                   model_uri=RARELINK_CDM.family_member_deceased, domain=None, range=Optional[Union[str, "YesNoUnknown"]])

slots.family_member_cause_of_death = Slot(uri=RARELINK.family_member_cause_of_death, name="family_member_cause_of_death", curie=RARELINK.curie('family_member_cause_of_death'),
                   model_uri=RARELINK_CDM.family_member_cause_of_death, domain=None, range=Optional[str])

slots.family_member_deceased_age = Slot(uri=RARELINK.family_member_deceased_age, name="family_member_deceased_age", curie=RARELINK.curie('family_member_deceased_age'),
                   model_uri=RARELINK_CDM.family_member_deceased_age, domain=None, range=Optional[int])

slots.family_member_disease = Slot(uri=RARELINK.family_member_disease, name="family_member_disease", curie=RARELINK.curie('family_member_disease'),
                   model_uri=RARELINK_CDM.family_member_disease, domain=None, range=Optional[str])

slots.rarelink_6_4_family_history_complete = Slot(uri=RARELINK.rarelink_6_4_family_history_complete, name="rarelink_6_4_family_history_complete", curie=RARELINK.curie('rarelink_6_4_family_history_complete'),
                   model_uri=RARELINK_CDM.rarelink_6_4_family_history_complete, domain=None, range=Optional[str])

slots.consent_status = Slot(uri=RARELINK.consent_status, name="consent_status", curie=RARELINK.curie('consent_status'),
                   model_uri=RARELINK_CDM.consent_status, domain=None, range=Union[str, "ConsentStatus"])

slots.consent_date = Slot(uri=RARELINK.consent_date, name="consent_date", curie=RARELINK.curie('consent_date'),
                   model_uri=RARELINK_CDM.consent_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.health_policy_monitoring = Slot(uri=RARELINK.health_policy_monitoring, name="health_policy_monitoring", curie=RARELINK.curie('health_policy_monitoring'),
                   model_uri=RARELINK_CDM.health_policy_monitoring, domain=None, range=str)

slots.agreement_to_contact = Slot(uri=RARELINK.agreement_to_contact, name="agreement_to_contact", curie=RARELINK.curie('agreement_to_contact'),
                   model_uri=RARELINK_CDM.agreement_to_contact, domain=None, range=Union[str, "YesNoUnknown"])

slots.consent_to_reuse_data = Slot(uri=RARELINK.consent_to_reuse_data, name="consent_to_reuse_data", curie=RARELINK.curie('consent_to_reuse_data'),
                   model_uri=RARELINK_CDM.consent_to_reuse_data, domain=None, range=Union[str, "YesNoUnknown"])

slots.biological_sample = Slot(uri=RARELINK.biological_sample, name="biological_sample", curie=RARELINK.curie('biological_sample'),
                   model_uri=RARELINK_CDM.biological_sample, domain=None, range=Optional[Union[str, "YesNoUnknown"]])

slots.biobank_link = Slot(uri=RARELINK.biobank_link, name="biobank_link", curie=RARELINK.curie('biobank_link'),
                   model_uri=RARELINK_CDM.biobank_link, domain=None, range=Optional[str])

slots.rarelink_7_consent_complete = Slot(uri=RARELINK.rarelink_7_consent_complete, name="rarelink_7_consent_complete", curie=RARELINK.curie('rarelink_7_consent_complete'),
                   model_uri=RARELINK_CDM.rarelink_7_consent_complete, domain=None, range=str)

slots.icf_score = Slot(uri=RARELINK.icf_score, name="icf_score", curie=RARELINK.curie('icf_score'),
                   model_uri=RARELINK_CDM.icf_score, domain=None, range=str)

slots.rarelink_8_disability_complete = Slot(uri=RARELINK.rarelink_8_disability_complete, name="rarelink_8_disability_complete", curie=RARELINK.curie('rarelink_8_disability_complete'),
                   model_uri=RARELINK_CDM.rarelink_8_disability_complete, domain=None, range=str)

slots.codeSystemsContainer__ncbi_taxon = Slot(uri=RARELINK.ncbi_taxon, name="codeSystemsContainer__ncbi_taxon", curie=RARELINK.curie('ncbi_taxon'),
                   model_uri=RARELINK_CDM.codeSystemsContainer__ncbi_taxon, domain=None, range=Union[str, "NCBITaxon"])

slots.codeSystemsContainer__snomed = Slot(uri=RARELINK.snomed, name="codeSystemsContainer__snomed", curie=RARELINK.curie('snomed'),
                   model_uri=RARELINK_CDM.codeSystemsContainer__snomed, domain=None, range=Union[str, "SNOMED"])

slots.codeSystemsContainer__mondo = Slot(uri=RARELINK.mondo, name="codeSystemsContainer__mondo", curie=RARELINK.curie('mondo'),
                   model_uri=RARELINK_CDM.codeSystemsContainer__mondo, domain=None, range=Union[str, "MONDO"])

slots.codeSystemsContainer__hpo = Slot(uri=RARELINK.hpo, name="codeSystemsContainer__hpo", curie=RARELINK.curie('hpo'),
                   model_uri=RARELINK_CDM.codeSystemsContainer__hpo, domain=None, range=Union[str, "HP"])

slots.codeSystemsContainer__loinc = Slot(uri=RARELINK.loinc, name="codeSystemsContainer__loinc", curie=RARELINK.curie('loinc'),
                   model_uri=RARELINK_CDM.codeSystemsContainer__loinc, domain=None, range=Union[str, "LOINC"])

slots.codeSystemsContainer__omim = Slot(uri=RARELINK.omim, name="codeSystemsContainer__omim", curie=RARELINK.curie('omim'),
                   model_uri=RARELINK_CDM.codeSystemsContainer__omim, domain=None, range=Union[str, "OMIM"])

slots.codeSystemsContainer__orpha = Slot(uri=RARELINK.orpha, name="codeSystemsContainer__orpha", curie=RARELINK.curie('orpha'),
                   model_uri=RARELINK_CDM.codeSystemsContainer__orpha, domain=None, range=Union[str, "ORPHA"])

slots.codeSystemsContainer__ncit = Slot(uri=RARELINK.ncit, name="codeSystemsContainer__ncit", curie=RARELINK.curie('ncit'),
                   model_uri=RARELINK_CDM.codeSystemsContainer__ncit, domain=None, range=Union[str, "NCIT"])

slots.codeSystemsContainer__uo = Slot(uri=RARELINK.uo, name="codeSystemsContainer__uo", curie=RARELINK.curie('uo'),
                   model_uri=RARELINK_CDM.codeSystemsContainer__uo, domain=None, range=Union[str, "UO"])

slots.codeSystemsContainer__hgnc = Slot(uri=RARELINK.hgnc, name="codeSystemsContainer__hgnc", curie=RARELINK.curie('hgnc'),
                   model_uri=RARELINK_CDM.codeSystemsContainer__hgnc, domain=None, range=Union[str, "HGNC"])

slots.codeSystemsContainer__hgvs = Slot(uri=RARELINK.hgvs, name="codeSystemsContainer__hgvs", curie=RARELINK.curie('hgvs'),
                   model_uri=RARELINK_CDM.codeSystemsContainer__hgvs, domain=None, range=Union[str, "HGVS"])

slots.codeSystemsContainer__ga4gh = Slot(uri=RARELINK.ga4gh, name="codeSystemsContainer__ga4gh", curie=RARELINK.curie('ga4gh'),
                   model_uri=RARELINK_CDM.codeSystemsContainer__ga4gh, domain=None, range=Union[str, "GA4GH"])

slots.codeSystemsContainer__hl7fhir = Slot(uri=RARELINK.hl7fhir, name="codeSystemsContainer__hl7fhir", curie=RARELINK.curie('hl7fhir'),
                   model_uri=RARELINK_CDM.codeSystemsContainer__hl7fhir, domain=None, range=Union[str, "HL7FHIR"])

slots.codeSystemsContainer__icd11 = Slot(uri=RARELINK.icd11, name="codeSystemsContainer__icd11", curie=RARELINK.curie('icd11'),
                   model_uri=RARELINK_CDM.codeSystemsContainer__icd11, domain=None, range=Union[str, "ICD11"])

slots.codeSystemsContainer__icd10cm = Slot(uri=RARELINK.icd10cm, name="codeSystemsContainer__icd10cm", curie=RARELINK.curie('icd10cm'),
                   model_uri=RARELINK_CDM.codeSystemsContainer__icd10cm, domain=None, range=Union[str, "ICD10CM"])

slots.codeSystemsContainer__icd10gm = Slot(uri=RARELINK.icd10gm, name="codeSystemsContainer__icd10gm", curie=RARELINK.curie('icd10gm'),
                   model_uri=RARELINK_CDM.codeSystemsContainer__icd10gm, domain=None, range=Union[str, "ICD10GM"])

slots.codeSystemsContainer__so = Slot(uri=RARELINK.so, name="codeSystemsContainer__so", curie=RARELINK.curie('so'),
                   model_uri=RARELINK_CDM.codeSystemsContainer__so, domain=None, range=Union[str, "SO"])

slots.codeSystemsContainer__geno = Slot(uri=RARELINK.geno, name="codeSystemsContainer__geno", curie=RARELINK.curie('geno'),
                   model_uri=RARELINK_CDM.codeSystemsContainer__geno, domain=None, range=Union[str, "GENO"])

slots.codeSystemsContainer__icd9 = Slot(uri=RARELINK.icd9, name="codeSystemsContainer__icd9", curie=RARELINK.curie('icd9'),
                   model_uri=RARELINK_CDM.codeSystemsContainer__icd9, domain=None, range=Union[str, "ICD9"])

slots.codeSystemsContainer__iso3166 = Slot(uri=RARELINK.iso3166, name="codeSystemsContainer__iso3166", curie=RARELINK.curie('iso3166'),
                   model_uri=RARELINK_CDM.codeSystemsContainer__iso3166, domain=None, range=Union[str, "ISO3166"])

slots.codeSystemsContainer__icf = Slot(uri=RARELINK.icf, name="codeSystemsContainer__icf", curie=RARELINK.curie('icf'),
                   model_uri=RARELINK_CDM.codeSystemsContainer__icf, domain=None, range=Union[str, "ICF"])
