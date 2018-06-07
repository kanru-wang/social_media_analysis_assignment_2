import networkx as nx
import matplotlib.pyplot as plt

# Weighted Graph
G = nx.Graph()
G.add_node('A')
G.add_node('B')
G.add_node('C')

G.add_edge('A', 'B', sign='+')
G.add_edge('C', 'B', sign='-')

sign_labels = nx.get_node_attributes(G, 'sign')
print(sign_labels)

pos = nx.kamada_kawai_layout(G) # This is the graph layout algorithm

sign_labels = nx.get_node_attributes(G, 'sign')
nx.draw_networkx(G, pos, label=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=sign_labels)

plt.show()
