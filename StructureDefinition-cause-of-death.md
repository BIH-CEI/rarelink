# Cause of Death - RareLink Implementation Guide v2.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Cause of Death**

## Extension: Cause of Death 

| | |
| :--- | :--- |
| *Official URL*:https://rarelink.bih-charite.de/fhir/StructureDefinition/cause-of-death | *Version*:2.0.0 |
| Draft as of 2025-12-15 | *Computable Name*:CauseOfDeath |

The cause of death for the patient.

**Context of Use**

**Usage info**

**Usages:**

* Use this Extension: [RareLink IPS Patient](StructureDefinition-rarelink-ips-patient.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/rarelink-ig|current/StructureDefinition/cause-of-death)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-cause-of-death.csv), [Excel](StructureDefinition-cause-of-death.xlsx), [Schematron](StructureDefinition-cause-of-death.sch) 

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "cause-of-death",
  "url" : "https://rarelink.bih-charite.de/fhir/StructureDefinition/cause-of-death",
  "version" : "2.0.0",
  "name" : "CauseOfDeath",
  "title" : "Cause of Death",
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
  "description" : "The cause of death for the patient.",
  "fhirVersion" : "4.0.1",
  "mapping" : [
    {
      "identity" : "rim",
      "uri" : "http://hl7.org/v3",
      "name" : "RIM Mapping"
    }
  ],
  "kind" : "complex-type",
  "abstract" : false,
  "context" : [
    {
      "type" : "element",
      "expression" : "Element"
    }
  ],
  "type" : "Extension",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Extension",
  "derivation" : "constraint",
  "differential" : {
    "element" : [
      {
        "id" : "Extension",
        "path" : "Extension",
        "short" : "Cause of Death",
        "definition" : "The cause of death for the patient."
      },
      {
        "id" : "Extension.extension",
        "path" : "Extension.extension",
        "min" : 2
      },
      {
        "id" : "Extension.extension:causeOfDeath",
        "path" : "Extension.extension",
        "sliceName" : "causeOfDeath",
        "min" : 1,
        "max" : "1",
        "type" : [
          {
            "code" : "Extension",
            "profile" : [
              "https://rarelink.bih-charite.de/fhir/StructureDefinition/cause-of-death-code"
            ]
          }
        ]
      },
      {
        "id" : "Extension.extension:codeDefinition",
        "path" : "Extension.extension",
        "sliceName" : "codeDefinition",
        "min" : 1,
        "max" : "1",
        "type" : [
          {
            "code" : "Extension",
            "profile" : [
              "https://rarelink.bih-charite.de/fhir/StructureDefinition/cause-of-death-definition"
            ]
          }
        ]
      },
      {
        "id" : "Extension.url",
        "path" : "Extension.url",
        "fixedUri" : "https://rarelink.bih-charite.de/fhir/StructureDefinition/cause-of-death"
      },
      {
        "id" : "Extension.value[x]",
        "path" : "Extension.value[x]",
        "max" : "0"
      }
    ]
  }
}

```
