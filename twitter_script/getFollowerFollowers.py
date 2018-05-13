# @author: a small world
# @description: to get the 100 random list of followers from an egocentric user's followers

import networkx as nx
import random
import twitterGetNetwork
import twitterClient

# Read the graph file
G = nx.read_graphml('R_Programming_tweets.graphml')

# specify egocentric user
userName1 = 'pydatasci'

# Get the followers' name
followers = [item[0] for item in G.nodes(data=True)]
n = len(followers)
k = 100
k = min(k, n)

print('{} has {} followers; we choose {} first-level followers randomly.'.format(userName1, n, k))
print('For each first-level followers, we choose 50 or lower followers randomly.')

followers = random.sample(followers, 100)
client = twitterClient.twitterClient()

for item in followers:
	print('Trying to scrap data from {}'.format(item))
	twitterGetNetwork.scrap_network(item, client, 50)