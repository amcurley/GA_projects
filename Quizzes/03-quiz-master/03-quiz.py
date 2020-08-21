#!/usr/bin/env python3

"""
Quiz 3

Task:
Your task for quiz 3 is to write a python script that:
- Imports the libraries you need
- Reads in the data: data/nba_rookies.csv
- Processes data:
    1. Set the 'Name' column as the index
    2. Converts the 'TARGET_5Yrs' column to 0/1 using 0 for 'No' and 1 for 'Yes'
- Models data using any classification algorithm you would like
    - If you do not know what to do here, feel free to fit a Logistic Regression model with default hyperparameters. But you are free to use any other model or methods that you know if you think that would be better!
    - Use a random state of 42 when splitting your data into training and testing
    - Use ALL columns (except your target) as your X matrix
- Generates predictions on your test data
- Creates a new DataFrame that has:
    1. One column called 'predictions' which is the predictions from your model on your test data
    2. An index that is the name of the player associated with the prediction from your test data
- Writes the DataFrame with the predictions to a csv called 'predictions.csv' in the data folder in this repository

Fill free to write this script in a Jupyter Notebook! Don't forget to add comments.
As a bonus, you can write it in this .py script:
This script should be able to be run in your terminal: python 03-quiz.py
Fill in this .py file with your solutions. Comments of the above instructions are included to guide your workflow.
"""

#################################
# Your Info
# Please fill out the following questions:

# Your name:
# Aidan Curley
# Your email:
# aidancurley1012@gmail.com
#################################

# Import the libraries you need
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
# Read in the data: data/nba_rookies.csv
# This shouldn't be the absolute path
data = pd.read_csv('./data/nba_rookies.csv')

# Process data:
data.head()
# 1. Set the 'Name' column as the index
# data.set_index('Name')
data.set_index('Name', inplace = True)
# 2. Convert the 'TARGET_5Yrs' column to 0/1 using 0 for 'No' and 1 for 'Yes'
data['TARGET_5Yrs'] = data['TARGET_5Yrs'].map({'No': 0, 'Yes': 1})

# Model data using any classification algorithm you would like
# If you do not know what to do here, feel free to fit a Logistic Regression model with default hyperparameters
# But you are free to use any other model or methods that you know if you think that would be better!
# Use a random state of 42 when splitting your data into training and testing
X = data.drop(columns='TARGET_5Yrs')
y = data['TARGET_5Yrs']

# Train, test, split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 42, stratify = y)

# Instantiate the model
lr = LogisticRegression('l1', solver='liblinear')  # Lasso performed slighlty better

# Fit the model
lr.fit(X_train, y_train)

# Get scores for my LogisticRegression
print(f"Simple LogisticRegression train score is {lr.score(X_train, y_train)}")
print(f"Simple LogisticRegression test score is {lr.score(X_test, y_test)}")

# Generate predictions on your test data
y_preds = lr.predict(X_test)

# Create a new DataFrame for predictions
pred_df = pd.DataFrame({'predictions': y_preds,})
# 2. Have one column called 'predictions'
# which is the predictions from your model on your test data

# 1. Have an index that is the name of the player
predictions_df = pred_df.set_index(X_test.index)

# Write the DataFrame you created to a csv called 'predictions.csv'
predictions_df.to_csv('./data/predictions.csv')
# in the data folder in this repository

#  KNN
X_train_2, X_test_2, y_train_2, y_test_2 = train_test_split(X, y, random_state = 42, stratify = y)

sc = StandardScaler()
Z_train = sc.fit_transform(X_train_2)
Z_test = sc.transform(X_test_2)

knn = KNeighborsClassifier()

knn.fit(Z_train, y_train)

print(f"Knn train score is {knn.score(Z_train, y_train)}")
print(f"Knn test score is {knn.score(Z_test, y_test)}")

# KNN performed worse than the simple LogisticRegression so we won't make predictions with it.
