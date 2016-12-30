from .btt.twitter import TwitterAPIWrapper
from .models import Campaign, Engagement, EngagementPurpose


class EngagementActor(TwitterAPIWrapper):

    def respond_directly( tweet, response ):
        pass

    def schedule_direct_response( tweet, response ):
        pass

    def respond_to_followers( tweet, response, follower_count=None ):
        pass

    def schedule_follower_response( tweet, response, follower_count=None ):
        pass


    def process_scheduled_responses():
        pass
