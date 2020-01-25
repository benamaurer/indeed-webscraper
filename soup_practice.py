#Importing packages...
import json
import lxml
import datetime
import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.indeed.com/jobs?q=mergers%20acquisitions%20healthcare%20(mergers%20or%20acquisitions%20or%20diligence%20or%20investment%20or%20partnership%20or%20joint%20or%20venture%20or%20healthcare%20or%20JV%20or%20divestiture)%20-IQVIA%20-Aramco&l=California&radius=100&start=50&vjk=b4f69d685b6562ba')

soup = BeautifulSoup(page.content, 'lxml')

def test():
    try:
        for a in soup.find_all(name='a', attrs={'data-tn-element': 'jobTitle'}):
            print(a.text.strip())
            #return a.text.strip()

    except:
        return 'Not found'

##for all in test():
##    print(test())

test()
