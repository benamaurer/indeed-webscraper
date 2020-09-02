#Importing packages...
import math
import json
import lxml
import datetime
import requests
from bs4 import BeautifulSoup

#Importing function from Beautiful Soup Tutorial

page = requests.get('https://www.indeed.com/jobs?q=mergers%20acquisitions%20healthcare%20(mergers%20or%20acquisitions%20or%20diligence%20or%20investment%20or%20partnership%20or%20joint%20or%20venture%20or%20healthcare%20or%20JV%20or%20divestiture)%20-IQVIA%20-Aramco&l=California&radius=100&start=50&vjk=b4f69d685b6562ba')

soup = BeautifulSoup(page.content, 'lxml')

print('pre-function print')

#-------------------
def find_description(soup):
##    descriptions = 0
##    result = ''
    try:
        for div in soup.find_all(name='div',attrs={'id':'vjs-desc'}):
            description = 
            #Debug print
            print(div.text.strip())
            #result = span.text.strip()
            #descriptions = descriptions + 1
    except:
        #Debug print
        print('Not found')
        #result = 'Not found'

##    finally:
##        return result
##    print()
##    print(descriptions)
##    print('-----------------------------------------')
