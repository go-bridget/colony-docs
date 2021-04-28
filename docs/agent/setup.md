# Getting started

The supported way of setting up the Colony Agent is using [docker-compose](https://docs.docker.com/compose/).

Create the following `docker-compose.yml` file:

~~~yaml
version: '3.5'

services:
  colony-agent:
    hostname: colony-agent
    container_name: colony-agent
    image: gobridget/colony-agent:latest
    restart: always
    user: "65534:$DOCKER_GID"
    volumes:
      # needs socket to read events
      - /var/run/docker.sock:/var/run/docker.sock:ro
    environment:
    - REGISTRY=172.17.0.1:30000
~~~

You will need to declare `$DOCKER_GID` to match your `docker.sock` group.<br/>
Please see the [permissions](/agent/permissions/) section to continue.
