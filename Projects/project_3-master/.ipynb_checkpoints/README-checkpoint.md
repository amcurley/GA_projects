# Self Classifiying Reddit Posts

Aidan Curley | US-DSIR-720 | 08.28.2020

## Problem Statement  

According to Reddit you can, “reach passionate and diverse communities organized around thousands of different topics, ” through advertising. Reddit had 199 million posts in 2019 alone according to their blog and approximately 138,000 active subreddits among their total 1.2 million subreddits. With so much information, how do they make sure people are posting in the right subreddits? Well they don't. So, how can we ensure the posts are going into the proper subreddit’s? Through machine learning! 

## Table of Contents

- [Project Directory](#projectdirectory)
- [Executive Summary](#executivesummary)
- [The Dataset](#dataset)
- [Feature Selection](#featureselection)
- [Modelling Process](#modellingprocess)
- [Future Steps](#futuresteps)
- [Conclusions & Recommendations](#c&r)
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

Our best score was ___ which is awesome! With this accuracy score we are confident in moving forward with this project and moving on to the next steps. The next steps consist of creating this same process but for every subreddit on Reddit. For Reddit to be able to self classify the post as it is being written we will need a lot of data. In the future we plan to scrape Reddit and pull 2,000 posts from each subreddit. If we are able to pull 2,000 posts from every single subreddit we will have a total of 2.4 billion posts. However, according to Reddit there are only 138,000 active subreddits so if we only pull 2,000 posts from those subreddits we will have in total 276,000,000 posts to work with.



<a name="dataset"></a>
## The Dataset 

The dataset I am using from this project consists of a total of 31,299 posts from each subreddit which is 62,598 posts in total. From these posts I only used the 'title'(the title of the post) and the 'selftext'(the content within the post) columns. I used the [pushshift api](https://github.com/pushshift/api) to scrape this data from reddit. 


<a name="modellingprocess"></a>
## Modeling Process  

After cleaning our data we now move onto the modeling process. The modeling process has multiple steps

The modelling process had multiple steps.  

In a natural language processing classification task there are a few steps we have to take before modeling. 

I pulled in 31,299 posts from each subreddit as a start. After I had all of my data I had to convert the data into 



<a name="futuresteps"></a>
## Future Steps

As we move forward looking for potential investment properties this model will have to improve. Although it is satisfactory for getting an estimation on what we could buy/sell the house for it will need to improve. Especially with residential properties being under or over \$30,000 is not the best. However, if we see a potential property that catches our eye this model can be extremely helpful. We can run the properties features through our model and evaluate what needs to get fixed. Such as improving the overall quality of house from a 4 to a 10 will increase our potential sale price. 

In the future we plan to tweak and add to this model as we expand to new markets. Performing this model on different markets will show us what else we need to add that we did not have in version 1.0. Possibly using a different machine learning model will produce a better RMSE than just a linear regression model. We will continuously tweak and edit the code to make this model predict better and be more reproducible to future datasets.

Once we get a satisfactory replicable model we hope to add a section to our website that will make the process of predicting easier. This section on our website will have places to input the features we use to predict the sale price so we don't have to manually enter them into a csv file and run all of the notebooks again. This will be able to give you a prediction instantly. This feature will only be accessible by our team of investors.

<a name="c&r"></a>
## Conclusions & Recommendations 

First of all this is not a model that should be used to predict and then simply buy the property based on this estimation, since there are many aspects of a house that cannot be accounted for by a model. 

Depending on your specifc investment strategies these are some things to take into consideration before purchasing an investment property:

- School District
- Neighbors
- Economic Climate
- Supply and Demand 
- Interest Rates
- Area Demographics

Use this model as a ballpark number in mind and then go research that specific property in more detail. If your strategy is a fix and flip you might search for properties with quality features less than 5 and focus on improving them to 8+. You can then predict if I raise this house's quality features how much does that raise the sale price of a house. If the numbers make sense then go research the property in more detail. If your strategy is to find tenants you might want to focus on different qualities that aren't in this model such as paint colors, quality of furniture, ease of access to public transportation, etc. 

As I tweak and add to this model I hope to make it more accurate and replicable to different markets. 

<a name="cite"></a>
## Citations

Special thanks to David Lee, Eric Heidbreder, Haley Taft, and Chris Johnson on certain parts of this project.

- https://redditblog.com/2019/12/04/reddits-2019-year-in-review/
