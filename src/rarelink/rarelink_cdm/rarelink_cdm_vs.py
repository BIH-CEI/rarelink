from phenopacket_mapper.data_standards import Coding, CodeSystem, Date, ValueSet
from . import RARELINK_CDM_V2_0_0_RESOURCES as res

class RareLink_CDM_v2_0_0_ValueSets:
    """
    This class is a container for the value sets used in the RareLink CDM.
    ___version__ = '2.0.0'
    """
# 1. Formal Criteria
    vs_1_1 = ValueSet(
        elements=[str],
        name="Value set for 1.1 Pseudonym",
        description="The (local) patient-related Identification code."
       )

    vs_1_2 = ValueSet(
        elements=[Date],
        name="Value set for 1.2 Date of Admission",
        description="The date of admission or data capture of the individual."
       )
# 2. Personal Information
    # 2.1 Date of Birth
    vs_2_1 = ValueSet(
        elements=[Date],
        name="Value set for 2.1 Date of Birth",
        description=("The individual's date of birth. If the exact month or day "
                     "is allowed to be captured or not known, select the 1st day "
                     "of the month or the 1st month of the year, respectively.")
    )

    # 2.2 Sex at Birth
    vs_2_2 = ValueSet(
        elements=[
            Coding(system=res.SNOMED_CT, code="248152002", 
                   display="Female"),
            Coding(system=res.SNOMED_CT, code="248153007", display="Male"),
            Coding(system=res.SNOMED_CT, code="184115007", 
                   display="Patient sex unknown"),
            Coding(system=res.SNOMED_CT, code="32570691000036108", 
                   display="Intersex"),
            Coding(system=res.SNOMED_CT, code="1220561009", 
                   display="Not recorded")
        ],
        name="Value set for 2.2 Sex at Birth",
        description=("The individual's sex that was assigned at birth.")
    )

    # 2.3 Karyotypic Sex
    vs_2_3 = ValueSet(
        elements=[
            Coding(system=res.SNOMED_CT, code="261665006", 
                   display="Unknown"),
            Coding(system=res.SNOMED_CT, code="734875008", display="XX"),
            Coding(system=res.SNOMED_CT, code="734876009", display="XY"),
            Coding(system=res.SNOMED_CT, code="80427008", display="X0"),
            Coding(system=res.SNOMED_CT, code="65162001", display="XXY"),
            Coding(system=res.SNOMED_CT, code="35111009", display="XXX"),
            Coding(system=res.SNOMED_CT, code="403760006", display="XXYY"),
            Coding(system=res.SNOMED_CT, code="78317008", display="XXXY"),
            Coding(system=res.SNOMED_CT, code="10567003", display="XXXX"),
            Coding(system=res.SNOMED_CT, code="48930007", display="XYY"),
            Coding(system=res.SNOMED_CT, code="74964007", display="Other")
        ],
        name="Value set for 2.3 Karyotypic Sex",
        description=("The chromosomal sex of an individual.")
    )

    # 2.4 Gender Identity
    vs_2_4 = ValueSet(
        elements=[
            Coding(system=res.SNOMED_CT, code="446141000124107", 
                   display="Female gender identity"),
            Coding(system=res.SNOMED_CT, code="446151000124109", 
                   display="Male gender identity"),
            Coding(system=res.SNOMED_CT, code="394743007", 
                   display="Gender unknown"),
            Coding(system=res.SNOMED_CT, code="33791000087105", 
                   display="Identifies as nonbinary gender"),
            Coding(system=res.SNOMED_CT, code="1220561009", 
                   display="Not recorded")
        ],
        name="Value set for 2.4 Gender Identity",
        description=("The self-assigned gender of the individual.")
    )

    # 2.5 Country of Birth
    vs_2_5 = ValueSet(
        elements=[res.ISO3166],
        name="Value set for 2.5 Country of Birth",
        description="The country in which the individual was born."
    )


