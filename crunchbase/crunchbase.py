from bs4 import BeautifulSoup
import requests
from pandas import *
import lxml

csv_data = read_csv('similar_company_search.csv')
csv_list = csv_data['company name'].tolist()
crunchbase_list = []
for name in csv_list:
    search = f'{name} crunchbase'
    url = 'https://www.google.com/search'
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82',
    }
    parameters = {'q': search}
    content = requests.get(url, headers=headers, params=parameters).text
    soup = BeautifulSoup(content, 'html.parser')
    search = soup.find(id='search')
    first_link = search.find('a')
    crunchbase_url = first_link['href']
    if 'https://www.crunchbase.com/' in crunchbase_url:
        crunchbase_list.append(f'{crunchbase_url}/org_similarity_overview')
        print(f'{crunchbase_url}/org_similarity_overview')
    else:
        pass

def get_similars(company,soup):
    print('fetching similar companies')
    similar_companies = []
    for possible_similar in soup.find_all(name='a',attrs={'class':'link-accent ng-star-inserted'}):
        not_including = ['/search/organizations/', company]
        if any(substring in str(possible_similar) for substring in not_including):
            pass
        else:
            company_name = str(possible_similar.get('href')).replace('/organization/','')
            if company_name not in similar_companies:
                similar_companies.append(company_name)
            else:
                pass
    return similar_companies

for url in crunchbase_list:
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82',
    }
    page_to_scrape = requests.get(url, headers=headers)
    soup = BeautifulSoup(page_to_scrape.content, 'lxml')
    company_searched = url.replace('https://www.crunchbase.com/organization/','').replace('/org_similarity_overview','')
    print(company_searched)
    print(url)
    print(soup)
    # print(get_similars(company_searched,soup))
