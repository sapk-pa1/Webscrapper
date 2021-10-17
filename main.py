from bs4 import BeautifulSoup
import requests
import random
headers ={'user_agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) \
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'}
url = 'https://news.ycombinator.com/'
response = requests.get(url, headers)
# sending the user agent string as the header to spoof the website to thinking it is the browser 
# print(response.content)
soup = BeautifulSoup(response.content, 'lxml')
news= []
news_link = []
for items in soup.find_all('tr'):
    if items.select('.storylink'):
        news.append(items.select('.storylink')[0].get_text())
        news_link.append(items.select('.storylink')[0]['href'])
#create a random integere
rand_int = random.randint(1, len(news))
print(news[rand_int])
print('Link: '+ news_link[rand_int])

