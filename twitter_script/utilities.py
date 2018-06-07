"""
COSC2671: Assignment 2, 2018
@author a small world
@description some user-defined utility functions to simplify the network analysis

"""

import networkx as nx
import sys
from community import community_louvain
from collections import Counter

def compute_centrality(g, centrality_type, n):

	"""
	To obtain the centrality measures of a graph

	@param g: a grapml file
	@param centrality_type: {Degree, Eigenvector, Katz} centrality measures
	@param n: number of top central nodes

	@return: a dictionary of top central nodes and a centrality

	"""


	if centrality_type == 'eigen':
		centrality = nx.eigenvector_centrality_numpy(g)
	elif centrality_type == 'degree':
		centrality = nx.degree_centrality(g)
	else:
		centrality = nx.katz_centrality_numpy(g)

	# Return the top n accounts by the highest centrality value
	ordered_accounts = tuple(centrality.items())
	ordered_accounts = sorted(ordered_accounts, reverse=True, key = lambda x: x[1])
	result = {}

	for item in ordered_accounts[0:n]:
		result[item[0]] = item[1]
		print('{}: {} centrality of {}'.format(centrality_type, item[0], item[1]))


	return result



def shortest_path_length(centrality, G):

	"""
	To return dictionary of shortest paths among the nodes
 	@param centrality: a dictionary which records the top n most central nodes
	@param G: a  graph file

	@return: a descending ordered dictionary of shortest paths among the nodes
	"""

	k = 0
	a = list(centrality.keys())
	shortest_path = {}
	for i in range(len(a)):
		for z, y in zip(a[i+1:], a):
			try:
				k += 1
				shortest_path[k] = z, y, nx.shortest_path_length(G, z, y)
			except nx.exception.NetworkXNoPath:
				print('no path between {} and {}.'.format(z, y))

	sorted(shortest_path.values())  # sorted from min to max shortest path value
	return shortest_path


def community_detection(k, G):

	""""
	To detect k-CPM or Louvain community and label each node with respective k
	if k = 0, it returns the Louvain labels

	@param k: clique size
	@param G: graph

	@return: G with the k-cpm or Louvain id
	"""

	try:
		# Obtain the number of nodes of G
		m = len(G)

		# Initialise the size of nodes which do not belong to any detected community
		n = m

		if k == 0:

			dLouvainComms = community_louvain.best_partition(nx.to_undirected(G))

			louvainCommNum = max([y for (x,y) in dLouvainComms.items()]) + 1
			print('Number of the Louvain Communities: {}'.format(louvainCommNum ))

			# louvain labels, stored in node attribute 'louvain'
			lLouvainComms = dictToSetFormat(dLouvainComms, louvainCommNum)

			# Obtain the percentage nodes in each detected community
			c = Counter(dLouvainComms.values())

			for i, j in c.items():
				print('\tLouvain community label {} has {} % of nodes'.format(i, round(j/m*100, 2)))
				n = n - j

			# To make sure it results in 09
			print('\t{} of total nodes are removed from the Louvain communities'.format(n))

			for clusId, lComms in enumerate(lLouvainComms):
				for nodeId in lComms:
					G.node[nodeId]['louvain'] = clusId
		else:

			# Get the k-clique community
			CpmComms = list(nx.algorithms.community.k_clique_communities(nx.to_undirected(G), k))

			print('Number of communities detected using {} clique size: {}'.format(k, len(CpmComms)))

			# Print out the percentage of nodes in each detected communities
			for i in range(0, len(CpmComms)):

				# Obtain the detected size of community
				size = len(CpmComms[i])
				n = n - size

				print('\t{}-clique community {} contains {} % of total nodes'.format(k, i+1, round(size/m*100, 2)))

			print('\t{} % of total nodes are removed from {}-clique communities'.format(round(n/m*100, 2), k))

			for clusId, lComms in enumerate(CpmComms):
				for nodeId in lComms:
					G.node[nodeId]['cpmClusId'+str(k)] = clusId

		return G

	except TypeError:
		sys.exit(1)


def dictToSetFormat(dComms, maxCommNum):
	"""
	Converts dictionary to set format (modified based on Jeffrey's Chan)

	@param dComms: dictionary of communities, in the form of {(node id : comm id)}
	@param maxCommNum: number of communities in the dictionary

	@return: list representation [set(node ids...), ...]
	"""
	lGroundTruth = [set() for x in range(maxCommNum)]
	for (name, clusId) in dComms.items():
		lGroundTruth[clusId].add(name)

	return lGroundTruth
