from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.compute import Server
from diagrams.onprem.container import Docker
from diagrams.aws.compute import EKS, Lambda
from diagrams.aws.database import Redshift
from diagrams.aws.integration import SQS
from diagrams.aws.storage import S3
from diagrams.oci.connectivity import DNS
from diagrams.onprem.client import Client
from diagrams.onprem.network import Nginx
from diagrams.onprem.network import Bind9

graph_attr = {
  "pad": "0",
  "fontsize": "12",
  "labelfontsize": "10",
  "height": "200.0",
  "center": "false"
}

with Diagram("Event Flows - Service proxy", filename="service-proxy", show=False, graph_attr=graph_attr):
    with Cluster("Example deployment"):
        with Cluster("Colony Registry Cluster"):
            dns = DNS("registry1")
            dns2 = DNS("registry...")

        with Cluster("Docker Host ..."):
            i2 = Nginx("App proxy")

            with Cluster("Applications"):
                b1 = [Docker("www"), Docker("api"), Docker("mysql2")]

        with Cluster("Docker Host 1"):
            i1 = Nginx("App Proxy")

            with Cluster("Applications"):
                a1 = [Docker("www"), Docker("api"), Docker("mysql1")]


    i1 >> a1
    i2 >> b1
    dns >> Edge(label="DNS Response A host2 IP") >> i2
    dns >> Edge(label="DNS Response A host1 IP") >> i1