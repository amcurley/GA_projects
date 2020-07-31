# Project 1: Do Politics Play a Role in SAT and ACT Participation Rates?

### Overview

While analyzing the 2017, 2018, and 2019 data I came across what looks like a possible correlation between Politics and ACT and SAT participation rates. Republican states tend to have a higher ACT participation rate while Democrat states tend to have a higher SAT participation rate. Do Republican states have more state mandation? Are states providing the tests for free? These are some of the questions that sparked my interest. 

---

### Data Issues

Before I started analyzing the data there were multiple data issues I encountered. 

- All of the 'Participation' columns were objects instead of floats.
- Maryland in the 2017 SAT dataset the column 'math_sat' needed to be changed from 52 to 524.
- Maryland in the 2017 ACT dataset the column 'science_act' needed to be changed 2.3 from 23.2.
- Wyoming in the 2017 ACT dataset the column 'composite' needed to be changed 20.2x from 20.2.
- In the 2017 dataset there was an extra row that needed to be dropped.
- In the 2018 ACT dataset there was an extra Maine row that needed to be dropped.
- In the 2019 SAT dataset there were two extra rows that needed to be dropped they were 'Puerto Rico' and 'Virgin Islands'
- In the 2019 ACT dataset the last row needed to be dropped to match the 2019 SAT dataset
- In the final dataset Florida's participation rate in 2017 is 83% then in 2018 it is 56% then in 2019 it is 100%. However in a report from college board Florida, in 2018 had a 97% participation rate. 

After resolving these issues I merged all of the dataframes together making a final and complete overview of all of the given data.

### Primary Findings

After cleaning my data, I had a couple of primary findings that stood out to me.

- Colorado had a 70 % decrease in act participation rates from 2017 to 2018 and an 89% increase in SAT participation rates from 2017 to 2018. This is because Colorado instituted a state mandation for the SAT instead of the ACT. Requiring all students to take the sat.
- Illinois had a 90% increase in SAT participation rates from 2017 to 2018. This is because thet also instituted a state mandation for the SAT requiring all students to take the SAT test.
- Middle states and southern states are predominantly ACT focused meanwhile Eastern and Western states are predominantly SAT focused.
- There is an inverse relationship between participation rates and mean scores.

### Selection Bias

After cleaning my data, I had a couple of primary findings that stood out to me.

- Colorado had a 70 % decrease in act participation rates from 2017 to 2018 and an 89% increase in SAT participation rates from 2017 to 2018. This is because Colorado instituted a state mandation for the SAT instead of the ACT. Requiring all students to take the sat.
- Illinois had a 90% increase in SAT participation rates from 2017 to 2018. This is because thet also instituted a state mandation for the SAT requiring all students to take the SAT test.
- Middle states and southern states are predominantly ACT focused meanwhile Eastern and Western states are predominantly SAT focused.
- There is an inverse relationship between participation rates and mean scores.

![Screen Shot 2020-07-31 at 10.39.59 AM.png](/Users/aidancurley/Documents/dsir/Submissions/Projects/project-1-master/Assets/Screen Shot 2020-07-31 at 10.39.59 AM.png)





