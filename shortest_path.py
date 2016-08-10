#DFS  BFS and so on
import networkx as nx
G = nx.Graph()
G.add_edge(0,1)
G.add_edge(0,3)
G.add_edge(0,4)
G.add_edge(1,2)
G.add_edge(2,4)
path=nx.all_pairs_shortest_path(G)
print path[0][2]
print G.nodes()
print G.edges()
print G.number_of_edges()