# Age at Diagnosis - RareLink Implementation Guide v2.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Age at Diagnosis**

## Extension: Age at Diagnosis 

| | |
| :--- | :--- |
| *Official URL*:https://rarelink.bih-charite.de/fhir/StructureDefinition/age-at-diagnosis | *Version*:2.0.0 |
| Draft as of 2025-12-15 | *Computable Name*:AgeAtDiagnosis |

ERDRI-CDS - The age at which the condition was diagnosed.

**Context of Use**

**Usage info**

**Usages:**

* Use this Extension: [RareLink IPS Condition](StructureDefinition-rarelink-ips-condition.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/rarelink-ig|current/StructureDefinition/age-at-diagnosis)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-age-at-diagnosis.csv), [Excel](StructureDefinition-age-at-diagnosis.xlsx), [Schematron](StructureDefinition-age-at-diagnosis.sch) 

#### Terminology Bindings

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "age-at-diagnosis",
  "url" : "https://rarelink.bih-charite.de/fhir/StructureDefinition/age-at-diagnosis",
  "version" : "2.0.0",
  "name" : "AgeAtDiagnosis",
  "title" : "Age at Diagnosis",
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
  "description" : "ERDRI-CDS - The age at which the condition was diagnosed.",
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
        "short" : "Age at Diagnosis",
        "definition" : "ERDRI-CDS - The age at which the condition was diagnosed."
      },
      {
        "id" : "Extension.extension",
        "path" : "Extension.extension",
        "max" : "0"
      },
      {
        "id" : "Extension.url",
        "path" : "Extension.url",
        "fixedUri" : "https://rarelink.bih-charite.de/fhir/StructureDefinition/age-at-diagnosis"
      },
      {
        "id" : "Extension.value[x]",
        "path" : "Extension.value[x]",
        "type" : [
          {
            "code" : "CodeableConcept"
          }
        ],
        "binding" : {
          "strength" : "extensible",
          "valueSet" : "https://rarelink.bih-charite.de/fhir/ValueSet/age-at-diagnosis-vs"
        }
      }
    ]
  }
}

```
