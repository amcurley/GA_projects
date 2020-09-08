import pandas as pd
import numpy as np
import twitter_bot





new_model = tf.keras.models.load_model('saved_model/my_model')

# Check its architecture
new_model.summary()



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
