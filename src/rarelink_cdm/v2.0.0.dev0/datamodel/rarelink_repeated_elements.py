# Auto generated from rarelink_repeated_elements.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-12-14T22:29:21
# Schema: rarelink_repeated_elements
#
# id: https://github.com/BIH-CEI/RareLink/blob/develop/src/rarelink_cdm_linkml/v2.0.0.dev0/linkml/rarelink_repeated_elements.yaml
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

from linkml_runtime.linkml_model.types import Date, Integer, String
from linkml_runtime.utils.metamodelcore import XSDDate

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

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

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.redcap_repeat_instrument is not None and not isinstance(self.redcap_repeat_instrument, str):
            self.redcap_repeat_instrument = str(self.redcap_repeat_instrument)

        if self.redcap_repeat_instance is not None and not isinstance(self.redcap_repeat_instance, int):
            self.redcap_repeat_instance = int(self.redcap_repeat_instance)

        if self.patient_status is not None and not isinstance(self.patient_status, PatientStatus):
            self.patient_status = PatientStatus(**as_dict(self.patient_status))

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
    class_model_uri: ClassVar[URIRef] = RARELINK.PatientStatus

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


# Enumerations
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

# Slots
class slots:
    pass

slots.patient_status = Slot(uri=RARELINK.patient_status, name="patient_status", curie=RARELINK.curie('patient_status'),
                   model_uri=RARELINK.patient_status, domain=None, range=Optional[Union[dict, PatientStatus]])

slots.redcap_repeat_instrument = Slot(uri=RARELINK.redcap_repeat_instrument, name="redcap_repeat_instrument", curie=RARELINK.curie('redcap_repeat_instrument'),
                   model_uri=RARELINK.redcap_repeat_instrument, domain=None, range=Optional[str])

slots.redcap_repeat_instance = Slot(uri=RARELINK.redcap_repeat_instance, name="redcap_repeat_instance", curie=RARELINK.curie('redcap_repeat_instance'),
                   model_uri=RARELINK.redcap_repeat_instance, domain=None, range=Optional[int])

slots.patient_status_date = Slot(uri=RARELINK.patient_status_date, name="patient_status_date", curie=RARELINK.curie('patient_status_date'),
                   model_uri=RARELINK.patient_status_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.snomed_278844005 = Slot(uri=RARELINK.snomed_278844005, name="snomed_278844005", curie=RARELINK.curie('snomed_278844005'),
                   model_uri=RARELINK.snomed_278844005, domain=None, range=Optional[Union[str, "ClinicalVitalStatus"]])

slots.snomed_398299004 = Slot(uri=RARELINK.snomed_398299004, name="snomed_398299004", curie=RARELINK.curie('snomed_398299004'),
                   model_uri=RARELINK.snomed_398299004, domain=None, range=Optional[Union[str, UnionDateString]])

slots.snomed_184305005 = Slot(uri=RARELINK.snomed_184305005, name="snomed_184305005", curie=RARELINK.curie('snomed_184305005'),
                   model_uri=RARELINK.snomed_184305005, domain=None, range=Optional[str])

slots.snomed_105727008 = Slot(uri=RARELINK.snomed_105727008, name="snomed_105727008", curie=RARELINK.curie('snomed_105727008'),
                   model_uri=RARELINK.snomed_105727008, domain=None, range=Optional[Union[str, "AgeCategory"]])

slots.snomed_412726003 = Slot(uri=RARELINK.snomed_412726003, name="snomed_412726003", curie=RARELINK.curie('snomed_412726003'),
                   model_uri=RARELINK.snomed_412726003, domain=None, range=Optional[str])

slots.snomed_723663001 = Slot(uri=RARELINK.snomed_723663001, name="snomed_723663001", curie=RARELINK.curie('snomed_723663001'),
                   model_uri=RARELINK.snomed_723663001, domain=None, range=Optional[Union[str, "YesNo"]])

slots.rarelink_3_patient_status_complete = Slot(uri=RARELINK.rarelink_3_patient_status_complete, name="rarelink_3_patient_status_complete", curie=RARELINK.curie('rarelink_3_patient_status_complete'),
                   model_uri=RARELINK.rarelink_3_patient_status_complete, domain=None, range=str)
