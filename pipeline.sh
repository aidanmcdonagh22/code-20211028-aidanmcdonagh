#!/bin/bash

# Stop Running Container
docker container kill aidanmcdonagh

# Remove and Delete Old Containers
docker image prune --all --force && docker system prune --all --force

# Build Container
docker build -t aidanmcdonagh-image:latest .

# RUn Container
docker run -p 8000:80 -d --name aidanmcdonagh aidanmcdonagh-image

# Test Using Django Test
if docker exec aidanmcdonagh python manage.py test; then
    # Success: bundle code for deployment
    echo "Tests Successful, Code now bundling..."
    SECRET_KEY="$(< secret_key.txt)" python3 setup.py sdist
else
    # Failure: exit
    echo "Tests Failed, please fix. Code will not proceed to build stage"
fi