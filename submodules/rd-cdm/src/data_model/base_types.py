from dataclasses import dataclass, field
import decimal
from typing import List, Optional, Union, Literal
from datetime import datetime

@dataclass(slots=True, frozen=True)
class CodeSystem:
    """
    Represents a system of codes used to define concepts (e.g., SNOMED CT, 
    LOINC, ICD). A CodeSystem holds codes and related metadata for standardized 
    data representation in domains like healthcare and bioinformatics.

    Attributes:
    name : str
        The full name of the CodeSystem (e.g., "SNOMED CT").
    
    namespace_prefix : str
        A short prefix used to reference the CodeSystem (e.g., "SNOMED").
    
    url : str, optional
        A URL for more information about the CodeSystem (e.g., documentation).
    
    iri_prefix : str, optional
        IRI prefix for representing codes in semantic web technologies.
    
    synonyms : list, optional
        Alternative names or abbreviations for the CodeSystem.
    
    Methods:
    __eq__(self, other):
        Checks equality based on `namespace_prefix` or `synonyms`.
    
    __str__(self):
        Returns a simple string representation of the CodeSystem.
    
    __repr__(self):
        Same as __str__, useful for debugging.
    """

    name: str
    namespace_prefix: str
    url: str = None
    iri_prefix: str = None
    synonyms: list = field(default_factory=list)

    def __eq__(self, other):
        if not isinstance(other, CodeSystem):
            return False
        return (self.namespace_prefix == other.namespace_prefix or
                self.namespace_prefix in other.synonyms)

    def __str__(self):
        return f"CodeSystem(name={self.name}, namespace_prefix={self.namespace_prefix})"

    def __repr__(self):
        return str(self)


@dataclass(frozen=True, slots=True, eq=True)
class Coding:
    """Data class for Coding

    A `Coding` is a representation of a concept defined by a code and a code system. It is used in the `CodeableConcept`
    data class.

    :ivar system: The code system that defines the code.
    :ivar code: The code that represents the concept (treated as 'Code').
    :ivar display: The human-readable representation of the concept.
    :ivar text: A human-readable description or additional text of the concept.
    """
    system: Union[str, CodeSystem] = field(compare=True)
    code: str = field(compare=True)  # Assuming "Code" is a string representation of the code.
    display: str = field(default="", compare=False)
    text: str = field(default="", compare=False)

    @staticmethod
    def parse_coding(
        coding_str: str,
        resources: List[CodeSystem],
        compliance: Literal['soft', 'hard'] = 'soft'
    ) -> 'Coding':
        """Parse a string representing a coding into a Coding object.

        Expected format: <namespace_prefix>:<code>.

        E.g.:
        >>> snomed = CodeSystem(name="SNOMED CT", namespace_prefix="SNOMED", url="https://snomed.org")
        >>> Coding.parse_coding("SNOMED:404684003", [snomed])
        Coding(system=CodeSystem(name=SNOMED CT, namespace_prefix=SNOMED), code='404684003', display='', text='')

        This function recognizes name space prefixes belonging to code systems provided in the resources list.
        If a name space is not found, it returns a Coding object with the system as the name space prefix and the code.

        :param coding_str: A string representing a coding.
        :param resources: A list of all resources (code systems) used.
        :param compliance: Whether to throw a ValueError or just issue a warning if a name space prefix is not found.
        :return: a Coding object as specified in the input string.
        """
        try:
            namespace, code = coding_str.split(":")
        except ValueError:
            raise ValueError(f"Invalid coding format: {coding_str}. Expected format: <namespace_prefix>:<code>")

        for resource in resources:
            if resource.namespace_prefix == namespace:
                return Coding(system=resource, code=code)

        if compliance == 'hard':
            raise ValueError(f"Code system with namespace prefix '{namespace}' not found in resources.")
        else:
            print(f"Warning: Code system with namespace prefix '{namespace}' not found in resources.")
            print(f"Warning: Returning Coding object with system as namespace prefix and code as '{code}'")
            return Coding(system=namespace, code=code)

    def __str__(self):
        if isinstance(self.system, CodeSystem):
            return f"{self.system.namespace_prefix}:{self.code}"
        return f"{self.system}:{self.code}"


@dataclass(frozen=True, slots=True, eq=True)
class CodeableConcept:
    """Data class for CodeableConcept

    A `CodeableConcept` represents a concept defined by one or more codings. It may also have a text representation.

    :ivar coding: A list of `Coding` instances that define the concept.
    :ivar text: A text representation of the concept.
    """
    coding: List[Coding] = field(compare=True)
    text: str = field(default="", compare=False)

    def __str__(self):
        return f"CodeableConcept(codings=[{', '.join(map(str, self.coding))}], text={self.text})"
    
from dataclasses import dataclass
from datetime import datetime
from typing import Union

@dataclass(frozen=True, slots=True)
class Date:
    """Represents a date in the formats YYYY, YYYY-MM, or YYYY-MM-DD."""
    value: Union[str, datetime]

    def __post_init__(self):
        if not self.is_valid_format(self.value):
            raise ValueError(f"Invalid date format: {self.value}")

    @staticmethod
    def is_valid_format(date_str):
        """Validate that the date is in the correct format."""
        formats = ["%Y", "%Y-%m", "%Y-%m-%d"]
        for fmt in formats:
            try:
                datetime.strptime(date_str, fmt)
                return True
            except ValueError:
                continue
        return False

    def to_json(self):
        """Return the date as a string for JSON serialization."""
        return str(self.value)


@dataclass(frozen=True, slots=True)
class Code:
    """Represents a coded value."""
    system: str
    code: str

    def to_json(self):
        """Return a dictionary representing this Code."""
        return {"system": self.system, "code": self.code}


@dataclass(frozen=True, slots=True)
class Address:
    """Represents an address."""
    country: str
    street: Optional[str] = field(default=None)
    city: Optional[str] = field(default=None)
    zip_code: Optional[str] = field(default=None)

    def to_json(self):
        """Return a dictionary representing this Address, excluding None values."""
        return {
            "country": self.country,
            "street": self.street if self.street else "",
            "city": self.city if self.city else "",
            "zip_code": self.zip_code if self.zip_code else ""
        }

@dataclass(frozen=True, slots=True)
class Identifier:
    """Represents an identifier."""
    id: str
    type: str

    def to_json(self):
        """Return a dictionary representing this Identifier."""
        return {"id": self.id, "type": self.type}
    

@dataclass(frozen=True, slots=True)
class String:
    """Represents a string data type."""
    value: str

    def __post_init__(self):
        if not isinstance(self.value, str):
            raise ValueError(
                f"Invalid value for String: {self.value}. Expected a string.")

@dataclass(frozen=True, slots=True)
class Boolean:
    """Represents a boolean data type."""
    value: bool

    def __post_init__(self):
        if not isinstance(self.value, bool):
            raise ValueError(
                f"Invalid value for Boolean: {self.value}. Expected a boolean.")
        
@dataclass(frozen=True, slots=True)
class Integer:
    """Represents an integer data type."""
    value: int

    def __post_init__(self):
        if not isinstance(self.value, int):
            raise ValueError(
                f"Invalid value for Integer: {self.value}. Expected an integer.")

@dataclass(frozen=True, slots=True)
class Value:
    """Represents a value."""
    value: Union[float]

    def __post_init__(self):
        if not isinstance(self.value, (float)):
            raise ValueError(
                f"Invalid value for Value: {self.value}. Expected a float.")

    def to_json(self):
        """Return a dictionary representing this Value."""
        return {"value": self.value}