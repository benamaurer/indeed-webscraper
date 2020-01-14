#importing modules
import json
import requests
import lxml
from bs4 import BeautifulSoup

#placeholder to import parameters

with open('Parameters.json') as f:
       data = json.load(f)
       cities = data["cities_to_search"]
       job_keywords_1 = data["job_keywords_1"]
       job_keywords_2 = data["job_keywords_2"]
       range_mi = data["range_(mi)"]
       excluded_words = data["excluded_words"]

    #parameteres, keywords, range, locations, 
#cities = ['Chicago','Atlanta','Boston','Charlotte']


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

#Beautiful Soup Parsing
soup = BeautifulSoup(page.content, 'lxml')
print(soup.prettify())
