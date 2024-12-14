from pathlib import Path
from typing import Union
from phenopacket_mapper.data_standards import DataModel, DataField, DataSet, OrGroup, ValueSet, DataSection
from phenopacket_mapper.data_standards import Coding, CodeSystem, Date, ValueSet
from . import RARELINK_CDM_V2_0_0_RESOURCES as res
from rarelink.utils.rarelink_cdm.rarelink_cdm_vs import RARELINK_CDM_V2_0_0_VS as VS

RARELINK_CDM_V2_0_0 = DataModel(
    name="RareLink Common Data Model 2.0.0",
    fields=()
)
#     fields=(
#         DataSection(
#             name="ODM",
#             fields=(
#                 DataField(
#                     name="xmlns",
#                     specification=str,
#                     required=True,
#                     description="Namespace for ODM v1.3,\
#                         e.g. http://www.cdisc.org/ns/odm/v1.3"
#                 ),
#                 DataField(
#                     name="xmlns:ds",
#                     specification=str,
#                     required=True,
#                     description="Namespace for XML digital signature (e.g.,\
#                         http://www.w3.org/2000/09/xmldsig#)"
#                 ),
#                 DataField(
#                     name="xmlns:xsi",
#                     specification=str,
#                     required=True,
#                     description="Namespace for XML Schema instance (e.g.,\
#                         http://www.w3.org/2001/XMLSchema-instance)"
#                 ),
#                 DataField(
#                     name="xmlns:redcap",
#                     specification=str,
#                     required=True,
#                     description="Namespace for REDCap extension (e.g.,\
#                         https://projectredcap.org)"
#                 ),
#                 DataField(
#                     name="xsi:schemaLocation",
#                     specification=str,
#                     required=True,
#                     description="Location of the ODM schema file (e.g.,\
#                         http://www.cdisc.org/ns/odm/v1.3 schema/odm/ODM1-3-1.xsd)"
#                 ),
#                 DataField(
#                     name="ODMVersion",
#                     specification=str,
#                     required=True,
#                     description="Version of the ODM format (e.g., 1.3.1)"
#                 ),
#                 DataField(
#                     name="FileOID",
#                     specification=str,
#                     required=True,
#                     description="Unique identifier for the ODM file (e.g.,\
#                             000-00-0000)"
#                 ),
#                 DataField(
#                     name="FileType",
#                     specification=str,
#                     required=True,
#                     description="Type of the file (e.g., Snapshot)"
#                 ),
#                 DataField(
#                     name="Description",
#                     specification=str,
#                     required=True,
#                     description="Description of the ODM file content (e.g., \
#                         the name of the local REDCap project)"
#                 ),
#                 DataField(
#                     name="AsOfDateTime",
#                     specification=Date,
#                     required=True,
#                     description="Date and time of the data snapshot"
#                 ),
#                 DataField(
#                     name="CreationDateTime",
#                     specification=Date,
#                     required=True,
#                     description="Date and time when the ODM file was created"
#                 ),
#                 DataField(
#                     name="SourceSystem",
#                     specification=str,
#                     required=True,
#                     description="System that generated the ODM file (e.g.,\
#                         REDCap)"
#                 ),
#                 DataField(
#                     name="SourceSystemVersion",
#                     specification=str,
#                     required=True,
#                     description="Version of the source system (e.g. 14.6.9)"
#                 ),
#                 DataSection(
#                     name="ClinicalData",
#                     fields=(
#                         DataField(
#                             name="StudyOID",
#                             specification=str,
#                             required=True,
#                             description="Unique identifier for the study or\
#                                 project (e.g., Project.ProjectName)"
#                         ),
#                         DataField(
#                             name="MetaDataVersionOID",
#                             specification=str,
#                             required=True,
#                             description="Version identifier for the metadata\
#                                 structure of the project (e.g.\
#                                     'Project.ProjectName_2024-10-14_1145')."
#                         ),
#                         DataSection(
#                             name="SubjectData",
#                             fields=(
#                                 DataField(
#                                     name="SubjectKey",
#                                     specification=str,
#                                     required=True,
#                                     description="Identifier for the subject\
#                                         or patient within the REDCap database."
#                                 ),
#                                 DataField(
#                                     name="redcap:RecordIdField",
#                                     specification=str,
#                                     required=True,
#                                     description="The primary record identifier\
#                                         field for REDCap (e.g. 'record_id')"
#                                 ),
#                                 DataSection(
#                                     name="FormData",
#                                     fields=(
#                                         DataField(
#                                             name="FormOID",
#                                             specification=str,
#                                             required=True,
#                                             description="Unique identifier for\
#                                                 the form using the REDCap form\
#                                                     name (e.g., 'Form.form_name')"
#                                         ),
#                                         DataField(
#                                             name="FormRepeatKey",
#                                             specification=str,
#                                             required=True,
#                                             description="Unique identifier for\
#                                                 the form repeat instance."
#                                         ),
#                                         DataSection(
#                                             name="ItemGroupData",
#                                             fields=(
#                                                 DataField(
#                                                     name="ItemGroupOID",
#                                                     specification=str,
#                                                     required=True,
#                                                     description="Unique identifier\
#                                                         for the item group using the\
#                                                             REDCap field name (e.g.,\
#                                                                 'form_name.variable_name')"
#                                                 ),
#                                                 DataField(
#                                                     name="ItemGroupRepeatKey",
#                                                     specification=str,
#                                                     required=True,
#                                                     description="Unique identifier\
#                                                         for the item group repeat instance."
#                                                 ),
#                                                 DataSection(
#                                                     name="ItemData",
#                                                     fields=(
#                                                         [DataField(
#                                                             name="ItemOID",
#                                                             specification=str,
#                                                             required=True,
#                                                             description="Unique identifier\
#                                                                 within the REDCap project \
#                                                                 (e.g., record_id)"
#                                                             ),
#                                                         DataField(
#                                                             name="Value",
#                                                             specification=str,
#                                                             required=True,
#                                                             description="Value of the record_id"
#                                                         )
#                                                         ],
#                                                         [
                                                            
