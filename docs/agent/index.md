# About

The Colony Agent is a service that provides:

- Reading container lifecycle events from `docker.sock` or remote API,
- Registering and Unregistering container names on the Colony Registry API
- A pprof endpoint on port 6060, enabled by default

In order to work, you will need to [adjust
permissions](/agent/permissions.md) of the container user group to enable
access to `docker.sock`, and Colony Registry endpoints need to be
[configured](/agent/config.md).

The Colony Agent needs to run on every host with running services. It
will broadcast container names and labels to configured registries. Upon
start-up, all running containers will be sent to the registries.