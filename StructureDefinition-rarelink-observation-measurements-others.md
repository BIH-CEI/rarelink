# RareLink Observation Measurements (Others) - RareLink Implementation Guide v2.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **RareLink Observation Measurements (Others)**

## Resource Profile: RareLink Observation Measurements (Others) 

| | |
| :--- | :--- |
| *Official URL*:https://rarelink.bih-charite.de/fhir/StructureDefinition/rarelink-observation-measurements-others | *Version*:2.0.0 |
| Draft as of 2025-12-15 | *Computable Name*:RareLinkIPSMeasurementsOthers |

 
A RareLink-specific profile for measurements that do not fall under IPS laboratory, radiology, procedures, or vital signs. 

**Usages:**

* This Profile is not used by any profiles in this Implementation Guide

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/rarelink-ig|current/StructureDefinition/rarelink-observation-measurements-others)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-rarelink-observation-measurements-others.csv), [Excel](StructureDefinition-rarelink-observation-measurements-others.xlsx), [Schematron](StructureDefinition-rarelink-observation-measurements-others.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "rarelink-observation-measurements-others",
  "url" : "https://rarelink.bih-charite.de/fhir/StructureDefinition/rarelink-observation-measurements-others",
  "version" : "2.0.0",
  "name" : "RareLinkIPSMeasurementsOthers",
  "title" : "RareLink Observation Measurements (Others)",
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
  "description" : "A RareLink-specific profile for measurements that do not fall under IPS laboratory, radiology, procedures, or vital signs.",
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
        "mustSupport" : true
      },
      {
        "id" : "Observation.category",
        "path" : "Observation.category",
        "min" : 1,
        "max" : "1"
      },
      {
        "id" : "Observation.category.coding",
        "path" : "Observation.category.coding",
        "min" : 1,
        "max" : "1"
      },
      {
        "id" : "Observation.category.coding.system",
        "path" : "Observation.category.coding.system",
        "patternUri" : "https://hl7.org/fhir/R4/codesystem-observation-category.html"
      },
      {
        "id" : "Observation.category.coding.version",
        "path" : "Observation.category.coding.version",
        "patternString" : "4.0.1"
      },
      {
        "id" : "Observation.category.coding.code",
        "path" : "Observation.category.coding.code",
        "mustSupport" : true
      },
      {
        "id" : "Observation.code.coding",
        "path" : "Observation.code.coding",
        "min" : 1,
        "max" : "1"
      },
      {
        "id" : "Observation.code.coding.system",
        "path" : "Observation.code.coding.system",
        "min" : 1,
        "patternUri" : "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl"
      },
      {
        "id" : "Observation.code.coding.code",
        "path" : "Observation.code.coding.code",
        "min" : 1,
        "patternCode" : "C60819"
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
        "id" : "Observation.value[x]",
        "path" : "Observation.value[x]",
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
        "id" : "Observation.value[x]:valueQuantity",
        "path" : "Observation.value[x]",
        "sliceName" : "valueQuantity",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "code" : "Quantity"
          }
        ]
      },
      {
        "id" : "Observation.value[x]:valueQuantity.value",
        "path" : "Observation.value[x].value",
        "mustSupport" : true
      },
      {
        "id" : "Observation.value[x]:valueQuantity.system",
        "path" : "Observation.value[x].system",
        "min" : 1,
        "patternUri" : "http://purl.obolibrary.org/obo/uo.owl"
      },
      {
        "id" : "Observation.value[x]:valueQuantity.code",
        "path" : "Observation.value[x].code",
        "mustSupport" : true
      },
      {
        "id" : "Observation.interpretation.coding.system",
        "path" : "Observation.interpretation.coding.system",
        "patternUri" : "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl"
      },
      {
        "id" : "Observation.interpretation.coding.code",
        "path" : "Observation.interpretation.coding.code",
        "mustSupport" : true
      },
      {
        "id" : "Observation.method.coding.system",
        "path" : "Observation.method.coding.system",
        "patternUri" : "http://snomed.info/sct"
      },
      {
        "id" : "Observation.method.coding.code",
        "path" : "Observation.method.coding.code",
        "mustSupport" : true
      }
    ]
  }
}

```
