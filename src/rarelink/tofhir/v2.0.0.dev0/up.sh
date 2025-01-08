#!/bin/bash

docker-compose -f docker-compose.yml --project-directory ./ -p tofhir-redcap up -d

