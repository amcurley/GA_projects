---
title: Data Science Venn Diagram
type: exercise
creator:
    name: Alexander Combs
    city: NYC
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png)  Data Science Venn Diagram

Today we are going to have a team-based competition. The goal is to create the best performing model on a hold-out sample of data. Simple right?

Well, there is a catch.

This will be a constrained optimization. To understand what that means, let's take a look at the Project Management Venn Diagram, below.

![](https://berkonomics.com/wp-content/uploads/2015/11/goodfastcheap1-1.png)

The idea is that for any project you can have any two of these. You can have good work done cheap, but it will take a long time. You can have good work done fast, but it won't be cheap. Or you can have work done fast and on the cheap, but it won't be good.

Today we will apply this concept to data science.

You will be given a dataset and teams will be randomly assigned to one constraint: samples, features or algorithm.

---

### Team Sample Constraint
- Your choice of algorithm
- Your choice of features
- **Must use the cheap train sample**

### Team Features Constraint
- Your choice of algorithm
- **Limited to a maximum of 20 features**
- Your choice of samples

### Team Algorithm Constraint
- **Must use a Random Forest**
- Your choice of features
- Your choice of samples

## Deliverables
Your team will have until TBD (presentation time) to build the best model possible under those constraints.

- Modeling, predictions csv, and slide deck done by TBD (presentation time)
- Group presentations (_semi-technical audience_) with slide deck between TBD (presentation time)
- Repo with organized notebooks and README.md due by 9pm PST / midnight EST

# ![](https://media.giphy.com/media/aL4bDxt8fbpy8/giphy.gif)

 Descriptions of the data can be found [here](https://archive.ics.uci.edu/ml/datasets/adult). 
 
### Submission
---

The task is to predict if a person's income is in excess of $50,000 given certain profile information, and more specifically to generate the labels for income being **above** $50,000 for each row in the test set. This will simply be a csv with a single column of the predictions [0,1] **_with 'wage' as the column header_**. One member from each group will submit the link to your group's GitHub repository by TBD with the csv file complete, with final changes made by 12:00am EST / 9:00pm PST.

Good luck!