# 3. Personal Information
    # 3.1 Vital Status
    vs_3_1 = ValueSet(
        elements=[
            Coding(system=res.SNOMED_CT, code="438949009", display="Alive"),
            Coding(system=res.SNOMED_CT, code="419099009", display="Dead"),
            Coding(system=res.SNOMED_CT, code="399307001", 
                   display="Unknown - Lost in follow-up"),
            Coding(system=res.SNOMED_CT, code="185924006", 
                   display="Unknown - Opted-out"),
            Coding(system=res.SNOMED_CT, code="261665006", 
                   display="Unknown - Other Reason")
        ],
        name="Value set for 3.1 Vital Status",
        description=("The individual’s general clinical status or vital status.")
    )

    # 3.2 Time of Death
    vs_3_2 = ValueSet(
        elements=[Date], 
        name="Value set for 3.2 Time of Death",
        description=("If deceased, the individual’s date of death. If the specific "
                     "month or day is not known, select the 1st day of the "
                     "month or the 1st month of the year, respectively.")
    )

    # 3.3 Cause of Death [ICD10CM]
    vs_3_3 = ValueSet(
        elements=[res.ICD10CM],
        name="Value set for 3.3 Cause of Death [ICD10CM]",
        description=("If deceased, the individual’s primary cause of death "
                     "(i.e. according to the death certificate).")
    )

    # 3.4 Age Category
    vs_3_4 = ValueSet(
        elements=[
            Coding(system=res.SNOMED_CT, code="3658006", display="Infancy"),
            Coding(system=res.SNOMED_CT, code="713153009", 
                   display="Toddler"),
            Coding(system=res.SNOMED_CT, code="255398004", 
                   display="Childhood"),
            Coding(system=res.SNOMED_CT, code="263659003", 
                   display="Adolescence"),
            Coding(system=res.SNOMED_CT, code="41847000", 
                   display="Adulthood"),
            Coding(system=res.SNOMED_CT, code="303112003", 
                   display="Fetal period"),
            Coding(system=res.SNOMED_CT, code="419099009", display="Dead"),
            Coding(system=res.SNOMED_CT, code="261665006", 
                   display="Unknown")
        ],
        name="Value set for 3.4 Age Category",
        description=("The individual's age category at the time of data capture (1.2).")
    )

    # 3.5 Length of Gestation at Birth [weeks+days]
    vs_3_5 = ValueSet(
        elements=[str],
        name="Value set for 3.5 Length of Gestation at Birth [weeks+days]",
        description=("The length of gestation at birth in weeks and days.")
    )

    # 3.6 Undiagnosed RD Case
    vs_3_6 = ValueSet(
        elements=[
            Coding(system=res.SNOMED_CT, code="373066001", display="Yes"),
            Coding(system=res.SNOMED_CT, code="373067005", display="No")
        ],
        name="Value set for 3.6 Undiagnosed RD Case",
        description=("Identifies cases where an RD diagnosis has not been established.")
    )

# 4. Care Pathway
    # 4.1 Encounter Start
    vs_4_1 = ValueSet(
        elements=[Date],
        name="Value set for 4.1 Encounter Start",
        description=("The date of the start of the encounter.")
    )

    # 4.2 Encounter End
    vs_4_2 = ValueSet(
        elements=[Date],
        name="Value set for 4.2 Encounter End",
        description=("The date of the end of the encounter.")
    )

    # 4.3 Encounter Status
    vs_4_3 = ValueSet(
        elements=[
            Coding(system=res.HL7FHIR, code="planned", 
                   display="Planned"),
            Coding(system=res.HL7FHIR, code="arrived", 
                   display="Arrived"),
            Coding(system=res.HL7FHIR, code="triaged", 
                   display="Triaged"),
            Coding(system=res.HL7FHIR, code="in-progress", 
                   display="In Progress"),
            Coding(system=res.HL7FHIR, code="onleave", 
                   display="On Leave"),
            Coding(system=res.HL7FHIR, code="finished", 
                   display="Finished"),
            Coding(system=res.HL7FHIR, code="cancelled", 
                   display="Cancelled"),
            Coding(system=res.HL7FHIR, code="entered-in-error", 
                   display="Entered in Error"),
            Coding(system=res.HL7FHIR, code="unknown", 
                   display="Unknown")
        ],
        name="Value set for 4.3 Encounter Status",
        description=("The status of an encounter of the individual at the time of "
                     "data capture.")
    )

    # 4.4 Encounter Class
    vs_4_4 = ValueSet(
        elements=[
            Coding(system=res.HL7FHIR, code="amb", display="Ambulatory"),
            Coding(system=res.HL7FHIR, code="imp", display="Inpatient"),
            Coding(system=res.HL7FHIR, code="obsenc", 
                   display="Observation"),
            Coding(system=res.HL7FHIR, code="emer", display="Emergency"),
            Coding(system=res.HL7FHIR, code="vr", display="Virtual"),
            Coding(system=res.HL7FHIR, code="hh", display="Home Health"),
            Coding(system=res.HL7FHIR, code="rdc", 
                   display="RD Specialist Center"),
            Coding(system=res.SNOMED_CT, code="261665006", display="Unknown")
        ],
        name="Value set for 4.4 Encounter Class",
        description=("The class of an encounter of the individual at the time of "
                     "data capture.")
    )


