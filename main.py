from bs4 import BeautifulSoup as bs
import requests
import time
response = requests.get('https://books.toscrape.com/').text
time.sleep(2)
soup = bs(response,'lxml')
print(response)