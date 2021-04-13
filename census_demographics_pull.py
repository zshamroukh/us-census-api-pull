#manipulate dataframes in python
import pandas as pd

#make API calls with python
import requests

#allows us to store results of API call cleanly
import json

#put your census API key here
api_key = "7369adb64373951f80f4f1816f9c54f808f59a40"

#construct the API call we will use
calledAPI = f"https://api.census.gov/data/2019/acs/acs5?get=B01003_001E,B03001_003E,B03002_012E,B03003_003E,B06011_001E,B01001_026E,B01001_002E&for=zip%20code%20tabulation%20area:*&in=state:51&key={api_key}"

#call the API and collect the response
response = requests.get(calledAPI)

#load the response into a JSON, ignoring the first element which is just field labels
formattedResponse = json.loads(response.text)[1:]

#store the response in a dataframe
VA_zip_demographics = pd.DataFrame(columns=['Total Pop', 'HISPANIC OR LATINO ORIGIN BY SPECIFIC ORIGIN', 'HISPANIC OR LATINO ORIGIN BY RACE', 'HISPANIC OR LATINO ORIGIN', 'MEDIAN INCOME IN THE PAST 12 MONTHS (IN 2019 INFLATION-ADJUSTED DOLLARS) BY PLACE OF BIRTH IN THE UNITED STATES', 'Total Female Pop', 'Total Male Pop', 'State', 'Zipcode'], data=formattedResponse)

#save that dataframe to a CSV spreadsheet
VA_zip_demographics.to_csv('VA_zip_demographics.csv', index=False)