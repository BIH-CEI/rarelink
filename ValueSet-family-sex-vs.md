# Family Member Sex Value Set - RareLink Implementation Guide v2.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Family Member Sex Value Set**

## ValueSet: Family Member Sex Value Set 

| | |
| :--- | :--- |
| *Official URL*:https://rarelink.bih-charite.de/fhir/ValueSet/family-sex-vs | *Version*:2.0.0 |
| Draft as of 2025-12-15 | *Computable Name*:FamilySexVS |

 
Value set for capturing the sex of a family member. 

 **References** 

* [RareLink Family History](StructureDefinition-rarelink-familyhistory.md)

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
  "id" : "family-sex-vs",
  "url" : "https://rarelink.bih-charite.de/fhir/ValueSet/family-sex-vs",
  "version" : "2.0.0",
  "name" : "FamilySexVS",
  "title" : "Family Member Sex Value Set",
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
  "description" : "Value set for capturing the sex of a family member.",
  "compose" : {
    "include" : [
      {
        "system" : "http://snomed.info/sct",
        "concept" : [
          {
            "code" : "248152002",
            "display" : "Female"
          },
          {
            "code" : "248153007",
            "display" : "Male"
          },
          {
            "code" : "184115007",
            "display" : "Patient sex unknown"
          },
          {
            "code" : "32570691000036108",
            "display" : "Intersex"
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
