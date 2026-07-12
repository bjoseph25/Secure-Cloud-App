#!/bin/bash

mkdir -p app/{api,core,db,models,schemas,services,auth}
mkdir -p tests
mkdir -p alembic
mkdir -p docker
mkdir -p nginx
mkdir -p scripts
mkdir -p .github/workflows

touch app/main.py
touch Dockerfile
touch docker-compose.yml
touch requirements.txt

echo "✅ Secure Cloud App project structure created!"
