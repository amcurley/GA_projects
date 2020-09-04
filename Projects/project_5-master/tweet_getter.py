import GetOldTweets3 as got
import time
from datetime import datetime, date, timedelta
import pandas as pd
import numpy as np

def DownloadTweets(SinceDate, UntilDate, query, sleep=900, maxtweet=0) :
    #create a list of day numbers
    since = datetime.strptime(SinceDate, '%Y-%m-%d')
    days = list(range(0, (datetime.strptime(UntilDate, '%Y-%m-%d') - datetime.strptime(SinceDate, '%Y-%m-%d')).days+1))
    tweets = []

    for day in days:
        init = got.manager.TweetCriteria().setQuerySearch(query).setSince((since + timedelta(days=day)).strftime('%Y-%m-%d')).setUntil((since+ timedelta(days=day+1)).strftime('%Y-%m-%d')).setMaxTweets(maxtweet)
        get = got.manager.TweetManager.getTweets(init)
        tweets.append([[
        # tweet.id,
        # tweet.date, this could allow me to loop through?
        tweet.text
        ] for tweet in get])

        print("day", day+1, "of", len(days), "completed")
        print("sleeping for", sleep, "seconds")
        time.sleep(sleep)
    #flatten list
    tweets = [tweet for sublist in tweets for tweet in sublist]

    # [print(n[0], sep='\n') for n in tweets]
    hmm = [n[0] for n in tweets]
    # print(hmm)
    # print(type(hmm))
    return print(len(hmm))


#%%
since = "2020-09-01"
until = "2020-09-02"

tweets = DownloadTweets(since, until, query=' my power went out ', maxtweet=5, sleep=10)


# Change the maxtweet
