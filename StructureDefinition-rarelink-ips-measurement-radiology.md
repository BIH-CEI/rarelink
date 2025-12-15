# RareLink IPS Measurement Radiology - RareLink Implementation Guide v2.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **RareLink IPS Measurement Radiology**

## Resource Profile: RareLink IPS Measurement Radiology 

| | |
| :--- | :--- |
| *Official URL*:https://rarelink.bih-charite.de/fhir/StructureDefinition/rarelink-ips-measurement-radiology | *Version*:2.0.0 |
| Draft as of 2025-12-15 | *Computable Name*:RareLinkIPSMeasurementRadiology |

 
A RareLink-specific profile for radiology measurements based on the IPS Observation profile. 

**Usages:**

* This Profile is not used by any profiles in this Implementation Guide

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/rarelink-ig|current/StructureDefinition/rarelink-ips-measurement-radiology)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-rarelink-ips-measurement-radiology.csv), [Excel](StructureDefinition-rarelink-ips-measurement-radiology.xlsx), [Schematron](StructureDefinition-rarelink-ips-measurement-radiology.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "rarelink-ips-measurement-radiology",
  "url" : "https://rarelink.bih-charite.de/fhir/StructureDefinition/rarelink-ips-measurement-radiology",
  "version" : "2.0.0",
  "name" : "RareLinkIPSMeasurementRadiology",
  "title" : "RareLink IPS Measurement Radiology",
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
  "description" : "A RareLink-specific profile for radiology measurements based on the IPS Observation profile.",
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
  "baseDefinition" : "http://hl7.org/fhir/uv/ips/StructureDefinition/Observation-results-radiology-uv-ips",
  "derivation" : "constraint",
  "differential" : {
    "element" : [
      {
        "id" : "Observation",
        "path" : "Observation"
      },
      {
        "id" : "Observation.category",
        "path" : "Observation.category",
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
        "patternUri" : "http://terminology.hl7.org/CodeSystem/observation-category"
      },
      {
        "id" : "Observation.category.coding.code",
        "path" : "Observation.category.coding.code",
        "patternCode" : "imaging"
      },
      {
        "id" : "Observation.subject",
        "path" : "Observation.subject",
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
        "id" : "Observation.subject.identifier",
        "path" : "Observation.subject.identifier",
        "mustSupport" : true
      },
      {
        "id" : "Observation.performer.extension:dataAbsentReason",
        "path" : "Observation.performer.extension",
        "sliceName" : "dataAbsentReason",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "code" : "Extension",
            "profile" : ["http://hl7.org/fhir/StructureDefinition/data-absent-reason"]
          }
        ]
      },
      {
        "id" : "Observation.performer.extension:dataAbsentReason.value[x]",
        "path" : "Observation.performer.extension.value[x]",
        "patternCode" : "unknown"
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
        "patternUri" : "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl"
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
