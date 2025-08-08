#!/bin/bash
docker-compose -f src/rarelink/tofhir/v2_0_2/docker-compose.yml --project-directory ./ -p tofhir-redcap up -d
