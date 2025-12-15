# Family Relationship Value Set - RareLink Implementation Guide v2.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Family Relationship Value Set**

## ValueSet: Family Relationship Value Set 

| | |
| :--- | :--- |
| *Official URL*:https://rarelink.bih-charite.de/fhir/ValueSet/family-relationship-vs | *Version*:2.0.0 |
| Draft as of 2025-12-15 | *Computable Name*:FamilyRelationshipVS |

 
Value set for capturing family member relationships. 

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
  "id" : "family-relationship-vs",
  "url" : "https://rarelink.bih-charite.de/fhir/ValueSet/family-relationship-vs",
  "version" : "2.0.0",
  "name" : "FamilyRelationshipVS",
  "title" : "Family Relationship Value Set",
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
  "description" : "Value set for capturing family member relationships.",
  "compose" : {
    "include" : [
      {
        "system" : "http://snomed.info/sct",
        "concept" : [
          {
            "code" : "65656005",
            "display" : "Natural mother"
          },
          {
            "code" : "9947008",
            "display" : "Natural father"
          },
          {
            "code" : "83420006",
            "display" : "Natural daughter"
          },
          {
            "code" : "113160008",
            "display" : "Natural son"
          },
          {
            "code" : "60614009",
            "display" : "Natural brother"
          },
          {
            "code" : "73678001",
            "display" : "Natural sister"
          },
          {
            "code" : "11286003",
            "display" : "Twin sibling"
          },
          {
            "code" : "45929001",
            "display" : "Half-brother"
          },
          {
            "code" : "2272004",
            "display" : "Half-sister"
          },
          {
            "code" : "62296006",
            "display" : "Natural grandfather"
          },
          {
            "code" : "17945006",
            "display" : "Natural grandmother"
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