You can see the sources for the SAT data [here](https://blog.collegevine.com/here-are-the-average-sat-scores-by-state/) and [here](https://blog.prepscholar.com/average-sat-scores-by-state-most-recent), and the source for the ACT data [here](https://blog.prepscholar.com/act-scores-by-state-averages-highs-and-lows). **Make sure you cross-reference your data with your data sources to eliminate any data collection or data entry issues.**

#### Additional Data
(_This data is for your reference only. It is not needed to complete the project. You are required to include all of the above csv data._)

2018 and 2019 state-by-state average results and participation for the SAT are available in PDF reports [here](https://reports.collegeboard.org/sat-suite-program-results/state-results). 2018 ACT state-by-state mean composite scores and participation rates are [here](http://www.act.org/content/dam/act/unsecured/documents/cccr2018/Average-Scores-by-State.pdf) and 2019 data can be found [here](https://www.act.org/content/dam/act/secured/documents/cccr-2019/Average-Scores-by-State.pdf).

**This data has been compiled into CSV files which are also included in the *data* directory of this repo**

---

### Deliverables

All of your projects will comprise of a written technical report and a presentation. As we continue in the course, your technical report will grow in complexity, but for this initial project it will comprise:
- A Jupyter notebook that describes your data with visualizations & statistical analysis.
- A README markdown file the provides an introduction to and overview of your project.
- Your presentation slideshow rendered as a .pdf file.
**NOTE**: Your entire Github repository will be evaluated as your technical report. Make sure that your files and directories are named appropriately, that all necessary files are included, and that no unnecessary or incomplete files are included.

For your first presentation, you'll be presenting to a **non-technical** audience. You should prepare a slideshow with appropriately scaled visuals to complement a compelling narrative. **Presentation duration will differ by market, so check with your local instructor.**

---

### Technical Report Starter Code

Future projects will require you to decide on the entire structure of your technical report. Here, we provide you with [starter code](./code/starter-code.ipynb) in a Jupyter notebook that will help to guide your data exploration and analysis. **If you choose to edit the core structure of this notebook, make sure you don't exclude any of the requested operations**.

---

### Style Guide and Suggested Resources

[Tim Dwyer](https://www.linkedin.com/in/jtimdwyer/) (former DSI student and TA) put together [this style guide](https://git.generalassemb.ly/DSIR-720/style-guide). Some recommendations are geared toward future projects (which will include modeling and span multiple notebooks), but generally these are great recommendations.

Here's a link on [how to give a good lightning talk](https://www.semrush.com/blog/16-ways-to-prepare-for-a-lightning-talk/), which provides some good recommendations for short presentations.

[Here's a great summary](https://towardsdatascience.com/storytelling-with-data-a-data-visualization-guide-for-business-professionals-97d50512b407) of the main points of the book _Storytelling with Data_, which I can't recommend enough. [Here's a blog post](http://www.storytellingwithdata.com/blog/2017/8/9/my-guiding-principles) by the author about his guiding principles for visualizations.

---

### Submission

**Your slides must be ready for presentation by the beginning of class on July 31.**

**Materials must be submitted on Google Classroom by EOD (end of day) on July 31.**

Your technical report will be hosted on Github Enterprise. Make sure it includes:

- A README.md (that isn't this file)
- Jupyter notebook(s) with your analysis (renamed to describe your project)
- Data files
- Presentation slides
- Any other necessary files (images, etc.)

---

### Presentation Structure

- **Must be within 10 minutes. Aim for ~7 minutes to allow ~3 minutes for Q&A.**
- Use Google Slides or some other visual aid (Keynote, Powerpoint, etc).
- Consider the audience. Assume you are presenting to non-technical executives with the College Board (the organization that administers the SATs).
- Start with the **data science problem**.
- Use visuals that are appropriately scaled and interpretable.
- Talk about your procedure/methodology (high level, **CODE IS ALWAYS INAPPROPRIATE FOR A NON-TECHNICAL AUDIENCE**).
- Talk about your primary findings.
- Make sure you provide **clear recommendations** that follow logically from your analyses and narrative and answer your data science problem.

Be sure to rehearse and time your presentation before class.

---

### Rubric
Your instructors and IAs will evaluate your project (for the most part) using the following criteria.  You should make sure that you consider and/or follow most if not all of the considerations/recommendations outlined below **while** working through your project.

**Scores will be out of 21 points based on the 7 items in the rubric.** <br>
*3 points per section*<br>

| Score | Interpretation |
| --- | --- |
| **0** | *Project fails to meet the minimum requirements for this item.* |
| **1** | *Project meets the minimum requirements for this item, but falls significantly short of portfolio-ready expectations.* |
| **2** | *Project exceeds the minimum requirements for this item, but falls short of portfolio-ready expectations.* |
| **3** | *Project meets or exceeds portfolio-ready expectations; demonstrates a thorough understanding of every outlined consideration.* |

**Project Organization**
- Are modules imported correctly (using appropriate aliases)?
- Are data imported/saved using relative paths?
- Does the README provide a good executive summary of the project?
- Is markdown formatting used appropriately to structure notebooks?
- Are there an appropriate amount of comments to support the code?
- Are files & directories organized correctly?
- Are there unnecessary files included?
- Do files and directories have well-structured, appropriate, consistent names?

**Clarity of Message**
- Is the problem statement clearly presented?
- Does a strong narrative run through the project?
- Does the student provide appropriate context to connect individual steps back to the overall project?
- Is it clear how the final recommendations were reached?
- Are the conclusions/recommendations clearly stated?

**Python Syntax and Control Flow**
- Is care taken to write human readable code?
- Is the code syntactically correct (no runtime errors)?
- Does the code generate desired results (logically correct)?
- Does the code follows general best practices and style guidelines?
- Are Pandas functions used appropriately?
- Does the student demonstrate mastery masking in Pandas?
- Does the student demonstrate mastery sorting in Pandas?

**Data Cleaning and EDA**
- Does the student fix data entry issues?
- Are data appropriately labeled?
- Are data appropriately typed?
- Are datasets combined correctly?
- Are appropriate summary statistics provided?
- Are steps taken during data cleaning and EDA framed appropriately?

**Visualizations**
- Are the requested visualizations provided?
- Do plots accurately demonstrate valid relationships?
- Are plots labeled properly?
- Plots interpreted appropriately?
- Are plots formatted and scaled appropriately for inclusion in a notebook-based technical report?

**Research and Conceptual Understanding**
- Were useful insights gathered from outside sources?
- Are sources clearly identified?
- Does the student provide appropriate interpretation with regards to descriptive and inferential statistics?

**Presentation**
- Is the problem statement clearly presented?
- Does a strong narrative run through the presentation building toward a final conclusion?
- Are the conclusions/recommendations clearly stated?
- Is the level of technicality appropriate for the intended audience?
- Is the student substantially over or under time?
- Does the student appropriately pace their presentation?
- Does the student deliver their message with clarity and volume?
- Are appropriate visualizations generated for the intended audience?
- Are visualizations necessary and useful for supporting conclusions/explaining findings?

In order to pass the project, students must earn a minimum score of 1 for each category.
- Earning below a 1 in one or more of the above categories would result in a failing project.
- While a minimum of 1 in each category is the required threshold for graduation, students should aim to earn at least an average of 1.5 across each category. An average score below 1.5, while it may be passing, means students may want to solicit specific feedback in order to significantly improve the project before showcasing it as part of a portfolio or the job search.

### REMEMBER:

This is a learning environment and you are encouraged to try new things, even if they don't work out as well as you planned! While this rubric outlines what we look for in a _good_ project, it is up to you to go above and beyond to create a _great_ project. **Learn from your failures and you'll be prepared to succeed in the workforce**.
