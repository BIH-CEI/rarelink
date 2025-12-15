# Reference Genome Value Set - RareLink Implementation Guide v2.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Reference Genome Value Set**

## ValueSet: Reference Genome Value Set 

| | |
| :--- | :--- |
| *Official URL*:https://rarelink.bih-charite.de/fhir/ValueSet/reference-genome-vs | *Version*:2.0.0 |
| Draft as of 2025-12-15 | *Computable Name*:ReferenceGenomeVS |

 
LOINC LA codes specifying the reference genome build. 

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
  "id" : "reference-genome-vs",
  "url" : "https://rarelink.bih-charite.de/fhir/ValueSet/reference-genome-vs",
  "version" : "2.0.0",
  "name" : "ReferenceGenomeVS",
  "title" : "Reference Genome Value Set",
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
  "description" : "LOINC LA codes specifying the reference genome build.",
  "compose" : {
    "include" : [
      {
        "system" : "http://loinc.org",
        "concept" : [
          {
            "code" : "LA14032-9",
            "display" : "NCBI Build 34 (hg16)"
          },
          {
            "code" : "LA14029-5",
            "display" : "GRCh37 (hg19)"
          },
          {
            "code" : "LA14030-3",
            "display" : "NCBI Build 36.1 (hg18)"
          },
          {
            "code" : "LA14031-1",
            "display" : "NCBI Build 35 (hg17)"
          },
          {
            "code" : "LA26806-2",
            "display" : "GRCh38 (hg38)"
          }
        ]
      }
    ]
  }
}

```
