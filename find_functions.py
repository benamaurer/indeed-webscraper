
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
def find_identifier():
    ids = 0
    try:
        for div in soup.find_all(name='div',attrs={'class':'row'}):
            #Debug print
            print(div['id'])
            #return a.text.strip()
            ids = ids + 1
    except:
        #Debug print
        print('Not found')
        #return 'Not found'
    print()
    print(ids)
    print('-----------------------------------------')
    

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
    print('-----------------------------------------')


#-------------------
def find_location():
    locations = 0
    try:
        for div in soup.find_all(name='div',attrs={'class':'location'}):
            #Debug print
            print(div.text.strip())
            #return div.text.strip()
            locations = locations + 1
        for span in soup.find_all(name='span',attrs={'class':'location'}):
            #Debug print
            print(span.text.strip())
            #return span.text.strip()
            locations = locations + 1
        
    except:
        #Debug print
        print('Not found')
        #return 'Not found'
    print()
    print(locations)
    print('-----------------------------------------')


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
    print('-----------------------------------------')


#-------------------
def find_description():
    descriptions = 0
    try:
        for div in soup.find_all(name='div',attrs={'class':'summary'}):
            #Debug print
            print(div.text.strip())
            #return span.text.strip()
            descriptions = descriptions + 1
    except:
        #Debug print
        print('Not found')
        #return 'Not found'
    print()
    print(descriptions)
    print('-----------------------------------------')


#-------------------
def find_date():
    dates = 0
    try:
        for span in soup.find_all(name='span',class_='date'):
            #Debug print
            print(span.text.strip())
            #return span.text.strip()
            dates = dates + 1
    except:
        #Debug print
        print('Not found')
        #return 'Not found'
    print()
    print(dates)
    print('-----------------------------------------')


#-------------------
def find_link():
    links = 0
    try:
        for a in soup.find_all(name='a',attrs={'data-tn-element':'jobTitle'}):
            #Debug print
            print(a['href'])
            #return a.text.strip()
            links = links + 1
    except:
        #Debug print
        print('Not found')
        #return 'Not found'
    print()
    print(links)
    print('-----------------------------------------')


#-------------------
##def find_fulltext
##    fulltext = 


##debug set
##find_identifier()
##find_title()
##find_company()
##find_date()
##find_description()
##find_location()
##find_link()
