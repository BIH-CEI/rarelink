# RareLink Encounter - RareLink Implementation Guide v2.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **RareLink Encounter**

## Resource Profile: RareLink Encounter 

| | |
| :--- | :--- |
| *Official URL*:https://rarelink.bih-charite.de/fhir/StructureDefinition/rarelink-encounter | *Version*:2.0.0 |
| Draft as of 2025-12-15 | *Computable Name*:RareLinkEncounter |

 
A RareLink-specific Encounter profile based on the Encounter resource. 

**Usages:**

* This Profile is not used by any profiles in this Implementation Guide

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/rarelink-ig|current/StructureDefinition/rarelink-encounter)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-rarelink-encounter.csv), [Excel](StructureDefinition-rarelink-encounter.xlsx), [Schematron](StructureDefinition-rarelink-encounter.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "rarelink-encounter",
  "url" : "https://rarelink.bih-charite.de/fhir/StructureDefinition/rarelink-encounter",
  "version" : "2.0.0",
  "name" : "RareLinkEncounter",
  "title" : "RareLink Encounter",
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
  "description" : "A RareLink-specific Encounter profile based on the Encounter resource.",
  "fhirVersion" : "4.0.1",
  "mapping" : [
    {
      "identity" : "workflow",
      "uri" : "http://hl7.org/fhir/workflow",
      "name" : "Workflow Pattern"
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
      "identity" : "v2",
      "uri" : "http://hl7.org/v2",
      "name" : "HL7 v2 Mapping"
    }
  ],
  "kind" : "resource",
  "abstract" : false,
  "type" : "Encounter",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Encounter",
  "derivation" : "constraint",
  "differential" : {
    "element" : [
      {
        "id" : "Encounter",
        "path" : "Encounter"
      },
      {
        "id" : "Encounter.status",
        "path" : "Encounter.status",
        "binding" : {
          "strength" : "required",
          "valueSet" : "http://hl7.org/fhir/ValueSet/encounter-status"
        }
      },
      {
        "id" : "Encounter.class",
        "path" : "Encounter.class",
        "binding" : {
          "strength" : "required",
          "valueSet" : "https://rarelink.bih-charite.de/fhir/ValueSet/encounter-class-vs"
        }
      },
      {
        "id" : "Encounter.subject",
        "path" : "Encounter.subject",
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
        "id" : "Encounter.subject.reference",
        "path" : "Encounter.subject.reference",
        "mustSupport" : true
      },
      {
        "id" : "Encounter.subject.identifier",
        "path" : "Encounter.subject.identifier",
        "mustSupport" : true
      }
    ]
  }
}

```
