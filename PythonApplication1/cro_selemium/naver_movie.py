from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

driver = webdriver.Chrome('/chromedriver')
driver.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')

soup = BeautifulSoup(driver.page_source, 'html.parser')


# print(soup.prettify)

for i in [div.a.get_text() for div in soup.find_all('div', {'class' : 'tit3'})]:
    print(i)

driver.close()


