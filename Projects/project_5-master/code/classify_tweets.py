import pandas as pd
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sys
import preprocess
import numpy as np
import tensorflow as tf
from tensorflow import keras
import twitter_bot

exec(open("twitter_bot.py").read())
# Bring in out csv from bot
out = pd.read_csv('../data/out.csv')

print(len(out))

# Run through preprocessing


# Run through modeling IF label == 1 save person else drop person







"""

Bring in the out.csv with all of the tweets pulled.

Run this csv through preprocess.py to clean the text.

Run the cleaned tweets through:

new_tweet = ["test tweet"]
seq = tokenizer.texts_to_sequences(new_tweet)
padded = pad_sequences(seq, maxlen=max_sequence_length)
pred = model.predict(padded)
labels = [0, 1]
print(pred, labels[np.argmax(pred)])


Then if 1 we grab that users location and map in tableau.
     if 0 we pass.
"""
# if __name__ == '__main__':
#     # service.py executed as script
#     # do something
#     twitter_bot.StreamListener(tweepy.StreamListener)
