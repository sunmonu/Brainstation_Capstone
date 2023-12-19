# Project Overview
This project aims to analyze demographic data across various counties over time to answer the question "Where should we open the next Target location?"

### The analysis involves:

1. Exploratory Data Analysis (EDA) to understand the distribution and trends within the Target and household debt data.
2. Logistic Regression to predict where Target's are currently located and understand coefficients
3. KMeans Clustering 

The final outcome of the project will be a set of models and visualizations that can aid in helping Target understand what counties provide the best ROI on their brick-and-mortar stores and predict what counties currently do not have Target stores but would be a great location based on demographic data.


### Data Dictionary for Household Debt Data

* Date -	The date when the data was recorded. Typically in a YYYY-MM-DD format.

* area_fips-	FIPS (Federal Information Processing Standards) code identifying counties or county-equivalent entities in the United States.
* low- Lower bound estimate of household debt in the area represented by area_fips.
* high - 	Float	Upper bound estimate of household debt in the area represented by area_fips.

### Data Dictionary for Target Data 

* Data Dictionary for target.csv
* Address.AddressLine1: The street address of the Target store.
* Address.City: The city in which the Target store is located.
* Address.County: The county in which the Target store is located.
* Address.Latitude: The geographical latitude coordinate of the Target store.
* Address.Longitude: The geographical longitude coordinate of the Target store.
* Address.PostalCode: The postal code or ZIP code for the Target store's location.
* Address.Subdivision: The state or province in which the Target store is located.
* LocationMilestones.LastRemodelDate: The date of the last remodeling of the Target store, if applicable.
* LocationMilestones.OpenDate: The date when the Target store was opened.
* Name: The name of the Target store.
* Store.StoreDistrictID: An identifier for the district in which the Target store is located.
* Store.StoreGroupID: An identifier for the group to which the Target store belongs.
* Store.StoreRegionID: An identifier for the region in which the Target store is located.
* SubTypeDescription: A description of the Target store subtype, if applicable.
* TypeCode: A code indicating the type of Target store.
* AllCapability: A descriptor of all capabilities that the store possesses.
* Remodeled: A flag indicating whether the store has been remodeled (True or False).


## Data Dictionary for Age by Population & Sex
- IBRC_Geo_ID: Full Fips Code
- Statefips
- Countyfips
- Description
- Year
- Total Population
- Population 0-4
- Population 5-17
- Population 18-24
- Population 25-44
- Population 45-64
- Population 65+
- Population Under 18
- Population 18-54
- Population 55+
- Male Population
- Female Population

## Data Dictionary for Race by County Data
- IBRC_Geo_ID: Full Fips code
- Statefips
- Countyfips
- Description
- Year
- Total Population
- White Alone
- Black Alone
- American Indian or Alaskan Native
- Asian Alone
- Hawaiian or Pacific Islander Alone
- Two or More Races
- Not Hispanic
- Hispanic

