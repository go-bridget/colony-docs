.PHONY: all up down restart logs meta

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
