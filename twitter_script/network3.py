import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

G_mat = np.array([[0, 1, 1, 1, 0, 1, 0, 0, 0, 0],
				  [1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
				  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				  [1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
				  [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
				  [1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
				  [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
				  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
				  [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
				  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]])

G = nx.DiGraph(G_mat)
print(G.edges())
print(G.degree())
nx.draw_networkx(G, label=True)
plt.show()