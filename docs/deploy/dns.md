# DNS

Each Colony Registry server listens on udp `:5353` by default for DNS
requests. Requests not in the defined service zone will result in a
`NXDOMAIN` (Non-existent domain).

> *Notice*: The Colony Registry server doesn't perform DNS forwarding.

You can use the following script to query multiple domains using `dig`,
adjusting the hosts and destination port and hostname as deployed.

```bash
#!/bin/bash
NAMES="colony-agent colony-registry nginx-proxy"
for NAME in $NAMES; do
        dig -p 53530 $NAME.service @localhost | egrep -v '^(;|$)'
done
```

The above gives the following output:

```perl
colony-agent.service.	 3600	IN	A	172.24.0.2
colony-registry.service. 3600	IN	A	172.24.0.2
nginx-proxy.service.	 3600	IN	A	172.24.0.2
```