
#Importing packages...
import json
import lxml
import datetime
import requests
from bs4 import BeautifulSoup

#Importing function from Beautiful Soup Tutorial

page = requests.get('https://www.indeed.com/jobs?q=mergers%20acquisitions%20healthcare%20(mergers%20or%20acquisitions%20or%20diligence%20or%20investment%20or%20partnership%20or%20joint%20or%20venture%20or%20healthcare%20or%20JV%20or%20divestiture)%20-IQVIA%20-Aramco&l=California&radius=100&start=50&vjk=b4f69d685b6562ba')

soup = BeautifulSoup(page.content, 'lxml')


#-------------------
def find_identifier
    ids = 0
    try:
        for div in soup.find_all(name='div', attrs='id'):
            #Debug print
            print(div.text.strip())
            #return a.text.strip()
            titles = titles + 1
    except:
        #Debug print
        print('Not found')
        #return 'Not found'
    print()
    print(titles)

#-------------------
def find_company():
    companies = 0
    try:
        for span in soup.find_all(name='span', attrs='company'):
            #Debug print
            print(span.text.strip())
            #return(a.text.strip())
            companies = companies + 1
              
    except:
        #Debug print
        #print('Not found')
        return 'Not found'
    print()
    print(companies)


#-------------------
##def find_location
##    location = 


#-------------------
def find_title():
    titles = 0
    try:
        for a in soup.find_all(name='a', attrs={'data-tn-element': 'jobTitle'}):
            #Debug print
            print(a.text.strip())
            #return a.text.strip()
            titles = titles + 1
    except:
        #Debug print
        print('Not found')
        #return 'Not found'
    print()
    print(titles)


#-------------------
##def find_description
##    description = 


#-------------------
##def find_date
##    date = 


#-------------------
##def find_link
##    link = 


#-------------------
##def find_fulltext
##    fulltext = 

find_title()
print('-----------------------------------------')
find_company()



