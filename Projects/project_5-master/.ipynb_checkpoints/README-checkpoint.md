# Using Social Media to Map Potential Power Outages


## Problem Statement  

During a disaster, residential areas often experience massive power outages, that in many cases last for days. Traditional methods to map power outages include live feeds and data that is provided by major utility companies as well as on satellite data that capture the extent of light emitted at night. Our tool will utilize a Twitter bot we created to pull live tweets about power outages and if the tweet is actually about a power outage we will map that users location. We will determine if a tweet is actually about a power outage using the combination of logistic regression, naive bayes, a random forest, and a LSTM RNN. If each of these models classify a tweet as a poweroutage then we will map that user. Our metric to evaluate will be accuracy 

**Team Members:**

- [Bill Fu]
- [David Lee](https://www.linkedin.com/in/daviddaeshinlee/)
- [Nathan Seither](https://www.linkedin.com/in/nseither/)

This project was completed in cooperation with [General Assembly](https://generalassemb.ly/) in September 2020.

## Requirements

- Windows, Linux, and MacOS are supported. ?

## Project Files
Here is the project workflow:
- 01_scraping_tweets.ipynb
- 02_preprocess.py
- 03_outage_analysis.py
- 04_models.py
- 05_twitter_bot.py
- 06_classify_tweets.py


## Executive Summary

Hello