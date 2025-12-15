# Structural Variant Method Value Set - RareLink Implementation Guide v2.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Structural Variant Method Value Set**

## ValueSet: Structural Variant Method Value Set 

| | |
| :--- | :--- |
| *Official URL*:https://rarelink.bih-charite.de/fhir/ValueSet/structural-variant-method-vs | *Version*:2.0.0 |
| Draft as of 2025-12-15 | *Computable Name*:StructuralVariantMethodVS |

 
LOINC LA codes enumerating methods for detecting structural variants. 

 **References** 

* [RareLink Genetic Variant Observation](StructureDefinition-rarelink-genetic-variant.md)

### Logical Definition (CLD)

 

### Expansion

-------

 Explanation of the columns that may appear on this page: 

| | |
| :--- | :--- |
| Level | A few code lists that FHIR defines are hierarchical - each code is assigned a level. In this scheme, some codes are under other codes, and imply that the code they are under also applies |
| System | The source of the definition of the code (when the value set draws in codes defined elsewhere) |
| Code | The code (used as the code in the resource instance) |
| Display | The display (used in the*display*element of a[Coding](http://hl7.org/fhir/R4/datatypes.html#Coding)). If there is no display, implementers should not simply display the code, but map the concept into their application |
| Definition | An explanation of the meaning of the concept |
| Comments | Additional notes about how to use the code |



## Resource Content

```json
{
  "resourceType" : "ValueSet",
  "id" : "structural-variant-method-vs",
  "url" : "https://rarelink.bih-charite.de/fhir/ValueSet/structural-variant-method-vs",
  "version" : "2.0.0",
  "name" : "StructuralVariantMethodVS",
  "title" : "Structural Variant Method Value Set",
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
  "description" : "LOINC LA codes enumerating methods for detecting structural variants.",
  "compose" : {
    "include" : [
      {
        "system" : "http://loinc.org",
        "concept" : [
          {
            "code" : "LA26406-1",
            "display" : "Karyotyping"
          },
          {
            "code" : "LA26404-6",
            "display" : "FISH"
          },
          {
            "code" : "LA26418-6",
            "display" : "PCR"
          },
          {
            "code" : "LA26419-4",
            "display" : "qPCR (real-time PCR)"
          },
          {
            "code" : "LA26400-4",
            "display" : "SNP array"
          },
          {
            "code" : "LA26813-8",
            "display" : "Restriction fragment length polymorphism (RFLP)"
          },
          {
            "code" : "LA26810-4",
            "display" : "DNA hybridization"
          },
          {
            "code" : "LA26398-0",
            "display" : "Sequencing"
          },
          {
            "code" : "LA26415-2",
            "display" : "MLPA"
          },
          {
            "code" : "LA46-8",
            "display" : "Other"
          }
        ]
      }
    ]
  }
}

```
