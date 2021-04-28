# Configuration

The Colony Agent supports configuration via flags and environment variables.

~~~
# ./agent-linux-amd64 --help
Usage: colony-agent (command) [--flags]

   start    Start colony agent service

      --pprof-addr string        pprof listen address (default ":6060")
      --registry host:port,...   Registry HTTP RPC endpoints (CSV, host:port,...)

pflag: help requested
~~~

The Agent can be configured using the following environment variables:

- `REGISTRY` (e.g. `host1:3000,host2:3000`)
- `PPROF_ADDR` (default `:6060`, set to `0`, `false` or `off` to disable)

Adjust your `docker-compose.yml` according to your needs.
