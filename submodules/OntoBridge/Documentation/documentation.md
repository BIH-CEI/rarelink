# Introduction
OntoBridge is a medical database standardization tool that enables users to transform their local database into different standards through a single pipeline. OntoBridge uses a set of ontologies that represent the knowledge of both the local database and the various standards to which the data will be transformed, relating them to each other to facilitate standardization. 

OntoBridge was developed by the Clinical Informatics team at Hospital Clínic de Barcelona to address the need to standardize their local data under various standards. With the goal of promoting open science and data democratization, the tool has been made available in an open repository for public use. 

This guide aims to provide users with the basic knowledge necessary to use OntoBridge and streamline the process of transforming relational data into standardized formats. Throughout the guide, a detailed walkthrough of preparatory steps, essential configurations, and methodologies for the effective standardization and integration of clinical data is provided. 

# Preparing the Local Database for OntoBridge Integration
Preparing the local database is a crucial step before leveraging the OntoBridge framework to transform relational database content. Ensure the local database is hosted on a queryable DBMS. This setup is necessary because OntoBridge is designed to interface smoothly with relational databases, allowing for efficient data retrieval and manipulation. Apart from the data stored in clinical events tables, local dictionaries and mapping tables should be created if they do not already exist. 

## Development of Dictionaries and Mapping Tables
Local dictionaries may already exist in the source database; otherwise, they need to be created. These typically hold a local code and its description, although they may be more complex depending on the clinical subdomain. Every concept of any column that could be reused throughout events tables should be included in these dictionaries (e.g., diagnosis, codes for types of diagnosis, drug routes, medical units, etc.). 

Standard dictionaries should be created according to the site’s needs and possibilities. For our case, we downloaded a database from OHDSI’s Athena containing all the vocabularies we use. We then created a table that contains the subset of terms within Athena that are represented in our local dictionaries. 

Mapping tables should contain the semantic mappings between local concepts (e.g., “SO2”) and standard concepts (e.g., SNOMED CT code 442440005). Ideally, mapping tables should represent the local code, the local domain, the standard vocabulary, and the standard code. Our mapping table, focused on OMOP and i2b2 as CDMs, looks like this: 

![Dictionary_example](/images/Dictionary_example.PNG)


In this example, local_uri refers to the name of the individual (after the namespace), local_ref is the local code, local domain refers to the domain within the local dictionaries, and the rest of the terms are either from OMOP (concept_code, concept_id, concept_name, vocabulary_id, omop_domain) or from i2b2 (concept_cd, concept_path). These tables are vital for ensuring consistency and interoperability with the target data model. 

# Ontologies
OntoBridge relies on a set of ontologies to represent the knowledge of different databases. Although there are various options for creating ontologies, we recommend using Protégé because it is open-source software with a simple interface that allows quick and methodical ontology creation. The ontological system we use has three different conceptual parts: 

1. **Local Data Model Ontologies:** Represented by the Local Model Ontology, which models the structure of the database, and the Clinical Records Ontology, which contains the clinical data of patients as instances.

2. **Standard Data Model Ontologies:** Represented by the CDM Ontology, modeling the structure of the CDM, and the Standard Dictionary Ontology, which contains all standard codes used for the use case as instances organized into classes representing each domain.

3. **Mapping Ontology:** Maps the local model to the standard model, consisting of a single ontology called Mapping Ontology.

![Ontobridge_schema](/images/Ontobridge_schema.png)


Users who want to use OntoBridge must create the ontologies that represent the local model and the ontology that maps the local model to the standard.

## Local Data Model Ontology
As defined above, the local database is modeled within a single ontology called the Local Model Ontology. 

### Modeling Tables and Attributes 

* **Modeling Tables:** Each table in the local database is represented by a class. Create a class for each table in the local data repository. 

* **Modeling Attributes:** Attributes of the tables are modeled as properties, with the table class as the domain and the attribute values as the range. Use owl:DatatypeProperty for attributes like dates, numerical values, or strings, and owl:ObjectProperty for attributes with local database codes, setting the relevant class from the local dictionary as the range. 

By following this structure, when an instance is created within a class modeling a table, it inherits all the properties representing the attributes of that table. 

### Modeling the dictionary of the Local Model Ontology 
To model the dictionary within the ontology, first create a class called "Local_dictionary." Then, create a class for each set of codes that can be assigned within an attribute of a local model table. For example, if the "medications" table has an attribute "Medication Route," create a Drug_route class as a child of the Local_dictionary class and instances within the Drug_route class for each route type in the local database. 

