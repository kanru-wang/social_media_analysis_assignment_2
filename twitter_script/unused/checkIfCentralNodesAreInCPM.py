"""
COSC2671: Assignment 2, 2018
@author a small world
@description To check if the starting nodes and most central nodes are included
             in detected CPM and Louvain communities

"""

import json
import glob
import os
import networkx as nx
import utilities as ux

cwd = os.getcwd()

# Check if the top most central nodes are included in k-CPM communities
# Read the starting modes and most central nodes by degrees & eigenvector

with open('top_degree_centrality.json', 'r') as fp:
	d1 = json.load(fp)

with open('eigen_centrality.json', 'r') as fp:
	d2 = json.load(fp)

# To define starting nodes/obtain the most central nodes in lists
d0 = ['RProgramming', 'pydatasci', 'DataCamp', 'R_programming', 'rstudio', 'pycharm', 'kaggle']
d1 = list(d1)
d2 = list(d2)

# To obtain the nodes from the detected k-CPM communities
for k in range(3, 6):
	file_name = '/community_' + str(k) + '*.graphml'
	graphml = glob.glob(cwd+file_name)
	n = len(graphml)
	print('You have {} {}-clique communities....\n'.format(n, k))

	for i in range(0, n):
		G = nx.read_graphml(graphml[i])

		print('Returning which starting nodes are included in {}-clique community {}\n'.format(k, i+1))
		ux.check_nodes_included(d0, G)

		print('Returning which most central nodes (by degreeness) are included in {}-clique community {}\n'.format(k, i+1))
		ux.check_nodes_included(d1, G)

		print('Returning which most central nodes (by eigenvector) are included in {}-clique community {}\n'.format(k, i+1))
		ux.check_nodes_included(d2, G)