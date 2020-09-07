import tweepy
import datetime
import time
import preprocess
import pandas as pd
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sys

consumer_key= 'nOj8CQ7XjcNbTS9fFPp6wUNQF'
consumer_secret= '0VtlM5UXl2ZLAL0WMMT9WQ0kHFz4ufKTtn8T1bNVNpvdzYb2Mi'
access_token= '1301516905136771072-TrLtF8u5u0pUBmkSULnErXQcuyVk9i'
access_token_secret= 'hxCKEmbRNE1w0kn0H1owznIQJfuSjDGF3AaZLBCXgqQBO'

# StreamListener class inherits from tweepy.StreamListener and overrides on_status/on_error methods.
class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        # print(status.id_str)
        # if "retweeted_status" attribute exists, flag this tweet as a retweet.
        # main_count = 100
        # while main_count >= 0
        count = 2
        while count > 1:

            is_retweet = hasattr(status, "retweeted_status")

            if is_retweet:
                pass
            else:

                print(status.id_str)
                # Extend tweet so it shows all characters
                if hasattr(status,"extended_tweet"):
                    text = status.extended_tweet["full_text"]
                else:
                    text = status.text

                # check if this is a quote tweet.
                is_quote = hasattr(status, "quoted_status")
                quoted_text = ""
                if is_quote:
                    # check if quoted tweet's text has been truncated before recording it
                    if hasattr(status.quoted_status,"extended_tweet"):
                        quoted_text = status.quoted_status.extended_tweet["full_text"]
                    else:
                        quoted_text = status.quoted_status.text

                # remove characters that might cause problems with csv encoding
                remove_characters = [",","#","\n"]
                for c in remove_characters:
                    text = text.replace(c," ")
                    quoted_text = quoted_text.replace(c, " ")

                with open("out.csv", "a", encoding='utf-8') as f:
                    f.write("%s,%s,%s,%s,%s,%s\n" % (status.user.screen_name,is_retweet,is_quote,text,quoted_text, status.user.location))

            count -= 1

        time.sleep(5)
        count += 1

    def on_error(self, status_code):
        print("Encountered streaming error (", status_code, ")")
        sys.exit()

if __name__ == "__main__":
    # complete authorization and initialize API endpoint
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    # initialize stream
    streamListener = StreamListener()
    stream = tweepy.Stream(auth=api.auth, listener=streamListener,tweet_mode='extended')
    with open("out.csv", "w", encoding='utf-8') as f:
        f.write("user,is_retweet,is_quote,text,quoted_text, location\n")
    tags = [" python ", " coding ", " money ", " investing ", " nyc "]
    stream.filter(locations=[-74.1687,40.5722,-73.8062,40.9467], track=tags)
