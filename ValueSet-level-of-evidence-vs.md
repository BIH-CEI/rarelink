# Level of Evidence Value Set - RareLink Implementation Guide v2.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Level of Evidence Value Set**

## ValueSet: Level of Evidence Value Set 

| | |
| :--- | :--- |
| *Official URL*:https://rarelink.bih-charite.de/fhir/ValueSet/level-of-evidence-vs | *Version*:2.0.0 |
| Draft as of 2025-12-15 | *Computable Name*:LevelOfEvidenceVS |

 
LOINC LA codes describing evidence strength for a variant. 

 **References** 

* [RareLink Diagnostic Implication Observation](StructureDefinition-rarelink-diagnostic-implication.md)

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
  "id" : "level-of-evidence-vs",
  "url" : "https://rarelink.bih-charite.de/fhir/ValueSet/level-of-evidence-vs",
  "version" : "2.0.0",
  "name" : "LevelOfEvidenceVS",
  "title" : "Level of Evidence Value Set",
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
  "description" : "LOINC LA codes describing evidence strength for a variant.",
  "compose" : {
    "include" : [
      {
        "system" : "http://loinc.org",
        "concept" : [
          {
            "code" : "LA30200-2",
            "display" : "Very strong evidence pathogenic"
          },
          {
            "code" : "LA30201-0",
            "display" : "Strong evidence pathogenic"
          },
          {
            "code" : "LA30202-8",
            "display" : "Moderate evidence pathogenic"
          },
          {
            "code" : "LA30203-6",
            "display" : "Supporting evidence pathogenic"
          },
          {
            "code" : "LA30204-4",
            "display" : "Supporting evidence benign"
          },
          {
            "code" : "LA30205-1",
            "display" : "Strong evidence benign"
          },
          {
            "code" : "LA30206-9",
            "display" : "Stand-alone evidence pathogenic"
          }
        ]
      }
    ]
  }
}

```
