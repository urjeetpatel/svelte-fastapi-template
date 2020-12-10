#! /usr/bin/env sh

# Exit in case of error
set -e
INSTALL_DEV=true \
docker-compose config > docker-stack.yml

docker-compose -f docker-stack.yml build
docker-compose -f docker-stack.yml down -v --remove-orphans # Remove possibly previous broken stacks left hanging after an error
docker-compose -f docker-stack.yml up
#docker-compose -f docker-stack.yml exec -T backend bash -c pytest
docker-compose -f docker-stack.yml down -v --remove-orphans
