from dataclasses import dataclass, field
from typing import List
from .base_types import CodeSystem, Code, Coding

@dataclass(slots=True, frozen=True)
class ValueSetChoice:
    """Data class representing a single choice in a value set."""
    choiceDisplay: str
    choiceCode: Coding
    choiceCodeSystem: CodeSystem

@dataclass(slots=True, frozen=True)
class ValueSet:
    """Data class representing a value set."""
    valueSetName: str
    valueSetOrigin: str
    valueSetLink: str
    display: str
    valueSetCode: Coding
    valueSetCodeSystem: CodeSystem
    valueSetChoices: List[ValueSetChoice] = field(default_factory=list)