# 5. Disease
    # 5.1 Disease
    vs_5_1a = ValueSet(
       elements=[res.MONDO],
       name="Value set for 5.1a Disease [MONDO]",
       description=("A disease that the individual was affected by as classified by MONDO.")
       )
    vs_5_1b = ValueSet(
       elements=[res.ORDO],
       name="Value set for 5.1b Disease [ORDO]",
       description=("A disease that the individual was affected by as classified by ORDO.")
       )
    vs_5_1c = ValueSet(
       elements=[res.ICD10CM],
       name="Value set for 5.1c Disease [ICD-10-CM]",
       description=("A disease that the individual was affected by as classified by ICD-10-CM.")
       )
    vs_5_1d = ValueSet(
       elements=[res.ICD11],
       name="Value set for 5.1d Disease [ICD-11]",
       description=("A disease that the individual was affected by as classified by ICD-11.")
       )
    vs_5_1e = ValueSet(
       elements=[res.OMIM],
       name="Value set for 5.1e Disease [OMIM]",
       description=("A disease that the individual was affected by as classified by OMIM.")
       )

    # 5.2 Verification Status
    vs_5_2 = ValueSet(
        elements=[
            Coding(system=res.HL7FHIR, code="unconfirmed", 
                   display="Unconfirmed"),
            Coding(system=res.HL7FHIR, code="provisional", 
                   display="Provisional"),
            Coding(system=res.HL7FHIR, code="differential", 
                   display="Differential"),
            Coding(system=res.HL7FHIR, code="confirmed", 
                   display="Confirmed"),
            Coding(system=res.HL7FHIR, code="refuted", display="Refuted"),
            Coding(system=res.HL7FHIR, code="entered-in-error", 
                   display="Entered in Error")
        ],
        name="Value set for 5.2 Verification Status",
        description=("The verification status of the disease.")
    )

    # 5.3 Age at Onset
    vs_5_3 = ValueSet(
        elements=[
            Coding(system=res.SNOMED_CT, code="118189007", 
                   display="Prenatal"),
            Coding(system=res.SNOMED_CT, code="3950001", display="Birth"),
            Coding(system=res.SNOMED_CT, code="410672004", display="Date"),
            Coding(system=res.SNOMED_CT, code="261665006", display="Unknown")
        ],
        name="Value set for 5.3 Age at Onset",
        description=("The age at the onset of the first symptoms or signs "
                     "of the disease.")
    )

    # 5.4 Date of Onset
    vs_5_4 = ValueSet(
        elements=[Date],
        name="Value set for 5.4 Date of Onset",
        description=("The date at onset of first symptoms or signs of the "
                     "disease. If the specific month or day is not known, "
                     "select the 1st day of the month or the 1st month "
                     "of the year, respectively.")
    )

    # 5.5 Age at Diagnosis
    vs_5_5 = ValueSet(
        elements=[
            Coding(system=res.SNOMED_CT, code="118189007", 
                   display="Prenatal"),
            Coding(system=res.SNOMED_CT, code="3950001", display="Birth"),
            Coding(system=res.SNOMED_CT, code="410672004", display="Date"),
            Coding(system=res.SNOMED_CT, code="261665006", 
                   display="Unknown")
        ],
        name="Value set for 5.5 Age at Diagnosis",
        description=("The individual’s age when the diagnosis was made.")
    )

    # 5.6 Date of Diagnosis
    vs_5_6 = ValueSet(
        elements=[Date],
        name="Value set for 5.6 Date of Diagnosis",
        description=("If the specific month or day is not known, select the 1st "
                     "day of the month or the 1st month of the year, respectively.")
    )

    # 5.7 Body Site [SNOMED_CT CT]
    vs_5_7 = ValueSet(
        elements=[res.SNOMED_CT],
        name="Value set for 5.7 Body Site [SNOMED_CT CT]",
        description=("The specific body site affected by disease is encoded using all "
                     "descendants of SCT Body Structure (123037004).")
    )

    # 5.8 Clinical Status
    vs_5_8 = ValueSet(
        elements=[
            Coding(system=res.HL7FHIR, code="active", display="Active"),
            Coding(system=res.HL7FHIR, code="recurrence", 
                   display="Recurrence"),
            Coding(system=res.HL7FHIR, code="relapse", 
                   display="Relapse"),
            Coding(system=res.HL7FHIR, code="inactive", 
                   display="Inactive"),
            Coding(system=res.HL7FHIR, code="remission", 
                   display="Remission"),
            Coding(system=res.HL7FHIR, code="resolved", 
                   display="Resolved")
        ],
        name="Value set for 5.8 Clinical Status",
        description=("The clinical status of the disease indicates whether "
                     "it is active, inactive, or resolved.")
    )

    # 5.9 Severity
    vs_5_9 = ValueSet(
        elements=[
            Coding(system=res.SNOMED_CT, code="24484000", display="Severe"),
            Coding(system=res.SNOMED_CT, code="6736007", 
                   display="Moderate"),
            Coding(system=res.SNOMED_CT, code="255604002", display="Mild")
        ],
        name="Value set for 5.9 Severity",
        description=("The severity of the disease is categorised"
                     "by clinical evaluation.")
    )

