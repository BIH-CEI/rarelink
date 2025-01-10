Generate FHIR Resources
=======================

.. attention::
    This section is still to be implemented in the documentation and the RareLink
    command-line interface.

Via the RareLink CLI type:

.. code-block:: bash

    rarelink setup -pipeline toFHIR
    rarelink pipeline -run toFHIR

The FHIR module in RareLink allows users to generate FHIR resources from REDCap data.

---

ToFHIR Pipeline Setup
======================

To set up the ToFHIR pipeline for the RareLink framework, use the following command:

.. code-block:: bash

    rarelink fhir setup

This command ensures all configurations are validated and helps users prepare the ToFHIR pipeline for FHIR resource generation.

.. _4_4:

Steps for `rarelink fhir setup`
-------------------------------

1. **Validate API Keys and Configurations**:
   The setup process validates the following configurations:

   - BIOPORTAL_API_TOKEN
   - REDCAP_PROJECT_URL
   - REDCAP_PROJECT_ID
   - REDCAP_API_TOKEN

   If these are not set up correctly, the setup will prompt you to configure them.

.. note::
    Run the command ``rarelink setup api-keys`` if any configurations are missing or incorrect.

2. **FHIR Server Configuration**:
   - If you have a FHIR server, provide the URL when prompted (e.g., `http://100.11.000.111:0000/fhir`).
   - The configuration will be saved to `rarelink_fhirconfig.json`.

   .. tip::
      If you don’t have a FHIR server, consult the RareLink documentation for guidance on setting one up.

3. **Docker and Colima Setup**:
   - Ensure Docker and Colima are installed.
   - The setup will verify Colima is running. If not, it will prompt to install and start Colima via Homebrew.

   .. attention::
      Colima is essential for managing the ToFHIR pipeline. Installation is mandatory to proceed.

4. **Next Steps**:
   - Once setup is complete, run additional commands such as:

     .. code-block:: bash

         rarelink fhir export

   - Refer to the documentation for advanced usage and examples.

---

What Users Need to Set Up RareLink CLI in the Environment
=========================================================

.. note::
    The following components and configurations are required to set up and use the RareLink CLI:

1. **System Requirements**:
   - Docker and Docker Compose installed on the system.
   - Colima installed and running.

2. **Environment Variables**:
   - Set up the `.env` file with the following:
     - `BIOPORTAL_API_TOKEN`
     - `REDCAP_PROJECT_URL`
     - `REDCAP_PROJECT_ID`
     - `REDCAP_API_TOKEN`

3. **Configuration Files**:
   - `docker-compose.yml`: Includes services and volumes.
   - `rarelink_apiconfig.json`: Contains REDCap project configurations.
   - `tofhir-redcap-application.conf`: Configures the ToFHIR-Redcap integration.

4. **Scripts**:
   - Use `up.sh` and `down.sh` scripts to start and stop services.

5. **Testing**:
   - Validate the setup with `docker logs` and test REDCap integration by setting up the Data Entry Trigger URL in the REDCap project.

---

Additional Docker Configuration Help
====================================

1. **Quitting and Restarting Docker Containers**:

   .. code-block:: bash

       # Stop all running containers
       docker stop $(docker ps -q)

       # Remove all stopped containers
       docker rm $(docker ps -aq)

       # Restart containers using docker-compose
       docker-compose down
       docker-compose up -d

2. **Inspecting Containers**:
   - Access a container to check configurations:

     .. code-block:: bash

         docker exec -it <container_name> /bin/bash

   - List environment variables inside a container:

     .. code-block:: bash

         docker exec -it <container_name> printenv

3. **Copying Files from a Container**:
   - To inspect configuration files:

     .. code-block:: bash

         docker cp <container_name>:/path/to/file /local/destination

4. **Viewing Logs**:
   - Check logs for troubleshooting:

     .. code-block:: bash

         docker logs <container_name>

5. **Health Check**:
   - Verify container health status:

     .. code-block:: bash

         docker ps -a

---

.. tip::
    For detailed troubleshooting steps, refer to the RareLink documentation or contact support.
