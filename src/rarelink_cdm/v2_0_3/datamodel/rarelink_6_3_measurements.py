# Auto generated from rarelink_6_3_measurements.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-03-23T15:59:43
# Schema: rarelink_6_3_measurements
#
# id: https://github.com/BIH-CEI/RareLink/rarelink_6_3_measurements.yaml
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

from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import YAMLRoot
from rdflib import (
    URIRef
)

from linkml_runtime.linkml_model.types import String
from linkml_runtime.utils.metamodelcore import XSDDate

metamodel_version = "1.7.0"
version = None


# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
LOINC = CurieNamespace('loinc', 'https://loinc.org/')
NCIT = CurieNamespace('ncit', 'http://purl.obolibrary.org/obo/NCIT_')
RARELINK = CurieNamespace('rarelink', 'https://github.com/BIH-CEI/rarelink/')
SNOMEDCT = CurieNamespace('snomedct', 'http://snomed.info/sct/')
UO = CurieNamespace('uo', 'http://purl.obolibrary.org/obo/UO_')
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


# Enumerations


# Slots
class slots:
    pass

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
