# RareLink Observation Gestation at Birth - RareLink Implementation Guide v2.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **RareLink Observation Gestation at Birth**

## Resource Profile: RareLink Observation Gestation at Birth 

| | |
| :--- | :--- |
| *Official URL*:https://rarelink.bih-charite.de/fhir/StructureDefinition/rarelink-observation-gestation-at-birth | *Version*:2.0.0 |
| Draft as of 2025-12-15 | *Computable Name*:RareLinkGestationAtBirth |

 
A RareLink-specific profile for capturing gestation length at birth. 

**Usages:**

* This Profile is not used by any profiles in this Implementation Guide

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/rarelink-ig|current/StructureDefinition/rarelink-observation-gestation-at-birth)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-rarelink-observation-gestation-at-birth.csv), [Excel](StructureDefinition-rarelink-observation-gestation-at-birth.xlsx), [Schematron](StructureDefinition-rarelink-observation-gestation-at-birth.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "rarelink-observation-gestation-at-birth",
  "url" : "https://rarelink.bih-charite.de/fhir/StructureDefinition/rarelink-observation-gestation-at-birth",
  "version" : "2.0.0",
  "name" : "RareLinkGestationAtBirth",
  "title" : "RareLink Observation Gestation at Birth",
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
  "description" : "A RareLink-specific profile for capturing gestation length at birth.",
  "fhirVersion" : "4.0.1",
  "mapping" : [
    {
      "identity" : "workflow",
      "uri" : "http://hl7.org/fhir/workflow",
      "name" : "Workflow Pattern"
    },
    {
      "identity" : "sct-concept",
      "uri" : "http://snomed.info/conceptdomain",
      "name" : "SNOMED CT Concept Domain Binding"
    },
    {
      "identity" : "v2",
      "uri" : "http://hl7.org/v2",
      "name" : "HL7 v2 Mapping"
    },
    {
      "identity" : "rim",
      "uri" : "http://hl7.org/v3",
      "name" : "RIM Mapping"
    },
    {
      "identity" : "w5",
      "uri" : "http://hl7.org/fhir/fivews",
      "name" : "FiveWs Pattern Mapping"
    },
    {
      "identity" : "sct-attr",
      "uri" : "http://snomed.org/attributebinding",
      "name" : "SNOMED CT Attribute Binding"
    }
  ],
  "kind" : "resource",
  "abstract" : false,
  "type" : "Observation",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Observation",
  "derivation" : "constraint",
  "differential" : {
    "element" : [
      {
        "id" : "Observation",
        "path" : "Observation"
      },
      {
        "id" : "Observation.status",
        "path" : "Observation.status",
        "patternCode" : "final"
      },
      {
        "id" : "Observation.code",
        "path" : "Observation.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "http://snomed.info/sct",
              "code" : "412726003"
            }
          ]
        }
      },
      {
        "id" : "Observation.code.coding",
        "path" : "Observation.code.coding",
        "min" : 1,
        "max" : "1"
      },
      {
        "id" : "Observation.subject",
        "path" : "Observation.subject",
        "min" : 1,
        "type" : [
          {
            "code" : "Reference",
            "targetProfile" : [
              "https://rarelink.bih-charite.de/fhir/StructureDefinition/rarelink-ips-patient"
            ]
          }
        ]
      },
      {
        "id" : "Observation.subject.reference",
        "path" : "Observation.subject.reference",
        "mustSupport" : true
      },
      {
        "id" : "Observation.subject.identifier",
        "path" : "Observation.subject.identifier",
        "mustSupport" : true
      },
      {
        "id" : "Observation.effective[x]",
        "path" : "Observation.effective[x]",
        "slicing" : {
          "discriminator" : [
            {
              "type" : "type",
              "path" : "$this"
            }
          ],
          "ordered" : false,
          "rules" : "open"
        }
      },
      {
        "id" : "Observation.effective[x]:effectiveDateTime",
        "path" : "Observation.effective[x]",
        "sliceName" : "effectiveDateTime",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "code" : "dateTime"
          }
        ],
        "mustSupport" : true
      },
      {
        "id" : "Observation.component",
        "path" : "Observation.component",
        "slicing" : {
          "discriminator" : [
            {
              "type" : "pattern",
              "path" : "code"
            }
          ],
          "rules" : "open"
        }
      },
      {
        "id" : "Observation.component:length_of_gestation_in_weeks",
        "path" : "Observation.component",
        "sliceName" : "length_of_gestation_in_weeks",
        "min" : 0,
        "max" : "1"
      },
      {
        "id" : "Observation.component:length_of_gestation_in_weeks.code.coding",
        "path" : "Observation.component.code.coding",
        "min" : 1,
        "max" : "1"
      },
      {
        "id" : "Observation.component:length_of_gestation_in_weeks.code.coding.system",
        "path" : "Observation.component.code.coding.system",
        "patternUri" : "http://snomed.info/sct"
      },
      {
        "id" : "Observation.component:length_of_gestation_in_weeks.code.coding.code",
        "path" : "Observation.component.code.coding.code",
        "patternCode" : "412726003"
      },
      {
        "id" : "Observation.component:length_of_gestation_in_weeks.code.coding.display",
        "path" : "Observation.component.code.coding.display",
        "patternString" : "Length of gestation at birth"
      },
      {
        "id" : "Observation.component:length_of_gestation_in_weeks.value[x]",
        "path" : "Observation.component.value[x]",
        "type" : [
          {
            "code" : "Quantity"
          }
        ]
      },
      {
        "id" : "Observation.component:length_of_gestation_in_weeks.value[x].unit",
        "path" : "Observation.component.value[x].unit",
        "patternString" : "week"
      },
      {
        "id" : "Observation.component:length_of_gestation_in_weeks.value[x].system",
        "path" : "Observation.component.value[x].system",
        "patternUri" : "http://www.ontobee.org/ontology/UO"
      },
      {
        "id" : "Observation.component:length_of_gestation_in_weeks.value[x].code",
        "path" : "Observation.component.value[x].code",
        "patternCode" : "0000034"
      },
      {
        "id" : "Observation.component:length_of_gestation_in_days",
        "path" : "Observation.component",
        "sliceName" : "length_of_gestation_in_days",
        "min" : 0,
        "max" : "1"
      },
      {
        "id" : "Observation.component:length_of_gestation_in_days.code.coding",
        "path" : "Observation.component.code.coding",
        "min" : 1,
        "max" : "1"
      },
      {
        "id" : "Observation.component:length_of_gestation_in_days.code.coding.system",
        "path" : "Observation.component.code.coding.system",
        "patternUri" : "http://snomed.info/sct"
      },
      {
        "id" : "Observation.component:length_of_gestation_in_days.code.coding.code",
        "path" : "Observation.component.code.coding.code",
        "patternCode" : "412726003"
      },
      {
        "id" : "Observation.component:length_of_gestation_in_days.code.coding.display",
        "path" : "Observation.component.code.coding.display",
        "patternString" : "Length of gestation at birth"
      },
      {
        "id" : "Observation.component:length_of_gestation_in_days.value[x]",
        "path" : "Observation.component.value[x]",
        "type" : [
          {
            "code" : "Quantity"
          }
        ]
      },
      {
        "id" : "Observation.component:length_of_gestation_in_days.value[x].unit",
        "path" : "Observation.component.value[x].unit",
        "patternString" : "day"
      },
      {
        "id" : "Observation.component:length_of_gestation_in_days.value[x].system",
        "path" : "Observation.component.value[x].system",
        "patternUri" : "http://www.ontobee.org/ontology/UO"
      },
      {
        "id" : "Observation.component:length_of_gestation_in_days.value[x].code",
        "path" : "Observation.component.value[x].code",
        "patternCode" : "0000033"
      }
    ]
  }
}

```
