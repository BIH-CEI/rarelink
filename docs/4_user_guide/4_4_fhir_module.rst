.. _4_4:

FHIR Module
=============

The RareLink FHIR module implements the `open-source toFHIR engine <https://github.com/srdc/tofhir>`_ 
which converts all data from the :ref:`2_2` into FHIR resources. This section details the commands available in the RareLink CLI to manage the
FHIR module and associated pipelines.

.. attention:: 
   - Please ensure you are **authorized to export (real-world) data** to
     the configured FHIR server. This includes verifying compliance with
     the ethical agreement and data protection regulations of your study 
     or registry
   - Be aware of your projects **development and production mode**. Read the
     :ref:`1_6` section and discuss this with your FHIR server administrator!

_____________________________________________________________________________________  

**Overview**

- :ref:`get_started`
- :ref:`fhir_profiles`
- :ref:`cli_fhir_commands`
   - :ref:`setup_command`
   - :ref:`hapi_server_command`
   - :ref:`export_command`
   - :ref:`restart_docker_command`
   - :ref:`docker_commands`
- :ref:`cdis-module`

_____________________________________________________________________________________

.. _get_started:

Geting started
---------------

To use these functionalities, you need a running REDCap project with API access 
and the RareLink-CDM instruments. You also need the framework and all its
components running. You can run the following commands to set everything up: 

- ``rarelink framework update`` to update the framework and all components.
- ``rarelink setup redcap-project`` to set up a REDCap project with your REDCap 
  administrator. 
- ``rarelink setup keys`` to set up the REDCap API access locally.

_____________________________________________________________________________________

.. _fhir_profiles:

RareLink-CDM FHIR Profiles
---------------------------

These FHIR resources generated are based on the HL7 FHIR `International Patient Summary (IPS) <https://www.hl7.org/fhir/ips.html>`_
and `Genomoics Reporting <https://hl7.org/fhir/uv/genomics-reporting/STU3/index.html>`_ 
profiles. The :ref:`2_2` FHIR profiles include these dependencies to generate
the FHIR resources that are compliant with the IPS and the GenomicsReporting 
profiles. For more information on FHIR, please read the background section
:ref:`1_4`.

.. hint::
   You can check out the :ref:`2_2` FHIR Profiles in **draft** `here <https://github.com/BIH-CEI/rarelink/tree/develop/src/fsh/input/fsh>`_ 

_____________________________________________________________________________________

.. _cli_fhir_commands:

RareLink-CLI FHIR Commands
--------------------------

.. _setup_command:

1. Setup Command
___________________

.. code-block:: bash

   rarelink fhir setup

**What it does**:

- Configures the `toFHIR` pipeline for RareLink.
- Validates required setup files (`.env`, `redcap-projects.json`).
- Prompts for the FHIR server URL and saves it to `.env`.

**Requirements**:
 
- Docker and Docker Compose must be installed.
- A FHIR server must be accessible or created locally using ``rarelink fhir hapi-server``.

**Steps**:

1. Ensure the `.env` file exists and contains:

.. code:: bash
    
   BIOPORTAL_API_TOKEN:<your_bioportal_api_token>
   REDCAP_URL:<your_redcap_url>
   REDCAP_PROJECT_ID:<your_redcap_project_id>
   REDCAP_API_TOKEN:<your_redcap_api_token>

... otherwise run ``rarelink setup keys`` to set them up.

2. Run the command and provide the FHIR server URL.
3. Confirm Docker is installed, or follow prompts to install it.

_____________________________________________________________________________________

.. _hapi_server_command:

2. HAPI Server Command
________________________

.. code-block:: bash

   rarelink fhir hapi-server

**What it does**:

- Sets up a local HAPI FHIR server using Docker.
- Creates a Docker network (`shared-network`) if not present.
- Runs the HAPI FHIR server container.

**Requirements**:

- Docker must be installed.

**Steps**:

1. Run the command.
2. If the server container already exists, it restarts it.
3. Access the server at `http://localhost:8080`.

**Hints**:

- Data is stored in the Docker container. Avoid removing it to preserve data.
- Use this command if no external FHIR server is available.


_____________________________________________________________________________________

.. _export_command:

3. Export Command
_____________________

.. code-block:: bash

   rarelink fhir export

**What it does**:

- Exports data from REDCap to the configured FHIR server.
- Validates `.env` and `redcap-projects.json` files.
- Runs the ToFHIR pipeline using Docker Compose.

**Requirements**:

- `.env` and `redcap-projects.json` must be valid.
- Docker and Docker Compose must be installed.

**Steps**:

1. Validate setup files using ``rarelink fhir setup``.
2. Ensure the ethical agreement for exporting data is fulfilled.
3. Run the command to start the ToFHIR pipeline.

**Logs**:

- Use ``docker logs -f tofhir`` to monitor the export process in real time.

