# Auto generated from form_6_inactivated_vaccines.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-03-22T12:47:32
# Schema: inactivated_vaccine
#
# id: https://github.com/BIH-CEI/cieinr/src/cieinr/v1_0_0/linkml_schemas/inactivated_vaccine.yaml
# description: Schema for the inactivated vaccine history and specific immune response form.
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
class InactivatedVaccineHistory(YAMLRoot):
    """
    Form capturing inactivated vaccine history and specific immune response.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CIEINR["InactivatedVaccineHistory"]
    class_class_curie: ClassVar[str] = "cieinr:InactivatedVaccineHistory"
    class_name: ClassVar[str] = "InactivatedVaccineHistory"
    class_model_uri: ClassVar[URIRef] = CIEINR.InactivatedVaccineHistory

    completion_of_inact_vax: Optional[Union[str, UnionDateString]] = None
    inactiv_vax: Optional[Union[str, "InactivatedVaccineTypeEnum"]] = None
    inactiv_vax_other: Optional[str] = None
    inactiv_vax_dose: Optional[Union[str, "InactivatedVaccineDoseEnum"]] = None
    inactiv_vax_ae: Optional[Union[str, "AdverseEventEnum"]] = None
    inactiv_vax_ae_other: Optional[str] = None
    inactiv_vax_ae_severity: Optional[Union[str, "InactivatedVaccineAdverseEventSeverityEnum"]] = None
    vo_0000424_before_pneu: Optional[Union[str, "PneumococcalResponseEnum"]] = None
    inactiv_vax_response: Optional[Union[str, "VaccineResponseEnum"]] = None
    inactiv_vax_response_date: Optional[Union[str, UnionDateString]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.completion_of_inact_vax is not None and not isinstance(self.completion_of_inact_vax, UnionDateString):
            self.completion_of_inact_vax = UnionDateString(self.completion_of_inact_vax)

        if self.inactiv_vax is not None and not isinstance(self.inactiv_vax, InactivatedVaccineTypeEnum):
            self.inactiv_vax = InactivatedVaccineTypeEnum(self.inactiv_vax)

        if self.inactiv_vax_other is not None and not isinstance(self.inactiv_vax_other, str):
            self.inactiv_vax_other = str(self.inactiv_vax_other)

        if self.inactiv_vax_dose is not None and not isinstance(self.inactiv_vax_dose, InactivatedVaccineDoseEnum):
            self.inactiv_vax_dose = InactivatedVaccineDoseEnum(self.inactiv_vax_dose)

        if self.inactiv_vax_ae is not None and not isinstance(self.inactiv_vax_ae, AdverseEventEnum):
            self.inactiv_vax_ae = AdverseEventEnum(self.inactiv_vax_ae)

        if self.inactiv_vax_ae_other is not None and not isinstance(self.inactiv_vax_ae_other, str):
            self.inactiv_vax_ae_other = str(self.inactiv_vax_ae_other)

        if self.inactiv_vax_ae_severity is not None and not isinstance(self.inactiv_vax_ae_severity, InactivatedVaccineAdverseEventSeverityEnum):
            self.inactiv_vax_ae_severity = InactivatedVaccineAdverseEventSeverityEnum(self.inactiv_vax_ae_severity)

        if self.vo_0000424_before_pneu is not None and not isinstance(self.vo_0000424_before_pneu, PneumococcalResponseEnum):
            self.vo_0000424_before_pneu = PneumococcalResponseEnum(self.vo_0000424_before_pneu)

        if self.inactiv_vax_response is not None and not isinstance(self.inactiv_vax_response, VaccineResponseEnum):
            self.inactiv_vax_response = VaccineResponseEnum(self.inactiv_vax_response)

        if self.inactiv_vax_response_date is not None and not isinstance(self.inactiv_vax_response_date, UnionDateString):
            self.inactiv_vax_response_date = UnionDateString(self.inactiv_vax_response_date)

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
class InactivatedVaccineTypeEnum(EnumDefinitionImpl):
    """
    Types of inactivated vaccines.
    """
    vo_0000738 = PermissibleValue(
        text="vo_0000738",
        description="DTap (Diphtheria, Tetanus, Acellular Pertussis)",
        meaning=CIEINR["vo_0000738"])
    vo_0000662 = PermissibleValue(
        text="vo_0000662",
        description="Haemophilus Influenza Type b",
        meaning=CIEINR["vo_0000662"])
    vo_0010211 = PermissibleValue(
        text="vo_0010211",
        description="PrevNar/Pneu-C-13",
        meaning=CIEINR["vo_0010211"])
    vo_0006041 = PermissibleValue(
        text="vo_0006041",
        description="PrevNar/Pneu-C-15",
        meaning=CIEINR["vo_0006041"])
    vo_0010356 = PermissibleValue(
        text="vo_0010356",
        description="PrevNar/Pneu-C-20",
        meaning=CIEINR["vo_0010356"])
    vo_0010440 = PermissibleValue(
        text="vo_0010440",
        description="V116, Pneu-21",
        meaning=CIEINR["vo_0010440"])
    vo_0006033 = PermissibleValue(
        text="vo_0006033",
        description="Men-C",
        meaning=CIEINR["vo_0006033"])
    vo_0010205 = PermissibleValue(
        text="vo_0010205",
        description="Men-B",
        meaning=CIEINR["vo_0010205"])
    vo_0010727 = PermissibleValue(
        text="vo_0010727",
        description="Meningococcal Quadrivalent Vaccine",
        meaning=CIEINR["vo_0010727"])
    vo_0000667 = PermissibleValue(
        text="vo_0000667",
        description="HPV",
        meaning=CIEINR["vo_0000667"])
    vo_0000644 = PermissibleValue(
        text="vo_0000644",
        description="Hepatitis B",
        meaning=CIEINR["vo_0000644"])
    vo_0003196 = PermissibleValue(
        text="vo_0003196",
        description="Acellular Pertussis",
        meaning=CIEINR["vo_0003196"])
    vo_0000664 = PermissibleValue(
        text="vo_0000664",
        description="IPV (Polio)",
        meaning=CIEINR["vo_0000664"])
    vo_0000088 = PermissibleValue(
        text="vo_0000088",
        description="Pneumovax",
        meaning=CIEINR["vo_0000088"])
    vo_0004908 = PermissibleValue(
        text="vo_0004908",
        description="COVID-19",
        meaning=CIEINR["vo_0004908"])
    vo_0000642 = PermissibleValue(
        text="vo_0000642",
        description="Flu",
        meaning=CIEINR["vo_0000642"])
    other = PermissibleValue(
        text="other",
        description="Other",
        meaning=CIEINR["other"])

    _defn = EnumDefinition(
        name="InactivatedVaccineTypeEnum",
        description="Types of inactivated vaccines.",
    )

class InactivatedVaccineDoseEnum(EnumDefinitionImpl):
    """
    Number of doses for inactivated vaccine.
    """
    _defn = EnumDefinition(
        name="InactivatedVaccineDoseEnum",
        description="Number of doses for inactivated vaccine.",
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
        setattr(cls, "6",
            PermissibleValue(
                text="6",
                description="Vaccine not received",
                meaning=CIEINR["6"]))

class AdverseEventEnum(EnumDefinitionImpl):
    """
    Adverse event observation for inactivated vaccine.
    """
    hp_0020085 = PermissibleValue(
        text="hp_0020085",
        description="True",
        meaning=CIEINR["hp_0020085"])
    hp_0020085_exluded = PermissibleValue(
        text="hp_0020085_exluded",
        description="False",
        meaning=CIEINR["hp_0020085_exluded"])
    snomedct_261665006 = PermissibleValue(
        text="snomedct_261665006",
        description="Unknown",
        meaning=CIEINR["snomedct_261665006"])

    _defn = EnumDefinition(
        name="AdverseEventEnum",
        description="Adverse event observation for inactivated vaccine.",
    )

class InactivatedVaccineAdverseEventSeverityEnum(EnumDefinitionImpl):
    """
    Severity levels of adverse events.
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
        name="InactivatedVaccineAdverseEventSeverityEnum",
        description="Severity levels of adverse events.",
    )

