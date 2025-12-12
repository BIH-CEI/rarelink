#!/bin/bash
docker-compose -f src/rarelink/tofhir/docker-compose.yml --project-directory ./ -p tofhir-redcap down