#                                                         ]
#                                                     )
#                                                 )
                                                
#                                         )
#                                 )
#                             )
#                         )
#                     )
#                 )
#             )
#         )
#     )
# )))



            
            
                
                
                
#                 DataSection(
#                     name="1. Formal Criteria",
#                     fields=(
#                         DataField(
#                             name="Pseudonym",
#                             ordinal="1.1",
#                             specification=str,
#                             required=True,
#                             description="The (local) patient-related Identification code."
#                         ),
#                         DataField(
#                             name="Date of Admission",
#                             ordinal="1.2",
#                             specification=Date,
#                             required=True,
#                             description="The date of admission or data capture of the individual."
#                         ),   
#                     )
#                 ),
            
#                 DataSection(
#                     name="6.2 Phenotypic Feature",
#                     fields=(
#                         DataField(
#                             name="Phenotypic Feature",
#                             ordinal="6.2.1",
#                             specification=Coding,
#                             required=True,
#                             description="An observed physical and clinical\
#                                 characteristic encoded with HPO."
#                         ),
#                         DataField(
#                             name="Status",
#                             ordinal="6.2.2",
#                             specification=ValueSet(
#                                 name="Value set for 6.2.2 Phenotype Status",
#                                 elements=[
#                                     Coding(system=res.SNOMED_CT, code="410605003", 
#                                             display="Confirmed present"),
#                                     Coding(system=res.SNOMED_CT, code="723511001",
#                                         display="Refuted")
#                                 ]
#                             ),
#                             required=False,
#                             description="The current status of the phenotypic feature,\
#                                     indicating whether it is confirmed or refuted."
#                         ),
#                         DataField(
#                             name="Determination Date",
#                             ordinal="6.2.3",
#                             specification=Date,
#                             required=False,
#                             description="The date on which the phenotypic feature was\
#                                     observed or recorded."
#                         ),
#                         DataField(
#                             name="Resolution Date",
#                             ordinal="6.2.4",
#                             specification=Date,
#                             required=False,
#                             description="Time at which the feature resolved or abated."
#                         ),
#                         DataField(
#                             name="Age of Onset",
#                             ordinal="6.2.5",
#                             specification=ValueSet(
#                                 name="Value Set for 6.2.5 Onset Category",
#                                 elements=[
#                                     Coding(system=res.HPO, code="0011460", 
#                                             display="Embryonal onset (0w-8w embryonal)"),
#                                     Coding(system=res.HPO, code="0011461",
#                                             display="Fetal onset (8w embryonal - birth)"),
#                                     Coding(system=res.HPO, code="0003577", 
#                                             display="Congenital onset (at birth)"),
#                                     Coding(system=res.HPO, code="0003623", 
#                                             display="Neonatal onset (0d-28d)"),
#                                     Coding(system=res.HPO, code="0003593", 
#                                             display="Infantile onset (28d-1y)"),
#                                     Coding(system=res.HPO, code="0011463", 
#                                             display="Childhood onset (1y-5y)"),
#                                     Coding(system=res.HPO, code="0003621", 
#                                             display="Juvenile onset (5y-15y)"),
#                                     Coding(system=res.HPO, code="0011462", 
#                                             display="Young adult onset (16y-40y)"),
#                                     Coding(system=res.HPO, code="0003596", 
#                                             display="Middle age adult onset (40y-60y)"),
#                                     Coding(system=res.HPO, code="0003584", 
#                                             display="Late adult onset (60y+)"),
#                                 ],
#                             required=False,
#                             description="Time at which the feature was first observed\
#                                     within HPO onset categories"
#                             )
#                         ),
#                         DataField(
#                             name="Temporal Pattern",
#                             ordinal="6.2.6",
#                             specification=ValueSet(
#                                 name="Value Set for 6.2.6 Temporal Pattern",
#                                 elements=[
#                                     Coding(system=res.HPO, code="0011009",
#                                         display="Acute"),
#                                     Coding(system=res.HPO, code="0011010",
#                                         display="Chronic"),
#                                     Coding(system=res.HPO, code="0031914",
#                                         display="Fluctuating"),
#                                     Coding(system=res.HPO, code="0025297",
#                                         display="Prolonged"),
#                                     Coding(system=res.HPO, code="0031796",
#                                         display="Recurrent"),
#                                     Coding(system=res.HPO, code="0031915",
#                                         display="Stable"),
#                                     Coding(system=res.HPO, code="0011011",
#                                         display="Subactue"),
#                                     Coding(system=res.HPO, code="0025153",
#                                         display="Transient"),
#                                     ],
#                             required=False,
#                             description="The temporal pattern of the phenotypic feature."
#                             )
#                         ),
#                         DataField(
#                             name="Phenotype Severity",
#                             ordinal="6.2.7",
#                             specification=ValueSet(
#                                 name="Value Set for 6.2.7 Phenotype Severity",
#                                 elements=[
#                                     Coding(system=res.HPO, code="0012827",
#                                         display="Borderline"),
#                                     Coding(system=res.HPO, code="0012825",
#                                         display="Mild"),
#                                     Coding(system=res.HPO, code="0012826",
#                                         display="Moderate"),
#                                     Coding(system=res.HPO, code="0012829",
#                                         display="Profound"),
#                                     Coding(system=res.HPO, code="0012828",
#                                         display="Severe"),
#                                 ]
#                             ),
#                             required=False,
#                             description="A description of the severity of the\
#                                 feature described."
#                         ),
#                         DataField(
#                             name="Modifier_HPO_1",
#                             ordinal="6.2.8a",
#                             specification=Coding,
#                             required=False,
#                             description="Further clinical modifiers to describe a\
#                                 specific phenotypic feature, such as severity or linked\
#                                 causative agents."
#                         ),
#                         DataField(
#                             name="Modifier_HPO_1",
#                             ordinal="6.2.8b",
#                             specification=Coding,
#                             required=False,
#                             description="Further clinical modifiers to describe a\
#                                 specific phenotypic feature, such as severity or linked\
#                                 causative agents."
#                         ),
#                         DataField(
#                             name="Modifier_HPO_3",
#                             ordinal="6.2.8c",
#                             specification=Coding,
#                             required=False,
#                             description="Further clinical modifiers to describe a\
#                                 specific phenotypic feature, such as severity or linked\
#                                 causative agents."
#                         )
#                     )
#                 )      
#             )
#         )   
#     )
# )
    
        # RARELINK_CDM_V2_0_0.fields.append(
        #     DataField(section="6.2 Phenotypic Feature", ordinal="6.2.8a", 
        #               name=f"Modifier_HPO_1_{i}", specification=VS.vs_6_2_8a)
        # )
        # RARELINK_CDM_V2_0_0.fields.append(
        #     DataField(section="6.2 Phenotypic Feature", ordinal="6.2.8b", 
        #               name=f"Modifier_HPO_2_{i}", specification=VS.vs_6_2_8b)
        # )
        # RARELINK_CDM_V2_0_0.fields.append(
        #     DataField(section="6.2 Phenotypic Feature", ordinal="6.2.8c", 
        #               name=f"Modifier_HPO_3_{i}", specification=VS.vs_6_2_8c)
        # )
        # RARELINK_CDM_V2_0_0.fields.append(
        #     DataField(section="6.2 Phenotypic Feature", ordinal="6.2.8d", 
        #               name=f"Modifier_NCBITaxon_{i}", specification=VS.vs_6_2_8d)
        # )
        # RARELINK_CDM_V2_0_0.fields.append(
        #     DataField(section="6.2 Phenotypic Feature", ordinal="6.2.8e", 
        #               name=f"Modifier_SNOMED_CT_{i}", specification=VS.vs_6_2_8e)
        # )
        # RARELINK_CDM_V2_0_0.fields.append(
        #     DataField(section="6.2 Phenotypic Feature", ordinal="6.2.9", 
        #               name=f"Evidence_{i}", specification=VS.vs_6_2_9)
        # )


