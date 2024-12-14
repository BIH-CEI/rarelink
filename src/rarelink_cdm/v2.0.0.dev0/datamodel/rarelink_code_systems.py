# Auto generated from rarelink_code_systems.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-12-14T23:21:16
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
class CodeSystems(YAMLRoot):
    """
    A container for all code systems used in RareLink CDM. Each entry is a `CodeSystem` object that defines the
    metadata of the code system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RARELINK["CodeSystems"]
    class_class_curie: ClassVar[str] = "rarelink:CodeSystems"
    class_name: ClassVar[str] = "CodeSystems"
    class_model_uri: ClassVar[URIRef] = RARELINK.CodeSystems

    code_systems: Union[Union[dict, "CodeSystem"], List[Union[dict, "CodeSystem"]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.code_systems):
            self.MissingRequiredField("code_systems")
        self._normalize_inlined_as_dict(slot_name="code_systems", slot_type=CodeSystem, key_name="name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CodeSystem(YAMLRoot):
    """
    A class representing a CodeSystem, with fields for name, prefix, URL, version, and synonyms. This structure is
    reusable for defining and referencing code systems.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RARELINK["CodeSystem"]
    class_class_curie: ClassVar[str] = "rarelink:CodeSystem"
    class_name: ClassVar[str] = "CodeSystem"
    class_model_uri: ClassVar[URIRef] = RARELINK.CodeSystem

    name: str = None
    prefix: str = None
    version: str = None
    url: Optional[str] = None
    iri_prefix: Optional[str] = None
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

        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, str):
            self.version = str(self.version)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        if self.iri_prefix is not None and not isinstance(self.iri_prefix, str):
            self.iri_prefix = str(self.iri_prefix)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.codeSystems__code_systems = Slot(uri=RARELINK.code_systems, name="codeSystems__code_systems", curie=RARELINK.curie('code_systems'),
                   model_uri=RARELINK.codeSystems__code_systems, domain=None, range=Union[Union[dict, CodeSystem], List[Union[dict, CodeSystem]]])

slots.codeSystem__name = Slot(uri=RARELINK.name, name="codeSystem__name", curie=RARELINK.curie('name'),
                   model_uri=RARELINK.codeSystem__name, domain=None, range=str)

slots.codeSystem__prefix = Slot(uri=RARELINK.prefix, name="codeSystem__prefix", curie=RARELINK.curie('prefix'),
                   model_uri=RARELINK.codeSystem__prefix, domain=None, range=str)

slots.codeSystem__url = Slot(uri=RARELINK.url, name="codeSystem__url", curie=RARELINK.curie('url'),
                   model_uri=RARELINK.codeSystem__url, domain=None, range=Optional[str])

slots.codeSystem__version = Slot(uri=RARELINK.version, name="codeSystem__version", curie=RARELINK.curie('version'),
                   model_uri=RARELINK.codeSystem__version, domain=None, range=str)

slots.codeSystem__iri_prefix = Slot(uri=RARELINK.iri_prefix, name="codeSystem__iri_prefix", curie=RARELINK.curie('iri_prefix'),
                   model_uri=RARELINK.codeSystem__iri_prefix, domain=None, range=Optional[str])

slots.codeSystem__synonyms = Slot(uri=RARELINK.synonyms, name="codeSystem__synonyms", curie=RARELINK.curie('synonyms'),
                   model_uri=RARELINK.codeSystem__synonyms, domain=None, range=Optional[Union[str, List[str]]])
