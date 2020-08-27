# Self Classifiying Reddit Posts

Aidan Curley | US-DSIR-720 | 08.28.2020

## Problem Statement  

According to Reddit you can, “reach passionate and diverse communities organized around thousands of different topics, ” through advertising. Reddit had 199 million posts in 2019 alone according to their blog and approximately 138,000 active subreddits among their total 1.2 million subreddits. With so much information, how do they make sure people are posting in the right subreddits? Well they don't. So, how can we ensure the posts are going into the proper subreddit’s? Through machine learning! 

## Table of Contents

- [Project Directory](#projectdirectory)
- [Executive Summary](#executivesummary)
- [Data](#data)
- [Modelling Process](#modellingprocess)
- [Conclusions & Recommendations](#c&r)
- [Future Steps](#futuresteps)
- [Citations](#cite)


<a name="projectdirectory"></a>
## Project Directory
    
```
project_3-master
|__ assets 
|   |__ goldswan.png
|   |__ neighborhoodboxplot.png
|__ code       
|   |__ 01_get_data.ipynb  
|   |__ 02_baseline_score.ipynb  
|   |__ 03_title_only.ipynb  
|   |__ 04_title_selftext.ipynb  
|__ data  
|   |__ data_ai.csv  
|   |__ data_ml.csv  
|__ Presentation.pdf  
|__ README.md  

```

<a name="executivesummary"></a>
## Executive Summary

As Reddit continues to grow so does the chances of posting in the wrong subreddit's. One or two posts in the wrong subreddit's are not a problem but when Reddit is averaging more than 16 million posts a month there is a lot of room for error. So how does reddit make sure posts are going in the right subreddit? They don't. The user has to specify the specific subreddit that post should belong too or if the person posts in the wrong subreddit, usually people in that subreddit direct them to the proper subreddit for their post. 

So whats the solution to this problem? A way to reduce the likelihood of human error when selecting a subreddit is if Reddit had a recommendation system that as you are writing your reddit post it says with a certain amount of accuracy which subreddit that post should belong to. Implementing this could reduce the amount of posting in the wrong subreddit which could lead to cleaner subreddit's and potentially more targeted advertising within these subreddit's.   

For this project I chose the two subreddits r/MachineLearning and r/artificial because these topics have a lot of overlapping content and words. I will use Natural Language Processing and a variety of classification machine learning models such as logistic regression, naive bayes, random forests, and an LSTM RNN to classify a post to either be in the r/MachineLearning subreddit or the r/artificial subreddit. We will evaluate each of these models based on their accuracy scores. I chose a handful of models to see how the accuracy score improves as model complexitiy increases. 

My best accuracy score so far was 86.15%. With this accuracy score on two subreddits that are very similiar in topic I am confident in moving forward with this project and moving on to the next steps. The next steps consist of creating this same process but for every subreddit on Reddit. 


<a name="data"></a>
## Data 

The data I am using for this project consists of a total of 31,299 posts from each subreddit which is 62,598 posts in total.  From these posts I only used the 'title'(the title of the post) and the 'selftext'(the content within the post) columns. I used the [pushshift api](https://github.com/pushshift/api) to scrape this data from reddit. For these two subreddits there were a couple cleaning steps that had to be addressed. In the 'selftext' column there were a lot of NaN values and removed and deleted posts. My way around these issue were replacing those values with a space so my models can still use that data. 

Replicating this process for future advancements is time consuming however very doable. Scraping the 276 million posts and gathering 2,000 posts from each subreddit would take approximately 24 hours using a mulit threading scraping process. The final file would be approximately be around 150 GB as well.


<a name="modellingprocess"></a>
## Modeling Process  

After bringing in our data we move onto the modeling process.

After performing the common natural langugage processing tasks such as removing stop words, numbers, special characters and tokenizing the data we are finally able to model our data. 

Before moving onto modeling the data I wanted to see the most common words in each subreddit after cleaning the data. These were the 15 most common words in each subbreddit:

![](./assets/wordcount.png)  

As we can see in these charts there were a lot of overlapping words that seemed to play a role in deciding which subreddit a post belonged to. We will keep an eye on these words while modeling and decide later on if we should remove some of these words or not since there is a lot of overlap.

The metric I am scoring the models on is accuracy. Before getting the accuracy for the more complex models I had to get the baseline accuracy score. This baseline score was 50% since I had perfectly balanced classes.

I did one set of modeling for just the 'title' column and another set of modeling for the 'title' and 'selftext' columns together. I wanted to see if adding the 'selftext' column increased my model's accuracy, made it stay the same, or made the accuracy score decrease. 

**Title Only Model & Accuracy:**
- Simple Logisitic Regression had an accuracy score of 80.79% 
- Logistic Regression with Gridsearch had an accuracy score of 80.97%
- Naive Bayes with Gridsearch had an accuracy score of **86.15%**

**Title and Selftext Model & Accuracy:**
- Simple Logisitic Regression had an accuracy score of 80.46%
- Logistic Regression with Gridsearch had an accuracy score of 80.09%
- Naive Bayes with Gridsearch had an accuracy score of 82.43%

**LSTM RNN**
- I was able to achieve an accuracy score of 81.60%


Since the model with the highest accuracy is the Gridseached Naive Bayes model with an accuracy score of 86.15% I will choose this model as my final model. 

This is the confusion matrix for that model: 

![](./assets/naive_bayes_gs_cm.png)  

With this model we were able to achive a very good accuracy and a fairly low missclassification rate for how close these subreddits are to each other in terms of content and topics. Accuracy and missclassification rate are metrics that will be important to monitor in future advancements of this project.


<a name="c&r"></a>
## Conclusions & Recommendations 

Since we verified that even with very close topics we can achieve an accuracy score of 86.15% I believe that this is a high enough accuracy score to continue with future developments of this project.

Here are a list of benefits from adding this tool:

- Cleaner subreddits
- More accurate advertising
- Reduce the wordload for reddit moderators
- Easier posting for users
- Accumulating massive amounts of text data

Although we got a pretty decent accuracy scores for these two subreddits it is important to remember that this model was only trained on only these two subreddits. 

<a name="futuresteps"></a>
## Future Steps

For Reddit to be able to self classify the post as it is being written we will need a lot of data. In the future we plan to scrape Reddit and pull 2,000 posts from each subreddit. If we are able to pull approximately 2,000 posts from every single subreddit we will have a total of 2.4 billion posts. However, according to Reddit there are only 138,000 active subreddits so if we only pull 2,000 posts from those subreddits we will have in total 276 million posts to work with. This feature will be an amazing add-on to Reddit for two main reason. This first reason is that users will have less trouble in deciding where to post their content since our program can give them recommendations where their post should go. Second, implementing this program can make sure that post are going in the right subreddits which would mean that advertising becomes more accurate, which means that advertisers are getting a better return on their ad spend. 


<a name="cite"></a>
## Citations

Special thanks to David Lee, Eric Heidbreder, Haley Taft, and Chris Johnson on certain parts of this project.

- https://redditblog.com/2019/12/04/reddits-2019-year-in-review/
- https://foundationinc.co/lab/reddit-statistics/
- https://redditblog.com/2019/12/04/reddits-2019-year-in-review/
- https://towardsdatascience.com/multi-class-text-classification-with-lstm-1590bee1bd17
- https://www.tensorflow.org/guide/keras/train_and_evaluate
- https://keras.io/guides/sequential_model/
- 