# 6.1 Genetic Findings

    # 6.1.1 Genomic Diagnosis [MONDO, OMIM]
    vs_6_1_1 = ValueSet(
        elements=[res.MONDO, res.OMIM],
        name="Value set for 6.1.1 Genomic Diagnosis [MONDO]",
        description=("The genetic finding of a variant can be linked to a  "
                    "disease in (5.1) if the same MONDO code is used.")
    )

    # 6.1.2 Progress Status of Interpretation
    vs_6_1_2 = ValueSet(
        elements=[
            Coding(system=res.GA4GH, code="UNKNOWN_PROGRESS", 
                   display="No information is available about the diagnosis"),
            Coding(system=res.GA4GH, code="IN_PROGRESS", 
                   display="No diagnosis has been found to date but additional\
                     differential diagnostic work is in progress."),
            Coding(system=res.GA4GH, code="COMPLETED", 
                   display="The work on the interpretation is complete."),
            Coding(system=res.GA4GH, code="SOLVED", 
                   display="The interpretation is complete and also considered\
                     to be a definitive diagnosis"),
            Coding(system=res.GA4GH, code="UNSOLVED", 
                   display="The interpretation is complete but no definitive\
                     diagnosis was found")
        ],
        name="Value set for 6.1.2 Progress Status of Interpretation",
        description=("The interpretation has a ProgressStatus that refers to"
                    "the status of the attempted diagnosis.")
    )

    # 6.1.3 Interpretation Status
    vs_6_1_3 = ValueSet(
        elements=[
            Coding(system=res.GA4GH, code="UNKNOWN_STATUS", 
                   display="No information is available about the status"),
            Coding(system=res.GA4GH, code="REJECTED", 
                   display="The variant or gene reported here is interpreted\
                      not to be related to the diagnosis"),
            Coding(system=res.GA4GH, code="CANDIDATE", 
                   display="The variant or gene reported here is interpreted\
                      to possibly be related to the diagnosis"),
            Coding(system=res.GA4GH, code="CONTRIBUTORY", 
                   display="The variant or gene reported here is interpreted\
                      to be related to the diagnosis"),
            Coding(system=res.GA4GH, code="CAUSATIVE", 
                   display="The variant or gene reported here is interpreted\
                      to be causative of the diagnosis")
        ],
        name="Value set for 6.1.3 Interpretation Status",
        description=("An enumeration that describes the conclusion made about "
                    "the genomic interpretation.")
    )

    # 6.1.4 Structural Variant Analysis Method
    vs_6_1_4 = ValueSet(
        elements=[
            Coding(system=res.LOINC, code="LA26406-1", 
                   display="Karyotyping"),
            Coding(system=res.LOINC, code="LA26404-6", display="FISH"),
            Coding(system=res.LOINC, code="LA26418-6", display="PCR"),
            Coding(system=res.LOINC, code="LA26419-4", 
                   display="qPCR (real-time PCR)"),
            Coding(system=res.LOINC, code="LA26400-4", display="SNP array"),
            Coding(system=res.LOINC, code="LA26813-8", 
                   display="Restriction fragment length polymorphism (RFLP)"),
            Coding(system=res.LOINC, code="LA26810-4", 
                   display="DNA hybridization"),
            Coding(system=res.LOINC, code="LA26398-0", 
                   display="Sequencing"),
            Coding(system=res.LOINC, code="LA26415-2", display="MLPA"),
            Coding(system=res.LOINC, code="LA46-8", display="Other"),
            res.LOINC
        ],
        name="Value set for 6.1.4 Structural Variant Analysis Method",
        description=("The method used to analyse structural variants in the genome.")
    )
