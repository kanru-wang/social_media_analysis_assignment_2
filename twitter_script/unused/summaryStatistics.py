"""
COSC2671: Assignment 2, 2018
@author a small world
@description To read the final graphml file and compute & visualise the basic measures of a graph.
			 It also calculates the clustering coefficient of the initial (starting) ego-centric users

"""

import networkx as nx
import matplotlib.pyplot as plt


G = nx.read_graphml('all_nodes.graphml')
starting_users = ['pydatasci', 'RProgramming', 'DataCamp',
				  'R_programming', 'rstudio', 'pycharm',
				  'kaggle']
top_n = 20

def compute_centrality(g, centrality_type, n):

	if centrality_type == 'eigen':
		centrality = nx.eigenvector_centrality_numpy(g)
	elif centrality_type == 'degree':
		centrality = nx.degree_centrality(g)
	else:
		centrality = nx.katz_centrality_numpy(g)

	# Return the top 10 accounts by highest centrality
	ordered_accounts = tuple(centrality.items())
	ordered_accounts = sorted(ordered_accounts, reverse=True, key = lambda x: x[1])

	for item in ordered_accounts[0:n]:
		print('{}: {} centrality of {}'.format(centrality_type, item[0], item[1]))

	return centrality.values()

print('Obtaining {} most central nodes....'.format(top_n))
print('\n\tDegree centrality')
degree  = compute_centrality(G, 'degree', n=top_n)

print('\n\tEigenvector centrality')
eigen = compute_centrality(G, 'eigen', n=top_n)

# print('\n\tKatz centrality')
# katz  = compute_centrality(G, 'katz', n=top_n)

print('Visualising of degree distributions....')
plt.subplot(1,3,1)
plt.hist(list(eigen))
plt.xlabel('Eigenvector centrality')
plt.ylabel('Degree')

# plt.subplot(1,3,2)
# plt.hist(list(katz))
# plt.title('Degree')
# plt.xlabel('Katz centrality')

plt.subplot(1,3,3)
plt.hist(list(degree))
plt.xlabel('Degree centrality')

plt.show()

# Visualisation of in- and out degree distributions

if nx.is_directed(G):
	print('The graph is directed.')
	print(nx.in_degree_centrality(G))
	print(nx.out_degree_centrality(G))

# Global clustering coefficient or transitivity of a graph
# Remember to convert to undirected graph
print('\nClustering coefficients of Ego users')

# Getting average clustering for the starting users
starting_users_clustering = []
for users in starting_users:
	x = nx.clustering(G.to_undirected(), users)
	starting_users_clustering.append(x)
	print(x)

print('Average clustering for G is {}'.format(nx.average_clustering(G.to_undirected())))
print('\nTransitivity')
print(nx.transitivity(G.to_undirected()))


# Distances: short path between userName1 and userName2
# print(nx.shortest_path(G, userName1, userName2))
# print(nx.shortest_path_length(G, userName1, userName2))

# Diameter and eccentricity are applicable when the graph is strongly connected
# number of strongly/weakly connected components
if nx.is_strongly_connected(G):
	print('G is strongly connected')
	print(sorted(nx.strongly_connected_components(G)))
	print(nx.number_connected_components(G))
	print(nx.eccentricity(G)) # Eccentricity of a node: the largest distance between n and all other nodes.
	print(nx.diameter(G))     # Diameter: maximum distance between any pair of nodes

elif nx.is_weakly_connected(G):
	print('G is weakly connected')

# If the graph is weakly connected it only has one weakly connected component.

print('Closeness centrality')

# TODO: to visualise the closeness

# TODO: number of bridges
# TODO: robustness, Node connectivity
# TODO: Betweenness centraliy

# TODO: Compare centrality

