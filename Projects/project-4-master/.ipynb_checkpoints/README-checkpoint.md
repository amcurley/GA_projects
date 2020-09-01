# Project 4 GA Think Tank

Group 7: David Lee, Chris Johnson, & Aidan Curley| US-DSIR-720 | 08.31.2020

## Problem Statement  

Do certain features have an impact on whether someone makes over $50,000 Per Year?


## Table of Contents

- [Project Directory](#projectdirectory)
- [Executive Summary](#executivesummary)
- [Data Cleaning & EDA](#data)
- [Modeling Process](#modellingprocess)
- [Conclusions](#c&r)
- [Future Steps](#futuresteps)
- [Citations](#cite)


<a name="projectdirectory"></a>
## Project Directory
    
```
project_3-master
|__ assets 
|   |__ cm_benchmark.png
|   |__ cm_continuous.png
|   |__ cm_tuned.png
|   |__ conclusion.png
|__ code       
|   |__ 01_get_data.ipynb  
|   |__ 02_baseline_score.ipynb  
|   |__ 03_title_only.ipynb  
|   |__ 04_title_selftext.ipynb
|   |__ 05_lstm_rnn.ipynb  
|__ data  
|   |__ cheap_train_sample.csv  
|   |__ large_train_sample.csv  
|   |__ test_data.csv  
|   |__ wage_submission.csv  cm
|__ Project4Presentation.pdf
|__ README.md  

```

<a name="executivesummary"></a>
## Executive Summary

We worked with a dataset which included over 30,000 individuals with various attributes such as age, education, native country, sex, etc. We used this dataset to develop a machine learning model to accurately predict whether an individual makes over 50,000. We also used this information to determine if certain features may impact the potential to earn more than 50,000.

Before moving onto the random forest model we had to establish the baseline accuracy score. Our baseline accuracy score was 76% accuracy score in predicting someone to make less than $50,000 per year. Our production model with tuned hyperparameters had an accuracy score of 85.6% which is a 9.6% increase from our baseline score.

After modeling we came to the conclusion that the native country and working class did not have an impact on if someone made over $50,000 per year or not.


<a name="data"></a>
## Data Cleaning/EDA

We worked with a dataset which included over 30,000 individuals with various demographic attributes. 

We first reviewed the descriptive statistics for the numeric values, such as the mean, max, min, and std deviation for age, education years, hours per week, and others. We created a loop which eliminated outliers whose values were greater than three standard deviations from the mean.  Although, in some rows there were '?' for certain features we came to the conclusion to leave those in since the data in the other columns was still relevant to our model. We also reviewed categorical columns such as education type, sex, relationship, and marital status. 

After we did get dummies on our categorical features we had to repeat this process for our text.csv and while doing that we noticed that 'native-country_Holand-Netherlands' was not in the test.csv so we had to drop this column.

<a name="modellingprocess"></a>
## Modeling Process  

The model that we chose was a Random forest model with different parameters. Random Forest models are strong and flexible models that are more robust than single decision trees. They limit over fitting by aggregating many decision trees.

Since our baseline accuracy score was 76% that is the accuracy score to beat.

### **Benchmark Model:**
A random forest model with all of the one hot encoding categorical features and the continuous features.
![](./assets/cm_benchmark.png)

### **Continuous Model:**  
A random forest model with only the continuous features.  
![](./assets/cm_continuous.png)

### **Tuned Model:**
For the tuned model we decided to remove the native countries and work class features due to scoring very low on a feature importance analysis.
![](./assets/cm_tuned.png)


<a name="c&r"></a>
## Conclusions

We came to the conclusion that native country and working class did not have an impact on predicting whether or not someone met our threshold of earning over 50k per year, because our models show that when we took out the native country and work class features our accuracy score improved by a very small margin. 

![](./assets/conclusion.png)

As seen above dropping these columns shows almost no difference on the accuracy of our model.


<a name="futuresteps"></a>
## Future Steps

- In future steps we plan to create different classification models such as logistic regression, k-nearest neighbors, support vector machines, and a neural network to hopefully achieve a higher accuracy score. 
- We would also like to collect more data and continue to feed that data into our different models.


<a name="cite"></a>
## Citations

Python Version: 3.7
- [Packages: pandas, numpy, matplotlib, sklearn]

- https://archive.ics.uci.edu/ml/datasets/adult  