class PneumococcalResponseEnum(EnumDefinitionImpl):
    """
    Pneumococcal response measured before vaccination.
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
        description="Unknown",
        meaning=CIEINR["snomedct_261665006"])

    _defn = EnumDefinition(
        name="PneumococcalResponseEnum",
        description="Pneumococcal response measured before vaccination.",
    )

class VaccineResponseEnum(EnumDefinitionImpl):
    """
    Post-vaccination response evaluation.
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
        description="Post-vaccination response evaluation.",
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

slots.completion_of_inact_vax = Slot(uri=CIEINR.completion_of_inact_vax, name="completion_of_inact_vax", curie=CIEINR.curie('completion_of_inact_vax'),
                   model_uri=CIEINR.completion_of_inact_vax, domain=None, range=Optional[Union[str, UnionDateString]])

slots.inactiv_vax = Slot(uri=CIEINR.inactiv_vax, name="inactiv_vax", curie=CIEINR.curie('inactiv_vax'),
                   model_uri=CIEINR.inactiv_vax, domain=None, range=Optional[Union[str, "InactivatedVaccineTypeEnum"]])

slots.inactiv_vax_other = Slot(uri=CIEINR.inactiv_vax_other, name="inactiv_vax_other", curie=CIEINR.curie('inactiv_vax_other'),
                   model_uri=CIEINR.inactiv_vax_other, domain=None, range=Optional[str])

