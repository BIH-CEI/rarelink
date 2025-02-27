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

.. _cdis-module:

Importing FHIR to REDCap
--------------------------

Clinical Data Interoperability Services (CDIS) is a feature in REDCap that 
lets your project pull clinical data from an external electronic health record 
(EHR) system. With CDIS, you can use standard FHIR APIs or custom web services 
to import data into your REDCap project. CDIS is divided into three modules:
 
- **Clinical Data Pull (CDP)**
- **Clinical Data Mart (CDM)**
- **Dynamic Data Pull (DDP)**

Each module has its own process for mapping data from the EHR to your REDCap 
forms. This guide explains how to use each module and shows where to add your 
model-specific mapping details.

Modules Overview
__________________

Clinical Data Pull (CDP)
"""""""""""""""""""""""""

The CDP module is used for importing clinical data for one patient at a time.
It requires you to:

1. **Create REDCap Instruments:**  
   Set up the necessary REDCap forms (e.g., *Patient*, *Condition*, and 
   *Lab Result*) before using CDP.

2. **Field Mappings:**  
   After creating your forms, navigate to the CDP Mapping page. Here, you map 
   fixed EHR source fields to the fields in your REDCap forms. The mapping is 
   mandatory for the patient identifier (e.g., Medical Record Number).

   A sample mapping table might look like:

   .. code-block:: rst

      +----------------------+-------------------------+------------------------+
      | **REDCap Field**     | **EHR Source Field**    | **Preselect Strategy** |
      +======================+=========================+========================+
      | Patient ID           | MedicalRecordNumber     | N/A                    |
      +----------------------+-------------------------+------------------------+
      | Date of Birth        | DOB                     | Latest Value           |
      +----------------------+-------------------------+------------------------+
      | Lab Result Value     | Glucose [Presence]      | Nearest Timestamp      |
      +----------------------+-------------------------+------------------------+

   **Mapping Configuration Placeholder:**  
   *[Insert your model-specific mapping details here. Replace the example above 
   with your project's defined mapping configuration.]*

3. **Adjudication:**  
   Once mapping is complete, users review and approve (adjudicate) the data 
   fetched from the EHR before it is saved into the REDCap project. This helps 
   ensure data accuracy.

Clinical Data Mart (CDM)
"""""""""""""""""""""""""""

The CDM module is designed for bulk data import. When creating a CDM project, 
you:

1. **Project Creation:**  
   Select the Clinical Data Mart option on the project creation page.

2. **Automatic Instrument Creation:**  
   REDCap automatically creates data collection instruments based on the 
   selected source fields (e.g., Demography, Labs, etc.).

3. **Optional Filters:**  
   Configure a time filter (to limit data by date range) and patient ID filters 
   (to target specific patients).

   **Mapping Configuration Placeholder:**  
   *[Add any model-specific mapping overrides or transformation rules here if the 
   default mappings need adjustment.]*

Dynamic Data Pull (DDP)
"""""""""""""""""""""""""""

The DDP module is for cases where the list of source fields may change over time. 
It uses two web services:

1. **Metadata Web Service:**  
   Retrieves a dynamic list of source fields.

2. **Data Web Service:**  
   Fetches the actual patient data from the source system.

After enabling DDP and setting up the web services, the process is similar to 
CDP: create your REDCap forms, set up field mappings, and then adjudicate the 
fetched data.

   **Mapping Configuration Placeholder:**  
   *[Insert your dynamic mapping logic here. Use your custom metadata and data 
   web services configuration and specify how dynamic fields are mapped to your 
   REDCap fields.]*

Modules Comparison
____________________

Below is a summary comparison of the three CDIS modules:

+----------------------------------------+-------------------------------------------+
| **Feature**                            | **CDP / CDM**                             |
+========================================+===========================================+
| Data Mapping                           | CDP: User-defined mappings per record     |
|                                        | CDM: Predefined instrument mappings       |
+----------------------------------------+-------------------------------------------+
| Activation Process                     | CDP: REDCap admin must enable CDP         |
|                                        | CDM: User permission required             |
+----------------------------------------+-------------------------------------------+
| Data Pull Process                      | CDP: Data fetched during record creation  |
|                                        | CDM: Data fetched in bulk upon user action|
+----------------------------------------+-------------------------------------------+
| Adjudication                           | Manual review before saving               |
+----------------------------------------+-------------------------------------------+
| When to Use                            | CDP: When custom mapping is needed        |
|                                        | CDM: When default mappings suffice        |
+----------------------------------------+-------------------------------------------+

+-------------------------------------------------------------------------+
| **Dynamic Data Pull (DDP)**                                             |
+-------------------------------------------------------------------------+
| - Uses dynamic web services for metadata and data                       |
| - Requires custom implementation for mapping                            |
| - Use when standard source fields are insufficient or your use case     |
|   requires additional, dynamically determined fields                    |
+-------------------------------------------------------------------------+

Final Notes
____________

This guide is intended to help users understand how to implement and use the 
CDIS modules. As your project evolves, update the mapping configurations and 
any transformation logic to align with your common data model.

If you have any questions or need further assistance, please refer to the 
additional documentation provided by REDCap or contact your project administrator.


