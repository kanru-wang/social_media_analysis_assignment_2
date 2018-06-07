"""
COSC2671: Assignment 2, 2018
@author a small world
@description To detect community using Louvain's method. Modified based on Jeffrey's Chan script

"""


import networkx as nx
import random
from community import community_louvain
import json

random.seed(9001)

G = nx.read_graphml('all_nodes.graphml')
UG = nx.to_undirected(G)

print('Number of nodes of the graph: {}'.format(len(UG)))

dLouvainComms = community_louvain.best_partition(UG)

# Get the number of Louvain Community
louvainCommNum = max([y for (x,y) in dLouvainComms.items()]) + 1
print('Number of nodes of the Louvain Community: {}'.format(louvainCommNum ))

def dictToSetFormat(dComms, maxCommNum):
	"""
	Converts dictionary to set format.

	@param dComms: dictionary of communities, in the form of {(node id : comm id)}
	@param maxCommNum: number of communities in the dictionary
	@return: list representation [set(node ids...), ...]
	"""
	lGroundTruth = [set() for x in range(maxCommNum)]
	for (name, clusId) in dComms.items():
		lGroundTruth[clusId].add(name)

	return lGroundTruth


lLouvainComms = dictToSetFormat(dLouvainComms, louvainCommNum)

# louvain labels, stored in node attribute 'louvain'
for clusId, lComms in enumerate(lLouvainComms):
	for nodeId in lComms:
		UG.node[nodeId]['louvain'] = clusId

nx.readwrite.write_graphml(G, 'Louvain_G.graphml', infer_numeric_types=True)
