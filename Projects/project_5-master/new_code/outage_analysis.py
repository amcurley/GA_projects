import pandas as pd
import numpy as np
import preprocess

np.random.seed(42)

bad_words = ["Omari","Hardwick","50","cent","Joseph","Rotimi","Naturi","Naughton","Lela","Loren",
"Larenz","Tate","internet","Internet","Shane","Johnson","Jerry","Ferrara","Lucy","Walters",
"Sinqua","Walls","Andy","Bean","David","Fumero","Sung","Kang","kidding","jk","Ghost", "politics",
"trump", "biden" "wifi's", "attorney", "point", "powerpoint", "girl", "guy", "black", "white", "austin",
"abusing", "abused", "Starz", "starz",  "ruiz", "estelle", "kanan", "dre", "wifi", "hotel", "woman",
"man", "guess", "potency", "competenecy", "competence", "brawn", "horsepower", "hp", "acceleration",
"grunt", "vacation", "resort", "GOP", "nazi"]

final_csv = pd.read_csv('../data/done_processing.csv')


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


# Add bad words csv's here!
bad_words1 = pd.read_csv('../data/bad_words1.csv')
bad_words2 = pd.read_csv('../data/bad_words2.csv')
# Label all of these as non power outage tweets
bad_words1['label'] = 0
bad_words2['label'] = 0
# Drop any NaN values
bad_words1.dropna(inplace=True)
bad_words2.dropna(inplace=True)

bad_words1['tweet'] = bad_words1['tweet'].apply(preprocess.clean_text)
bad_words2['tweet'] = bad_words2['tweet'].apply(preprocess.clean_text)

# print(tweets)
final_csv = final_csv.append([bad_words1, bad_words2])

print(final_csv.head())
# print(label)
print(final_csv.shape)
print(final_csv['label'].value_counts())
print(final_csv['label'].value_counts(normalize=True))

final_csv.to_csv('../data/ready_for_modeling.csv', index=False)

"""

After running this script you will now go onto the modeling

"""
