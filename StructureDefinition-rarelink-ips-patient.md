# RareLink IPS Patient - RareLink Implementation Guide v2.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **RareLink IPS Patient**

## Resource Profile: RareLink IPS Patient 

| | |
| :--- | :--- |
| *Official URL*:https://rarelink.bih-charite.de/fhir/StructureDefinition/rarelink-ips-patient | *Version*:2.0.0 |
| Draft as of 2025-12-15 | *Computable Name*:RareLinkIPSPatient |

 
A RareLink-specific profile for the IPS Patient resource. 

**Usages:**

* Refer to this Profile: [RareLink Condition for Undiagnosed RD Case](StructureDefinition-rarelink-condition-undiagnosed-rd-case.md), [RareLink Consent](StructureDefinition-rarelink-consent.md), [RareLink Encounter](StructureDefinition-rarelink-encounter.md), [RareLink Family History](StructureDefinition-rarelink-familyhistory.md)...Show 11 more,[RareLink Genetic Variant Observation](StructureDefinition-rarelink-genetic-variant.md),[RareLink IPS Condition](StructureDefinition-rarelink-ips-condition.md),[RareLink IPS Measurement Laboratory](StructureDefinition-rarelink-ips-measurement-laboratory.md),[RareLink IPS Measurement Radiology](StructureDefinition-rarelink-ips-measurement-radiology.md),[RareLink IPS Procedure](StructureDefinition-rarelink-ips-procedure.md),[RareLink Observation Karyotypic Sex](StructureDefinition-rarelink-karyotypic-sex.md),[RareLink Observation Age Category](StructureDefinition-rarelink-observation-age-category.md),[RareLink Observation Gestation at Birth](StructureDefinition-rarelink-observation-gestation-at-birth.md),[RareLink Observation Measurements (Others)](StructureDefinition-rarelink-observation-measurements-others.md),[RareLink Vital Signs Measurements](StructureDefinition-rarelink-observation-vital-signs.md)and[RareLink Observation Phenotypic Feature](StructureDefinition-rarelink-phenotypic-feature.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/rarelink-ig|current/StructureDefinition/rarelink-ips-patient)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-rarelink-ips-patient.csv), [Excel](StructureDefinition-rarelink-ips-patient.xlsx), [Schematron](StructureDefinition-rarelink-ips-patient.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "rarelink-ips-patient",
  "url" : "https://rarelink.bih-charite.de/fhir/StructureDefinition/rarelink-ips-patient",
  "version" : "2.0.0",
  "name" : "RareLinkIPSPatient",
  "title" : "RareLink IPS Patient",
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
  "description" : "A RareLink-specific profile for the IPS Patient resource.",
  "fhirVersion" : "4.0.1",
  "mapping" : [
    {
      "identity" : "rim",
      "uri" : "http://hl7.org/v3",
      "name" : "RIM Mapping"
    },
    {
      "identity" : "cda",
      "uri" : "http://hl7.org/v3/cda",
      "name" : "CDA (R2)"
    },
    {
      "identity" : "w5",
      "uri" : "http://hl7.org/fhir/fivews",
      "name" : "FiveWs Pattern Mapping"
    },
    {
      "identity" : "v2",
      "uri" : "http://hl7.org/v2",
      "name" : "HL7 v2 Mapping"
    },
    {
      "identity" : "loinc",
      "uri" : "http://loinc.org",
      "name" : "LOINC code for the element"
    }
  ],
  "kind" : "resource",
  "abstract" : false,
  "type" : "Patient",
  "baseDefinition" : "http://hl7.org/fhir/uv/ips/StructureDefinition/Patient-uv-ips",
  "derivation" : "constraint",
  "differential" : {
    "element" : [
      {
        "id" : "Patient",
        "path" : "Patient"
      },
      {
        "id" : "Patient.extension",
        "path" : "Patient.extension",
        "slicing" : {
          "discriminator" : [
            {
              "type" : "value",
              "path" : "url"
            }
          ],
          "ordered" : false,
          "rules" : "open"
        }
      },
      {
        "id" : "Patient.extension:birth_place",
        "path" : "Patient.extension",
        "sliceName" : "birth_place",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "code" : "Extension",
            "profile" : [
              "https://rarelink.bih-charite.de/fhir/StructureDefinition/birth-place"
            ]
          }
        ]
      },
      {
        "id" : "Patient.extension:date_of_admission",
        "path" : "Patient.extension",
        "sliceName" : "date_of_admission",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "code" : "Extension",
            "profile" : [
              "https://rarelink.bih-charite.de/fhir/StructureDefinition/date-of-admission"
            ]
          }
        ]
      },
      {
        "id" : "Patient.extension:recorded_sex_at_birth",
        "path" : "Patient.extension",
        "sliceName" : "recorded_sex_at_birth",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "code" : "Extension",
            "profile" : [
              "https://rarelink.bih-charite.de/fhir/StructureDefinition/recorded-sex-at-birth"
            ]
          }
        ]
      },
      {
        "id" : "Patient.extension:cause_of_death",
        "path" : "Patient.extension",
        "sliceName" : "cause_of_death",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "code" : "Extension",
            "profile" : [
              "https://rarelink.bih-charite.de/fhir/StructureDefinition/cause-of-death"
            ]
          }
        ]
      },
      {
        "id" : "Patient.extension:vital_status",
        "path" : "Patient.extension",
        "sliceName" : "vital_status",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "code" : "Extension",
            "profile" : [
              "https://rarelink.bih-charite.de/fhir/StructureDefinition/vital-status"
            ]
          }
        ],
        "mustSupport" : true
      },
      {
        "id" : "Patient.identifier.use",
        "path" : "Patient.identifier.use",
        "patternCode" : "official"
      },
      {
        "id" : "Patient.identifier.type.coding.system",
        "path" : "Patient.identifier.type.coding.system",
        "patternUri" : "http://snomed.info/sct"
      },
      {
        "id" : "Patient.identifier.type.coding.code",
        "path" : "Patient.identifier.type.coding.code",
        "patternCode" : "422549004"
      },
      {
        "id" : "Patient.identifier.value",
        "path" : "Patient.identifier.value",
        "mustSupport" : true
      },
      {
        "id" : "Patient.name.extension:dataAbsentReason",
        "path" : "Patient.name.extension",
        "sliceName" : "dataAbsentReason",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "code" : "Extension",
            "profile" : ["http://hl7.org/fhir/StructureDefinition/data-absent-reason"]
          }
        ]
      },
      {
        "id" : "Patient.name.extension:dataAbsentReason.value[x]",
        "path" : "Patient.name.extension.value[x]",
        "patternCode" : "unknown"
      },
      {
        "id" : "Patient.deceased[x]",
        "path" : "Patient.deceased[x]",
        "slicing" : {
          "discriminator" : [
            {
              "type" : "type",
              "path" : "$this"
            }
          ],
          "ordered" : false,
          "rules" : "open"
        },
        "mustSupport" : true
      },
      {
        "id" : "Patient.deceased[x]:deceasedBoolean",
        "path" : "Patient.deceased[x]",
        "sliceName" : "deceasedBoolean",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "code" : "boolean"
          }
        ],
        "mustSupport" : true
      },
      {
        "id" : "Patient.deceased[x]:deceasedDateTime",
        "path" : "Patient.deceased[x]",
        "sliceName" : "deceasedDateTime",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "code" : "dateTime"
          }
        ],
        "mustSupport" : true
      }
    ]
  }
}

```
