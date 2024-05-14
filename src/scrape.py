import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.nba.com/players'

driver = webdriver.Safari()
driver.get(url)

time.sleep(3) 

next_button_class = 'Pagination_button__sqGoH'
driver.find_element(By.XPATH, "//button[@title='Next Page Button']").click()
time.sleep(3)

html_content = driver.page_source
soup = BeautifulSoup(html_content, 'html.parser')

data = []

table = soup.find('table', class_='players-list')
table_body = table.find('tbody')
rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])
    
print(data)

driver.quit()
