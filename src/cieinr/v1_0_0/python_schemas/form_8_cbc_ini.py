# Auto generated from form_8_cbc_ini.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-03-22T12:53:22
# Schema: cbc
#
# id: https://github.com/BIH-CEI/cieinr/src/cieinr/v1_0_0/limkml_schemas/cbc.yaml
# description: Complete Blood Count (CBC) form capturing lab test information including test type,  date, and measurements for haemoglobin, platelets, leukocytes, neutrophils, eosinophils,  lymphocytes, and monocytes.
#
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

from linkml_runtime.linkml_model.types import Decimal, Float, Integer, String
from linkml_runtime.utils.metamodelcore import Decimal

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
LOINC = CurieNamespace('LOINC', 'http://loinc.org/')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
UO = CurieNamespace('UO', 'http://purl.obolibrary.org/obo/UO_')
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
class CBC(YAMLRoot):
    """
    Complete Blood Count (CBC) measurements including the type of test performed, the capture date, and lab values for
    multiple blood components.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CIEINR["CBC"]
    class_class_curie: ClassVar[str] = "cieinr:CBC"
    class_name: ClassVar[str] = "CBC"
    class_model_uri: ClassVar[URIRef] = CIEINR.CBC

    cbc_type: Optional[Union[str, "CBCTypeEnum"]] = None
    cbc_date: Optional[Union[str, UnionDateString]] = None
    cbc_haemoglobin: Optional[Union[str, "HaemoglobinTestEnum"]] = None
    cbc_haemoglobin_unit: Optional[Union[str, "HaemoglobinUnitEnum"]] = None
    cbc_haemoglobin_range: Optional[Union[str, "LabRangeEnum"]] = None
    cbc_haemoglobin_val: Optional[Decimal] = None
    cbc_platelets: Optional[Union[str, "PlateletsTestEnum"]] = None
    cbc_platelets_unit: Optional[Union[str, "BloodCellUnitEnum"]] = None
    cbc_platelets_range: Optional[Union[str, "LabRangeEnum"]] = None
    cbc_platelets_val: Optional[int] = None
    cbc_leukocytes: Optional[Union[str, "LeukocytesTestEnum"]] = None
    cbc_leukocytes_unit: Optional[Union[str, "BloodCellUnitEnum"]] = None
    cbc_leukocytes_range: Optional[Union[str, "LabRangeEnum"]] = None
    cbc_leukocytes_val: Optional[int] = None
    cbc_neutrophils: Optional[Union[str, "NeutrophilsTestEnum"]] = None
    cbc_neutrophils_unit: Optional[Union[str, "BloodCellUnitEnum"]] = None
    cbc_neutrophils_range: Optional[Union[str, "LabRangeEnum"]] = None
    cbc_neutrophils_val: Optional[int] = None
    cbc_eosinophils: Optional[Union[str, "EosinophilsTestEnum"]] = None
    cbc_eosinophils_unit: Optional[Union[str, "BloodCellUnitEnum"]] = None
    cbc_eosinophils_range: Optional[Union[str, "LabRangeEnum"]] = None
    cbc_eosinophils_val: Optional[int] = None
    cbc_lymphocytes: Optional[Union[str, "LymphocytesTestEnum"]] = None
    cbc_lymphocytes_unit: Optional[Union[str, "BloodCellUnitEnum"]] = None
    cbc_lymphocytes_range: Optional[Union[str, "LabRangeEnum"]] = None
    cbc_lymphocytes_val: Optional[int] = None
    cbc_monocytes: Optional[Union[str, "MonocytesTestEnum"]] = None
    cbc_monocytes_unit: Optional[Union[str, "BloodCellUnitEnum"]] = None
    cbc_monocytes_range: Optional[Union[str, "LabRangeEnum"]] = None
    cbc_monocytes_val: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.cbc_type is not None and not isinstance(self.cbc_type, CBCTypeEnum):
            self.cbc_type = CBCTypeEnum(self.cbc_type)

        if self.cbc_date is not None and not isinstance(self.cbc_date, UnionDateString):
            self.cbc_date = UnionDateString(self.cbc_date)

        if self.cbc_haemoglobin is not None and not isinstance(self.cbc_haemoglobin, HaemoglobinTestEnum):
            self.cbc_haemoglobin = HaemoglobinTestEnum(self.cbc_haemoglobin)

        if self.cbc_haemoglobin_unit is not None and not isinstance(self.cbc_haemoglobin_unit, HaemoglobinUnitEnum):
            self.cbc_haemoglobin_unit = HaemoglobinUnitEnum(self.cbc_haemoglobin_unit)

        if self.cbc_haemoglobin_range is not None and not isinstance(self.cbc_haemoglobin_range, LabRangeEnum):
            self.cbc_haemoglobin_range = LabRangeEnum(self.cbc_haemoglobin_range)

        if self.cbc_haemoglobin_val is not None and not isinstance(self.cbc_haemoglobin_val, Decimal):
            self.cbc_haemoglobin_val = Decimal(self.cbc_haemoglobin_val)

        if self.cbc_platelets is not None and not isinstance(self.cbc_platelets, PlateletsTestEnum):
            self.cbc_platelets = PlateletsTestEnum(self.cbc_platelets)

        if self.cbc_platelets_unit is not None and not isinstance(self.cbc_platelets_unit, BloodCellUnitEnum):
            self.cbc_platelets_unit = BloodCellUnitEnum(self.cbc_platelets_unit)

        if self.cbc_platelets_range is not None and not isinstance(self.cbc_platelets_range, LabRangeEnum):
            self.cbc_platelets_range = LabRangeEnum(self.cbc_platelets_range)

        if self.cbc_platelets_val is not None and not isinstance(self.cbc_platelets_val, int):
            self.cbc_platelets_val = int(self.cbc_platelets_val)

        if self.cbc_leukocytes is not None and not isinstance(self.cbc_leukocytes, LeukocytesTestEnum):
            self.cbc_leukocytes = LeukocytesTestEnum(self.cbc_leukocytes)

        if self.cbc_leukocytes_unit is not None and not isinstance(self.cbc_leukocytes_unit, BloodCellUnitEnum):
            self.cbc_leukocytes_unit = BloodCellUnitEnum(self.cbc_leukocytes_unit)

        if self.cbc_leukocytes_range is not None and not isinstance(self.cbc_leukocytes_range, LabRangeEnum):
            self.cbc_leukocytes_range = LabRangeEnum(self.cbc_leukocytes_range)

        if self.cbc_leukocytes_val is not None and not isinstance(self.cbc_leukocytes_val, int):
            self.cbc_leukocytes_val = int(self.cbc_leukocytes_val)

        if self.cbc_neutrophils is not None and not isinstance(self.cbc_neutrophils, NeutrophilsTestEnum):
            self.cbc_neutrophils = NeutrophilsTestEnum(self.cbc_neutrophils)

        if self.cbc_neutrophils_unit is not None and not isinstance(self.cbc_neutrophils_unit, BloodCellUnitEnum):
            self.cbc_neutrophils_unit = BloodCellUnitEnum(self.cbc_neutrophils_unit)

        if self.cbc_neutrophils_range is not None and not isinstance(self.cbc_neutrophils_range, LabRangeEnum):
            self.cbc_neutrophils_range = LabRangeEnum(self.cbc_neutrophils_range)

        if self.cbc_neutrophils_val is not None and not isinstance(self.cbc_neutrophils_val, int):
            self.cbc_neutrophils_val = int(self.cbc_neutrophils_val)

        if self.cbc_eosinophils is not None and not isinstance(self.cbc_eosinophils, EosinophilsTestEnum):
            self.cbc_eosinophils = EosinophilsTestEnum(self.cbc_eosinophils)

        if self.cbc_eosinophils_unit is not None and not isinstance(self.cbc_eosinophils_unit, BloodCellUnitEnum):
            self.cbc_eosinophils_unit = BloodCellUnitEnum(self.cbc_eosinophils_unit)

        if self.cbc_eosinophils_range is not None and not isinstance(self.cbc_eosinophils_range, LabRangeEnum):
            self.cbc_eosinophils_range = LabRangeEnum(self.cbc_eosinophils_range)

        if self.cbc_eosinophils_val is not None and not isinstance(self.cbc_eosinophils_val, int):
            self.cbc_eosinophils_val = int(self.cbc_eosinophils_val)

        if self.cbc_lymphocytes is not None and not isinstance(self.cbc_lymphocytes, LymphocytesTestEnum):
            self.cbc_lymphocytes = LymphocytesTestEnum(self.cbc_lymphocytes)

        if self.cbc_lymphocytes_unit is not None and not isinstance(self.cbc_lymphocytes_unit, BloodCellUnitEnum):
            self.cbc_lymphocytes_unit = BloodCellUnitEnum(self.cbc_lymphocytes_unit)

        if self.cbc_lymphocytes_range is not None and not isinstance(self.cbc_lymphocytes_range, LabRangeEnum):
            self.cbc_lymphocytes_range = LabRangeEnum(self.cbc_lymphocytes_range)

        if self.cbc_lymphocytes_val is not None and not isinstance(self.cbc_lymphocytes_val, int):
            self.cbc_lymphocytes_val = int(self.cbc_lymphocytes_val)

        if self.cbc_monocytes is not None and not isinstance(self.cbc_monocytes, MonocytesTestEnum):
            self.cbc_monocytes = MonocytesTestEnum(self.cbc_monocytes)

        if self.cbc_monocytes_unit is not None and not isinstance(self.cbc_monocytes_unit, BloodCellUnitEnum):
            self.cbc_monocytes_unit = BloodCellUnitEnum(self.cbc_monocytes_unit)

        if self.cbc_monocytes_range is not None and not isinstance(self.cbc_monocytes_range, LabRangeEnum):
            self.cbc_monocytes_range = LabRangeEnum(self.cbc_monocytes_range)

        if self.cbc_monocytes_val is not None and not isinstance(self.cbc_monocytes_val, int):
            self.cbc_monocytes_val = int(self.cbc_monocytes_val)

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
class CBCTypeEnum(EnumDefinitionImpl):
    """
    Types of CBC tests.
    """
    ncit_c199317 = PermissibleValue(
        text="ncit_c199317",
        description="Test before the time of diagnosis",
        meaning=NCIT["C199317"])
    ncit_c158810 = PermissibleValue(
        text="ncit_c158810",
        description="Test at time of Diagnosis",
        meaning=NCIT["C158810"])
    ncit_c100059 = PermissibleValue(
        text="ncit_c100059",
        description="Test after diagnosis",
        meaning=NCIT["C100059"])
    ncit_c4647 = PermissibleValue(
        text="ncit_c4647",
        description="Annual test",
        meaning=NCIT["C4647"])

    _defn = EnumDefinition(
        name="CBCTypeEnum",
        description="Types of CBC tests.",
    )

class HaemoglobinTestEnum(EnumDefinitionImpl):
    """
    Hemoglobin test for CBC.
    """
    loinc_718_7 = PermissibleValue(
        text="loinc_718_7",
        description="Hemoglobin [g/dL] in Blood",
        meaning=LOINC["718-7"])

    _defn = EnumDefinition(
        name="HaemoglobinTestEnum",
        description="Hemoglobin test for CBC.",
    )

class PlateletsTestEnum(EnumDefinitionImpl):
    """
    Platelets test for CBC.
    """
    loinc_777_3 = PermissibleValue(
        text="loinc_777_3",
        description="Platelets [10*9/L] in Blood",
        meaning=LOINC["777-3"])

    _defn = EnumDefinition(
        name="PlateletsTestEnum",
        description="Platelets test for CBC.",
    )

class LeukocytesTestEnum(EnumDefinitionImpl):
    """
    Leukocytes test for CBC.
    """
    loinc_6690_2 = PermissibleValue(
        text="loinc_6690_2",
        description="Leukocytes [10*9/L] in Blood",
        meaning=LOINC["6690-2"])

    _defn = EnumDefinition(
        name="LeukocytesTestEnum",
        description="Leukocytes test for CBC.",
    )

class NeutrophilsTestEnum(EnumDefinitionImpl):
    """
    Neutrophils test for CBC.
    """
    loinc_26499_4 = PermissibleValue(
        text="loinc_26499_4",
        description="Neutrophils [10*9/L] in Blood",
        meaning=LOINC["26499-4"])

    _defn = EnumDefinition(
        name="NeutrophilsTestEnum",
        description="Neutrophils test for CBC.",
    )

class EosinophilsTestEnum(EnumDefinitionImpl):
    """
    Eosinophils test for CBC.
    """
    loinc_26449_9 = PermissibleValue(
        text="loinc_26449_9",
        description="Eosinophils [10*9/L] in Blood",
        meaning=LOINC["26449-9"])

    _defn = EnumDefinition(
        name="EosinophilsTestEnum",
        description="Eosinophils test for CBC.",
    )

class LymphocytesTestEnum(EnumDefinitionImpl):
    """
    Lymphocytes test for CBC.
    """
    loinc_26474_7 = PermissibleValue(
        text="loinc_26474_7",
        description="Lymphocytes [10*9/L] in Blood",
        meaning=LOINC["26474-7"])

    _defn = EnumDefinition(
        name="LymphocytesTestEnum",
        description="Lymphocytes test for CBC.",
    )

class MonocytesTestEnum(EnumDefinitionImpl):
    """
    Monocytes test for CBC.
    """
    loinc_26484_6 = PermissibleValue(
        text="loinc_26484_6",
        description="Monocytes [10*9/L] in Blood",
        meaning=LOINC["26484-6"])

    _defn = EnumDefinition(
        name="MonocytesTestEnum",
        description="Monocytes test for CBC.",
    )

class HaemoglobinUnitEnum(EnumDefinitionImpl):
    """
    Unit for haemoglobin.
    """
    uo_0000208 = PermissibleValue(
        text="uo_0000208",
        description="g/dL",
        meaning=UO["0000208"])

    _defn = EnumDefinition(
        name="HaemoglobinUnitEnum",
        description="Unit for haemoglobin.",
    )

class BloodCellUnitEnum(EnumDefinitionImpl):
    """
    Unit for blood cell counts.
    """
    uo_0000179 = PermissibleValue(
        text="uo_0000179",
        description="10*9/L",
        meaning=UO["0000179"])

    _defn = EnumDefinition(
        name="BloodCellUnitEnum",
        description="Unit for blood cell counts.",
    )

class LabRangeEnum(EnumDefinitionImpl):
    """
    Interpretation of lab value ranges.
    """
    ncit_c78801 = PermissibleValue(
        text="ncit_c78801",
        description="Below age-related reference range",
        meaning=NCIT["C78801"])
    ncit_c78800 = PermissibleValue(
        text="ncit_c78800",
        description="Within age-related reference range",
        meaning=NCIT["C78800"])
    ncit_c78727 = PermissibleValue(
        text="ncit_c78727",
        description="Above age-related reference range",
        meaning=NCIT["C78727"])

    _defn = EnumDefinition(
        name="LabRangeEnum",
        description="Interpretation of lab value ranges.",
    )

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

slots.cbc_type = Slot(uri=CIEINR.cbc_type, name="cbc_type", curie=CIEINR.curie('cbc_type'),
                   model_uri=CIEINR.cbc_type, domain=None, range=Optional[Union[str, "CBCTypeEnum"]])

slots.cbc_date = Slot(uri=CIEINR.cbc_date, name="cbc_date", curie=CIEINR.curie('cbc_date'),
                   model_uri=CIEINR.cbc_date, domain=None, range=Optional[Union[str, UnionDateString]])

slots.cbc_haemoglobin = Slot(uri=CIEINR.cbc_haemoglobin, name="cbc_haemoglobin", curie=CIEINR.curie('cbc_haemoglobin'),
                   model_uri=CIEINR.cbc_haemoglobin, domain=None, range=Optional[Union[str, "HaemoglobinTestEnum"]])

slots.cbc_haemoglobin_unit = Slot(uri=CIEINR.cbc_haemoglobin_unit, name="cbc_haemoglobin_unit", curie=CIEINR.curie('cbc_haemoglobin_unit'),
                   model_uri=CIEINR.cbc_haemoglobin_unit, domain=None, range=Optional[Union[str, "HaemoglobinUnitEnum"]])

slots.cbc_haemoglobin_range = Slot(uri=CIEINR.cbc_haemoglobin_range, name="cbc_haemoglobin_range", curie=CIEINR.curie('cbc_haemoglobin_range'),
                   model_uri=CIEINR.cbc_haemoglobin_range, domain=None, range=Optional[Union[str, "LabRangeEnum"]])

slots.cbc_haemoglobin_val = Slot(uri=CIEINR.cbc_haemoglobin_val, name="cbc_haemoglobin_val", curie=CIEINR.curie('cbc_haemoglobin_val'),
                   model_uri=CIEINR.cbc_haemoglobin_val, domain=None, range=Optional[Decimal])

slots.cbc_platelets = Slot(uri=CIEINR.cbc_platelets, name="cbc_platelets", curie=CIEINR.curie('cbc_platelets'),
                   model_uri=CIEINR.cbc_platelets, domain=None, range=Optional[Union[str, "PlateletsTestEnum"]])

slots.cbc_platelets_unit = Slot(uri=CIEINR.cbc_platelets_unit, name="cbc_platelets_unit", curie=CIEINR.curie('cbc_platelets_unit'),
                   model_uri=CIEINR.cbc_platelets_unit, domain=None, range=Optional[Union[str, "BloodCellUnitEnum"]])

slots.cbc_platelets_range = Slot(uri=CIEINR.cbc_platelets_range, name="cbc_platelets_range", curie=CIEINR.curie('cbc_platelets_range'),
                   model_uri=CIEINR.cbc_platelets_range, domain=None, range=Optional[Union[str, "LabRangeEnum"]])

slots.cbc_platelets_val = Slot(uri=CIEINR.cbc_platelets_val, name="cbc_platelets_val", curie=CIEINR.curie('cbc_platelets_val'),
                   model_uri=CIEINR.cbc_platelets_val, domain=None, range=Optional[int])

slots.cbc_leukocytes = Slot(uri=CIEINR.cbc_leukocytes, name="cbc_leukocytes", curie=CIEINR.curie('cbc_leukocytes'),
                   model_uri=CIEINR.cbc_leukocytes, domain=None, range=Optional[Union[str, "LeukocytesTestEnum"]])

slots.cbc_leukocytes_unit = Slot(uri=CIEINR.cbc_leukocytes_unit, name="cbc_leukocytes_unit", curie=CIEINR.curie('cbc_leukocytes_unit'),
                   model_uri=CIEINR.cbc_leukocytes_unit, domain=None, range=Optional[Union[str, "BloodCellUnitEnum"]])

slots.cbc_leukocytes_range = Slot(uri=CIEINR.cbc_leukocytes_range, name="cbc_leukocytes_range", curie=CIEINR.curie('cbc_leukocytes_range'),
                   model_uri=CIEINR.cbc_leukocytes_range, domain=None, range=Optional[Union[str, "LabRangeEnum"]])

slots.cbc_leukocytes_val = Slot(uri=CIEINR.cbc_leukocytes_val, name="cbc_leukocytes_val", curie=CIEINR.curie('cbc_leukocytes_val'),
                   model_uri=CIEINR.cbc_leukocytes_val, domain=None, range=Optional[int])

slots.cbc_neutrophils = Slot(uri=CIEINR.cbc_neutrophils, name="cbc_neutrophils", curie=CIEINR.curie('cbc_neutrophils'),
                   model_uri=CIEINR.cbc_neutrophils, domain=None, range=Optional[Union[str, "NeutrophilsTestEnum"]])

slots.cbc_neutrophils_unit = Slot(uri=CIEINR.cbc_neutrophils_unit, name="cbc_neutrophils_unit", curie=CIEINR.curie('cbc_neutrophils_unit'),
                   model_uri=CIEINR.cbc_neutrophils_unit, domain=None, range=Optional[Union[str, "BloodCellUnitEnum"]])

slots.cbc_neutrophils_range = Slot(uri=CIEINR.cbc_neutrophils_range, name="cbc_neutrophils_range", curie=CIEINR.curie('cbc_neutrophils_range'),
                   model_uri=CIEINR.cbc_neutrophils_range, domain=None, range=Optional[Union[str, "LabRangeEnum"]])

slots.cbc_neutrophils_val = Slot(uri=CIEINR.cbc_neutrophils_val, name="cbc_neutrophils_val", curie=CIEINR.curie('cbc_neutrophils_val'),
                   model_uri=CIEINR.cbc_neutrophils_val, domain=None, range=Optional[int])

slots.cbc_eosinophils = Slot(uri=CIEINR.cbc_eosinophils, name="cbc_eosinophils", curie=CIEINR.curie('cbc_eosinophils'),
                   model_uri=CIEINR.cbc_eosinophils, domain=None, range=Optional[Union[str, "EosinophilsTestEnum"]])

slots.cbc_eosinophils_unit = Slot(uri=CIEINR.cbc_eosinophils_unit, name="cbc_eosinophils_unit", curie=CIEINR.curie('cbc_eosinophils_unit'),
                   model_uri=CIEINR.cbc_eosinophils_unit, domain=None, range=Optional[Union[str, "BloodCellUnitEnum"]])

slots.cbc_eosinophils_range = Slot(uri=CIEINR.cbc_eosinophils_range, name="cbc_eosinophils_range", curie=CIEINR.curie('cbc_eosinophils_range'),
                   model_uri=CIEINR.cbc_eosinophils_range, domain=None, range=Optional[Union[str, "LabRangeEnum"]])

slots.cbc_eosinophils_val = Slot(uri=CIEINR.cbc_eosinophils_val, name="cbc_eosinophils_val", curie=CIEINR.curie('cbc_eosinophils_val'),
                   model_uri=CIEINR.cbc_eosinophils_val, domain=None, range=Optional[int])

slots.cbc_lymphocytes = Slot(uri=CIEINR.cbc_lymphocytes, name="cbc_lymphocytes", curie=CIEINR.curie('cbc_lymphocytes'),
                   model_uri=CIEINR.cbc_lymphocytes, domain=None, range=Optional[Union[str, "LymphocytesTestEnum"]])

slots.cbc_lymphocytes_unit = Slot(uri=CIEINR.cbc_lymphocytes_unit, name="cbc_lymphocytes_unit", curie=CIEINR.curie('cbc_lymphocytes_unit'),
                   model_uri=CIEINR.cbc_lymphocytes_unit, domain=None, range=Optional[Union[str, "BloodCellUnitEnum"]])

slots.cbc_lymphocytes_range = Slot(uri=CIEINR.cbc_lymphocytes_range, name="cbc_lymphocytes_range", curie=CIEINR.curie('cbc_lymphocytes_range'),
                   model_uri=CIEINR.cbc_lymphocytes_range, domain=None, range=Optional[Union[str, "LabRangeEnum"]])

slots.cbc_lymphocytes_val = Slot(uri=CIEINR.cbc_lymphocytes_val, name="cbc_lymphocytes_val", curie=CIEINR.curie('cbc_lymphocytes_val'),
                   model_uri=CIEINR.cbc_lymphocytes_val, domain=None, range=Optional[int])

slots.cbc_monocytes = Slot(uri=CIEINR.cbc_monocytes, name="cbc_monocytes", curie=CIEINR.curie('cbc_monocytes'),
                   model_uri=CIEINR.cbc_monocytes, domain=None, range=Optional[Union[str, "MonocytesTestEnum"]])

slots.cbc_monocytes_unit = Slot(uri=CIEINR.cbc_monocytes_unit, name="cbc_monocytes_unit", curie=CIEINR.curie('cbc_monocytes_unit'),
                   model_uri=CIEINR.cbc_monocytes_unit, domain=None, range=Optional[Union[str, "BloodCellUnitEnum"]])

slots.cbc_monocytes_range = Slot(uri=CIEINR.cbc_monocytes_range, name="cbc_monocytes_range", curie=CIEINR.curie('cbc_monocytes_range'),
                   model_uri=CIEINR.cbc_monocytes_range, domain=None, range=Optional[Union[str, "LabRangeEnum"]])

slots.cbc_monocytes_val = Slot(uri=CIEINR.cbc_monocytes_val, name="cbc_monocytes_val", curie=CIEINR.curie('cbc_monocytes_val'),
                   model_uri=CIEINR.cbc_monocytes_val, domain=None, range=Optional[int])

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
