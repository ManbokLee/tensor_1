from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('/chromedriver')
driver.implicitly_wait(3) # Lazy Loading

driver.get('https://nid.naver.com/nidlogin.login')
driver.find_element_by_name('id').send_keys('')
driver.find_element_by_name('pw').send_keys('')
driver.implicitly_wait(3) # Lazy Loading

driver.find_element_by_xpath("//*[@id='frmNIDLogin']/fieldset/input").click()
driver.implicitly_wait(3) # Lazy Loading


driver.get('https://order.pay.naver.com/home')
html = driver.page_source

soup = BeautifulSoup(html, 'lxml')

notice = soup.select('div.p_inr > div.p_info > a > span')

for i in notice:
    print(i.text.strip())

# driver.close()