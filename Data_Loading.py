import requests
import pandas as pd

# Base url for Chicago Open Data Portal crime API; plus addin of date and location filters
baseurl = "https://data.cityofchicago.org/resource/w98m-zvie.json"

# syntax for below filter is  'within_box(location_col, NW_lat, NW_long, SE_lat, SE_long)'

datebetw = "?$where=date between '2019-01-01T12:00:00' and '2019-07-16T14:00:00'"
boxurl = 'within_box(location,latitude, longitude, latitude, longitude)'
#boxurl = 'within_box(location, 41.808000, -88.111000, 41.881644, -87.632095)'

# Create the overall URL to interogate API with our data and location filters
ourl = baseurl + datebetw + ' AND ' + boxurl

text = requests.get(ourl).json()

# create pandas dataframe dictionary container object
global df
df = pd.DataFrame(
    text, columns=['date', 'primary_type', 'description', 'arrest', 'domestic'])
