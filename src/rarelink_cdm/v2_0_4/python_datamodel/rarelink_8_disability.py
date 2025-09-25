# Auto generated from rarelink_8_disability.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-03-23T16:00:45
# Schema: rarelink_8_disability
#
# id: https://github.com/BIH-CEI/RareLink/rarelink_8_disability.yaml
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

from dataclasses import dataclass
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot
)
from rdflib import (
    URIRef
)

metamodel_version = "1.7.0"
version = None


# Namespaces
ICF = CurieNamespace('ICF', 'https://bioportal.bioontology.org/ontologies/ICF/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RARELINK = CurieNamespace('rarelink', 'https://github.com/BIH-CEI/rarelink/')
DEFAULT_ = RARELINK


# Types

# Class references



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
    class_model_uri: ClassVar[URIRef] = RARELINK.Disability

    rarelink_icf_score: str = None
    rarelink_8_disability_complete: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.rarelink_icf_score):
            self.MissingRequiredField("rarelink_icf_score")
        if not isinstance(self.rarelink_icf_score, str):
            self.rarelink_icf_score = str(self.rarelink_icf_score)

        if self._is_empty(self.rarelink_8_disability_complete):
            self.MissingRequiredField("rarelink_8_disability_complete")
        if not isinstance(self.rarelink_8_disability_complete, str):
            self.rarelink_8_disability_complete = str(self.rarelink_8_disability_complete)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.rarelink_icf_score = Slot(uri=RARELINK.rarelink_icf_score, name="rarelink_icf_score", curie=RARELINK.curie('rarelink_icf_score'),
                   model_uri=RARELINK.rarelink_icf_score, domain=None, range=str)

slots.rarelink_8_disability_complete = Slot(uri=RARELINK.rarelink_8_disability_complete, name="rarelink_8_disability_complete", curie=RARELINK.curie('rarelink_8_disability_complete'),
                   model_uri=RARELINK.rarelink_8_disability_complete, domain=None, range=str)
