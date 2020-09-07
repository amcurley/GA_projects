import tweepy
import datetime
import time
import preprocess
import pandas as pd
# import neural network


consumer_key= 'nOj8CQ7XjcNbTS9fFPp6wUNQF'
consumer_secret= '0VtlM5UXl2ZLAL0WMMT9WQ0kHFz4ufKTtn8T1bNVNpvdzYb2Mi'
access_token= '1301516905136771072-TrLtF8u5u0pUBmkSULnErXQcuyVk9i'
access_token_secret= 'hxCKEmbRNE1w0kn0H1owznIQJfuSjDGF3AaZLBCXgqQBO'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# We will use this api variable to make our requests to the Twitter API
api = tweepy.API(auth, wait_on_rate_limit=True)


queries = ["my power went out",
            "i lost power",
            "I hate these blackouts",
            "I have no power"
            ]

tweets = []
username = []
x = 3

# Load in neural net
# new_model = tf.keras.models.load_model('saved_model/my_model')
#
# Check its architecture
# new_model.summary()



for tweet in tweepy.Cursor(api.search, q='doggies -filter:retweets').items(x):
    x -= 1
    tweets = []
    username = []
    location = []
    try:
        if tweet.text[0] == "RT":
            pass
        else:
            tweets.append(tweet.text)
            username.append(tweet.user.screen_name)
            location.append(tweet.user.location)
        time.sleep(5)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break

    for each in tweets:
        each = preprocess.clean_text(each)

        # new_tweet = [each]
        # seq = tokenizer.texts_to_sequences(new_tweet)
        # padded = pad_sequences(seq, maxlen=max_sequence_length)
        # pred = model.predict(padded)
        # labels = [0, 1]
        # print(pred, labels[np.argmax(pred)])

        # if labels[np.argmax(pred)] == 0:
        #   pass
        # # else:
        # try:
        #     tweet.user.follow()
        #     print('Followed the user')
        # except:
        #     pass

        # the screen name of the user
    time.sleep(5)
    # location_final = []
    # for xi in username:
    #
    #     screen_name = xi
    #
    #     try:
    #         user = api.get_user(screen_name)
    #
    #         name = user.name
    #
    #         location = user.location
    #
    #
    #         if location == "":
    #             location_final.append("The user has not mentioned their location")
    #         else:
    #             location_final.append(location)
    #
    #     except tw.TweepError:
    #             print(f"The user {screen_name} does not exist")
    #             location_final.append("The user has not mentioned their location")
    #
    # time.sleep(5)


    # print(location_final)
    #
    #
    #     # # Like the tweet, follow, and comment under tweet
    #     # Comment with Most important tip plus here is a link to more resources
    #
    #     # @aidancurleyy We see you might have no power be safe! here is a list of
    #     # resources/tips that you might need www.david.com
    # print(username)
    # print(each)

david_df = pd.DataFrame({"tweet": tweets, "username": username, "location": location})


print(david_df)
