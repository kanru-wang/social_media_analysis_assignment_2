"""
COSC2671: Assignment 2, 2018
@author a small world
@description To read the final graphml file and compute & visualise the basic measures of a graph.
			 It also calculates the clustering coefficient of the initial (starting) ego-centric users

"""

import networkx as nx
import json



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
	result ={}

	for item in ordered_accounts[0:n]:
		result[item[0]] = item[1]
		print('{}: {} centrality of {}'.format(centrality_type, item[0], item[1]))

	return result, centrality.values()

print('Obtaining {} most central nodes....'.format(top_n))
print('\n\tDegree centrality')
degree = compute_centrality(G, 'degree', n=top_n)


with open('degree.json', 'w') as fp:
	json.dump(degree[0], fp)

with open('degree.json', 'r') as fp:
	degree = json.load(fp)

print(degree)


starting_users_clustering = {}
for users in starting_users:
	starting_users_clustering[users] = nx.clustering(G.to_undirected(), users)

with open('starting_users_clustering.json', 'w') as fp:
	json.dump(starting_users_clustering, fp)

with open('starting_users_clustering.json', 'r') as fp:
	starting_users_clustering = json.load(fp)

print(starting_users_clustering)