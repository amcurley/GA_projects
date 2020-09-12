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
import pickle

np.random.seed(42)

exec(open("twitter_bot.py").read())
# Bring in out csv from bot
out = pd.read_csv('../data/out.csv')
out.to_csv('../data/baseline_checker.csv')
print(out.shape)
# Run through preprocessing
out['tweet'] = out['tweet'].apply(preprocess.clean_text)

# print(out['tweet'])
# print(out['tweet'])

X = out['tweet']

model_lr = pickle.load(open("gridsearch_lr_model.sav", "rb"))
model_nb = pickle.load(open("gridsearch_nb_model.sav", "rb"))
# print(model.predict_proba(X))

pred_lr = model_lr.predict(X)
pred_nb = model_nb.predict(X)
# print(pred)



out['predict_lr'] = pred_lr
out['predict_nb'] = pred_nb
print(out.head())

out.to_csv('../data/lr_predictions.csv', index=False)
# labels = [0, 1]
# print(pred, labels[np.argmax(pred)])
# LogisticRegression Model Brought in using pickle
# pred = model.predict(X)
# labels = [0, 1]
# print(pred, labels[np.argmax(pred)])




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