#         # 2. Personal Information
#         DataField(section="2. Personal Information", ordinal="2.1", 
#                    name="Date of Birth", specification=VS.vs_2_1),
#         DataField(section="2. Personal Information", ordinal="2.2", 
#                    name="Sex at Birth", specification=VS.vs_2_2),
#         DataField(section="2. Personal Information", ordinal="2.3", 
#                    name="Karyotypic Sex", specification=VS.vs_2_3),
#         DataField(section="2. Personal Information", ordinal="2.4", 
#                    name="Gender Identity", specification=VS.vs_2_4),
#         DataField(section="2. Personal Information", ordinal="2.5", 
#                    name="Country of Birth", specification=VS.vs_2_5),

#         # 3. Patient Status
#         DataField(section="3. Patient Status", ordinal="3.1", 
#                    name="Vital Status", specification=VS.vs_3_1),
#         DataField(section="3. Patient Status", ordinal="3.2", 
#                    name="Time of Death", specification=VS.vs_3_2),
#         DataField(section="3. Patient Status", ordinal="3.3", 
#                    name="Cause of Death", specification=VS.vs_3_3),
#         DataField(section="3. Patient Status", ordinal="3.4", 
#                    name="Age Category", specification=VS.vs_3_4),
#         DataField(section="3. Patient Status", ordinal="3.5", 
#                    name="Length of Gestation at Birth", specification=VS.vs_3_5),
#         DataField(section="3. Patient Status", ordinal="3.6", 
#                    name="Undiagnosed RD Case", specification=VS.vs_3_6),

