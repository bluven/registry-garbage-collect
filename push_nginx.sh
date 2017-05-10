#!/bin/sh

docker pull nginx:1.9
docker tag nginx:1.9 localhost:5000/lib/nginx:1.9
docker push localhost:5000/lib/nginx:1.9
