# What is Colony?

Colony is a simple DNS-based service discovery for stand-alone Docker
hosts. It is aiming to provide a low-touch method that doesn't require
modifying your applications to enable service discovery.

The Colony Agent listens to the Docker events API for container start and
stop events, and then registers or unregisters the DNS records on the
Colony Registry based on the container name and labels. The Colony
Registry provides a DNS service for resolution. By running the Agent on
multiple docker hosts, cluster-wide service discovery is achieved.

For stand-alone docker hosts, a local service proxy is recommended:

- [jwilder/nginx](https://github.com/nginx-proxy/nginx-proxy)
- [wemake-services/caddy-gen](https://github.com/wemake-services/caddy-gen)

Using a service proxy means that you can route the traffic from a
consistent port (e.g. `80`) to the individual local service containers.
The individual containers don't need to expose any ports in this case.