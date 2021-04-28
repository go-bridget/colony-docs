# Permissions

By default, the Docker image built drops all privileges to `nobody`,
`uid=65534(nobody)`, `gid=65534(nobody)`. This means, you will need to
adjust the permissions by declaring `DOCKER_GID` used in the Docker
Compose configuration.

To find out the `docker.sock` group ID on your system:

~~~
# stat -c "%g" /var/run/docker.sock
128
~~~

You can use this `Makefile` which does this for you (Linux only, For OSX
it should be `stat -f` instead of `stat -c`).

```Makefile
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
```

Put the `Makefile` in the same folder as `docker-compose.yml` and run
`make` to start the agent. Other container lifecycle commands include:

- `make up` - start the containers
- `make down` - stop the containers
- `make pull` - pull the latest version
- `make restart` - restart the containers
- `make logs` - view container logs
- `make meta` - helper to generate metadata like `.env` files

