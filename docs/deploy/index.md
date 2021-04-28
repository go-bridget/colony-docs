# HTTP API

In addition to checking the log output of both the Agent and Registry, the Registry
allows you to query the registered service names via a HTTP request:

```bash
ENDPOINT=http://127.0.0.1:30000/twirp/registry.RegistryService/List
curl -s -XPOST -d"{}" -H "Content-type: application/json" | jq '.records | keys'
```

The `List` API call lists all the domains and the IPs they point to. Using
`jq '.records | keys'` we only display the domains for brevity:

```json
[
  "colony-agent.service.",
  "colony-docs_mkdocs_1.service.",
  "colony-registry.service.",
  "gotenberg.service.",
  "mkdocs.service.",
  "nginx-proxy.service.",
  "offers_gotenberg_1.service.",
  "sink.service.",
  "sink_sink_1.service."
]
```

The API is protobuf enabled, but the JSON transport is in use. The
protobuf definitions are located in
[repository/rpc/repository.proto](https://github.com/go-bridget/colony/blob/master/registry/rpc/registry.proto).
The API surface is minimal, but may be extended to add functionality.