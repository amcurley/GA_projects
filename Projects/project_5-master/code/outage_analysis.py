import utils
import pandas as pd
import numpy as np

bad_words = ["Omari","Hardwick","50","cent","Joseph","Rotimi","Naturi","Naughton","Lela","Loren",
"Larenz","Tate","internet","Internet","Shane","Johnson","Jerry","Ferrara","Lucy","Walters",
"Sinqua","Walls","Andy","Bean","David","Fumero","Sung","Kang","kidding","jk","Ghost", "politics",
"trump", "biden" "wifi's", "attorney", "point", "powerpoint", "girl", "guy", "black", "white", "austin",
"abusing", "abused", "Starz", "starz",  "ruiz", "estelle", "kanan", "dre", "wifi", "hotel", "woman",
"man", "guess", "potency", "competenecy", "competence", "brawn", "horsepower", "hp", "acceleration",
"grunt", "vacation", "resort", "GOP", "nazi"]

final_csv = pd.read_csv('../datasets/processed_csv.csv')


# csvs = final_csv.head()

tweets = []

for xi in final_csv['tweet']:
    tweets.append(xi)


label = []

for test in tweets:
    res = any(ele in test for ele in bad_words)
    if res == True:
        label.append(0)
    else:
        label.append(1)

final_csv['label'] = label

# print(tweets)
print(final_csv.head())
# print(label)
print(final_csv.shape)
print(final_csv['label'].value_counts())
print(final_csv['label'].value_counts(normalize=True))

final_csv.to_csv('../datasets/neuralnetwork.csv', index=False)

"""

After running this script you will now go onto the LSTM RNN notebook

"""