#         # 7. Consent
#         DataField(section="7. Consent", ordinal="7.1", 
#                   name="Consent Status", specification=VS.vs_7_1),
#         DataField(section="7. Consent", ordinal="7.2", 
#                   name="Consent Date", specification=VS.vs_7_2),
#         DataField(section="7. Consent", ordinal="7.3", 
#                   name="Health Policy Monitoring", specification=VS.vs_7_3),
#         DataField(section="7. Consent", ordinal="7.4", name="Agreement to be contacted for research purposes", specification=VS.vs_7_4), 
#         DataField(section="7. Consent", ordinal="7.5", 
#                   name="Consent to the reuse of data", 
#                   specification=VS.vs_7_5),
#         DataField(section="7. Consent", ordinal="7.6", 
#                   name="Biological sample", 
#                   specification=VS.vs_7_6),
#         DataField(section="7. Consent", ordinal="7.7", 
#                   name="Link to a biobank", 
#                   specification=VS.vs_7_7),
    
#         # 8. Classification of functioning / disability
#         DataField(section="8. Classification", ordinal="8.1", 
#                   name="Classification of functioning / disability", 
#                   specification=VS.vs_8_1), 

#     ]
# )
# repeating fields:
# # 4. Care Pathway
# def append_care_pathway_fields(data_model, n=9999):
#     for i in range(n):
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="4. Care Pathway", ordinal="4.1", 
#                       name=f"Encounter Start_{i}", specification=VS.vs_4_1)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="4. Care Pathway", ordinal="4.2", 
#                       name=f"Encounter End_{i}", specification=VS.vs_4_2)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="4. Care Pathway", ordinal="4.3", 
#                       name=f"Encounter Status_{i}", specification=VS.vs_4_3)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="4. Care Pathway", ordinal="4.4", 
#                       name=f"Encounter Class_{i}", specification=VS.vs_4_4)
#         )


