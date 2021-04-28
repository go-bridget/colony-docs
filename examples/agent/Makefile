.PHONY: all up down restart logs meta

export DOCKER_GID=$(shell stat -c "%g" /var/run/docker.sock)

all: meta up

up:
	@docker-compose up -d --remove-orphans

down:
	@docker-compose down --remove-orphans

pull:
	@docker-compose pull

restart:
	@docker-compose restart

logs:
	@docker-compose logs -f

meta:
	@echo -n
