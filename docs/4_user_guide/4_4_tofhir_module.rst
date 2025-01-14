.. _fhir_commands:

FHIR Commands
=============

This section details the commands available in the RareLink CLI to manage the
FHIR module and associated pipelines.

.. attention:: 
   - Please ensure you are authorized to export (real-world) data to
      the configured FHIR server. This includes verifying compliance with
      the ethical agreement and data protection regulations of your study 
      or registry
   - Be aware of your projects development and production mode. Read the
      :ref:`1_6` section and discuss this with your FHIR server administrator!

.. _setup_command:

1. Setup Command
----------------

.. code-block:: bash

   rarelink fhir setup

**What it does**:
- Configures the `toFHIR` pipeline for RareLink.
- Validates required setup files (`.env`, `redcap-projects.json`).
- Prompts for the FHIR server URL and saves it to `.env`.

**Requirements**:
- Docker and Docker Compose must be installed.
- A FHIR server must be accessible or created locally using `rarelink fhir hapi-server`.

**Steps**:
1. Ensure the `.env` file exists and contains:
   - `BIOPORTAL_API_TOKEN`
   - `REDCAP_URL`
   - `REDCAP_PROJECT_ID`
   - `REDCAP_API_TOKEN`
   ... otherwise run `rarelink setup keys` to set them up.
2. Run the command and provide the FHIR server URL.
3. Confirm Docker is installed, or follow prompts to install it.

---

.. _hapi_server_command:

2. HAPI Server Command
----------------------

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

---

.. _export_command:

3. Export Command
-----------------

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
1. Validate setup files using `rarelink fhir setup`.
2. Ensure the ethical agreement for exporting data is fulfilled.
3. Run the command to start the ToFHIR pipeline.

**Logs**:
- Use `docker logs -f tofhir` to monitor the export process in real time.

---

.. _restart_docker_command:

4. Restart Docker Command
-------------------------

.. code-block:: bash

   rarelink fhir restart-dockers

**What it does**:
- Stops all running Docker containers.
- Removes stopped containers.
- Restarts the necessary containers using `docker-compose`.

**Steps**:
1. Run the command.
2. Monitor logs if needed (e.g., `docker logs -f <container>`).

---

.. _docker_commands:

Docker Commands
===============

These commands help manage Docker containers used in the RareLink framework.

1. **Stop All Containers**:

   .. code-block:: bash

      docker stop $(docker ps -q)

2. **Remove Stopped Containers**:

   .. code-block:: bash

      docker rm $(docker ps -aq)

3. **Restart Containers with Docker Compose**:

   .. code-block:: bash

      docker-compose down
      docker-compose up -d

4. **Inspect a Running Container**:

   .. code-block:: bash

      docker exec -it <container_name> /bin/bash

5. **View Logs**:

   .. code-block:: bash

      docker logs -f <container_name>

   For example:

   .. code-block:: bash

      docker logs -f tofhir

   This shows real-time logs for the `tofhir` export process.

6. **Copy Files from a Container**:

   .. code-block:: bash

      docker cp <container_name>:/path/to/file /local/destination

---

**Tip**:
For detailed troubleshooting, refer to the RareLink documentation or :ref:`12` 
us.