_____________________________________________________________________________________

.. _restart_docker_command:

4. Restart Docker Command
____________________________

.. code-block:: bash

   rarelink fhir restart-dockers

**What it does**:

- Stops all running Docker containers.
- Removes stopped containers.
- Restarts the necessary containers using `docker-compose`.

**Steps**:

1. Run the command.
2. Monitor logs if needed (e.g., `docker logs -f <container>`).

_____________________________________________________________________________________

.. _docker_commands:

Docker Commandsss
----------------

These commands help manage Docker containers used in the RareLink framework.

- **Stop All Containers**:

   .. code-block:: bash

      docker stop $(docker ps -q)

- **Remove Stopped Containers**:

   .. code-block:: bash

      docker rm $(docker ps -aq)

- **Restart Containers with Docker Compose**:

   .. code-block:: bash

      docker-compose down
      docker-compose up -d

- **Inspect a Running Container**:

   .. code-block:: bash

      docker exec -it <container_name> /bin/bash

- **View Logs**:

   .. code-block:: bash

      docker logs -f <container_name>

   For example:

   .. code-block:: bash

      docker logs -f tofhir

   This shows real-time logs for the `tofhir` export process.

- **Copy Files from a Container**:

   .. code-block:: bash

      docker cp <container_name>:/path/to/file /local/destination

_____________________________________________________________________________________

_____________________________________________________________________________________

.. _cdis-module:

Importing FHIR to REDCap
--------------------------

**Clinical Data Interoperability Services (CDIS)** is a module in REDCap that 
lets your project pull clinical data from an external electronic health record 
(EHR) system. With CDIS, you can use standard FHIR APIs or custom web services 
to import data into your REDCap project. This guide is intended to help users 
understand how to implement and use the CDIS modules for RareLink and the 
:ref:`2_2`.  

.. note::
   The CDIS modules can only be enabled by a REDCap administrator. If you need
   access to these modules, please contact your REDCap administrator.
   
.. hint:: 
   For more information please read:

   - CDIS REDCap: https://projectredcap.org/software/cdis/
   - CDIS Paper: https://doi.org/10.1016/j.jbi.2021.103871

CDIS is divided into three modules:
 
- **Clinical Data Pull (CDP)**
- **Clinical Data Mart (CDM)**
- **Dynamic Data Pull (DDP)**

Each module has its own process for mapping data from the EHR to your REDCap 
forms. This guide explains how to use each module and shows where to add your 
model-specific mapping details.

_____________________________________________________________________________________

Modules Overview
__________________

Clinical Data Pull (CDP)
"""""""""""""""""""""""""

The CDP module is used for importing clinical data for one patient at a time.
It requires you to:

1. **Create REDCap Instruments:**  

   :ref:`3_3`, i.e. the corresponding REDCap forms you want to use from the 
   :ref:`2_2` before using CDP. 
   
   - If you developed your own forms, ensure they to use the 
     :ref:`fhir_profiles` for its core and develop extensional forms
     using the :ref:`4_5` guide.
   
_____


2. **Field Mappings:**  

   After creating your forms, navigate to the CDP Mapping page. Here, you map 
   fixed EHR source fields to the fields in your REDCap forms. 

   - **REDCap Field**: this column lists the variables in your REDCap forms
   - **External Source Field**: this column lists the available source fields 
     in the EHR
   - **Date/Time**: The date field which is associated with the temporal fields.
     It is disabled by default, and it will be enabled if you select a temporal 
     field from External Source Field list.
   - **Preselect Strategy**: this column indicates how the data is fetched
   
.. note:: 
   The mapping is mandatory for the patient identifier 
   (e.g., Medical Record Number) which corresponds to element 1.1 in the
   :ref:`2_2`. The rest of the fields are optional.

.. hint:: 
   Check out either the :ref:`cdm_overview` or the :ref:`rarelink_cdm_linkml`  
   sections in our docs to find all the field variables and forms of the 
   :ref:`2_2`.


A sample mapping table with values from the :ref:`2_2` might look like:

.. code-block:: rst

   +---------------------------+----------------------+---------------------+------------------------+
   | **External Source Field** | **REDCap Field**     | **Date/Time Field** | **Preselect Strategy** |
   +===========================+======================+=====================+========================+
   | MedicalRecordNumber       | snomedct_422549004   |                     | N/A                    |
   +---------------------------+----------------------+---------------------+------------------------+
   | DOB                       | snomedct_399423000   |                     | Latest Value           |
   +---------------------------+----------------------+---------------------+------------------------+
   | Glucose [Presence]        | ncit_c60819          | ncit_c82577         | Nearest Timestamp      |
   +---------------------------+----------------------+---------------------+------------------------+


*In this example, these RareLink-CDM elements in REDCap are mapped to
the corresponding EHR source field names:*

