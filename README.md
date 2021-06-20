# ML_Use-case: Death-VS-Income
## <ins> Project Description </ins>
The project is about to determine whether death taken place due to respiratory illness is relevant to income and ozone levels in a specific county or not. To understand the same the dataset explored was the CDC data from 2010-2019. (Data folder attached).
There are 2 use cases that have been explored while analysing the dataset for a county, which were:-

1)- Impact of income and Ozone level in determining deaths due to respiratory illness.

2)- To determine the no of deaths in regard to population, cause of death and income level.

## Data Preprocessing, Feature Engineering and Selection
-In the Personal Income dataset, the two categories ‘population’ (persons) and ‘personal income’
(in thousands of dollars) were not necessary for this analysis because ‘per capita personal
income’ (‘personal income’ divided by ‘population’) contained this information. 
-These were dropped from the dataset so that only per capita personal income (in dollars) remained. The data
was then averaged over 10 years (2010-2019) so that there was one average income level for
each county.
-In the Underlying Cause of Death dataset, several fields were dropped from the dataset as they
did not bring additional value to the analysis. These fields were 'Notes', 'Crude Rate', 'Year Code',
7and 'County Code.’ ‘Deaths by cause’ were averaged by year (2010-2019) so that for each
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


