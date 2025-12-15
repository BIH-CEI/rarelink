# RareLink Observation Phenotypic Feature - RareLink Implementation Guide v2.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **RareLink Observation Phenotypic Feature**

## Resource Profile: RareLink Observation Phenotypic Feature 

| | |
| :--- | :--- |
| *Official URL*:https://rarelink.bih-charite.de/fhir/StructureDefinition/rarelink-phenotypic-feature | *Version*:2.0.0 |
| Draft as of 2025-12-15 | *Computable Name*:RareLinkPhenotypicFeature |

 
A RareLink-specific profile for capturing phenotypic features. 

**Usages:**

* This Profile is not used by any profiles in this Implementation Guide

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/rarelink-ig|current/StructureDefinition/rarelink-phenotypic-feature)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-rarelink-phenotypic-feature.csv), [Excel](StructureDefinition-rarelink-phenotypic-feature.xlsx), [Schematron](StructureDefinition-rarelink-phenotypic-feature.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "rarelink-phenotypic-feature",
  "url" : "https://rarelink.bih-charite.de/fhir/StructureDefinition/rarelink-phenotypic-feature",
  "version" : "2.0.0",
  "name" : "RareLinkPhenotypicFeature",
  "title" : "RareLink Observation Phenotypic Feature",
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
  "description" : "A RareLink-specific profile for capturing phenotypic features.",
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
        "id" : "Observation.extension",
        "path" : "Observation.extension",
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
        "id" : "Observation.extension:phenotype_status",
        "path" : "Observation.extension",
        "sliceName" : "phenotype_status",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "code" : "Extension",
            "profile" : [
              "https://rarelink.bih-charite.de/fhir/StructureDefinition/phenotype-status"
            ]
          }
        ]
      },
      {
        "id" : "Observation.extension:resolution_date",
        "path" : "Observation.extension",
        "sliceName" : "resolution_date",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "code" : "Extension",
            "profile" : [
              "https://rarelink.bih-charite.de/fhir/StructureDefinition/resolution-date"
            ]
          }
        ]
      },
      {
        "id" : "Observation.extension:temporal_pattern",
        "path" : "Observation.extension",
        "sliceName" : "temporal_pattern",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "code" : "Extension",
            "profile" : [
              "https://rarelink.bih-charite.de/fhir/StructureDefinition/temporal-pattern"
            ]
          }
        ]
      },
      {
        "id" : "Observation.extension:phenotype_severity",
        "path" : "Observation.extension",
        "sliceName" : "phenotype_severity",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "code" : "Extension",
            "profile" : [
              "https://rarelink.bih-charite.de/fhir/StructureDefinition/phenotype-severity"
            ]
          }
        ]
      },
      {
        "id" : "Observation.extension:clinical_modifier_1",
        "path" : "Observation.extension",
        "sliceName" : "clinical_modifier_1",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "code" : "Extension",
            "profile" : [
              "https://rarelink.bih-charite.de/fhir/StructureDefinition/clinical-modifier-1"
            ]
          }
        ]
      },
      {
        "id" : "Observation.extension:clinical_modifier_2",
        "path" : "Observation.extension",
        "sliceName" : "clinical_modifier_2",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "code" : "Extension",
            "profile" : [
              "https://rarelink.bih-charite.de/fhir/StructureDefinition/clinical-modifier-2"
            ]
          }
        ]
      },
      {
        "id" : "Observation.extension:clinical_modifier_3",
        "path" : "Observation.extension",
        "sliceName" : "clinical_modifier_3",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "code" : "Extension",
            "profile" : [
              "https://rarelink.bih-charite.de/fhir/StructureDefinition/clinical-modifier-3"
            ]
          }
        ]
      },
      {
        "id" : "Observation.extension:causing_organism",
        "path" : "Observation.extension",
        "sliceName" : "causing_organism",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "code" : "Extension",
            "profile" : [
              "https://rarelink.bih-charite.de/fhir/StructureDefinition/causing-agent"
            ]
          }
        ]
      },
      {
        "id" : "Observation.status",
        "path" : "Observation.status",
        "patternCode" : "registered"
      },
      {
        "id" : "Observation.category.coding.system",
        "path" : "Observation.category.coding.system",
        "patternUri" : "http://purl.obolibrary.org/obo/hp.owl"
      },
      {
        "id" : "Observation.category.coding.code",
        "path" : "Observation.category.coding.code",
        "binding" : {
          "strength" : "required",
          "valueSet" : "https://rarelink.bih-charite.de/fhir/ValueSet/age-of-onset-vs"
        }
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
        "patternUri" : "http://purl.obolibrary.org/obo/hp.owl"
      },
      {
        "id" : "Observation.code.coding.code",
        "path" : "Observation.code.coding.code",
        "mustSupport" : true
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
      }
    ]
  }
}

```
