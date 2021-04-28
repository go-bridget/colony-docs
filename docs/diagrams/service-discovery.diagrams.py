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

with Diagram("Example Service Registration", filename="service-discovery", show=False, graph_attr=graph_attr):
    with Cluster("Example deployment"):
        with Cluster("Docker Hosts, Colony Agents"):
            other = [Docker("...")]
            master = Docker("host1")

        with Cluster("Colony Registries"):
            r2 = Server("...")
            r1 = Server("registry1")

    e = Edge(label="Service registration")

    master >> Edge(label="Service registration", labelfloat="false", label_scheme="0") >> r1
    master >> r2
    other[0] >> [r1, r2]
