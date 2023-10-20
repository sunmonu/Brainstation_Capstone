In this project, we aim to uncover insights into the relationship between household debt to income ratio and the strategic decisions of store openings by Target. While we don't have access to the performance data of existing stores, we can use economic information to identify regions with high potential for new store success. By analyzing household debt characteristics, we can recommend prime locations for Target's expansion.

Our key question is: How can household debt, specifically the household debt-to-income ratio, inform Target's strategic decisions when opening new stores?

We will be using two datasets for this project:

targets.csv - This dataset includes a record for Target locations currently in operation as of April 2017
debt_county.csv - This dataset includes a record of the household debt to income ration since 1999


Features - target.csv 

'Address.AddressLine1',
'Address.City', 
'Address.County',
'Address.Latitude', 
'Address.Longitude', 
'Address.PostalCode',
'Address.Subdivision', 
'LocationMilestones.LastRemodelDate',
'LocationMilestones.OpenDate',
'Name', 
'Store.StoreDistrictID',
'Store.StoreGroupID', 
'Store.StoreRegionID', 
'SubTypeDescription',
'TypeCode',
'AllCapability', 
'Remodeled'


Features- debt_county.csv
Label		Description
year		Yearly observation date.
qtr 		Quarterly observation date, end of period.
area_fips 	Combination of 2-digit U.S. state Federal Information Processing Standard(FIPS) code preceding 3-digit U.S. county FIPS code.
low		Lower bound of Debt-to-Income ratio category.
high		Upper bound of Debt-to-Income ratio category.