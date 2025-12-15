# RareLink Condition for Undiagnosed RD Case - RareLink Implementation Guide v2.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **RareLink Condition for Undiagnosed RD Case**

## Resource Profile: RareLink Condition for Undiagnosed RD Case 

| | |
| :--- | :--- |
| *Official URL*:https://rarelink.bih-charite.de/fhir/StructureDefinition/rarelink-condition-undiagnosed-rd-case | *Version*:2.0.0 |
| Draft as of 2025-12-15 | *Computable Name*:RareLinkConditionUndiagnosedRDCase |

 
A RareLink-specific Condition profile for documenting undiagnosed rare disease cases based on the IPS Condition profile. 

**Usages:**

* This Profile is not used by any profiles in this Implementation Guide

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/rarelink-ig|current/StructureDefinition/rarelink-condition-undiagnosed-rd-case)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-rarelink-condition-undiagnosed-rd-case.csv), [Excel](StructureDefinition-rarelink-condition-undiagnosed-rd-case.xlsx), [Schematron](StructureDefinition-rarelink-condition-undiagnosed-rd-case.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "rarelink-condition-undiagnosed-rd-case",
  "url" : "https://rarelink.bih-charite.de/fhir/StructureDefinition/rarelink-condition-undiagnosed-rd-case",
  "version" : "2.0.0",
  "name" : "RareLinkConditionUndiagnosedRDCase",
  "title" : "RareLink Condition for Undiagnosed RD Case",
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
  "description" : "A RareLink-specific Condition profile for documenting undiagnosed rare disease cases based on the IPS Condition profile.",
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
    }
  ],
  "kind" : "resource",
  "abstract" : false,
  "type" : "Condition",
  "baseDefinition" : "http://hl7.org/fhir/uv/ips/StructureDefinition/Condition-uv-ips",
  "derivation" : "constraint",
  "differential" : {
    "element" : [
      {
        "id" : "Condition",
        "path" : "Condition"
      },
      {
        "id" : "Condition.code.coding",
        "path" : "Condition.code.coding",
        "min" : 1,
        "max" : "1"
      },
      {
        "id" : "Condition.code.coding.code",
        "path" : "Condition.code.coding.code",
        "binding" : {
          "strength" : "required",
          "valueSet" : "https://rarelink.bih-charite.de/fhir/ValueSet/undiagnosed-rd-case-vs"
        }
      },
      {
        "id" : "Condition.subject",
        "path" : "Condition.subject",
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
        "id" : "Condition.subject.identifier",
        "path" : "Condition.subject.identifier",
        "mustSupport" : true
      }
    ]
  }
}

```
