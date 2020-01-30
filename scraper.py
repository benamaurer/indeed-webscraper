#importing modules
import json
import requests
import lxml
from bs4 import BeautifulSoup
from find_functions import *

#placeholder to import parameters

with open('Parameters.json') as f:
       data = json.load(f)
       cities = data["cities_to_search"]
       job_keywords_1 = data["job_keywords_1"]
       job_keywords_2 = data["job_keywords_2"]
       range_mi = data["range_(mi)"]
       excluded_words = data["excluded_words"]

def print_cities():
       for x in range(len(cities)-1):
              print(cities[x], end = ', ')
       print('and ' + cities[-1] + ".")



##QUERY CHECK AND INPUT
#---------------------------------------------

print('-------------------------------------------------------')
print('Starting Indeed web scraper 1.0 --')
print('Created by Ben Maurer')
print('-------------------------------------------------------')
print()
print()
print('Current search parameters from JSON:')
print('-------------------------------------------------------')
print('Cities to search: \t', end='')
print_cities()
print('Job query set 1: \t' + job_keywords_1 + '.')
print('Job query set 2: \t' + job_keywords_2 + '.')
print('Search radius (mi): \t' + range_mi + '.')
print('Exclusion criteria: \t' + excluded_words + '.')
print('-------------------------------------------------------')
print()
print()
print('To start search press enter...')
input()




##MAIN SCRAPER FUNCTION
#--------------------------------------------------

    #Prints status message with number of cities to search and lists cities
print("Starting search in " + str(len(cities)) + " cities:")

#debug link
link = 'http://www.google.com'

    #fetches page data using requests and displays page load status
page = requests.get(link)
if str(page) == '<Response [200]>':
    print('Connected...')
else:
    print('Error: unable to reach page.')



##jobs - job_identifier()
##
##for job in jobs:
##
##        for city in cities:
##
##        
