import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener, Stream
from config import api_key, api_secret, access_key, access_secret
import time
# import pandas as pd

auth = OAuthHandler(api_key, api_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

def get_tweets():
    #geofilter = "geocode="33.574450,-112.156970,150mi","
    geosearch = api.search(q="ducey -filter:retweets AND -filter:links",tweet_mode="extended")
    nearme = []
    for x in geosearch:
        # data = {
        #     'author':  x.author.screen_name,
        #     'followers': x.author.followers_count,
        #     'text': x.full_text,
        #     'favorited': x.favorited,
        #     'fav_count' : x.favorite_count,
        #     'retweet_count': x.retweet_count,
        #     'retweeted': x.retweeted,
        #     'created_at': x.created_at,
        #    }
        # nearme.append(data)
        if len(x.full_text) > 100:
            pass
        else:
            try:
                api.retweet(x.id)
            except:
                pass