- **1.1 Pseudnoym** ``snomedct_42254900`` *corresponds to* ``MedicalRecordNumber`` in the EHR system.
- **1.2 Date of Birth** ``snomedct_399423000`` *corresponds to* ``DOB`` in the EHR system.
- **6.3.1 Assay** ``ncit_c60819`` & **6.3.5 Time Observed** ``ncit_c82577``
  *correspond to*  ``Glucose [Presence]`` in the EHR system.

_____


3. **Adjudication:**  
   Adjudication refers to the process in which EHR data is manually reviewed 
   and approved by a user before it is officially saved and stored in the REDCap
   project. Once mapping is complete, users review and approve (adjudicate) 
   the data fetched from the EHR before it is saved into the REDCap project. 
   This helps ensure data accuracy.

.. hint:: 
   You can find more information on the **adjudication process** with pictures in
   the *2.6 Data adjudication in CDP* Methods section of the `paper by Cheng A.C., et al. <https://www.sciencedirect.com/science/article/pii/S1532046421002008>`_.

_____

Clinical Data Mart (CDM)
"""""""""""""""""""""""""""

The CDM module enables bulk import of EHR data into REDCap. It is set up
during project creation, and a REDCap administrator must be involved to
enable and configure this feature.

*Steps:*

1. **Project Creation:**  
   Select the "Clinical Data Mart" option on the project creation page.
   (Note: REDCap administrator approval is required.)

2. **Automatic Instrument Creation:**  
   REDCap auto-generates instruments for each selected source field 
   category (e.g., Demography, Labs, Condition).

3. **Optional Filters:**  

   - **Time Range:** Set a date filter to limit data (e.g., for lab results).  
   - **Patient ID:** Optionally, specify patient identifiers (MRNs) to fetch data 
     for specific patients.

4. **RareLink-CDM Mapping Configuration:** please see the information above for
   the step *2. Field Mappings* in the CDP module section on how to develop 
   your specific mapping table.

After setup, use the ``Fetch all records`` button on the Clinical Data Mart page
to retrieve and populate the instruments with EHR data.

.. hint:: 
   You can find more information on the **Clinical Data Mart** in the *2.2. Defining
   initial use cases and operational data flow requirements* Methods section of 
   the `paper by Cheng A.C., et al. <https://www.sciencedirect.com/science/article/pii/S1532046421002008>`_.

_____

Dynamic Data Pull (DDP)
"""""""""""""""""""""""""""
The DDP module is used when the list of source fields may change over time.
Unlike CDP, which uses a fixed field list from the EHR's FHIR API, DDP uses
web services to dynamically retrieve fields and data.

1. **Metadata Web Service:**  
   Retrieves a dynamic list of available source fields.

2. **Data Web Service:**  
   Fetches the actual patient data from the external system.

Before enabling DDP, a REDCap administrator must implement and configure these 
web services (set the metadata and data web service URLs) as described in the 
official documentation. Once configured, DDP follows a similar flow to CDP:
create your REDCap forms, set up field mappings, and adjudicate the fetched data.

**RareLink-DDP Mapping Configuration:**  
please see the information above for
the step *2. Field Mappings* in the CDP module section on how to develop your 
specific mapping table.

.. hint::
   You can find more information on the **Dynamic Data Pull** in the
   `paper by Campion Jr Thomas R, et al. <https://pmc.ncbi.nlm.nih.gov/articles/PMC5543341/>`_.

_____

Modules Comparison
____________________

Below is a summary comparison of the three CDIS modules:

+----------------------+---------------------------------------+---------------------------------------+----------------------------------------------------------+
| **Feature**          | **CDP**                               | **CDM**                               | **DDP**                                                  |
+======================+=======================================+=======================================+==========================================================+
| Data Mapping         | User-defined mappings per record      | Predefined instrument mappings        | Custom mapping via dynamic metadata                      |
+----------------------+---------------------------------------+---------------------------------------+----------------------------------------------------------+
| Activation Process   | REDCap admin must enable CDP          | User permission required              | REDCap admin must enable DDP                             |
+----------------------+---------------------------------------+---------------------------------------+----------------------------------------------------------+
| Data Pull Process    | Fetched during record creation        | Fetched in bulk upon user action      | Pulled from web service during record creation           |
+----------------------+---------------------------------------+---------------------------------------+----------------------------------------------------------+
| Adjudication         | Manual review before saving           | Manual review before saving           | Manual review before saving (post web service mapping)   |
+----------------------+---------------------------------------+---------------------------------------+----------------------------------------------------------+
| When to Use          | When custom mapping is needed         | When default mappings suffice         | When standard source fields are insufficient or when     |
|                      |                                       |                                       | dynamic mapping is required                              |
+----------------------+---------------------------------------+---------------------------------------+----------------------------------------------------------+



