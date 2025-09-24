# Auto generated from rarelink_1_formal_criteria.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-03-23T15:59:01
# Schema: rarelink_1_formal_criteria
#
# id: https://github.com/BIH-CEI/RareLink/blob/develop/src/rarelink/v2.0.4/linkml/rarelink_1_formal_criteria.yaml
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
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_str
)
from rdflib import (
    URIRef
)
from linkml_runtime.utils.metamodelcore import XSDDate

metamodel_version = "1.7.0"
version = None


# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RARELINK = CurieNamespace('rarelink', 'https://github.com/BIH-CEI/RareLink/blob/develop/src/rarelink')
DEFAULT_ = RARELINK


# Types

# Class references
class FormalCriteriaSnomedct422549004(extended_str):
    pass


@dataclass(repr=False)
class FormalCriteria(YAMLRoot):
    """
    Section containing the RareLink (1) Formal Criteria Sheet
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RARELINK["FormalCriteria"]
    class_class_curie: ClassVar[str] = "rarelink:FormalCriteria"
    class_name: ClassVar[str] = "FormalCriteria"
    class_model_uri: ClassVar[URIRef] = RARELINK.FormalCriteria

    snomedct_422549004: Union[str, FormalCriteriaSnomedct422549004] = None
    snomedct_399423000: Union[str, XSDDate] = None
    rarelink_1_formal_criteria_complete: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.snomedct_422549004):
            self.MissingRequiredField("snomedct_422549004")
        if not isinstance(self.snomedct_422549004, FormalCriteriaSnomedct422549004):
            self.snomedct_422549004 = FormalCriteriaSnomedct422549004(self.snomedct_422549004)

        if self._is_empty(self.snomedct_399423000):
            self.MissingRequiredField("snomedct_399423000")
        if not isinstance(self.snomedct_399423000, XSDDate):
            self.snomedct_399423000 = XSDDate(self.snomedct_399423000)

        if self.rarelink_1_formal_criteria_complete is not None and not isinstance(self.rarelink_1_formal_criteria_complete, str):
            self.rarelink_1_formal_criteria_complete = str(self.rarelink_1_formal_criteria_complete)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.snomedct_422549004 = Slot(uri=RARELINK.snomedct_422549004, name="snomedct_422549004", curie=RARELINK.curie('snomedct_422549004'),
                   model_uri=RARELINK.snomedct_422549004, domain=None, range=URIRef)

slots.snomedct_399423000 = Slot(uri=RARELINK.snomedct_399423000, name="snomedct_399423000", curie=RARELINK.curie('snomedct_399423000'),
                   model_uri=RARELINK.snomedct_399423000, domain=None, range=Union[str, XSDDate])

slots.rarelink_1_formal_criteria_complete = Slot(uri=RARELINK.rarelink_1_formal_criteria_complete, name="rarelink_1_formal_criteria_complete", curie=RARELINK.curie('rarelink_1_formal_criteria_complete'),
                   model_uri=RARELINK.rarelink_1_formal_criteria_complete, domain=None, range=Optional[str])
