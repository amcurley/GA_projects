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
print(out.shape)
# Run through preprocessing
out['tweet'] = out['tweet'].apply(preprocess.clean_text)

print(out['tweet'])
# Run through modeling IF label == 1 save person else drop person


model = tf.keras.models.load_model('../saved_model/lstm_rnn_model')

accr = model.evaluate(X_test,y_test)
print('Test set\n  Loss: {:0.3f}\n  Accuracy: {:0.3f}'.format(accr[0],accr[1]))


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
