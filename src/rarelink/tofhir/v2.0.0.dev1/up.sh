#!/bin/bash
docker-compose -f src/rarelink/tofhir/v2.0.0.dev1/docker-compose.yml --project-directory ./ -p tofhir-redcap up -d
