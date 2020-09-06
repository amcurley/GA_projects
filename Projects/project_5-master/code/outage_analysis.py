import utils
import pandas as pd


bad_words = ["Omari","Hardwick","50","cent","Joseph","Rotimi","Naturi","Naughton","Lela","Loren",
"Larenz","Tate","internet","Internet","Shane","Johnson","Jerry","Ferrara","Lucy","Walters",
"Sinqua","Walls","Andy","Bean","David","Fumero","Sung","Kang","kidding","jk","Ghost", "politics",
"trump", "biden" "wifi"]

final_csv = pd.read_csv('processed_csv.csv')


csvs = final_csv.head()

tweets = []

for xi in csvs['tweet']:
    tweets.append(xi)


label = []

for test in tweets:
    res = any(ele in test for ele in bad_words)
    if res == True:
        label.append(0)
    else:
        label.append(1)

csvs['label'] = label

print(tweets)
print(csvs)
print(label)
