#!/bin/sh 

curl -v --header "Accept:application/vnd.docker.distribution.manifest.v2+json" http://localhost:5000/v2/lib/nginx/manifests/1.9
