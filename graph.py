#Undirected graph
import networkx as nx
G = nx.Graph()
G.add_node(1)
G.add_edge(2,3)
#G.add_edge(3,2)
print G.nodes()
print G.edges()
print G.number_of_edges()