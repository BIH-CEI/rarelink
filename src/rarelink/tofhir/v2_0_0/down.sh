#!/bin/bash
docker-compose -f src/rarelink/tofhir/v2_0_0/docker-compose.yml --project-directory ./ -p tofhir-redcap down
