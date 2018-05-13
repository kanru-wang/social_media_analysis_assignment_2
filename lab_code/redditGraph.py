"""
COSC2671 Social Media and Network Analytics
@author Jeffrey Chan, 2018

"""


import networkx as nx
from argparse import ArgumentParser

from redditClient import redditClient

import matplotlib.pyplot as plt



#######################


def main():
    """
    Builds a reply graph from Reddit API.

    """

    # command line parsing
    parser = buildParser()
    args = parser.parse_args()

    # construct Reddit client
    client = redditClient()

    # construct directed graph
    replyGraph = nx.DiGraph()

    # this dictionary used to track the ids of submissions and posts, in order for us to construct
    # the links in the graph
    dSubCommentId = dict()

    # specify which subreddit we are interested in - 'python'
    subreddit = client.subreddit('python')

    counter = 1
    # loop through the hot submissions
    for submission in subreddit.hot():
        print(counter)
        print(submission.author.name)
        print(submission.name)
        submission.comments.replace_more(limit=None)
        for comment in submission.comments.list():
            if comment.author is not None and comment.author.name != 'ExternalUserError':
                print(comment.author.name)
        counter = counter + 1

        # check if author name is in the reply graph - if so, we update the number of submissions
        # associated with this user
        # if not, we construct a new node with 1 associated submission
#        if submission.author.name in replyGraph:
#            replyGraph.node[submission.author.name]['subNum'] += 1
#        else:
#            replyGraph.add_node(submission.author.name, subNum=1)

#        submissionId = submission.name;
        # this stores the submissionId (in submission.name) and associate it to the author
        # (submission.author.name).
#        dSubCommentId[submissionId] = {submissionId : submission.author.name}

        # for the current submission, retrieve the associated comments
#        submission.comments.replace_more(limit=None)
#        for comment in submission.comments.list():

            # some data checking to cater for deleted comments
            # we only add a link if the comment hasn't been deleted
#            if comment.author is not None and comment.author.name != 'ExternalUserError':
#                dSubCommentId[submissionId].update({comment.name : comment.author.name})

                # check if we have seen the comment's parent yet.  If not, then parent comment has been
                # deleted
#                if comment.parent_id in dSubCommentId[submissionId]:
                    # if edge exists, increment the replyNum, otherwise add a new edge
#                    if replyGraph.has_edge(comment.author.name, dSubCommentId[submissionId][comment.parent_id]):
#                        replyGraph[comment.author.name][dSubCommentId[submissionId][comment.parent_id]]['replyNum'] += 1
#                     else:
                        # need to check if the nodes have been added yet, if not add it and set subNum to 0
#                        if not comment.author.name in replyGraph:
#                            replyGraph.add_node(comment.author.name, subNum=0)

#                        if not dSubCommentId[submissionId][comment.parent_id] in replyGraph:
#                            replyGraph.add_node(dSubCommentId[submissionId][comment.parent_id], subNum=0)

#                        replyGraph.add_edge(comment.author.name, dSubCommentId[submissionId][comment.parent_id], replyNum=1)

    #
    # TODO: save graph to file












#######################


def buildParser():
    """
    Constructs the command line argument parser.

    @return: parser object
    """

    parser = ArgumentParser(description='Write out follower/followed for a user.')
    # look at the help= part to understand what the argument is for
    parser.add_argument('--replyFilename', help='Filename to output graph. Default is lab6.graphml', default='lab6.graphml')


    return parser




#######################

if __name__ == '__main__':
    main()

