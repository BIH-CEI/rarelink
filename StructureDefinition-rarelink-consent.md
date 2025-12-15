# RareLink Consent - RareLink Implementation Guide v2.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **RareLink Consent**

## Resource Profile: RareLink Consent 

| | |
| :--- | :--- |
| *Official URL*:https://rarelink.bih-charite.de/fhir/StructureDefinition/rarelink-consent | *Version*:2.0.0 |
| Draft as of 2025-12-15 | *Computable Name*:RareLinkConsent |

 
A RareLink-specific Consent profile based on the Consent resource. 

**Usages:**

* This Profile is not used by any profiles in this Implementation Guide

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/rarelink-ig|current/StructureDefinition/rarelink-consent)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-rarelink-consent.csv), [Excel](StructureDefinition-rarelink-consent.xlsx), [Schematron](StructureDefinition-rarelink-consent.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "rarelink-consent",
  "url" : "https://rarelink.bih-charite.de/fhir/StructureDefinition/rarelink-consent",
  "version" : "2.0.0",
  "name" : "RareLinkConsent",
  "title" : "RareLink Consent",
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
  "description" : "A RareLink-specific Consent profile based on the Consent resource.",
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
  "type" : "Consent",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Consent",
  "derivation" : "constraint",
  "differential" : {
    "element" : [
      {
        "id" : "Consent",
        "path" : "Consent"
      },
      {
        "id" : "Consent.extension",
        "path" : "Consent.extension",
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
        "id" : "Consent.extension:consent_to_reuse_data",
        "path" : "Consent.extension",
        "sliceName" : "consent_to_reuse_data",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "code" : "Extension",
            "profile" : [
              "https://rarelink.bih-charite.de/fhir/StructureDefinition/erdri-consent-to-reuse-data"
            ]
          }
        ]
      },
      {
        "id" : "Consent.extension:agreement_to_be_contacted",
        "path" : "Consent.extension",
        "sliceName" : "agreement_to_be_contacted",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "code" : "Extension",
            "profile" : [
              "https://rarelink.bih-charite.de/fhir/StructureDefinition/erdri-agreement-to-be-contacted"
            ]
          }
        ]
      },
      {
        "id" : "Consent.scope.coding.system",
        "path" : "Consent.scope.coding.system",
        "patternUri" : "http://terminology.hl7.org/CodeSystem/consentscope"
      },
      {
        "id" : "Consent.scope.coding.code",
        "path" : "Consent.scope.coding.code",
        "patternCode" : "research"
      },
      {
        "id" : "Consent.category",
        "path" : "Consent.category",
        "max" : "1"
      },
      {
        "id" : "Consent.category.coding.system",
        "path" : "Consent.category.coding.system",
        "patternUri" : "http://terminology.hl7.org/CodeSystem/consentcategorycodes"
      },
      {
        "id" : "Consent.category.coding.code",
        "path" : "Consent.category.coding.code",
        "patternCode" : "research"
      },
      {
        "id" : "Consent.patient",
        "path" : "Consent.patient",
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
        "id" : "Consent.patient.reference",
        "path" : "Consent.patient.reference",
        "mustSupport" : true
      },
      {
        "id" : "Consent.patient.identifier",
        "path" : "Consent.patient.identifier",
        "mustSupport" : true
      },
      {
        "id" : "Consent.policy",
        "path" : "Consent.policy",
        "min" : 1,
        "max" : "1"
      }
    ]
  }
}

```
