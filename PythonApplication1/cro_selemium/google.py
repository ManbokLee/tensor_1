from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('/chromedriver')
driver.get('https://www.google.com')

# ID 로 태그 검색하기
# searchBar = driver.find_element_by_id("lst-ib")
searchBar = driver.find_element_by_css_selector("input[title='검색']")

# 데이터 값 삽입
searchBar.send_keys('스크랩핑 대상')

# form 을 전송한다.

searchBar.submit()

# 10초간 대기
sleep(10)

driver.close()