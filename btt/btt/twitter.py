import tweepy
# http://tweepy.readthedocs.io/en/v3.5.0/getting_started.html

from .settings import TWITTER_API_CONSUMER_KEY, TWITTER_API_CONSUMER_SECRET, TWITTER_API_USER_ACCESS_TOKEN, TWITTER_API_USER_ACCESS_SECRET


class TwitterAPIWrapper(object):

    def __init__(self, consumer_key=TWITTER_API_CONSUMER_KEY, consumer_secret=TWITTER_API_CONSUMER_SECRET, access_token=TWITTER_API_USER_ACCESS_TOKEN, access_secret=TWITTER_API_USER_ACCESS_SECRET):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_secret)

        self.api = tweepy.API(self.auth)
