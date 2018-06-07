"""
COSC2671: Assignment 2, 2018
@author a small world
@description To compute and export the basic measures of the final (stacked) graph.
The basic measures are exported in JSON files. The basic measures include:
1. Centrality measures such as top 20 most central nodes
2. Global Clustering, transitivity of the graph
3. Average Clustering of the most central nodes
4. Shortest path among the most central users and close centrality
5. Connectivity of the graph

"""

import networkx as nx
import json
import utilities as ut

G = nx.read_graphml('all_nodes.graphml')
top_n = 20

# 1. Saving and exporting the central measures
# Note: Not able to calculate Katz Centrality
print('Obtaining and saving {} most central nodes....'.format(top_n))

print('\nDegree centrality')
degree = ut.compute_centrality(G, 'degree', n=top_n)
with open('degree_centrality.json', 'w') as fp:
	json.dump(degree, fp)

print('\nEigenvector centrality')
eigen = ut.compute_centrality(G, 'eigen', n=top_n)
with open('eigen_centrality.json', 'w') as fp:
	json.dump(eigen, fp)

# 2. Global clustering, transitivity of the graph
print('\nCalculating and exporting global clustering and transitivity of the graph....')
global_clustering = {}
global_clustering['clustering'] = nx.average_clustering(G.to_undirected())
global_clustering['transitivity'] = nx.transitivity(G.to_undirected())
with open('global_clustering.json', 'w') as fp:
	json.dump(global_clustering, fp)

# 3. Average Clustering of the most central users
UG = G.to_undirected()

print('\nCalculating and exporting average clustering of most central users by degree....')
degree_central_users_clustering = {}
for users in list(degree.keys()) :
	degree_central_users_clustering[users] = nx.clustering(UG, users)

with open('degree_central_users_clustering.json', 'w') as fp:
	json.dump(degree_central_users_clustering, fp)


print('\nCalculating and exporting average clustering of most central users by eigenvector....')
eigen_central_users_clustering = {}
for users in list(eigen.keys()):
	eigen_central_users_clustering[users] = nx.clustering(UG, users)

with open('eigen_central_users_clustering.json', 'w') as fp:
	json.dump(eigen_central_users_clustering, fp)


# 4. Shortest path among the most central users and close centrality
print('Computing and exporting the shortest path length among most central nodes by degree...')
with open('shortest_path_length_degree.json', 'w') as fp:
	json.dump(ut.shortest_path_length(degree, G), fp)

with open('shortest_path_length_eigen.json', 'w') as fp:
	json.dump(ut.shortest_path_length(eigen, G), fp)


# 5. Connectivity of the graph
connectivity = {}
if nx.is_strongly_connected(G):
	connectivity['strongly_connected'] = True
	connectivity['average_shortest_path_length'] = nx.average_shortest_path_length(G)
	connectivity['number_connected_components'] = nx.number_connected_components(G)
	connectivity['eccentricity'] = nx.eccentricity(G)
	connectivity['diamater'] = nx.diameter(G)
	connectivity['connected_components'] = sorted(nx.strongly_connected_components(G))

	# Eccentricity of a node: the largest distance between n and all other nodes.
	# Diameter: maximum distance between any pair of nodes

elif nx.is_weakly_connected(G):
	print('G is weakly connected')
	connectivity['strongly_connected'] = False
	connectivity['average_shortest_path_length'] = nx.average_shortest_path_length(G)

with open('connectivity.json', 'w') as fp:
	json.dump(connectivity, fp)