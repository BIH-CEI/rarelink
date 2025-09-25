# Auto generated from rarelink_repeated_elements.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-03-02T17:05:38
# Schema: rarelink_repeated_elements
#
# id: https://github.com/BIH-CEI/RareLink/blob/develop/src/rarelink_cdm_linkml/v2_0_4/linkml/rarelink_repeated_elements.yaml
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

from dataclasses import dataclass
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot
)
from rdflib import (
    URIRef
)

from linkml_runtime.linkml_model.types import String
from linkml_runtime.utils.metamodelcore import Bool, XSDDate

metamodel_version = "1.7.0"
version = None


# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RARELINK = CurieNamespace('rarelink', 'https://github.com/BIH-CEI/rarelink/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = RARELINK


# Types
class UnionDateString(String):
    """ A field that allows both dates and empty strings. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "union_date_string"
    type_model_uri = RARELINK.UnionDateString


# Class references



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
    class_model_uri: ClassVar[URIRef] = RARELINK.RepeatedElement

    redcap_repeat_instrument: Optional[str] = None
    redcap_repeat_instance: Optional[int] = None
    patient_status: Optional[Union[dict, "PatientStatus"]] = None
    care_pathway: Optional[Union[dict, "CarePathway"]] = None
    disease: Optional[Union[dict, "Disease"]] = None
    genetic_findings: Optional[Union[dict, "GeneticFindings"]] = None
    phenotypic_feature: Optional[Union[dict, "PhenotypicFeature"]] = None
    measurements: Optional[Union[dict, "Measurement"]] = None
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

        if self.measurements is not None and not isinstance(self.measurements, Measurement):
            self.measurements = Measurement(**as_dict(self.measurements))

        if self.family_history is not None and not isinstance(self.family_history, FamilyHistory):
            self.family_history = FamilyHistory(**as_dict(self.family_history))

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
    class_model_uri: ClassVar[URIRef] = RARELINK.CodeSystemsContainer

    ncbi_taxon: Union[str, "NCBITaxon"] = None
    SNOMEDCT: Union[str, "SNOMEDCT"] = None
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
    iso3166: Union[str, "ISO3166"] = None
    icf: Union[str, "ICF"] = None

@dataclass(repr=False)
class PatientStatus(YAMLRoot):
    """
    The section Patient Status (3) of the RareLink CDM.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RARELINK["PatientStatus"]
    class_class_curie: ClassVar[str] = "rarelink:PatientStatus"
    class_name: ClassVar[str] = "PatientStatus"
    class_model_uri: ClassVar[URIRef] = RARELINK.PatientStatus

    rarelink_3_patient_status_complete: str = None
    patient_status_date: Optional[Union[str, XSDDate]] = None
    snomedct_278844005: Optional[Union[str, "ClinicalVitalStatus"]] = None
    snomedct_398299004: Optional[Union[str, UnionDateString]] = None
    snomedct_184305005: Optional[str] = None
    snomedct_105727008: Optional[Union[str, "AgeCategory"]] = None
    snomedct_412726003: Optional[str] = None
    snomedct_723663001: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.rarelink_3_patient_status_complete):
            self.MissingRequiredField("rarelink_3_patient_status_complete")
        if not isinstance(self.rarelink_3_patient_status_complete, str):
            self.rarelink_3_patient_status_complete = str(self.rarelink_3_patient_status_complete)

        if self.patient_status_date is not None and not isinstance(self.patient_status_date, XSDDate):
            self.patient_status_date = XSDDate(self.patient_status_date)

        if self.snomedct_278844005 is not None and not isinstance(self.snomedct_278844005, ClinicalVitalStatus):
            self.snomedct_278844005 = ClinicalVitalStatus(self.snomedct_278844005)

        if self.snomedct_398299004 is not None and not isinstance(self.snomedct_398299004, UnionDateString):
            self.snomedct_398299004 = UnionDateString(self.snomedct_398299004)

        if self.snomedct_184305005 is not None and not isinstance(self.snomedct_184305005, str):
            self.snomedct_184305005 = str(self.snomedct_184305005)

        if self.snomedct_105727008 is not None and not isinstance(self.snomedct_105727008, AgeCategory):
            self.snomedct_105727008 = AgeCategory(self.snomedct_105727008)

        if self.snomedct_412726003 is not None and not isinstance(self.snomedct_412726003, str):
            self.snomedct_412726003 = str(self.snomedct_412726003)

        if self.snomedct_723663001 is not None and not isinstance(self.snomedct_723663001, Bool):
            self.snomedct_723663001 = Bool(self.snomedct_723663001)

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
    class_model_uri: ClassVar[URIRef] = RARELINK.CarePathway

    snomedct_305058001: Union[str, "EncounterStatus"] = None
    hl7fhir_encounter_class: Union[str, "EncounterClass"] = None
    rarelink_4_care_pathway_complete: str = None
    hl7fhir_enc_period_start: Optional[Union[str, UnionDateString]] = None
    hl7fhir_enc_period_end: Optional[Union[str, UnionDateString]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.snomedct_305058001):
            self.MissingRequiredField("snomedct_305058001")
        if not isinstance(self.snomedct_305058001, EncounterStatus):
            self.snomedct_305058001 = EncounterStatus(self.snomedct_305058001)

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
    class_model_uri: ClassVar[URIRef] = RARELINK.Disease

    disease_coding: Union[str, "DiseaseCodeSystems"] = None
    loinc_99498_8: Union[str, "VerificationStatus"] = None
    rarelink_5_disease_complete: str = None
    snomedct_64572001_mondo: Optional[str] = None
    snomedct_64572001_ordo: Optional[str] = None
    snomedct_64572001_icd10cm: Optional[str] = None
    snomedct_64572001_icd11: Optional[str] = None
    snomedct_64572001_omim_p: Optional[str] = None
    snomedct_424850005: Optional[Union[str, "AgeAtOnset"]] = None
    snomedct_298059007: Optional[Union[str, UnionDateString]] = None
    snomedct_423493009: Optional[Union[str, "AgeAtDiagnosis"]] = None
    snomedct_432213005: Optional[Union[str, UnionDateString]] = None
    snomedct_363698007: Optional[str] = None
    snomedct_263493007: Optional[Union[str, "ClinicalStatus"]] = None
    snomedct_246112005: Optional[Union[str, "DiseaseSeverity"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.disease_coding):
            self.MissingRequiredField("disease_coding")
        if not isinstance(self.disease_coding, DiseaseCodeSystems):
            self.disease_coding = DiseaseCodeSystems(self.disease_coding)

        if self._is_empty(self.loinc_99498_8):
            self.MissingRequiredField("loinc_99498_8")
        if not isinstance(self.loinc_99498_8, VerificationStatus):
            self.loinc_99498_8 = VerificationStatus(self.loinc_99498_8)

        if self._is_empty(self.rarelink_5_disease_complete):
            self.MissingRequiredField("rarelink_5_disease_complete")
        if not isinstance(self.rarelink_5_disease_complete, str):
            self.rarelink_5_disease_complete = str(self.rarelink_5_disease_complete)

        if self.snomedct_64572001_mondo is not None and not isinstance(self.snomedct_64572001_mondo, str):
            self.snomedct_64572001_mondo = str(self.snomedct_64572001_mondo)

        if self.snomedct_64572001_ordo is not None and not isinstance(self.snomedct_64572001_ordo, str):
            self.snomedct_64572001_ordo = str(self.snomedct_64572001_ordo)

        if self.snomedct_64572001_icd10cm is not None and not isinstance(self.snomedct_64572001_icd10cm, str):
            self.snomedct_64572001_icd10cm = str(self.snomedct_64572001_icd10cm)

        if self.snomedct_64572001_icd11 is not None and not isinstance(self.snomedct_64572001_icd11, str):
            self.snomedct_64572001_icd11 = str(self.snomedct_64572001_icd11)

        if self.snomedct_64572001_omim_p is not None and not isinstance(self.snomedct_64572001_omim_p, str):
            self.snomedct_64572001_omim_p = str(self.snomedct_64572001_omim_p)

        if self.snomedct_424850005 is not None and not isinstance(self.snomedct_424850005, AgeAtOnset):
            self.snomedct_424850005 = AgeAtOnset(self.snomedct_424850005)

        if self.snomedct_298059007 is not None and not isinstance(self.snomedct_298059007, UnionDateString):
            self.snomedct_298059007 = UnionDateString(self.snomedct_298059007)

        if self.snomedct_423493009 is not None and not isinstance(self.snomedct_423493009, AgeAtDiagnosis):
            self.snomedct_423493009 = AgeAtDiagnosis(self.snomedct_423493009)

        if self.snomedct_432213005 is not None and not isinstance(self.snomedct_432213005, UnionDateString):
            self.snomedct_432213005 = UnionDateString(self.snomedct_432213005)

        if self.snomedct_363698007 is not None and not isinstance(self.snomedct_363698007, str):
            self.snomedct_363698007 = str(self.snomedct_363698007)

        if self.snomedct_263493007 is not None and not isinstance(self.snomedct_263493007, ClinicalStatus):
            self.snomedct_263493007 = ClinicalStatus(self.snomedct_263493007)

        if self.snomedct_246112005 is not None and not isinstance(self.snomedct_246112005, DiseaseSeverity):
            self.snomedct_246112005 = DiseaseSeverity(self.snomedct_246112005)

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
    class_model_uri: ClassVar[URIRef] = RARELINK.GeneticFindings

    genetic_diagnosis_code: str = None
    rarelink_6_1_genetic_findings_complete: str = None
    snomedct_106221001_mondo: Optional[str] = None
    snomedct_106221001_omim_p: Optional[str] = None
    ga4gh_progress_status: Optional[Union[str, "InterpretationProgressStatus"]] = None
    ga4gh_interp_status: Optional[Union[str, "InterpretationStatus"]] = None
    loinc_81304_8: Optional[Union[str, "StructuralVariantMethod"]] = None
    loinc_81304_8_other: Optional[str] = None
    loinc_62374_4: Optional[Union[str, "ReferenceGenome"]] = None
    loinc_lp7824_8: Optional[str] = None
    variant_expression: Optional[Union[str, "VariantExpressionType"]] = None
    loinc_81290_9: Optional[str] = None
    loinc_48004_6: Optional[str] = None
    loinc_48005_3: Optional[str] = None
    variant_validation: Optional[Union[bool, Bool]] = None
    loinc_48018_6: Optional[str] = None
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

        if self.snomedct_106221001_mondo is not None and not isinstance(self.snomedct_106221001_mondo, str):
            self.snomedct_106221001_mondo = str(self.snomedct_106221001_mondo)

        if self.snomedct_106221001_omim_p is not None and not isinstance(self.snomedct_106221001_omim_p, str):
            self.snomedct_106221001_omim_p = str(self.snomedct_106221001_omim_p)

        if self.ga4gh_progress_status is not None and not isinstance(self.ga4gh_progress_status, InterpretationProgressStatus):
            self.ga4gh_progress_status = InterpretationProgressStatus(self.ga4gh_progress_status)

        if self.ga4gh_interp_status is not None and not isinstance(self.ga4gh_interp_status, InterpretationStatus):
            self.ga4gh_interp_status = InterpretationStatus(self.ga4gh_interp_status)

        if self.loinc_81304_8 is not None and not isinstance(self.loinc_81304_8, StructuralVariantMethod):
            self.loinc_81304_8 = StructuralVariantMethod(self.loinc_81304_8)

        if self.loinc_81304_8_other is not None and not isinstance(self.loinc_81304_8_other, str):
            self.loinc_81304_8_other = str(self.loinc_81304_8_other)

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

        if self.variant_validation is not None and not isinstance(self.variant_validation, Bool):
            self.variant_validation = Bool(self.variant_validation)

        if self.loinc_48018_6 is not None and not isinstance(self.loinc_48018_6, str):
            self.loinc_48018_6 = str(self.loinc_48018_6)

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
    class_model_uri: ClassVar[URIRef] = RARELINK.PhenotypicFeature

    snomedct_8116006: str = None
    rarelink_6_2_phenotypic_feature_complete: str = None
    snomedct_363778006: Optional[Union[str, "PhenotypicFeatureStatus"]] = None
    snomedct_8116006_onset: Optional[Union[str, XSDDate]] = None
    snomedct_8116006_resolut: Optional[Union[str, UnionDateString]] = None
    hp_0003674: Optional[Union[str, "AgeOfOnset"]] = None
    hp_0011008: Optional[Union[str, "TemporalPattern"]] = None
    hp_0012824: Optional[Union[str, "PhenotypeSeverity"]] = None
    hp_0012823_hp1: Optional[str] = None
    hp_0012823_hp2: Optional[str] = None
    hp_0012823_hp3: Optional[str] = None
    hp_0012823_ncbitaxon: Optional[str] = None
    hp_0012823_snomedct: Optional[str] = None
    phenotypicfeature_evidence: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.snomedct_8116006):
            self.MissingRequiredField("snomedct_8116006")
        if not isinstance(self.snomedct_8116006, str):
            self.snomedct_8116006 = str(self.snomedct_8116006)

        if self._is_empty(self.rarelink_6_2_phenotypic_feature_complete):
            self.MissingRequiredField("rarelink_6_2_phenotypic_feature_complete")
        if not isinstance(self.rarelink_6_2_phenotypic_feature_complete, str):
            self.rarelink_6_2_phenotypic_feature_complete = str(self.rarelink_6_2_phenotypic_feature_complete)

        if self.snomedct_363778006 is not None and not isinstance(self.snomedct_363778006, PhenotypicFeatureStatus):
            self.snomedct_363778006 = PhenotypicFeatureStatus(self.snomedct_363778006)

        if self.snomedct_8116006_onset is not None and not isinstance(self.snomedct_8116006_onset, XSDDate):
            self.snomedct_8116006_onset = XSDDate(self.snomedct_8116006_onset)

        if self.snomedct_8116006_resolut is not None and not isinstance(self.snomedct_8116006_resolut, UnionDateString):
            self.snomedct_8116006_resolut = UnionDateString(self.snomedct_8116006_resolut)

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

        if self.hp_0012823_snomedct is not None and not isinstance(self.hp_0012823_snomedct, str):
            self.hp_0012823_snomedct = str(self.hp_0012823_snomedct)

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
    class_model_uri: ClassVar[URIRef] = RARELINK.Measurement

    measurement_category: str = None
    ncit_c60819: str = None
    rarelink_6_3_measurements_complete: str = None
    measurement_status: Optional[str] = None
    ln_85353_1: Optional[str] = None
    ln_85353_1_other: Optional[str] = None
    ncit_c25712: Optional[float] = None
    ncit_c92571: Optional[str] = None
    ncit_c41255: Optional[str] = None
    ncit_c82577: Optional[Union[str, XSDDate]] = None
    snomedct_122869004_ncit: Optional[str] = None
    snomedct_122869004_snomed: Optional[str] = None
    snomedct_122869004: Optional[str] = None
    snomedct_122869004_bdsite: Optional[str] = None
    snomedct_122869004_status: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.measurement_category):
            self.MissingRequiredField("measurement_category")
        if not isinstance(self.measurement_category, str):
            self.measurement_category = str(self.measurement_category)

        if self._is_empty(self.ncit_c60819):
            self.MissingRequiredField("ncit_c60819")
        if not isinstance(self.ncit_c60819, str):
            self.ncit_c60819 = str(self.ncit_c60819)

        if self._is_empty(self.rarelink_6_3_measurements_complete):
            self.MissingRequiredField("rarelink_6_3_measurements_complete")
        if not isinstance(self.rarelink_6_3_measurements_complete, str):
            self.rarelink_6_3_measurements_complete = str(self.rarelink_6_3_measurements_complete)

        if self.measurement_status is not None and not isinstance(self.measurement_status, str):
            self.measurement_status = str(self.measurement_status)

        if self.ln_85353_1 is not None and not isinstance(self.ln_85353_1, str):
            self.ln_85353_1 = str(self.ln_85353_1)

        if self.ln_85353_1_other is not None and not isinstance(self.ln_85353_1_other, str):
            self.ln_85353_1_other = str(self.ln_85353_1_other)

        if self.ncit_c25712 is not None and not isinstance(self.ncit_c25712, float):
            self.ncit_c25712 = float(self.ncit_c25712)

        if self.ncit_c92571 is not None and not isinstance(self.ncit_c92571, str):
            self.ncit_c92571 = str(self.ncit_c92571)

        if self.ncit_c41255 is not None and not isinstance(self.ncit_c41255, str):
            self.ncit_c41255 = str(self.ncit_c41255)

        if self.ncit_c82577 is not None and not isinstance(self.ncit_c82577, XSDDate):
            self.ncit_c82577 = XSDDate(self.ncit_c82577)

        if self.snomedct_122869004_ncit is not None and not isinstance(self.snomedct_122869004_ncit, str):
            self.snomedct_122869004_ncit = str(self.snomedct_122869004_ncit)

        if self.snomedct_122869004_snomed is not None and not isinstance(self.snomedct_122869004_snomed, str):
            self.snomedct_122869004_snomed = str(self.snomedct_122869004_snomed)

        if self.snomedct_122869004 is not None and not isinstance(self.snomedct_122869004, str):
            self.snomedct_122869004 = str(self.snomedct_122869004)

        if self.snomedct_122869004_bdsite is not None and not isinstance(self.snomedct_122869004_bdsite, str):
            self.snomedct_122869004_bdsite = str(self.snomedct_122869004_bdsite)

        if self.snomedct_122869004_status is not None and not isinstance(self.snomedct_122869004_status, str):
            self.snomedct_122869004_status = str(self.snomedct_122869004_status)

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
    class_model_uri: ClassVar[URIRef] = RARELINK.FamilyHistory

    family_history_pseudonym: Optional[str] = None
    snomedct_64245008: Optional[str] = None
    snomedct_408732007: Optional[str] = None
    snomedct_842009: Optional[str] = None
    snomedct_444018008: Optional[str] = None
    hl7fhir_fmh_status: Optional[str] = None
    loinc_54123_5: Optional[str] = None
    loinc_54141_7: Optional[int] = None
    loinc_54124_3: Optional[Union[str, XSDDate]] = None
    snomedct_740604001: Optional[str] = None
    loinc_54112_8: Optional[str] = None
    loinc_92662_6: Optional[int] = None
    loinc_75315_2: Optional[str] = None
    rarelink_6_4_family_history_complete: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.family_history_pseudonym is not None and not isinstance(self.family_history_pseudonym, str):
            self.family_history_pseudonym = str(self.family_history_pseudonym)

        if self.snomedct_64245008 is not None and not isinstance(self.snomedct_64245008, str):
            self.snomedct_64245008 = str(self.snomedct_64245008)

        if self.snomedct_408732007 is not None and not isinstance(self.snomedct_408732007, str):
            self.snomedct_408732007 = str(self.snomedct_408732007)

        if self.snomedct_842009 is not None and not isinstance(self.snomedct_842009, str):
            self.snomedct_842009 = str(self.snomedct_842009)

        if self.snomedct_444018008 is not None and not isinstance(self.snomedct_444018008, str):
            self.snomedct_444018008 = str(self.snomedct_444018008)

        if self.hl7fhir_fmh_status is not None and not isinstance(self.hl7fhir_fmh_status, str):
            self.hl7fhir_fmh_status = str(self.hl7fhir_fmh_status)

        if self.loinc_54123_5 is not None and not isinstance(self.loinc_54123_5, str):
            self.loinc_54123_5 = str(self.loinc_54123_5)

        if self.loinc_54141_7 is not None and not isinstance(self.loinc_54141_7, int):
            self.loinc_54141_7 = int(self.loinc_54141_7)

        if self.loinc_54124_3 is not None and not isinstance(self.loinc_54124_3, XSDDate):
            self.loinc_54124_3 = XSDDate(self.loinc_54124_3)

        if self.snomedct_740604001 is not None and not isinstance(self.snomedct_740604001, str):
            self.snomedct_740604001 = str(self.snomedct_740604001)

        if self.loinc_54112_8 is not None and not isinstance(self.loinc_54112_8, str):
            self.loinc_54112_8 = str(self.loinc_54112_8)

        if self.loinc_92662_6 is not None and not isinstance(self.loinc_92662_6, int):
            self.loinc_92662_6 = int(self.loinc_92662_6)

        if self.loinc_75315_2 is not None and not isinstance(self.loinc_75315_2, str):
            self.loinc_75315_2 = str(self.loinc_75315_2)

        if self.rarelink_6_4_family_history_complete is not None and not isinstance(self.rarelink_6_4_family_history_complete, str):
            self.rarelink_6_4_family_history_complete = str(self.rarelink_6_4_family_history_complete)

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

