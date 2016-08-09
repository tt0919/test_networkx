#Undirected graph
import networkx as nx
G = nx.Graph()
G.add_weighted_edges_from([(0,1,3.0),(1,2,7.5)])
print G.nodes()
print G.edges()
print G.number_of_edges()
print G.get_edge_data(1,2)