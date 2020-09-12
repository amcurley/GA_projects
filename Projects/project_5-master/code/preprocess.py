"""
This file needs to preprocess the words in each tweet so we
can do outage_analysis on the tweets to determine if the tweet
is actually a power outage or not!
"""

import pandas as pd
import numpy as np
import re

np.random.seed(42)

csv = pd.read_csv('../data/ready_for_processing.csv')


# These will be replaced by a space ' '
symbol_replace_space = re.compile('[/(){}\[\]\|@,;.£]')

# We will get rid of all these in the function below
bad_symbols = re.compile('[^0-9a-z #+_]')


def clean_text(tweet):

    # Make all of the text lower case
    tweet = tweet.lower()

    # Replace symbol_replace_space with a space
    tweet = symbol_replace_space.sub(' ', tweet)

    # Replace bad_symbols with a space
    tweet = bad_symbols.sub('', tweet)

    # Make all of the text lower case
    tweet = tweet.lower()

    # This gets rid of the integers
    tweet = re.sub(r'\d+', '', tweet)

    # Replace multiple spaces with a single space
    tweet = re.sub(r'\s+', ' ', tweet)

    return tweet

# Applying the clean_text function above to every tweet
csv['tweet'] = csv['tweet'].apply(clean_text)

csv.to_csv('../data/done_processing.csv', index=False)