#        # 6.1.4a Other Structural Variant Analysis Method
#     vs_6_1_4a = ValueSet(
#               elements=[res.LOINC],
#               name="Value set for 6.1.4a Other Structural Variant Analysis Method",
#               description=("The method used to analyse structural variants\
#                             in the genome.")
#        )

    # 6.1.5 Reference Genome
    vs_6_1_5 = ValueSet(
        elements=[
            Coding(system=res.LOINC, code="LA14032-9", 
                   display="NCBI Build 34 (hg16)"),
            Coding(system=res.LOINC, code="LA14029-5", 
                   display="GRCh37 (hg19)"),
            Coding(system=res.LOINC, code="LA14030-3", 
                   display="NCBI Build 36.1 (hg18)"),
            Coding(system=res.LOINC, code="LA14031-1", 
                   display="NCBI Build 35 (hg17)"),
            Coding(system=res.LOINC, code="LA26806-2", 
                   display="GRCh38 (hg38)")
        ],
        name="Value set for 6.1.5 Reference Genome",
        description=("The reference genome used for analyzing the genetic\
                      variant.")
    )

    # 6.1.6 Genetic Mutation String
    vs_6_1_6 = ValueSet(
        elements=[str],  # HGVS strings for genetic mutations
        name="Value set for 6.1.6 Genetic Mutation String",
        description=("An unvalidated (HGVS) string that describes the variant\
                      change.")
    )

    # 6.1.7 Genomic DNA Change [g.HGVS]
    vs_6_1_7 = ValueSet(
        elements=[res.HGVS],  # HGVS strings for genomic DNA change
        name="Value set for 6.1.7 Genomic DNA Change [g.HGVS]",
        description=("The specific change in the genomic DNA sequence encoded "
                    "with a validated g.HGVS expression.")
    )

    # 6.1.8 Sequence DNA Change [c.HGVS]
    vs_6_1_8 = ValueSet(
        elements=[res.HGVS],  # HGVS strings for DNA sequence changes
        name="Value set for 6.1.8 Sequence DNA Change [c.HGVS]",
        description=("The specific change in the DNA sequence at the nucleotide  "
                    "level with a validated c.HGVS expression.")
    )

    # 6.1.9 Amino Acid Change [p.HGVS]
    vs_6_1_9 = ValueSet(
        elements=[res.HGVS],  # HGVS strings for amino acid changes
        name="Value set for 6.1.9 Amino Acid Change [p.HGVS]",
        description=("The specific change in the amino acid sequence resulting "
                    "from a genetic variant as a validated p.HGVS expression.")
    )

    # 6.1.10 Gene [HGNC-NR]
    vs_6_1_10 = ValueSet(
        elements=[res.HGNC],  # Gene codes
        name="Value set for 6.1.10 Gene [HGNC-NR]",
        description=("The specific gene or genes that were analyzed or "
                    " identified in the study.")
    )
    vs_6_1_10a = ValueSet(
       elements=[str], # Gene Label
       name="Value set for 6.1.10a Gene Label",
       description=("The specific gene or genes that were analyzed or "
              " identified in the study.")
    )

    # 6.1.11 Zygosity
    vs_6_1_11 = ValueSet(
        elements=[
            Coding(system=res.LOINC, code="LA6705-3", 
                   display="Homozygous"),
            Coding(system=res.LOINC, code="LA6706-1", 
                   display="(simple) Heterozygous"),
            Coding(system=res.LOINC, code="LA26217-2", 
                   display="Compound heterozygous"),
            Coding(system=res.LOINC, code="LA26220-6", 
                   display="Double heterozygous"),
            Coding(system=res.LOINC, code="LA6707-9", 
                   display="Hemizygous"),
            Coding(system=res.LOINC, code="LA6703-8", 
                   display="Heteroplasmic"),
            Coding(system=res.LOINC, code="LA6704-6", 
                   display="Homoplasmic"),
            Coding(system=res.LOINC, code="53034-5_other", 
                   display="Other"),
              res.LOINC
        ],
        name="Value set for 6.1.11 Zygosity",
        description=("The zygosity of the genetic variant.")
    )

#     # 6.1.11a Other Zygosity
#     vs_6_1_11a = ValueSet(
#               elements=[res.LOINC],
#               name="Value set for 6.1.11a Other Zygosity",
#               description=("The zygosity of the genetic variant.")
#     )

    # 6.1.12 Genomic Source Class
    vs_6_1_12 = ValueSet(
        elements=[
            Coding(system=res.LOINC, code="LA6683-2", 
                   display="Germline"),
            Coding(system=res.LOINC, code="LA6684-0", 
                   display="Somatic"),
            Coding(system=res.LOINC, code="LA10429-1", display="Fetal"),
            Coding(system=res.LOINC, code="LA18194-3", 
                   display="Likely germline"),
            Coding(system=res.LOINC, code="LA18195-0", 
                   display="Likely somatic"),
            Coding(system=res.LOINC, code="LA18196-8", 
                   display="Likely fetal"),
            Coding(system=res.LOINC, code="LA18197-6", 
                   display="Unknown genomic origin"),
            Coding(system=res.LOINC, code="LA26807-0", 
                   display="De novo")
        ],
        name="Value set for 6.1.12 Genomic Source Class",
        description=("The classification of the genomic source, such as germline, "
                    "somatic, or other origins.")
    )

       # 6.1.13 DNA Change Type
    vs_6_1_13 = ValueSet(
        elements=[
            Coding(system=res.LOINC, code="LA9658-1", 
                   display="Wild type"),
            Coding(system=res.LOINC, code="LA6692-3", display="Deletion"),
            Coding(system=res.LOINC, code="LA6686-5", 
                   display="Duplication"),
            Coding(system=res.LOINC, code="LA6687-3", display="Insertion"),
            Coding(system=res.LOINC, code="LA6688-1", 
                   display="Insertion/Deletion"),
            Coding(system=res.LOINC, code="LA6689-9", display="Inversion"),
            Coding(system=res.LOINC, code="LA6690-7", 
                   display="Substitution"),
            Coding(system=res.LOINC, code="48019-4_other", 
                   display="Other"),
            res.LOINC,
        ],
        name="Value set for 6.1.13 DNA Change Type",
        description=("The variant’s type of DNA change, such as point mutation, "
                    "deletion, insertion, or other types.")
    )
