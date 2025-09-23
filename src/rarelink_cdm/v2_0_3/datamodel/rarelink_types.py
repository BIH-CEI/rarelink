# Auto generated from rarelink_types.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-03-02T17:06:12
# Schema: rarelink_types
#
# id: https://github.com/BIH-CEI/RareLink/types
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/


from linkml_runtime.utils.curienamespace import CurieNamespace

from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = None


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




# Enumerations


# Slots
class slots:
    pass


