"""
COSC2671: Assignment 2, 2018
@author a small world
@description To read all graphml files from the current directory and stack them into one single graphml files

"""

import glob
import os
import networkx as nx
import sys

cwd = os.getcwd()
print('Your current directory is {}'.format(cwd))
graphml = glob.glob(cwd+"/*.graphml")
print('You have {} graphml files.'.format(len(graphml)))

# Initialise a directed graph and compose it
# with graph files read in the directory

print('\nStacking or composing graphs begins.....')
G = nx.DiGraph()
for item in graphml:
	try:
		sub_g = nx.read_graphml(item)
		G = nx.compose(G, sub_g)
	except TypeError:
		sys.stderr.write("Erroneous graphml\n")
		sys.exit(1)

nx.write_graphml(G, 'all_nodes.graphml')
print('Stacking is completed!')