#        # 6.1.13a Other DNA Change Type
#     vs_6_1_13a = ValueSet(
#               elements=[res.LOINC],
#               name="Value set for 6.1.13a Other DNA Change Type",
#               description=("The variant’s type of DNA change, such as\
#                             missense, frameshift, or other types of mutation.")
#     )

    # 6.1.14 Clinical Significance [ACMG]
    vs_6_1_14 = ValueSet(
        elements=[
            Coding(system=res.LOINC, code="LA6668-3", 
                   display="Pathogenic"),
            Coding(system=res.LOINC, code="LA26332-9", 
                   display="Likely pathogenic"),
            Coding(system=res.LOINC, code="LA26333-7", 
                   display="Uncertain significance"),
            Coding(system=res.LOINC, code="LA26334-5", 
                   display="Likely benign"),
            Coding(system=res.LOINC, code="LA6675-8", display="Benign"),
            Coding(system=res.LOINC, code="LA4489-6", display="Unknown")
        ],
        name="Value set for 6.1.14 Clinical Significance [ACMG]",
        description=("The clinical significance of the genetic variant, "
                    "indicating its impact on health and disease.")
    )

    # 6.1.15 Therapeutic Actionability
    vs_6_1_15 = ValueSet(
        elements=[
            Coding(system=res.GA4GH, code="UNKNOWN_ACTIONABILITY", 
                   display="There is not enough information at this time to\
                      support any therapeutic actionability for this variant"),
            Coding(system=res.GA4GH, code="NOT_ACTIONABLE", 
                   display="This variant has no therapeutic actionability."),
            Coding(system=res.GA4GH, code="ACTIONABLE", 
                   display="This variant is known to be therapeutically\
                      actionable.")
        ],
        name="Value set for 6.1.15 Therapeutic Actionability",
        description=("This field flags the variant as being a candidate for\
                      treatment/clinical intervention, which could improve the\
                      clinical outcome.")
    )

    # 6.1.16 Clinical Annotation Level Of Evidence
    vs_6_1_16 = ValueSet(
        elements=[
            Coding(system=res.LOINC, code="LA30200-2", 
                   display="Very strong evidence pathogenic"),
            Coding(system=res.LOINC, code="LA30201-0", 
                   display="Strong evidence pathogenic"),
            Coding(system=res.LOINC, code="LA30202-8", 
                   display="Moderate evidence pathogenic"),
            Coding(system=res.LOINC, code="LA30203-6", 
                   display="Supporting evidence pathogenic"),
            Coding(system=res.LOINC, code="LA30204-4", 
                   display="Supporting evidence benign"),
            Coding(system=res.LOINC, code="LA30205-1", 
                   display="Strong evidence benign"),
            Coding(system=res.LOINC, code="LA30206-9", 
                   display="Stand-alone evidence pathogenic")
        ],
        name="Value set for 6.1.16 Clinical Annotation Level Of Evidence",
        description=("The level of evidence supporting the clinical annotation  "
                    "of the genetic variant.")
    )

# 6.2 Phenotypic Feature
    # 6.2.1 Phenotypic Feature
    vs_6_2_1 = ValueSet(
        elements=[res.HPO],
        name="Value set for 6.2.1 Phenotypic Feature",
        description=("An observed physical and clinical characteristic encoded "
                     "with HPO.")
    )

    # 6.2.2 Determination Date
    vs_6_2_2 = ValueSet(
        elements=[Date],
        name="Value set for 6.2.2 Determination Date",
        description=("The date on which the phenotypic feature was observed "
                     "or recorded.")
    )

    # 6.2.3 Status
    vs_6_2_3 = ValueSet(
        elements=[
            Coding(system=res.SNOMED_CT, code="410605003", 
                   display="Confirmed present"),
            Coding(system=res.SNOMED_CT, code="723511001", display="Refuted")
        ],
        name="Value set for 6.2.3 Status",
        description=("The current status of the phenotypic feature, indicating "
                     "whether it is confirmed or refuted.")
    )

    # 6.2.4 Modifier
    vs_6_2_4 = ValueSet(
        elements=[res.HPO, res.NCBITaxon, res.SNOMED_CT],
        name="Value set for 6.2.4 Modifier",
        description=("Further clinical modifiers to describe a specific "
                     "phenotypic feature, such as severity or linked\
                              causative agents.")
    )

