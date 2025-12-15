# RareLink IPS Condition - RareLink Implementation Guide v2.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **RareLink IPS Condition**

## Resource Profile: RareLink IPS Condition 

| | |
| :--- | :--- |
| *Official URL*:https://rarelink.bih-charite.de/fhir/StructureDefinition/rarelink-ips-condition | *Version*:2.0.0 |
| Draft as of 2025-12-15 | *Computable Name*:RareLinkIPSCondition |

 
A RareLink-specific Condition profile based on the IPS Condition profile. 

**Usages:**

* This Profile is not used by any profiles in this Implementation Guide

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/rarelink-ig|current/StructureDefinition/rarelink-ips-condition)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-rarelink-ips-condition.csv), [Excel](StructureDefinition-rarelink-ips-condition.xlsx), [Schematron](StructureDefinition-rarelink-ips-condition.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "rarelink-ips-condition",
  "url" : "https://rarelink.bih-charite.de/fhir/StructureDefinition/rarelink-ips-condition",
  "version" : "2.0.0",
  "name" : "RareLinkIPSCondition",
  "title" : "RareLink IPS Condition",
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
  "description" : "A RareLink-specific Condition profile based on the IPS Condition profile.",
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
        "id" : "Condition.extension",
        "path" : "Condition.extension",
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
        "id" : "Condition.extension:age_at_diagnosis",
        "path" : "Condition.extension",
        "sliceName" : "age_at_diagnosis",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "code" : "Extension",
            "profile" : [
              "https://rarelink.bih-charite.de/fhir/StructureDefinition/age-at-diagnosis"
            ]
          }
        ]
      },
      {
        "id" : "Condition.extension:age_at_onset",
        "path" : "Condition.extension",
        "sliceName" : "age_at_onset",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "code" : "Extension",
            "profile" : [
              "https://rarelink.bih-charite.de/fhir/StructureDefinition/age-at-onset"
            ]
          }
        ]
      },
      {
        "id" : "Condition.clinicalStatus",
        "path" : "Condition.clinicalStatus",
        "min" : 1,
        "binding" : {
          "strength" : "required",
          "valueSet" : "http://terminology.hl7.org/ValueSet/condition-clinical"
        }
      },
      {
        "id" : "Condition.verificationStatus",
        "path" : "Condition.verificationStatus",
        "min" : 1,
        "binding" : {
          "strength" : "required",
          "valueSet" : "http://terminology.hl7.org/ValueSet/condition-ver-status"
        }
      },
      {
        "id" : "Condition.severity.coding",
        "path" : "Condition.severity.coding",
        "max" : "1"
      },
      {
        "id" : "Condition.severity.coding.system",
        "path" : "Condition.severity.coding.system",
        "patternUri" : "http://snomed.info/sct"
      },
      {
        "id" : "Condition.severity.coding.code",
        "path" : "Condition.severity.coding.code",
        "binding" : {
          "strength" : "extensible",
          "valueSet" : "https://rarelink.bih-charite.de/fhir/ValueSet/severity-vs"
        }
      },
      {
        "id" : "Condition.bodySite",
        "path" : "Condition.bodySite",
        "mustSupport" : true
      },
      {
        "id" : "Condition.bodySite.coding",
        "path" : "Condition.bodySite.coding",
        "max" : "1"
      },
      {
        "id" : "Condition.bodySite.coding.system",
        "path" : "Condition.bodySite.coding.system",
        "patternUri" : "http://snomed.info/sct"
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
      },
      {
        "id" : "Condition.onset[x]",
        "path" : "Condition.onset[x]",
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
        "id" : "Condition.onset[x]:onsetDateTime",
        "path" : "Condition.onset[x]",
        "sliceName" : "onsetDateTime",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "extension" : [
              {
                "url" : "http://hl7.org/fhir/StructureDefinition/elementdefinition-type-must-support",
                "valueBoolean" : true
              }
            ],
            "code" : "dateTime"
          }
        ]
      }
    ]
  }
}

```
