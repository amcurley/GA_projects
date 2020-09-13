
import tweepy
import datetime
import time
import pandas as pd
import numpy as np
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sys

np.random.seed(42)

consumer_key= '9C0nedFj98hB83LQCsW5xIDvZ' # Don't have these in the final
consumer_secret= 'J60uZyJ2JhZe0POGTdM7uUD6hno8kia42yg8TNBCIHHoUFS8l5'# Don't have these in the final
access_token= '1301167716456374272-7KDrVSaJYt6u0qKYiGOz1NJr6CsvSz'# Don't have these in the final
access_token_secret= 'a9woFTFbP2FcHwVpfyOUGZIuqaI95xOWIwY5HhfBma9vw'# Don't have these in the final

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    count = 2 # This is to pull in only 1 tweet per loop so we do not get rate limited
    while count > 1:
        def on_status(self, tweet):
            is_retweet = hasattr(tweet, "retweeted_status")
            if is_retweet: # If the tweet has the attribute "retweeted_status" pass
                pass
            else:
                is_quote = hasattr(tweet, "quoted_status")
                if is_quote: # If the tweet has the attribute "quoted_status" pass
                    pass
                else:
                    print(f"{tweet.user.name}")
                    print(f"{tweet.text}")
                    api.update_status(f'python is fun')

            count -= 1

    time.sleep(2)
    count += 1

    def on_error(self, status_code):
        print("Encountered streaming error (", status_code, ")")
        sys.exit()

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, listener)
stream.filter(track=["Python"], languages=["en"])
