#!/bin/bash
docker exec -ti registrygarbagecollect_registry_1 ./bin/registry garbage-collect /etc/docker/registry/config.yml
