# Age Category Value Set - RareLink Implementation Guide v2.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Age Category Value Set**

## ValueSet: Age Category Value Set 

| | |
| :--- | :--- |
| *Official URL*:https://rarelink.bih-charite.de/fhir/ValueSet/age-category-vs | *Version*:2.0.0 |
| Draft as of 2025-12-15 | *Computable Name*:AgeCategoryVS |

 
Value set for capturing the age category of a patient. 

 **References** 

* [RareLink Observation Age Category](StructureDefinition-rarelink-observation-age-category.md)

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
  "id" : "age-category-vs",
  "url" : "https://rarelink.bih-charite.de/fhir/ValueSet/age-category-vs",
  "version" : "2.0.0",
  "name" : "AgeCategoryVS",
  "title" : "Age Category Value Set",
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
  "description" : "Value set for capturing the age category of a patient.",
  "compose" : {
    "include" : [
      {
        "system" : "http://snomed.info/sct",
        "concept" : [
          {
            "code" : "3658006",
            "display" : "Infancy"
          },
          {
            "code" : "713153009",
            "display" : "Toddler"
          },
          {
            "code" : "255398004",
            "display" : "Childhood"
          },
          {
            "code" : "263659003",
            "display" : "Adolescence"
          },
          {
            "code" : "41847000",
            "display" : "Adulthood"
          },
          {
            "code" : "303112003",
            "display" : "Fetal period"
          },
          {
            "code" : "419099009",
            "display" : "Dead"
          },
          {
            "code" : "261665006",
            "display" : "Unknown"
          }
        ]
      }
    ]
  }
}

```
