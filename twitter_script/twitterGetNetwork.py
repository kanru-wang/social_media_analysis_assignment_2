"""
COSC2671: Assignment 2, 2018
@author a small world
@description Scrap the network data from a twitter account (ego) and save as a graphml file

"""
import tweepy as tw
import networkx as nx
import random


def scrap_network(egoname, client, n):

	"""

	To scrap followers and followees from an ego-centric twitter account.
	This function has the following parameters:

	@param egoname: a string of the ego-centric account
	@param client: a tweepy.API object with sleep mechanism
	@param n: number of randomly selected followees and followers
	       if n = 0, it will return the full list of followees and followers

	"""

	# Initialise a directed graph
	G = nx.DiGraph()
	G.add_node(egoname)

	try:

		# Get followers of the ego
		followerPages = tw.Cursor(client.followers_ids, screen_name=egoname).pages()
		currPage = next(followerPages)

		# if n is not zero,
		# Ceiling at the maximum number of followers or the specified n
		if n > 0:

			m = min(len(currPage), n)
			currPage  = random.sample(currPage, m)

		for userId in currPage:
			user = client.get_user(id=userId)
			sFollowerName = user.screen_name
			G.add_node(sFollowerName, followerCount=int(user.followers_count))
			G.add_edge(sFollowerName, egoname)

		# Get whom the ego follows
		followedPages = tw.Cursor(client.friends_ids, id=egoname).pages()
		currPage = next(followedPages)

		if n > 0:
			m = min(len(currPage), n)
			currPage  = random.sample(currPage, m)

		for userId in currPage:
			user = client.get_user(id=userId)
			G.add_node(user.screen_name)
			G.add_edge(egoname, user.screen_name, followerCount=int(user.followers_count))

		nx.write_graphml(G, egoname+'_tweets.graphml')

	except tw.TweepError:

		# In case the ego-centric user is a protected account
		print("Failed to run the command on that {}".format(egoname))
