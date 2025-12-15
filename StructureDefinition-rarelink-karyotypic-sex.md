# RareLink Observation Karyotypic Sex - RareLink Implementation Guide v2.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **RareLink Observation Karyotypic Sex**

## Resource Profile: RareLink Observation Karyotypic Sex 

| | |
| :--- | :--- |
| *Official URL*:https://rarelink.bih-charite.de/fhir/StructureDefinition/rarelink-karyotypic-sex | *Version*:2.0.0 |
| Draft as of 2025-12-15 | *Computable Name*:RareLinkKaryotypicSex |

 
A RareLink-specific profile for capturing karyotypic sex information. 

**Usages:**

* This Profile is not used by any profiles in this Implementation Guide

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/rarelink-ig|current/StructureDefinition/rarelink-karyotypic-sex)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-rarelink-karyotypic-sex.csv), [Excel](StructureDefinition-rarelink-karyotypic-sex.xlsx), [Schematron](StructureDefinition-rarelink-karyotypic-sex.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "rarelink-karyotypic-sex",
  "url" : "https://rarelink.bih-charite.de/fhir/StructureDefinition/rarelink-karyotypic-sex",
  "version" : "2.0.0",
  "name" : "RareLinkKaryotypicSex",
  "title" : "RareLink Observation Karyotypic Sex",
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
  "description" : "A RareLink-specific profile for capturing karyotypic sex information.",
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
              "code" : "1296886006"
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
        "id" : "Observation.value[x]",
        "path" : "Observation.value[x]",
        "min" : 1,
        "type" : [
          {
            "code" : "CodeableConcept"
          }
        ]
      },
      {
        "id" : "Observation.value[x].coding",
        "path" : "Observation.value[x].coding",
        "min" : 1,
        "max" : "1"
      },
      {
        "id" : "Observation.value[x].coding.system",
        "path" : "Observation.value[x].coding.system",
        "patternUri" : "http://snomed.info/sct"
      },
      {
        "id" : "Observation.value[x].coding.code",
        "path" : "Observation.value[x].coding.code",
        "binding" : {
          "strength" : "required",
          "valueSet" : "https://rarelink.bih-charite.de/fhir/ValueSet/karyotypic-sex-vs"
        }
      }
    ]
  }
}

```
