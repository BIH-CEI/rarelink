# RareLink Diagnostic Implication Observation - RareLink Implementation Guide v2.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **RareLink Diagnostic Implication Observation**

## Resource Profile: RareLink Diagnostic Implication Observation 

| | |
| :--- | :--- |
| *Official URL*:https://rarelink.bih-charite.de/fhir/StructureDefinition/rarelink-diagnostic-implication | *Version*:2.0.0 |
| Draft as of 2025-12-15 | *Computable Name*:RareLinkDiagnosticImplication |

 
A RareLink-specific profile extending the HL7 Genomics Reporting 'diagnostic-implication' profile for documenting diagnostic significance, evidence levels, and associated phenotypes (genetic_findings.diagnostic_implication). 

**Usages:**

* This Profile is not used by any profiles in this Implementation Guide

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/rarelink-ig|current/StructureDefinition/rarelink-diagnostic-implication)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-rarelink-diagnostic-implication.csv), [Excel](StructureDefinition-rarelink-diagnostic-implication.xlsx), [Schematron](StructureDefinition-rarelink-diagnostic-implication.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "rarelink-diagnostic-implication",
  "url" : "https://rarelink.bih-charite.de/fhir/StructureDefinition/rarelink-diagnostic-implication",
  "version" : "2.0.0",
  "name" : "RareLinkDiagnosticImplication",
  "title" : "RareLink Diagnostic Implication Observation",
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
  "description" : "A RareLink-specific profile extending the HL7 Genomics Reporting 'diagnostic-implication' profile \nfor documenting diagnostic significance, evidence levels, and associated phenotypes \n(genetic_findings.diagnostic_implication).\n",
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
  "baseDefinition" : "http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/diagnostic-implication|3.0.0",
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
        "fixedCode" : "final"
      },
      {
        "id" : "Observation.code.coding.system",
        "path" : "Observation.code.coding.system",
        "fixedUri" : "http://hl7.org/fhir/uv/genomics-reporting/CodeSystem/tbd-codes-cs"
      },
      {
        "id" : "Observation.code.coding.version",
        "path" : "Observation.code.coding.version",
        "patternString" : "3.0.0"
      },
      {
        "id" : "Observation.code.coding.code",
        "path" : "Observation.code.coding.code",
        "fixedCode" : "diagnostic-implication"
      },
      {
        "id" : "Observation.derivedFrom:rarelinkVariant",
        "path" : "Observation.derivedFrom",
        "sliceName" : "rarelinkVariant",
        "min" : 1,
        "max" : "1"
      },
      {
        "id" : "Observation.derivedFrom:rarelinkVariant.reference",
        "path" : "Observation.derivedFrom.reference",
        "min" : 1
      },
      {
        "id" : "Observation.component:evidenceLevel",
        "path" : "Observation.component",
        "sliceName" : "evidenceLevel",
        "min" : 0,
        "max" : "1"
      },
      {
        "id" : "Observation.component:evidenceLevel.extension:workflow-relatedArtifactComponent",
        "path" : "Observation.component.extension",
        "sliceName" : "workflow-relatedArtifactComponent"
      },
      {
        "id" : "Observation.component:evidenceLevel.code.coding.system",
        "path" : "Observation.component.code.coding.system",
        "fixedUri" : "http://loinc.org"
      },
      {
        "id" : "Observation.component:evidenceLevel.code.coding.code",
        "path" : "Observation.component.code.coding.code",
        "patternCode" : "93044-6"
      },
      {
        "id" : "Observation.component:evidenceLevel.value[x]",
        "path" : "Observation.component.value[x]",
        "type" : [
          {
            "code" : "CodeableConcept"
          }
        ],
        "binding" : {
          "strength" : "required",
          "valueSet" : "https://rarelink.bih-charite.de/fhir/ValueSet/level-of-evidence-vs"
        }
      },
      {
        "id" : "Observation.component:clinicalSignificance",
        "path" : "Observation.component",
        "sliceName" : "clinicalSignificance",
        "min" : 0,
        "max" : "1"
      },
      {
        "id" : "Observation.component:clinicalSignificance.extension:workflow-relatedArtifactComponent",
        "path" : "Observation.component.extension",
        "sliceName" : "workflow-relatedArtifactComponent"
      },
      {
        "id" : "Observation.component:clinicalSignificance.code.coding.system",
        "path" : "Observation.component.code.coding.system",
        "fixedUri" : "http://loinc.org"
      },
      {
        "id" : "Observation.component:clinicalSignificance.code.coding.code",
        "path" : "Observation.component.code.coding.code",
        "patternCode" : "53037-8"
      },
      {
        "id" : "Observation.component:clinicalSignificance.value[x]",
        "path" : "Observation.component.value[x]",
        "type" : [
          {
            "code" : "CodeableConcept"
          }
        ],
        "binding" : {
          "strength" : "required",
          "valueSet" : "https://rarelink.bih-charite.de/fhir/ValueSet/clinical-significance-vs"
        }
      },
      {
        "id" : "Observation.component:predictedPhenotype",
        "path" : "Observation.component",
        "sliceName" : "predictedPhenotype",
        "min" : 0,
        "max" : "1"
      },
      {
        "id" : "Observation.component:predictedPhenotype.extension:workflow-relatedArtifactComponent",
        "path" : "Observation.component.extension",
        "sliceName" : "workflow-relatedArtifactComponent"
      },
      {
        "id" : "Observation.component:predictedPhenotype.code.coding.system",
        "path" : "Observation.component.code.coding.system",
        "fixedUri" : "http://loinc.org"
      },
      {
        "id" : "Observation.component:predictedPhenotype.code.coding.code",
        "path" : "Observation.component.code.coding.code",
        "patternCode" : "81259-4"
      },
      {
        "id" : "Observation.component:predictedPhenotype.value[x]",
        "path" : "Observation.component.value[x]",
        "type" : [
          {
            "code" : "CodeableConcept"
          }
        ]
      },
      {
        "id" : "Observation.component:predictedPhenotype.value[x].coding",
        "path" : "Observation.component.value[x].coding",
        "slicing" : {
          "discriminator" : [
            {
              "type" : "value",
              "path" : "system"
            }
          ],
          "rules" : "closed"
        }
      },
      {
        "id" : "Observation.component:predictedPhenotype.value[x].coding:mondo",
        "path" : "Observation.component.value[x].coding",
        "sliceName" : "mondo",
        "min" : 0,
        "max" : "*"
      },
      {
        "id" : "Observation.component:predictedPhenotype.value[x].coding:mondo.system",
        "path" : "Observation.component.value[x].coding.system",
        "min" : 1,
        "fixedUri" : "http://purl.obolibrary.org/obo/mondo.owl"
      },
      {
        "id" : "Observation.component:predictedPhenotype.value[x].coding:omim",
        "path" : "Observation.component.value[x].coding",
        "sliceName" : "omim",
        "min" : 0,
        "max" : "*"
      },
      {
        "id" : "Observation.component:predictedPhenotype.value[x].coding:omim.system",
        "path" : "Observation.component.value[x].coding.system",
        "min" : 1,
        "fixedUri" : "http://omim.org"
      }
    ]
  }
}

```
