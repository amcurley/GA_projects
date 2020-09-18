# Using Social Media to Map Potential Power Outages
***Authors:*** Aidan Curley, Bill Fu, David Lee, Nathan Seither  

## Problem Statement  
During a disaster, residential areas often experience massive power outages, that can last for hours or days. Traditional methods to map power outages include live feeds and data that is provided by major utility companies as well as on satellite data that capture the extent of light emitted at night. Although accurate, it does not reach the customer in a way that is impactful to the end consumer. Our method will utilize a Twitter bot to detect tweets about power outages in real time and map the users location if they are experiencing a power outage. Additionaly we hope to respond to each tweet with supporting material and resources.
  

## Project Files
Here is the project workflow:  
- [01_scraping_tweets.ipynb](./new_code/01_scraping_tweets_5.ipynb)     
- [02_preprocess.py](./new_code/02_preprocess.py)      
- [03_outage_analysis.py](./new_code/03_outage_analysis.py)  
- [04_models.py](./new_code/04_models.py)  
- [04b lstm_rnn.py](./new_code/04b_lstm_rnn.ipynb)  
- [05_twitter_bot.py](./new_code/05_twitter_bot.py)     
- [05b_neural.py](./new_code/05b_neural.py)  
- [06_classify_tweets.py](./new_code/06_classify_tweets.py)  

## Executive Summary  

Our team approached this problem using an automated social media tool called a Twitter bot to locate the areas of power outages using natural language processing. We came to the conclusion that using Twitter will be the best platform since it's in realtime and has the production capability of operating continuously. Our final product was able to successfully find tweets in real time, verify it's accuracy, and insert it into a dataframe that could be queried and analyzed. There are additional capabilities within our model making it a plug and play application, customizable to any business needs.
 
## Data Collection  

Before deploying a bot we had to train our models on a lot of data so when we pull in tweets from the bot we can get accurate predictions if the tweet is actually a power outage or not. So, we used GetOldTweets3 to scrape 280,000 tweets from January 1st, 2020 to August 31st, 2020. From those tweets 150,000 of them contain the queries "my power went out", "i lost power", "there is a power outage", or "I have no power." The remaining 130,000 tweets are for random queries such as "we went out shopping" and "The weather is nice." We wanted to add noise into our data so the models can better understand what tweets are actually about power outages.   
![](assets/tweets_gathered.png)
  
## EDA  
This analysis was done with 28k tweets we collected at the beginning stages of the projects. Among these 28,000 post, 11,000 of them had location information.  
  
From the chart at top left, we can see that most of  the outages located in coastal states and north east and central east states
The bottom chart had the top 15 outage states plotted with their populations, we noticed that the power outages were highly correlated with population.  
![](assets/initial_analysis.png)  

## Modeling Process  
After doing the intital data cleaning, analysis, and labeling, we built four models to classify whether a post is a true power outage or not. The models were: a Naive Bayes classifier, a logistic regression classifier, a random forest classifer, and long short-term memeroy (LSTM) recurrent neural network (RNN) classifier. 
![](assets/model_strategy.png)
Each model generated a predicting label for a tweet: 0 for not power outage and 1 for power outage. With the collected data, we were able to achieve 89% accuracy on both training and testing datasets for each of these models.
In order to push our models to the production enviroment, we need to eliminate false positives (false power outages). So that we used a four pronged approach to our final modeling strategy. Namely, if each individual model generateed a 1 then we will classify that tweet as a true power outage. This enabled our models to have the greatest chance at making the most accurate prediction
![](assets/model_analysis.png)
![](assets/model_metrics.png)
## Implementation
After modeling was completed, we moved onto the implementation of our twitter bot. The twitter bot was implemented by python scripts at this stage. When it was running, the twitter bot would be listening for tweets 24/7 until it was told to stop.   
![](assets/implementation_sneak_peak.png)
This was as real time monitoring tweets. As the monitoring criteria was met, a new tweet came in. It would go through preprocessing and the modeling automatically. Then this tweet got a predicted label: either being a 0 for not a power outage or 1 for a power outage tweet. If this tweet was classified as a power outage tweet, the twitter bot would automatically try to contact the owner of the posts. At this stage, due to the accessibility of the twitter user information and authorization from Twitter, the automatically contacting features of the twitter bot were limited.
## Conclusions
After testing our twitter bot with our multi-layered model implementation, our team concludes that mapping power outages through Tweets is possible. We successfully were able to label new tweets with a prediction generated from our layered model. Even though our train and test scores were very impressive, we were able to identify areas where we can further improve our classification accuracy on live new tweets with adjustments on the initial scraped tweets for training our models along with adjusting hyper parameters.
Identifying twitter API limitations also point our team to generalizing the key phrases we used for evaluating our model to lower bias in our analysis. Our accuracy on 227 streamed tweets we manually labeled suggests that we have over fit our model on the key phrases we initially trained on. Gathering more data is a necessary step to increase accuracy.
## Next Steps 
Our hope is that one day we can help power providers in ensuring that users that tweet about experiencing an outage would know safety best practices, with links to helpful resources.
![](assets/Response_tweet.png)
With this technology we believe we can map out power outage disasters and help both energy providers and the customers they serve.
By helping providers in implementing an early detection system through Tweets, resulting in streamlining the handling of their manpower for faster restoration, and ensuring residential safety and assurance, we hope our tool will help bridge the gap between power companies, and the residents they serve.
To ensure this goal our refinement and scaleability will have to include the following:
1. Refine our production models to achieve a higher accuracy rating
2. Containerize the application using Docker containers, to ensure compatibility across different platforms and to easily scale our solution. 
    - These containers would include a database such as Redis or Mongodb.
3. Partnership with Twitter to increase successful implementation and location data
4. Increase the number of bots to ensure 100% operatational capacity
![](assets/vision.png)
## Citations  
 - http://docs.tweepy.org/en/v3.5.0/index.html  
 - https://github.com/Mottl/GetOldTweets3  
 - https://github.com/Mottl/GetOldTweets3/issues/57 Clairedevries 
 - https://github.com/vprusso/youtube_tutorials/blob/master/twitter_python/part_1_streaming_tweets/tweepy_streamer.py
 - https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States_by_population  
 - https://www.youtube.com/watch?v=fqMOX6JJhGo  