# Auto generated from rarelink_6_2_phenotypic_feature.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-03-23T15:59:26
# Schema: rarelink_6_2_phenotypic_feature
#
# id: https://github.com/BIH-CEI/RareLink/blob/develop/src/rarelink_cdm_linkml/v2_0_4/linkml/rarelink_6_2_phenotypic_feature.yaml
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

metamodel_version = "1.7.0"
version = None


# Namespaces
ECO = CurieNamespace('eco', 'http://purl.obolibrary.org/obo/ECO_')
HP = CurieNamespace('hp', 'http://purl.obolibrary.org/obo/HP_')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NCBITAXON = CurieNamespace('ncbitaxon', 'http://purl.obolibrary.org/obo/NCBITaxon_')
RARELINK = CurieNamespace('rarelink', 'https://github.com/BIH-CEI/rarelink/')
SNOMED = CurieNamespace('snomed', 'http://snomed.info/sct/')
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
    snomedct_8116006_onset: Optional[Union[str, UnionDateString]] = None
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

        if self.snomedct_8116006_onset is not None and not isinstance(self.snomedct_8116006_onset, UnionDateString):
            self.snomedct_8116006_onset = UnionDateString(self.snomedct_8116006_onset)

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


# Enumerations
class PhenotypicFeatureStatus(EnumDefinitionImpl):

    snomedct_410605003 = PermissibleValue(
        text="snomedct_410605003",
        description="Confirmed present",
        meaning=SNOMED["410605003"])
    snomedct_723511001 = PermissibleValue(
        text="snomedct_723511001",
        description="Refuted",
        meaning=SNOMED["723511001"])

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

# Slots
class slots:
    pass

slots.snomedct_8116006 = Slot(uri=RARELINK.snomedct_8116006, name="snomedct_8116006", curie=RARELINK.curie('snomedct_8116006'),
                   model_uri=RARELINK.snomedct_8116006, domain=None, range=str)

slots.snomedct_363778006 = Slot(uri=RARELINK.snomedct_363778006, name="snomedct_363778006", curie=RARELINK.curie('snomedct_363778006'),
                   model_uri=RARELINK.snomedct_363778006, domain=None, range=Optional[Union[str, "PhenotypicFeatureStatus"]])

slots.snomedct_8116006_onset = Slot(uri=RARELINK.snomedct_8116006_onset, name="snomedct_8116006_onset", curie=RARELINK.curie('snomedct_8116006_onset'),
                   model_uri=RARELINK.snomedct_8116006_onset, domain=None, range=Optional[Union[str, UnionDateString]])

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
