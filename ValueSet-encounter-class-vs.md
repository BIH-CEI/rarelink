# Encounter Class Value Set - RareLink Implementation Guide v2.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Encounter Class Value Set**

## ValueSet: Encounter Class Value Set 

| | |
| :--- | :--- |
| *Official URL*:https://rarelink.bih-charite.de/fhir/ValueSet/encounter-class-vs | *Version*:2.0.0 |
| Draft as of 2025-12-15 | *Computable Name*:EncounterClassVS |

 
Value set for encounter classes, including custom RareLink-specific codes. 

 **References** 

* [RareLink Encounter](StructureDefinition-rarelink-encounter.md)

### Logical Definition (CLD)

 

### Expansion

No Expansion for this valueset (not supported by Publication Tooling)

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
  "id" : "encounter-class-vs",
  "url" : "https://rarelink.bih-charite.de/fhir/ValueSet/encounter-class-vs",
  "version" : "2.0.0",
  "name" : "EncounterClassVS",
  "title" : "Encounter Class Value Set",
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
  "description" : "Value set for encounter classes, including custom RareLink-specific codes.",
  "compose" : {
    "include" : [
      {
        "system" : "http://hl7.org/fhir/R4",
        "concept" : [
          {
            "code" : "AMB",
            "display" : "Ambulatory"
          },
          {
            "code" : "IMP",
            "display" : "Inpatient"
          },
          {
            "code" : "OBSENC",
            "display" : "Observation"
          },
          {
            "code" : "EMER",
            "display" : "Emergency"
          },
          {
            "code" : "VR",
            "display" : "Virtual"
          },
          {
            "code" : "HH",
            "display" : "Home Health"
          }
        ]
      },
      {
        "system" : "http://github.com/BIH-CEI/RareLink",
        "concept" : [
          {
            "code" : "RDC",
            "display" : "RD Specialist Center"
          }
        ]
      },
      {
        "system" : "http://snomed.info/sct",
        "concept" : [
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
