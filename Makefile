.PHONY: all up down restart logs meta deploy

all: meta up

deploy:
	@docker-compose exec --env SSH_AUTH_SOCK=${SSH_AUTH_SOCK} mkdocs mkdocs gh-deploy

up:
	@docker-compose up -d --remove-orphans

build:
	@docker-compose build

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
