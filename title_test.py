#Importing packages...
import json
import lxml
import datetime
import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.indeed.com/jobs?q=mergers%20acquisitions%20healthcare%20(mergers%20or%20acquisitions%20or%20diligence%20or%20investment%20or%20partnership%20or%20joint%20or%20venture%20or%20healthcare%20or%20JV%20or%20divestiture)%20-IQVIA%20-Aramco&l=California&radius=100&start=50&vjk=b4f69d685b6562ba')

soup = BeautifulSoup(page.content, 'lxml')

def find_identifier():
    ids = 0
    try:
        for div in soup.find_all(name='id'
                                 ):
            #Debug print
            print(div.text.strip())
            #return a.text.strip()
            ids = ids + 1
    except:
        #Debug print
        print('Not found')
        #return 'Not found'
    print()
    print(ids)

find_identifier()

