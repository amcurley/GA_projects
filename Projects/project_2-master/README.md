# Regression Model to Predict Sale Price of a Home

Aidan Curley | US-DSIR-720 | 08.14.2020

## Problem Statement  

Being the lead data scientist at GA & Associates Realty I was given the task of creating a model that will shorten our timeframe for evaluating a potential real estate investment property. This model should inform us on the features that have an effect on price when we go to buy the house and when we go to sell the house. Our model should be able to predict the price within \$30,000 since this will give us room to negotiate, renovate, and eventually resell the property. 

I will use the Ames Iowa housing dataset to build a baseline regression model to predict the sale price of a house in order to evaluate if that property is a potential real estate investment.

## Table of Contents

Project Directory  
Executive Summary  


## Project Directory
    
```
project_2-master   
|__ code       
|   |__ 01_continous_cleaning.ipynb  
|   |__ 02_discrete_cleaning.ipynb  
|   |__ 03_ordinal_cleaning.ipynb  
|   |__ 04_nominal_cleaning.ipynb  
|   |__ 05_function_cleaning.ipynb  
|   |__ 06_model_submission.ipynb 
|__ data  
|   |__ continous_test.csv  
|   |__ continous_train.csv  
|   |__ discrete_test.csv  
|   |__ discrete_train.csv  
|   |__ merged_test.csv  
|   |__ merged_train.csv  
|   |__ new_submission.csv  
|   |__ ordinal_test.csv  
|   |__ ordinal_train.csv  
|   |__ ridge_submission.csv   
|   |__ test.csv  
|   |__ train.csv  
|__ capstone_presentation.pdf  
|__ README.md  
```

## Executive Summary

I was given a dataset of Ames Iowa houses with a total of 80 columns for features of the houses and one column for the sale price. There were four different types of data: nominal, ordinal, continous, and discrete. I went through all of the 80 columns and picked the columns in those four categories that can best be replicated for future data. There were features in this dataset that could have been used to better predict the sale price for this specifc city however would not have been translated nicely if later down the line we wanted to input data from different cities across the United States.   

With these specific features that I chose for the regression model I hope that this model can be replicated and used as a tool to evaluate a real estate invesment deal. When new deals come across the table we can run them through this model and see if the price for that house seems satisfactory for an investment or not. When we are looking to sell a property we can also run that property though this model and predict what we can potentially get from the house.

## Feature Selection

I wanted to focus on features that most real estate agents can easily find out for us. This was important so we can evaluate deals as quickly and as easily as possible. After selecting a handful of features I decided to check the correlation between these features and the 'SalePrice' column that was provided in the training csv file. After finding out which features had the most correlation with the 'SalePrice' columns and were easy features that a real estate agent can get for us I had to clean those features.

**The features I selected were:**
- Total Basement Square Feet (Total Bsmt SF)
- First Floor Square Feet (1st Flr SF)
- Above Grade (Ground) Living Area Square Feet (Gr Liv Area)
- Garage Area (Garage Area)
- Neighborhood (Neighborhood)
- Overall Quality (Overall Qual) (The real estate agent will give their best guess)   
- Exterior Quality (Exter Qual) (The real estate agent will give their best guess)  
- Basement Quality (Bsmt Qual) (The real estate agent will give their best guess)  
- Kitchen Quality (Kitchen Qual) (The real estate agent will give their best guess)
- Year Built (Year Built)  
- Full Bath (Full Bath)  
- Total Rooms Above Ground (TotRms AbvGrd)  

These features will allow us to deploy models very quickly and allow us to replicate on future markets. This was very important to selecting these features. After picking these features I also wanted to add the relationship between some of these features to our feature list as well. I wanted to emphasize houses that had a relationship with Gr Liv Area & Total Bsmt SF, Overall Qual & Exter Qual, Overall Qual & Gr Liv Area, and Gr Liv Area & Garage Area. Although these features could have added multicollinearity they are important relationships that I believe could impact the overall sale price of home.  


![](/Users/aidancurley/Documents/dsir/Submissions/Projects/project_2-master/assets/neighborhoodboxplot.png)


## Modelling Process  

The modelling process had multiple steps.      

The first step in my modelling process was finding out my baseline score with my cleaned dataset with my selected features. With my model the RMSE (Root Mean Square Error) to beat was 80039.93 for the training dataset and 77354.33 for the testing dataset. 


After evaluating the baseline score I then moved onto predicting the best score I could with my chosen features. I instantiated a new linear regression model and passed my features into this models train test split. This model performed expontentially better than the baseline model. The training RMSE was 28091.21 and the testing RMSE was 28408.52. 

After I did this model I instantiated another model however this was with using standard scaler and ridge regression. I wanted to see if scaling my features and doing ridge regression would improve my scores. This time I used R2 to score this model. The R2 for this model was .87 on train in train test split and .87 on test in train test split. Comparing this to my model without scaled features for my R2 I got .88 on the train in train test split and .86 on the test in train test split. I did the same process with lasso regression and I achieved about the same R2 scores, I got .88 on the train in train test split and .87 on the test in train test split.



- **Must be within time limit established by instructors.**
- Use Google Slides or some other visual aid (Keynote, Powerpoint, etc).
- Consider the audience.
- Start with the **data science problem**.
- Use visuals that are appropriately scaled and interpretable.
- Talk about your procedure/methodology (high level).
- Talk about your primary findings.
- Make sure you provide **clear recommendations** that follow logically from your analyses and narrative and answer your data science problem.

Be sure to rehearse and time your presentation before class.

---