class SNOMEDCT(EnumDefinitionImpl):
    """
    SNOMED CT
    """
    _defn = EnumDefinition(
        name="SNOMEDCT",
        description="SNOMED CT",
        code_set_version="SNOMEDCT_US_2024_09_01",
    )

class MONDO(EnumDefinitionImpl):
    """
    Monarch Disease Ontology
    """
    _defn = EnumDefinition(
        name="MONDO",
        description="Monarch Disease Ontology",
        code_set_version="2025-06-03",
    )

class HP(EnumDefinitionImpl):
    """
    Human Phenotype Ontology
    """
    _defn = EnumDefinition(
        name="HP",
        description="Human Phenotype Ontology",
        code_set_version="2025-05-06",
    )

class LOINC(EnumDefinitionImpl):
    """
    Logical Observation Identifiers Names and Codes
    """
    _defn = EnumDefinition(
        name="LOINC",
        description="Logical Observation Identifiers Names and Codes",
        code_set_version="LNC278",
    )

class OMIM(EnumDefinitionImpl):
    """
    Online Mendelian Inheritance
    """
    _defn = EnumDefinition(
        name="OMIM",
        description="Online Mendelian Inheritance",
        code_set_version="OMIM2024_08_09",
    )

class ORPHA(EnumDefinitionImpl):
    """
    Orphanet Rare Disease Ontology
    """
    _defn = EnumDefinition(
        name="ORPHA",
        description="Orphanet Rare Disease Ontology",
        code_set_version="OMIM2024_08_09",
    )

