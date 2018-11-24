
from bs4 import BeautifulSoup
import re


def readFile():
    file = open('C:/consumer_reports.txt', 'rt', encoding='UTF-8')
    data = file.read()
    file.close()
    return data


soup = BeautifulSoup(readFile(), 'lxml')
all_div = soup.find_all('div', attrs=({'class':'entry-letter'}))

products = [div.div.a.span.string for div in all_div]

for product in products:
    print(product)










