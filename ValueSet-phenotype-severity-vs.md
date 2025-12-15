# Phenotype Severity Value Set - RareLink Implementation Guide v2.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Phenotype Severity Value Set**

## ValueSet: Phenotype Severity Value Set 

| | |
| :--- | :--- |
| *Official URL*:https://rarelink.bih-charite.de/fhir/ValueSet/phenotype-severity-vs | *Version*:2.0.0 |
| Draft as of 2025-12-15 | *Computable Name*:PhenotypeSeverityVS |

 
Value set for capturing phenotype severity. 

 **References** 

* [Phenotype Severity](StructureDefinition-phenotype-severity.md)

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
  "id" : "phenotype-severity-vs",
  "url" : "https://rarelink.bih-charite.de/fhir/ValueSet/phenotype-severity-vs",
  "version" : "2.0.0",
  "name" : "PhenotypeSeverityVS",
  "title" : "Phenotype Severity Value Set",
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
  "description" : "Value set for capturing phenotype severity.",
  "compose" : {
    "include" : [
      {
        "system" : "http://purl.obolibrary.org/obo/hp.owl",
        "concept" : [
          {
            "code" : "HP:0012827",
            "display" : "Borderline"
          },
          {
            "code" : "HP:0012825",
            "display" : "Mild"
          },
          {
            "code" : "HP:0012826",
            "display" : "Moderate"
          },
          {
            "code" : "HP:0012829",
            "display" : "Profound"
          },
          {
            "code" : "HP:0012828",
            "display" : "Severe"
          }
        ]
      }
    ]
  }
}

```