# # 5. Disease
# def append_disease_fields(data_model, n=9999):
#     for i in range(n):
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="5. Disease", ordinal="5.1A", 
#                       name=f"Disease MONDO_{i}", specification=VS.vs_5_1a)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="5. Disease", ordinal="5.1B", 
#                       name=f"Disease ORDO_{i}", specification=VS.vs_5_1b)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="5. Disease", ordinal="5.1C", 
#                       name=f"Disease ICD10CM_{i}", specification=VS.vs_5_1c)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="5. Disease", ordinal="5.1D", 
#                       name=f"Disease ICD11_{i}", specification=VS.vs_5_1d)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="5. Disease", ordinal="5.1E", 
#                       name=f"Disease OMIM_P_{i}", specification=VS.vs_5_1e)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="5. Disease", ordinal="5.2", 
#                       name=f"Verification Status_{i}", specification=VS.vs_5_2)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="5. Disease", ordinal="5.3", 
#                       name=f"Age at Onset_{i}", specification=VS.vs_5_3)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="5. Disease", ordinal="5.4", 
#                       name=f"Date of Onset_{i}", specification=VS.vs_5_4)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="5. Disease", ordinal="5.5", 
#                       name=f"Age at Diagnosis_{i}", specification=VS.vs_5_5)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="5. Disease", ordinal="5.6", 
#                       name=f"Date of Diagnosis_{i}", specification=VS.vs_5_6)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="5. Disease", ordinal="5.7", 
#                       name=f"Body Site_{i}", specification=VS.vs_5_7)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="5. Disease", ordinal="5.8", 
#                       name=f"Clinical Status_{i}", specification=VS.vs_5_8)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="5. Disease", ordinal="5.9", 
#                       name=f"Disease Severity_{i}", specification=VS.vs_5_9)
#         )

