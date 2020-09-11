import tweepy
import datetime
import time
import preprocess
import pandas as pd
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sys

consumer_key= 'nOj8CQ7XjcNbTS9fFPp6wUNQF' # Don't have these in the final
consumer_secret= '0VtlM5UXl2ZLAL0WMMT9WQ0kHFz4ufKTtn8T1bNVNpvdzYb2Mi'# Don't have these in the final
access_token= '1301516905136771072-TrLtF8u5u0pUBmkSULnErXQcuyVk9i'# Don't have these in the final
access_token_secret= 'hxCKEmbRNE1w0kn0H1owznIQJfuSjDGF3AaZLBCXgqQBO'# Don't have these in the final

class StreamListener(tweepy.StreamListener):

    tweet_counter = 0 # Static variable

    def on_status(self, status):
        stati = []
        count = 2
        while count > 1:

            is_retweet = hasattr(status, "retweeted_status")

            if is_retweet:
                pass
            else:

                print(status.id_str)
                stati.append(status.id_str)
                # Extend tweet so it shows all characters
                if hasattr(status,"extended_tweet"):
                    text = status.extended_tweet["full_text"]
                else:
                    text = status.text

                # remove characters that might cause problems with csv encoding
                remove_characters = [",","#","\n"]
                for c in remove_characters:
                    text = text.replace(c," ")

                with open("../data/out.csv", "a", encoding='utf-8') as f:
                    f.write("%s,%s,%s,%s\n" % (status.user.screen_name,is_retweet,text, status.user.location)) # Need to fix this

            count -= 1

            if StreamListener.tweet_counter <= 3: #This number plus 2 is how many tweets I will get!
                StreamListener.tweet_counter += 1
                pass
            else:
                stream.disconnect()


        time.sleep(5)
        count += 1
        # StreamListener.tweet_counter += 1

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
    with open("../data/out.csv", "w", encoding='utf-8') as f:
        f.write("user,is_retweet,tweet,location, state, state_1\n")

    tags = [" python ", " coding ", " money ", " investing ", " stocks "]
    # These bounding boxes https://www.bmc.com/blogs/track-tweets-location/#:~:text=filter()%20method%20of%20Tweepy,are%20the%20top%20right%20corner.
    NYC = [-74.1687,40.5722,-73.8062,40.9467] #check docs for these

    stream.filter(locations= NYC#, track = tags
    )
