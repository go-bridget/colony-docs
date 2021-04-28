from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.compute import Server
from diagrams.onprem.container import Docker
from diagrams.aws.compute import EKS, Lambda
from diagrams.aws.database import Redshift
from diagrams.aws.integration import SQS
from diagrams.aws.storage import S3
from diagrams.oci.connectivity import DNS
from diagrams.onprem.client import Client

graph_attr = {
  "pad": "0",
  "fontsize": "10",
  "labelfontsize": "10",
  "height": "200.0",
  "center": "false"
}

with Diagram("Event Flows - DNS Service Discovery", filename="service-resolution", show=False, graph_attr=graph_attr):
    with Cluster("Example deployment"):
        with Cluster("Docker hosts, Applications"):
            c1 = [Docker("host1"), Docker("...")]

        with Cluster("Colony Registries"):
            r1 = Server("registry1")
            r2 = Server("...")

    e = Edge(label="DNS Query")

    c1[0] >> e >> r1
    c1[0] >> e >> r2
