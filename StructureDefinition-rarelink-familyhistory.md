# RareLink Family History - RareLink Implementation Guide v2.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **RareLink Family History**

## Resource Profile: RareLink Family History 

| | |
| :--- | :--- |
| *Official URL*:https://rarelink.bih-charite.de/fhir/StructureDefinition/rarelink-familyhistory | *Version*:2.0.0 |
| Draft as of 2025-12-15 | *Computable Name*:RareLinkFamilyHistory |

 
A RareLink-specific FamilyMemberHistory profile based on the FamilyMemberHistory resource. 

**Usages:**

* This Profile is not used by any profiles in this Implementation Guide

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/rarelink-ig|current/StructureDefinition/rarelink-familyhistory)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-rarelink-familyhistory.csv), [Excel](StructureDefinition-rarelink-familyhistory.xlsx), [Schematron](StructureDefinition-rarelink-familyhistory.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "rarelink-familyhistory",
  "url" : "https://rarelink.bih-charite.de/fhir/StructureDefinition/rarelink-familyhistory",
  "version" : "2.0.0",
  "name" : "RareLinkFamilyHistory",
  "title" : "RareLink Family History",
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
  "description" : "A RareLink-specific FamilyMemberHistory profile based on the FamilyMemberHistory resource.",
  "fhirVersion" : "4.0.1",
  "mapping" : [
    {
      "identity" : "workflow",
      "uri" : "http://hl7.org/fhir/workflow",
      "name" : "Workflow Pattern"
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
  "type" : "FamilyMemberHistory",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/FamilyMemberHistory",
  "derivation" : "constraint",
  "differential" : {
    "element" : [
      {
        "id" : "FamilyMemberHistory",
        "path" : "FamilyMemberHistory"
      },
      {
        "id" : "FamilyMemberHistory.extension",
        "path" : "FamilyMemberHistory.extension",
        "slicing" : {
          "discriminator" : [
            {
              "type" : "value",
              "path" : "url"
            }
          ],
          "ordered" : false,
          "rules" : "open"
        }
      },
      {
        "id" : "FamilyMemberHistory.extension:propositus",
        "path" : "FamilyMemberHistory.extension",
        "sliceName" : "propositus",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "code" : "Extension",
            "profile" : [
              "https://rarelink.bih-charite.de/fhir/StructureDefinition/propositus"
            ]
          }
        ]
      },
      {
        "id" : "FamilyMemberHistory.extension:consanguinity",
        "path" : "FamilyMemberHistory.extension",
        "sliceName" : "consanguinity",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "code" : "Extension",
            "profile" : [
              "https://rarelink.bih-charite.de/fhir/StructureDefinition/consanguinity"
            ]
          }
        ]
      },
      {
        "id" : "FamilyMemberHistory.patient",
        "path" : "FamilyMemberHistory.patient",
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
        "id" : "FamilyMemberHistory.patient.reference",
        "path" : "FamilyMemberHistory.patient.reference",
        "mustSupport" : true
      },
      {
        "id" : "FamilyMemberHistory.patient.identifier",
        "path" : "FamilyMemberHistory.patient.identifier",
        "mustSupport" : true
      },
      {
        "id" : "FamilyMemberHistory.relationship.coding",
        "path" : "FamilyMemberHistory.relationship.coding",
        "min" : 1,
        "max" : "1"
      },
      {
        "id" : "FamilyMemberHistory.relationship.coding.system",
        "path" : "FamilyMemberHistory.relationship.coding.system",
        "patternUri" : "http://snomed.info/sct"
      },
      {
        "id" : "FamilyMemberHistory.relationship.coding.code",
        "path" : "FamilyMemberHistory.relationship.coding.code",
        "binding" : {
          "strength" : "required",
          "valueSet" : "https://rarelink.bih-charite.de/fhir/ValueSet/family-relationship-vs"
        }
      },
      {
        "id" : "FamilyMemberHistory.sex.coding",
        "path" : "FamilyMemberHistory.sex.coding",
        "min" : 1,
        "max" : "1"
      },
      {
        "id" : "FamilyMemberHistory.sex.coding.system",
        "path" : "FamilyMemberHistory.sex.coding.system",
        "patternUri" : "http://hl7.org/fhir/administrative-gender"
      },
      {
        "id" : "FamilyMemberHistory.sex.coding.code",
        "path" : "FamilyMemberHistory.sex.coding.code",
        "binding" : {
          "strength" : "extensible",
          "valueSet" : "https://rarelink.bih-charite.de/fhir/ValueSet/family-sex-vs"
        }
      }
    ]
  }
}

```
