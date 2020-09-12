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
# import neural

np.random.seed(42)

# This will run the twitter_bot.py script
exec(open("twitter_bot.py").read())

# Bring in out csv from twitter_bot.py
out = pd.read_csv('../data/out.csv')
# out.to_csv('../data/baseline_checker.csv')
print(out.shape)

# Run through preprocessing
out['tweet'] = out['tweet'].apply(preprocess.clean_text)


X = out['tweet']

# Load in the LogisticRegression
model_lr = pickle.load(open("gridsearch_lr_model.sav", "rb"))

# Load in the Naive Bayes Model
model_nb = pickle.load(open("gridsearch_nb_model.sav", "rb"))

# Load in the Random Forest Model
# model_rf = pickle.load(open("gridsearch_rf_model.sav", "rb"))


# Predicting
pred_lr = model_lr.predict(X)
pred_nb = model_nb.predict(X)
# pred_rf = model_rf.predict(X)
# pred_rnn = neural.neural(out)

# Adding prediction columns
out['predict_lr'] = pred_lr
out['predict_nb'] = pred_nb
# out['predict_rnn'] = pred_rnn
# out['predict_rf'] = pred_rf

# Seeing the spread of 0's and 1's
print(out['predict_lr'].value_counts(normalize=True))
print(out['predict_nb'].value_counts(normalize=True))
# print(out['pred_rf'].value_counts(normalize=True))
# print(out['predict_rnn'].value_counts(normalize=True))

# Saving the final csv
out.to_csv('../data/predictions.csv', index=False)