Finally, create properties to set additional information for the instances representing the different local concepts used. For example, create a Creation_date property as an owl:DatatypeProperty to record the creation date of each code. 

## Standard Model Ontologies

The standard model comprises two separate ontologies: 

1. **Standard Model Ontology:** Contains the structure of the CDM. CDM tables are modeled as rdf:Property metaclasses, with their table properties as sub-metaclasses. This structure aids in mapping the local model to the CDM, which is done once. 

2. **Standard Codes Ontology:** Contains the standard codes organized by domains. This ontology is crucial for semantic mapping, aligning local codes with universal standards to ensure data interoperability and semantic consistency. 

![OMOP_Onto](/images/OMOP_example.PNG)

## Mapping Ontology
The mapping ontology includes two levels of mappings: 

1. **Semantic Mappings:** Represented by sameAs triplets, linking local code instances to their standard equivalents for semantic data integration. 

2. **Syntactic Mappings:** Local properties (e.g., database columns) are mapped to CDM structure properties using rdf:Property metaclasses, enabling syntactic transformation from the local schema to the CDM schema, preserving data meaning and context. 

## Clinical Events Ontology
The clinical events ontology imports the structure from the local database, which is contained within the local data model ontology. It is within this ontology that the data regarding patients' clinical events are subsequently inserted as instances. This process is detailed in the following sections.

# Transformation of Relational Database into RDF through Ontop

## Creation of the clinical data RDF files using Ontop
Ontop is a framework designed for data virtualization, providing a way to access relational databases through the abstraction layer of the Semantic Web. It allows users to map relational data to RDF (Resource Description Framework) graphs using SQL queries as a bridge. 

## Ontop Materialize 
Ontop Materialize is a specific functionality within the Ontop framework that allows for the generation (or "materialization") of RDF triples from relational databases based on predefined mappings. 

Steps to Use Ontop's Materialize Tool

1. **Define R2RML Mappings:** Before using the materialize tool, R2RML mappings must be defined. These mappings specify how tables and columns in the relational database correspond to RDF individuals, classes and properties.

2. **Configuration:** Ontop must be correctly configured with the database connection details, this is done in the properties file

3. **Running the Materialize Tool:** This process will read the database using the R2RML mappings and generate RDF triples.

4. **Output:** The output will be a set of RDF triples in the chosen format (e.g., Turtle, RDF/XML, etc.).

## Creation of the R2RML mappings 

### R2RML Clinical Events 

As we have already seen throughout this document, it is essential to have the clinical data inserted within the ontology, since in this way they can be mapped to the standard to which they wish to be transformed. Below we explain step by step how we would proceed to create an R2RML to insert patient diagnostic event data into an ontology. 

**Prefix Declarations**

The prefixes define short forms for commonly used URIs. This helps to keep the mappings concise and readable. 

```turtle
@prefix rr: <http://www.w3.org/ns/r2rml#>.

@prefix dtnex: <http://infmed.fcrb.es/ontologias/datanex.owl#>.

@prefix xsd: <http://www.w3.org/2001/XMLSchema#>.
```

**TriplesMap Declaration**
A TriplesMap defines how data from a relational table is mapped to RDF triples. 

```turtle
<#diagnosticos-mapping>
  a rr:TriplesMap  ;
```

**Logical Table**
The "TriplesMap" takes as a data source the result of executing the SQL query SELECT DISTINCT * FROM diagnostic_events and uses each row resulting from that query to generate RDF triples. The triples are built using the logic in the following sections.

```turtle
  rr:logicalTable [     rr:sqlQuery "SELECT DISTINCT * FROM diagnostic_events" ];
  a rr:TriplesMap  ;
```

**Subject Map**

```turtle
  rr:subjectMap [
    rr:template "http://infmed.fcrb.es/ontologias/reg_datanex.owl#Diagnostico_{diag_id}";
    rr:class dtnex:Diagnostic_event ;
  ];
```

The subject map indicates that for each processed data row, an RDF subject (an entity) will be generated with a URI based on the template http://infmed.fcrb.es/ontologias/reg_datanex.owl#Diagnostico_{diag_id}, where {diag_id} is replaced with the corresponding value of the diagnosis identifier. This RDF subject will be an individual of the dtnex:Diagnostic_event class, which represents a diagnostic event in the dtnex ontology.

**Predicate-Object Maps**