# # 6.1 Genetic Findings
# def append_genetic_findings_fields(data_model, n=9999):
#     for i in range(n):
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.1 Genetic Findings", ordinal="6.1.1", 
#                       name=f"Genomic Diagnosis_MONDO_{i}", specification=VS.vs_6_1_1a)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.1 Genetic Findings", ordinal="6.1.1", 
#                       name=f"Genomic Diagnosis_OMIM_P_{i}", specification=VS.vs_6_1_1b)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.1 Genetic Findings", ordinal="6.1.2", 
#                       name=f"Progress Status of Interpretation_{i}", specification=VS.vs_6_1_2)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.1 Genetic Findings", ordinal="6.1.3", 
#                       name=f"Interpretation Status_{i}", specification=VS.vs_6_1_3)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.1 Genetic Findings", ordinal="6.1.4", 
#                       name=f"Structural Variant Analysis Method_{i}", specification=VS.vs_6_1_4)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.1 Genetic Findings", ordinal="6.1.4a", 
#                       name=f"Structural Variant Analysis Method_other_{i}", specification=VS.vs_6_1_4a)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.1 Genetic Findings", ordinal="6.1.5", 
#                       name=f"Reference Genome_{i}", specification=VS.vs_6_1_5)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.1 Genetic Findings", ordinal="6.1.6", 
#                       name=f"Genetic Mutation String_{i}", specification=VS.vs_6_1_6)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.1 Genetic Findings", ordinal="6.1.7", 
#                       name=f"Genomic DNA Change [g.HGVS]_{i}", specification=VS.vs_6_1_7)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.1 Genetic Findings", ordinal="6.1.8", 
#                       name=f"Sequence DNA Change [c.HGVS]_{i}", specification=VS.vs_6_1_8)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.1 Genetic Findings", ordinal="6.1.9", 
#                       name=f"Amino Acid Change [p.HGVS]_{i}", specification=VS.vs_6_1_9)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.1 Genetic Findings", ordinal="6.1.10", 
#                       name=f"Gene_{i}", specification=VS.vs_6_1_10)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.1 Genetic Findings", ordinal="6.1.10a", 
#                       name=f"Gene Label_{i}", specification=VS.vs_6_1_10a)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.1 Genetic Findings", ordinal="6.1.11", 
#                       name=f"Zygosity_{i}", specification=VS.vs_6_1_11)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.1 Genetic Findings", ordinal="6.1.11a", 
#                       name=f"Zygosity_other_{i}", specification=VS.vs_6_1_11a)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.1 Genetic Findings", ordinal="6.1.12", 
#                       name=f"Genomic Source Class_{i}", specification=VS.vs_6_1_12)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.1 Genetic Findings", ordinal="6.1.13", 
#                       name=f"DNA Change Type_{i}", specification=VS.vs_6_1_13)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.1 Genetic Findings", ordinal="6.1.13a", 
#                       name=f"DNA Change Type_other_{i}", specification=VS.vs_6_1_13a)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.1 Genetic Findings", ordinal="6.1.14", 
#                       name=f"Clinical Significance [ACMG]_{i}",
#                       specification=VS.vs_6_1_14)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.1 Genetic Findings", ordinal="6.1.15", 
#                       name=f"Therapeutic Actionability_{i}",
#                       specification=VS.vs_6_1_15)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.1 Genetic Findings", ordinal="6.1.16", 
#                       name=f"Clinical Annotation Level Of Evidence_{i}",
#                       specification=VS.vs_6_1_16)
#         )

# # 6.2 Phenotypic Feature
# def append_phenotypic_features(data_model, n=9999):
#     for i in range(n):
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.2 Phenotypic Feature", ordinal="6.2.1", 
#                       name=f"Phenotypic Feature_{i}", specification=VS.vs_6_2_1)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.2 Phenotypic Feature", ordinal="6.2.2", 
#                       name=f"Status_{i}", specification=VS.vs_6_2_2)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.2 Phenotypic Feature", ordinal="6.2.3", 
#                       name=f"Determination Date_{i}", specification=VS.vs_6_2_3)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.2 Phenotypic Feature", ordinal="6.2.4", 
#                       name=f"Resolution Date_{i}", specification=VS.vs_6_2_4)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.2 Phenotypic Feature", ordinal="6.2.5", 
#                       name=f"Onset Category_{i}", specification=VS.vs_6_2_5)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.2 Phenotypic Feature", ordinal="6.2.6", 
#                       name=f"Temporal Pattern_{i}", specification=VS.vs_6_2_6)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.2 Phenotypic Feature", ordinal="6.2.7", 
#                       name=f"Phenotype Severity_{i}", specification=VS.vs_6_2_7)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.2 Phenotypic Feature", ordinal="6.2.8a", 
#                       name=f"Modifier_HPO_1_{i}", specification=VS.vs_6_2_8a)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.2 Phenotypic Feature", ordinal="6.2.8b", 
#                       name=f"Modifier_HPO_2_{i}", specification=VS.vs_6_2_8b)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.2 Phenotypic Feature", ordinal="6.2.8c", 
#                       name=f"Modifier_HPO_3_{i}", specification=VS.vs_6_2_8c)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.2 Phenotypic Feature", ordinal="6.2.8d", 
#                       name=f"Modifier_NCBITaxon_{i}", specification=VS.vs_6_2_8d)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.2 Phenotypic Feature", ordinal="6.2.8e", 
#                       name=f"Modifier_SNOMED_CT_{i}", specification=VS.vs_6_2_8e)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.2 Phenotypic Feature", ordinal="6.2.9", 
#                       name=f"Evidence_{i}", specification=VS.vs_6_2_9)
#         )





        
# # 6.3 Mesaurments
# def append_measurements_fields(data_model, n=9999):
#     for i in range(n):
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.3 Measurements", ordinal="6.3.1",
#                       name=f"Assay_{i}", specification=VS.vs_6_3_1)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.3 Measurements", ordinal="6.3.2",
#                       name=f"Value_{i}", specification=VS.vs_6_3_2)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.3 Measurements", ordinal="6.3.3",
#                       name=f"Value Unit_{i}", specification=VS.vs_6_3_3)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.3 Measurements", ordinal="6.3.4",
#                       name=f"Interpretation_{i}", specification=VS.vs_6_3_4)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.3 Measurements", ordinal="6.3.5",
#                       name=f"Time Observed_{i}", specification=VS.vs_6_3_5)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.3 Measurements", ordinal="6.3.6",
#                       name=f"Procedure_{i}", specification=VS.vs_6_3_6)
#         )
        
        
        
