# Auto generated from form_4_conditions.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-03-22T11:40:57
# Schema: conditions_initial
#
# id: https://github.com/BIH-CEI/cieinr/src/cieinr/v1_0_0/limkml_schemas/form_4_conditions.yaml
# description: Initial conditions form with types, severity, onset dates,  and patterns for Phenopackets export.
#
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
from dataclasses import dataclass
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import YAMLRoot
from rdflib import URIRef

from linkml_runtime.linkml_model.types import Float, Integer, String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
HP = CurieNamespace('HP', 'https://purl.obolibrary.org/obo/HP_')
MONDO = CurieNamespace('MONDO', 'https://purl.obolibrary.org/obo/MONDO_')
NCBITAXON = CurieNamespace('NCBITAXON', 'https://www.ncbi.nlm.nih.gov/taxonomy')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT/')
SNOMEDCT = CurieNamespace('SNOMEDCT', 'http://snomed.info/sct/')
CIEINR = CurieNamespace('cieinr', 'https://github.com/BIH-CEI/cieinr')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CIEINR


# Types
class UnionDateString(String):
    """ A field that allows both dates and empty strings. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "union_date_string"
    type_model_uri = CIEINR.UnionDateString


class AgeInYears(Integer):
    """ Age in completed years """
    type_class_uri = XSD["integer"]
    type_class_curie = "xsd:integer"
    type_name = "age_in_years"
    type_model_uri = CIEINR.AgeInYears


class AgeInMonths(Integer):
    """ Age in completed months """
    type_class_uri = XSD["integer"]
    type_class_curie = "xsd:integer"
    type_name = "age_in_months"
    type_model_uri = CIEINR.AgeInMonths


class Percent(Float):
    """ A percentage value """
    type_class_uri = XSD["float"]
    type_class_curie = "xsd:float"
    type_name = "percent"
    type_model_uri = CIEINR.Percent


class IeiCode(String):
    """ A code for an Inborn Error of Immunity """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "iei_code"
    type_model_uri = CIEINR.IeiCode


class LabValue(Float):
    """ A laboratory measurement value, can be negative in some cases """
    type_class_uri = XSD["float"]
    type_class_curie = "xsd:float"
    type_name = "lab_value"
    type_model_uri = CIEINR.LabValue


class PositiveLabValue(Float):
    """ A laboratory measurement value that cannot be negative """
    type_class_uri = XSD["float"]
    type_class_curie = "xsd:float"
    type_name = "positive_lab_value"
    type_model_uri = CIEINR.PositiveLabValue


class NonNegativeInteger(Integer):
    """ An integer value that cannot be negative """
    type_class_uri = XSD["integer"]
    type_class_curie = "xsd:integer"
    type_name = "non_negative_integer"
    type_model_uri = CIEINR.NonNegativeInteger


class TextOrNull(String):
    """ A text field that can be empty or null """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "text_or_null"
    type_model_uri = CIEINR.TextOrNull


class CodedValue(String):
    """ A coded value from a standardized terminology """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "coded_value"
    type_model_uri = CIEINR.CodedValue


class RedcapCheckbox(String):
    """ REDCap checkbox field (contains checked values as comma-separated list) """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "redcap_checkbox"
    type_model_uri = CIEINR.RedcapCheckbox


class RedcapCompletionStatus(String):
    """ REDCap form completion status """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "redcap_completion_status"
    type_model_uri = CIEINR.RedcapCompletionStatus


class BooleanAsInteger(Integer):
    """ Boolean represented as 0 (false) or 1 (true) """
    type_class_uri = XSD["integer"]
    type_class_curie = "xsd:integer"
    type_name = "boolean_as_integer"
    type_model_uri = CIEINR.BooleanAsInteger


# Class references



@dataclass(repr=False)
class ConditionsInitial(YAMLRoot):
    """
    Initial conditions form with types, severity, onset dates, and patterns for Phenopackets export.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CIEINR["ConditionsInitial"]
    class_class_curie: ClassVar[str] = "cieinr:ConditionsInitial"
    class_name: ClassVar[str] = "ConditionsInitial"
    class_model_uri: ClassVar[URIRef] = CIEINR.ConditionsInitial

    type_of_condition: Optional[Union[str, "ConditionTypeEnum"]] = None
    snomedct_95320005: Optional[Union[str, "SkinConditionEnum"]] = None
    snomedct_118938008: Optional[Union[str, "DentalConditionEnum"]] = None
    snomedct_50043002: Optional[Union[str, "SinoPulmonaryConditionEnum"]] = None
    snomedct_49601007: Optional[Union[str, "CardiovascularConditionEnum"]] = None
    mondo_0005570: Optional[Union[str, "HematologicLymphoidConditionEnum"]] = None
    snomedct_928000: Optional[Union[str, "MusculoskeletalConditionEnum"]] = None
    snomedct_119292006: Optional[Union[str, "GastrointestinalConditionEnum"]] = None
    hp_0002037_evidence: Optional[Union[str, "IBDEvidenceEnum"]] = None
    snomedct_362969004: Optional[Union[str, "EndocrineMetabolicConditionEnum"]] = None
    snomedct_42030000: Optional[Union[str, "GenitourinaryConditionEnum"]] = None
    snomedct_55342001: Optional[Union[str, "NeoplasticConditionEnum"]] = None
    hp_0012539_modifier: Optional[Union[str, "EBVStatusEnum"]] = None
    hp_0012189_modifier: Optional[Union[str, "EBVStatusEnum"]] = None
    hp_0005523_modifier: Optional[Union[str, "EBVStatusEnum"]] = None
    snomedct_85828009: Optional[Union[str, "AutoimmuneConditionEnum"]] = None
    hp_0025142: Optional[Union[str, "ConstitutionalConditionEnum"]] = None
    snomedct_5294002: Optional[Union[str, "GrowthDevelopmentConditionEnum"]] = None
    condition_other_hp: Optional[str] = None
    new_condition: Optional[str] = None
    condition_severity: Optional[Union[str, "ConditionSeverityEnum"]] = None
    condition_temp_pattern: Optional[Union[str, "ConditionTemporalPatternEnum"]] = None
    condition_date: Optional[Union[str, "YesNoEnum"]] = None
    condition_date_1: Optional[Union[str, UnionDateString]] = None
    conditions_initial_form_complete: Optional[Union[str, "CompletionStatusEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.type_of_condition is not None and not isinstance(self.type_of_condition, ConditionTypeEnum):
            self.type_of_condition = ConditionTypeEnum(self.type_of_condition)

        if self.snomedct_95320005 is not None and not isinstance(self.snomedct_95320005, SkinConditionEnum):
            self.snomedct_95320005 = SkinConditionEnum(self.snomedct_95320005)

        if self.snomedct_118938008 is not None and not isinstance(self.snomedct_118938008, DentalConditionEnum):
            self.snomedct_118938008 = DentalConditionEnum(self.snomedct_118938008)

        if self.snomedct_50043002 is not None and not isinstance(self.snomedct_50043002, SinoPulmonaryConditionEnum):
            self.snomedct_50043002 = SinoPulmonaryConditionEnum(self.snomedct_50043002)

        if self.snomedct_49601007 is not None and not isinstance(self.snomedct_49601007, CardiovascularConditionEnum):
            self.snomedct_49601007 = CardiovascularConditionEnum(self.snomedct_49601007)

        if self.mondo_0005570 is not None and not isinstance(self.mondo_0005570, HematologicLymphoidConditionEnum):
            self.mondo_0005570 = HematologicLymphoidConditionEnum(self.mondo_0005570)

        if self.snomedct_928000 is not None and not isinstance(self.snomedct_928000, MusculoskeletalConditionEnum):
            self.snomedct_928000 = MusculoskeletalConditionEnum(self.snomedct_928000)

        if self.snomedct_119292006 is not None and not isinstance(self.snomedct_119292006, GastrointestinalConditionEnum):
            self.snomedct_119292006 = GastrointestinalConditionEnum(self.snomedct_119292006)

        if self.hp_0002037_evidence is not None and not isinstance(self.hp_0002037_evidence, IBDEvidenceEnum):
            self.hp_0002037_evidence = IBDEvidenceEnum(self.hp_0002037_evidence)

        if self.snomedct_362969004 is not None and not isinstance(self.snomedct_362969004, EndocrineMetabolicConditionEnum):
            self.snomedct_362969004 = EndocrineMetabolicConditionEnum(self.snomedct_362969004)

        if self.snomedct_42030000 is not None and not isinstance(self.snomedct_42030000, GenitourinaryConditionEnum):
            self.snomedct_42030000 = GenitourinaryConditionEnum(self.snomedct_42030000)

        if self.snomedct_55342001 is not None and not isinstance(self.snomedct_55342001, NeoplasticConditionEnum):
            self.snomedct_55342001 = NeoplasticConditionEnum(self.snomedct_55342001)

        if self.hp_0012539_modifier is not None and not isinstance(self.hp_0012539_modifier, EBVStatusEnum):
            self.hp_0012539_modifier = EBVStatusEnum(self.hp_0012539_modifier)

        if self.hp_0012189_modifier is not None and not isinstance(self.hp_0012189_modifier, EBVStatusEnum):
            self.hp_0012189_modifier = EBVStatusEnum(self.hp_0012189_modifier)

        if self.hp_0005523_modifier is not None and not isinstance(self.hp_0005523_modifier, EBVStatusEnum):
            self.hp_0005523_modifier = EBVStatusEnum(self.hp_0005523_modifier)

        if self.snomedct_85828009 is not None and not isinstance(self.snomedct_85828009, AutoimmuneConditionEnum):
            self.snomedct_85828009 = AutoimmuneConditionEnum(self.snomedct_85828009)

        if self.hp_0025142 is not None and not isinstance(self.hp_0025142, ConstitutionalConditionEnum):
            self.hp_0025142 = ConstitutionalConditionEnum(self.hp_0025142)

        if self.snomedct_5294002 is not None and not isinstance(self.snomedct_5294002, GrowthDevelopmentConditionEnum):
            self.snomedct_5294002 = GrowthDevelopmentConditionEnum(self.snomedct_5294002)

        if self.condition_other_hp is not None and not isinstance(self.condition_other_hp, str):
            self.condition_other_hp = str(self.condition_other_hp)

        if self.new_condition is not None and not isinstance(self.new_condition, str):
            self.new_condition = str(self.new_condition)

        if self.condition_severity is not None and not isinstance(self.condition_severity, ConditionSeverityEnum):
            self.condition_severity = ConditionSeverityEnum(self.condition_severity)

        if self.condition_temp_pattern is not None and not isinstance(self.condition_temp_pattern, ConditionTemporalPatternEnum):
            self.condition_temp_pattern = ConditionTemporalPatternEnum(self.condition_temp_pattern)

        if self.condition_date is not None and not isinstance(self.condition_date, YesNoEnum):
            self.condition_date = YesNoEnum(self.condition_date)

        if self.condition_date_1 is not None and not isinstance(self.condition_date_1, UnionDateString):
            self.condition_date_1 = UnionDateString(self.condition_date_1)

        if self.conditions_initial_form_complete is not None and not isinstance(self.conditions_initial_form_complete, CompletionStatusEnum):
            self.conditions_initial_form_complete = CompletionStatusEnum(self.conditions_initial_form_complete)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CodeSystemsContainer(YAMLRoot):
    """
    A container class for all code systems used in CIEINR.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CIEINR["CodeSystemsContainer"]
    class_class_curie: ClassVar[str] = "cieinr:CodeSystemsContainer"
    class_name: ClassVar[str] = "CodeSystemsContainer"
    class_model_uri: ClassVar[URIRef] = CIEINR.CodeSystemsContainer

    ncbi_taxon: Union[str, "NCBITaxon"] = None
    snomedct: Union[str, "SNOMEDCT"] = None
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
    bioportal: Union[str, "BIOPORTAL"] = None
    iuis: Union[str, "IUIS"] = None

# Enumerations
class ConditionTypeEnum(EnumDefinitionImpl):
    """
    Types of conditions
    """
    snomedct_95320005 = PermissibleValue(
        text="snomedct_95320005",
        description="Skin Conditions",
        meaning=SNOMEDCT["95320005"])
    snomedct_118938008 = PermissibleValue(
        text="snomedct_118938008",
        description="Dental/Oral Conditions",
        meaning=SNOMEDCT["118938008"])
    snomedct_50043002 = PermissibleValue(
        text="snomedct_50043002",
        description="Sino-Pulmonary Conditions",
        meaning=SNOMEDCT["50043002"])
    snomedct_49601007 = PermissibleValue(
        text="snomedct_49601007",
        description="Cardiovascular Conditions",
        meaning=SNOMEDCT["49601007"])
    mondo_0005570 = PermissibleValue(
        text="mondo_0005570",
        description="Hematologic-Lymphoid Conditions",
        meaning=MONDO["0005570"])
    snomedct_928000 = PermissibleValue(
        text="snomedct_928000",
        description="Musculoskeletal Conditions",
        meaning=SNOMEDCT["928000"])
    snomedct_119292006 = PermissibleValue(
        text="snomedct_119292006",
        description="Gastrointestinal Conditions",
        meaning=SNOMEDCT["119292006"])
    snomedct_362969004 = PermissibleValue(
        text="snomedct_362969004",
        description="Endocrine-Metabolic Conditions",
        meaning=SNOMEDCT["362969004"])
    snomedct_42030000 = PermissibleValue(
        text="snomedct_42030000",
        description="Genitourinary Conditions",
        meaning=SNOMEDCT["42030000"])
    snomedct_55342001 = PermissibleValue(
        text="snomedct_55342001",
        description="Neoplastic Conditions",
        meaning=SNOMEDCT["55342001"])
    snomedct_85828009 = PermissibleValue(
        text="snomedct_85828009",
        description="Autoimmune Conditions",
        meaning=SNOMEDCT["85828009"])
    hp_0025142 = PermissibleValue(
        text="hp_0025142",
        description="Constitutional Conditions",
        meaning=HP["0025142"])
    snomedct_5294002 = PermissibleValue(
        text="snomedct_5294002",
        description="Growth and Development Conditions",
        meaning=SNOMEDCT["5294002"])
    other = PermissibleValue(
        text="other",
        description="Other",
        meaning=CIEINR["other"])

    _defn = EnumDefinition(
        name="ConditionTypeEnum",
        description="Types of conditions",
    )

class SkinConditionEnum(EnumDefinitionImpl):
    """
    Types of skin conditions
    """
    hp_0001595 = PermissibleValue(
        text="hp_0001595",
        description="Abnormal Hair",
        meaning=HP["0001595"])
    hp_0001596 = PermissibleValue(
        text="hp_0001596",
        description="Alopecia",
        meaning=HP["0001596"])
    hp_0000968 = PermissibleValue(
        text="hp_0000968",
        description="Anhydrotic Ectodermal Dysplasia",
        meaning=HP["0000968"])
    hp_0000964 = PermissibleValue(
        text="hp_0000964",
        description="Atopic Dermatitis/Eczema",
        meaning=HP["0000964"])
    hp_0000966 = PermissibleValue(
        text="hp_0000966",
        description="Hypohidrosis / Decreased Sweating",
        meaning=HP["0000966"])
    hp_0032434 = PermissibleValue(
        text="hp_0032434",
        description="Delayed Separation of Umbilical Cord",
        meaning=HP["0032434"])
    hp_0001058 = PermissibleValue(
        text="hp_0001058",
        description="Delayed Wound Healing",
        meaning=HP["0001058"])
    hp_0007417 = PermissibleValue(
        text="hp_0007417",
        description="Discoid Lupus",
        meaning=HP["0007417"])
    hp_0001019 = PermissibleValue(
        text="hp_0001019",
        description="Erythroderma",
        meaning=HP["0001019"])
    hp_0032252 = PermissibleValue(
        text="hp_0032252",
        description="Granulomas",
        meaning=HP["0032252"])
    mondo_0013730 = PermissibleValue(
        text="mondo_0013730",
        description="GVHD or GVHD-like rash",
        meaning=MONDO["0013730"])
    hp_0001597 = PermissibleValue(
        text="hp_0001597",
        description="Nail Defects",
        meaning=HP["0001597"])
    hp_0000989 = PermissibleValue(
        text="hp_0000989",
        description="Pruritis",
        meaning=HP["0000989"])
    hp_0003765 = PermissibleValue(
        text="hp_0003765",
        description="Psoriasis",
        meaning=HP["0003765"])
    hp_0001009 = PermissibleValue(
        text="hp_0001009",
        description="Telangiectasia",
        meaning=HP["0001009"])
    snomedct_95320005_other = PermissibleValue(
        text="snomedct_95320005_other",
        description="Other",
        meaning=SNOMEDCT["95320005_other"])

    _defn = EnumDefinition(
        name="SkinConditionEnum",
        description="Types of skin conditions",
    )

class DentalConditionEnum(EnumDefinitionImpl):
    """
    Types of dental/oral conditions
    """
    hp_0006482 = PermissibleValue(
        text="hp_0006482",
        description="Abnormal Tooth Morphology",
        meaning=HP["0006482"])
    hp_0032154 = PermissibleValue(
        text="hp_0032154",
        description="Apthous Ulcers",
        meaning=HP["0032154"])
    hp_0000670 = PermissibleValue(
        text="hp_0000670",
        description="Caries (excessive)",
        meaning=HP["0000670"])
    hp_0000175 = PermissibleValue(
        text="hp_0000175",
        description="Cleft Palate",
        meaning=HP["0000175"])
    hp_0000698 = PermissibleValue(
        text="hp_0000698",
        description="Cone/Peg Teeth",
        meaning=HP["0000698"])
    hp_0000684 = PermissibleValue(
        text="hp_0000684",
        description="Delayed Eruption of Teeth",
        meaning=HP["0000684"])
    hp_0006335 = PermissibleValue(
        text="hp_0006335",
        description="Delayed Shedding of Teeth",
        meaning=HP["0006335"])
    hp_0000230 = PermissibleValue(
        text="hp_0000230",
        description="Gingivitis",
        meaning=HP["0000230"])
    hp_0000668 = PermissibleValue(
        text="hp_0000668",
        description="Hypodontia",
        meaning=HP["0000668"])
    hp_0000706 = PermissibleValue(
        text="hp_0000706",
        description="Missing Teeth (Eruption failure)",
        meaning=HP["0000706"])
    snomedct_118938008_other = PermissibleValue(
        text="snomedct_118938008_other",
        description="Other",
        meaning=SNOMEDCT["118938008_other"])

    _defn = EnumDefinition(
        name="DentalConditionEnum",
        description="Types of dental/oral conditions",
    )

class SinoPulmonaryConditionEnum(EnumDefinitionImpl):
    """
    Types of sino‐pulmonary conditions
    """
    mondo_0004979 = PermissibleValue(
        text="mondo_0004979",
        description="Asthma",
        meaning=MONDO["0004979"])
    mondo_0005607 = PermissibleValue(
        text="mondo_0005607",
        description="Bronchitis (chronic)",
        meaning=MONDO["0005607"])
    hp_0002110 = PermissibleValue(
        text="hp_0002110",
        description="Bronchiectasis",
        meaning=HP["0002110"])
    hp_0011946 = PermissibleValue(
        text="hp_0011946",
        description="Bronchiolitis Obliterans",
        meaning=HP["0011946"])
    hp_0011945 = PermissibleValue(
        text="hp_0011945",
        description="Bronchiolitis Obliterans Organizing",
        meaning=HP["0011945"])
    hp_0001217 = PermissibleValue(
        text="hp_0001217",
        description="Clubbing",
        meaning=HP["0001217"])
    hp_0006510 = PermissibleValue(
        text="hp_0006510",
        description="COPD",
        meaning=HP["0006510"])
    hp_0002097 = PermissibleValue(
        text="hp_0002097",
        description="Emphysema",
        meaning=HP["0002097"])
    hp_0032252 = PermissibleValue(
        text="hp_0032252",
        description="Granulomas",
        meaning=HP["0032252"])
    hp_0006530 = PermissibleValue(
        text="hp_0006530",
        description="Interstitial Lung Disease",
        meaning=HP["0006530"])
    hp_0002204 = PermissibleValue(
        text="hp_0002204",
        description="Pulmonary Embolism",
        meaning=HP["0002204"])
    snomedct_50043002_other = PermissibleValue(
        text="snomedct_50043002_other",
        description="Other",
        meaning=SNOMEDCT["50043002_other"])

    _defn = EnumDefinition(
        name="SinoPulmonaryConditionEnum",
        description="Types of sino‐pulmonary conditions",
    )

class CardiovascularConditionEnum(EnumDefinitionImpl):
    """
    Types of cardiovascular conditions
    """
    hp_0001627 = PermissibleValue(
        text="hp_0001627",
        description="Congenital Heart Disease",
        meaning=HP["0001627"])
    hp_0002563 = PermissibleValue(
        text="hp_0002563",
        description="Constrictive Pericarditis",
        meaning=HP["0002563"])
    hp_0000822 = PermissibleValue(
        text="hp_0000822",
        description="Hypertension",
        meaning=HP["0000822"])
    hp_0001658 = PermissibleValue(
        text="hp_0001658",
        description="Myocardial Infarction",
        meaning=HP["0001658"])
    hp_0001297 = PermissibleValue(
        text="hp_0001297",
        description="Stroke (CVA)",
        meaning=HP["0001297"])
    hp_0001977 = PermissibleValue(
        text="hp_0001977",
        description="Thrombosis",
        meaning=HP["0001977"])
    hp_0002326 = PermissibleValue(
        text="hp_0002326",
        description="Transient Ischemic Attack",
        meaning=HP["0002326"])
    hp_0025015 = PermissibleValue(
        text="hp_0025015",
        description="Vascular Malformation",
        meaning=HP["0025015"])
    snomedct_49601007_other = PermissibleValue(
        text="snomedct_49601007_other",
        description="Other",
        meaning=SNOMEDCT["49601007_other"])

    _defn = EnumDefinition(
        name="CardiovascularConditionEnum",
        description="Types of cardiovascular conditions",
    )

class HematologicLymphoidConditionEnum(EnumDefinitionImpl):
    """
    Types of hematologic-lymphoid conditions
    """
    hp_0002732 = PermissibleValue(
        text="hp_0002732",
        description="Lymph node hypoplasia",
        meaning=HP["0002732"])
    customcode_lymphnodeabsence = PermissibleValue(
        text="customcode_lymphnodeabsence",
        description="Lymph node absence",
        meaning=CIEINR["lymphnodeabsence"])
    hp_0005359 = PermissibleValue(
        text="hp_0005359",
        description="Absent Thymus Shadow",
        meaning=HP["0005359"])
    hp_0030813 = PermissibleValue(
        text="hp_0030813",
        description="Absent Tonsils",
        meaning=HP["0030813"])
    hp_0001903 = PermissibleValue(
        text="hp_0001903",
        description="Anemia",
        meaning=HP["0001903"])
    hp_0001915 = PermissibleValue(
        text="hp_0001915",
        description="Aplastic Anemia",
        meaning=HP["0001915"])
    snomedct_82545002 = PermissibleValue(
        text="snomedct_82545002",
        description="Blood Transfusion Reaction",
        meaning=SNOMEDCT["82545002"])
    hp_0031035 = PermissibleValue(
        text="hp_0031035",
        description="Chronic Infection",
        meaning=HP["0031035"])
    hp_0003256 = PermissibleValue(
        text="hp_0003256",
        description="Coagulopathy",
        meaning=HP["0003256"])
    customcode_engraftment_maternalcells = PermissibleValue(
        text="customcode_engraftment_maternalcells",
        description="Engraftment by Maternal Cells",
        meaning=CIEINR["engraftment_maternalcells"])
    hp_0000421 = PermissibleValue(
        text="hp_0000421",
        description="Epistaxis",
        meaning=HP["0000421"])
    hp_0032252 = PermissibleValue(
        text="hp_0032252",
        description="Granulomas",
        meaning=HP["0032252"])
    hp_0005261 = PermissibleValue(
        text="hp_0005261",
        description="Hemarthrosis",
        meaning=HP["0005261"])
    hp_0001971 = PermissibleValue(
        text="hp_0001971",
        description="Hypersplenism",
        meaning=HP["0001971"])
    hp_0001890 = PermissibleValue(
        text="hp_0001890",
        description="Autoimmune hemolytic anemia",
        meaning=HP["0001890"])
    hp_0001891 = PermissibleValue(
        text="hp_0001891",
        description="Iron Deficiency",
        meaning=HP["0001891"])
    hp_0001974 = PermissibleValue(
        text="hp_0001974",
        description="Leukocytosis",
        meaning=HP["0001974"])
    hp_0002716 = PermissibleValue(
        text="hp_0002716",
        description="Lymphadenopathy",
        meaning=HP["0002716"])
    hp_0001888 = PermissibleValue(
        text="hp_0001888",
        description="Lymphopenia",
        meaning=HP["0001888"])
    hp_0002863 = PermissibleValue(
        text="hp_0002863",
        description="Myelodysplasia",
        meaning=HP["0002863"])
    hp_0001875 = PermissibleValue(
        text="hp_0001875",
        description="Neutropenia",
        meaning=HP["0001875"])
    mondo_0008228 = PermissibleValue(
        text="mondo_0008228",
        description="Pernicious Anemia",
        meaning=MONDO["0008228"])
    hp_0000967 = PermissibleValue(
        text="hp_0000967",
        description="Petechia",
        meaning=HP["0000967"])
    hp_0001744 = PermissibleValue(
        text="hp_0001744",
        description="Splenomegaly",
        meaning=HP["0001744"])
    hp_0001873 = PermissibleValue(
        text="hp_0001873",
        description="Thrombocytopenia",
        meaning=HP["0001873"])
    hp_0001973 = PermissibleValue(
        text="hp_0001973",
        description="Thrombocytopenia - immune",
        meaning=HP["0001973"])
    hp_0001977 = PermissibleValue(
        text="hp_0001977",
        description="Thrombosis",
        meaning=HP["0001977"])
    mondo_0018896 = PermissibleValue(
        text="mondo_0018896",
        description="Thrombotic Thrombocytopenia Purpura",
        meaning=MONDO["0018896"])
    mondo_0005570_other = PermissibleValue(
        text="mondo_0005570_other",
        description="Other",
        meaning=MONDO["0005570_other"])

    _defn = EnumDefinition(
        name="HematologicLymphoidConditionEnum",
        description="Types of hematologic-lymphoid conditions",
    )

class MusculoskeletalConditionEnum(EnumDefinitionImpl):
    """
    Types of musculoskeletal conditions
    """
    hp_0002829 = PermissibleValue(
        text="hp_0002829",
        description="Arthralgia",
        meaning=HP["0002829"])
    hp_0001369 = PermissibleValue(
        text="hp_0001369",
        description="Arthritis",
        meaning=HP["0001369"])
    hp_0002757 = PermissibleValue(
        text="hp_0002757",
        description="Frequent Fractures",
        meaning=HP["0002757"])
    hp_0005261 = PermissibleValue(
        text="hp_0005261",
        description="Hemarthrosis",
        meaning=HP["0005261"])
    hp_0001382 = PermissibleValue(
        text="hp_0001382",
        description="Hyperextensibility",
        meaning=HP["0001382"])
    hp_0005681 = PermissibleValue(
        text="hp_0005681",
        description="Juvenile Idiopathic Arthritis",
        meaning=HP["0005681"])
    hp_0100614 = PermissibleValue(
        text="hp_0100614",
        description="Myositis",
        meaning=HP["0100614"])
    hp_0002758 = PermissibleValue(
        text="hp_0002758",
        description="Osteoarthritis",
        meaning=HP["0002758"])
    hp_0000939 = PermissibleValue(
        text="hp_0000939",
        description="Osteoporosis",
        meaning=HP["0000939"])
    hp_0001370 = PermissibleValue(
        text="hp_0001370",
        description="Rheumatoid Arthritis",
        meaning=HP["0001370"])
    hp_0002650 = PermissibleValue(
        text="hp_0002650",
        description="Scoliosis",
        meaning=HP["0002650"])
    hp_0004322 = PermissibleValue(
        text="hp_0004322",
        description="Short Stature",
        meaning=HP["0004322"])
    hp_0000924 = PermissibleValue(
        text="hp_0000924",
        description="Skeletal Abnormality",
        meaning=HP["0000924"])
    hp_0010754 = PermissibleValue(
        text="hp_0010754",
        description="Temporal-Mandibular Joint Dysfunction",
        meaning=HP["0010754"])
    hp_0001324 = PermissibleValue(
        text="hp_0001324",
        description="Muscle weakness",
        meaning=HP["0001324"])
    snomedct_928000_other = PermissibleValue(
        text="snomedct_928000_other",
        description="Other",
        meaning=SNOMEDCT["928000_other"])

    _defn = EnumDefinition(
        name="MusculoskeletalConditionEnum",
        description="Types of musculoskeletal conditions",
    )

class GastrointestinalConditionEnum(EnumDefinitionImpl):
    """
    Types of gastrointestinal conditions
    """
    hp_0002027 = PermissibleValue(
        text="hp_0002027",
        description="Abdominal Pain",
        meaning=HP["0002027"])
    hp_0032154 = PermissibleValue(
        text="hp_0032154",
        description="Aphthous Ulcers",
        meaning=HP["0032154"])
    hp_6000143 = PermissibleValue(
        text="hp_6000143",
        description="Appendicitis",
        meaning=HP["6000143"])
    mondo_0016264 = PermissibleValue(
        text="mondo_0016264",
        description="Autoimmune Hepatitis",
        meaning=MONDO["0016264"])
    hp_0002608 = PermissibleValue(
        text="hp_0002608",
        description="Celiac Disease",
        meaning=HP["0002608"])
    mondo_0005154 = PermissibleValue(
        text="mondo_0005154",
        description="Liver Disease",
        meaning=MONDO["0005154"])
    hp_0001394 = PermissibleValue(
        text="hp_0001394",
        description="Cirrhosis",
        meaning=HP["0001394"])
    hp_0002583 = PermissibleValue(
        text="hp_0002583",
        description="Colitis",
        meaning=HP["0002583"])
    hp_0002019 = PermissibleValue(
        text="hp_0002019",
        description="Constipation",
        meaning=HP["0002019"])
    hp_4000055 = PermissibleValue(
        text="hp_4000055",
        description="Enteritis",
        meaning=HP["4000055"])
    hp_0410151 = PermissibleValue(
        text="hp_0410151",
        description="Eosinophilic Esophagitis",
        meaning=HP["0410151"])
    hp_0100819 = PermissibleValue(
        text="hp_0100819",
        description="Fistula",
        meaning=HP["0100819"])
    hp_0005264 = PermissibleValue(
        text="hp_0005264",
        description="Gall Bladder Disease",
        meaning=HP["0005264"])
    hp_0001081 = PermissibleValue(
        text="hp_0001081",
        description="Gall Stones",
        meaning=HP["0001081"])
    hp_0004386 = PermissibleValue(
        text="hp_0004386",
        description="Gastroenteritis",
        meaning=HP["0004386"])
    hp_0002020 = PermissibleValue(
        text="hp_0002020",
        description="GE Reflux",
        meaning=HP["0002020"])
    hp_0002240 = PermissibleValue(
        text="hp_0002240",
        description="Hepatomegaly",
        meaning=HP["0002240"])
    hp_0002037 = PermissibleValue(
        text="hp_0002037",
        description="Inflammatory Bowel Disease",
        meaning=HP["0002037"])
    hp_0011956 = PermissibleValue(
        text="hp_0011956",
        description="Intestinal Nodular Lymphoid Hyperplasia",
        meaning=HP["0011956"])
    hp_0001399 = PermissibleValue(
        text="hp_0001399",
        description="Liver Failure",
        meaning=HP["0001399"])
    hp_0001410 = PermissibleValue(
        text="hp_0001410",
        description="Liver Function Abnormalities",
        meaning=HP["0001410"])
    hp_0002024 = PermissibleValue(
        text="hp_0002024",
        description="Malabsorption",
        meaning=HP["0002024"])
    hp_0004796 = PermissibleValue(
        text="hp_0004796",
        description="Obstruction",
        meaning=HP["0004796"])
    hp_0005218 = PermissibleValue(
        text="hp_0005218",
        description="Anoperineal fistula",
        meaning=HP["0005218"])
    hp_0002586 = PermissibleValue(
        text="hp_0002586",
        description="Peritonitis",
        meaning=HP["0002586"])
    mondo_0005538 = PermissibleValue(
        text="mondo_0005538",
        description="Proctitis",
        meaning=MONDO["0005538"])
    hp_0002243 = PermissibleValue(
        text="hp_0002243",
        description="Protein Losing Gastroenteropathy",
        meaning=HP["0002243"])
    hp_0030991 = PermissibleValue(
        text="hp_0030991",
        description="Sclerosing Cholangitis",
        meaning=HP["0030991"])
    hp_0001746 = PermissibleValue(
        text="hp_0001746",
        description="Asplenia",
        meaning=HP["0001746"])
    hp_0001744 = PermissibleValue(
        text="hp_0001744",
        description="Splenomegaly",
        meaning=HP["0001744"])
    snomedct_119292006_other = PermissibleValue(
        text="snomedct_119292006_other",
        description="Other",
        meaning=SNOMEDCT["119292006_other"])

    _defn = EnumDefinition(
        name="GastrointestinalConditionEnum",
        description="Types of gastrointestinal conditions",
    )

class IBDEvidenceEnum(EnumDefinitionImpl):
    """
    Evidence for IBD diagnosis
    """
    snomedct_39154008 = PermissibleValue(
        text="snomedct_39154008",
        description="Clinical diagnosis",
        meaning=SNOMEDCT["39154008"])
    snomedct_88101002 = PermissibleValue(
        text="snomedct_88101002",
        description="Pathology diagnosis (Biopsy-proven)",
        meaning=SNOMEDCT["88101002"])

    _defn = EnumDefinition(
        name="IBDEvidenceEnum",
        description="Evidence for IBD diagnosis",
    )

class EndocrineMetabolicConditionEnum(EnumDefinitionImpl):
    """
    Types of endocrine-metabolic conditions
    """
    hp_0000846 = PermissibleValue(
        text="hp_0000846",
        description="Adrenal Insufficiency",
        meaning=HP["0000846"])
    hp_0003118 = PermissibleValue(
        text="hp_0003118",
        description="Cushing's Disease",
        meaning=HP["0003118"])
    hp_0100651 = PermissibleValue(
        text="hp_0100651",
        description="Diabetes-Type 1",
        meaning=HP["0100651"])
    hp_0005978 = PermissibleValue(
        text="hp_0005978",
        description="Diabetes-Type 2",
        meaning=HP["0005978"])
    hp_0034323 = PermissibleValue(
        text="hp_0034323",
        description="Growth Hormone Deficiency",
        meaning=HP["0034323"])
    hp_0000872 = PermissibleValue(
        text="hp_0000872",
        description="Hashimoto's Thyroiditis",
        meaning=HP["0000872"])
    hp_0003072 = PermissibleValue(
        text="hp_0003072",
        description="Hypercalcemia",
        meaning=HP["0003072"])
    hp_0002901 = PermissibleValue(
        text="hp_0002901",
        description="Hypocalcemia",
        meaning=HP["0002901"])
    hp_0000836 = PermissibleValue(
        text="hp_0000836",
        description="Hyperthyroidism",
        meaning=HP["0000836"])
    hp_0000821 = PermissibleValue(
        text="hp_0000821",
        description="Hypothyroidism",
        meaning=HP["0000821"])
    hp_0040075 = PermissibleValue(
        text="hp_0040075",
        description="Pituitary Insufficiency",
        meaning=HP["0040075"])
    hp_0008209 = PermissibleValue(
        text="hp_0008209",
        description="Primary Ovarian Failure",
        meaning=HP["0008209"])
    snomedct_362969004_other = PermissibleValue(
        text="snomedct_362969004_other",
        description="Other",
        meaning=SNOMEDCT["362969004_other"])

    _defn = EnumDefinition(
        name="EndocrineMetabolicConditionEnum",
        description="Types of endocrine-metabolic conditions",
    )

class GenitourinaryConditionEnum(EnumDefinitionImpl):
    """
    Types of genitourinary conditions
    """
    hp_0100577 = PermissibleValue(
        text="hp_0100577",
        description="Cystitis (non-infectious)",
        meaning=HP["0100577"])
    hp_0000031 = PermissibleValue(
        text="hp_0000031",
        description="Epididymitis",
        meaning=HP["0000031"])
    hp_0000099 = PermissibleValue(
        text="hp_0000099",
        description="Glomerulonephritis",
        meaning=HP["0000099"])
    hp_0000790 = PermissibleValue(
        text="hp_0000790",
        description="Hematuria",
        meaning=HP["0000790"])
    hp_0005575 = PermissibleValue(
        text="hp_0005575",
        description="Hemolytic Uremic Syndrome",
        meaning=HP["0005575"])
    hp_0000123 = PermissibleValue(
        text="hp_0000123",
        description="Nephritis (unspecified)",
        meaning=HP["0000123"])
    hp_0000100 = PermissibleValue(
        text="hp_0000100",
        description="Nephrosis",
        meaning=HP["0000100"])
    hp_0100796 = PermissibleValue(
        text="hp_0100796",
        description="Orchitis",
        meaning=HP["0100796"])
    hp_0000024 = PermissibleValue(
        text="hp_0000024",
        description="Prostatitis",
        meaning=HP["0000024"])
    hp_0000083 = PermissibleValue(
        text="hp_0000083",
        description="Renal Failure",
        meaning=HP["0000083"])
    hp_0000787 = PermissibleValue(
        text="hp_0000787",
        description="Renal Stone",
        meaning=HP["0000787"])
    hp_0041047 = PermissibleValue(
        text="hp_0041047",
        description="Urinary Outlet Obstruction",
        meaning=HP["0041047"])
    snomedct_42030000_other = PermissibleValue(
        text="snomedct_42030000_other",
        description="Other",
        meaning=SNOMEDCT["42030000_other"])

    _defn = EnumDefinition(
        name="GenitourinaryConditionEnum",
        description="Types of genitourinary conditions",
    )

class NeoplasticConditionEnum(EnumDefinitionImpl):
    """
    Types of neoplastic conditions
    """
    hp_0006721 = PermissibleValue(
        text="hp_0006721",
        description="Acute Lymphocytic Leukemia (ALL)",
        meaning=HP["0006721"])
    hp_0004808 = PermissibleValue(
        text="hp_0004808",
        description="Acute Myelogenous Leukemia (AML)",
        meaning=HP["0004808"])
    hp_0005550 = PermissibleValue(
        text="hp_0005550",
        description="Chronic Lymphocytic Leukemia (CLL)",
        meaning=HP["0005550"])
    hp_0005506 = PermissibleValue(
        text="hp_0005506",
        description="Chronic Myelogenous Leukemia (CML)",
        meaning=HP["0005506"])
    hp_0001909 = PermissibleValue(
        text="hp_0001909",
        description="Unspecified Leukemia",
        meaning=HP["0001909"])
    hp_0012539 = PermissibleValue(
        text="hp_0012539",
        description="Lymphoma - Non-Hodgkin's",
        meaning=HP["0012539"])
    hp_0012189 = PermissibleValue(
        text="hp_0012189",
        description="Lymphoma - Hodgkin's",
        meaning=HP["0012189"])
    hp_0031047 = PermissibleValue(
        text="hp_0031047",
        description="Monoclonal Gammopathy",
        meaning=HP["0031047"])
    hp_0005523 = PermissibleValue(
        text="hp_0005523",
        description="Polyclonal Lymphoproliferation",
        meaning=HP["0005523"])
    hp_0002664 = PermissibleValue(
        text="hp_0002664",
        description="Solid Tumor",
        meaning=HP["0002664"])
    hp_0100522 = PermissibleValue(
        text="hp_0100522",
        description="Thymoma",
        meaning=HP["0100522"])
    snomedct_55342001_other = PermissibleValue(
        text="snomedct_55342001_other",
        description="Other",
        meaning=SNOMEDCT["55342001_other"])

    _defn = EnumDefinition(
        name="NeoplasticConditionEnum",
        description="Types of neoplastic conditions",
    )

class EBVStatusEnum(EnumDefinitionImpl):
    """
    Epstein-Barr Virus status
    """
    ncit_c129454 = PermissibleValue(
        text="ncit_c129454",
        description="Epstein-Barr Virus Positive",
        meaning=NCIT["C129454"])
    ncit_c141321 = PermissibleValue(
        text="ncit_c141321",
        description="Epstein-Barr Virus Negative",
        meaning=NCIT["C141321"])

    _defn = EnumDefinition(
        name="EBVStatusEnum",
        description="Epstein-Barr Virus status",
    )

class AutoimmuneConditionEnum(EnumDefinitionImpl):
    """
    Types of autoimmune conditions
    """
    hp_0001904 = PermissibleValue(
        text="hp_0001904",
        description="Autoimmune Neutropenia",
        meaning=HP["0001904"])
    hp_0001890 = PermissibleValue(
        text="hp_0001890",
        description="Autoimmune Hemolytic Anemia",
        meaning=HP["0001890"])
    hp_0001973 = PermissibleValue(
        text="hp_0001973",
        description="Autoimmune Thrombocytopenia",
        meaning=HP["0001973"])
    mondo_0019167 = PermissibleValue(
        text="mondo_0019167",
        description="Henoch-Schonlein Purpura (HSP)",
        meaning=MONDO["0019167"])
    hp_0001101 = PermissibleValue(
        text="hp_0001101",
        description="Iritis",
        meaning=HP["0001101"])
    hp_0100324 = PermissibleValue(
        text="hp_0100324",
        description="Scleroderma",
        meaning=HP["0100324"])
    hp_0002725 = PermissibleValue(
        text="hp_0002725",
        description="Systemic Lupus Erythematosus (SLE)",
        meaning=HP["0002725"])
    hp_0000554 = PermissibleValue(
        text="hp_0000554",
        description="Uveitis",
        meaning=HP["0000554"])
    hp_0005318 = PermissibleValue(
        text="hp_0005318",
        description="Vasculitis - CNS",
        meaning=HP["0005318"])
    hp_0005310 = PermissibleValue(
        text="hp_0005310",
        description="Vasculitis - Large Vessel",
        meaning=HP["0005310"])
    hp_0011944 = PermissibleValue(
        text="hp_0011944",
        description="Vasculitis - Small Vessel",
        meaning=HP["0011944"])
    snomedct_85828009_other = PermissibleValue(
        text="snomedct_85828009_other",
        description="Other",
        meaning=SNOMEDCT["85828009_other"])

    _defn = EnumDefinition(
        name="AutoimmuneConditionEnum",
        description="Types of autoimmune conditions",
    )

class ConstitutionalConditionEnum(EnumDefinitionImpl):
    """
    Types of constitutional conditions
    """
    hp_0033047 = PermissibleValue(
        text="hp_0033047",
        description="Aches",
        meaning=HP["0033047"])
    hp_0012378 = PermissibleValue(
        text="hp_0012378",
        description="Fatigue",
        meaning=HP["0012378"])
    hp_0001945 = PermissibleValue(
        text="hp_0001945",
        description="Fever",
        meaning=HP["0001945"])
    hp_0033834 = PermissibleValue(
        text="hp_0033834",
        description="Malaise",
        meaning=HP["0033834"])
    hp_0002329 = PermissibleValue(
        text="hp_0002329",
        description="Sleepiness",
        meaning=HP["0002329"])
    hp_0100785 = PermissibleValue(
        text="hp_0100785",
        description="Sleeplessness",
        meaning=HP["0100785"])
    hp_0000975 = PermissibleValue(
        text="hp_0000975",
        description="Sweating",
        meaning=HP["0000975"])
    hp_0025142_other = PermissibleValue(
        text="hp_0025142_other",
        description="Other",
        meaning=HP["0025142_other"])

    _defn = EnumDefinition(
        name="ConstitutionalConditionEnum",
        description="Types of constitutional conditions",
    )

class GrowthDevelopmentConditionEnum(EnumDefinitionImpl):
    """
    Types of growth and development conditions
    """
    hp_0001263 = PermissibleValue(
        text="hp_0001263",
        description="Delayed Developmental Milestones",
        meaning=HP["0001263"])
    hp_0100555 = PermissibleValue(
        text="hp_0100555",
        description="Dysmorphic Features",
        meaning=HP["0100555"])
    hp_0001508 = PermissibleValue(
        text="hp_0001508",
        description="Failure to Thrive",
        meaning=HP["0001508"])
    hp_0001824 = PermissibleValue(
        text="hp_0001824",
        description="Unintended Weight Loss",
        meaning=HP["0001824"])
    hp_0000365 = PermissibleValue(
        text="hp_0000365",
        description="Hearing Impairment (non-congenital)",
        meaning=HP["0000365"])
    hp_0001249 = PermissibleValue(
        text="hp_0001249",
        description="Intellectual Disability",
        meaning=HP["0001249"])
    hp_0025502 = PermissibleValue(
        text="hp_0025502",
        description="Over-Weight",
        meaning=HP["0025502"])
    hp_0004322 = PermissibleValue(
        text="hp_0004322",
        description="Short Stature",
        meaning=HP["0004322"])
    hp_0004325 = PermissibleValue(
        text="hp_0004325",
        description="Under-Weight",
        meaning=HP["0004325"])
    snomedct_5294002_other = PermissibleValue(
        text="snomedct_5294002_other",
        description="Other",
        meaning=SNOMEDCT["5294002_other"])

    _defn = EnumDefinition(
        name="GrowthDevelopmentConditionEnum",
        description="Types of growth and development conditions",
    )

class ConditionSeverityEnum(EnumDefinitionImpl):
    """
    Severity levels of conditions
    """
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
        name="ConditionSeverityEnum",
        description="Severity levels of conditions",
    )

class ConditionTemporalPatternEnum(EnumDefinitionImpl):
    """
    Temporal patterns of conditions
    """
    hp_0011009 = PermissibleValue(
        text="hp_0011009",
        description="Acute",
        meaning=HP["0011009"])
    hp_0011011 = PermissibleValue(
        text="hp_0011011",
        description="Subacute",
        meaning=HP["0011011"])
    hp_0025297 = PermissibleValue(
        text="hp_0025297",
        description="Prolonged",
        meaning=HP["0025297"])
    hp_0025153 = PermissibleValue(
        text="hp_0025153",
        description="Transient",
        meaning=HP["0025153"])
    hp_0031796 = PermissibleValue(
        text="hp_0031796",
        description="Recurrent",
        meaning=HP["0031796"])
    hp_0011010 = PermissibleValue(
        text="hp_0011010",
        description="Chronic",
        meaning=HP["0011010"])

    _defn = EnumDefinition(
        name="ConditionTemporalPatternEnum",
        description="Temporal patterns of conditions",
    )

class YesNoEnum(EnumDefinitionImpl):
    """
    Yes/No response
    """
    _defn = EnumDefinition(
        name="YesNoEnum",
        description="Yes/No response",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "True",
            PermissibleValue(
                text="True",
                description="Yes",
                meaning=CIEINR["yes"]))
        setattr(cls, "False",
            PermissibleValue(
                text="False",
                description="No",
                meaning=CIEINR["no"]))

class CompletionStatusEnum(EnumDefinitionImpl):
    """
    Enumeration for form completion status
    """
    _defn = EnumDefinition(
        name="CompletionStatusEnum",
        description="Enumeration for form completion status",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "0",
            PermissibleValue(
                text="0",
                description="Incomplete",
                meaning=CIEINR["0"]))
        setattr(cls, "1",
            PermissibleValue(
                text="1",
                description="Unverified",
                meaning=CIEINR["1"]))
        setattr(cls, "2",
            PermissibleValue(
                text="2",
                description="Complete",
                meaning=CIEINR["2"]))

class NCBITaxon(EnumDefinitionImpl):
    """
    NCBI organismal classification
    """
    _defn = EnumDefinition(
        name="NCBITaxon",
        description="NCBI organismal classification",
        code_set=URIRef(str(NCBITAXON)),
        code_set_version="2024-07-03",
    )

class SNOMEDCT(EnumDefinitionImpl):
    """
    SNOMED CT
    """
    _defn = EnumDefinition(
        name="SNOMEDCT",
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

class BIOPORTAL(EnumDefinitionImpl):
    """
    BioPortal ontology repository
    """
    _defn = EnumDefinition(
        name="BIOPORTAL",
        description="BioPortal ontology repository",
        code_set_version="2024-09-01",
    )

class IUIS(EnumDefinitionImpl):
    """
    International Union of Immunological Societies Classification
    """
    _defn = EnumDefinition(
        name="IUIS",
        description="International Union of Immunological Societies Classification",
        code_set_version="2024",
    )

# Slots
class slots:
    pass

slots.type_of_condition = Slot(uri=CIEINR.type_of_condition, name="type_of_condition", curie=CIEINR.curie('type_of_condition'),
                   model_uri=CIEINR.type_of_condition, domain=None, range=Optional[Union[str, "ConditionTypeEnum"]])

slots.snomedct_95320005 = Slot(uri=CIEINR.snomedct_95320005, name="snomedct_95320005", curie=CIEINR.curie('snomedct_95320005'),
                   model_uri=CIEINR.snomedct_95320005, domain=None, range=Optional[Union[str, "SkinConditionEnum"]])

slots.snomedct_118938008 = Slot(uri=CIEINR.snomedct_118938008, name="snomedct_118938008", curie=CIEINR.curie('snomedct_118938008'),
                   model_uri=CIEINR.snomedct_118938008, domain=None, range=Optional[Union[str, "DentalConditionEnum"]])

slots.snomedct_50043002 = Slot(uri=CIEINR.snomedct_50043002, name="snomedct_50043002", curie=CIEINR.curie('snomedct_50043002'),
                   model_uri=CIEINR.snomedct_50043002, domain=None, range=Optional[Union[str, "SinoPulmonaryConditionEnum"]])

slots.snomedct_49601007 = Slot(uri=CIEINR.snomedct_49601007, name="snomedct_49601007", curie=CIEINR.curie('snomedct_49601007'),
                   model_uri=CIEINR.snomedct_49601007, domain=None, range=Optional[Union[str, "CardiovascularConditionEnum"]])

slots.mondo_0005570 = Slot(uri=CIEINR.mondo_0005570, name="mondo_0005570", curie=CIEINR.curie('mondo_0005570'),
                   model_uri=CIEINR.mondo_0005570, domain=None, range=Optional[Union[str, "HematologicLymphoidConditionEnum"]])

slots.snomedct_928000 = Slot(uri=CIEINR.snomedct_928000, name="snomedct_928000", curie=CIEINR.curie('snomedct_928000'),
                   model_uri=CIEINR.snomedct_928000, domain=None, range=Optional[Union[str, "MusculoskeletalConditionEnum"]])

slots.snomedct_119292006 = Slot(uri=CIEINR.snomedct_119292006, name="snomedct_119292006", curie=CIEINR.curie('snomedct_119292006'),
                   model_uri=CIEINR.snomedct_119292006, domain=None, range=Optional[Union[str, "GastrointestinalConditionEnum"]])

slots.hp_0002037_evidence = Slot(uri=CIEINR.hp_0002037_evidence, name="hp_0002037_evidence", curie=CIEINR.curie('hp_0002037_evidence'),
                   model_uri=CIEINR.hp_0002037_evidence, domain=None, range=Optional[Union[str, "IBDEvidenceEnum"]])

slots.snomedct_362969004 = Slot(uri=CIEINR.snomedct_362969004, name="snomedct_362969004", curie=CIEINR.curie('snomedct_362969004'),
                   model_uri=CIEINR.snomedct_362969004, domain=None, range=Optional[Union[str, "EndocrineMetabolicConditionEnum"]])

slots.snomedct_42030000 = Slot(uri=CIEINR.snomedct_42030000, name="snomedct_42030000", curie=CIEINR.curie('snomedct_42030000'),
                   model_uri=CIEINR.snomedct_42030000, domain=None, range=Optional[Union[str, "GenitourinaryConditionEnum"]])

slots.snomedct_55342001 = Slot(uri=CIEINR.snomedct_55342001, name="snomedct_55342001", curie=CIEINR.curie('snomedct_55342001'),
                   model_uri=CIEINR.snomedct_55342001, domain=None, range=Optional[Union[str, "NeoplasticConditionEnum"]])

slots.hp_0012539_modifier = Slot(uri=CIEINR.hp_0012539_modifier, name="hp_0012539_modifier", curie=CIEINR.curie('hp_0012539_modifier'),
                   model_uri=CIEINR.hp_0012539_modifier, domain=None, range=Optional[Union[str, "EBVStatusEnum"]])

slots.hp_0012189_modifier = Slot(uri=CIEINR.hp_0012189_modifier, name="hp_0012189_modifier", curie=CIEINR.curie('hp_0012189_modifier'),
                   model_uri=CIEINR.hp_0012189_modifier, domain=None, range=Optional[Union[str, "EBVStatusEnum"]])

slots.hp_0005523_modifier = Slot(uri=CIEINR.hp_0005523_modifier, name="hp_0005523_modifier", curie=CIEINR.curie('hp_0005523_modifier'),
                   model_uri=CIEINR.hp_0005523_modifier, domain=None, range=Optional[Union[str, "EBVStatusEnum"]])

slots.snomedct_85828009 = Slot(uri=CIEINR.snomedct_85828009, name="snomedct_85828009", curie=CIEINR.curie('snomedct_85828009'),
                   model_uri=CIEINR.snomedct_85828009, domain=None, range=Optional[Union[str, "AutoimmuneConditionEnum"]])

slots.hp_0025142 = Slot(uri=CIEINR.hp_0025142, name="hp_0025142", curie=CIEINR.curie('hp_0025142'),
                   model_uri=CIEINR.hp_0025142, domain=None, range=Optional[Union[str, "ConstitutionalConditionEnum"]])

slots.snomedct_5294002 = Slot(uri=CIEINR.snomedct_5294002, name="snomedct_5294002", curie=CIEINR.curie('snomedct_5294002'),
                   model_uri=CIEINR.snomedct_5294002, domain=None, range=Optional[Union[str, "GrowthDevelopmentConditionEnum"]])

slots.condition_other_hp = Slot(uri=CIEINR.condition_other_hp, name="condition_other_hp", curie=CIEINR.curie('condition_other_hp'),
                   model_uri=CIEINR.condition_other_hp, domain=None, range=Optional[str])

slots.new_condition = Slot(uri=CIEINR.new_condition, name="new_condition", curie=CIEINR.curie('new_condition'),
                   model_uri=CIEINR.new_condition, domain=None, range=Optional[str])

slots.condition_severity = Slot(uri=CIEINR.condition_severity, name="condition_severity", curie=CIEINR.curie('condition_severity'),
                   model_uri=CIEINR.condition_severity, domain=None, range=Optional[Union[str, "ConditionSeverityEnum"]])

slots.condition_temp_pattern = Slot(uri=CIEINR.condition_temp_pattern, name="condition_temp_pattern", curie=CIEINR.curie('condition_temp_pattern'),
                   model_uri=CIEINR.condition_temp_pattern, domain=None, range=Optional[Union[str, "ConditionTemporalPatternEnum"]])

slots.condition_date = Slot(uri=CIEINR.condition_date, name="condition_date", curie=CIEINR.curie('condition_date'),
                   model_uri=CIEINR.condition_date, domain=None, range=Optional[Union[str, "YesNoEnum"]])

slots.condition_date_1 = Slot(uri=CIEINR.condition_date_1, name="condition_date_1", curie=CIEINR.curie('condition_date_1'),
                   model_uri=CIEINR.condition_date_1, domain=None, range=Optional[Union[str, UnionDateString]])

slots.conditions_initial_form_complete = Slot(uri=CIEINR.conditions_initial_form_complete, name="conditions_initial_form_complete", curie=CIEINR.curie('conditions_initial_form_complete'),
                   model_uri=CIEINR.conditions_initial_form_complete, domain=None, range=Optional[Union[str, "CompletionStatusEnum"]])

slots.codeSystemsContainer__ncbi_taxon = Slot(uri=CIEINR.ncbi_taxon, name="codeSystemsContainer__ncbi_taxon", curie=CIEINR.curie('ncbi_taxon'),
                   model_uri=CIEINR.codeSystemsContainer__ncbi_taxon, domain=None, range=Union[str, "NCBITaxon"])

slots.codeSystemsContainer__snomedct = Slot(uri=CIEINR.snomedct, name="codeSystemsContainer__snomedct", curie=CIEINR.curie('snomedct'),
                   model_uri=CIEINR.codeSystemsContainer__snomedct, domain=None, range=Union[str, "SNOMEDCT"])

slots.codeSystemsContainer__mondo = Slot(uri=CIEINR.mondo, name="codeSystemsContainer__mondo", curie=CIEINR.curie('mondo'),
                   model_uri=CIEINR.codeSystemsContainer__mondo, domain=None, range=Union[str, "MONDO"])

slots.codeSystemsContainer__hpo = Slot(uri=CIEINR.hpo, name="codeSystemsContainer__hpo", curie=CIEINR.curie('hpo'),
                   model_uri=CIEINR.codeSystemsContainer__hpo, domain=None, range=Union[str, "HP"])

slots.codeSystemsContainer__loinc = Slot(uri=CIEINR.loinc, name="codeSystemsContainer__loinc", curie=CIEINR.curie('loinc'),
                   model_uri=CIEINR.codeSystemsContainer__loinc, domain=None, range=Union[str, "LOINC"])

slots.codeSystemsContainer__omim = Slot(uri=CIEINR.omim, name="codeSystemsContainer__omim", curie=CIEINR.curie('omim'),
                   model_uri=CIEINR.codeSystemsContainer__omim, domain=None, range=Union[str, "OMIM"])

slots.codeSystemsContainer__orpha = Slot(uri=CIEINR.orpha, name="codeSystemsContainer__orpha", curie=CIEINR.curie('orpha'),
                   model_uri=CIEINR.codeSystemsContainer__orpha, domain=None, range=Union[str, "ORPHA"])

slots.codeSystemsContainer__ncit = Slot(uri=CIEINR.ncit, name="codeSystemsContainer__ncit", curie=CIEINR.curie('ncit'),
                   model_uri=CIEINR.codeSystemsContainer__ncit, domain=None, range=Union[str, "NCIT"])

slots.codeSystemsContainer__uo = Slot(uri=CIEINR.uo, name="codeSystemsContainer__uo", curie=CIEINR.curie('uo'),
                   model_uri=CIEINR.codeSystemsContainer__uo, domain=None, range=Union[str, "UO"])

slots.codeSystemsContainer__hgnc = Slot(uri=CIEINR.hgnc, name="codeSystemsContainer__hgnc", curie=CIEINR.curie('hgnc'),
                   model_uri=CIEINR.codeSystemsContainer__hgnc, domain=None, range=Union[str, "HGNC"])

slots.codeSystemsContainer__hgvs = Slot(uri=CIEINR.hgvs, name="codeSystemsContainer__hgvs", curie=CIEINR.curie('hgvs'),
                   model_uri=CIEINR.codeSystemsContainer__hgvs, domain=None, range=Union[str, "HGVS"])

slots.codeSystemsContainer__ga4gh = Slot(uri=CIEINR.ga4gh, name="codeSystemsContainer__ga4gh", curie=CIEINR.curie('ga4gh'),
                   model_uri=CIEINR.codeSystemsContainer__ga4gh, domain=None, range=Union[str, "GA4GH"])

slots.codeSystemsContainer__hl7fhir = Slot(uri=CIEINR.hl7fhir, name="codeSystemsContainer__hl7fhir", curie=CIEINR.curie('hl7fhir'),
                   model_uri=CIEINR.codeSystemsContainer__hl7fhir, domain=None, range=Union[str, "HL7FHIR"])

slots.codeSystemsContainer__icd11 = Slot(uri=CIEINR.icd11, name="codeSystemsContainer__icd11", curie=CIEINR.curie('icd11'),
                   model_uri=CIEINR.codeSystemsContainer__icd11, domain=None, range=Union[str, "ICD11"])

slots.codeSystemsContainer__icd10cm = Slot(uri=CIEINR.icd10cm, name="codeSystemsContainer__icd10cm", curie=CIEINR.curie('icd10cm'),
                   model_uri=CIEINR.codeSystemsContainer__icd10cm, domain=None, range=Union[str, "ICD10CM"])

slots.codeSystemsContainer__bioportal = Slot(uri=CIEINR.bioportal, name="codeSystemsContainer__bioportal", curie=CIEINR.curie('bioportal'),
                   model_uri=CIEINR.codeSystemsContainer__bioportal, domain=None, range=Union[str, "BIOPORTAL"])

slots.codeSystemsContainer__iuis = Slot(uri=CIEINR.iuis, name="codeSystemsContainer__iuis", curie=CIEINR.curie('iuis'),
                   model_uri=CIEINR.codeSystemsContainer__iuis, domain=None, range=Union[str, "IUIS"])
