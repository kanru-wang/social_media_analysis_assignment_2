# @author: Yong Kai Wong, Chi Ting Low
# @description: to read and return the networks

# TODO: Automate the basic analysis such as summary statistics and measures
# TODO: Ddd system time to track run time

import networkx as nx
import matplotlib.pyplot as plt
import sys
import datetime

# TODO: Read all twitter and Linked-In graphml and connect directed graphs by a list/dictionary
# TODO: Read all reddit csv

G1 = nx.read_graphml('RProgramming_tweets.graphml')
G2 = nx.read_graphml('pydatasci_tweets.graphml')
G3 = nx.read_graphml('R_Programming_tweets.graphml')
G  = nx.compose(G1, G2)
G  = nx.compose(G3, G)

# egocentric users
userName1 = 'RProgramming'
userName2 = 'pydatasci'
userName3 = 'RProgramming_tweets.graphml'

# TODO: Sort the top followers by their follower counts
# TODO: Extract their followers from these top followers
# for item in G.nodes(data=True):
# 	print(item)

# for item in G.edges(data=True):
#	print(item)


# Define a function to compute centrality
# TODO: Extend to other centrality measures

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

print('\nDegree centrality')
degree  = compute_centrality(G, 'degree', n = 10)

print('Eigenvector centrality')
eigen = compute_centrality(G, 'eigen', n = 10)

print('\nKatz centrality')
katz  = compute_centrality(G, 'katz', n = 10)


# Visualisation of degree distributions
plt.subplot(1,3,1)
plt.hist(list(eigen))
plt.xlabel('Eigenvector centrality')
plt.ylabel('Degree')

plt.subplot(1,3,2)
plt.hist(list(katz))
plt.title('Degree')
plt.xlabel('Katz centrality')

plt.subplot(1,3,3)
plt.hist(list(degree))
plt.xlabel('Degree centrality')

plt.show()

# Visualisation of in- and out degree distributions


if nx.is_directed(G):
	print('graph is directed.')
	print(nx.in_degree_centrality(G))
	print(nx.out_degree_centrality(G))

# global clustering coefficient or transitivity of a graph
# Remember to convert to undirected graph
print('\nClustering coefficients of Ego users')
print('Clustering for {}: {}'.format(userName1, nx.clustering(G.to_undirected(), userName1)))
print('Average clustering for G is {}'.format(nx.average_clustering(G.to_undirected())))
print('\nTransitivity')
print(nx.transitivity(G.to_undirected()))


# Distances: short path between userName1 and userName2
# TODO: to extend to multiple egousers and central nodes based on Eigenvector and Katz
# TODO: to evaluate which centrality measures
print(nx.shortest_path(G, userName1, userName2))
print(nx.shortest_path_length(G, userName1, userName2))

# Breadth-First Search
T = nx.bfs_tree(G, userName2)
print(T.edges())

print(nx.shortest_path_length(G, userName2))


# Diameter and eccentricity are applicable when the graph is strongly connected
# number of strongly/weakly connected components
if nx.is_strongly_connected(G):
	print('Hrap')
	print(sorted(nx.strongly_connected_components(G)))
	print(nx.eccentricity(G)) # Eccentricity of a node: the largest distance between n and all other nodes.
	print(nx.diameter(G))     # Diameter: maximum distance between any pair of nodes


elif nx.is_weakly_connected(G):
	print(sorted(nx.weakly_connected_components(G)))

print('Closeness centrality')

# TODO: to visualise the closeness
# Closeness Centrality assumes important nodes are close to other nodes.
print(nx.closeness_centrality(G, normalized = True))

# TODO: number of bridges
# TODO: robustness, Node connectivity
# TODO: Betweenness centraliy

# TODO: Compare centrality