# # 6.4 Family History
# def append_family_history_fields(data_model, n=9999):
#     for i in range(n):
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.4 Family History", ordinal="6.4.1", 
#                       name=f"Family Member Pseudonym_{i}", specification=VS.vs_6_4_1)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.4 Family History", ordinal="6.4.2", 
#                       name=f"Propositus/-a_{i}", specification=VS.vs_6_4_2)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.4 Family History", ordinal="6.4.3", 
#                       name=f"Relationship of the individual to the index\
#                           case/propositus/a_{i}", 
#                       specification=VS.vs_6_4_3)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.4 Family History", ordinal="6.4.4", 
#                       name=f"Consanguinity_{i}", specification=VS.vs_6_4_4)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.4 Family History", ordinal="6.4.5", 
#                       name=f"Family Member Relationship_{i}",
#                       specification=VS.vs_6_4_5)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.4 Family History", ordinal="6.4.6", 
#                       name=f"Family Member Record Status_{i}",
#                       specification=VS.vs_6_4_6)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.4 Family History", ordinal="6.4.7", 
#                       name=f"Family Member Sex_{i}",
#                       specification=VS.vs_6_4_7)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.4 Family History", ordinal="6.4.8", 
#                       name=f"Family Member Age_{i}",
#                       specification=VS.vs_6_4_8)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.4 Family History", ordinal="6.4.9", 
#                       name=f"Family Member Date of Birth_{i}",
#                       specification=VS.vs_6_4_9)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.4 Family History", ordinal="6.4.10", 
#                       name=f"Family Member Deceased_{i}",
#                       specification=VS.vs_6_4_10)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.4 Family History", ordinal="6.4.11", 
#                       name=f"Family Member Cause of Death_{i}",
#                       specification=VS.vs_6_4_11)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.4 Family History", ordinal="6.4.12", 
#                       name=f"Family Member Deceased Age_{i}",
#                       specification=VS.vs_6_4_12)
#         )
#         RARELINK_CDM_V2_0_0.fields.append(
#             DataField(section="6.4 Family History", ordinal="6.4.13", 
#                       name=f"Family Member Disease_{i}", specification=VS.vs_6_4_13)
#         )


# append_care_pathway_fields(RARELINK_CDM_V2_0_0)
# append_disease_fields(RARELINK_CDM_V2_0_0)
# append_genetic_findings_fields(RARELINK_CDM_V2_0_0)
# append_phenotypic_features(RARELINK_CDM_V2_0_0)
# append_family_history_fields(RARELINK_CDM_V2_0_0)


def load_rarelink_data(path: Union[str, Path], data_model: DataModel = RARELINK_CDM_V2_0_0) -> DataSet:
    """This loads data from a path using the latest version of the Rarelink CDM.
    :param path: The path to the data file.
    :param data_model: The data model to use for loading the data.
    :return: The loaded data set.
    """
    return data_model.load_data(
        path,
    )
