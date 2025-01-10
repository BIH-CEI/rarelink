.. _4_4:

FHIR Module
================

.. attention::
    This section is still to be implemented in the documentation and the RareLink
    command-line interface.

Pre-setup
----------

1. **System Requirements**:
   - Docker and Docker Compose installed on the system.
   - Colima installed and running.

.. note::
   We recommend installing colima with brew (https://brew.sh/) and starting
   before running the setup command.

2. **Environment Variables**:
     - `BIOPORTAL_API_TOKEN`
     - `REDCAP_PROJECT_URL`
     - `REDCAP_PROJECT_ID`
     - `REDCAP_API_TOKEN`

Please make sure you have configured the API keys and REDCap details before 
running the ToFHIR pipeline. If you haven't done so, please run the following 
command:

.. code-block:: bash

    rarelink setup api-keys


ToFHIR Pipeline Setup
---------------------

To set up the ToFHIR pipeline for the RareLink framework, use the following command:

.. code-block:: bash

    rarelink fhir setup

This command ensures all configurations are validated and helps users prepare
the ToFHIR pipeline for FHIR resource generation.


Steps for `rarelink fhir setup`
-------------------------------

1. **Validate API Keys and Configurations** using `rarelink setup api-keys`.

2. **FHIR Server Configuration**:
   - If you have a FHIR server, provide the URL when prompted 
   (e.g., `http://100.11.000.111:0000/fhir`).
   - The configuration will be saved to `rarelink_fhirconfig.json`.

   .. tip::
      If you don’t have a FHIR server, you will be guided through the command 
      line to set up a local FHIR server using Docker.

3. **Docker and Colima Setup**:
   - Ensure Docker and Colima are installed.
   - The setup will verify Colima is running. If not, it will prompt to install
   and start Colima via Homebrew.

   .. attention::
      Colima is essential for managing the ToFHIR pipeline. Installation is 
      mandatory to proceed.

4. **Next Steps**:
   - Once setup is complete, run additional commands such as:

     .. code-block:: bash

         rarelink fhir export

   - Refer to the documentation for advanced usage and examples.

---

Overview Usage
----------------

- **Configuration Files**:
   - `docker-compose.yml`: Includes services and volumes.
   - `rarelink_apiconfig.json`: Contains REDCap project configurations.
   - `tofhir-redcap-application.conf`: Configures the ToFHIR-Redcap integration.

- **Scripts**:
   - Use `up.sh` and `down.sh` scripts to start and stop services.

- **Testing**:
   - Validate the setup with `docker logs` and test REDCap integration by 
   setting up the Data Entry Trigger URL in the REDCap project.

---

Additional Docker Configuration Help
------------------------------------

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
