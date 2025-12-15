# Phenotype Causing Organism - RareLink Implementation Guide v2.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Phenotype Causing Organism**

## Extension: Phenotype Causing Organism 

| | |
| :--- | :--- |
| *Official URL*:https://rarelink.bih-charite.de/fhir/StructureDefinition/causing-agent | *Version*:2.0.0 |
| Draft as of 2025-12-15 | *Computable Name*:CausingOrganism |

The organism that is causing the phenotypic feature (e.g., a virus, bacteria, etc.).

**Context of Use**

**Usage info**

**Usages:**

* Use this Extension: [RareLink Observation Phenotypic Feature](StructureDefinition-rarelink-phenotypic-feature.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/rarelink-ig|current/StructureDefinition/causing-agent)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-causing-agent.csv), [Excel](StructureDefinition-causing-agent.xlsx), [Schematron](StructureDefinition-causing-agent.sch) 

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "causing-agent",
  "url" : "https://rarelink.bih-charite.de/fhir/StructureDefinition/causing-agent",
  "version" : "2.0.0",
  "name" : "CausingOrganism",
  "title" : "Phenotype Causing Organism",
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
  "description" : "The organism that is causing the phenotypic feature (e.g., a virus, bacteria, etc.).",
  "fhirVersion" : "4.0.1",
  "mapping" : [
    {
      "identity" : "rim",
      "uri" : "http://hl7.org/v3",
      "name" : "RIM Mapping"
    }
  ],
  "kind" : "complex-type",
  "abstract" : false,
  "context" : [
    {
      "type" : "element",
      "expression" : "Element"
    }
  ],
  "type" : "Extension",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Extension",
  "derivation" : "constraint",
  "differential" : {
    "element" : [
      {
        "id" : "Extension",
        "path" : "Extension",
        "short" : "Phenotype Causing Organism",
        "definition" : "The organism that is causing the phenotypic feature (e.g., a virus, bacteria, etc.)."
      },
      {
        "id" : "Extension.extension",
        "path" : "Extension.extension",
        "max" : "0"
      },
      {
        "id" : "Extension.url",
        "path" : "Extension.url",
        "fixedUri" : "https://rarelink.bih-charite.de/fhir/StructureDefinition/causing-agent"
      },
      {
        "id" : "Extension.value[x]",
        "path" : "Extension.value[x]",
        "type" : [
          {
            "code" : "CodeableConcept"
          }
        ]
      },
      {
        "id" : "Extension.value[x].coding",
        "path" : "Extension.value[x].coding",
        "min" : 1,
        "max" : "1"
      },
      {
        "id" : "Extension.value[x].coding.system",
        "path" : "Extension.value[x].coding.system",
        "patternUri" : "http://purl.obolibrary.org/obo/NCBITaxon.owl"
      },
      {
        "id" : "Extension.value[x].coding.code",
        "path" : "Extension.value[x].coding.code",
        "mustSupport" : true
      }
    ]
  }
}

```
