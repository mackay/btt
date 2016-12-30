from .btt.twitter import TwitterAPIWrapper
from .models import Tweet


class TweetCollector(TwitterAPIWrapper):

    def collect_tweets_for_account( account_id, after_date=None, maximum_count=None ):
        pass

    def collect_tweets_for_term( term, after_date=None, maximum_count=None ):
        pass

    def persist_tweets( tweets ):
        pass


class TweetClassifier(object):

    def __init__(self):
        pass

    def classify_tweet(self, tweet ):
        pass
