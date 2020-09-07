"""
This file needs to preprocess the words in each tweet so we
can do outage_analysis on the tweets to determine if the tweet
is actually a power outage or not!
"""

import pandas as pd
import numpy as np
import re

csv = pd.read_csv('../aidan_final_df.csv')

# These will be replaced by a space ' '
symbol_replace_space = re.compile('[/(){}\[\]\|@,;]')

# We will get rid of all these in the function below
bad_symbols = re.compile('[^0-9a-z #+_]')

# We will get rid of all of the stopwords
# STOPWORDS = set(stopwords.words('english')) # Might want to add these?

# lemmatizer = WordNetLemmatizer() # Should we do this?

def clean_text(tweet):

    # Make all of the text lower case
    tweet = tweet.lower()

    # Replace symbol_replace_space with a space
    tweet = symbol_replace_space.sub(' ', tweet)

    # Replace bad_symbols with a space
    tweet = bad_symbols.sub('', tweet)

    # This gets rid of the integers
    tweet = re.sub(r'\d+', '', tweet)

    # Replace multiple spaces with a single space
    tweet = re.sub(r'\s+', ' ', tweet)

    """
    Might need to add more stuff in here such as emoji remover?
    lemmatizer?
    Stopwords?
    """

#     [lemmatizer.lemmatize(i) for i in text]

    # remove stopwords from text
    # text = ' '.join(word for word in text.split() if word not in STOPWORDS)

    return tweet

# Applying the clean_text function above to every tweet
csv['tweet'] = csv['tweet'].apply(clean_text)

csv['tweet'][3] = "my power went out haha just kidding it did not"

# print(csv.head())

csv.to_csv('../datasets/processed_csv.csv', index=False)
