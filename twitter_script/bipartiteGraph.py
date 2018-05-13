import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt

B = nx.Graph() # No separate class for bipartite graphs
B.add_nodes_from(['A', 'B', 'C', 'D', 'E'], bipartite=0)
B.add_nodes_from([1, 2, 3, 4], bipartite=1)
B.add_edges_from([('A', 1), ('B', 1), ('C', 1), ('C', 3), ('D', 2), ('E', 3), ('E', 4)])
print(bipartite.is_bipartite(B))
nx.draw_networkx(B)
plt.show()

X = set([1,2,3,4])
print(bipartite.is_bipartite_node_set(B, X))