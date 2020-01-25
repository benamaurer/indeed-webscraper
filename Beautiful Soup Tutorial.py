#import packages
import json
import requests
import lxml
import datetime
from bs4 import BeautifulSoup

#placeholder to import parameters

#import parameters from json file
with open('Parameters.json') as f:
    data = json.load(f)
    cities = data["cities_to_search"]
    job_keywords_1 = ["job_keywords_1"]
    job_keywords_2 = ["job_keywords_2"]
    range_mi = ["range_(mi)"]
    excluded_words = ["excluded_words"]

print(cities + job_keywords_1 + jobs_keywords_2 + range_mi + excluded_words)


    #Prints status message with number of cities to search and lists cities
print("Starting search in " + str(len(cities)) + " cities:")
for x in range(len(cities)-1):
       print(cities[x], end = ', ')
print('and ' + cities[-1] + ".")


    #placeholder to build link based on parameters
#link = "http://google.com"

    #DEBUG LINK
link = 'http://dataquestio.github.io/web-scraping-pages/simple.html'


    #fetches page data using requests and displays page load status
page = requests.get(link)
if str(page) == '<Response [200]>':
    print('Connected...')
else:
    print('Error: unable to reach page.')

#cities for loop
#for city in cities:

    #job keywords for loop
    #for jobs in job_keywords

    

#Beautiful Soup Parsing
soup = BeautifulSoup(page.content, 'lxml')
print(soup.prettify())
