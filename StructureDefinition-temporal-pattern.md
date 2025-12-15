# Phenotype Temporal Pattern - RareLink Implementation Guide v2.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Phenotype Temporal Pattern**

## Extension: Phenotype Temporal Pattern 

| | |
| :--- | :--- |
| *Official URL*:https://rarelink.bih-charite.de/fhir/StructureDefinition/temporal-pattern | *Version*:2.0.0 |
| Draft as of 2025-12-15 | *Computable Name*:TemporalPattern |

The speed at which a disease manifestations appear and develop.

**Context of Use**

**Usage info**

**Usages:**

* Use this Extension: [RareLink Observation Phenotypic Feature](StructureDefinition-rarelink-phenotypic-feature.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/rarelink-ig|current/StructureDefinition/temporal-pattern)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-temporal-pattern.csv), [Excel](StructureDefinition-temporal-pattern.xlsx), [Schematron](StructureDefinition-temporal-pattern.sch) 

#### Terminology Bindings

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "temporal-pattern",
  "url" : "https://rarelink.bih-charite.de/fhir/StructureDefinition/temporal-pattern",
  "version" : "2.0.0",
  "name" : "TemporalPattern",
  "title" : "Phenotype Temporal Pattern",
  "status" : "draft",
  "date" : "2025-12-15T08:42:23+00:00",
  "publisher" : "Berlin Institute of Health - Charité Universitätsmedizin Berlin",
  "contact" : [
    {
      "name" : "Berlin Institute of Health - Charité Universitätsmedizin Berlin",
      "telecom" : [
        {
          "system" : "url",
          "value" : "https://github.com/BIH-CEI/RareLink"
        },
        {
          "system" : "email",
          "value" : "adam.graefe@charite.de"
        }
      ]
    }
  ],
  "description" : "The speed at which a disease manifestations appear and develop.",
  "fhirVersion" : "4.0.1",
  "mapping" : [
    {
      "identity" : "rim",
      "uri" : "http://hl7.org/v3",
      "name" : "RIM Mapping"
    }
  ],
  "kind" : "complex-type",
  "abstract" : false,
  "context" : [
    {
      "type" : "element",
      "expression" : "Element"
    }
  ],
  "type" : "Extension",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Extension",
  "derivation" : "constraint",
  "differential" : {
    "element" : [
      {
        "id" : "Extension",
        "path" : "Extension",
        "short" : "Phenotype Temporal Pattern",
        "definition" : "The speed at which a disease manifestations appear and develop."
      },
      {
        "id" : "Extension.extension",
        "path" : "Extension.extension",
        "max" : "0"
      },
      {
        "id" : "Extension.url",
        "path" : "Extension.url",
        "fixedUri" : "https://rarelink.bih-charite.de/fhir/StructureDefinition/temporal-pattern"
      },
      {
        "id" : "Extension.value[x]",
        "path" : "Extension.value[x]",
        "type" : [
          {
            "code" : "CodeableConcept"
          }
        ]
      },
      {
        "id" : "Extension.value[x].coding",
        "path" : "Extension.value[x].coding",
        "min" : 1,
        "max" : "1"
      },
      {
        "id" : "Extension.value[x].coding.system",
        "path" : "Extension.value[x].coding.system",
        "patternUri" : "http://purl.obolibrary.org/obo/hp.owl"
      },
      {
        "id" : "Extension.value[x].coding.code",
        "path" : "Extension.value[x].coding.code",
        "binding" : {
          "strength" : "required",
          "valueSet" : "https://rarelink.bih-charite.de/fhir/ValueSet/temporal-pattern-vs"
        }
      }
    ]
  }
}

```
