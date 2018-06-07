"""
COSC2671: Assignment 2, 2018
@author a small world
@description To detect community using CPM and Louvain's method

"""

import networkx as nx
import random
import utilities as ut

random.seed(9001)
G = nx.read_graphml('all_nodes.graphml')

print('Number of nodes of the graph: {}'.format(len(G)))

# Note that community_detection(k = 0, G) returns the louvain's label id
G = ut.community_detection(0, G)

# k-CPM for k = 3, 4, 5
G = ut.community_detection(3, G)
G = ut.community_detection(4, G)
G = ut.community_detection(5, G)

nx.readwrite.write_graphml(G, 'G_with_communitie.graphml', infer_numeric_types=True)