class NCIT(EnumDefinitionImpl):
    """
    NCI Thesaurus OBO Edition
    """
    _defn = EnumDefinition(
        name="NCIT",
        description="NCI Thesaurus OBO Edition",
        code_set_version="24.01e",
    )

class UO(EnumDefinitionImpl):
    """
    Units of Measurement Ontology
    """
    _defn = EnumDefinition(
        name="UO",
        description="Units of Measurement Ontology",
        code_set_version="OMIM2024_08_09",
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
        code_set_version="SNOMEDCT_US_2024_09_01",
    )

class ICD10CM(EnumDefinitionImpl):
    """
    International Classification of Diseases, Tenth Revision, Clinical Modification
    """
    _defn = EnumDefinition(
        name="ICD10CM",
        description="International Classification of Diseases, Tenth Revision, Clinical Modification",
        code_set_version="SNOMEDCT_US_2024_09_01",
    )

class ICD10GM(EnumDefinitionImpl):
    """
    International Classification of Diseases, Tenth Revision, German Modification
    """
    _defn = EnumDefinition(
        name="ICD10GM",
        description="International Classification of Diseases, Tenth Revision, German Modification",
        code_set_version="SNOMEDCT_US_2024_09_01",
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

class ClinicalVitalStatus(EnumDefinitionImpl):

    snomedct_438949009 = PermissibleValue(
        text="snomedct_438949009",
        description="Alive",
        meaning=SNOMEDCT["438949009"])
    snomedct_419099009 = PermissibleValue(
        text="snomedct_419099009",
        description="Dead",
        meaning=SNOMEDCT["419099009"])
    snomedct_399307001 = PermissibleValue(
        text="snomedct_399307001",
        description="Unknown - Lost in follow-up",
        meaning=SNOMEDCT["399307001"])
    snomedct_185924006 = PermissibleValue(
        text="snomedct_185924006",
        description="Unknown - Opted-out",
        meaning=SNOMEDCT["185924006"])
    snomedct_261665006 = PermissibleValue(
        text="snomedct_261665006",
        description="Unknown - Other Reason",
        meaning=SNOMEDCT["261665006"])

    _defn = EnumDefinition(
        name="ClinicalVitalStatus",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

class AgeCategory(EnumDefinitionImpl):

    snomedct_3658006 = PermissibleValue(
        text="snomedct_3658006",
        description="Infancy",
        meaning=SNOMEDCT["3658006"])
    snomedct_713153009 = PermissibleValue(
        text="snomedct_713153009",
        description="Toddler",
        meaning=SNOMEDCT["713153009"])
    snomedct_255398004 = PermissibleValue(
        text="snomedct_255398004",
        description="Childhood",
        meaning=SNOMEDCT["255398004"])
    snomedct_263659003 = PermissibleValue(
        text="snomedct_263659003",
        description="Adolescence",
        meaning=SNOMEDCT["263659003"])
    snomedct_41847000 = PermissibleValue(
        text="snomedct_41847000",
        description="Adulthood",
        meaning=SNOMEDCT["41847000"])
    snomedct_303112003 = PermissibleValue(
        text="snomedct_303112003",
        description="Fetal period",
        meaning=SNOMEDCT["303112003"])
    snomedct_419099009 = PermissibleValue(
        text="snomedct_419099009",
        description="Dead",
        meaning=SNOMEDCT["419099009"])
    snomedct_261665006 = PermissibleValue(
        text="snomedct_261665006",
        description="Unknown",
        meaning=SNOMEDCT["261665006"])

    _defn = EnumDefinition(
        name="AgeCategory",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

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
    snomedct_261665006 = PermissibleValue(
        text="snomedct_261665006",
        description="Unknown",
        meaning=SNOMEDCT["261665006"])

    _defn = EnumDefinition(
        name="EncounterClass",
    )

class DiseaseCodeSystems(EnumDefinitionImpl):

    mondo = PermissibleValue(
        text="mondo",
        description="MONDO",
        meaning=RARELINK["MONDO"])
    ordo = PermissibleValue(
        text="ordo",
        description="ORDO",
        meaning=RARELINK["ORDO"])
    icd10cm = PermissibleValue(
        text="icd10cm",
        description="ICD-10-CM",
        meaning=RARELINK["ICD10CM"])
    icd11 = PermissibleValue(
        text="icd11",
        description="ICD-11",
        meaning=RARELINK["ICD11"])
    omim_p = PermissibleValue(
        text="omim_p",
        description="OMIM",
        meaning=RARELINK["OMIM"])

    _defn = EnumDefinition(
        name="DiseaseCodeSystems",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

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
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

class AgeAtOnset(EnumDefinitionImpl):

    snomedct_118189007 = PermissibleValue(
        text="snomedct_118189007",
        description="Prenatal",
        meaning=SNOMEDCT["118189007"])
    snomedct_3950001 = PermissibleValue(
        text="snomedct_3950001",
        description="Birth",
        meaning=SNOMEDCT["3950001"])
    snomedct_410672004 = PermissibleValue(
        text="snomedct_410672004",
        description="Date",
        meaning=SNOMEDCT["410672004"])
    snomedct_261665006 = PermissibleValue(
        text="snomedct_261665006",
        description="Unknown",
        meaning=SNOMEDCT["261665006"])

    _defn = EnumDefinition(
        name="AgeAtOnset",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

class AgeAtDiagnosis(EnumDefinitionImpl):

    snomedct_118189007 = PermissibleValue(
        text="snomedct_118189007",
        description="Prenatal",
        meaning=SNOMEDCT["118189007"])
    snomedct_3950001 = PermissibleValue(
        text="snomedct_3950001",
        description="Birth",
        meaning=SNOMEDCT["3950001"])
    snomedct_410672004 = PermissibleValue(
        text="snomedct_410672004",
        description="Date",
        meaning=SNOMEDCT["410672004"])
    snomedct_261665006 = PermissibleValue(
        text="snomedct_261665006",
        description="Unknown",
        meaning=SNOMEDCT["261665006"])

    _defn = EnumDefinition(
        name="AgeAtDiagnosis",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

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

    @classmethod
    def _addvals(cls):
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

class DiseaseSeverity(EnumDefinitionImpl):

    snomedct_24484000 = PermissibleValue(
        text="snomedct_24484000",
        description="Severe",
        meaning=SNOMEDCT["24484000"])
    snomedct_6736007 = PermissibleValue(
        text="snomedct_6736007",
        description="Moderate",
        meaning=SNOMEDCT["6736007"])
    snomedct_255604002 = PermissibleValue(
        text="snomedct_255604002",
        description="Mild",
        meaning=SNOMEDCT["255604002"])

    _defn = EnumDefinition(
        name="DiseaseSeverity",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

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

    @classmethod
    def _addvals(cls):
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

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

    @classmethod
    def _addvals(cls):
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

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
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

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
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

class VariantExpressionType(EnumDefinitionImpl):

    ghgvs = PermissibleValue(
        text="ghgvs",
        description="Genomic DNA change [g.HGVS]",
        meaning=RARELINK["g.HGVS"])
    chgvs = PermissibleValue(
        text="chgvs",
        description="Sequence DNA change [c.HGVS]",
        meaning=RARELINK["c.HGVS"])
    phgvs = PermissibleValue(
        text="phgvs",
        description="Amino Acid Change [p.HGVS]",
        meaning=RARELINK["p.HGVS"])

    _defn = EnumDefinition(
        name="VariantExpressionType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

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
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

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
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

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
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

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
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

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

    @classmethod
    def _addvals(cls):
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

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
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

class PhenotypicFeatureStatus(EnumDefinitionImpl):

    snomedct_410605003 = PermissibleValue(
        text="snomedct_410605003",
        description="Confirmed present",
        meaning=SNOMEDCT["410605003"])
    snomedct_723511001 = PermissibleValue(
        text="snomedct_723511001",
        description="Refuted",
        meaning=SNOMEDCT["723511001"])

    _defn = EnumDefinition(
        name="PhenotypicFeatureStatus",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

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

    @classmethod
    def _addvals(cls):
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

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

    @classmethod
    def _addvals(cls):
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

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

    @classmethod
    def _addvals(cls):
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

class PropositusStatus(EnumDefinitionImpl):
    """
    Indicates whether the individual is the first affected family member who seeks medical attention.
    """
    snomedct_373066001 = PermissibleValue(
        text="snomedct_373066001",
        description="True",
        meaning=SNOMEDCT["373066001"])
    snomedct_373067005 = PermissibleValue(
        text="snomedct_373067005",
        description="False",
        meaning=SNOMEDCT["373067005"])
    snomedct_261665006 = PermissibleValue(
        text="snomedct_261665006",
        description="Unknown",
        meaning=SNOMEDCT["261665006"])
    snomedct_1220561009 = PermissibleValue(
        text="snomedct_1220561009",
        description="Not recorded",
        meaning=SNOMEDCT["1220561009"])

    _defn = EnumDefinition(
        name="PropositusStatus",
        description="""Indicates whether the individual is the first affected family member who seeks medical attention.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

class RelationshipToIndexCase(EnumDefinitionImpl):
    """
    Specifies the relationship of the individual to the index case.
    """
    snomedct_65656005 = PermissibleValue(
        text="snomedct_65656005",
        description="Natural mother",
        meaning=SNOMEDCT["65656005"])
    snomedct_9947008 = PermissibleValue(
        text="snomedct_9947008",
        description="Natural father",
        meaning=SNOMEDCT["9947008"])
    snomedct_83420006 = PermissibleValue(
        text="snomedct_83420006",
        description="Natural daughter",
        meaning=SNOMEDCT["83420006"])
    snomedct_113160008 = PermissibleValue(
        text="snomedct_113160008",
        description="Natural son",
        meaning=SNOMEDCT["113160008"])
    snomedct_60614009 = PermissibleValue(
        text="snomedct_60614009",
        description="Natural brother",
        meaning=SNOMEDCT["60614009"])
    snomedct_73678001 = PermissibleValue(
        text="snomedct_73678001",
        description="Natural sister",
        meaning=SNOMEDCT["73678001"])
    snomedct_11286003 = PermissibleValue(
        text="snomedct_11286003",
        description="Twin sibling",
        meaning=SNOMEDCT["11286003"])
    snomedct_45929001 = PermissibleValue(
        text="snomedct_45929001",
        description="Half-brother",
        meaning=SNOMEDCT["45929001"])
    snomedct_2272004 = PermissibleValue(
        text="snomedct_2272004",
        description="Half-sister",
        meaning=SNOMEDCT["2272004"])
    snomedct_62296006 = PermissibleValue(
        text="snomedct_62296006",
        description="Natural grandfather",
        meaning=SNOMEDCT["62296006"])
    snomedct_17945006 = PermissibleValue(
        text="snomedct_17945006",
        description="Natural grandmother",
        meaning=SNOMEDCT["17945006"])
    snomedct_1220561009 = PermissibleValue(
        text="snomedct_1220561009",
        description="Not recorded",
        meaning=SNOMEDCT["1220561009"])

    _defn = EnumDefinition(
        name="RelationshipToIndexCase",
        description="""Specifies the relationship of the individual to the index case.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

class FamilyRelationship(EnumDefinitionImpl):
    """
    Specifies the relationship of the selected family member to the patient.
    """
    snomedct_65656005 = PermissibleValue(
        text="snomedct_65656005",
        description="Natural mother",
        meaning=SNOMEDCT["65656005"])
    snomedct_9947008 = PermissibleValue(
        text="snomedct_9947008",
        description="Natural father",
        meaning=SNOMEDCT["9947008"])
    snomedct_83420006 = PermissibleValue(
        text="snomedct_83420006",
        description="Natural daughter",
        meaning=SNOMEDCT["83420006"])
    snomedct_113160008 = PermissibleValue(
        text="snomedct_113160008",
        description="Natural son",
        meaning=SNOMEDCT["113160008"])
    snomedct_60614009 = PermissibleValue(
        text="snomedct_60614009",
        description="Natural brother",
        meaning=SNOMEDCT["60614009"])
    snomedct_73678001 = PermissibleValue(
        text="snomedct_73678001",
        description="Natural sister",
        meaning=SNOMEDCT["73678001"])
    snomedct_11286003 = PermissibleValue(
        text="snomedct_11286003",
        description="Twin sibling",
        meaning=SNOMEDCT["11286003"])
    snomedct_45929001 = PermissibleValue(
        text="snomedct_45929001",
        description="Half-brother",
        meaning=SNOMEDCT["45929001"])
    snomedct_2272004 = PermissibleValue(
        text="snomedct_2272004",
        description="Half-sister",
        meaning=SNOMEDCT["2272004"])
    snomedct_62296006 = PermissibleValue(
        text="snomedct_62296006",
        description="Natural grandfather",
        meaning=SNOMEDCT["62296006"])
    snomedct_17945006 = PermissibleValue(
        text="snomedct_17945006",
        description="Natural grandmother",
        meaning=SNOMEDCT["17945006"])
    snomedct_1220561009 = PermissibleValue(
        text="snomedct_1220561009",
        description="Not recorded",
        meaning=SNOMEDCT["1220561009"])

    _defn = EnumDefinition(
        name="FamilyRelationship",
        description="""Specifies the relationship of the selected family member to the patient.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

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
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

class FamilyMemberSex(EnumDefinitionImpl):
    """
    Specifies the sex (or gender) of the specific family member.
    """
    snomedct_248152002 = PermissibleValue(
        text="snomedct_248152002",
        description="Female",
        meaning=SNOMEDCT["248152002"])
    snomedct_248153007 = PermissibleValue(
        text="snomedct_248153007",
        description="Male",
        meaning=SNOMEDCT["248153007"])
    snomedct_184115007 = PermissibleValue(
        text="snomedct_184115007",
        description="Patient sex unknown",
        meaning=SNOMEDCT["184115007"])
    snomedct_32570691000036108 = PermissibleValue(
        text="snomedct_32570691000036108",
        description="Intersex",
        meaning=SNOMEDCT["32570691000036108"])
    snomedct_1220561009 = PermissibleValue(
        text="snomedct_1220561009",
        description="Not recorded",
        meaning=SNOMEDCT["1220561009"])

    _defn = EnumDefinition(
        name="FamilyMemberSex",
        description="""Specifies the sex (or gender) of the specific family member.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "",
            PermissibleValue(
                text="",
                description="No value provided"))

# Slots
class slots:
    pass

slots.redcap_repeat_instrument = Slot(uri=RARELINK.redcap_repeat_instrument, name="redcap_repeat_instrument", curie=RARELINK.curie('redcap_repeat_instrument'),
                   model_uri=RARELINK.redcap_repeat_instrument, domain=None, range=Optional[str])

slots.redcap_repeat_instance = Slot(uri=RARELINK.redcap_repeat_instance, name="redcap_repeat_instance", curie=RARELINK.curie('redcap_repeat_instance'),
                   model_uri=RARELINK.redcap_repeat_instance, domain=None, range=Optional[int])

slots.patient_status = Slot(uri=RARELINK.patient_status, name="patient_status", curie=RARELINK.curie('patient_status'),
                   model_uri=RARELINK.patient_status, domain=None, range=Optional[Union[dict, PatientStatus]])

slots.care_pathway = Slot(uri=RARELINK.care_pathway, name="care_pathway", curie=RARELINK.curie('care_pathway'),
                   model_uri=RARELINK.care_pathway, domain=None, range=Optional[Union[dict, CarePathway]])

slots.disease = Slot(uri=RARELINK.disease, name="disease", curie=RARELINK.curie('disease'),
                   model_uri=RARELINK.disease, domain=None, range=Optional[Union[dict, Disease]])

slots.genetic_findings = Slot(uri=RARELINK.genetic_findings, name="genetic_findings", curie=RARELINK.curie('genetic_findings'),
                   model_uri=RARELINK.genetic_findings, domain=None, range=Optional[Union[dict, GeneticFindings]])

slots.phenotypic_feature = Slot(uri=RARELINK.phenotypic_feature, name="phenotypic_feature", curie=RARELINK.curie('phenotypic_feature'),
                   model_uri=RARELINK.phenotypic_feature, domain=None, range=Optional[Union[dict, PhenotypicFeature]])

slots.measurements = Slot(uri=RARELINK.measurements, name="measurements", curie=RARELINK.curie('measurements'),
                   model_uri=RARELINK.measurements, domain=None, range=Optional[Union[dict, Measurement]])

slots.family_history = Slot(uri=RARELINK.family_history, name="family_history", curie=RARELINK.curie('family_history'),
                   model_uri=RARELINK.family_history, domain=None, range=Optional[Union[dict, FamilyHistory]])

slots.patient_status_date = Slot(uri=RARELINK.patient_status_date, name="patient_status_date", curie=RARELINK.curie('patient_status_date'),
                   model_uri=RARELINK.patient_status_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.snomedct_278844005 = Slot(uri=RARELINK.snomedct_278844005, name="snomedct_278844005", curie=RARELINK.curie('snomedct_278844005'),
                   model_uri=RARELINK.snomedct_278844005, domain=None, range=Optional[Union[str, "ClinicalVitalStatus"]])

slots.snomedct_398299004 = Slot(uri=RARELINK.snomedct_398299004, name="snomedct_398299004", curie=RARELINK.curie('snomedct_398299004'),
                   model_uri=RARELINK.snomedct_398299004, domain=None, range=Optional[Union[str, UnionDateString]])

slots.snomedct_184305005 = Slot(uri=RARELINK.snomedct_184305005, name="snomedct_184305005", curie=RARELINK.curie('snomedct_184305005'),
                   model_uri=RARELINK.snomedct_184305005, domain=None, range=Optional[str])

slots.snomedct_105727008 = Slot(uri=RARELINK.snomedct_105727008, name="snomedct_105727008", curie=RARELINK.curie('snomedct_105727008'),
                   model_uri=RARELINK.snomedct_105727008, domain=None, range=Optional[Union[str, "AgeCategory"]])

slots.snomedct_412726003 = Slot(uri=RARELINK.snomedct_412726003, name="snomedct_412726003", curie=RARELINK.curie('snomedct_412726003'),
                   model_uri=RARELINK.snomedct_412726003, domain=None, range=Optional[str])

slots.snomedct_723663001 = Slot(uri=RARELINK.snomedct_723663001, name="snomedct_723663001", curie=RARELINK.curie('snomedct_723663001'),
                   model_uri=RARELINK.snomedct_723663001, domain=None, range=Optional[Union[bool, Bool]])

slots.rarelink_3_patient_status_complete = Slot(uri=RARELINK.rarelink_3_patient_status_complete, name="rarelink_3_patient_status_complete", curie=RARELINK.curie('rarelink_3_patient_status_complete'),
                   model_uri=RARELINK.rarelink_3_patient_status_complete, domain=None, range=str)

slots.hl7fhir_enc_period_start = Slot(uri=RARELINK.hl7fhir_enc_period_start, name="hl7fhir_enc_period_start", curie=RARELINK.curie('hl7fhir_enc_period_start'),
                   model_uri=RARELINK.hl7fhir_enc_period_start, domain=None, range=Optional[Union[str, UnionDateString]])

slots.hl7fhir_enc_period_end = Slot(uri=RARELINK.hl7fhir_enc_period_end, name="hl7fhir_enc_period_end", curie=RARELINK.curie('hl7fhir_enc_period_end'),
                   model_uri=RARELINK.hl7fhir_enc_period_end, domain=None, range=Optional[Union[str, UnionDateString]])

slots.snomedct_305058001 = Slot(uri=RARELINK.snomedct_305058001, name="snomedct_305058001", curie=RARELINK.curie('snomedct_305058001'),
                   model_uri=RARELINK.snomedct_305058001, domain=None, range=Union[str, "EncounterStatus"])

slots.hl7fhir_encounter_class = Slot(uri=RARELINK.hl7fhir_encounter_class, name="hl7fhir_encounter_class", curie=RARELINK.curie('hl7fhir_encounter_class'),
                   model_uri=RARELINK.hl7fhir_encounter_class, domain=None, range=Union[str, "EncounterClass"])

slots.rarelink_4_care_pathway_complete = Slot(uri=RARELINK.rarelink_4_care_pathway_complete, name="rarelink_4_care_pathway_complete", curie=RARELINK.curie('rarelink_4_care_pathway_complete'),
                   model_uri=RARELINK.rarelink_4_care_pathway_complete, domain=None, range=str)

slots.disease_coding = Slot(uri=RARELINK.disease_coding, name="disease_coding", curie=RARELINK.curie('disease_coding'),
                   model_uri=RARELINK.disease_coding, domain=None, range=Union[str, "DiseaseCodeSystems"])

slots.snomedct_64572001_mondo = Slot(uri=RARELINK.snomedct_64572001_mondo, name="snomedct_64572001_mondo", curie=RARELINK.curie('snomedct_64572001_mondo'),
                   model_uri=RARELINK.snomedct_64572001_mondo, domain=None, range=Optional[str])

slots.snomedct_64572001_ordo = Slot(uri=RARELINK.snomedct_64572001_ordo, name="snomedct_64572001_ordo", curie=RARELINK.curie('snomedct_64572001_ordo'),
                   model_uri=RARELINK.snomedct_64572001_ordo, domain=None, range=Optional[str])

slots.snomedct_64572001_icd10cm = Slot(uri=RARELINK.snomedct_64572001_icd10cm, name="snomedct_64572001_icd10cm", curie=RARELINK.curie('snomedct_64572001_icd10cm'),
                   model_uri=RARELINK.snomedct_64572001_icd10cm, domain=None, range=Optional[str])

slots.snomedct_64572001_icd11 = Slot(uri=RARELINK.snomedct_64572001_icd11, name="snomedct_64572001_icd11", curie=RARELINK.curie('snomedct_64572001_icd11'),
                   model_uri=RARELINK.snomedct_64572001_icd11, domain=None, range=Optional[str])

slots.snomedct_64572001_omim_p = Slot(uri=RARELINK.snomedct_64572001_omim_p, name="snomedct_64572001_omim_p", curie=RARELINK.curie('snomedct_64572001_omim_p'),
                   model_uri=RARELINK.snomedct_64572001_omim_p, domain=None, range=Optional[str])

slots.loinc_99498_8 = Slot(uri=RARELINK.loinc_99498_8, name="loinc_99498_8", curie=RARELINK.curie('loinc_99498_8'),
                   model_uri=RARELINK.loinc_99498_8, domain=None, range=Union[str, "VerificationStatus"])

slots.snomedct_424850005 = Slot(uri=RARELINK.snomedct_424850005, name="snomedct_424850005", curie=RARELINK.curie('snomedct_424850005'),
                   model_uri=RARELINK.snomedct_424850005, domain=None, range=Optional[Union[str, "AgeAtOnset"]])

slots.snomedct_298059007 = Slot(uri=RARELINK.snomedct_298059007, name="snomedct_298059007", curie=RARELINK.curie('snomedct_298059007'),
                   model_uri=RARELINK.snomedct_298059007, domain=None, range=Optional[Union[str, UnionDateString]])

slots.snomedct_423493009 = Slot(uri=RARELINK.snomedct_423493009, name="snomedct_423493009", curie=RARELINK.curie('snomedct_423493009'),
                   model_uri=RARELINK.snomedct_423493009, domain=None, range=Optional[Union[str, "AgeAtDiagnosis"]])

slots.snomedct_432213005 = Slot(uri=RARELINK.snomedct_432213005, name="snomedct_432213005", curie=RARELINK.curie('snomedct_432213005'),
                   model_uri=RARELINK.snomedct_432213005, domain=None, range=Optional[Union[str, UnionDateString]])

slots.snomedct_363698007 = Slot(uri=RARELINK.snomedct_363698007, name="snomedct_363698007", curie=RARELINK.curie('snomedct_363698007'),
                   model_uri=RARELINK.snomedct_363698007, domain=None, range=Optional[str])

slots.snomedct_263493007 = Slot(uri=RARELINK.snomedct_263493007, name="snomedct_263493007", curie=RARELINK.curie('snomedct_263493007'),
                   model_uri=RARELINK.snomedct_263493007, domain=None, range=Optional[Union[str, "ClinicalStatus"]])

slots.snomedct_246112005 = Slot(uri=RARELINK.snomedct_246112005, name="snomedct_246112005", curie=RARELINK.curie('snomedct_246112005'),
                   model_uri=RARELINK.snomedct_246112005, domain=None, range=Optional[Union[str, "DiseaseSeverity"]])

slots.rarelink_5_disease_complete = Slot(uri=RARELINK.rarelink_5_disease_complete, name="rarelink_5_disease_complete", curie=RARELINK.curie('rarelink_5_disease_complete'),
                   model_uri=RARELINK.rarelink_5_disease_complete, domain=None, range=str)

slots.genetic_diagnosis_code = Slot(uri=RARELINK.genetic_diagnosis_code, name="genetic_diagnosis_code", curie=RARELINK.curie('genetic_diagnosis_code'),
                   model_uri=RARELINK.genetic_diagnosis_code, domain=None, range=str)

slots.snomedct_106221001_mondo = Slot(uri=RARELINK.snomedct_106221001_mondo, name="snomedct_106221001_mondo", curie=RARELINK.curie('snomedct_106221001_mondo'),
                   model_uri=RARELINK.snomedct_106221001_mondo, domain=None, range=Optional[str])

slots.snomedct_106221001_omim_p = Slot(uri=RARELINK.snomedct_106221001_omim_p, name="snomedct_106221001_omim_p", curie=RARELINK.curie('snomedct_106221001_omim_p'),
                   model_uri=RARELINK.snomedct_106221001_omim_p, domain=None, range=Optional[str])

slots.ga4gh_progress_status = Slot(uri=RARELINK.ga4gh_progress_status, name="ga4gh_progress_status", curie=RARELINK.curie('ga4gh_progress_status'),
                   model_uri=RARELINK.ga4gh_progress_status, domain=None, range=Optional[Union[str, "InterpretationProgressStatus"]])

slots.ga4gh_interp_status = Slot(uri=RARELINK.ga4gh_interp_status, name="ga4gh_interp_status", curie=RARELINK.curie('ga4gh_interp_status'),
                   model_uri=RARELINK.ga4gh_interp_status, domain=None, range=Optional[Union[str, "InterpretationStatus"]])

slots.loinc_81304_8 = Slot(uri=RARELINK.loinc_81304_8, name="loinc_81304_8", curie=RARELINK.curie('loinc_81304_8'),
                   model_uri=RARELINK.loinc_81304_8, domain=None, range=Optional[Union[str, "StructuralVariantMethod"]])

slots.loinc_81304_8_other = Slot(uri=RARELINK.loinc_81304_8_other, name="loinc_81304_8_other", curie=RARELINK.curie('loinc_81304_8_other'),
                   model_uri=RARELINK.loinc_81304_8_other, domain=None, range=Optional[str])

slots.loinc_62374_4 = Slot(uri=RARELINK.loinc_62374_4, name="loinc_62374_4", curie=RARELINK.curie('loinc_62374_4'),
                   model_uri=RARELINK.loinc_62374_4, domain=None, range=Optional[Union[str, "ReferenceGenome"]])

slots.loinc_lp7824_8 = Slot(uri=RARELINK.loinc_lp7824_8, name="loinc_lp7824_8", curie=RARELINK.curie('loinc_lp7824_8'),
                   model_uri=RARELINK.loinc_lp7824_8, domain=None, range=Optional[str])

slots.variant_expression = Slot(uri=RARELINK.variant_expression, name="variant_expression", curie=RARELINK.curie('variant_expression'),
                   model_uri=RARELINK.variant_expression, domain=None, range=Optional[Union[str, "VariantExpressionType"]])

slots.loinc_81290_9 = Slot(uri=RARELINK.loinc_81290_9, name="loinc_81290_9", curie=RARELINK.curie('loinc_81290_9'),
                   model_uri=RARELINK.loinc_81290_9, domain=None, range=Optional[str])

slots.loinc_48004_6 = Slot(uri=RARELINK.loinc_48004_6, name="loinc_48004_6", curie=RARELINK.curie('loinc_48004_6'),
                   model_uri=RARELINK.loinc_48004_6, domain=None, range=Optional[str])

slots.loinc_48005_3 = Slot(uri=RARELINK.loinc_48005_3, name="loinc_48005_3", curie=RARELINK.curie('loinc_48005_3'),
                   model_uri=RARELINK.loinc_48005_3, domain=None, range=Optional[str])

slots.variant_validation = Slot(uri=RARELINK.variant_validation, name="variant_validation", curie=RARELINK.curie('variant_validation'),
                   model_uri=RARELINK.variant_validation, domain=None, range=Optional[Union[bool, Bool]])

slots.loinc_48018_6 = Slot(uri=RARELINK.loinc_48018_6, name="loinc_48018_6", curie=RARELINK.curie('loinc_48018_6'),
                   model_uri=RARELINK.loinc_48018_6, domain=None, range=Optional[str])

slots.loinc_53034_5 = Slot(uri=RARELINK.loinc_53034_5, name="loinc_53034_5", curie=RARELINK.curie('loinc_53034_5'),
                   model_uri=RARELINK.loinc_53034_5, domain=None, range=Optional[Union[str, "Zygosity"]])

slots.loinc_53034_5_other = Slot(uri=RARELINK.loinc_53034_5_other, name="loinc_53034_5_other", curie=RARELINK.curie('loinc_53034_5_other'),
                   model_uri=RARELINK.loinc_53034_5_other, domain=None, range=Optional[str])

slots.loinc_48002_0 = Slot(uri=RARELINK.loinc_48002_0, name="loinc_48002_0", curie=RARELINK.curie('loinc_48002_0'),
                   model_uri=RARELINK.loinc_48002_0, domain=None, range=Optional[Union[str, "GenomicSourceClass"]])

slots.loinc_48019_4 = Slot(uri=RARELINK.loinc_48019_4, name="loinc_48019_4", curie=RARELINK.curie('loinc_48019_4'),
                   model_uri=RARELINK.loinc_48019_4, domain=None, range=Optional[Union[str, "DNAChangeType"]])

slots.loinc_48019_4_other = Slot(uri=RARELINK.loinc_48019_4_other, name="loinc_48019_4_other", curie=RARELINK.curie('loinc_48019_4_other'),
                   model_uri=RARELINK.loinc_48019_4_other, domain=None, range=Optional[str])

slots.loinc_53037_8 = Slot(uri=RARELINK.loinc_53037_8, name="loinc_53037_8", curie=RARELINK.curie('loinc_53037_8'),
                   model_uri=RARELINK.loinc_53037_8, domain=None, range=Optional[Union[str, "ClinicalSignificance"]])

slots.ga4gh_therap_action = Slot(uri=RARELINK.ga4gh_therap_action, name="ga4gh_therap_action", curie=RARELINK.curie('ga4gh_therap_action'),
                   model_uri=RARELINK.ga4gh_therap_action, domain=None, range=Optional[Union[str, "TherapeuticActionability"]])

slots.loinc_93044_6 = Slot(uri=RARELINK.loinc_93044_6, name="loinc_93044_6", curie=RARELINK.curie('loinc_93044_6'),
                   model_uri=RARELINK.loinc_93044_6, domain=None, range=Optional[Union[str, "LevelOfEvidence"]])

slots.rarelink_6_1_genetic_findings_complete = Slot(uri=RARELINK.rarelink_6_1_genetic_findings_complete, name="rarelink_6_1_genetic_findings_complete", curie=RARELINK.curie('rarelink_6_1_genetic_findings_complete'),
                   model_uri=RARELINK.rarelink_6_1_genetic_findings_complete, domain=None, range=str)

slots.snomedct_8116006 = Slot(uri=RARELINK.snomedct_8116006, name="snomedct_8116006", curie=RARELINK.curie('snomedct_8116006'),
                   model_uri=RARELINK.snomedct_8116006, domain=None, range=str)

slots.snomedct_363778006 = Slot(uri=RARELINK.snomedct_363778006, name="snomedct_363778006", curie=RARELINK.curie('snomedct_363778006'),
                   model_uri=RARELINK.snomedct_363778006, domain=None, range=Optional[Union[str, "PhenotypicFeatureStatus"]])

slots.snomedct_8116006_onset = Slot(uri=RARELINK.snomedct_8116006_onset, name="snomedct_8116006_onset", curie=RARELINK.curie('snomedct_8116006_onset'),
                   model_uri=RARELINK.snomedct_8116006_onset, domain=None, range=Optional[Union[str, XSDDate]])

slots.snomedct_8116006_resolut = Slot(uri=RARELINK.snomedct_8116006_resolut, name="snomedct_8116006_resolut", curie=RARELINK.curie('snomedct_8116006_resolut'),
                   model_uri=RARELINK.snomedct_8116006_resolut, domain=None, range=Optional[Union[str, UnionDateString]])

slots.hp_0003674 = Slot(uri=RARELINK.hp_0003674, name="hp_0003674", curie=RARELINK.curie('hp_0003674'),
                   model_uri=RARELINK.hp_0003674, domain=None, range=Optional[Union[str, "AgeOfOnset"]])

slots.hp_0011008 = Slot(uri=RARELINK.hp_0011008, name="hp_0011008", curie=RARELINK.curie('hp_0011008'),
                   model_uri=RARELINK.hp_0011008, domain=None, range=Optional[Union[str, "TemporalPattern"]])

slots.hp_0012824 = Slot(uri=RARELINK.hp_0012824, name="hp_0012824", curie=RARELINK.curie('hp_0012824'),
                   model_uri=RARELINK.hp_0012824, domain=None, range=Optional[Union[str, "PhenotypeSeverity"]])

slots.hp_0012823_hp1 = Slot(uri=RARELINK.hp_0012823_hp1, name="hp_0012823_hp1", curie=RARELINK.curie('hp_0012823_hp1'),
                   model_uri=RARELINK.hp_0012823_hp1, domain=None, range=Optional[str])

slots.hp_0012823_hp2 = Slot(uri=RARELINK.hp_0012823_hp2, name="hp_0012823_hp2", curie=RARELINK.curie('hp_0012823_hp2'),
                   model_uri=RARELINK.hp_0012823_hp2, domain=None, range=Optional[str])

slots.hp_0012823_hp3 = Slot(uri=RARELINK.hp_0012823_hp3, name="hp_0012823_hp3", curie=RARELINK.curie('hp_0012823_hp3'),
                   model_uri=RARELINK.hp_0012823_hp3, domain=None, range=Optional[str])

slots.hp_0012823_ncbitaxon = Slot(uri=RARELINK.hp_0012823_ncbitaxon, name="hp_0012823_ncbitaxon", curie=RARELINK.curie('hp_0012823_ncbitaxon'),
                   model_uri=RARELINK.hp_0012823_ncbitaxon, domain=None, range=Optional[str])

slots.hp_0012823_snomedct = Slot(uri=RARELINK.hp_0012823_snomedct, name="hp_0012823_snomedct", curie=RARELINK.curie('hp_0012823_snomedct'),
                   model_uri=RARELINK.hp_0012823_snomedct, domain=None, range=Optional[str])

slots.phenotypicfeature_evidence = Slot(uri=RARELINK.phenotypicfeature_evidence, name="phenotypicfeature_evidence", curie=RARELINK.curie('phenotypicfeature_evidence'),
                   model_uri=RARELINK.phenotypicfeature_evidence, domain=None, range=Optional[str])

slots.rarelink_6_2_phenotypic_feature_complete = Slot(uri=RARELINK.rarelink_6_2_phenotypic_feature_complete, name="rarelink_6_2_phenotypic_feature_complete", curie=RARELINK.curie('rarelink_6_2_phenotypic_feature_complete'),
                   model_uri=RARELINK.rarelink_6_2_phenotypic_feature_complete, domain=None, range=str)

slots.measurement_category = Slot(uri=RARELINK.measurement_category, name="measurement_category", curie=RARELINK.curie('measurement_category'),
                   model_uri=RARELINK.measurement_category, domain=None, range=str)

slots.measurement_status = Slot(uri=RARELINK.measurement_status, name="measurement_status", curie=RARELINK.curie('measurement_status'),
                   model_uri=RARELINK.measurement_status, domain=None, range=Optional[str])

slots.ncit_c60819 = Slot(uri=RARELINK.ncit_c60819, name="ncit_c60819", curie=RARELINK.curie('ncit_c60819'),
                   model_uri=RARELINK.ncit_c60819, domain=None, range=str)

slots.ln_85353_1 = Slot(uri=RARELINK.ln_85353_1, name="ln_85353_1", curie=RARELINK.curie('ln_85353_1'),
                   model_uri=RARELINK.ln_85353_1, domain=None, range=Optional[str])

slots.ln_85353_1_other = Slot(uri=RARELINK.ln_85353_1_other, name="ln_85353_1_other", curie=RARELINK.curie('ln_85353_1_other'),
                   model_uri=RARELINK.ln_85353_1_other, domain=None, range=Optional[str])

slots.ncit_c25712 = Slot(uri=RARELINK.ncit_c25712, name="ncit_c25712", curie=RARELINK.curie('ncit_c25712'),
                   model_uri=RARELINK.ncit_c25712, domain=None, range=Optional[float])

slots.ncit_c92571 = Slot(uri=RARELINK.ncit_c92571, name="ncit_c92571", curie=RARELINK.curie('ncit_c92571'),
                   model_uri=RARELINK.ncit_c92571, domain=None, range=Optional[str])

slots.ncit_c41255 = Slot(uri=RARELINK.ncit_c41255, name="ncit_c41255", curie=RARELINK.curie('ncit_c41255'),
                   model_uri=RARELINK.ncit_c41255, domain=None, range=Optional[str])

slots.ncit_c82577 = Slot(uri=RARELINK.ncit_c82577, name="ncit_c82577", curie=RARELINK.curie('ncit_c82577'),
                   model_uri=RARELINK.ncit_c82577, domain=None, range=Optional[Union[str, XSDDate]])

slots.snomedct_122869004_ncit = Slot(uri=RARELINK.snomedct_122869004_ncit, name="snomedct_122869004_ncit", curie=RARELINK.curie('snomedct_122869004_ncit'),
                   model_uri=RARELINK.snomedct_122869004_ncit, domain=None, range=Optional[str])

slots.snomedct_122869004_snomed = Slot(uri=RARELINK.snomedct_122869004_snomed, name="snomedct_122869004_snomed", curie=RARELINK.curie('snomedct_122869004_snomed'),
                   model_uri=RARELINK.snomedct_122869004_snomed, domain=None, range=Optional[str])

slots.snomedct_122869004 = Slot(uri=RARELINK.snomedct_122869004, name="snomedct_122869004", curie=RARELINK.curie('snomedct_122869004'),
                   model_uri=RARELINK.snomedct_122869004, domain=None, range=Optional[str])

slots.snomedct_122869004_bdsite = Slot(uri=RARELINK.snomedct_122869004_bdsite, name="snomedct_122869004_bdsite", curie=RARELINK.curie('snomedct_122869004_bdsite'),
                   model_uri=RARELINK.snomedct_122869004_bdsite, domain=None, range=Optional[str])

slots.snomedct_122869004_status = Slot(uri=RARELINK.snomedct_122869004_status, name="snomedct_122869004_status", curie=RARELINK.curie('snomedct_122869004_status'),
                   model_uri=RARELINK.snomedct_122869004_status, domain=None, range=Optional[str])

slots.rarelink_6_3_measurements_complete = Slot(uri=RARELINK.rarelink_6_3_measurements_complete, name="rarelink_6_3_measurements_complete", curie=RARELINK.curie('rarelink_6_3_measurements_complete'),
                   model_uri=RARELINK.rarelink_6_3_measurements_complete, domain=None, range=str)

slots.family_history_pseudonym = Slot(uri=RARELINK.family_history_pseudonym, name="family_history_pseudonym", curie=RARELINK.curie('family_history_pseudonym'),
                   model_uri=RARELINK.family_history_pseudonym, domain=None, range=Optional[str])

slots.snomedct_64245008 = Slot(uri=RARELINK.snomedct_64245008, name="snomedct_64245008", curie=RARELINK.curie('snomedct_64245008'),
                   model_uri=RARELINK.snomedct_64245008, domain=None, range=Optional[str])

slots.snomedct_408732007 = Slot(uri=RARELINK.snomedct_408732007, name="snomedct_408732007", curie=RARELINK.curie('snomedct_408732007'),
                   model_uri=RARELINK.snomedct_408732007, domain=None, range=Optional[str])

slots.snomedct_842009 = Slot(uri=RARELINK.snomedct_842009, name="snomedct_842009", curie=RARELINK.curie('snomedct_842009'),
                   model_uri=RARELINK.snomedct_842009, domain=None, range=Optional[str])

slots.snomedct_444018008 = Slot(uri=RARELINK.snomedct_444018008, name="snomedct_444018008", curie=RARELINK.curie('snomedct_444018008'),
                   model_uri=RARELINK.snomedct_444018008, domain=None, range=Optional[str])

slots.hl7fhir_fmh_status = Slot(uri=RARELINK.hl7fhir_fmh_status, name="hl7fhir_fmh_status", curie=RARELINK.curie('hl7fhir_fmh_status'),
                   model_uri=RARELINK.hl7fhir_fmh_status, domain=None, range=Optional[str])

slots.loinc_54123_5 = Slot(uri=RARELINK.loinc_54123_5, name="loinc_54123_5", curie=RARELINK.curie('loinc_54123_5'),
                   model_uri=RARELINK.loinc_54123_5, domain=None, range=Optional[str])

slots.loinc_54141_7 = Slot(uri=RARELINK.loinc_54141_7, name="loinc_54141_7", curie=RARELINK.curie('loinc_54141_7'),
                   model_uri=RARELINK.loinc_54141_7, domain=None, range=Optional[int])

slots.loinc_54124_3 = Slot(uri=RARELINK.loinc_54124_3, name="loinc_54124_3", curie=RARELINK.curie('loinc_54124_3'),
                   model_uri=RARELINK.loinc_54124_3, domain=None, range=Optional[Union[str, XSDDate]])

slots.snomedct_740604001 = Slot(uri=RARELINK.snomedct_740604001, name="snomedct_740604001", curie=RARELINK.curie('snomedct_740604001'),
                   model_uri=RARELINK.snomedct_740604001, domain=None, range=Optional[str])

slots.loinc_54112_8 = Slot(uri=RARELINK.loinc_54112_8, name="loinc_54112_8", curie=RARELINK.curie('loinc_54112_8'),
                   model_uri=RARELINK.loinc_54112_8, domain=None, range=Optional[str])

slots.loinc_92662_6 = Slot(uri=RARELINK.loinc_92662_6, name="loinc_92662_6", curie=RARELINK.curie('loinc_92662_6'),
                   model_uri=RARELINK.loinc_92662_6, domain=None, range=Optional[int])

slots.loinc_75315_2 = Slot(uri=RARELINK.loinc_75315_2, name="loinc_75315_2", curie=RARELINK.curie('loinc_75315_2'),
                   model_uri=RARELINK.loinc_75315_2, domain=None, range=Optional[str])

slots.rarelink_6_4_family_history_complete = Slot(uri=RARELINK.rarelink_6_4_family_history_complete, name="rarelink_6_4_family_history_complete", curie=RARELINK.curie('rarelink_6_4_family_history_complete'),
                   model_uri=RARELINK.rarelink_6_4_family_history_complete, domain=None, range=Optional[str])

slots.codeSystemsContainer__ncbi_taxon = Slot(uri=RARELINK.ncbi_taxon, name="codeSystemsContainer__ncbi_taxon", curie=RARELINK.curie('ncbi_taxon'),
                   model_uri=RARELINK.codeSystemsContainer__ncbi_taxon, domain=None, range=Union[str, "NCBITaxon"])

slots.codeSystemsContainer__SNOMEDCT = Slot(uri=RARELINK.SNOMEDCT, name="codeSystemsContainer__SNOMEDCT", curie=RARELINK.curie('SNOMEDCT'),
                   model_uri=RARELINK.codeSystemsContainer__SNOMEDCT, domain=None, range=Union[str, "SNOMEDCT"])

slots.codeSystemsContainer__mondo = Slot(uri=RARELINK.mondo, name="codeSystemsContainer__mondo", curie=RARELINK.curie('mondo'),
                   model_uri=RARELINK.codeSystemsContainer__mondo, domain=None, range=Union[str, "MONDO"])

slots.codeSystemsContainer__hpo = Slot(uri=RARELINK.hpo, name="codeSystemsContainer__hpo", curie=RARELINK.curie('hpo'),
                   model_uri=RARELINK.codeSystemsContainer__hpo, domain=None, range=Union[str, "HP"])

slots.codeSystemsContainer__loinc = Slot(uri=RARELINK.loinc, name="codeSystemsContainer__loinc", curie=RARELINK.curie('loinc'),
                   model_uri=RARELINK.codeSystemsContainer__loinc, domain=None, range=Union[str, "LOINC"])

slots.codeSystemsContainer__omim = Slot(uri=RARELINK.omim, name="codeSystemsContainer__omim", curie=RARELINK.curie('omim'),
                   model_uri=RARELINK.codeSystemsContainer__omim, domain=None, range=Union[str, "OMIM"])

slots.codeSystemsContainer__orpha = Slot(uri=RARELINK.orpha, name="codeSystemsContainer__orpha", curie=RARELINK.curie('orpha'),
                   model_uri=RARELINK.codeSystemsContainer__orpha, domain=None, range=Union[str, "ORPHA"])

slots.codeSystemsContainer__ncit = Slot(uri=RARELINK.ncit, name="codeSystemsContainer__ncit", curie=RARELINK.curie('ncit'),
                   model_uri=RARELINK.codeSystemsContainer__ncit, domain=None, range=Union[str, "NCIT"])

slots.codeSystemsContainer__uo = Slot(uri=RARELINK.uo, name="codeSystemsContainer__uo", curie=RARELINK.curie('uo'),
                   model_uri=RARELINK.codeSystemsContainer__uo, domain=None, range=Union[str, "UO"])

slots.codeSystemsContainer__hgnc = Slot(uri=RARELINK.hgnc, name="codeSystemsContainer__hgnc", curie=RARELINK.curie('hgnc'),
                   model_uri=RARELINK.codeSystemsContainer__hgnc, domain=None, range=Union[str, "HGNC"])

slots.codeSystemsContainer__hgvs = Slot(uri=RARELINK.hgvs, name="codeSystemsContainer__hgvs", curie=RARELINK.curie('hgvs'),
                   model_uri=RARELINK.codeSystemsContainer__hgvs, domain=None, range=Union[str, "HGVS"])

slots.codeSystemsContainer__ga4gh = Slot(uri=RARELINK.ga4gh, name="codeSystemsContainer__ga4gh", curie=RARELINK.curie('ga4gh'),
                   model_uri=RARELINK.codeSystemsContainer__ga4gh, domain=None, range=Union[str, "GA4GH"])

slots.codeSystemsContainer__hl7fhir = Slot(uri=RARELINK.hl7fhir, name="codeSystemsContainer__hl7fhir", curie=RARELINK.curie('hl7fhir'),
                   model_uri=RARELINK.codeSystemsContainer__hl7fhir, domain=None, range=Union[str, "HL7FHIR"])

slots.codeSystemsContainer__icd11 = Slot(uri=RARELINK.icd11, name="codeSystemsContainer__icd11", curie=RARELINK.curie('icd11'),
                   model_uri=RARELINK.codeSystemsContainer__icd11, domain=None, range=Union[str, "ICD11"])

slots.codeSystemsContainer__icd10cm = Slot(uri=RARELINK.icd10cm, name="codeSystemsContainer__icd10cm", curie=RARELINK.curie('icd10cm'),
                   model_uri=RARELINK.codeSystemsContainer__icd10cm, domain=None, range=Union[str, "ICD10CM"])

slots.codeSystemsContainer__icd10gm = Slot(uri=RARELINK.icd10gm, name="codeSystemsContainer__icd10gm", curie=RARELINK.curie('icd10gm'),
                   model_uri=RARELINK.codeSystemsContainer__icd10gm, domain=None, range=Union[str, "ICD10GM"])

slots.codeSystemsContainer__so = Slot(uri=RARELINK.so, name="codeSystemsContainer__so", curie=RARELINK.curie('so'),
                   model_uri=RARELINK.codeSystemsContainer__so, domain=None, range=Union[str, "SO"])

slots.codeSystemsContainer__geno = Slot(uri=RARELINK.geno, name="codeSystemsContainer__geno", curie=RARELINK.curie('geno'),
                   model_uri=RARELINK.codeSystemsContainer__geno, domain=None, range=Union[str, "GENO"])

slots.codeSystemsContainer__iso3166 = Slot(uri=RARELINK.iso3166, name="codeSystemsContainer__iso3166", curie=RARELINK.curie('iso3166'),
                   model_uri=RARELINK.codeSystemsContainer__iso3166, domain=None, range=Union[str, "ISO3166"])

slots.codeSystemsContainer__icf = Slot(uri=RARELINK.icf, name="codeSystemsContainer__icf", curie=RARELINK.curie('icf'),
                   model_uri=RARELINK.codeSystemsContainer__icf, domain=None, range=Union[str, "ICF"])
