import networkx as nx
import matplotlib.pyplot as plt

# Undirected Graph
UG = nx.Graph()
UG.add_edges_from([(0, 1),
				   (0, 2),
				   (0, 3),
				   (0, 5),
				   (1, 3),
				   (1, 6)])
plt.subplot(121)
nx.draw_networkx(UG)

# Directed Graph
G = nx.DiGraph()
G.add_node('A', role='trader')
G.add_node('B', role='boss')
G.add_node('C', role='boss')
G.add_edge('A', 'B', weight=1, relation='supervisor')
G.add_edge('A', 'C', weight=2, relation='family')

plt.subplot(122)
pos = nx.kamada_kawai_layout(G) # This is the graph layout algorithm
weight_labels = nx.get_edge_attributes(G, 'weight')
rel_labels = nx.get_edge_attributes(G, 'relation')
nx.draw_networkx(G, pos, label=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=weight_labels)
nx.draw_networkx_edge_labels(G, pos, edge_labels=rel_labels)
plt.show()

print(G.edges(data=True))
print(nx.get_node_attributes(G,'role'))
print(G.nodes(data=True))


