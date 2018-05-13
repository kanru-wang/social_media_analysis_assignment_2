# @author Yong Kai Wong, 2018
# @description Scrap the network dat from a twitter account (ego) and save as a graphml file
# TODO: To extend to parser with account_id

import tweepy as tw
import twitterClient
import networkx as nx

sEgoName = 'R_Programming'

# Initialise a directed graph
G = nx.DiGraph()
G.add_node(sEgoName)

# Get followers of the ego
client = twitterClient.twitterClient()
followerPages = tw.Cursor(client.followers_ids, screen_name=sEgoName).pages()
currPage = next(followerPages)

for userId in currPage:
	user = client.get_user(id=userId)
	sFollowerName = user.screen_name
	G.add_node(sFollowerName, followerCount=int(user.followers_count))
	G.add_edge(sFollowerName, sEgoName)

# Get whom the ego follows
followedPages = tw.Cursor(client.friends_ids, id=sEgoName).pages()
currPage = next(followedPages)

for userId in currPage:
	user = client.get_user(id=userId)
	G.add_node(user.screen_name)
	G.add_edge(sEgoName, user.screen_name, followerCount=int(user.followers_count))

nx.write_graphml(G, sEgoName+'_tweets.graphml')
