# @author: a small world
# @description: to get the 100 random list of followers from an egocentric user's followers

import networkx as nx
import random
import twitterGetNetwork
import twitterClient

# set a random seed
random.seed(9001)

def getFollowerFollowers(userName, k1, k2):

	"""
	# To get the followers' followers of an ego-centric
	# @param username: ego-centric name
	# @param k1: number of first-level followers
	# @param k2: number of second-level followers

	"""
	try:
		G = nx.read_graphml(userName+'_tweets.graphml')


		# Get the followers' name
		followers = [item[0] for item in G.nodes(data=True)]
		n = len(followers)

		print('{} has {} followers; we choose {} first-level followers randomly.'.format(userName, n, k1))
		print('For each first-level followers, we choose {} or lower followers randomly.'.format(k2))

		followers = random.sample(followers, k1)
		client = twitterClient.twitterClient()

		for item in followers:
			print('Trying to scrap data from {}'.format(item))
			twitterGetNetwork.scrap_network(item, client, k2)

	except TypeError:
		print("Failed to run this function on {}".format(userName))


getFollowerFollowers('pycharm', 100, 50)