# Propositus Value Set - RareLink Implementation Guide v2.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Propositus Value Set**

## ValueSet: Propositus Value Set 

| | |
| :--- | :--- |
| *Official URL*:https://rarelink.bih-charite.de/fhir/ValueSet/propositus-vs | *Version*:2.0.0 |
| Draft as of 2025-12-15 | *Computable Name*:PropositusVS |

 
Value set for indicating whether the family member is the propositus. 

 **References** 

* [Propositus](StructureDefinition-propositus.md)

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
  "id" : "propositus-vs",
  "url" : "https://rarelink.bih-charite.de/fhir/ValueSet/propositus-vs",
  "version" : "2.0.0",
  "name" : "PropositusVS",
  "title" : "Propositus Value Set",
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
  "description" : "Value set for indicating whether the family member is the propositus.",
  "compose" : {
    "include" : [
      {
        "system" : "http://snomed.info/sct",
        "concept" : [
          {
            "code" : "373066001",
            "display" : "Yes"
          },
          {
            "code" : "373067005",
            "display" : "No"
          },
          {
            "code" : "261665006",
            "display" : "Unknown"
          },
          {
            "code" : "1220561009",
            "display" : "Not recorded"
          }
        ]
      }
    ]
  }
}

```
