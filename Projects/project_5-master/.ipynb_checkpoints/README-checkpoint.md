# Using Social Media to Map Potential Power Outages

***Authors:*** Aidan Curley, Bill Fu, David Lee, Nathan Seither  

## Problem Statement  

During a disaster, residential areas often experience massive power outages, that in many cases last for days. Traditional methods to map power outages include live feeds and data that is provided by major utility companies as well as on satellite data that capture the extent of light emitted at night. Our method will utilize a Twitter bot to detect tweets about power outages in real time and map the users location if they are experiencing a power outage.


## Requirements  

Here we will write what they need to have installed to run this code.

```   
pip install tweepy   
```    
- Windows, Linux, and MacOS are supported. ?

## Project Files
Here is the project workflow:  

- [01_scraping_tweets.ipynb](https://git.generalassemb.ly/insigh1/Submissions/blob/master/ProjectsDL/project_5-master/new_code/01_scraping_tweets_5.ipynb)     
- [02_preprocess.py](https://git.generalassemb.ly/insigh1/Submissions/blob/master/ProjectsDL/project_5-master/new_code/02_preprocess.py)      
- [03_outage_analysis.py](https://git.generalassemb.ly/insigh1/Submissions/blob/master/ProjectsDL/project_5-master/new_code/03_outage_analysis.py)  
- [04_models.py](https://git.generalassemb.ly/insigh1/Submissions/blob/master/ProjectsDL/project_5-master/new_code/04_models.py)  
- [04b lstm_rnn.py](https://git.generalassemb.ly/insigh1/Submissions/blob/master/ProjectsDL/project_5-master/new_code/04b_lstm_rnn.ipynb)  
- [05_twitter_bot.py](https://git.generalassemb.ly/insigh1/Submissions/blob/master/ProjectsDL/project_5-master/new_code/05_twitter_bot.py)     
- [05b_neural.py](https://git.generalassemb.ly/insigh1/Submissions/blob/master/ProjectsDL/project_5-master/new_code/05b_neural.py)  
- [06_classify_tweets.py](https://git.generalassemb.ly/insigh1/Submissions/blob/master/ProjectsDL/project_5-master/new_code/06_classify_tweets.py)      


## Executive Summary  
Our team's approach to developing this tool was to first determine which social media's we will use to pull data from. We came to the conclusion that using Twitter will be the best platform. Twitter is the best platform for this problem since it is the one platform that we can deploy a bot and track certain words in posts in real time. 

Before deploying a bot we had to train our models on a lot of data so when we pull in tweets from the bot we can get accurate predictions if the tweet is actually a power outage or not. So, we used GetOldTweets3 to scrape 280,000 tweets from January 1st, 2020 to August 31st, 2020. From those tweets 150,000 of them contain the queries "my power went out", "i lost power", "there is a power outage", or "I have no power." The remaining 130,000 tweets are for random queries such as "we went out shopping" and "The weather is nice." We wanted to add noise into our data so the models can better understand what tweets are actually about power outages. 



## Modeling Process
After doing the intital data cleaning we moved on to

## Conclusions and Future Steps
We were able to make a 


## Citations