#         "snomed_422549004",
#     )
#         "snomed_399423000",
#         "snomed_184099003",
#         "snomed_281053000",
#         "snomed_1296886006",
#         "snomed_263495000",
#         "snomed_370159000",
#         "snomed_278844005",
#         "snomed_398299004",
#         "snomed_184305005",
#         "snomed_105727008",
#         "snomed_412726003",
#         "snomed_723663001",
#         "snomed_309370004",
#         "hl7fhir_consent_datetime",
#         "snomed_386318002",
#         "rarelink_consent_contact",
#         "rarelink_consent_data",
#         "snomed_123038009",
#         "rarelink_biobank_link", 
#         "rarelink_icf_score",
    # )    #     verification_status_column="loinc_99498_8",
    #     age_at_onset_column="snomed_424850005",
    #     date_of_onset_column="snomed_298059007",
    #     age_at_diagnosis_column="snomed_423493009",
    #     date_of_diagnosis_column="snomed_432213005",
    #     body_site_column="snomed_363698007",
    #     clinical_status_column="snomed_263493007",
    #     disease_severity_column="snomed_246112005",
    #     genomic_diagnosis_mondo_column="snomed_106221001_mondo",
    #     genomic_diagnosis_omim_p="snomed_106221001_omim_p",
    #     progress_status_of_interpretation_column="ga4gh_progress_status",
    #     interpretation_status_column="ga4gh_interp_status",
    #     structural_variant_analysis_method_column="loinc_81304_8",
    #     structural_variant_analysis_method_other_column="loinc_81304_8_other",
    #     reference_genome_column="loinc_62374_4",
    #     genetic_mutation_string_column="loinc_lp7824_8",
    #     genomic_dna_change_column="loinc_81290_9",
    #     sequence_dna_change_column="loinc_48004_6",
    #     amino_acid_change_column="loinc_48005_3",
    #     gene_column="loinc_48018_6",
    #     gene_label_column="loinc_48018_6_label",
    #     zygosity_column="loinc_53034_5",
    #     zygosity_other_column="loinc_53034_5_other",
    #     genomic_source_class_column="loinc_48002_0",
    #     dna_change_type_column="loinc_48019_4",
    #     dna_change_type_other_column="loinc_48019_4_other",
    #     clinical_significance_acmg_column="loinc_53037_8",
    #     therapeutic_actionability_column="ga4gh_therap_action",
    #     clinical_annotation_level_of_evidence_column="loinc_93044_6",
    #     phenotypic_feature_column="snomed_8116006",
    #     status_column="snomed_363778006",
    #     determination_date_column="snomed_8116006_onset",
    #     resolution_date_column="snomed_8116006_resolution",
    #     age_of_onset_column="hp_0003674",
    #     temporal_pattern_column="hp_0011008",        
    #     phenotype_severity_column="hp_0012824",
    #     modifier_hpo_1_column="hp_0012823_hp1", 
    #     modifier_hpo_2_column="hp_0012823_hp2",
    #     modifier_hpo_3_column="hp_0012823_hp3",
    #     modifier_ncbitaxon_column="hp_0012823_ncbitaxon",
    #     modifier_snomed_ct_column="hp_0012823_snomed",
    #     evidence_columnn="phenotypicfeature_evidence",
    #     assay_column="ncit_c60819",
    #     value_column="ncit_c25712",
    #     value_unit_column="ncit_c92571",
    #     interpretation_column="ncit_c41255",
    #     time_observed_column="ncit_c82577",
    #     procedure_column="snomed_122869004",
    #     family_member_pseudonym_column="family_history_pseudonym",
    #     propositus_a_column="snomed_64245008",
    #     relationship_of_the_individual_to_the_index_case_propositus_a_column=
    #                         "snomed_408732007",
    #     consanguinity_column="snomed_842009",
    #     family_member_relationship_column="snomed_444018008",
    #     family_member_record_status_column="hl7fhir_fmh_status",
    #     family_member_sex_column="loinc_54123_5",
    #     family_member_age_column="loinc_54141_7",
    #     family_member_date_of_birth_column="loinc_54124_3",
    #     family_member_deceased_column="snomed_740604001",
    #     family_member_cause_of_death_column="loinc_54112_8",
    #     family_member_deceased_age_column="loinc_92662_6",
    #     family_member_disease_column="loinc_75315_2",
    #     consent_status_column="snomed_309370004",
    #     consent_date_column="hl7fhir_consent_datetime",
    #     health_policy_monitoring_column="snomed_386318002",
    #     agreement_to_be_contacted_for_research_purposes_column="rarelink_consent_contact",
    #     consent_to_the_reuse_of_data_column="rarelink_consent_data",
    #     biological_sample_column="snomed_123038009",
    #     link_to_a_biobank_column="rarelink_biobank_link", 
    #     classification_of_functioning_disability_column="rarelink_icf_score",
    # )


