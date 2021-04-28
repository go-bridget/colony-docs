# About

The Colony Registry is a service that provides:

- A HTTP API on port 3000
- A DNS responder on UDP port 5353
- A pprof endpoint on port 6060, enabled by default

Any Colony Registry installation should allow traffic on these two ports.

Since the Colony Registries don't communicate in a P2P/RAFT/consensus
fashion, we can tolerate an outage of N-1 nodes. If a Colony Registry
goes offline, it will receive the complete container lists from Agents
upon it's return. We recommend having at least 2 instances.

Recommended setup:

- Two Dedicated hosts for Colony Registry,
- No particular resource requirements (lowmem, lowdisk,...)

It is expected that the Colony Registry is set up on stand-alone docker
hosts with docker "host" networking, but port forwarding is functional as
well. In case of host networking, the DNS service will respond with the
shortest path. For example:

```
host1: [web.service, api.service, db.service]
host2: [web.service, api.service]
host3: [elk-apm.service]
host4: [elk-apm.service]
```

Example queries and responses:

```
host1: web.service => [host1]*
host2: elk-apm.service => [host3, host4]
host3: api.service => [host1, host2]
```

The shortest path example are queries from `host1` and `host2` for the
services that are running on both hosts. If the requested service lives
on the same host where the query is coming from, then Colony Registry
will resolve the DNS query onto the source host.

If Colony Registry is running on a bridge network with exposed ports, the
DNS query source IP will be the docker gateway, `docker0`, and not the
source IPs from the various hosts. This makes shortest path responses
only possible with the host network.

This is also why it's not possible to run the Colony Registry on shared
hosts, as the requests will come from the various LAN IPs on the Docker
networks. It's possible that this will be improved in the future, by
specifying the host IP on the Colony Agents.
