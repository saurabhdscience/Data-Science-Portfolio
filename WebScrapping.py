"""
Web Scraping - Beautiful Soup
"""
# importing required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# target URL to scrap

# # headers
headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
    }

cards_data_all = []
all_data = 0
rows = []
for x in range(200, 500):

	url = "https://www.99acres.com/property-in-delhi-ncr-ffid-page-{0}".format(x)

	# send request to download the data
	response = requests.request("GET", url, headers=headers)
	data = BeautifulSoup(response.text, 'html.parser')

	# find all the sections with specifiedd class name
	cards_data = data.find_all('div', attrs={'class', 'srpTuple__tupleDetails'})

	# cards_data_all.append(cards_data)
	# all_data = all_data+len(cards_data)
	# total number of cards
	# print('Total Number of Cards Found : ', )

	# extract the hotel name and price per room
	for card in cards_data:

	    # get the hotel name
	    # hotel_name = card.find('td', attrs={'id': 'srp_tuple_society_heading'})
	    location = card.find('a', attrs={'class': 'body_med srpTuple__propertyName'})
	    price = card.find('td', attrs={'id': 'srp_tuple_price'})
	    area = card.find('td', attrs={'id': 'srp_tuple_primary_area'})
	    bedrooms = card.find('td', attrs={'id': 'srp_tuple_bedroom'})
	    rows.append([
	    	location.text,
    		price.text,
    		area.text,
    		bedrooms.text])
	print(x)
df = pd.DataFrame(rows, columns=["location", "price", "area", "bedroom"])
print(df.head(10))
df.to_csv("99acres_2.csv", index=False)
