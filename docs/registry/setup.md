# Getting started

The supported way of setting up the Colony Registry is using [docker-compose](https://docs.docker.com/compose/).

Create the following `docker-compose.yml` file:

~~~yaml
version: '3.5'

services:
  colony-registry:
    network_mode: host
    hostname: colony-registry
    container_name: colony-registry
    image: gobridget/colony-registry:latest
    restart: always
~~~

Start up the Colony Registry with `docker-compose up -d`.