# 6.3 Family History
    # 6.3.0 Family Member Pseudonym
    vs_6_3_0 = ValueSet(
        elements=[str],
        name="Value set for 6.3.0 Pseudonym",
        description=("If a pseudonym was already assigned to the specific "
                     "family member, please enter it here to identify across "
                     "records.")
    )

    # 6.3.1 Propositus/-a
    vs_6_3_1 = ValueSet(
        elements=[
            Coding(system=res.SNOMED_CT, code="373066001", 
                   display="Yes"),
            Coding(system=res.SNOMED_CT, code="373067005", 
                   display="No"),
            Coding(system=res.SNOMED_CT, code="261665006", 
                   display="Unknown"),
            Coding(system=res.SNOMED_CT, code="1220561009", 
                   display="Not recorded")
        ],
        name="Value set for 6.3.1 Propositus/-a",
        description=("Is the individual the first affected family member who "
                     "seeks medical attention for a genetic disorder, leading "
                     "to the diagnosis of other family members.")
    )

    # 6.3.2 Relationship of the individual to the index case / 
    # propositus/a
    vs_6_3_2 = ValueSet(
        elements=[
            Coding(system=res.SNOMED_CT, code="65656005", 
                   display="Natural mother"),
            Coding(system=res.SNOMED_CT, code="9947008", 
                   display="Natural father"),
            Coding(system=res.SNOMED_CT, code="83420006", 
                   display="Natural daughter"),
            Coding(system=res.SNOMED_CT, code="113160008", 
                   display="Natural son"),
            Coding(system=res.SNOMED_CT, code="60614009", 
                   display="Natural brother"),
            Coding(system=res.SNOMED_CT, code="73678001", 
                   display="Natural sister"),
            Coding(system=res.SNOMED_CT, code="11286003", 
                   display="Twin sibling"),
            Coding(system=res.SNOMED_CT, code="45929001", 
                   display="Half-brother"),
            Coding(system=res.SNOMED_CT, code="2272004", 
                   display="Half-sister"),
            Coding(system=res.SNOMED_CT, code="62296006", 
                   display="Natural grandfather"),
            Coding(system=res.SNOMED_CT, code="17945006", 
                   display="Natural grandmother"),
            Coding(system=res.SNOMED_CT, code="1220561009", 
                   display="Not recorded")
        ],
        name="Value set for 6.3.2 Relationship of the individual to the "
             "index case / propositus/a",
        description=("Specifies the familial relationship of the individual being "
                     "evaluated to the index case or propositus/proposita.")
    )

    # 6.3.3 Consanguinity
    vs_6_3_3 = ValueSet(
        elements=[
            Coding(system=res.SNOMED_CT, code="373066001", 
                   display="Yes"),
            Coding(system=res.SNOMED_CT, code="373067005", 
                   display="No"),
            Coding(system=res.SNOMED_CT, code="261665006", 
                   display="Unknown"),
            Coding(system=res.SNOMED_CT, code="1220561009", 
                   display="Not recorded")
        ],
        name="Value set for 6.3.3 Consanguinity",
        description=("The presence of a biological relationship between parents "
                     "who are related by blood, typically as first or second "
                     "cousins.")
    )

    # 6.3.4 Family Member Relationship
    vs_6_3_4 = ValueSet(
        elements=[
            Coding(system=res.SNOMED_CT, code="65656005", 
                   display="Natural mother"),
            Coding(system=res.SNOMED_CT, code="9947008", 
                   display="Natural father"),
            Coding(system=res.SNOMED_CT, code="83420006", 
                   display="Natural daughter"),
            Coding(system=res.SNOMED_CT, code="113160008", 
                   display="Natural son"),
            Coding(system=res.SNOMED_CT, code="60614009", 
                   display="Natural brother"),
            Coding(system=res.SNOMED_CT, code="73678001", 
                   display="Natural sister"),
            Coding(system=res.SNOMED_CT, code="11286003", 
                   display="Twin sibling"),
            Coding(system=res.SNOMED_CT, code="45929001", 
                   display="Half-brother"),
            Coding(system=res.SNOMED_CT, code="2272004", 
                   display="Half-sister"),
            Coding(system=res.SNOMED_CT, code="62296006", 
                   display="Natural grandfather"),
            Coding(system=res.SNOMED_CT, code="17945006", 
                   display="Natural grandmother"),
            Coding(system=res.SNOMED_CT, code="1220561009", 
                   display="Not recorded")
        ],
        name="Value set for 6.3.4 Family Member Relationship",
        description=("Specifies the relationship of the selected family member to "
                     "the patient.")
    )

    # 6.3.5 Family Member Record Status
    vs_6_3_5 = ValueSet(
        elements=[
            Coding(system=res.HL7FHIR, code="partial", 
                   display="Partial"),
            Coding(system=res.HL7FHIR, code="completed", 
                   display="Completed"),
            Coding(system=res.HL7FHIR, code="entered-in-error", 
                   display="Entered in Error"),
            Coding(system=res.HL7FHIR, code="health-unknown", 
                   display="Health Unknown")
        ],
        name="Value set for 6.3.5 Family Member Record Status",
        description=("Specifies the record’s status of the family history of a "
                     "specific family member.")
    )

    # 6.3.6 Family Member Sex
    vs_6_3_6 = ValueSet(
        elements=[
            Coding(system=res.SNOMED_CT, code="248152002", 
                   display="Female"),
            Coding(system=res.SNOMED_CT, code="248153007", 
                   display="Male"),
            Coding(system=res.SNOMED_CT, code="184115007", 
                   display="Patient sex unknown"),
            Coding(system=res.SNOMED_CT, code="32570691000036108", 
                   display="Intersex"),
            Coding(system=res.SNOMED_CT, code="1220561009", 
                   display="Not recorded")
        ],
        name="Value set for 6.3.6 Family Member Sex",
        description=("Specifies the sex (or gender) of the specific family member. "
                     "If possible, the sex assigned at birth should be selected.")
    )

    # 6.3.7 Family Member Age
    vs_6_3_7 = ValueSet(
        elements=[int],
        name="Value set for 6.3.7 Family Member Age",
        description=("Records the current age in full years of the selected family "
                     "member.")
    )

    # 6.3.8 Family Member Date of Birth
    vs_6_3_8 = ValueSet(
        elements=[Date],
        name="Value set for 6.3.8 Family Member Date of Birth",
        description=("Records the date of birth of the selected family member.")
    )

    # 6.3.9 Family Member Deceased
    vs_6_3_9 = ValueSet(
        elements=[
            Coding(system=res.SNOMED_CT, code="373066001", 
                   display="Yes"),
            Coding(system=res.SNOMED_CT, code="373067005", 
                   display="No"),
            Coding(system=res.SNOMED_CT, code="261665006", 
                   display="Unknown")
        ],
        name="Value set for 6.3.9 Family Member Deceased",
        description=("Indicates whether the selected family member is deceased.")
    )

    # 6.3.10 Family Member Cause of Death [ICD10CM]
    vs_6_3_10 = ValueSet(
        elements=[res.ICD10CM],
        name="Value set for 6.3.10 Family Member Cause of Death [ICD10CM]",
        description=("Records the cause of death of the selected deceased\
                      family member.")
    )

    # 6.3.11 Family Member Deceased Age
    vs_6_3_11 = ValueSet(
        elements=[int],
        name="Value set for 6.3.11 Family Member Deceased Age",
        description=("Records the age in full years of the selected family member "
                     "at death.")
    )

    # 6.3.12 Family Member Disease [MONDO]
    vs_6_3_12 = ValueSet(
        elements=[res.MONDO],
        name="Value set for 6.3.12 Family Member Disease [MONDO]",
        description=("Indicates whether the selected family member is affected "
                     "by the same RD as the individual or a different rare "
                     "disease.")
    )

    # 7.1 Consent Status
    vs_7_1 = ValueSet(
        elements=[
            Coding(system=res.HL7FHIR, code="draft", display="Pending"),
            Coding(system=res.HL7FHIR, code="proposed", display="Proposed"),
            Coding(system=res.HL7FHIR, code="active", display="Active"),
            Coding(system=res.HL7FHIR, code="rejected", display="Rejected"),
            Coding(system=res.HL7FHIR, code="inactive", display="Inactive"),
            Coding(system=res.HL7FHIR, code="entered-in-error", 
                   display="Entered in Error")
        ],
        name="Value set for 7.1 Consent Status",
        description=("Indicates the current status of the consent.")
    )

    # 7.2 Consent Date
    vs_7_2 = ValueSet(
        elements=[Date],
        name="7.2 Consent Date",
        description=("Records the date when the consent was given.")
    )

    # 7.3 Health Policy Monitoring
    vs_7_3 = ValueSet(
        elements=[str],
        name="7.3 Health Policy Monitoring",
        description=("The references to the policies that are included in this "
                    "consent scope. Policies may be organisational, but are often "
                    "defined jurisdictionally, or in law.")
    )

    # 7.4 Agreement to be contacted for research purposes
    vs_7_4 = ValueSet(
        elements=[
            Coding(system=res.SNOMED_CT, code="373066001", display="Yes"),
            Coding(system=res.SNOMED_CT, code="373067005", display="No"),
            Coding(system=res.SNOMED_CT, code="261665006", display="Unknown")
        ],
        name="Value set for 7.4 Agreement to be contacted for research purposes",
        description=("Indicates whether the patient agrees to be contacted for "
                    "research purposes.")
    )

    # 7.5 Consent to the reuse of data
    vs_7_5 = ValueSet(
        elements=[
            Coding(system=res.SNOMED_CT, code="373066001", display="Yes"),
            Coding(system=res.SNOMED_CT, code="373067005", display="No"),
            Coding(system=res.SNOMED_CT, code="261665006", display="Unknown")
        ],
        name="7.5 Consent to the reuse of data",
        description=("Indicates whether the patient consents to the reuse of  "
                    "their data.")
    )

    # 7.6 Biological sample
    vs_7_6 = ValueSet(
        elements=[
            Coding(system=res.SNOMED_CT, code="373066001", display="Yes"),
            Coding(system=res.SNOMED_CT, code="373067005", display="No"),
            Coding(system=res.SNOMED_CT, code="261665006", display="Unknown")
        ],
        name="7.6 Biological sample",
        description=("Indicates whether a patient's biological sample is  "
                    "available for research.")
    )

    # 7.7 Link to a biobank
    vs_7_7 = ValueSet(
        elements=[str],
        name="7.7 Link to a biobank",
        description=("If there is a biological sample, this data element\
                      indicates the link to the biobank of the patient's\
                      biological sample.")
    )

    #8.1 Classification of functioning / disability
    vs_8_1 = ValueSet(
    elements=[res.ICF],
    name="Value set for 8.1 Classification of functioning / disability",
    description=("Classification of functioning and disability based on the "
                 "International Classification of Functioning, Disability and "
                 "Health (ICF)."
    )
)


RARELINK_CDM_V2_0_0_VS = RareLink_CDM_v2_0_0_ValueSets()