slots.inactiv_vax_dose = Slot(uri=CIEINR.inactiv_vax_dose, name="inactiv_vax_dose", curie=CIEINR.curie('inactiv_vax_dose'),
                   model_uri=CIEINR.inactiv_vax_dose, domain=None, range=Optional[Union[str, "InactivatedVaccineDoseEnum"]])

slots.inactiv_vax_ae = Slot(uri=CIEINR.inactiv_vax_ae, name="inactiv_vax_ae", curie=CIEINR.curie('inactiv_vax_ae'),
                   model_uri=CIEINR.inactiv_vax_ae, domain=None, range=Optional[Union[str, "AdverseEventEnum"]])

slots.inactiv_vax_ae_other = Slot(uri=CIEINR.inactiv_vax_ae_other, name="inactiv_vax_ae_other", curie=CIEINR.curie('inactiv_vax_ae_other'),
                   model_uri=CIEINR.inactiv_vax_ae_other, domain=None, range=Optional[str])

slots.inactiv_vax_ae_severity = Slot(uri=CIEINR.inactiv_vax_ae_severity, name="inactiv_vax_ae_severity", curie=CIEINR.curie('inactiv_vax_ae_severity'),
                   model_uri=CIEINR.inactiv_vax_ae_severity, domain=None, range=Optional[Union[str, "InactivatedVaccineAdverseEventSeverityEnum"]])

slots.vo_0000424_before_pneu = Slot(uri=CIEINR.vo_0000424_before_pneu, name="vo_0000424_before_pneu", curie=CIEINR.curie('vo_0000424_before_pneu'),
                   model_uri=CIEINR.vo_0000424_before_pneu, domain=None, range=Optional[Union[str, "PneumococcalResponseEnum"]])

slots.inactiv_vax_response = Slot(uri=CIEINR.inactiv_vax_response, name="inactiv_vax_response", curie=CIEINR.curie('inactiv_vax_response'),
                   model_uri=CIEINR.inactiv_vax_response, domain=None, range=Optional[Union[str, "VaccineResponseEnum"]])

slots.inactiv_vax_response_date = Slot(uri=CIEINR.inactiv_vax_response_date, name="inactiv_vax_response_date", curie=CIEINR.curie('inactiv_vax_response_date'),
                   model_uri=CIEINR.inactiv_vax_response_date, domain=None, range=Optional[Union[str, UnionDateString]])

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
