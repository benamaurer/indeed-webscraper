#IMPORTING MODULES
#---------------------------------------------
import json
import os
import datetime
import time
import math
import pandas as pd
import requests
import lxml
from bs4 import BeautifulSoup

#DEFINING FUNCTIONS

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


##LOADING PARAMETERS FROM JSON
#---------------------------------------------
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
print('Starting Indeed web scraper --')
print('Created by Ben Maurer')
print('-------------------------------------------------------')
print()
print()
print('Current search parameters from JSON:')
print('-------------------------------------------------------')
print('Locations to search: \t', end='')
print_cities()
print('Job query set 1: \t' + job_keywords_1 + '.')
print('Job query set 2: \t' + job_keywords_2 + '.')
print('Search radius (mi): \t' + range_mi + '.')
print('Exclusion criteria: \t' + excluded_words + '.')
print('-------------------------------------------------------')
print()
print()
#print('To start search press enter...')
#input()




##MAIN SCRAPER FUNCTION
#--------------------------------------------------


#Prints status message with number of cities to search and lists cities
print("Starting search in " + str(len(cities)) + " cities:")


#debug link
#link = 'http://www.google.com'
#link = ('http://www.indeed.com/jobs?as_and=' + job_keywords_1 + '&radius=100' + '&l=' + str(city) + '&start=' + '&start=' + str(page))


#setting up dataframe in pandas
df = pd.DataFrame(columns = ['pid', 'Company', 'Location', 'Job Title', 'Days ago posted', 'Date Added', 'Link', 'Description', 'Rank'])


#debug to check if functions are imported
#is_imported()


#checking for internet connection
test_connection = requests.get('http://indeed.com')
if str(test_connection) == '<Response [200]>':
       print('Connected...')
       print()
       print()
       print('-------------------------------------------------------')
       
else:
       print('Unable to connect to page, exiting.')
       exit


#beginning counts for info readout
city_complete = 0
total_count = 0
city_results = 0

#begin search loop: -> city -> pages
for city in cities:

       #debug print
       #print(city)
       starting_link = ('http://www.indeed.com/jobs?as_and=' + job_keywords_1 + '&as_not=' + excluded_words + '&l=' + str(city) + '&radius=' + range_mi + '&start=' + '&start=1')
       total_pages = find_search_pages(starting_link)
       

       #debug pring
       #print(pages)
       
       #updating counts
       city_complete = city_complete + 1
       city_results = 0

       #looping for each page
       for page_number in range(0, total_pages):

              #building link and requesting
              link = ('http://www.indeed.com/jobs?as_and=' + str(job_keywords_1) + '&as_not=' + excluded_words + '&l=' + str(city) + '&radius=' + range_mi + '&start=' + str(page_number*10))
              page = requests.get(link)
              #print(link)


              #waiting 1 second between pages
              time.sleep(1)
              

              full_soup = BeautifulSoup(page.content, 'lxml')

              #list of pids from each page
              listings = []

              #appending pids to list in for loop
              for div in full_soup.find_all(name='div',attrs={'class':'row'}):
                     #Debug print
                     #print(div['id'])
                     listings.append(div['id'])

              #print(listings)
                     
              #ensuring non-blank results
              if(len(listings) == 0):
                     break

              #loop to search listings using pid
              for listing in listings:

                     soup = full_soup.find(name='div', attrs={'id':listing})

                     #print(soup)
                     #print(listing)

                     #RANK BLOCK
                     #-----------------------------------
                     rank = 0
                     rank_string = str(find_title(soup))
                     if ('Developer' or 'developer' or 'Development' or 'development') in rank_string:
                            rank = rank + 1
                     if ('Business') in rank_string:
                            rank = rank + 1
                     if ('Mergers' or 'Merger' or 'mergers') in rank_string:
                            rank = rank + 1
                     if ('Acquisitions' or 'Acquisition') in rank_string:
                            rank = rank + 1
                            
                     
                     #updating counts
                     total_count = total_count + 1
                     city_results = city_results + 1
            
                     #numbering to increment row in df
                     num = (len(df) + 1)
                     
                     #list of data appended for each pid
                     job_data = []

                     #returning results from find_functions
                     job_data.append(listing)
                     job_data.append(find_company(soup))
                     job_data.append(find_location(soup))
                     job_data.append(find_title(soup))
                     job_data.append(find_date(soup))
                     job_data.append(datetime.date.today())
                     job_data.append(find_link(soup))
                     job_data.append(find_description(soup))
                     job_data.append(rank)

                     df.loc[num] = job_data

       #removing duplicate results
       #df.drop_duplicates(subset = 'pid', inplace = True)             
       #city_results = (len(df.index) - city_results)
                     
       print('{:<20s}{:>4s}{:>20s}{:>17s}'.format(city, '(' + str(city_complete) + '/' + str(len(cities)) + ')','completed, with',str(city_results) + ' results.'))

       

#counting total results
result_count = len(df.index)
print(result_count)


#removing duplicates
df.drop_duplicates(subset = 'pid', inplace = True)

#counting total results
result_count = len(df.index)

#change directory to results file
os.chdir(str(os.getcwd()) + '/Search_results')

#saving to csv
df.to_csv('Search_' + str(time.strftime('%Y-%m-%d_%H.%M')) + '.csv', encoding='utf-8-sig')
#print('csv created')


##FINISH STATUS MESSAGE
#--------------------------------------------------
print()
print('-------------------------------------------------------')
print('Search of ' + str(len(cities)) + ' locations completed with ' + str(result_count) + ' results. (duplicates removed)')
print('-------------------------------------------------------')
                     
exit()
                     

