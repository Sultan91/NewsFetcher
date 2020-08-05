import requests
from bs4 import BeautifulSoup
import datetime


def retrieve_news():
    page = requests.get('https://news.ycombinator.com/')
    titles = []
    urls = []
    soup = BeautifulSoup(page.content, 'html.parser')

    for row in soup.find("table", id='hnmain').findAll('tr', {'class': 'athing'}):
        title = row.find('a', attrs={'class': 'storylink'})
        url = title['href']
        if title.text:
            titles.append(title.text)
            if 'item?id' in url:
                url = 'https://news.ycombinator.com/'+url
            urls.append(url)
    return [titles, urls]





