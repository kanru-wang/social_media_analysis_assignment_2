import networkx as nx

G = nx.read_graphml('all_nodes.graphml')
UG = G.to_undirected()

print(nx.node_connectivity(UG))
print(nx.minimum_node_cut(UG))
print(nx.edge_connectivity(UG))
print(nx.minimum_edge_cut(UG))