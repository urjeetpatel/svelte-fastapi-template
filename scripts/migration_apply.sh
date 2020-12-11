#! /usr/bin/env sh

# Exit in case of error
set -e
INSTALL_DEV=true \
docker-compose config > docker-stack.yml

#docker-compose -f docker-stack.yml build
docker-compose -f docker-stack.yml up -d db
#docker-compose -f docker-stack.yml exec -T backend bash -c pytest
docker-compose -f docker-stack.yml run -w /app/app -T backend alembic upgrade head
#docker-compose -f docker-stack.yml down -v --remove-orphans
