# Auto generated from form_7_live_vaccines.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-03-22T12:50:21
# Schema: live_vaccine
#
# id: https://github.com/BIH-CEI/cieinr/src/cieinr/v1_0_0/linkml_schemas/live_vaccine.yaml
# description: Schema for the live vaccine administration and specific immune response form.
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

from linkml_runtime.linkml_model.types import Float, Integer, String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
HP = CurieNamespace('HP', 'https://purl.obolibrary.org/obo/HP_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT/')
SNOMEDCT = CurieNamespace('SNOMEDCT', 'http://snomed.info/sct/')
VO = CurieNamespace('VO', 'https://purl.obolibrary.org/obo/VO_')
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
class LiveVaccineHistory(YAMLRoot):
    """
    Form capturing live vaccine administration and specific immune response.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CIEINR["LiveVaccineHistory"]
    class_class_curie: ClassVar[str] = "cieinr:LiveVaccineHistory"
    class_name: ClassVar[str] = "LiveVaccineHistory"
    class_model_uri: ClassVar[URIRef] = CIEINR.LiveVaccineHistory

    completion_live_vax: Optional[Union[str, UnionDateString]] = None
    live_vax: Optional[Union[str, "LiveVaccineTypeEnum"]] = None
    live_vax_other: Optional[str] = None
    live_vax_dosages: Optional[Union[str, "LiveVaccineDosagesEnum"]] = None
    live_vax_ae: Optional[Union[str, "VaccineAssociatedInfectionEnum"]] = None
    ae_live_vax: Optional[Union[str, "AdverseEventObservationEnum"]] = None
    live_vax_ae_other: Optional[str] = None
    live_vax_ae_severity: Optional[Union[str, "LiveVaccineAdverseEventSeverityEnum"]] = None
    live_vax_response: Optional[Union[str, "VaccineResponseEnum"]] = None
    life_vax_response_date: Optional[Union[str, UnionDateString]] = None
    measles_response: Optional[Union[str, "VaccineResponseEnum"]] = None
    mumps_response: Optional[Union[str, "VaccineResponseEnum"]] = None
    rubella_response: Optional[Union[str, "VaccineResponseEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.completion_live_vax is not None and not isinstance(self.completion_live_vax, UnionDateString):
            self.completion_live_vax = UnionDateString(self.completion_live_vax)

        if self.live_vax is not None and not isinstance(self.live_vax, LiveVaccineTypeEnum):
            self.live_vax = LiveVaccineTypeEnum(self.live_vax)

        if self.live_vax_other is not None and not isinstance(self.live_vax_other, str):
            self.live_vax_other = str(self.live_vax_other)

        if self.live_vax_dosages is not None and not isinstance(self.live_vax_dosages, LiveVaccineDosagesEnum):
            self.live_vax_dosages = LiveVaccineDosagesEnum(self.live_vax_dosages)

        if self.live_vax_ae is not None and not isinstance(self.live_vax_ae, VaccineAssociatedInfectionEnum):
            self.live_vax_ae = VaccineAssociatedInfectionEnum(self.live_vax_ae)

        if self.ae_live_vax is not None and not isinstance(self.ae_live_vax, AdverseEventObservationEnum):
            self.ae_live_vax = AdverseEventObservationEnum(self.ae_live_vax)

        if self.live_vax_ae_other is not None and not isinstance(self.live_vax_ae_other, str):
            self.live_vax_ae_other = str(self.live_vax_ae_other)

        if self.live_vax_ae_severity is not None and not isinstance(self.live_vax_ae_severity, LiveVaccineAdverseEventSeverityEnum):
            self.live_vax_ae_severity = LiveVaccineAdverseEventSeverityEnum(self.live_vax_ae_severity)

        if self.live_vax_response is not None and not isinstance(self.live_vax_response, VaccineResponseEnum):
            self.live_vax_response = VaccineResponseEnum(self.live_vax_response)

        if self.life_vax_response_date is not None and not isinstance(self.life_vax_response_date, UnionDateString):
            self.life_vax_response_date = UnionDateString(self.life_vax_response_date)

        if self.measles_response is not None and not isinstance(self.measles_response, VaccineResponseEnum):
            self.measles_response = VaccineResponseEnum(self.measles_response)

        if self.mumps_response is not None and not isinstance(self.mumps_response, VaccineResponseEnum):
            self.mumps_response = VaccineResponseEnum(self.mumps_response)

        if self.rubella_response is not None and not isinstance(self.rubella_response, VaccineResponseEnum):
            self.rubella_response = VaccineResponseEnum(self.rubella_response)

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
class LiveVaccineTypeEnum(EnumDefinitionImpl):
    """
    Types of live vaccines.
    """
    vo_0010209 = PermissibleValue(
        text="vo_0010209",
        description="Oral Polio vaccine",
        meaning=CIEINR["vo_0010209"])
    vo_0000731 = PermissibleValue(
        text="vo_0000731",
        description="MMR (Measles, Mumps, Rubella)",
        meaning=CIEINR["vo_0000731"])
    vo_0021165 = PermissibleValue(
        text="vo_0021165",
        description="Varicella",
        meaning=CIEINR["vo_0021165"])
    vo_0000433 = PermissibleValue(
        text="vo_0000433",
        description="Vaccinia",
        meaning=CIEINR["vo_0000433"])
    vo_0000771 = PermissibleValue(
        text="vo_0000771",
        description="BCG",
        meaning=CIEINR["vo_0000771"])
    vo_0000123 = PermissibleValue(
        text="vo_0000123",
        description="Yellow Fever",
        meaning=CIEINR["vo_0000123"])
    vo_0003495 = PermissibleValue(
        text="vo_0003495",
        description="Influenza",
        meaning=CIEINR["vo_0003495"])
    vo_0000658 = PermissibleValue(
        text="vo_0000658",
        description="Rotavirus",
        meaning=CIEINR["vo_0000658"])
    other = PermissibleValue(
        text="other",
        description="Other",
        meaning=CIEINR["other"])

    _defn = EnumDefinition(
        name="LiveVaccineTypeEnum",
        description="Types of live vaccines.",
    )

class LiveVaccineDosagesEnum(EnumDefinitionImpl):
    """
    Number of doses for live vaccine.
    """
    _defn = EnumDefinition(
        name="LiveVaccineDosagesEnum",
        description="Number of doses for live vaccine.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "1",
            PermissibleValue(
                text="1",
                description="Dose 1",
                meaning=CIEINR["1"]))
        setattr(cls, "2",
            PermissibleValue(
                text="2",
                description="Dose 2",
                meaning=CIEINR["2"]))
        setattr(cls, "3",
            PermissibleValue(
                text="3",
                description="Dose 3",
                meaning=CIEINR["3"]))
        setattr(cls, "4",
            PermissibleValue(
                text="4",
                description="Dose 4",
                meaning=CIEINR["4"]))
        setattr(cls, "5",
            PermissibleValue(
                text="5",
                description="Dose 5 and more",
                meaning=CIEINR["5"]))

class VaccineAssociatedInfectionEnum(EnumDefinitionImpl):
    """
    Vaccine-associated infection observation.
    """
    hp_0020085 = PermissibleValue(
        text="hp_0020085",
        description="Vaccine-associated infection was observed",
        meaning=CIEINR["hp_0020085"])
    hp_0020085_exluded = PermissibleValue(
        text="hp_0020085_exluded",
        description="No vaccine-associated infection was observed",
        meaning=CIEINR["hp_0020085_exluded"])
    snomedct_261665006 = PermissibleValue(
        text="snomedct_261665006",
        description="Unknown",
        meaning=CIEINR["snomedct_261665006"])

    _defn = EnumDefinition(
        name="VaccineAssociatedInfectionEnum",
        description="Vaccine-associated infection observation.",
    )

class AdverseEventObservationEnum(EnumDefinitionImpl):
    """
    Adverse event observation for live vaccine.
    """
    _defn = EnumDefinition(
        name="AdverseEventObservationEnum",
        description="Adverse event observation for live vaccine.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "1",
            PermissibleValue(
                text="1",
                description="True",
                meaning=CIEINR["1"]))
        setattr(cls, "2",
            PermissibleValue(
                text="2",
                description="False",
                meaning=CIEINR["2"]))
        setattr(cls, "3",
            PermissibleValue(
                text="3",
                description="Unknown",
                meaning=CIEINR["3"]))

class LiveVaccineAdverseEventSeverityEnum(EnumDefinitionImpl):
    """
    Severity levels of adverse events for live vaccine.
    """
    hp_0012825 = PermissibleValue(
        text="hp_0012825",
        description="Mild",
        meaning=CIEINR["hp_0012825"])
    hp_0012826 = PermissibleValue(
        text="hp_0012826",
        description="Moderate/medically attended",
        meaning=CIEINR["hp_0012826"])
    hp_0012828 = PermissibleValue(
        text="hp_0012828",
        description="Life threatening/medically attended",
        meaning=CIEINR["hp_0012828"])

    _defn = EnumDefinition(
        name="LiveVaccineAdverseEventSeverityEnum",
        description="Severity levels of adverse events for live vaccine.",
    )

class VaccineResponseEnum(EnumDefinitionImpl):
    """
    Vaccine response evaluation.
    """
    snomedct_365589000 = PermissibleValue(
        text="snomedct_365589000",
        description="Adequate antibody response",
        meaning=CIEINR["snomedct_365589000"])
    snomedct_266721009 = PermissibleValue(
        text="snomedct_266721009",
        description="No antibody response",
        meaning=CIEINR["snomedct_266721009"])
    snomedct_261665006 = PermissibleValue(
        text="snomedct_261665006",
        description="Not measured/unknown",
        meaning=CIEINR["snomedct_261665006"])
    other = PermissibleValue(
        text="other",
        description="Other",
        meaning=CIEINR["other"])

    _defn = EnumDefinition(
        name="VaccineResponseEnum",
        description="Vaccine response evaluation.",
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

slots.completion_live_vax = Slot(uri=CIEINR.completion_live_vax, name="completion_live_vax", curie=CIEINR.curie('completion_live_vax'),
                   model_uri=CIEINR.completion_live_vax, domain=None, range=Optional[Union[str, UnionDateString]])

slots.live_vax = Slot(uri=CIEINR.live_vax, name="live_vax", curie=CIEINR.curie('live_vax'),
                   model_uri=CIEINR.live_vax, domain=None, range=Optional[Union[str, "LiveVaccineTypeEnum"]])

slots.live_vax_other = Slot(uri=CIEINR.live_vax_other, name="live_vax_other", curie=CIEINR.curie('live_vax_other'),
                   model_uri=CIEINR.live_vax_other, domain=None, range=Optional[str])

slots.live_vax_dosages = Slot(uri=CIEINR.live_vax_dosages, name="live_vax_dosages", curie=CIEINR.curie('live_vax_dosages'),
                   model_uri=CIEINR.live_vax_dosages, domain=None, range=Optional[Union[str, "LiveVaccineDosagesEnum"]])

slots.live_vax_ae = Slot(uri=CIEINR.live_vax_ae, name="live_vax_ae", curie=CIEINR.curie('live_vax_ae'),
                   model_uri=CIEINR.live_vax_ae, domain=None, range=Optional[Union[str, "VaccineAssociatedInfectionEnum"]])

slots.ae_live_vax = Slot(uri=CIEINR.ae_live_vax, name="ae_live_vax", curie=CIEINR.curie('ae_live_vax'),
                   model_uri=CIEINR.ae_live_vax, domain=None, range=Optional[Union[str, "AdverseEventObservationEnum"]])

slots.live_vax_ae_other = Slot(uri=CIEINR.live_vax_ae_other, name="live_vax_ae_other", curie=CIEINR.curie('live_vax_ae_other'),
                   model_uri=CIEINR.live_vax_ae_other, domain=None, range=Optional[str])

slots.live_vax_ae_severity = Slot(uri=CIEINR.live_vax_ae_severity, name="live_vax_ae_severity", curie=CIEINR.curie('live_vax_ae_severity'),
                   model_uri=CIEINR.live_vax_ae_severity, domain=None, range=Optional[Union[str, "LiveVaccineAdverseEventSeverityEnum"]])

slots.live_vax_response = Slot(uri=CIEINR.live_vax_response, name="live_vax_response", curie=CIEINR.curie('live_vax_response'),
                   model_uri=CIEINR.live_vax_response, domain=None, range=Optional[Union[str, "VaccineResponseEnum"]])

slots.life_vax_response_date = Slot(uri=CIEINR.life_vax_response_date, name="life_vax_response_date", curie=CIEINR.curie('life_vax_response_date'),
                   model_uri=CIEINR.life_vax_response_date, domain=None, range=Optional[Union[str, UnionDateString]])

slots.measles_response = Slot(uri=CIEINR.measles_response, name="measles_response", curie=CIEINR.curie('measles_response'),
                   model_uri=CIEINR.measles_response, domain=None, range=Optional[Union[str, "VaccineResponseEnum"]])

slots.mumps_response = Slot(uri=CIEINR.mumps_response, name="mumps_response", curie=CIEINR.curie('mumps_response'),
                   model_uri=CIEINR.mumps_response, domain=None, range=Optional[Union[str, "VaccineResponseEnum"]])

slots.rubella_response = Slot(uri=CIEINR.rubella_response, name="rubella_response", curie=CIEINR.curie('rubella_response'),
                   model_uri=CIEINR.rubella_response, domain=None, range=Optional[Union[str, "VaccineResponseEnum"]])

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
