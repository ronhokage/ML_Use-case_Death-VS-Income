# ML_Use-case: Death-VS-Income
## <ins> Project Description </ins>
The project is about to determine whether death taken place due to respiratory illness is relevant to income and ozone levels in a specific county or not. To understand the same the dataset explored was the CDC data from 2010-2019. (Data folder attached).
There are 2 use cases that have been explored while analysing the dataset for a county, which were:-

1)- Impact of income and Ozone level in determining deaths due to respiratory illness.

2)- To determine the no of deaths in regard to population, cause of death and income level.

### <ins> Data Preprocessing, Feature Engineering and Selection </ins>
-In the Personal Income dataset, the two categories ‘population’ (persons) and ‘personal income’
(in thousands of dollars) were not necessary for this analysis because ‘per capita personal
income’ (‘personal income’ divided by ‘population’) contained this information.
-These were dropped from the dataset so that only per capita personal income (in dollars) remained. The data
was then averaged over 10 years (2010-2019) so that there was one average income level for
each county.

-In the Underlying Cause of Death dataset, several fields were dropped from the dataset as they
did not bring additional value to the analysis. These fields were 'Notes', 'Crude Rate', 'Year Code',
and 'County Code.’ ‘Deaths by cause’ were averaged by year (2010-2019) so that for each
county and each underlying cause of death, there was one average number of deaths.

-From the Air Quality Report, the only data used was data for ozone level (‘2nd max 1-hour’),
and all data for other pollutants were dropped. About twenty percent of the data was missing and
had to be filled.

-The data was sorted by state before forward filling so that missing data would
likely be filled with the mean ozone level from the same state.

-The feature ‘respiratory’ was added to the dataframe that took the value ‘yes’ if the cause of death 
was related to the respiratory system and ‘no’ if it was not. Some examples of the causes of death 
related to the respiratory system are 'Chronic obstructive pulmonary disease with acute lower 
respiratory infection,' 'Chronic respiratory failure,' 'Influenza with pneumonia, virus not
identified,' 'Asthma, unspecified,' 'Other disorders of lung,' 'Bronchiectasis,' and 'Bronchus or
lung, unspecified - Malignant neoplasms.'

-The most common cause of death was the one with the largest number of deaths by county.
Finally, all of the data were merged together into one DataFrame that included the following
features: county, per capita income, ozone level, cause of death (most common), and respiratory
(yes or no).

### <ins> Modelling </ins>
- The model was trained with variety of machine learning algorithms of which decision trees gave the best accuracy.
- Attached in the deployment folder is the image of the decision tree for this use case.
- The feature importance was also calculated. Ozone received a score of 0.27
and income received a score of 0.73 indicating the higher importance of income compared with
ozone in predicting the label.
- The hypothesis testing was performed, which concludes decision trees as the appropriate selection while modelling.

### <ins> Results </ins>

-The 10-fold cross validation of the random model had an average accuracy of 0.51 and the
decision tree model cross validation had an average accuracy of 0.70. 
The t-test score was found to be 3.8, with a resulting p-value of 0.001.

-Since 0.001 is much less than our significance threshold of 0.05, we reject the null hypothesis and accept the alternative, that the decision tree
model with income and ozone levels as features performs better than a random model at
predicting whether the most common cause of death in a county is respiratory related.

-There were 75 instances in which the model predicted true negatives (model predicted a label of ‘no’ correctly). In these
instances, respiratory disease was not the most common cause of the death and the model
predicted this correctly. There were 27 instances of false negatives (model predicted ‘no’
incorrectly), which means the model predicted that respiratory disease was not the most common
cause of death, but in reality it was (Type II Error).
There was 1 instance of false positive (model
predicted ‘yes’ incorrectly), which means the deaths were predicted to occur because of
respiratory disease, but in reality respiratory disease was not the most common cause (Type I
Error). There was also 1 instance of true positive (model predicted ‘yes’ correctly) which tells us
the deaths were predicted to occur due to respiratory diseases and that was the case in reality.
-From the confusion matrix for the logistic regression model, the results were
similar with this model, but there were no instances of false positives or true positives.

-From the confusion matrix, we can also compute the accuracy, specificity, and sensitivity of the
model. Accuracy comes out to be 73% for the same and is a measure of the ability of the model to predict class labels correctly.

-Specificity was 98.6%, which explains how well the model can predict cases in which respiratory related illnesses were not the most
common cause of death. This is also known as Recall. 

-Sensitivity comes to 50% for our model. This tells us how often the model predicts that
the most common cause of death was respiratory related correctly.This is also known as
Precision

