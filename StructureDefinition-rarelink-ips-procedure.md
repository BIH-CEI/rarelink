# RareLink IPS Procedure - RareLink Implementation Guide v2.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **RareLink IPS Procedure**

## Resource Profile: RareLink IPS Procedure 

| | |
| :--- | :--- |
| *Official URL*:https://rarelink.bih-charite.de/fhir/StructureDefinition/rarelink-ips-procedure | *Version*:2.0.0 |
| Draft as of 2025-12-15 | *Computable Name*:RareLinkIPSProcedure |

 
A RareLink-specific profile for the IPS Procedure resource. 

**Usages:**

* This Profile is not used by any profiles in this Implementation Guide

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/rarelink-ig|current/StructureDefinition/rarelink-ips-procedure)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-rarelink-ips-procedure.csv), [Excel](StructureDefinition-rarelink-ips-procedure.xlsx), [Schematron](StructureDefinition-rarelink-ips-procedure.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "rarelink-ips-procedure",
  "url" : "https://rarelink.bih-charite.de/fhir/StructureDefinition/rarelink-ips-procedure",
  "version" : "2.0.0",
  "name" : "RareLinkIPSProcedure",
  "title" : "RareLink IPS Procedure",
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
  "description" : "A RareLink-specific profile for the IPS Procedure resource.",
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
  "type" : "Procedure",
  "baseDefinition" : "http://hl7.org/fhir/uv/ips/StructureDefinition/Procedure-uv-ips",
  "derivation" : "constraint",
  "differential" : {
    "element" : [
      {
        "id" : "Procedure",
        "path" : "Procedure"
      },
      {
        "id" : "Procedure.status",
        "path" : "Procedure.status",
        "binding" : {
          "strength" : "required",
          "valueSet" : "http://hl7.org/fhir/ValueSet/event-status"
        }
      },
      {
        "id" : "Procedure.code.coding",
        "path" : "Procedure.code.coding",
        "min" : 1,
        "max" : "1"
      },
      {
        "id" : "Procedure.code.coding.system",
        "path" : "Procedure.code.coding.system",
        "binding" : {
          "strength" : "required",
          "valueSet" : "http://hl7.org/fhir/uv/ips/ValueSet/procedures-uv-ips"
        }
      },
      {
        "id" : "Procedure.subject",
        "path" : "Procedure.subject",
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
        "id" : "Procedure.subject.identifier",
        "path" : "Procedure.subject.identifier",
        "mustSupport" : true
      },
      {
        "id" : "Procedure.bodySite.coding.system",
        "path" : "Procedure.bodySite.coding.system",
        "patternUri" : "http://snomed.info/sct"
      }
    ]
  }
}

```
