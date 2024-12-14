# Auto generated from rarelink_code_systems.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-12-14T22:34:03
# Schema: rarelink_code_systems
#
# id: https://github.com/BIH-CEI/RareLink/code_systems
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

from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RARELINK = CurieNamespace('rarelink', 'https://github.com/BIH-CEI/rarelink/')
DEFAULT_ = RARELINK


# Types

# Class references



@dataclass(repr=False)
class CodeSystem(YAMLRoot):
    """
    A resource that defines a set of codes and their meanings. Examples include SNOMED CT, HPO, MONDO, OMIM, ORDO,
    LOINC, etc.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RARELINK["CodeSystem"]
    class_class_curie: ClassVar[str] = "rarelink:CodeSystem"
    class_name: ClassVar[str] = "CodeSystem"
    class_model_uri: ClassVar[URIRef] = RARELINK.CodeSystem

    name: str = None
    prefix: str = None
    url: Optional[str] = None
    iri_prefix: Optional[str] = None
    version: Optional[str] = None
    synonyms: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.prefix):
            self.MissingRequiredField("prefix")
        if not isinstance(self.prefix, str):
            self.prefix = str(self.prefix)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        if self.iri_prefix is not None and not isinstance(self.iri_prefix, str):
            self.iri_prefix = str(self.iri_prefix)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.name = Slot(uri=RARELINK.name, name="name", curie=RARELINK.curie('name'),
                   model_uri=RARELINK.name, domain=None, range=str)

slots.prefix = Slot(uri=RARELINK.prefix, name="prefix", curie=RARELINK.curie('prefix'),
                   model_uri=RARELINK.prefix, domain=None, range=str)

slots.url = Slot(uri=RARELINK.url, name="url", curie=RARELINK.curie('url'),
                   model_uri=RARELINK.url, domain=None, range=Optional[str])

slots.iri_prefix = Slot(uri=RARELINK.iri_prefix, name="iri_prefix", curie=RARELINK.curie('iri_prefix'),
                   model_uri=RARELINK.iri_prefix, domain=None, range=Optional[str])

slots.version = Slot(uri=RARELINK.version, name="version", curie=RARELINK.curie('version'),
                   model_uri=RARELINK.version, domain=None, range=Optional[str])

slots.synonyms = Slot(uri=RARELINK.synonyms, name="synonyms", curie=RARELINK.curie('synonyms'),
                   model_uri=RARELINK.synonyms, domain=None, range=Optional[Union[str, List[str]]])
