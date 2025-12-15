# Undiagnosed Rare Disease Case Value Set - RareLink Implementation Guide v2.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Undiagnosed Rare Disease Case Value Set**

## ValueSet: Undiagnosed Rare Disease Case Value Set 

| | |
| :--- | :--- |
| *Official URL*:https://rarelink.bih-charite.de/fhir/ValueSet/undiagnosed-rd-case-vs | *Version*:2.0.0 |
| Draft as of 2025-12-15 | *Computable Name*:UndiagnosedRDCaseVS |

 
Value set for capturing undiagnosed rare disease cases. 

 **References** 

* [RareLink Condition for Undiagnosed RD Case](StructureDefinition-rarelink-condition-undiagnosed-rd-case.md)

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
  "id" : "undiagnosed-rd-case-vs",
  "url" : "https://rarelink.bih-charite.de/fhir/ValueSet/undiagnosed-rd-case-vs",
  "version" : "2.0.0",
  "name" : "UndiagnosedRDCaseVS",
  "title" : "Undiagnosed Rare Disease Case Value Set",
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
  "description" : "Value set for capturing undiagnosed rare disease cases.",
  "compose" : {
    "include" : [
      {
        "system" : "http://www.orpha.net/ORDO",
        "concept" : [
          {
            "code" : "616874",
            "display" : "Rare disorder without a determined diagnosis after full investigation"
          }
        ]
      },
      {
        "system" : "http://snomed.info/sct",
        "concept" : [
          {
            "code" : "373067005",
            "display" : "A Rare Disease was diagnosed"
          }
        ]
      }
    ]
  }
}

```
