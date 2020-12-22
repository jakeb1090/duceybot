import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener, Stream
from config import az, fl
# import pandas as pd

class bot:
    def __init__(self, state):
        self.api_key = state['api_key']
        self.api_secret = state['api_secret']
        self.access_key = state['access_key']
        self.access_secret = state['access_secret']

    def get_params(self):
        return self.gov

    def authenticate(self):
        auth = OAuthHandler(self.api_key, self.api_secret)
        auth.set_access_token(self.access_key, self.access_secret)
        api = tweepy.API(auth)
        return api

    def run_botaz(self):
        api = self.authenticate()
        geosearch = api.search(q="ducey -filter:retweets AND -filter:links",tweet_mode="extended")
        for x in geosearch:
            if len(x.full_text) < 100:
                print(x.full_text, "\n")
                try:
                    api.retweet(x.id)
                except:
                    pass
                
    def run_botfl(self):
        api = self.authenticate()
        geosearch = api.search(q="desantis -filter:retweets AND -filter:links",tweet_mode="extended")
        for x in geosearch:
            if len(x.full_text) < 100:
                print(x.full_text, "\n")
                try:
                    api.retweet(x.id)
                except:
                    pass
                
    def run_aztest(self):
        api = self.authenticate()
        geosearch = api.search(q="ducey -filter:retweets AND -filter:links",tweet_mode="extended")
        results = []
        for x in geosearch:
            results.append(x)
        return results