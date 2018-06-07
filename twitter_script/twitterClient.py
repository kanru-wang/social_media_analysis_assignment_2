# @author a small world, 2018
# @description Modified on Jeffrey Chan's script, this returns a tweepy.API object with sleep mechanism

import sys
import tweepy as tw


def twitterAuth():
    """
        Setup Twitter API authentication.
        Replace keys and secrets with your own.

        @returns: tweepy.OAuthHandler object
    """

    try:
        consumerKey = ""
        consumerSecret = ""
        accessToken = ""
        accessSecret = ""
    except KeyError:
        sys.stderr.write("Key or secret token are invalid.\n") # standard output, input, and errors
        sys.exit(1)                                            # exit codes

    auth = tw.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessSecret)

    return auth




def twitterClient():
    """
        Setup Twitter API client.

        @returns: tweepy.API object
    """

    auth = twitterAuth()
    client = tw.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

    return client