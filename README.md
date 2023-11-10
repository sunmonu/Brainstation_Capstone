# Project Overview
This project aims to analyze household debt data across various counties over time, focusing on identifying trends and correlations between household debt levels and the opening and remodeling dates of Target stores.

##The analysis involves:

1. Exploratory Data Analysis (EDA) to understand the distribution and trends within the Target and household debt data.
2. Time Series Analysis using SARIMAX to model and forecast household debt levels.

The final outcome of the project will be a set of models and visualizations that can aid in understanding the impact, if any, of Target store events on local household debt levels.


##Data Dictionary for Household Debt Data

-Date -	The date when the data was recorded. Typically in a YYYY-MM-DD format.

-area_fips-	FIPS (Federal Information Processing Standards) code identifying counties or county-equivalent entities in the United States.

-low- Lower bound estimate of household debt in the area represented by area_fips.

-high - 	Float	Upper bound estimate of household debt in the area represented by area_fips.






### Requirements
-Python 3.8+
-pandas
-matplotlib
-statsmodels
See requirements.txt for more details.
