# Configuration

The Colony Registry supports configuration via flags and environment variables.

~~~
# ./registry-linux-amd64 --help
Usage: registry (command) [--flags]

   start    Start colony registry service

      --dns-addr string     DNS listen address (default ":5353")
      --http-addr string    HTTP API listen address (default ":3000")
      --pprof-addr string   pprof listen address (default ":6060")
      --zone string         DNS zone for service discovery (default ".service")

pflag: help requested
~~~

The Registry can be configured using the following environment variables:

- `DNS_ADDR` (default `:5353`)
- `HTTP_ADDR` (default `:3000`)
- `PPROF_ADDR` (default `:6060`, set to `0`, `false` or `off` to disable)
- `ZONE` (default: `.service`)

Adjust your `docker-compose.yml` according to your needs.
