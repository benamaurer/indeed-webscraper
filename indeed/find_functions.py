
#Importing packages...
import math
import json
import lxml
import datetime
import requests
from bs4 import BeautifulSoup

#Importing function from Beautiful Soup Tutorial

##page = requests.get('https://www.indeed.com/jobs?q=mergers%20acquisitions%20healthcare%20(mergers%20or%20acquisitions%20or%20diligence%20or%20investment%20or%20partnership%20or%20joint%20or%20venture%20or%20healthcare%20or%20JV%20or%20divestiture)%20-IQVIA%20-Aramco&l=California&radius=100&start=50&vjk=b4f69d685b6562ba')
##
##soup = BeautifulSoup(page.content, 'lxml')



#-------------------
def find_identifier(soup):
    ids = 0
    
    try:
        for div in soup.find_all(name='div',attrs={'class':'row'}):
            #Debug print
            #print(div['id'])
            return(div['id'])
            ids = ids + 1
    except:
        #Debug print
        #print('Not found')
        return('Not found')

    #print()
    #print(ids)
    #print('-----------------------------------------')
    

#-------------------
def find_company(soup):
    companies = 0
    result = ''
    try:
        for span in soup.find_all(name='span', attrs='company'):
            #Debug print
            #print(span.text.strip())
            result = (span.text.strip())
            companies = companies + 1
              
    except:
        #Debug print
        #print('Not found')
        result = 'Not found'
    
    finally:
        return result
##    print()
##    print(companies)
##    print('-----------------------------------------')


#-------------------
def find_location(soup):
    locations = 0
    result = ''
    try:
        for div in soup.find_all(name='div',attrs={'class':'location'}):
            #Debug print
            #print(div.text.strip())
            result = div.text.strip()
            locations = locations + 1
        for span in soup.find_all(name='span',attrs={'class':'location'}):
            #Debug print
            #print(span.text.strip())
            result = span.text.strip()
            locations = locations + 1
        
    except:
        #Debug print
        #print('Not found')
        result =  'Not found'

    finally:
        return result
##    print()
##    print(locations)
##    print('-----------------------------------------')


#-------------------
def find_title(soup):
    titles = 0
    result = ''
    try:
        for a in soup.find_all(name='a', attrs={'data-tn-element': 'jobTitle'}):
            #Debug print
            #print(a.text.strip())
            result = a.text.strip()
            titles = titles + 1
    except:
        #Debug print
        #print('Not found')
        result = 'Not found'

    finally:
        return result
##    print()
##    print(titles)
##    print('-----------------------------------------')


#-------------------
def find_description(soup):
    descriptions = 0
    result = ''
    try:
        for div in soup.find_all(name='div',attrs={'class':'summary'}):
            #Debug print
            #print(div.text.strip())
            result = span.text.strip()
            descriptions = descriptions + 1
    except:
        #Debug print
        #print('Not found')
        result = 'Not found'

    finally:
        return result
##    print()
##    print(descriptions)
##    print('-----------------------------------------')


#-------------------
def find_date(soup):
    dates = 0
    result = ''
    try:
        for span in soup.find_all(name='span',class_='date'):
            #Debug print
            #print(span.text.strip())
            result = span.text.strip()
            dates = dates + 1
    except:
        #Debug print
        #print('Not found')
        result = 'Not found'

    finally:
        return result
##    print()
##    print(dates)
##    print('-----------------------------------------')


#-------------------
def find_link(soup):
    links = 0
    result = ''
    try:
        for a in soup.find_all(name='a',attrs={'data-tn-element':'jobTitle'}):
            #Debug print
            #print(a['href'])
            result = (a['href'])
            links = links + 1
    except:
        #Debug print
        #print('Not found')
        result =  'Not found'

    finally:
        return result
##    print()
##    print(links)
##    print('-----------------------------------------')
##

#-------------------
##def find_fulltext
##    fulltext = 


#-------------------
def find_search_pages(starting_link):
    try:
        page = requests.get(starting_link)

        soup = BeautifulSoup(page.content, 'lxml')
        
        for div in soup.find_all(name='div',attrs={'id':'searchCountPages'}):
            word1, word2, word3, job_number, word5 = div.text.strip().split()
        #print(math.ceil(int(job_number)/10))
        #print(int(job_number)/10)
        pages = math.ceil(int(job_number)/10)
        #print(pages)
        
    except:
        pages = 0
    
    finally:
        return int(pages)


def is_imported():
    print('find_functions is imported')

##debug set
##print(find_identifier(soup))
##print(find_title(soup))
##print(find_company(soup))
##print(find_date(soup))
##print(find_description(soup))
##print(find_location(soup))
##print(find_link(soup))
##print(find_search_pages(soup))