Predicate-Object Maps define how data from a database table is mapped to an RDF model. Each predicateObjectMap defines a predicate (a property or relationship) and an object (a value) for an RDF triple. The object values ​​are obtained from specific database columns, and are assigned corresponding data types (xsd:long, xsd:datetime, etc.). In one case, the object is a dynamically generated IRI from a database template and value. These RDF triples are part of the generated RDF graph, where each subject (defined by the subjectMap shown above) is related to the objects defined in these predicateObjectMap through the specified predicates.

```turtle
  rr:predicateObjectMap [    rr:predicate dtnex:patient_id_dx;    rr:objectMap [      rr:column "patient_ref";      rr:datatype xsd:long;    ]
  ];

  rr:predicateObjectMap [    rr:predicate dtnex:episode_id_dx;    rr:objectMap [      rr:column "episode_ref";      rr:datatype xsd:long;    ]
  ];

  rr:predicateObjectMap [    rr:predicate dtnex:diag_reg_date;    rr:objectMap [      rr:column "reg_date";      rr:datatype xsd:datetime;    ]
  ];

  rr:predicateObjectMap [    rr:predicate dtnex:diag_ref;    rr:objectMap [      rr:column "diag_ref";      rr:termType rr:IRI;      rr:template "http://infmed.fcrb.es/ontologias/datanex.owl#Dx_{diag_ref}";    ]
  ];

  rr:predicateObjectMap [    rr:predicate dtnex:diag_id;    rr:objectMap [      rr:column "diag_id";    rr:datatype xsd:long;    ]
  ].
```

## R2RML Local concept codes
As we have seen previously, an essential part of OntoBridge is to have all the local codes used in the data use case that we want to standardize represented within the Local Codes Ontology. This implies that all the codes must be inserted within the ontology. In order to do this in a simple and dynamic way, it is advisable to do it through Ontop. Below is an example of how the codes that represent the gender of a patient can be inserted within the mapping ontology. As you can see, the codes are inserted as instances in the "Sex_dictionary" class, and the name that this variable receives in the local database is also included as a datatype.

```turtle
@prefix rr: <http://www.w3.org/ns/r2rml#>. 
@prefix dtnex: <http://infmed.fcrb.es/ontologias/datanex.owl#>. 
@prefix xsd: <http://www.w3.org/2001/XMLSchema#>. 

<#sex-mapping> 
  a rr:TriplesMap  ; 
  rr:logicalTable [ 
    rr:sqlQuery "SELECT DISTINCT sexo FROM paciente" 
  ]; 

  rr:subjectMap [ 
    rr:template "http://infmed.fcrb.es/ontologias/datanex.owl#Sex_{sexo}"; 
    rr:class dtnex:Sex_dictionary ; 
  ]; 

  rr:predicateObjectMap [ 
    rr:predicate dtnex:local_name; 
    rr:objectMap [ 
      rr:column "sexo"; 
      rr:datatype xsd:string; 
    ] 
  ]. 
```

## R2RML SameAs
Finally, the mapping between local variables and standard ones can also be performed using a TTL with Ontop, where the relationship of sameAs is established between the different instances to be mapped. For this purpose, the dictionary is used that maps local concepts to standards.

```turtle
<#sameas_classdiag_mapping> 

  rr:logicalTable [ 
    rr:sqlQuery "SELECT DISTINCT local_uri, concept_id FROM diccionario_hcb WHERE concept_id IS NOT NULL AND local_domain = 'Class_diag_dictionary' AND concept_id IN (SELECT DISTINCT concept_id FROM concept_datanex)" 
  ]; 

  rr:subjectMap [ 
    rr:template "http://infmed.fcrb.es/ontologias/datanex.owl#{local_uri}"; 
    rr:class dtnex:Class_diag_dictionary 
  ]; 

  rr:predicateObjectMap [    rr:predicate owl:sameAs;    rr:objectMap [      rr:column "concept_id";    rr:termType rr:IRI;      rr:template "http://ontoar.clinic.cat/ontologias/standard_concepts.owl#OMOP_{concept_id}";    ] 

  ]. 
```

## Isertion of clinical events data to OWLs
Once the RDFs have been created, they are inserted into the respective ontologies using a Python script that uses the rdflib library to work with graphs. Specifically, 4 insertions must be performed: The RDF of the local code dictionaries is inserted into the ontology of the local data model, the standard codes are inserted into the ontology of the standard model, the clinical event data is inserted into the clinical event ontology and, finally, the mappings between standard and non-standard codes are inserted into the mapping ontology.

To perform this insertion, the following Python code is used:

```python
def add_data_to_graph(files_directory, file_extension, file_format):
    graph = rdflib.Graph()
    files = glob.glob(files_directory + file_extension)
    for file in files:
        graph.parse(file, format=file_format)
    return graph

def add_rdf_to_owl(chosen_model): 
    rdf_graph = add_data_to_graph(VOLUME_PATH, 
        RDF_EXTENSION, RDF_FORMAT)   
    
    ontologies_graph = add_data_to_graph(ONTOLOGIES_PATH,
        ONTOLOGY_EXTENSION, ONTOLOGY_FORMAT)
        
    for rdf_subject, rdf_predicate, rdf_object in rdf_graph:
        ontologies_graph.add((rdf_subject, rdf_predicate, rdf_object))

    ontologies_graph.serialize(ONTOLOGIES_PATH + chosen_model+"/"+ REGISTER_ONTOLOGY, 
        format= ONTOLOGY_FORMAT)
```
## Extraction of the standard data tables
To extract the standard data, the following steps must be followed:

1. Uploading the Set of Ontologies to Jena Fuseki: The first step involves uploading a set of ontologies into Jena Fuseki (a popular open-source SPARQL server). 

2. Executing SPARQL Queries Using the SPARQLWrapper Python Library: Once the ontologies are uploaded, query this data to extract the CDM tables using SPARQL. The code to perform these queries using python is located in the "Table_creation" folder

3. Post-Processing in Python to Adjust Tables to the specific CDM (for example, OMOP) and extract data as CSV: After retrieving the necessary information from the ontologies, the post-processing is performed. This involves transforming the query results into a format that aligns with that of the CDM. Finally, CDM data tables are extracted in CSV format and ready to be loaded into a DBMS or directly used for analysis.

# Dockerization of OntoBridge
To make it easier for any user who requires OntoBridge to use it, regardless of their previous knowledge of the more technical aspects of the tool and the operating system they use, we decided to dockerize the entire process to make it easier to use.

Next, we will explain step by step how you can use OntoBridge to standardize your local database to the standard you want (i2b2, OMOP, iso13606).

## Previous stetps
Previous using the OntoBridge Docker, you will have to to build the local ontology that represents the database you will use. This step is explained in detail in the "Ontologies" section. Once you have the ontology created, insert it into the data/Ontologies/model directory to which you want to transform the data. Additionally, you must ensure that both the local clinical data and the dictionaries are stored in a database that allows queries to be made. We recommend using MySQL as the database management system (DBMS), since it is the one we have used throughout the process. If you need to use another DBMS, you will need to modify the content of the Ontop jdbc folder, as it contains the drivers to connect to MySQL.

# Run the docker
The first step is to download this GitHub repository, which contains everything you need to use OntoBridge. Once downloaded, navigate to the "ontobridge" directory in the terminal, where the "docker-compose.yaml" file is located. In this directory, run the command docker-compose up -d. This command will start the Docker container and proceed to install its image so that it can be used. If you examine the Dockerfile that builds the image, you'll see that it installs Ubuntu 22.04 and Python along with the necessary libraries. Finally, it runs the main.py file, which manages the entire operation of the Docker container.

```dockerfile
FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y python3.11 python3-pip openjdk-11-jdk && \
    apt-get install bash-completion && \
    apt-get install -y python3-pip

WORKDIR /app

COPY requirements.txt .

RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "main.py"]
```

## SQL-to-RDF Data Extraction and Transformation ##

Once the Docker container is up and running, navigate to localhost and the specific port where you have assigned OntoBridge to connect. This will open an interface identical to the one shown in the following image:

Once inside the interface, go to the "SQL Database Connection Parameters" section and enter your local database connection parameters. An example of these parameters would be:

JDBC Name: Local_database
JDBC URL: jdbc:mysql://[ip]:[port]/Local_database
JDBC User: User
JDBC Password: password

After entering the parameters, click "Submit." This will create the necessary Properties file to connect to your database using a Python script (you can check that it has been generated inside the data directory), and it will execute the ontop_materialize.sh script, which will generate the RDF with the data. Currently, the OntoBridge Docker container is designed to extract only local clinical data and not the elements necessary for dictionaries, as this has been done separately using Ontop manually. However, in the future, a method for performing these other extractions will be included in the interface.

## CDM Table Creation ##

Once you have generated the RDF with the data, choose the standard model you want to transform and click "create model tables". When you click the button, the data will be automatically inserted into the relevant ontological system and then the ontologies will be uploaded to the Fuseki endpoint and thus, also automatically, the SPARQL queries of the chosen model will be applied and thus, finally, the resulting tables will be obtained inside the data directory.

![interface](/images/interface.png)
interface.png