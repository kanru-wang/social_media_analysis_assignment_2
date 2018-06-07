import networkx as nx
import json


G = nx.read_graphml('all_nodes.graphml')

with open('degree_centrality.json', 'r') as fp:
	degree = json.load(fp)

# @param centrality_file = the file which records the top n most central nodes
# @param G = graph file
# @return shortest path = a descending ordered dictionary of shortest paths among the nodes
def shortest_path_length(centrality_file, G):
	k = 0
	a = list(centrality_file.keys())
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


